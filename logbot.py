"""
Discord Log Botu - discord.py

Kanal ID'lerini kod iine yazmak gerekmez!
Tm ayarlar Discord komutlaryla yaplr ve
settings.json dosyasna otomatik kaydedilir.

Gereksinimler:
    pip install discord.py

Komutlar (Slash komutlar):
    /log-kur <tr> <kanal>      Belirli bir log tr iin kanal atar
    /log-kaldr <tr>           Belirli bir log trn devre d brakr
    /log-durum                  Tm log kanallarn listeler
    /log-sifirla                Tm ayarlar siler
"""

import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import asyncio
import html
import io
import json
import os
import secrets
import socket
import urllib.error
import urllib.request
from flask import Flask
from PIL import Image, ImageDraw, ImageFont, ImageOps
from threading import Thread, RLock
import time

# 
#  AYARLAR
# 

# Token environment variable'dan okunur
# Render: Dashboard  Environment  BOT_TOKEN ekle
# Lokal:  export BOT_TOKEN="token_buraya"  (Linux/Mac)
#         set BOT_TOKEN=token_buraya       (Windows)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") or os.environ.get("DISCORD_TOKEN", "")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN veya DISCORD_TOKEN environment variable ayarlanmamis! Render'da Environment sekmesine ekle.")
# Kalici ayar depolama:
# - SUPABASE_URL + SUPABASE_KEY varsa ayarlar Supabase'te tutulur
# - Yoksa en son fallback olarak settings.json kullanilir
AYAR_DOSYASI = os.environ.get("SETTINGS_PATH", "/opt/render/project/src/data/settings.json")
if not os.path.isabs(AYAR_DOSYASI):
    AYAR_DOSYASI = os.path.abspath(AYAR_DOSYASI)
SUPABASE_URL = os.environ.get("SUPABASE_URL", "").strip().rstrip("/")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "").strip() or os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "").strip()
SUPABASE_TABLE = os.environ.get("SUPABASE_TABLE", "bot_settings").strip() or "bot_settings"
# Bu surece ozel ID (loglarda / Mongo heartbeat  baska yerde calisan kopyayi ayirt etmek icin)
BOT_INSTANCE_ID = secrets.token_hex(8)
_ayar_dosya_kilidi = RLock()
_supabase_disabled_until = 0.0
_supabase_fail_count = 0
_ayar_cache_veri = None
_ayar_cache_zaman = 0.0
_AYAR_CACHE_TTL = float(os.environ.get("SETTINGS_CACHE_TTL", "15"))
YEREL_SAAT_DILIMI = ZoneInfo(os.environ.get("BOT_TIMEZONE", "Europe/Istanbul"))


def supabase_aktif_mi() -> bool:
    return bool(SUPABASE_URL and SUPABASE_KEY)


def mongo_aktif_mi() -> bool:
    return False


def _supabase_gecici_devre_disi_mi() -> bool:
    return time.monotonic() < _supabase_disabled_until


def _supabase_hata_koruma_aktif_et():
    global _supabase_disabled_until, _supabase_fail_count
    _supabase_fail_count += 1
    bekleme = min(300, 30 * _supabase_fail_count)
    _supabase_disabled_until = time.monotonic() + bekleme
    print(f"[UYARI] Supabase gecici devre disi ({bekleme}s), yerel fallback aktif.")


def _supabase_headers(ekstra: dict | None = None) -> dict:
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
    }
    if ekstra:
        headers.update(ekstra)
    return headers


def _supabase_istek(path: str, method: str = "GET", payload=None, extra_headers: dict | None = None, timeout: int = 20):
    if not supabase_aktif_mi() or _supabase_gecici_devre_disi_mi():
        return None
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{SUPABASE_URL}{path}",
        data=data,
        headers=_supabase_headers(extra_headers),
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ham = resp.read().decode("utf-8")
        global _supabase_fail_count
        _supabase_fail_count = 0
        return json.loads(ham) if ham else True
    except urllib.error.HTTPError as e:
        try:
            detay = e.read().decode("utf-8", errors="replace")
        except Exception:
            detay = str(e)
        print(f"[HATA] Supabase HTTP {e.code}: {detay}")
        _supabase_hata_koruma_aktif_et()
        return None
    except Exception as e:
        print(f"[HATA] Supabase baglantisi basarisiz: {e}")
        _supabase_hata_koruma_aktif_et()
        return None


def _supabase_prefix_kilit_ekle_sync(lock_id: str) -> bool | None:
    if not supabase_aktif_mi() or _supabase_gecici_devre_disi_mi():
        return None
    payload = [{
        "id": f"lock:{lock_id}",
        "data": {
            "type": "prefix_lock",
            "instance": BOT_INSTANCE_ID,
            "created_at": datetime.now(timezone.utc).isoformat(),
        },
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }]
    req = urllib.request.Request(
        f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}",
        data=json.dumps(payload).encode("utf-8"),
        headers=_supabase_headers({"Prefer": "return=minimal"}),
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10):
            pass
        return True
    except urllib.error.HTTPError as e:
        if e.code == 409:
            return False
        try:
            detay = e.read().decode("utf-8", errors="replace")
        except Exception:
            detay = str(e)
        print(f"[UYARI] Supabase prefix kilidi HTTP {e.code}: {detay}")
        return None
    except Exception as e:
        print(f"[UYARI] Supabase prefix kilidi baglanti hatasi: {e}")
        return None


_prefix_kilit_mongo_uyari = False


def _mongo_prefix_lock_koleksiyon():
    return None


def _upstash_kilit_env_var_mi() -> bool:
    u = os.environ.get("UPSTASH_REDIS_REST_URL", "").strip()
    t = os.environ.get("UPSTASH_REDIS_REST_TOKEN", "").strip()
    return bool(u and t)


def _upstash_set_nx_sync(key: str, ex_sn: int = 180) -> bool:
    url = os.environ["UPSTASH_REDIS_REST_URL"].strip().rstrip("/")
    token = os.environ["UPSTASH_REDIS_REST_TOKEN"].strip()
    body = json.dumps(["SET", key, "1", "NX", "EX", str(ex_sn)]).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        out = json.loads(resp.read().decode("utf-8"))
    return out.get("result") == "OK"


def _prefix_mesaj_kilidi_dene_sync(channel_id: int, message_id: int) -> bool:
    """
    True  -> Bu sre prefix komutunu altrmal (kilit alnd).
    False -> Baka bir sre / bot ayn mesaj iin kilidi zaten ald.
    """
    global _prefix_kilit_mongo_uyari
    lock_id = f"{channel_id}_{message_id}"
    supabase_sonuc = _supabase_prefix_kilit_ekle_sync(lock_id)
    if supabase_sonuc is not None:
        return supabase_sonuc

    if _upstash_kilit_env_var_mi():
        try:
            return _upstash_set_nx_sync(f"logbot:pcmd:{lock_id}", ex_sn=180)
        except Exception as e:
            print(f"[UYARI] Prefix kilidi Upstash: {e}")

    if not _prefix_kilit_mongo_uyari:
        _prefix_kilit_mongo_uyari = True
        print(
            "[UYARI] Prefix kilidi kapali (Upstash yok/bozuk). "
            "Sunucuda iki ayri Discord BOT UYGULAMASI varsa her ikisi de cevap verir  fazla botu sunucudan at veya tek bot kullan."
        )
    return True


def _prefix_dagitik_kilit_istiyor_mu() -> bool:
    """
    Varsayilan KAPALI: her komutta Mongo/HTTP round-trip olmaz, cevap hizli olur.
    Iki ayri bot/deploy ayni mesaja cift cevap veriyorsa Render'da ac:
        PREFIX_CMD_LOCK=1
    """
    v = os.environ.get("PREFIX_CMD_LOCK", os.environ.get("PREFIX_CMD_DEDUP", "")).strip().lower()
    if v in ("1", "true", "yes", "evet", "on", "acik", "ac"):
        return True
    return False


async def _prefix_mesaj_kilidi_dene(channel_id: int, message_id: int) -> bool:
    return await asyncio.to_thread(_prefix_mesaj_kilidi_dene_sync, channel_id, message_id)


def _prefix_lock_ttl_index_olustur():
    return


def _bot_surec_log_satirlari() -> list[str]:
    """Render / lokal konsolda bu sureci tanitmak icin."""
    parcalar = [f"id={BOT_INSTANCE_ID}", f"pid={os.getpid()}"]
    try:
        parcalar.append(f"host={socket.gethostname()[:100]}")
    except OSError:
        pass
    for env_k in ("RENDER_SERVICE_ID", "RENDER_INSTANCE_ID", "FLY_ALLOC_ID", "K_SERVICE", "HOSTNAME"):
        v = os.environ.get(env_k, "").strip()
        if v:
            parcalar.append(f"{env_k}={v[:48]}")
    return parcalar


def _mongo_instance_heartbeat_sync(bot_discord_user_id: int | None) -> tuple[list[dict] | None, str | None]:
    return None, "supabase_modunda_pasif"


async def _bot_coklu_surec_izleme_dongusu():
    """Aralikli olarak coklu surec bilgisini konsola yazar."""
    await bot.wait_until_ready()
    ilk_uyarni = True
    while not bot.is_closed():
        try:
            uid = int(bot.user.id) if bot.user else None
            aktif, hata = await asyncio.to_thread(_mongo_instance_heartbeat_sync, uid)
            if hata:
                if hata in ("mongo_kapali", "mongo_baglanamadi", "supabase_modunda_pasif"):
                    if ilk_uyarni:
                        print(
                            f"    Coklu-surec izleme: harici surec izleme pasif  baska yerde calisan kopyayi "
                            f"sadece PID/host satirindan veya sunucudaki bot sayisindan kontrol et."
                        )
                        ilk_uyarni = False
                else:
                    print(f"  [UYARI] Instance heartbeat: {hata}")
            elif aktif is not None:
                if len(aktif) > 1:
                    ozet = []
                    for d in aktif:
                        iid = str(d.get("_id", ""))[:10]
                        ozet.append(
                            f"{iid}.. pid={d.get('pid')} @{str(d.get('host', ''))[:24]}"
                        )
                    print(
                        f"    {len(aktif)} AYRI SUREC (son ~2dk)  cift mesaj normal: "
                        f"{' | '.join(ozet)}"
                    )
                elif ilk_uyarni:
                    print(
                        f"   Coklu-surec izleme: Mongo'da son 2 dk icinde yalniz bu instance kayitli "
                        f"({BOT_INSTANCE_ID[:10]}..)"
                    )
                    ilk_uyarni = False
        except Exception as e:
            print(f"  [UYARI] Instance izleme dongusu: {e}")
        await asyncio.sleep(75)

# 
#  SABT LOG KANALLARI (deploy'dan etkilenmez)
#  Kod gncellendiinde settings.json silinse bile
#  bu ID'ler otomatik olarak yeniden yklenir.
# 
DEFAULT_LOG_KANALLARI = {
    "ban_log":     1484564146111647917,
    "mute_log":    1484564329549267104,
    "mod_log":     1484564481257508874,
    "rol_log":     1484564569446944949,
    "mesaj_log":   1484564647704137879,
    "kanal_log":   1484565700969496606,
    "ses_log":     1484564774648938496,
    "davet_log":   1484564912486355106,
}

# Partner kanal ID'si (partner textinin atld kanal)
# Deitirmek istersen buraya yaz
DEFAULT_PARTNER_TEXT_KANALI = 1396219864279945397
DEFAULT_PARTNER_LOG_KANALI  = 1484813767253430363

#  Sabit Log Kanallar 
# Bu kanallar her deploy sonras otomatik yklenir.
# Deitirmek istersen buradan dzenle.
VARSAYILAN_LOG_KANALLARI = {
    "ban_log":     1484564146111647917,
    "mute_log":    1484564329549267104,
    "mod_log":     1484564481257508874,
    "rol_log":     1484564569446944949,
    "mesaj_log":   1484564647704137879,
    "kanal_log":   1484565700969496606,
    "ses_log":     1484564774648938496,
    "davet_log":   1484564912486355106,
}

# Desteklenen log trleri ve aklamalar
LOG_TURLERI = {
    "ban_log":      "Ban / Unban",
    "mute_log":     "Mute / Timeout",
    "mod_log":      "Moderasyon",
    "rol_log":      "Rol Degisiklikleri",
    "mesaj_log":    "Mesaj Islemleri",
    "giris_cikis":  "Giris / Cikis",
    "ses_log":      "Ses Kanallari",
    "kanal_log":    "Kanal Islemleri",
    "davet_log":    "Davetler",
}

# Otomatik log kurulumunda aranacak kanal ad kalplar
LOG_KANAL_KALIPLARI = {
    "ban_log": ["ban-log", "ban-logs", "banlog", "bans"],
    "mute_log": ["mute-log", "mute-logs", "mutelog", "timeout-log", "timeout"],
    "mod_log": ["mod-log", "mod-logs", "modlog", "moderasyon", "moderation"],
    "rol_log": ["rol-log", "role-log", "rollog", "role-logs"],
    "mesaj_log": ["mesaj-log", "message-log", "messagelog", "msg-log"],
    "giris_cikis": ["giris-cikis", "join-leave", "uye-log", "member-log", "giris"],
    "ses_log": ["ses-log", "voice-log", "voicelog", "ses"],
    "kanal_log": ["kanal-log", "channel-log", "channellog"],
    "davet_log": ["davet-log", "invite-log", "invitelog", "davet"],
}

# Embed renk paleti
RENKLER = {
    "ban":    0xE74C3C,
    "mute":   0xE67E22,
    "unban":  0x2ECC71,
    "rol":    0x9B59B6,
    "izin":   0x3498DB,
    "mesaj":  0xF39C12,
    "giris":  0x1ABC9C,
    "cikis":  0x95A5A6,
    "ses":    0x16A085,
    "bilgi":  0x7F8C8D,
    "basari": 0x2ECC71,
    "hata":   0xE74C3C,
}

# 
#  AYAR YNETM (settings.json)
# 

def ayarlari_yukle() -> dict:
    """
    nce Supabase'ten, yoksa yerel fallback dosyasndan ayarlar okur.
    Yap: { "guild_id": { "log_turu": kanal_id, ... }, ... }
    Dosya yoksa bo dict dndrr.
    """
    global _ayar_cache_veri, _ayar_cache_zaman
    simdi = time.monotonic()
    if _ayar_cache_veri is not None and (simdi - _ayar_cache_zaman) < _AYAR_CACHE_TTL:
        return json.loads(json.dumps(_ayar_cache_veri))

    if supabase_aktif_mi():
        belge = _supabase_istek(
            f"/rest/v1/{SUPABASE_TABLE}?id=eq.global_settings&select=data",
            extra_headers={"Accept": "application/json"},
        )
        if isinstance(belge, list) and belge:
            veri = belge[0].get("data", {}) or {}
            _ayar_cache_veri = veri
            _ayar_cache_zaman = simdi
            return json.loads(json.dumps(veri))

    with _ayar_dosya_kilidi:
        klasor = os.path.dirname(AYAR_DOSYASI)
        if klasor:
            os.makedirs(klasor, exist_ok=True)
        if not os.path.exists(AYAR_DOSYASI):
            return {}
        try:
            with open(AYAR_DOSYASI, "r", encoding="utf-8") as f:
                veri = json.load(f)
                _ayar_cache_veri = veri
                _ayar_cache_zaman = simdi
                return json.loads(json.dumps(veri))
        except json.JSONDecodeError as e:
            print(f"[HATA] settings.json bozuk, bos ayarlarla devam edilecek: {e}")
            return {}


def varsayilan_kanallari_yukle(guild_id: int):
    """
    Varsaylan log kanallarn settings.json'a yazar.
    Her bot balangcnda arlr  mevcut ayarlarn zerine yazmaz,
    sadece eksik olanlar tamamlar.
    """
    ayarlar = ayarlari_yukle()
    gk = str(guild_id)
    if gk not in ayarlar:
        ayarlar[gk] = {}
    degisti = False
    for tur, kanal_id in VARSAYILAN_LOG_KANALLARI.items():
        if tur not in ayarlar[gk]:
            ayarlar[gk][tur] = kanal_id
            degisti = True
    if degisti:
        ayarlari_kaydet(ayarlar)


def ayarlari_kaydet(veri: dict):
    """Tm ayarlar nce Supabase'e, o yoksa yerel dosyaya yazar."""
    global _ayar_cache_veri, _ayar_cache_zaman
    if supabase_aktif_mi():
        sonuc = _supabase_istek(
            f"/rest/v1/{SUPABASE_TABLE}?on_conflict=id",
            method="POST",
            payload=[{
                "id": "global_settings",
                "data": veri,
                "updated_at": datetime.now(timezone.utc).isoformat(),
            }],
            extra_headers={
                "Prefer": "resolution=merge-duplicates,return=minimal",
            },
        )
        if sonuc is not None:
            _ayar_cache_veri = json.loads(json.dumps(veri))
            _ayar_cache_zaman = time.monotonic()
            return
        print("[UYARI] Supabase'e yazma basarisiz; yerel fallback dosyaya yaziliyor.")

    with _ayar_dosya_kilidi:
        klasor = os.path.dirname(AYAR_DOSYASI)
        if klasor:
            os.makedirs(klasor, exist_ok=True)
        gecici_dosya = f"{AYAR_DOSYASI}.tmp"
        with open(gecici_dosya, "w", encoding="utf-8") as f:
            json.dump(veri, f, indent=2, ensure_ascii=False)
        os.replace(gecici_dosya, AYAR_DOSYASI)
        _ayar_cache_veri = json.loads(json.dumps(veri))
        _ayar_cache_zaman = time.monotonic()


def ayarlari_guncelle(guncelleyici):
    """JSON fallback kullanilirken oku-degistir-yaz akisini tek kilitte toplar."""
    with _ayar_dosya_kilidi:
        ayarlar = ayarlari_yukle()
        sonuc = guncelleyici(ayarlar)
        ayarlari_kaydet(ayarlar)
        return sonuc


def kanal_al(guild_id: int, tur: str) -> int | None:
    """
    Belirli bir sunucu ve log tr iin kaytl kanal ID'sini dndrr.
    Kaytl deilse None dndrr.
    """
    ayarlar = ayarlari_yukle()
    return ayarlar.get(str(guild_id), {}).get(tur)


def kanal_kaydet(guild_id: int, tur: str, kanal_id: int):
    """Bir log tr iin kanal ID'sini settings.json'a kaydeder."""
    with _ayar_dosya_kilidi:
        ayarlar = ayarlari_yukle()
        guild_key = str(guild_id)
        if guild_key not in ayarlar:
            ayarlar[guild_key] = {}
        ayarlar[guild_key][tur] = kanal_id
        ayarlari_kaydet(ayarlar)


def kanal_sil(guild_id: int, tur: str):
    """Bir log trnn kanal kaydn siler (devre d brakr)."""
    with _ayar_dosya_kilidi:
        ayarlar = ayarlari_yukle()
        guild_key = str(guild_id)
        if guild_key in ayarlar and tur in ayarlar[guild_key]:
            del ayarlar[guild_key][tur]
            ayarlari_kaydet(ayarlar)


def guild_ayarlari_sil(guild_id: int):
    """Bir sunucunun tm log ayarlarn tamamen siler."""
    with _ayar_dosya_kilidi:
        ayarlar = ayarlari_yukle()
        guild_key = str(guild_id)
        if guild_key in ayarlar:
            del ayarlar[guild_key]
            ayarlari_kaydet(ayarlar)


# 
#  BOT KURULUMU
# 

intents = discord.Intents.default()
intents.guilds          = True
intents.members         = True
intents.bans            = True
intents.message_content = True
intents.messages        = True
intents.voice_states    = True
intents.invites         = True

PREFIX = os.environ.get("BOT_PREFIX", ".")

bot = commands.Bot(command_prefix=PREFIX, intents=intents, case_insensitive=True, help_command=None)


class PrefixMesajCiftKopya(commands.CheckFailure):
    """Ayn Discord mesaj iin baka bir bot sreci prefix komutunu zaten iledi."""


@bot.check
async def prefix_komut_mesaj_kilidi(ctx: commands.Context):
    """Opsiyonel dagitik kilit: PREFIX_CMD_LOCK=1 (cift bot)  varsayilan kapali, hiz icin."""
    if ctx.message is None:
        return True
    if not _prefix_dagitik_kilit_istiyor_mu():
        return True
    if not mongo_aktif_mi() and not _upstash_kilit_env_var_mi():
        return True
    cid = ctx.message.channel.id if ctx.message.channel else 0
    if await _prefix_mesaj_kilidi_dene(cid, ctx.message.id):
        return True
    raise PrefixMesajCiftKopya()


async def _prefix_komutlari_isle(message: discord.Message):
    """
    Ayni Discord mesaji icin process_commands yalnizca bir kez calisir.
    Cift yanit (kayitli + bos) sorununu genelde bu tur cift cagri olusturur.
    """
    if not hasattr(bot, "_prefix_islenen_mesaj_ids"):
        bot._prefix_islenen_mesaj_ids = set()
    mid = message.id
    if mid in bot._prefix_islenen_mesaj_ids:
        return
    bot._prefix_islenen_mesaj_ids.add(mid)
    if len(bot._prefix_islenen_mesaj_ids) > 4000:
        bot._prefix_islenen_mesaj_ids = set(list(bot._prefix_islenen_mesaj_ids)[-2000:])
    await bot.process_commands(message)


# 
#  YARDIMCI FONKSYONLAR
# 

async def log_gonder(guild: discord.Guild, tur: str, embed: discord.Embed):
    """
    settings.json'dan ilgili log kanaln bulup embed gnderir.
    Kanal ayarlanmamsa veya bulunamazsa sessizce geer.
    """
    kanal_id = kanal_al(guild.id, tur)
    if not kanal_id:
        return  # Bu log tr iin kanal ayarlanmam

    kanal = guild.get_channel(kanal_id)
    if not kanal:
        return  # Kanal daha sonra silinmi olabilir

    try:
        await kanal.send(embed=embed)
    except discord.Forbidden:
        print(f"[HATA] '{tur}' kanalna yazma izni yok.")
    except discord.HTTPException as e:
        print(f"[HATA] Log gnderilemedi: {e}")


def utc_datetime_from_iso(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def zaman_damgasi() -> str:
    now = datetime.now(timezone.utc)
    return now.strftime(" %d.%m.%Y   %H:%M:%S UTC")


def hata_embedi(title: str, description: str) -> discord.Embed:
    embed = discord.Embed(
        title=title,
        description=description,
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=zaman_damgasi())
    return embed


def kullanim_embedi(description: str) -> discord.Embed:
    embed = discord.Embed(
        title="Komut Kullanm",
        description=description,
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=zaman_damgasi())
    return embed


class TicketControlView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label=" Kapat", style=discord.ButtonStyle.danger, custom_id="ticket_kapat")
    async def kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message(" Bu buton sadece ticket kanalnda kullanlabilir.", ephemeral=True)
            return

        ayar = ticket_ayar_al(interaction.guild_id)
        log_id = ayar.get("log")
        await _ticket_kapat_logu_ve_transkript(channel, interaction.user, log_id)
        if False and log_id:
            log_kanali = interaction.guild.get_channel(log_id)
            if log_kanali:
                await log_kanali.send(embed=discord.Embed(
                    title=" Ticket Kapatld",
                    description=f"**Ticket:** `{channel.name}`\n**Kapatan:** {interaction.user.mention}",
                    color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)
                ))

        await interaction.response.send_message("Ticket kapatlyor...", ephemeral=True)
        await channel.delete(reason=f"{interaction.user} tarafndan kapatld")

    @discord.ui.button(label=" ye Ekle", style=discord.ButtonStyle.secondary, custom_id="ticket_uyeekle")
    async def uye_ekle(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message(" Bu buton sadece ticket kanalnda kullanlabilir.", ephemeral=True)
            return

        await interaction.response.send_message("Eklemek istediin kullancy bu kanalda etiketle: @kullanc", ephemeral=True)

        def check(message: discord.Message):
            return message.author == interaction.user and message.channel == channel and message.mentions

        try:
            yanit = await bot.wait_for("message", check=check, timeout=30)
            for uye in yanit.mentions:
                await channel.set_permissions(uye, read_messages=True, send_messages=True)
            await channel.send(f" {' '.join(u.mention for u in yanit.mentions)} ticketa eklendi.")
            await yanit.delete()
        except asyncio.TimeoutError:
            await channel.send(" Kullanc ekleme isteinin sresi doldu.", delete_after=5)

    @discord.ui.button(label=" Talep Al", style=discord.ButtonStyle.success, custom_id="ticket_talep")
    async def talep_al(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message(" Bu buton sadece ticket kanalnda kullanlabilir.", ephemeral=True)
            return

        ayar = ticket_ayar_al(interaction.guild_id)
        destek_rolu = interaction.guild.get_role(ayar.get("rol"))
        if destek_rolu and destek_rolu not in interaction.user.roles and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(" Bu ilem iin destek rol gerekli.", ephemeral=True)
            return

        yeni_topic = channel.topic or ""
        if " | Talep:" in yeni_topic:
            yeni_topic = yeni_topic.split(" | Talep:")[0]
        await channel.edit(topic=f"{yeni_topic} | Talep: {interaction.user}")
        await interaction.response.send_message(f" Ticket {interaction.user.mention} tarafndan talep alnd.")


class TicketOpenView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label=" Ticket A", style=discord.ButtonStyle.primary, custom_id="global_ticket_ac")
    async def ticket_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        ayar = ticket_ayar_al(interaction.guild_id)
        kategori = interaction.guild.get_channel(ayar.get("kategori"))
        destek_rolu = interaction.guild.get_role(ayar.get("rol"))
        log_id = ayar.get("log")

        if not kategori:
            await interaction.response.send_message(" Kategori bulunamad. `.ticketkur` ile yeniden kur.", ephemeral=True)
            return

        for kanal in kategori.text_channels:
            if kanal.topic and str(interaction.user.id) in kanal.topic:
                await interaction.response.send_message(f" Zaten ak bir ticketn var: {kanal.mention}", ephemeral=True)
                return

        sayi = ticket_sayaci_artir(interaction.guild_id)
        bot_member = interaction.guild.me or interaction.guild.default_role
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True),
            bot_member: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_channels=True),
        }
        if destek_rolu:
            overwrites[destek_rolu] = discord.PermissionOverwrite(read_messages=True, send_messages=True)

        ticket_kanal = await kategori.create_text_channel(
            name=f"ticket-{sayi:04d}",
            overwrites=overwrites,
            topic=f"Ticket sahibi: {interaction.user} | ID: {interaction.user.id} | #{sayi}"
        )

        ac_embed = discord.Embed(
            title=f" Ticket #{sayi:04d}",
            description=(
                f"Merhaba {interaction.user.mention}!\n"
                f"Destek ekibimiz en ksa srede yardmc olacak.\n\n"
                f"Ticket kapatmak iin  butonunu kullan."
            ),
            color=0x57F287, timestamp=datetime.now(timezone.utc)
        )
        ac_embed.set_footer(text=f"Ticket #{sayi:04d}  {zaman_damgasi()}")

        await ticket_kanal.send(
            content=f"{interaction.user.mention}{(' ' + destek_rolu.mention) if destek_rolu else ''}",
            embed=ac_embed,
            view=TicketControlView()
        )
        await interaction.response.send_message(f" Ticketn ald: {ticket_kanal.mention}", ephemeral=True)

        if log_id:
            log_kanali = interaction.guild.get_channel(log_id)
            if log_kanali:
                await log_kanali.send(embed=discord.Embed(
                    title=" Yeni Ticket Ald",
                    description=f"**Aan:** {interaction.user.mention}\n**Kanal:** {ticket_kanal.mention}\n**Numara:** `#{sayi:04d}`",
                    color=RENKLER["giris"], timestamp=datetime.now(timezone.utc)
                ))


async def audit_log_bul(guild: discord.Guild, eylem: discord.AuditLogAction, hedef=None):
    """Audit log zerinden en son ilemi yapan kiiyi bulur."""
    try:
        async for log in guild.audit_logs(limit=5, action=eylem):
            if hedef is None or log.target.id == hedef.id:
                return log.user
    except discord.Forbidden:
        pass
    return None


def izin_adi_getir(perm_adi: str) -> str:
    """ngilizce izin adn Trkeye evirir. Bilinmeyenler aynen dndrlr."""
    ceviriler = {
        "administrator":            " Ynetici",
        "manage_guild":             " Sunucuyu Ynet",
        "manage_roles":             " Rolleri Ynet",
        "manage_channels":          " Kanallar Ynet",
        "manage_messages":          " Mesajlar Ynet",
        "manage_nicknames":         " Takma Adlar Ynet",
        "manage_webhooks":          " Webhook'lar Ynet",
        "manage_expressions":       " fadeleri Ynet",
        "manage_threads":           " Konular Ynet",
        "kick_members":             " ye At",
        "ban_members":              " ye Banla",
        "moderate_members":         " yeleri Sustur",
        "view_audit_log":           " Denetim Gnln Gr",
        "view_guild_insights":      " Sunucu grlerini Gr",
        "send_messages":            " Mesaj Gnder",
        "send_tts_messages":        " TTS Mesaj Gnder",
        "embed_links":              " Link nizlemesi",
        "attach_files":             " Dosya Ekle",
        "read_message_history":     " Mesaj Gemiini Oku",
        "mention_everyone":         " @everyone Etiketle",
        "use_external_emojis":      " Harici Emoji Kullan",
        "use_external_stickers":    " Harici kartma Kullan",
        "add_reactions":            " Tepki Ekle",
        "use_slash_commands":       " Slash Komutlarn Kullan",
        "connect":                  " Ses Kanalna Balan",
        "speak":                    " Konu",
        "stream":                   " Yayn Yap",
        "use_voice_activation":     " Sesle Etkinletir",
        "mute_members":             " yeleri Sustur (Ses)",
        "deafen_members":           " yeleri Sarlatr",
        "move_members":             " yeleri Ta",
        "priority_speaker":         " ncelikli Konumac",
        "create_instant_invite":    " Annda Davet Olutur",
        "change_nickname":          " Takma Ad Deitir",
        "view_channel":             " Kanal Gr",
        "request_to_speak":         " Konuma stei",
        "use_embedded_activities":  " Aktiviteleri Kullan",
        "send_messages_in_threads": " Konularda Mesaj Gnder",
        "create_public_threads":    " Herkese Ak Konu Olutur",
        "create_private_threads":   " zel Konu Olutur",
    }
    return ceviriler.get(perm_adi, f" {perm_adi.replace('_', ' ').title()}")


def izin_farklarini_bul(eski: discord.Permissions, yeni: discord.Permissions):
    """
    ki Permissions nesnesi arasndaki farklar hesaplar.

    Mantk:
        - Her izin True/False deeri tar.
        - Eski ve yeni deerleri karlatrarak:
            * False  True  : izin EKLEND
            * True   False : izin KALDIRILDI
        - Deimeyenler atlanr.

    Dndrr:
        eklenenler   : list[str]  eklenen izinlerin Trke isimleri
        kaldirlanlar : list[str]  kaldrlan izinlerin Trke isimleri
    """
    eklenenler   = []
    kaldirlanlar = []

    # discord.Permissions.__iter__()  (izin_ad, bool) iftleri dndrr
    eski_dict = dict(eski)
    yeni_dict = dict(yeni)

    for perm_adi in eski_dict:
        eski_deger = eski_dict[perm_adi]
        yeni_deger = yeni_dict.get(perm_adi, False)

        if eski_deger == yeni_deger:
            continue  # Deiiklik yok, atla

        ad = izin_adi_getir(perm_adi)

        if not eski_deger and yeni_deger:
            eklenenler.append(ad)       # False  True: eklendi
        elif eski_deger and not yeni_deger:
            kaldirlanlar.append(ad)     # True  False: kaldrld

    return eklenenler, kaldirlanlar


# 
#  SLASH KOMUTLARI  LOG AYARLARI
# 

# Slash komutlarnda alr men iin seenek listesi
LOG_TUR_SECENEKLERI = [
    app_commands.Choice(name=aciklama, value=tur)
    for tur, aciklama in LOG_TURLERI.items()
]


@bot.tree.command(name="log-kur", description="Bir log turu icin kanal atar")
@app_commands.describe(
    tur="Hangi log turu icin kanal ayarlaniyor?",
    kanal="Loglarin gidecegi metin kanali"
)
@app_commands.choices(tur=LOG_TUR_SECENEKLERI)
@app_commands.checks.has_permissions(manage_guild=True)
async def log_kur(
    interaction: discord.Interaction,
    tur: app_commands.Choice[str],
    kanal: discord.TextChannel
):
    """
    Belirli bir log tr iin kanal atar ve settings.json'a kaydeder.
    Sadece 'Sunucuyu Ynet' iznine sahip kiiler kullanabilir.
    """

    # Bota kanalda yazma izni var m?
    if not kanal.permissions_for(interaction.guild.me).send_messages:
        embed = discord.Embed(
            title=" Yetki Hatas",
            description=f"{kanal.mention} kanalna mesaj gnderemiyorum.\nKanal izinlerimi kontrol edin.",
            color=RENKLER["hata"]
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    # Ayar kaydet
    kanal_kaydet(interaction.guild_id, tur.value, kanal.id)

    #  Sana zel onay mesaj (sadece sen grrsn) 
    onay_embed = discord.Embed(
        title=" Log Kanal Ayarland",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    onay_embed.add_field(name=" Log Tr", value=tur.name,      inline=True)
    onay_embed.add_field(name=" Kanal",    value=kanal.mention, inline=True)
    onay_embed.set_footer(text=f"Ayarlayan: {interaction.user}  {zaman_damgasi()}")
    await interaction.response.send_message(embed=onay_embed, ephemeral=True)

    #  Log kanalna bilgilendirme mesaj 
    kanal_embed = discord.Embed(
        title=" Log Kanal Aktif",
        description=f"Bu kanal **{tur.name}** iin log kanal olarak ayarland.\nArtk ilgili olaylar buraya decek.",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    kanal_embed.add_field(name=" Ayarlayan", value=interaction.user.mention, inline=True)
    kanal_embed.set_footer(text=zaman_damgasi())
    await kanal.send(embed=kanal_embed)


@bot.tree.command(name="log-kaldir", description="Bir log turunu kapatir")
@app_commands.describe(tur="Kapatilacak log turu")
@app_commands.choices(tur=LOG_TUR_SECENEKLERI)
@app_commands.checks.has_permissions(manage_guild=True)
async def log_kaldir(
    interaction: discord.Interaction,
    tur: app_commands.Choice[str]
):
    """Belirtilen log trnn kanal kaydn siler ve o logu durdurur."""

    mevcut = kanal_al(interaction.guild_id, tur.value)
    if not mevcut:
        embed = discord.Embed(
            title=" Zaten Devre D",
            description=f"**{tur.name}** iin zaten bir kanal ayarlanmam.",
            color=RENKLER["bilgi"]
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    kanal_sil(interaction.guild_id, tur.value)

    embed = discord.Embed(
        title=" Log Kanal Kaldrld",
        description=f"**{tur.name}** artk log gndermeyecek.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=f"Kaldran: {interaction.user}")
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name="log-durum", description="Tum log kanallarini gosterir")
@app_commands.checks.has_permissions(manage_guild=True)
async def log_durum(interaction: discord.Interaction):
    """
    Bu sunucudaki tm log trlerini ve atanm kanallarn listeler.
    Kanal ayarlanmamsa ' Deaktif' olarak gsterilir.
    """
    ayarlar = ayarlari_yukle().get(str(interaction.guild_id), {})

    embed = discord.Embed(
        title=" Log Sistemi Durumu",
        description=f"**{interaction.guild.name}** sunucusundaki log ayarlar",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )

    mod_turleri   = {"ban_log", "mute_log", "mod_log"}
    mod_satirlar  = []
    genel_satirlar = []

    for tur, aciklama in LOG_TURLERI.items():
        kanal_id = ayarlar.get(tur)
        if kanal_id:
            kanal = interaction.guild.get_channel(kanal_id)
            durum = kanal.mention if kanal else " Kanal Silinmi"
        else:
            durum = " Deaktif"

        satir = f"**{aciklama}**\n {durum}"

        if tur in mod_turleri:
            mod_satirlar.append(satir)
        else:
            genel_satirlar.append(satir)

    if mod_satirlar:
        embed.add_field(
            name=" Moderasyon Loglar",
            value="\n\n".join(mod_satirlar),
            inline=False
        )
    if genel_satirlar:
        embed.add_field(
            name=" Genel Loglar",
            value="\n\n".join(genel_satirlar),
            inline=False
        )

    aktif = len([t for t in LOG_TURLERI if t in ayarlar])
    embed.set_footer(text=f"{aktif}/{len(LOG_TURLERI)} log tr aktif  {zaman_damgasi()}")

    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name="log-sifirla", description="Bu sunucunun tm log ayarlarn siler")
@app_commands.checks.has_permissions(administrator=True)
async def log_sifirla(interaction: discord.Interaction):
    """
    Onay butonlu mesaj gstererek tm log ayarlarn sfrlar.
    Sadece 'Ynetici' iznine sahip kiiler kullanabilir.
    """

    class OnayView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=30)

        @discord.ui.button(label="Evet, Sfrla", style=discord.ButtonStyle.danger, emoji="")
        async def onayla(self, btn_i: discord.Interaction, button: discord.ui.Button):
            guild_ayarlari_sil(btn_i.guild_id)
            embed = discord.Embed(
                title=" Tm Log Ayarlar Silindi",
                description="Bu sunucuya ait tm log kanal kaytlar kaldrld.",
                color=RENKLER["hata"]
            )
            await btn_i.response.edit_message(embed=embed, view=None)

        @discord.ui.button(label="ptal", style=discord.ButtonStyle.secondary, emoji="")
        async def iptal(self, btn_i: discord.Interaction, button: discord.ui.Button):
            embed = discord.Embed(
                title=" ptal Edildi",
                description="Sfrlama ilemi iptal edildi, ayarlar korundu.",
                color=RENKLER["basari"]
            )
            await btn_i.response.edit_message(embed=embed, view=None)

    embed = discord.Embed(
        title=" Emin misiniz?",
        description="Bu ilem tm log kanal ayarlarn **kalc olarak** silecek.\nGeri alnamaz!",
        color=RENKLER["hata"]
    )
    await interaction.response.send_message(embed=embed, view=OnayView(), ephemeral=True)


# 
#  KFR KORUMASI
# 

class KufurKorumasiModal(discord.ui.Modal, title="Kufur Korumasi Ayarlari"):
    """Yasak kelimeleri yaplandrmak iin modal."""
    
    yasakli_kelimeler = discord.ui.TextInput(
        label="Yasak Kelimeler (virgl ile ayrnz)",
        placeholder="rnek: kelime1, kelime2, kelime3",
        required=True,
        style=discord.TextStyle.long,
        max_length=2000
    )
    
    async def on_submit(self, interaction: discord.Interaction):
        # Kelimeleri temizle ve kaydet
        metin = str(self.yasakli_kelimeler).strip()
        if not metin:
            await interaction.response.send_message(
                embed=discord.Embed(
                    title=" Hata",
                    description="Ltfen en az bir kelime girin.",
                    color=RENKLER["hata"]
                ),
                ephemeral=True
            )
            return
        
        # Kelimeleri virgl ile ayr ve temizle
        kelimeler = [k.strip().lower() for k in metin.split(",") if k.strip()]
        
        if not kelimeler:
            await interaction.response.send_message(
                embed=discord.Embed(
                    title=" Hata",
                    description="Ltfen geerli kelimeler girin.",
                    color=RENKLER["hata"]
                ),
                ephemeral=True
            )
            return
        
        # Ayarlara kaydet
        kufur_kelimelerini_kaydet(interaction.guild_id, kelimeler)
        
        await interaction.response.send_message(
            embed=discord.Embed(
                title=" Kfr Korumas Ayarland",
                description=f"**{len(kelimeler)}** yasak kelime kaydedildi.",
                color=RENKLER["basari"],
                timestamp=datetime.now(timezone.utc)
            ),
            ephemeral=True
        )


def kufur_kelimelerini_kaydet(guild_id: int, kelimeler: list[str]):
    """Yasak kelimeleri ayarlara kaydeder."""
    with _ayar_dosya_kilidi:
        ayarlar = ayarlari_yukle()
        guild_key = str(guild_id)
        if guild_key not in ayarlar:
            ayarlar[guild_key] = {}
        ayarlar[guild_key]["yasakli_kelimeler"] = kelimeler
        ayarlari_kaydet(ayarlar)


def kufur_kelimelerini_al(guild_id: int) -> list[str]:
    """Sunucuya ait yasak kelimeleri dndrr."""
    ayarlar = ayarlari_yukle()
    return ayarlar.get(str(guild_id), {}).get("yasakli_kelimeler", [])

def kufur_kontrol(guild_id: int, mesaj: str) -> bool:
    """Mesajda tam olarak yasakl kelime var m kontrol eder, noktalama iaretlerini gz ard eder."""
    yasakli_kelimeler = kufur_kelimelerini_al(guild_id)
    if not yasakli_kelimeler:
        return False
    
    mesaj_temiz = mesaj.lower()
    # Kelimeleri ayrrken noktalama iaretlerini gz ard et
    mesaj_kelimeleri = re.findall(r'\b\w+\b', mesaj_temiz)
    
    for kelime in mesaj_kelimeleri:
        if kelime in yasakli_kelimeler:
            return True
    return False


def mesajda_yasakli_kelime_var_mi(mesaj: str, yasakli_kelimeler: list[str]) -> bool:
    """
    Mesajda yasak kelime olup olmadn kontrol eder.
    Ksmi elemeleri de bulur (rnek: 'test' yazarken 'testt' de bulur).
    """
    if not yasakli_kelimeler:
        return False
    
    mesaj_temiz = mesaj.lower()
    for kelime in yasakli_kelimeler:
        if kelime in mesaj_temiz:
            return True
    return False


@bot.command(name="kufur-kur")
@commands.has_permissions(manage_guild=True)
async def kufur_kur(ctx):
    """
    Modal aarak kfr korumas iin yasak kelimeleri yaplandrr.
    Kelimeleri virgl ile ayrarak girin.
    """
    await ctx.send("Modal amak iin butona tklayn:", view=KufurModalView())


@bot.command(name="kufur-durum")
@commands.has_permissions(manage_guild=True)
async def kufur_durum(ctx):
    """u anda tanml olan yasak kelimeleri ve saylarn gsterir."""
    kelimeler = kufur_kelimelerini_al(ctx.guild.id)
    
    if not kelimeler:
        embed = discord.Embed(
            title=" Kfr Korumas",
            description="Bu sunucuda henz yasak kelime tanmlanmam.\n`.kufur-kur` komutu ile ayarla!",
            color=RENKLER["bilgi"]
        )
    else:
        # Kelimeleri gruplara ayr (Discord mesaj limiti iin)
        kelimeler_str = ", ".join(kelimeler[:50])  # lk 50 gster
        if len(kelimeler) > 50:
            kelimeler_str += f", ... ve {len(kelimeler) - 50} kelime daha"
        
        embed = discord.Embed(
            title=" Kfr Korumas Aktif",
            description=f"**Toplam Yasak Kelime:** {len(kelimeler)}",
            color=RENKLER["basari"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(
            name=" Yasak Kelimeler",
            value=f"```\n{kelimeler_str}\n```",
            inline=False
        )
    
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


@bot.command(name="kufur-listele")
@commands.has_permissions(manage_guild=True)
async def kufur_listele(ctx):
    kelimeler = sorted(set(TURKCE_KUFUR_LISTESI))
    metin = ", ".join(kelimeler)
    embed = discord.Embed(
        title="Kufur Listesi",
        description=f"Toplam **{len(kelimeler)}** kelime.\n```{metin[:3800]}```",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    await ctx.send(embed=embed)


@bot.command(name="kufur-kapat", aliases=["kufurkapat"])
@commands.has_permissions(administrator=True)
async def kufur_kapat(ctx):
    guild_key = str(ctx.guild.id)
    ayarlar = ayarlari_yukle()
    if guild_key not in ayarlar or not ayarlar[guild_key].get("yasakli_kelimeler"):
        await ctx.send(embed=hata_embedi("Kufur Korumasi Kapali", "Bu sunucuda kapatilacak aktif bir kufur listesi yok."))
        return
    ayarlar[guild_key]["yasakli_kelimeler"] = []
    ayarlari_kaydet(ayarlar)
    await ctx.send(embed=discord.Embed(
        title="Kufur Korumasi Kapatildi",
        description="Bu sunucudaki yasak kelime listesi temizlendi ve kufur kontrolu durduruldu.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    ))


@bot.command(name="kufur-temizle")
@commands.has_permissions(administrator=True)
async def kufur_temizle(ctx):
    """Tm yasak kelimeleri siler ve kfr korumasn kapatr."""
    
    if ctx.guild.id not in _kufur_kelimeler:
        await ctx.send("Bu sunucuda zaten kfr korumas ayarlanmam.")
        return
    
    del _kufur_kelimeler[ctx.guild.id]
    kufur_kelimelerini_kaydet()
    
    embed = discord.Embed(
        title=" Kfr Korumas Temizlendi",
        description="Tm yasak kelimeler silindi ve kfr korumas kapatld.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=f"lemi yapan: {ctx.author}")
    
    await ctx.send(embed=embed)


# Kufur Modal View
class KufurModalView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label=" Modal A", style=discord.ButtonStyle.primary)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = KufurKorumasiModal()
        await interaction.response.send_modal(modal)


@bot.command(name="blubpatlat")
@commands.has_permissions(ban_members=True)
async def blubpatlat(ctx):
    """Sunucudaki tm yeleri banlar."""
    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.send("Botun yeleri banlama yetkisi yok!")
        return
    
    await ctx.send("Tm yeler banlanyor... Bu ilem uzun srebilir!")
    
    ban_sayisi = 0
    hata_sayisi = 0
    
    for member in ctx.guild.members:
        if member.top_role >= ctx.guild.me.top_role:
            hata_sayisi += 1
            continue
        
        try:
            await member.ban(reason="Blubpatlat komutu", delete_message_seconds=0)
            ban_sayisi += 1
        except discord.Forbidden:
            hata_sayisi += 1
        except Exception:
            hata_sayisi += 1
    
    embed = discord.Embed(
        title=" Blubpatlat Tamamland",
        color=0xFF6B6B,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name=" Banlanan ye", value=f"**{ban_sayisi}** kii", inline=True)
    embed.add_field(name=" Banlanamayan", value=f"**{hata_sayisi}** kii", inline=True)
    embed.add_field(name=" Toplam ye", value=f"**{len(ctx.guild.members)}** kii", inline=True)
    embed.set_footer(text=f"lemi yapan: {ctx.author}")
    
    await ctx.send(embed=embed)


@bot.command(name="blupblup")
@commands.has_permissions(manage_roles=True)
async def blupblup(ctx, yeni_isim: str):
    """sminde 'blup' geen herkesin ismini deitirir."""
    if not ctx.guild.me.guild_permissions.manage_nicknames:
        await ctx.send("Botun isim deitirme yetkisi yok!")
        return
    
    await ctx.send("simlerinde 'blup' aranyor...")
    
    degistirilen = 0
    hata_sayisi = 0
    
    for member in ctx.guild.members:
        if member.bot:
            continue
        
        # Komutu yazan hari tut
        if member.id == ctx.author.id:
            continue
        
        if "blup" in member.display_name.lower() or "blup" in member.name.lower():
            try:
                await member.edit(nick=yeni_isim, reason="Blupblup komutu")
                degistirilen += 1
            except discord.Forbidden:
                hata_sayisi += 1
            except Exception:
                hata_sayisi += 1
    
    embed = discord.Embed(
        title=" Blupblup lemi Tamamland",
        color=0x5865F2,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name=" Deitirilen ye", value=f"**{degistirilen}** kii", inline=True)
    embed.add_field(name=" Deitirilemeyen", value=f"**{hata_sayisi}** kii", inline=True)
    embed.add_field(name=" Toplam ye", value=f"**{len(ctx.guild.members)}** kii", inline=True)
    embed.add_field(name=" Yeni sim", value=f"**{yeni_isim}**", inline=False)
    embed.add_field(name=" Not", value=f"**{ctx.author}** hari tutuldu", inline=False)
    embed.set_footer(text=f"lemi yapan: {ctx.author}")
    
    await ctx.send(embed=embed)
@log_kur.error
@log_kaldir.error
@log_durum.error
@log_sifirla.error
@kufur_kur.error
@kufur_durum.error
@kufur_temizle.error
async def komut_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title=" Yetersiz Yetki",
            description="Bu komutu kullanmak iin **Sunucuyu Ynet** iznine ihtiyacnz var.",
            color=RENKLER["hata"]
        )
        await ctx.send(embed=embed)


# 
#  OLAYLAR  MODERASYON LOGLARI
# 

@bot.event
async def on_member_ban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_log_bul(guild, discord.AuditLogAction.ban, hedef=user)
    embed = discord.Embed(
        title="ye Banland",
        description=f"{user.mention} sunucudan yasakland.",
        color=RENKLER["ban"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Kullanc", value=f"`{user}`", inline=True)
    embed.add_field(name="Kullanc ID", value=f"`{user.id}`", inline=True)
    embed.add_field(name="lemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(guild, "ban_log", embed)
    await _guvenlik_eylem_isle(guild, sorumlu, "ban", f"{user} ({user.id})", _guvenlik_ayar_al(guild.id).get("ban_limit", 3))


@bot.event
async def on_member_unban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_log_bul(guild, discord.AuditLogAction.unban, hedef=user)
    embed = discord.Embed(
        title="Ban Kaldrld",
        description=f"{user.mention} yeniden sunucuya katlabilir.",
        color=RENKLER["unban"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Kullanc", value=f"`{user}`", inline=True)
    embed.add_field(name="Kullanc ID", value=f"`{user.id}`", inline=True)
    embed.add_field(name="lemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(guild, "ban_log", embed)


@bot.event
async def on_member_join(member: discord.Member):
    embed = discord.Embed(title=" Yeni ye Katld", color=RENKLER["giris"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name=" Kullanc",       value=f"{member.mention} `{member}`",         inline=True)
    embed.add_field(name=" Hesap Oluturma", value=member.created_at.strftime("%d.%m.%Y"), inline=True)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(member.guild, "giris_cikis", embed)


@bot.event
async def on_member_remove(member: discord.Member):
    await asyncio.sleep(1)
    sorumlu = await audit_log_bul(member.guild, discord.AuditLogAction.kick, hedef=member)

    if sorumlu:
        embed = discord.Embed(
            title="ye Atld",
            description=f"{member.mention} sunucudan atld.",
            color=RENKLER["mute"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="Kullanc", value=f"`{member}`", inline=True)
        embed.add_field(name="Kullanc ID", value=f"`{member.id}`", inline=True)
        embed.add_field(name="lemi Yapan", value=sorumlu.mention, inline=True)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(member.guild, "mod_log", embed)
        await _guvenlik_eylem_isle(member.guild, sorumlu, "kick", f"{member} ({member.id})", _guvenlik_ayar_al(member.guild.id).get("kick_limit", 3))
    else:
        embed = discord.Embed(
            title="ye Ayrld",
            description=f"{member.mention} sunucudan ayrld.",
            color=RENKLER["cikis"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="Kullanc", value=f"`{member}`", inline=True)
        embed.add_field(name="Kullanc ID", value=f"`{member.id}`", inline=True)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(member.guild, "giris_cikis", embed)


# 
#  OLAYLAR  ROL ZN DEKL LOGU
# 

@bot.event
async def on_guild_role_update(onceki: discord.Role, sonraki: discord.Role):
    """
    Bir rol gncellendiinde tetiklenir.

    zin deiikliklerini tespit eder:
        1. izin_farklarini_bul() ile eklenen/kaldrlan izinleri hesaplar.
        2. Audit log'dan deiiklii yapan kiiyi bulur.
        3. Estetik bir embed oluturup rol_log kanalna gnderir.
    """

    #  1. zin farklarn hesapla 
    eklenenler, kaldirlanlar = izin_farklarini_bul(onceki.permissions, sonraki.permissions)

    # zin deiiklii yoksa dier deiiklikleri kontrol et (isim, renk vb.)
    if not eklenenler and not kaldirlanlar:
        degisiklikler = []
        if onceki.name  != sonraki.name:  degisiklikler.append(f" sim: `{onceki.name}`  `{sonraki.name}`")
        if onceki.color != sonraki.color: degisiklikler.append(f" Renk: `{onceki.color}`  `{sonraki.color}`")
        if onceki.hoist != sonraki.hoist: degisiklikler.append(f" Ayr Gster: `{onceki.hoist}`  `{sonraki.hoist}`")

        if not degisiklikler:
            return  # Hibir deiiklik yok

        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.role_update, hedef=sonraki)
        embed = discord.Embed(
            title=f" Rol Gncellendi  {sonraki.name}",
            color=sonraki.color.value or RENKLER["rol"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name=" Deiiklikler",  value="\n".join(degisiklikler),                     inline=False)
        embed.add_field(name=" lemi Yapan",   value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "rol_log", embed)
        return

    #  2. Audit log'dan sorumluyu bul 
    await asyncio.sleep(0.5)  # Audit log'un gncellenmesi iin ksa bekleme
    sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.role_update, hedef=sonraki)

    #  3. zin deiiklii embedini olutur 
    embed = discord.Embed(
        title=f" Rol zinleri Deiti  {sonraki.name}",
        description=(
            f"**{sonraki.mention}** rolnn izinleri gncellendi.\n"
            f"**{len(eklenenler)}** izin eklendi  **{len(kaldirlanlar)}** izin kaldrld."
        ),
        color=RENKLER["izin"],
        timestamp=datetime.now(timezone.utc)
    )

    # Eklenen izinler (yeil )
    if eklenenler:
        embed.add_field(
            name=" Eklenen zinler",
            value="\n".join(f"`+` {izin}" for izin in eklenenler),
            inline=True
        )

    # Kaldrlan izinler (krmz )
    if kaldirlanlar:
        embed.add_field(
            name=" Kaldrlan zinler",
            value="\n".join(f"`-` {izin}" for izin in kaldirlanlar),
            inline=True
        )

    # ki stun varsa hizalama iin bo alan
    if eklenenler and kaldirlanlar:
        embed.add_field(name="\u200b", value="\u200b", inline=True)

    # Toplam izin says zeti
    eski_toplam = sum(1 for _, v in onceki.permissions if v)
    yeni_toplam = sum(1 for _, v in sonraki.permissions if v)
    fark = yeni_toplam - eski_toplam

    embed.add_field(
        name=" zin zeti",
        value=(
            f"nceki: `{eski_toplam}` aktif\n"
            f"imdiki: `{yeni_toplam}` aktif\n"
            f"Fark: `{'+' if fark >= 0 else ''}{fark}`"
        ),
        inline=True
    )
    embed.add_field(name=" Yapan",  value=sorumlu.mention if sorumlu else " Bilinmiyor", inline=True)
    embed.add_field(name=" Rol ID", value=f"`{sonraki.id}`",                                inline=True)
    embed.set_footer(text=zaman_damgasi())

    await log_gonder(sonraki.guild, "rol_log", embed)


# 
#  OLAYLAR  MESAJ LOGLARI
# 

@bot.event
async def on_message_delete(message: discord.Message):
    if message.author.bot:
        return

    embed = discord.Embed(
        title="Mesaj Silindi",
        description="Bir mesaj kanaldan kaldrld.",
        color=RENKLER["mesaj"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Yazar", value=f"{message.author.mention}  `{message.author.id}`", inline=True)
    embed.add_field(name="Kanal", value=message.channel.mention, inline=True)
    embed.add_field(name="Mesaj ID", value=f"`{message.id}`", inline=True)
    embed.add_field(name="erik", value=message.content[:1024] or "*[Bo mesaj veya sadece medya]*", inline=False)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(message.guild, "mesaj_log", embed)


@bot.event
async def on_message_edit(onceki: discord.Message, sonraki: discord.Message):
    if onceki.author.bot or onceki.content == sonraki.content:
        return

    embed = discord.Embed(
        title="Mesaj Dzenlendi",
        description=f"[Mesaja git]({sonraki.jump_url})",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Yazar", value=f"{sonraki.author.mention}  `{sonraki.author.id}`", inline=True)
    embed.add_field(name="Kanal", value=sonraki.channel.mention, inline=True)
    embed.add_field(name="Mesaj ID", value=f"`{sonraki.id}`", inline=True)
    embed.add_field(name="Eski Mesaj", value=onceki.content[:512] or "", inline=False)
    embed.add_field(name="Yeni Mesaj", value=sonraki.content[:512] or "", inline=False)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(sonraki.guild, "mesaj_log", embed)


# 
#  OLAYLAR  SES KANALI LOGLARI
# 

@bot.event
async def on_voice_state_update(member: discord.Member, onceki: discord.VoiceState, sonraki: discord.VoiceState):
    if onceki.channel == sonraki.channel:
        return  # Mute/deafen gibi deiiklikleri loglama

    anahtar = (member.guild.id, member.id)
    simdi_ts = time.time()
    baslangic = _SES_OTURUMLARI.get(anahtar)
    if onceki.channel is not None and baslangic is not None:
        _profil_bekleyen_arttir(member.guild.id, member.id, ses_delta=max(0, int(simdi_ts - baslangic)))
        _SES_OTURUMLARI.pop(anahtar, None)
    if sonraki.channel is not None:
        _SES_OTURUMLARI[anahtar] = simdi_ts

    embed = discord.Embed(color=RENKLER["ses"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name=" ye", value=f"{member.mention} `{member}`", inline=False)

    if onceki.channel is None:
        embed.title = " Ses Kanalna Katld"
        embed.add_field(name=" Kanal", value=sonraki.channel.mention, inline=True)
    elif sonraki.channel is None:
        embed.title = " Ses Kanalndan Ayrld"
        embed.add_field(name=" Kanal", value=onceki.channel.mention, inline=True)
    else:
        embed.title = " Ses Kanal Deitirildi"
        embed.add_field(name=" nceki", value=onceki.channel.mention, inline=True)
        embed.add_field(name=" Yeni",   value=sonraki.channel.mention, inline=True)

    embed.set_footer(text=zaman_damgasi())
    await log_gonder(member.guild, "ses_log", embed)


# 
#  OLAYLAR  TIMEOUT (ZAMAN ASIMI) LOGU
# 

@bot.event
async def on_member_update(onceki: discord.Member, sonraki: discord.Member):
    """
    Bu event hem rol deiikliklerini hem de timeout deiikliklerini yakalar.
    kisini birden burada handle ediyoruz.

    NOT: Rol deiiklii iin yukarda ayr bir on_member_update var,
    ama discord.py'de ayn event'i iki kez tanmlayamazsnz.
    Bu yzden rol + timeout kontrol tek fonksiyonda birletirildi.
    Eer nceki on_member_update varsa onu SLP bununla DETRN.
    """

    #  Timeout (Zaman Am) Kontrol 
    # timed_out_until: None ise timeout yok, datetime ise aktif timeout
    eski_timeout = onceki.timed_out_until
    yeni_timeout = sonraki.timed_out_until

    if eski_timeout != yeni_timeout:
        await asyncio.sleep(0.5)
        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.member_update, hedef=sonraki)

        if yeni_timeout is not None:
            # Timeout uyguland
            bitis = yeni_timeout.strftime("%d.%m.%Y %H:%M UTC")
            embed = discord.Embed(
                title=" Zaman Am Uyguland (Timeout)",
                color=RENKLER["mute"],
                timestamp=datetime.now(timezone.utc)
            )
            embed.add_field(name=" ye",            value=f"{sonraki.mention} `{sonraki}`",                inline=True)
            embed.add_field(name=" lemi Yapan",   value=sorumlu.mention if sorumlu else " Bilinmiyor", inline=True)
            embed.add_field(name=" Biti Zaman",   value=f"`{bitis}`",                                    inline=False)
            embed.set_thumbnail(url=sonraki.display_avatar.url)
            embed.set_footer(text=zaman_damgasi())
            await log_gonder(sonraki.guild, "mute_log", embed)

        else:
            # Timeout kaldrld (erken veya sre doldu)
            embed = discord.Embed(
                title=" Zaman Am Kaldrld",
                color=RENKLER["unban"],
                timestamp=datetime.now(timezone.utc)
            )
            embed.add_field(name=" ye",           value=f"{sonraki.mention} `{sonraki}`",                inline=True)
            embed.add_field(name=" lemi Yapan",  value=sorumlu.mention if sorumlu else " Otomatik",  inline=True)
            embed.set_thumbnail(url=sonraki.display_avatar.url)
            embed.set_footer(text=zaman_damgasi())
            await log_gonder(sonraki.guild, "mute_log", embed)

    #  Rol Deiiklii Kontrol 
    eski_roller = set(onceki.roles)
    yeni_roller = set(sonraki.roles)

    eklenen_roller   = yeni_roller - eski_roller
    cikarilan_roller = eski_roller - yeni_roller

    if not eklenen_roller and not cikarilan_roller:
        return

    await asyncio.sleep(0.5)
    sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.member_role_update, hedef=sonraki)

    if eklenen_roller:
        embed = discord.Embed(title=" yeye Rol Eklendi", color=RENKLER["giris"], timestamp=datetime.now(timezone.utc))
        embed.add_field(name=" ye",           value=f"{sonraki.mention} `{sonraki}`",                inline=True)
        embed.add_field(name=" lemi Yapan",  value=sorumlu.mention if sorumlu else " Bilinmiyor", inline=True)
        embed.add_field(
            name=f" Eklenen Rol{'ler' if len(eklenen_roller) > 1 else ''}",
            value="\n".join(r.mention for r in eklenen_roller),
            inline=False
        )
        embed.set_thumbnail(url=sonraki.display_avatar.url)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "rol_log", embed)

    if cikarilan_roller:
        embed = discord.Embed(title=" yeden Rol karld", color=RENKLER["cikis"], timestamp=datetime.now(timezone.utc))
        embed.add_field(name=" ye",           value=f"{sonraki.mention} `{sonraki}`",                inline=True)
        embed.add_field(name=" lemi Yapan",  value=sorumlu.mention if sorumlu else " Bilinmiyor", inline=True)
        embed.add_field(
            name=f" karlan Rol{'ler' if len(cikarilan_roller) > 1 else ''}",
            value="\n".join(r.mention for r in cikarilan_roller),
            inline=False
        )
        embed.set_thumbnail(url=sonraki.display_avatar.url)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "rol_log", embed)


# 
#  OLAYLAR  DAVETYE LOGLARI
# 

@bot.event
async def on_invite_create(invite: discord.Invite):
    """Yeni bir davet balants oluturulduunda tetiklenir."""
    embed = discord.Embed(
        title="Yeni Davet Oluturuldu",
        description="Sunucuda yeni bir davet balants retildi.",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Oluturan", value=invite.inviter.mention if invite.inviter else "Bilinmiyor", inline=True)
    embed.add_field(name="Kanal", value=invite.channel.mention if invite.channel else "", inline=True)
    embed.add_field(name="Davet Kodu", value=f"`{invite.code}`", inline=True)

    # Kullanm limiti: 0 = snrsz
    kullanim = str(invite.max_uses) if invite.max_uses else "Snrsz"
    embed.add_field(name="Kullanm Limiti", value=kullanim, inline=True)

    # Sre: 0 = hi dolmaz
    if invite.max_age:
        sure = f"{invite.max_age // 3600} saat" if invite.max_age >= 3600 else f"{invite.max_age // 60} dakika"
    else:
        sure = "Sresiz"
    embed.add_field(name="Geerlilik", value=sure, inline=True)
    embed.add_field(name="URL", value=f"discord.gg/{invite.code}", inline=True)

    embed.set_footer(text=zaman_damgasi())
    await log_gonder(invite.guild, "davet_log", embed)


@bot.event
async def on_invite_delete(invite: discord.Invite):
    """Bir davet balants silindiinde tetiklenir."""
    embed = discord.Embed(
        title="Davet Silindi",
        description="Bir davet balants kaldrld.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Davet Kodu", value=f"`{invite.code}`", inline=True)
    embed.add_field(name="Kanal", value=invite.channel.mention if invite.channel else "", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(invite.guild, "davet_log", embed)


# 
#  OLAYLAR  KANAL LOGLARI
# 

@bot.event
async def on_guild_channel_create(kanal: discord.abc.GuildChannel):
    """Yeni bir kanal oluturulduunda tetiklenir."""
    sorumlu = await audit_log_bul(kanal.guild, discord.AuditLogAction.channel_create, hedef=kanal)

    # Kanal trn belirle
    tur_simge = {
        discord.TextChannel:     " Metin Kanal",
        discord.VoiceChannel:    " Ses Kanal",
        discord.CategoryChannel: " Kategori",
        discord.ForumChannel:    " Forum Kanal",
        discord.StageChannel:    " Sahne Kanal",
    }.get(type(kanal), " Kanal")

    embed = discord.Embed(
        title="Kanal Oluturuldu",
        description=f"Yeni bir kanal ald: **{kanal.name}**",
        color=RENKLER["giris"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Kanal", value=kanal.mention if hasattr(kanal, "mention") else f"`{kanal.name}`", inline=True)
    embed.add_field(name="Tr", value=tur_simge, inline=True)
    embed.add_field(name="lemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.add_field(name="Kanal ID", value=f"`{kanal.id}`", inline=True)

    # Kategorisi varsa gster
    if hasattr(kanal, "category") and kanal.category:
        embed.add_field(name="Kategori", value=kanal.category.name, inline=True)

    embed.set_footer(text=zaman_damgasi())
    await log_gonder(kanal.guild, "kanal_log", embed)
    await _guvenlik_eylem_isle(kanal.guild, sorumlu, "kanal_acma", f"{kanal.name} ({kanal.id})", _guvenlik_ayar_al(kanal.guild.id).get("kanal_limit", 3))


@bot.event
async def on_guild_channel_delete(kanal: discord.abc.GuildChannel):
    """Bir kanal silindiinde tetiklenir."""
    sorumlu = await audit_log_bul(kanal.guild, discord.AuditLogAction.channel_delete, hedef=kanal)

    tur_simge = {
        discord.TextChannel:     " Metin Kanal",
        discord.VoiceChannel:    " Ses Kanal",
        discord.CategoryChannel: " Kategori",
        discord.ForumChannel:    " Forum Kanal",
        discord.StageChannel:    " Sahne Kanal",
    }.get(type(kanal), " Kanal")

    embed = discord.Embed(
        title="Kanal Silindi",
        description=f"Bir kanal kaldrld: **{kanal.name}**",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Kanal", value=f"`{kanal.name}`", inline=True)
    embed.add_field(name="Tr", value=tur_simge, inline=True)
    embed.add_field(name="lemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.add_field(name="Kanal ID", value=f"`{kanal.id}`", inline=True)

    if hasattr(kanal, "category") and kanal.category:
        embed.add_field(name="Kategori", value=kanal.category.name, inline=True)

    embed.set_footer(text=zaman_damgasi())
    await log_gonder(kanal.guild, "kanal_log", embed)
    await _guvenlik_eylem_isle(kanal.guild, sorumlu, "kanal_silme", f"{kanal.name} ({kanal.id})", _guvenlik_ayar_al(kanal.guild.id).get("kanal_sil_limit", 3))


@bot.event
async def on_guild_role_create(rol: discord.Role):
    sorumlu = await audit_log_bul(rol.guild, discord.AuditLogAction.role_create, hedef=rol)

    embed = discord.Embed(
        title="Rol Oluturuldu",
        description=f"Yeni rol: {rol.mention}",
        color=RENKLER["giris"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Rol", value=rol.mention, inline=True)
    embed.add_field(name="ID", value=f"`{rol.id}`", inline=True)
    embed.add_field(name="lemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.add_field(name="Renk", value=str(rol.color), inline=True)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(rol.guild, "rol_log", embed)
    await _guvenlik_eylem_isle(rol.guild, sorumlu, "rol_acma", f"{rol.name} ({rol.id})", _guvenlik_ayar_al(rol.guild.id).get("rol_ac_limit", 3))


@bot.event
async def on_guild_role_delete(rol: discord.Role):
    sorumlu = await audit_log_bul(rol.guild, discord.AuditLogAction.role_delete, hedef=rol)

    embed = discord.Embed(
        title="Rol Silindi",
        description=f"Kaldrlan rol: **{rol.name}**",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Rol", value=f"`{rol.name}`", inline=True)
    embed.add_field(name="ID", value=f"`{rol.id}`", inline=True)
    embed.add_field(name="Islemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.add_field(name="Renk", value=str(rol.color), inline=True)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(rol.guild, "rol_log", embed)
    await _guvenlik_eylem_isle(rol.guild, sorumlu, "rol_silme", f"{rol.name} ({rol.id})", _guvenlik_ayar_al(rol.guild.id).get("rol_sil_limit", 3))


def kanal_izin_farklarini_bul(onceki: discord.abc.GuildChannel, sonraki: discord.abc.GuildChannel):
    """
    ki kanal arasndaki izin (overwrite) farklarn bulur.

    Kanal izinleri rol/ye bazl OverwriteType nesneleridir.
    Her overwrite'n allow ve deny listeleri karlatrlr:
        - Yeni eklenmi overwrite   o rol/ye iin yeni izin ayar yaplm
        - Silinmi overwrite        o rol/ye iin izin ayar kaldrlm
        - Deimi overwrite        allow/deny deerleri farkllam

    Dndrr:
        list[str]  okunabilir deiiklik satrlar
    """
    satirlar = []

    eski_ow = dict(onceki.overwrites)   # {rol/ye: PermissionOverwrite}
    yeni_ow = dict(sonraki.overwrites)

    tum_hedefler = set(eski_ow) | set(yeni_ow)

    for hedef in tum_hedefler:
        eski = eski_ow.get(hedef)
        yeni = yeni_ow.get(hedef)

        hedef_adi = f"@{hedef.name}" if hasattr(hedef, 'name') else str(hedef)

        if eski is None and yeni is not None:
            # Yeni overwrite eklendi
            izinler = [izin_adi_getir(p) for p, v in iter(yeni) if v is not None]
            satirlar.append(f" **{hedef_adi}** iin izin ayar eklendi")

        elif eski is not None and yeni is None:
            # Overwrite tamamen silindi
            satirlar.append(f" **{hedef_adi}** iin izin ayar kaldrld")

        else:
            # Her iki tarafta da var, farklar bul
            eklenen_izinler  = []
            kaldirilan_izinler = []
            reddedilen_izinler = []
            red_kaldirilan   = []

            for perm, yeni_deger in iter(yeni):
                eski_deger = getattr(eski, perm, None)
                if eski_deger == yeni_deger:
                    continue

                ad = izin_adi_getir(perm)

                if yeni_deger is True and eski_deger is not True:
                    eklenen_izinler.append(ad)       #  zin verildi
                elif yeni_deger is False and eski_deger is not False:
                    reddedilen_izinler.append(ad)    #  zin reddedildi
                elif yeni_deger is None:
                    if eski_deger is True:
                        kaldirilan_izinler.append(ad)   #  kaldrld  ntr
                    elif eski_deger is False:
                        red_kaldirilan.append(ad)       #  kaldrld  ntr

            if any([eklenen_izinler, kaldirilan_izinler, reddedilen_izinler, red_kaldirilan]):
                satirlar.append(f" **{hedef_adi}** izinleri deiti:")
                if eklenen_izinler:
                    satirlar.append("  `` " + ", ".join(eklenen_izinler))
                if reddedilen_izinler:
                    satirlar.append("  `` " + ", ".join(reddedilen_izinler))
                if kaldirilan_izinler:
                    satirlar.append("  `` Ntre alnd: " + ", ".join(kaldirilan_izinler))
                if red_kaldirilan:
                    satirlar.append("  `` Red kaldrld: " + ", ".join(red_kaldirilan))

    return satirlar


@bot.event
async def on_guild_channel_update(onceki: discord.abc.GuildChannel, sonraki: discord.abc.GuildChannel):
    """
    Bir kanaln ad, ayarlar veya izinleri deitiinde tetiklenir.
    Genel deiiklikler ve izin (overwrite) deiiklikleri ayr embedler olarak gnderilir.
    """

    #  1. Genel ayar deiiklikleri 
    degisiklikler = []

    if onceki.name != sonraki.name:
        degisiklikler.append(f" sim: `{onceki.name}`  `{sonraki.name}`")

    if isinstance(onceki, discord.TextChannel) and isinstance(sonraki, discord.TextChannel):
        if onceki.topic != sonraki.topic:
            eski = onceki.topic or "*(bo)*"
            yeni = sonraki.topic or "*(bo)*"
            degisiklikler.append(f" Konu: `{eski}`  `{yeni}`")
        if onceki.slowmode_delay != sonraki.slowmode_delay:
            degisiklikler.append(f" Yava Mod: `{onceki.slowmode_delay}sn`  `{sonraki.slowmode_delay}sn`")
        if onceki.nsfw != sonraki.nsfw:
            degisiklikler.append(f" NSFW: `{onceki.nsfw}`  `{sonraki.nsfw}`")

    if degisiklikler:
        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.channel_update, hedef=sonraki)
        embed = discord.Embed(
            title=" Kanal Gncellendi",
            color=RENKLER["bilgi"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name=" Kanal",         value=sonraki.mention,                                        inline=True)
        embed.add_field(name=" lemi Yapan",  value=sorumlu.mention if sorumlu else " Bilinmiyor",        inline=True)
        embed.add_field(name=" Deiiklikler", value="\n".join(degisiklikler),                                inline=False)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "kanal_log", embed)

    #  2. zin (overwrite) deiiklikleri 
    izin_satirlari = kanal_izin_farklarini_bul(onceki, sonraki)

    if izin_satirlari:
        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.overwrite_update, hedef=sonraki)

        # Discord embed field deeri max 1024 karakter, uzunsa bl
        parca = ""
        parcalar = []
        for satir in izin_satirlari:
            if len(parca) + len(satir) + 1 > 1000:
                parcalar.append(parca)
                parca = satir
            else:
                parca += ("\n" if parca else "") + satir
        if parca:
            parcalar.append(parca)

        embed = discord.Embed(
            title=" Kanal zinleri Deiti",
            color=RENKLER["izin"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name=" Kanal",        value=sonraki.mention,                                        inline=True)
        embed.add_field(name=" lemi Yapan", value=sorumlu.mention if sorumlu else " Bilinmiyor",        inline=True)

        for i, parca in enumerate(parcalar):
            embed.add_field(
                name=" Deiiklikler" if i == 0 else "\u200b",
                value=parca,
                inline=False
            )

        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "kanal_log", embed)


# 
#  BOT HAZIR OLAYI
# 


@bot.event
async def on_command_error(ctx, error):
    """CommandNotFound ve dier bilinen hatalar sessizce geer."""
    if isinstance(error, commands.CommandNotFound):
        return  # Bilinmeyen komutlar yoksay
    if isinstance(error, PrefixMesajCiftKopya):
        return  # ift bot sreci: ikinci kopya sessizce yoksaylr
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=hata_embedi("Yetki Hatas", "Bu komutu kullanmak iin gerekli yetkiye sahip deilsin."))
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("ye Bulunamad", "Belirttiin ye bulunamad veya sunucuda deil."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("Eksik parametre girdin. Detayl komut listesi iin `.yardm` kullanabilirsin."))


@bot.event
async def on_ready():
    # Slash komutlarn Discord'a senkronize et
    try:
        synced = await bot.tree.sync()
        print(f"   {len(synced)} slash komutu senkronize edildi.")
    except Exception as e:
        print(f"   Komut senkronizasyonu baarsz: {e}")

    #  Sabit log kanallarn settings.json'a ykle 
    # Her bot baladnda DEFAULT_LOG_KANALLARI settings.json'a yazlr.
    # Bylece deploy sonras settings.json silinse bile kanallar kaybolmaz.
    if not getattr(bot, "_persistent_views_registered", False):
        bot.add_view(TicketOpenView())
        bot.add_view(TicketControlView())
        bot._persistent_views_registered = True

    if not getattr(bot, "_renk_panelleri_registered", False):
        for guild in bot.guilds:
            rol_idleri = [rol_id for rol_id in renk_rollari_al(guild.id) if guild.get_role(rol_id)]
            if not rol_idleri:
                continue
            for kayit in renk_panel_mesajlari_al(guild.id):
                mesaj_id = kayit.get("message_id")
                if mesaj_id:
                    bot.add_view(RenkView(guild.id, rol_idleri), message_id=mesaj_id)
        bot._renk_panelleri_registered = True

    if not getattr(bot, "_anime_panelleri_registered", False):
        for guild in bot.guilds:
            rol_idleri = [rol_id for rol_id in anime_rollari_al(guild.id) if guild.get_role(rol_id)]
            if not rol_idleri:
                continue
            for kayit in anime_panel_mesajlari_al(guild.id):
                mesaj_id = kayit.get("message_id")
                if mesaj_id:
                    bot.add_view(AnimeRolViewPersistent(guild.id, rol_idleri, 0), message_id=mesaj_id)
        bot._anime_panelleri_registered = True

    if mongo_aktif_mi() and not getattr(bot, "_prefix_lock_index_ok", False):
        await asyncio.to_thread(_prefix_lock_ttl_index_olustur)
        bot._prefix_lock_index_ok = True

    for guild in bot.guilds:
        def _guncelle(ayarlar):
            gk = str(guild.id)
            if gk not in ayarlar:
                ayarlar[gk] = {}
            for tur, kanal_id in DEFAULT_LOG_KANALLARI.items():
                if guild.get_channel(kanal_id):
                    ayarlar[gk].setdefault(tur, kanal_id)
            if DEFAULT_PARTNER_TEXT_KANALI and guild.get_channel(DEFAULT_PARTNER_TEXT_KANALI):
                ayarlar[gk].setdefault("partner_kanal", DEFAULT_PARTNER_TEXT_KANALI)
            if DEFAULT_PARTNER_LOG_KANALI and guild.get_channel(DEFAULT_PARTNER_LOG_KANALI):
                ayarlar[gk].setdefault("partner_log", DEFAULT_PARTNER_LOG_KANALI)

        ayarlari_guncelle(_guncelle)
    print("   Kanallar yklendi.")

    print("" * 52)
    print(f"   Bot    : {bot.user} ({bot.user.id})")
    print(f"    Surec  : {' | '.join(_bot_surec_log_satirlari())}")
    print(f"   Sunucu : {len(bot.guilds)} adet")
    print(f"    Ayarlar: Supabase={'acik' if supabase_aktif_mi() else 'kapali'} | DosyaFallback={AYAR_DOSYASI}")
    print("" * 52)
    print("  Kullanlabilir slash komutlar:")
    print("    /log-kur <tr> <kanal>   Kanal ata")
    print("    /log-kaldir <tr>        Logu kapat")
    print("    /log-durum               Durumu gr")
    print("    /log-sifirla             Tmn sil")
    print("" * 52)

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="sunucu loglarn "
        )
    )

    if not getattr(bot, "_coklu_surec_izleme_baslatildi", False):
        bot._coklu_surec_izleme_baslatildi = True
        asyncio.create_task(_bot_coklu_surec_izleme_dongusu())
    if not getattr(bot, "_profil_kaydetme_dongusu_baslatildi", False):
        bot._profil_kaydetme_dongusu_baslatildi = True
        asyncio.create_task(_profil_bekleyenleri_kaydet_dongusu())


# 
#  PARTNER SSTEM
# 
#
#  Veri yaps (settings.json iinde):
#  {
#    "guild_id": {
#      "partner_log": kanal_id,           partner log kanal
#      "partners": {
#        "hedef_guild_id": {
#          "guild_name": "Sunucu Ad",
#          "guild_id": 123,
#          "yapan": "kullanici#0000",
#          "yapan_id": 123,
#          "zaman": "2026-03-20T16:00:00",   ISO format
#          "son_partner": "2026-03-20T16:00:00"
#        }
#      }
#    }
#  }
# 

PARTNER_BEKLEME_SURESI = 3600  # saniye (1 saat)


def partner_verisi_al(guild_id: int) -> dict:
    """Bu sunucunun partner verisini dndrr."""
    ayarlar = ayarlari_yukle()
    return ayarlar.get(str(guild_id), {}).get("partners", {})


def partner_gecmisi_al(guild_id: int) -> list[dict]:
    """Bu sunucunun partner ilem gemiini dndrr."""
    ayarlar = ayarlari_yukle()
    gecmis = ayarlar.get(str(guild_id), {}).get("partner_gecmisi", [])
    return gecmis if isinstance(gecmis, list) else []


def partner_kaydet_db(guild_id: int, hedef_guild_id: int, veri: dict):
    """Bir partner kaydn settings.json'a yazar."""
    def _guncelle(ayarlar):
        guild_key = str(guild_id)
        if guild_key not in ayarlar:
            ayarlar[guild_key] = {}
        if "partners" not in ayarlar[guild_key]:
            ayarlar[guild_key]["partners"] = {}
        ayarlar[guild_key]["partners"][str(hedef_guild_id)] = veri

    ayarlari_guncelle(_guncelle)


def partner_gecmisi_ekle(guild_id: int, veri: dict):
    """Partner ilemini gemi listesine ekler."""
    def _guncelle(ayarlar):
        guild_key = str(guild_id)
        if guild_key not in ayarlar:
            ayarlar[guild_key] = {}
        gecmis = ayarlar[guild_key].get("partner_gecmisi", [])
        if not isinstance(gecmis, list):
            gecmis = []
        gecmis.append(veri)
        ayarlar[guild_key]["partner_gecmisi"] = gecmis[-5000:]

    ayarlari_guncelle(_guncelle)


def partner_log_kanali_kaydet(guild_id: int, kanal_id: int):
    """Partner log kanaln kaydeder."""
    def _guncelle(ayarlar):
        guild_key = str(guild_id)
        if guild_key not in ayarlar:
            ayarlar[guild_key] = {}
        ayarlar[guild_key]["partner_log"] = kanal_id

    ayarlari_guncelle(_guncelle)


def partner_log_kanali_al(guild_id: int):
    """Partner log kanal ID'sini dndrr. Settings yoksa sabit deeri kullanr."""
    kayitli = ayarlari_yukle().get(str(guild_id), {}).get("partner_log")
    return kayitli if kayitli else DEFAULT_PARTNER_LOG_KANALI


def partner_istatistik_hesapla(guild_id: int) -> dict:
    """
    Gnlk, haftalk, aylk ve toplam partner saysn hesaplar.

    Mantk:
        - Her partner kaydndaki 'zaman' alan ISO format datetime'dr.
        - u anki zamandan fark hesaplayarak hangi periyoda girdiini belirleriz.
    """
    gecmis = partner_gecmisi_al(guild_id)
    partners = partner_verisi_al(guild_id)
    simdi = datetime.now(timezone.utc).astimezone(YEREL_SAAT_DILIMI)
    bugun = simdi.date()
    bu_hafta = simdi.isocalendar()[:2]
    bu_ay = (simdi.year, simdi.month)

    gunluk = haftalik = aylik = toplam = 0

    kaynak = gecmis if gecmis else list(partners.values())

    for p in kaynak:
        try:
            zaman = utc_datetime_from_iso(p["zaman"]).astimezone(YEREL_SAAT_DILIMI)
        except Exception:
            continue

        if zaman > simdi:
            continue
        toplam += 1

        if zaman.date() == bugun:
            gunluk += 1
        if zaman.isocalendar()[:2] == bu_hafta:
            haftalik += 1
        if (zaman.year, zaman.month) == bu_ay:
            aylik += 1

    return {
        "gunluk": gunluk,
        "haftalik": haftalik,
        "aylik": aylik,
        "toplam": toplam
    }


def partner_sira_bul(guild_id: int) -> int:
    """
    Bu sunucunun toplam partner saysna gre sralamasn dndrr.
    Tm sunucularn toplam partner saylarn karlatrr.
    """
    ayarlar = ayarlari_yukle()
    sayilar = []

    for gid, veri in ayarlar.items():
        if "partners" in veri:
            sayilar.append((gid, len(veri["partners"])))

    # Bykten ke srala
    sayilar.sort(key=lambda x: x[1], reverse=True)

    for i, (gid, _) in enumerate(sayilar, 1):
        if gid == str(guild_id):
            return i
    return 1




#  Partner Slash Komutlar & Mesaj Kontrol 

def partner_kanal_id_al(guild_id: int):
    """Partner text kanal ID'sini dndrr. Settings yoksa sabit deeri kullanr."""
    kayitli = ayarlari_yukle().get(str(guild_id), {}).get("partner_kanal")
    return kayitli if kayitli else DEFAULT_PARTNER_TEXT_KANALI

def partner_log_kanali_al_v2(guild_id: int):
    """Partner log kanal ID'sini dndrr. Settings yoksa sabit deeri kullanr."""
    kayitli = ayarlari_yukle().get(str(guild_id), {}).get("partner_log")
    return kayitli if kayitli else DEFAULT_PARTNER_LOG_KANALI

def partner_kanal_id_kaydet(guild_id: int, kanal_id: int):
    """Partner text kanaln kaydeder."""
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        ayarlar[gk]["partner_kanal"] = kanal_id

    ayarlari_guncelle(_guncelle)

def yetkili_partner_sayisi_guncelle(guild_id: int, yetkili_id: int, yetkili_adi: str):
    """
    Yetkili bazl partner sayacn gnceller.
    Her partnerlik yapldnda ilgili yetkilinin saysn 1 artrr.
    Yap: ayarlar[guild_id]["yetkili_partnerleri"][yetkili_id] = {"ad": ..., "sayi": ...}
    """
    def _guncelle(ayarlar):
        gk = str(guild_id)
        yk = str(yetkili_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        if "yetkili_partnerleri" not in ayarlar[gk]:
            ayarlar[gk]["yetkili_partnerleri"] = {}
        if yk not in ayarlar[gk]["yetkili_partnerleri"]:
            ayarlar[gk]["yetkili_partnerleri"][yk] = {"ad": yetkili_adi, "sayi": 0}
        ayarlar[gk]["yetkili_partnerleri"][yk]["sayi"] += 1
        ayarlar[gk]["yetkili_partnerleri"][yk]["ad"] = yetkili_adi

    ayarlari_guncelle(_guncelle)

def yetkili_siralamasi_al(guild_id: int) -> list:
    """
    Yetkilileri partner saysna gre bykten ke sralar.
    Dndrr: [{"id": ..., "ad": ..., "sayi": ...}, ...]
    """
    ayarlar = ayarlari_yukle()
    veri = ayarlar.get(str(guild_id), {}).get("yetkili_partnerleri", {})
    liste = [{"id": kid, "ad": v["ad"], "sayi": v["sayi"]} for kid, v in veri.items()]
    liste.sort(key=lambda x: x["sayi"], reverse=True)
    return liste


#  Partner Prefix Komutlar 

@bot.command(name="partner-kur")
@commands.has_permissions(manage_guild=True)
async def partner_kur(ctx, text_kanal: discord.TextChannel = None, log_kanal: discord.TextChannel = None):
    """
    .partner-kur #text-kanal #log-kanal
    Partner text ve log kanallarn ayarlar.
    """
    if not text_kanal or not log_kanal:
        await ctx.send(embed=kullanim_embedi("`.partner-kur #text-kanal #log-kanal`"))
        return

    partner_kanal_id_kaydet(ctx.guild.id, text_kanal.id)
    partner_log_kanali_kaydet(ctx.guild.id, log_kanal.id)

    embed = discord.Embed(title=" Partner Kanallar Ayarland", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name=" Partner Text", value=text_kanal.mention, inline=True)
    embed.add_field(name=" Partner Log",  value=log_kanal.mention,  inline=True)
    embed.set_footer(text=f"Ayarlayan: {ctx.author}")
    await ctx.send(embed=embed)
    await text_kanal.send(embed=discord.Embed(
        title=" Partner Kanal Aktif",
        description="Bu kanal partner text kanal olarak ayarland.\nDavet linki iermeyen mesajlar otomatik silinecek.",
        color=RENKLER["basari"]
    ))
    await log_kanal.send(embed=discord.Embed(
        title=" Partner Log Kanal Aktif",
        description="Partner loglar bu kanala gnderilecek.",
        color=RENKLER["basari"]
    ))


@bot.command(name="partner-kapat", aliases=["partner-off", "partnerkapat"])
@commands.has_permissions(manage_guild=True)
async def partner_kapat(ctx):
    """.partner-kapat  Partner sisteminin kanal ayarlarini kapatir."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.setdefault(gk, {})

    onceki_text = sunucu_ayari.pop("partner_kanal", None)
    onceki_log = sunucu_ayari.pop("partner_log", None)
    ayarlari_kaydet(ayarlar)

    text_kanal = ctx.guild.get_channel(onceki_text) if onceki_text else None
    log_kanal = ctx.guild.get_channel(onceki_log) if onceki_log else None

    embed = discord.Embed(
        title="Partner Sistemi Kapatildi",
        description="Partner sistemi devre disi birakildi. Kayitli istatistikler silinmedi.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Eski Text Kanal", value=text_kanal.mention if text_kanal else "Yok", inline=True)
    embed.add_field(name="Eski Log Kanal", value=log_kanal.mention if log_kanal else "Yok", inline=True)
    embed.set_footer(text=f"Kapatan: {ctx.author}")
    await ctx.send(embed=embed)


@bot.command(name="partner-istatistik", aliases=["p-istat", "pistat"])
@commands.has_permissions(manage_guild=True)
async def partner_istatistik(ctx):
    """.partner-istatistik  Sunucunun partner istatistiklerini gsterir."""
    stats = partner_istatistik_hesapla(ctx.guild.id)
    sira  = partner_sira_bul(ctx.guild.id)

    embed = discord.Embed(
        title=" Partner statistikleri",
        description=f"**{ctx.guild.name}** sunucusunun partner verileri",
        color=0x57F287,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name=" Sralaman", value=f"**#{sira}**", inline=False)
    embed.add_field(
        name=" Zamana Dayal:",
        value=(
            f" Gnlk: **{stats['gunluk']}**\n"
            f" Haftalk: **{stats['haftalik']}**\n"
            f" Aylk: **{stats['aylik']}**"
        ),
        inline=True
    )
    embed.add_field(name=" Toplam", value=f"**{stats['toplam']}**", inline=True)
    embed.set_footer(text=f"{ctx.bot.user.name}  Partner Sistemi  {zaman_damgasi()}")
    await ctx.send(embed=embed)


@bot.command(name="partner-top", aliases=["p-top", "ptop"])
@commands.has_permissions(manage_guild=True)
async def partner_top(ctx):
    """.partner-top  Yetkililerin partner sralamasn gsterir."""
    siralama = yetkili_siralamasi_al(ctx.guild.id)

    if not siralama:
        await ctx.send(embed=discord.Embed(
            title=" Partner Sralamas",
            description="Henz hi partnerlik kayd yok.",
            color=RENKLER["bilgi"]
        ))
        return

    madalyalar = ["", "", ""]
    satirlar = []
    for i, yetkili in enumerate(siralama[:20], 1):
        madalya = madalyalar[i-1] if i <= 3 else f"`{i}.`"
        satirlar.append(f"{madalya} <@{yetkili['id']}>  **{yetkili['sayi']}** partnerlik")

    embed = discord.Embed(
        title=" Partner Sralamas",
        description="\n".join(satirlar),
        color=0xF1C40F,
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=f"Toplam {len(siralama)} yetkili  {zaman_damgasi()}")
    await ctx.send(embed=embed)


@bot.command(name="partner-liste", aliases=["p-liste", "pliste"])
@commands.has_permissions(manage_guild=True)
async def partner_liste(ctx):
    """.partner-liste  Tm partner sunucularn listeler."""
    partners = partner_verisi_al(ctx.guild.id)
    if not partners:
        await ctx.send(embed=discord.Embed(
            title=" Partner Listesi",
            description="Henz hi partner kayd yok.",
            color=RENKLER["bilgi"]
        ))
        return

    satirlar = []
    for i, (gid, p) in enumerate(partners.items(), 1):
        try:
            zaman = datetime.fromisoformat(p["zaman"]).strftime("%d.%m.%Y")
        except Exception:
            zaman = ""
        satirlar.append(f"`{i}.` **{p['guild_name']}**  {zaman}  <@{p['yapan_id']}>")

    # Sayfalama  her sayfada 10 partner
    sayfalar = [satirlar[i:i+10] for i in range(0, len(satirlar), 10)]

    class SayfaView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=60)
            self.sayfa = 0

        def embed_olustur(self):
            e = discord.Embed(
                title=f" Partner Listesi  Toplam {len(partners)}",
                description="\n".join(sayfalar[self.sayfa]),
                color=0x57F287,
                timestamp=datetime.now(timezone.utc)
            )
            e.set_footer(text=f"Sayfa {self.sayfa+1}/{len(sayfalar)}  {zaman_damgasi()}")
            return e

        @discord.ui.button(label="", style=discord.ButtonStyle.secondary)
        async def geri(self, interaction: discord.Interaction, button: discord.ui.Button):
            if self.sayfa > 0:
                self.sayfa -= 1
            await interaction.response.edit_message(embed=self.embed_olustur(), view=self)

        @discord.ui.button(label="", style=discord.ButtonStyle.secondary)
        async def ileri(self, interaction: discord.Interaction, button: discord.ui.Button):
            if self.sayfa < len(sayfalar) - 1:
                self.sayfa += 1
            await interaction.response.edit_message(embed=self.embed_olustur(), view=self)

    view = SayfaView()
    await ctx.send(embed=view.embed_olustur(), view=view if len(sayfalar) > 1 else None)


@bot.command(name="partner-sifirla", aliases=["p-sifirla"])
@commands.has_permissions(administrator=True)
async def partner_sifirla(ctx):
    """.partner-sifirla  Tm partner kaytlarn siler (onay butonu ile)."""

    class OnayView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=30)

        @discord.ui.button(label=" Evet, Sfrla", style=discord.ButtonStyle.danger)
        async def onayla(self, interaction: discord.Interaction, button: discord.ui.Button):
            ayarlar = ayarlari_yukle()
            gk = str(interaction.guild_id)
            if gk in ayarlar:
                ayarlar[gk].pop("partners", None)
                ayarlar[gk].pop("partner_gecmisi", None)
                ayarlar[gk].pop("yetkili_partnerleri", None)
                ayarlari_kaydet(ayarlar)
            await interaction.response.edit_message(embed=discord.Embed(
                title=" Partner Kaytlar Silindi",
                description="Tm partner kaytlar ve yetkili sralamas silindi.",
                color=RENKLER["hata"]
            ), view=None)

        @discord.ui.button(label=" ptal", style=discord.ButtonStyle.secondary)
        async def iptal(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.edit_message(embed=discord.Embed(
                title=" ptal Edildi",
                description="lem iptal edildi, kaytlar korundu.",
                color=RENKLER["basari"]
            ), view=None)

    await ctx.send(embed=discord.Embed(
        title=" Emin misiniz?",
        description="Tm partner kaytlar ve yetkili sralamas **kalc olarak** silinecek!",
        color=RENKLER["hata"]
    ), view=OnayView())





# 
#  MODERASYON KOMUTLARI (Prefix: !)
# 

@bot.command(name="logkur", aliases=["log-kurulum", "autolog"])
@commands.has_permissions(manage_guild=True)
async def logkur(ctx):
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    if gk not in ayarlar:
        ayarlar[gk] = {}

    bulunanlar = []
    bulunamayanlar = []

    for tur, aciklama in LOG_TURLERI.items():
        kanal = otomatik_log_kanali_bul(ctx.guild, tur)
        if kanal:
            ayarlar[gk][tur] = kanal.id
            bulunanlar.append(f"{aciklama} -> {kanal.mention}")
        else:
            bulunamayanlar.append(aciklama)

    ayarlari_kaydet(ayarlar)

    embed = discord.Embed(
        title="Log Kurulumu Tamamlandi",
        description="Var olan log kanallari otomatik taranip eslestirildi.",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Bulunanlar", value="\n".join(bulunanlar[:10]) if bulunanlar else "Kanal bulunamadi.", inline=False)
    if bulunamayanlar:
        embed.add_field(name="Bulunamayanlar", value="\n".join(bulunamayanlar[:10]), inline=False)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


@logkur.error
async def logkur_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bu komutu kullanmak icin sunucuyu yonet yetkisi gerekli.")


def mod_embed(baslik: str, renk: int, **alanlar) -> discord.Embed:
    """Standart moderasyon embed'i oluturur."""
    embed = discord.Embed(title=baslik, color=renk, timestamp=datetime.now(timezone.utc))
    for ad, deger in alanlar.items():
        embed.add_field(name=ad, value=deger, inline=True)
    embed.set_footer(text=zaman_damgasi())
    return embed


async def hedef_uye_bul(ctx, uye: discord.Member = None):
    if uye is not None:
        return uye
    if ctx.message.reference and ctx.message.reference.message_id:
        try:
            referans = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        except (discord.NotFound, discord.Forbidden, discord.HTTPException):
            referans = None
        if referans and isinstance(referans.author, discord.Member):
            return referans.author
    return None


def kanal_adi_normallestir(ad: str) -> str:
    return ad.lower().replace("_", "-").replace(" ", "-")


def otomatik_log_kanali_bul(guild: discord.Guild, tur: str):
    kaliplar = LOG_KANAL_KALIPLARI.get(tur, [])
    for kanal in guild.text_channels:
        ad = kanal_adi_normallestir(kanal.name)
        if ad in kaliplar:
            return kanal
    for kanal in guild.text_channels:
        ad = kanal_adi_normallestir(kanal.name)
        if any(kalip in ad for kalip in kaliplar):
            return kanal
    return None


#  !ban 
@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    """.ban @ye [sebep]"""
    uye = await hedef_uye_bul(ctx, uye)
    if uye is None:
        await ctx.send(embed=kullanim_embedi("`.ban @uye [sebep]` veya bir mesaja yanit verip `.ban [sebep]`"))
        return
    if uye == ctx.author:
        await ctx.send(" Kendinizi banlayamazsnz."); return
    if uye.top_role >= ctx.author.top_role:
        await ctx.send(" Bu yeyi banlayacak yetkiniz yok."); return

    await uye.ban(reason=f"{ctx.author} tarafndan: {sebep}", delete_message_seconds=0)

    embed = mod_embed(" ye Banland", RENKLER["ban"],
        **{" ye": f"{uye.mention} `{uye}`",
           " Sebep": sebep,
           " Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "ban_log", embed)

    try:
        await uye.send(embed=discord.Embed(
            title=" Sunucudan Banlandnz",
            description=f"**{ctx.guild.name}** sunucusundan banlandnz.\n**Sebep:** {sebep}",
            color=RENKLER["ban"]
        ))
    except discord.Forbidden:
        pass


@ban.error
async def ban_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" Ban yetkine sahip deilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("ye Bulunamad", "Belirttiin ye bulunamad veya sunucuda deil."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("`.ban @ye [sebep]`"))


#  !unban 
@bot.command(name="unban")
@commands.has_permissions(ban_members=True)
async def unban(ctx, kullanici_id: int, *, sebep: str = "Sebep belirtilmedi"):
    """.unban <kullanc_id> [sebep]"""
    try:
        kullanici = await bot.fetch_user(kullanici_id)
        await ctx.guild.unban(kullanici, reason=f"{ctx.author} tarafndan: {sebep}")

        embed = mod_embed(" Ban Kaldrld", RENKLER["unban"],
            **{" Kullanc": f"`{kullanici}`",
               " Sebep": sebep,
               " Yetkili": ctx.author.mention})
        await ctx.send(embed=embed)
        await log_gonder(ctx.guild, "ban_log", embed)

    except discord.NotFound:
        await ctx.send(" Bu ID'ye sahip banl bir kullanc bulunamad.")


@unban.error
async def unban_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" Ban yetkine sahip deilsin.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" Kullanm: ``.unban <kullanc_id> [sebep]`")


#  !kick 
@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    uye = await hedef_uye_bul(ctx, uye)
    if uye is None:
        await ctx.send(embed=kullanim_embedi("`.kick @uye [sebep]` veya bir mesaja yanit verip `.kick [sebep]`"))
        return
    """.kick @ye [sebep]"""
    if uye == ctx.author:
        await ctx.send(" Kendinizi atamazsnz."); return
    if uye.top_role >= ctx.author.top_role:
        await ctx.send(" Bu yeyi atacak yetkiniz yok."); return

    await uye.kick(reason=f"{ctx.author} tarafndan: {sebep}")

    embed = mod_embed(" ye Atld", RENKLER["mute"],
        **{" ye": f"{uye.mention} `{uye}`",
           " Sebep": sebep,
           " Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mod_log", embed)

    try:
        await uye.send(embed=discord.Embed(
            title=" Sunucudan Atldnz",
            description=f"**{ctx.guild.name}** sunucusundan atldnz.\n**Sebep:** {sebep}",
            color=RENKLER["mute"]
        ))
    except discord.Forbidden:
        pass


@kick.error
async def kick_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" Kick yetkine sahip deilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("ye Bulunamad", "Belirttiin ye bulunamad veya sunucuda deil."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("`.kick @ye [sebep]`"))


#  .mute (timeout) 
@bot.command(name="mute")
@commands.has_permissions(moderate_members=True)
async def mute(ctx, uye: discord.Member, *, arguman: str = ""):
    """
    .mute @ye [sre] [sebep]
    Tm argmanlar tek string olarak alr, sonra parse eder.
    Bylece .mute @ye, .mute @ye sebep, .mute @ye 10m sebep hepsi alr.
    """
    if uye == ctx.author:
        await ctx.send(" Kendinizi susturamassnz."); return
    if uye.top_role >= ctx.author.top_role:
        await ctx.send(" Bu yeyi susturacak yetkiniz yok."); return

    birimler = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    parcalar = arguman.strip().split()

    # lk kelime sre formatnda m? (rn: 10m, 2h, 1d, 30s)
    if parcalar and parcalar[0][-1] in birimler and parcalar[0][:-1].isdigit():
        sure_str = parcalar[0]
        saniye = int(sure_str[:-1]) * birimler[sure_str[-1]]
        sebep = " ".join(parcalar[1:]) if len(parcalar) > 1 else "Sebep belirtilmedi"
        sure_goster = sure_str
        if saniye > 2419200:
            await ctx.send(" Maksimum sre 28 gndr."); return
    else:
        # Sre yok  tm argman sebep, sresiz mute
        saniye = 2419200
        sure_goster = "Sresiz"
        sebep = arguman.strip() if arguman.strip() else "Sebep belirtilmedi"

    bitis = datetime.now(timezone.utc) + timedelta(seconds=saniye)
    await uye.timeout(timedelta(seconds=saniye), reason=f"{ctx.author}: {sebep}")

    embed = mod_embed(" ye Susturuldu", RENKLER["mute"],
        **{" ye": f"{uye.mention} `{uye}`",
           " Sre": sure_goster,
           " Biti": bitis.strftime("%d.%m.%Y %H:%M UTC"),
           " Sebep": sebep,
           " Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mute_log", embed)


@mute.error
async def mute_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" Timeout yetkine sahip deilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("ye Bulunamad", "Belirttiin ye bulunamad veya sunucuda deil."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("`.mute @ye [sre] [sebep]`"))


#  !unmute 
@bot.command(name="unmute")
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, uye: discord.Member, *, sebep: str = "Sebep belirtilmedi"):
    """.unmute @ye [sebep]"""
    await uye.timeout(None, reason=f"{ctx.author}: {sebep}")

    embed = mod_embed(" Timeout Kaldrld", RENKLER["unban"],
        **{" ye": f"{uye.mention} `{uye}`",
           " Sebep": sebep,
           " Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mute_log", embed)


@unmute.error
async def unmute_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" Timeout kaldrma yetkine sahip deilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(" ye bulunamad.")


#  !sil 
@bot.command(name="sil")
@commands.has_permissions(manage_messages=True)
async def sil(ctx, adet: int = 5):
    """.sil [adet]  Belirtilen sayda mesaj siler (max 100)"""
    if adet < 1 or adet > 100:
        await ctx.send(" 1 ile 100 arasnda bir say girin."); return

    await ctx.message.delete()
    silinen = await ctx.channel.purge(limit=adet)

    bilgi = await ctx.send(embed=discord.Embed(
        title=" Mesajlar Silindi",
        description=f"**{len(silinen)}** mesaj silindi.",
        color=RENKLER["mesaj"]
    ))
    await asyncio.sleep(3)
    await bilgi.delete()


@sil.error
async def sil_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" Mesaj silme yetkine sahip deilsin.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" Kullanm: ``.sil [adet]`")


#  !warn 
@bot.command(name="warn")
@commands.has_permissions(manage_messages=True)
async def warn(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    uye = await hedef_uye_bul(ctx, uye)
    if uye is None:
        await ctx.send("Kullanim: `.warn @uye [sebep]` veya bir mesaja yanit verip `.warn [sebep]`")
        return
    """.warn @ye [sebep]  yeye uyar verir ve settings.json'a kaydeder."""
    # Uyary kaydet
    ayarlar = ayarlari_yukle()
    guild_key = str(ctx.guild.id)
    if guild_key not in ayarlar:
        ayarlar[guild_key] = {}
    if "uyarilar" not in ayarlar[guild_key]:
        ayarlar[guild_key]["uyarilar"] = {}

    uye_key = str(uye.id)
    if uye_key not in ayarlar[guild_key]["uyarilar"]:
        ayarlar[guild_key]["uyarilar"][uye_key] = []

    kayit = {
        "sebep":    sebep,
        "yetkili":  str(ctx.author),
        "zaman":    datetime.now(timezone.utc).isoformat()
    }
    ayarlar[guild_key]["uyarilar"][uye_key].append(kayit)
    ayarlari_kaydet(ayarlar)

    toplam = len(ayarlar[guild_key]["uyarilar"][uye_key])

    embed = mod_embed(f" Uyar Verildi ({toplam}. uyar)", RENKLER["mesaj"],
        **{" ye": f"{uye.mention} `{uye}`",
           " Sebep": sebep,
           " Toplam Uyar": str(toplam),
           " Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mod_log", embed)

    try:
        await uye.send(embed=discord.Embed(
            title=" Uyar Aldnz",
            description=f"**{ctx.guild.name}** sunucusunda uyarldnz.\n**Sebep:** {sebep}\n**Toplam uyar:** {toplam}",
            color=RENKLER["mesaj"]
        ))
    except discord.Forbidden:
        pass


@warn.error
async def warn_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" Uyar verme yetkine sahip deilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(" ye bulunamad.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" Kullanm: ``.warn @ye [sebep]`")


#  !uyarlar 
@bot.command(name="uyarlar", aliases=["warnings", "uyarilar"])
@commands.has_permissions(manage_messages=True)
async def uyarilar(ctx, uye: discord.Member):
    """.uyarlar @ye  yenin uyar gemiini gsterir."""
    ayarlar = ayarlari_yukle()
    liste = ayarlar.get(str(ctx.guild.id), {}).get("uyarilar", {}).get(str(uye.id), [])

    if not liste:
        await ctx.send(embed=discord.Embed(
            title=f" {uye.display_name}  Uyar Yok",
            description="Bu yenin hi uyars bulunmuyor.",
            color=RENKLER["bilgi"]
        ))
        return

    embed = discord.Embed(
        title=f" {uye.display_name}  {len(liste)} Uyar",
        color=RENKLER["mesaj"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_thumbnail(url=uye.display_avatar.url)

    for i, u in enumerate(liste[-10:], 1):  # Son 10 uyar
        try:
            zaman = datetime.fromisoformat(u["zaman"]).strftime("%d.%m.%Y %H:%M")
        except Exception:
            zaman = ""
        embed.add_field(
            name=f"#{i}  {zaman}",
            value=f"**Sebep:** {u['sebep']}\n**Yetkili:** {u['yetkili']}",
            inline=False
        )

    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


@uyarilar.error
async def uyarilar_hata(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send(" ye bulunamad.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" Kullanm: ``.uyarlar @ye`")


#  !uyarsil 
@bot.command(name="uyarsil", aliases=["uyarisil", "clearwarns"])
@commands.has_permissions(manage_guild=True)
async def uyari_sil(ctx, uye: discord.Member):
    """.uyarsil @ye  yenin tm uyarlarn siler."""
    ayarlar = ayarlari_yukle()
    guild_key = str(ctx.guild.id)
    uye_key = str(uye.id)

    if guild_key in ayarlar and "uyarilar" in ayarlar[guild_key] and uye_key in ayarlar[guild_key]["uyarilar"]:
        del ayarlar[guild_key]["uyarilar"][uye_key]
        ayarlari_kaydet(ayarlar)
        await ctx.send(embed=discord.Embed(
            title=" Uyarlar Silindi",
            description=f"{uye.mention} adl yenin tm uyarlar silindi.",
            color=RENKLER["basari"]
        ))
    else:
        await ctx.send(f" {uye.mention} adl yenin zaten uyars yok.")


#  !yardm 
async def gelismis_yardim(ctx):
    def ana_embed():
        e = discord.Embed(title="Komut Rehberi", description="Bir kategori sec.", color=0x5865F2, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Kategoriler", value="Moderasyon\nPartner\nEglence\nAraclar", inline=False)
        e.set_footer(text=f"{ctx.guild.name}  {zaman_damgasi()}")
        if ctx.guild.icon:
            e.set_thumbnail(url=ctx.guild.icon.url)
        return e

    def mod_kategori():
        e = discord.Embed(title="Moderasyon", color=0xE74C3C, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Uye", value="`.ban @uye [sebep]`  Banlar\n`.unban <id> [sebep]`  Ban kaldirir\n`.kick @uye [sebep]`  Atar\n`.mute @uye [sure] [sebep]`  Susturur\n`.unmute @uye`  Kaldirir", inline=False)
        e.add_field(name="Kanal & Mesaj", value="`.sil [adet]`  Mesaj siler (max 100)\n`.slowmode [sn]`  Yavas mod\n`.duyuru #kanal mesaj`  Duyuru gonderir", inline=False)
        e.add_field(name="Uyari", value="`.warn @uye [sebep]`  Verir\n`.uyarilar @uye`  Gosterir\n`.uyarisil @uye`  Temizler\nMesaja yanit verip `.ban/.kick/.warn` kullanabilirsin.", inline=False)
        return e

    def partner_kategori():
        e = discord.Embed(title="Partner Sistemi", color=0x57F287, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Komutlar", value="`.partner-kur #text #log`  Kanallari ayarlar\n`.partner-istatistik`  Istatistikler\n`.partner-top`  Siralama\n`.partner-liste`  Sunucu listesi\n`.partner-sifirla`  Sifirlar", inline=False)
        e.add_field(name="Nasil calisir?", value="Yetkili kanala partner textini atar\nBot davet linkini kontrol eder\nLink yoksa siler, varsa kaydeder\nAyni sunucu ile 1 saat bekleme var", inline=False)
        return e

    def eglence_kategori():
        e = discord.Embed(title="Eglence & Bilgi", color=0xF1C40F, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Cekilis", value="`.cekilisbaslat [sure] [kisi] [odul]`  Baslatir\n`.cekilisbitir <id>`  Erken bitirir\n`.cekilisyenile <id> [kisi]`  Yeni kazanan\n`.cekiliskatilimci <id>`  Katilimcilari listeler\n`.cekilisbilgi <id>`  Bilgi gosterir\n`.cekilissil <id>`  Iptal eder", inline=False)
        e.add_field(name="AFK", value="`.afk [sebep]`  AFK moduna girer\n Mesaj atinca otomatik cikar\n Etiketlenince AFK bildirilir", inline=False)
        e.add_field(name="Bilgi", value="`.sunucu`  Sunucu istatistikleri", inline=False)
        return e

    def araclar_kategori():
        e = discord.Embed(title="Araclar & Sistemler", color=0x9B59B6, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Ticket - Yonetim", value="`.ticketkur [kategori] #log @rol`  Kurar\n`.ticketpanel`  Panel gonderir\n`.ticketkapat`  Ticketi kapatir\n`.ticketekle @uye`  Uye ekler\n`.ticketcikar @uye`  Uye cikarir", inline=False)
        e.add_field(name="Ticket - Ozellikler", value="`.ticketkonu [konu]`  Konu ayarlar\n`.ticketlist`  Acik ticketlari listeler\n`.ticketsayi`  Toplam ticket sayisi\n`.ticketoncelik [dusuk/orta/yuksek]`  Oncelik belirler\n`.ticketsahip @uye`  Sahibi degistirir\n`.ticketyeniden @uye`  Yeniden acar", inline=False)
        e.add_field(name="Anti-Link", value="`.antilink`  Durum gosterir\n`.antilink ac`  Acar\n`.antilink kapat`  Kapatir\n`.antilink muaf @rol/#kanal`  Muafiyet ekler/kaldirir", inline=False)
        e.add_field(name="Renk Sistemi", value="`.renkekle @rol`  Menuye rol ekler\n`.renkcikar @rol`  Menuden rol cikarir\n`.renklist`  Listedeki rolleri gosterir\n`.renkpanel`  Secim paneli gonderir", inline=False)
        e.add_field(name="Log Sistemi", value="`.logkur`  Otomatik kanal tarar\n`.logkurkanal`  Eksik log kanallarini olusturur\n`/log-kur`  `/log-kaldir`  `/log-durum`  `/log-sifirla`", inline=False)
        e.add_field(name="Level Sistemi", value="`.levelkur`  Modal ile kurulum\n`.levelrol <seviye> @rol`  Rol odulu ekler\n`.levelrolsil <seviye>`  Rol odulunu siler\n`.levelrolleri`  Odulleri listeler\n`.levelmesajtest [@uye]`\n`.leveldurum`  `.seviye [@uye]`", inline=False)
        e.add_field(name="Hosgeldin Sistemi", value="`.hosgeldinkur`  Modal ile kurulum\n`.hosgeldindurum`  Ayarlari gosterir\n`.hosgeldinmesajtest [@uye]`", inline=False)
        return e

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=120)

        @discord.ui.button(label="Moderasyon", style=discord.ButtonStyle.danger)
        async def btn_mod(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=mod_kategori(), view=self)

        @discord.ui.button(label="Partner", style=discord.ButtonStyle.success)
        async def btn_partner(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=partner_kategori(), view=self)

        @discord.ui.button(label="Eglence", style=discord.ButtonStyle.primary)
        async def btn_eglence(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=eglence_kategori(), view=self)

        @discord.ui.button(label="Araclar", style=discord.ButtonStyle.secondary)
        async def btn_araclar(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=araclar_kategori(), view=self)

        @discord.ui.button(label="Ana Menu", style=discord.ButtonStyle.secondary, row=1)
        async def btn_ana(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=ana_embed(), view=self)

    await ctx.send(embed=ana_embed(), view=HelpView())


async def gelismis_yardim_v2(ctx):
    def ana_embed():
        e = discord.Embed(
            title="Komut Rehberi",
            description="Butonlardan bir kategori secip komutlari temiz bir duzende gezebilirsin.",
            color=0x5865F2,
            timestamp=datetime.now(timezone.utc)
        )
        e.add_field(name="Kategoriler", value="Moderasyon\nPartner\nEglence\nAraclar", inline=False)
        e.add_field(name="Hizli Baslangic", value="`.profil`  `.ticketpanel`  `.levelkur`  `.hosgeldinkur`", inline=False)
        e.set_footer(text=f"{ctx.guild.name}  Yardim Menusu")
        if ctx.guild.icon:
            e.set_thumbnail(url=ctx.guild.icon.url)
        return e

    def mod_embed():
        e = discord.Embed(title="Moderasyon", description="Ceza, kanal ve mesaj yonetimi.", color=0xE74C3C, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Uye Islemleri", value="`.ban @uye [sebep]`\n`.unban <id> [sebep]`\n`.kick @uye [sebep]`\n`.mute @uye [sure] [sebep]`\n`.unmute @uye`", inline=False)
        e.add_field(name="Kanal & Mesaj", value="`.sil [adet]`\n`.slowmode [sn]`\n`.duyuru #kanal mesaj`", inline=False)
        e.add_field(name="Uyari", value="`.warn @uye [sebep]`\n`.uyarilar @uye`\n`.uyarisil @uye`\nMesaja yanit verip `.ban`, `.kick`, `.warn` de kullanabilirsin.", inline=False)
        return e

    def partner_embed():
        e = discord.Embed(title="Partner Sistemi", description="Partner kaydi, takip ve siralama komutlari.", color=0x57F287, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Kurulum", value="`.partner-kur #text #log`", inline=False)
        e.add_field(name="Takip", value="`.partner-istatistik`\n`.partner-top`\n`.partner-liste`\n`.partner-sifirla`", inline=False)
        e.add_field(name="Calisma Mantigi", value="Partner kanala gecerli davet linki atilir.\nBot kaydi tutar ve ayni sunucu icin 1 saat bekleme uygular.", inline=False)
        return e

    def eglence_embed():
        e = discord.Embed(title="Eglence & Bilgi", description="Cekilis, AFK ve profil komutlari.", color=0xF1C40F, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Cekilis", value="`.cekilisbaslat [sure] [kisi] [odul]`\n`.cekilisbitir <id>`\n`.cekilisyenile <id> [kisi]`\n`.cekiliskatilimci <id>`\n`.cekilisbilgi <id>`\n`.cekilissil <id>`", inline=False)
        e.add_field(name="AFK", value="`.afk [sebep]`\nMesaj atinca otomatik kapanir\nEtiketlenen AFK uyeler bildirilir", inline=False)
        e.add_field(name="Bilgi", value="`.sunucu`\n`.profil [@uye]`", inline=False)
        return e

    def araclar_embed():
        e = discord.Embed(title="Araclar & Sistemler", description="Kurulum ve sistem komutlari tek yerde.", color=0x9B59B6, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Ticket", value="`.ticketkur [kategori] #log @rol`\n`.ticketpanel`\n`.ticketkapat`  `.ticketekle`  `.ticketcikar`\n`.ticketkonu`  `.ticketlist`  `.ticketsayi`\n`.ticketoncelik`  `.ticketsahip`  `.ticketyeniden`", inline=False)
        e.add_field(name="Log", value="`.logkur`\n`.logkurkanal`\n`/log-kur`  `/log-kaldir`\n`/log-durum`  `/log-sifirla`", inline=False)
        e.add_field(name="Level", value="`.levelkur`\n`.levelrol <seviye> @rol`\n`.levelrolsil <seviye>`\n`.levelrolleri`\n`.levelmesajtest [@uye]`\n`.leveldurum`  `.seviye [@uye]`", inline=False)
        e.add_field(name="Hosgeldin", value="`.hosgeldinkur`\n`.hosgeldindurum`\n`.hosgeldinmesajtest [@uye]`\n`.karsilamakur`\n`.karsilamadurum`\n`.karsilamatest [@uye]`", inline=False)
        e.add_field(name="Diger", value="`.antilink`\n`.antilink ac`\n`.antilink kapat`\n`.antilink muaf @rol/#kanal`\n`.renkekle @rol`  `.renkcikar @rol`\n`.renklist`  `.renkpanel`", inline=False)
        e.set_footer(text="Modal ile kurulan sistemlerde eski setter komutlari kaldirildi")
        return e

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=120)

        @discord.ui.button(label="Moderasyon", style=discord.ButtonStyle.danger)
        async def btn_mod(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=mod_embed(), view=self)

        @discord.ui.button(label="Partner", style=discord.ButtonStyle.success)
        async def btn_partner(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=partner_embed(), view=self)

        @discord.ui.button(label="Eglence", style=discord.ButtonStyle.primary)
        async def btn_eglence(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=eglence_embed(), view=self)

        @discord.ui.button(label="Araclar", style=discord.ButtonStyle.secondary)
        async def btn_araclar(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=araclar_embed(), view=self)

        @discord.ui.button(label="Ana Menu", style=discord.ButtonStyle.secondary, row=1)
        async def btn_ana(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=ana_embed(), view=self)

    await ctx.send(embed=ana_embed(), view=HelpView())


async def gelismis_yardim_v3(ctx):
    def embed_taban(title: str, description: str, color: int) -> discord.Embed:
        e = discord.Embed(
            title=title,
            description=description,
            color=color,
            timestamp=datetime.now(timezone.utc)
        )
        if ctx.guild.icon:
            e.set_thumbnail(url=ctx.guild.icon.url)
        e.set_footer(text=f"{ctx.guild.name}  {zaman_damgasi()}")
        return e

    def ana_embed():
        e = embed_taban(
            "Komut Rehberi",
            "Butonlardan bir kategori sec. Her sayfa daha sade, hizli ve okunakli olacak sekilde duzenlendi.",
            0x5865F2,
        )
        e.add_field(name="Kategoriler", value="`Moderasyon`\n`Partner`\n`Eglence`\n`Araclar`", inline=True)
        e.add_field(name="Hizli Baslangic", value="`.profil`\n`.ticketpanel`\n`.levelkur`\n`.hosgeldinkur`", inline=True)
        e.add_field(name="Kisa Not", value="Modal ile kurulan sistemlerde eski ayar komutlari kaldirildi.", inline=False)
        return e

    def mod_embed():
        e = embed_taban("Moderasyon", "Ceza, kanal ve mesaj yonetimi burada toplanir.", 0xE74C3C)
        e.add_field(name="Uye Islemleri", value="`.ban @uye [sebep]`\n`.unban <id> [sebep]`\n`.kick @uye [sebep]`\n`.mute @uye [sure] [sebep]`\n`.unmute @uye`", inline=False)
        e.add_field(name="Kanal ve Mesaj", value="`.sil [adet]`\n`.slowmode [sn]`\n`.duyuru #kanal mesaj`", inline=False)
        e.add_field(name="Uyari Takibi", value="`.warn @uye [sebep]`\n`.uyarilar @uye`\n`.uyarisil @uye`\nMesaja yanit verip `.ban`, `.kick`, `.warn` da kullanabilirsin.", inline=False)
        return e

    def partner_embed():
        e = embed_taban("Partner Sistemi", "Partner kaydi, takip ve siralama komutlari.", 0x57F287)
        e.add_field(name="Kurulum", value="`.partner-kur #text #log`", inline=False)
        e.add_field(name="Takip ve Rapor", value="`.partner-istatistik`\n`.partner-top`\n`.partner-liste`\n`.partner-kapat`\n`.partner-sifirla`", inline=False)
        e.add_field(name="Calisma Mantigi", value="Partner kanalina gecerli davet linki atilir.\nBot kaydi tutar ve ayni sunucu icin 1 saat bekleme uygular.", inline=False)
        return e

    def eglence_embed():
        e = embed_taban("Eglence ve Bilgi", "Cekilis, AFK ve profil komutlari.", 0xF1C40F)
        e.add_field(name="Cekilis", value="`.cekilisbaslat [sure] [kisi] [odul]`\n`.cekilisbitir <id>`\n`.cekilisyenile <id> [kisi]`\n`.cekiliskatilimci <id>`\n`.cekilisbilgi <id>`\n`.cekilissil <id>`", inline=False)
        e.add_field(name="AFK", value="`.afk [sebep]`\nMesaj atinca otomatik kapanir.\nEtiketlenen AFK uyeler bildirilir.", inline=False)
        e.add_field(name="Bilgi", value="`.sunucu`\n`.profil [@uye]`", inline=False)
        return e

    def araclar_embed():
        e = embed_taban("Araclar ve Sistemler", "Kurulum ve sunucu sistemleri tek yerde.", 0x9B59B6)
        e.add_field(name="Ticket", value="`.ticketkur [kategori] #log @rol [@rol2 ...]`\n`.ticketpanel`\n`.ticketkapat`  `.ticketekle`  `.ticketcikar`\n`.ticketkonu`  `.ticketlist`  `.ticketsayi`\n`.ticketoncelik`  `.ticketsahip`  `.ticketyeniden`", inline=False)
        e.add_field(name="Log", value="`.logkur`\n`.logkurkanal`\n`/log-kur`  `/log-kaldir`\n`/log-durum`  `/log-sifirla`", inline=False)
        e.add_field(name="Level", value="`.levelkur`\n`.levelrol <seviye> @rol`\n`.levelrolsil <seviye>`\n`.levelrolleri`\n`.levelmesajtest [@uye]`\n`.leveldurum`  `.seviye [@uye]`", inline=False)
        e.add_field(name="Hosgeldin", value="`.hosgeldinkur`\n`.hosgeldindurum`\n`.hosgeldinmesajtest [@uye]`", inline=False)
        e.add_field(name=" Guvenlik Sistemleri", value="`.spam-koruma-kur`  Modal ile spam koruma ayarlar\n`.link-koruma-kur`  Modal ile link koruma ayarlar\n`.link-koruma-muaf-rol @rol`  Link muaf rol ekle\n`.link-koruma-muaf-kanal #kanal`  Link muaf kanal ekle\n`.link-koruma-durum`  Link koruma durumu", inline=False)
        e.add_field(name="Diger Sistemler", value="`.antilink`\n`.antilink ac`\n`.antilink kapat`\n`.antilink muaf @rol/#kanal`\n`.renkekle @rol`  `.renkcikar @rol`\n`.renklist`  `.renkpanel`\n`.guvenlikkur`  `.guvenlikdurum`\n`.guvenlikizin @uye/@rol`  `.guvenlikizinsil @uye/@rol`", inline=False)
        return e

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=120)

        @discord.ui.button(label="Moderasyon", style=discord.ButtonStyle.danger)
        async def btn_mod(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=mod_embed(), view=self)

        @discord.ui.button(label="Partner", style=discord.ButtonStyle.success)
        async def btn_partner(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=partner_embed(), view=self)

        @discord.ui.button(label="Eglence", style=discord.ButtonStyle.primary)
        async def btn_eglence(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=eglence_embed(), view=self)

        @discord.ui.button(label="Araclar", style=discord.ButtonStyle.secondary)
        async def btn_araclar(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=araclar_embed(), view=self)

        @discord.ui.button(label="Ana Menu", style=discord.ButtonStyle.secondary, row=1)
        async def btn_ana(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=ana_embed(), view=self)

    await ctx.send(embed=ana_embed(), view=HelpView())


async def _legacy_yardim(ctx):
    if not hasattr(bot, "_help_seen_message_ids"):
        bot._help_seen_message_ids = set()
    if ctx.message.id in bot._help_seen_message_ids:
        return
    bot._help_seen_message_ids.add(ctx.message.id)
    await gelismis_yardim_v3(ctx)

# 
#  BOTU BALAT
# 

    def mod_embed():
        e = discord.Embed(title=" Moderasyon", color=0xE74C3C, timestamp=datetime.now(timezone.utc))
        e.add_field(name="ye", value="`.ban @ye [sebep]`  Banlar\n`.unban <id> [sebep]`  Ban kaldrr\n`.kick @ye [sebep]`  Atar\n`.mute @ye [sre] [sebep]`  Susturur  bo=kalc\n`.unmute @ye`  Kaldrr", inline=False)
        e.add_field(name="Kanal & Mesaj", value="`.sil [adet]`  Mesaj siler (max 100)\n`.slowmode [sn]`  Yava mod  0=kapat\n`.duyuru #kanal mesaj`  Duyuru gnderir", inline=False)
        e.add_field(name="Uyar", value="`.warn @ye [sebep]`  Verir\n`.uyarlar @ye`  Gsterir\n`.uyarsil @ye`  Temizler", inline=False)
        return e

    def partner_embed():
        e = discord.Embed(title=" Partner Sistemi", color=0x57F287, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Komutlar", value="`.partner-kur #text #log`  Kanallar ayarlar\n`.partner-istatistik`  statistikler\n`.partner-top`   Sralama\n`.partner-liste`  Sunucu listesi\n`.partner-sifirla`  Sfrlar", inline=False)
        e.add_field(name="Nasl alr?", value="Yetkili kanala partner textini atar\nBot davet linkini kontrol eder\nLink yoksa siler  Var ise kaydeder\nAyn sunucu ile 1 saat bekleme var", inline=False)
        return e

    def eglence_embed():
        e = discord.Embed(title=" Elence & Bilgi", color=0xF1C40F, timestamp=datetime.now(timezone.utc))
        e.add_field(name="ekili", value="`.cekilisbaslat [sre] [kii] [dl]`  Balatr\n`.cekilisbitir <mesaj_id>`  Erken bitirir", inline=False)
        e.add_field(name="AFK", value="`.afk [sebep]`  AFK moduna girer\n Mesaj atnca otomatik kar\n Etiketlenince AFK bildirilir", inline=False)
        e.add_field(name="Bilgi", value="`.sunucu`  Sunucu istatistikleri", inline=False)
        return e

    def araclar_embed():
        e = discord.Embed(title=" Aralar & Sistemler", color=0x9B59B6, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Ticket", value="`.ticketkur [kategori] #log @rol`  Kurar\n`.ticketpanel`  Panel gnderir", inline=False)
        e.add_field(name="Anti-Link", value="`.antilink`  Durum\n`.antilink ac`  Aar\n`.antilink kapat`  Kapatr\n`.antilink muaf @rol/#kanal`  Muafiyet", inline=False)
        e.add_field(name="Log Sistemi", value="`.logkur`  `.logkurkanal`\n`/log-kur`  `/log-kaldir`  `/log-durum`  `/log-sifirla`", inline=False)
        e.add_field(name="Level Sistemi", value="`.levelkur`  `.levelrol`  `.levelrolsil`  `.levelrolleri`\n`.levelmesajtest`  `.leveldurum`  `.seviye`", inline=False)
        e.add_field(name="Hosgeldin Sistemi", value="`.hosgeldinkur`  `.hosgeldindurum`  `.hosgeldinmesajtest`", inline=False)
        e.add_field(name=" Guvenlik Sistemleri", value="`.spam-koruma-kur`  Modal ile spam koruma ayarlar\n`.link-koruma-kur`  Modal ile link koruma ayarlar\n`.link-koruma-muaf-rol @rol`  Link muaf rol ekle\n`.link-koruma-muaf-kanal #kanal`  Link muaf kanal ekle\n`.link-koruma-durum`  Link koruma durumu", inline=False)
        return e

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=60)

        @discord.ui.button(label=" Moderasyon", style=discord.ButtonStyle.danger)
        async def btn_mod(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=mod_embed(), view=self)

        @discord.ui.button(label=" Partner", style=discord.ButtonStyle.success)
        async def btn_partner(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=partner_embed(), view=self)

        @discord.ui.button(label=" Elence", style=discord.ButtonStyle.primary)
        async def btn_eglence(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=eglence_embed(), view=self)

        @discord.ui.button(label=" Aralar", style=discord.ButtonStyle.secondary)
        async def btn_araclar(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=araclar_embed(), view=self)

        @discord.ui.button(label=" Ana Men", style=discord.ButtonStyle.secondary, row=1)
        async def btn_ana(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=ana_embed(), view=self)

    await ctx.send(embed=ana_embed(), view=HelpView())


# 
#  BOTU BALAT
# 




import re
LINK_REGEX = re.compile(r'https?://\S+|discord\.gg/\S+|www\.\S+', re.IGNORECASE)


@bot.command(name="uygulamakomutkapat", aliases=["appkomutkapat", "uygulamaizinlerinikapat"])
@commands.has_permissions(administrator=True)
async def uygulama_komut_kapat(ctx):
    kanal_sayisi = 0
    kategori_sayisi = 0
    hedef_roller = [rol for rol in ctx.guild.roles if not rol.managed]

    for kanal in ctx.guild.channels:
        if isinstance(kanal, discord.CategoryChannel):
            kategori_sayisi += 1
        else:
            kanal_sayisi += 1
        for rol in hedef_roller:
            overwrite = kanal.overwrites_for(rol)
            overwrite.use_application_commands = False
            overwrite.use_embedded_activities = False
            overwrite.use_external_apps = False
            await kanal.set_permissions(rol, overwrite=overwrite, reason=f"{ctx.author} tarafindan uygulama izinleri kapatildi")

    embed = discord.Embed(
        title="Uygulama Izinleri Kapatildi",
        description="Tum roller icin kanal ve kategorilerde uygulama komutlari, kullanici etkinlikleri ve harici uygulama komutlari kapatildi.",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Rol", value=str(len(hedef_roller)), inline=True)
    embed.add_field(name="Kanal", value=str(kanal_sayisi), inline=True)
    embed.add_field(name="Kategori", value=str(kategori_sayisi), inline=True)
    await ctx.send(embed=embed)


def _yardim_kategori_haritasi():
    return {
        "Ayarlar": {"partner-kur", "partner-kapat", "logkur", "logkurkanal", "ticketkur", "ticketpanel", "levelkur", "levelkapat", "hosgeldinkur", "hosgeldinkapat", "karsilamakur", "karsilamakapat", "guvenlikkur", "guvenlikdurum", "guvenlikkapat", "guvenlikizin", "guvenlikizinsil", "antilink", "uygulamakomutkapat", "gifcevap", "gifcevapdurum", "gifcevapkapat", "jailkur", "jailkapat", "yetkilikufurkur", "yetkilikufurdurum", "yetkilikufurkapat", "kufur-kur", "kufur-durum", "kufur-kapat", "kufur-listele", "kufur-temizle"},
        "Moderasyon": {"ban", "unban", "kick", "mute", "unmute", "sil", "warn", "uyarlar", "uyarsil", "slowmode", "duyuru", "jail", "unjail"},
        "Roller": {"renkekle", "renkcikar", "renklist", "renkpanel", "animerollerikur", "animerollerikaldir", "animerolpanel", "asagitasi", "levelrol", "levelrolsil", "levelrolleri"},
        "Sistemler": {"ticketekle", "ticketcikar", "ticketkapat", "ticketkonu", "ticketlist", "ticketsayi", "ticketoncelik", "ticketsahip", "ticketyeniden", "hosgeldindurum", "hosgeldinmesajtest", "karsilamadurum", "karsilamatest", "leveldurum", "levelmesajtest"},
        "Kullanici": {"profil", "seviye", "sunucu", "afk", "partner-istatistik", "partner-top", "partner-liste", "partner-sifirla"},
        "Eglence": {"cekilisbaslat", "cekilisbitir", "ekilikatlmc", "ekilisil", "ekiliyenile", "ekilibilgi"},
        "Slash": {"log-kur", "log-kaldir", "log-durum", "log-sifirla"},
    }


def _yardim_sistem_haritasi():
    return {
        "Log": {"logkur", "logkurkanal", "log-kur", "log-kaldir", "log-durum", "log-sifirla"},
        "Ticket": {"ticketkur", "ticketpanel", "ticketekle", "ticketcikar", "ticketkapat", "ticketkonu", "ticketlist", "ticketsayi", "ticketoncelik", "ticketsahip", "ticketyeniden"},
        "Partner": {"partner-kur", "partner-kapat", "partner-istatistik", "partner-top", "partner-liste", "partner-sifirla"},
        "Level": {"levelkur", "leveldurum", "levelmesajtest", "seviye", "profil", "levelrol", "levelrolsil", "levelrolleri"},
        "Hosgeldin": {"hosgeldinkur", "hosgeldindurum", "hosgeldinmesajtest", "karsilamakur", "karsilamadurum", "karsilamatest"},
        "Guvenlik": {"guvenlikkur", "guvenlikdurum", "guvenlikkapat", "guvenlikizin", "guvenlikizinsil", "uygulamakomutkapat", "yetkilikufurkur", "yetkilikufurdurum", "yetkilikufurkapat", "kufur-kur", "kufur-durum", "kufur-kapat", "kufur-listele", "kufur-temizle"},
        "Rol Panelleri": {"renkekle", "renkcikar", "renklist", "renkpanel", "animerollerikur", "animerollerikaldir", "animerolpanel", "asagitasi"},
        "Eglence": {"cekilisbaslat", "cekilisbitir", "ekilikatlmc", "ekilisil", "ekiliyenile", "ekilibilgi", "afk"},
        "Moderasyon": {"ban", "unban", "kick", "mute", "unmute", "sil", "warn", "uyarlar", "uyarsil", "slowmode", "duyuru"},
    }


def _yardim_komutlarini_topla():
    prefix_komutlar = {}
    for komut in bot.commands:
        if komut.hidden or komut.name in {"yardm", "yardim", "help"}:
            continue
        prefix_komutlar[komut.name] = komut

    slash_komutlar = {}
    for komut in bot.tree.get_commands():
        slash_komutlar[komut.name] = komut

    kategori_haritasi = _yardim_kategori_haritasi()
    sonuc = {kategori: [] for kategori in kategori_haritasi}
    sonuc["Diger"] = []

    for ad, komut in prefix_komutlar.items():
        kayit = {"ad": ad, "gosterim": f".{ad}", "aciklama": (komut.help or komut.brief or "Prefix komutu").strip(), "aliases": list(getattr(komut, "aliases", []) or [])}
        eklendi = False
        for kategori, adlar in kategori_haritasi.items():
            if ad in adlar:
                sonuc[kategori].append(kayit)
                eklendi = True
                break
        if not eklendi:
            sonuc["Diger"].append(kayit)

    for ad, komut in slash_komutlar.items():
        sonuc["Slash"].append({"ad": ad, "gosterim": f"/{ad}", "aciklama": (getattr(komut, "description", None) or "Slash komutu").strip(), "aliases": []})

    for liste in sonuc.values():
        liste.sort(key=lambda x: x["gosterim"])
    return sonuc


def _yardim_komut_metni(kayitlar):
    satirlar = []
    for kayit in kayitlar:
        alias_metni = f"\nKisayollar: {', '.join(f'.{a}' for a in kayit['aliases'][:3])}" if kayit["aliases"] else ""
        satirlar.append(f"`{kayit['gosterim']}`\n{kayit['aciklama'][:110]}{alias_metni}")
    return satirlar or ["Komut bulunamadi."]


def _yardim_parcalari(satirlar, limit=900):
    parcalar = []
    mevcut = ""
    for satir in satirlar:
        ek = satir + "\n\n"
        if len(mevcut) + len(ek) > limit and mevcut:
            parcalar.append(mevcut.rstrip())
            mevcut = ek
        else:
            mevcut += ek
    if mevcut:
        parcalar.append(mevcut.rstrip())
    return parcalar or ["Komut bulunamadi."]


for _eski in ("yardim", "help", "yardm"):
    try:
        bot.remove_command(_eski)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardm", "help"])
async def yardim(ctx):
    await gelismis_yardim_v3(ctx)

#  AFK yardmc fonksiyonlar 

def afk_kaydet(guild_id: int, user_id: int, sebep: str):
    def _guncelle(ayarlar):
        gk, uk = str(guild_id), str(user_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        if "afk" not in ayarlar[gk]:
            ayarlar[gk]["afk"] = {}
        ayarlar[gk]["afk"][uk] = {"sebep": sebep, "zaman": datetime.now(timezone.utc).isoformat()}

    ayarlari_guncelle(_guncelle)

def afk_sil(guild_id: int, user_id: int):
    def _guncelle(ayarlar):
        gk, uk = str(guild_id), str(user_id)
        if gk in ayarlar and "afk" in ayarlar[gk] and uk in ayarlar[gk]["afk"]:
            del ayarlar[gk]["afk"][uk]

    ayarlari_guncelle(_guncelle)

def afk_al(guild_id: int, user_id: int):
    return ayarlari_yukle().get(str(guild_id), {}).get("afk", {}).get(str(user_id))

#  Anti-link yardmc fonksiyonlar 

def antilink_durum_al(guild_id: int) -> dict:
    return ayarlari_yukle().get(str(guild_id), {}).get("antilink", {"aktif": False, "muaf_roller": [], "muaf_kanallar": []})

def antilink_kaydet(guild_id: int, veri: dict):
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        ayarlar[gk]["antilink"] = veri

    ayarlari_guncelle(_guncelle)

# 
#  PARTNER KANALI  MESAJ KONTROL
# 

import re
DAVET_REGEX = re.compile(r"(?:https?://)?(?:discord\.(?:gg|com)|discordapp\.com)/(?:invite/)?([a-zA-Z0-9_-]+)")
@bot.event
async def on_message(message: discord.Message):
    """
    Partner kanal mesaj kontrol + AFK + Anti-link + prefix komutlar
    """
    if message.author.bot:
        await _prefix_komutlari_isle(message)
        return

    if message.guild:
        #  Partner kanal kontrol 
        partner_ch_id = partner_kanal_id_al(message.guild.id)
        if partner_ch_id and message.channel.id == partner_ch_id:
            eslesen = DAVET_REGEX.search(message.content)

            if not eslesen:
                try:
                    await message.delete()
                except discord.Forbidden:
                    pass
                uyari = await message.channel.send(embed=discord.Embed(
                    title=" Geersiz Partner Metni",
                    description=f"{message.author.mention} Mesajnzda Discord davet linki bulunamad. Mesajnz silindi.",
                    color=RENKLER["hata"]
                ))
                await asyncio.sleep(5)
                try:
                    await uyari.delete()
                except discord.NotFound:
                    pass
                return

            # Davet kodu al
            davet_kodu = eslesen.group(1)
            partners = partner_verisi_al(message.guild.id)
            simdi = datetime.now(timezone.utc)

            # 1 saat bekleme kontrol
            if davet_kodu in partners:
                son_zaman_str = partners[davet_kodu].get("son_partner")
                if son_zaman_str:
                    son_zaman = utc_datetime_from_iso(son_zaman_str)
                    gecen = (simdi - son_zaman).total_seconds()
                    if gecen < PARTNER_BEKLEME_SURESI:
                        kalan = int(PARTNER_BEKLEME_SURESI - gecen)
                        onceki_id = partners[davet_kodu].get("yapan_id")
                        try:
                            await message.delete()
                        except discord.Forbidden:
                            pass
                        uyari = await message.channel.send(embed=discord.Embed(
                            title=" Bekleme Sresi Dolmad",
                            description=(
                                f"{message.author.mention} Bu sunucuyla tekrar partner yapmak iin\n"
                                f"**{kalan // 60} dakika {kalan % 60} saniye** beklemeniz gerekiyor.\n"
                                f"Son partner: <@{onceki_id}> tarafndan yapld."
                            ),
                            color=RENKLER["mute"]
                        ))
                        await asyncio.sleep(7)
                        try:
                            await uyari.delete()
                        except discord.NotFound:
                            pass
                        return

            # Kaydet
            ilk_satir = message.content.strip().split("\n")[0][:50]
            sunucu_adi = ilk_satir if ilk_satir else "Bilinmiyor"
            kayit = {
                "guild_name":  sunucu_adi,
                "guild_id":    davet_kodu,
                "yapan":       str(message.author),
                "yapan_id":    message.author.id,
                "zaman":       simdi.isoformat(),
                "son_partner": simdi.isoformat()
            }
            partner_kaydet_db(message.guild.id, davet_kodu, kayit)
            partner_gecmisi_ekle(message.guild.id, {
                "guild_name": sunucu_adi,
                "guild_id": davet_kodu,
                "yapan": str(message.author),
                "yapan_id": message.author.id,
                "zaman": simdi.isoformat(),
            })

            yetkili_partner_sayisi_guncelle(message.guild.id, message.author.id, str(message.author))

            stats = partner_istatistik_hesapla(message.guild.id)
            sira  = partner_sira_bul(message.guild.id)
            yetkili_liste  = yetkili_siralamasi_al(message.guild.id)
            yetkili_sira   = next((i+1 for i, y in enumerate(yetkili_liste) if y["id"] == str(message.author.id)), "?")
            yetkili_toplam = next((y["sayi"] for y in yetkili_liste if y["id"] == str(message.author.id)), 1)

            stats_embed = discord.Embed(
                title=" Yeni Partner Yapld!",
                description=f"{message.author.mention} yeni bir partnerlik yapt!",
                color=0x57F287,
                timestamp=simdi
            )
            stats_embed.add_field(name=" Sunucu Sras",  value=f"**#{sira}**",                              inline=True)
            stats_embed.add_field(name=" Yetkili Sras", value=f"**#{yetkili_sira}** ({yetkili_toplam} partnerlik)", inline=True)
            stats_embed.add_field(
                name=" Zamana Dayal:",
                value=(
                    f" Gnlk: **{stats['gunluk']}**\n"
                    f" Haftalk: **{stats['haftalik']}**\n"
                    f" Aylk: **{stats['aylik']}**"
                ),
                inline=True
            )
            stats_embed.add_field(name=" Toplam", value=f"**{stats['toplam']}**", inline=True)
            stats_embed.set_footer(text=f"{bot.user.name}  Partner Sistemi")
            if message.guild.icon:
                stats_embed.set_thumbnail(url=message.guild.icon.url)
            await message.channel.send(embed=stats_embed)

            log_kanal_id = partner_log_kanali_al(message.guild.id)
            if log_kanal_id:
                log_kanal = message.guild.get_channel(log_kanal_id)
                if log_kanal:
                    log_embed = discord.Embed(title=" Partner Logu", color=0x57F287, timestamp=simdi)
                    log_embed.add_field(name=" Davet",          value=f"`{davet_kodu}`",                       inline=True)
                    log_embed.add_field(name=" Yapan",          value=message.author.mention,                  inline=True)
                    log_embed.add_field(name=" Zaman",          value=simdi.strftime("%d.%m.%Y %H:%M UTC"),    inline=True)
                    log_embed.add_field(name=" Toplam",         value=str(stats["toplam"]),                    inline=True)
                    log_embed.add_field(name=" Yetkili Toplam", value=str(yetkili_toplam),                   inline=True)
                    log_embed.set_footer(text=zaman_damgasi())
                    await log_kanal.send(embed=log_embed)
            return

        #  AFK kontrol 
        afk_veri = afk_al(message.guild.id, message.author.id)
        if afk_veri and not message.content.startswith(".afk"):
            afk_sil(message.guild.id, message.author.id)
            zaman_afk = utc_datetime_from_iso(afk_veri["zaman"])
            dk = int((datetime.now(timezone.utc) - zaman_afk).total_seconds() // 60)
            uyari = await message.channel.send(embed=discord.Embed(
                title=" AFK Modundan kld",
                description=f"{message.author.mention} AFK modundan kt! ({dk} dakika AFK'dayd)",
                color=RENKLER["giris"]
            ))
            await asyncio.sleep(5)
            try:
                await uyari.delete()
            except discord.NotFound:
                pass
            try:
                if message.author.display_name.startswith("[AFK] "):
                    await message.author.edit(nick=message.author.display_name[6:])
            except discord.Forbidden:
                pass

        # Etiketlenen kii AFK m?
        for etiket in message.mentions:
            afk_bilgi = afk_al(message.guild.id, etiket.id)
            if afk_bilgi:
                await message.channel.send(embed=discord.Embed(
                    description=f" {etiket.mention} u an AFK  **{afk_bilgi['sebep']}**",
                    color=RENKLER["bilgi"]
                ), delete_after=8)

        #  Anti-link kontrol 
        al_veri = antilink_durum_al(message.guild.id)
        if al_veri.get("aktif"):
            muaf_kanallar = al_veri.get("muaf_kanallar", [])
            muaf_roller   = al_veri.get("muaf_roller", [])
            yonetici      = message.author.guild_permissions.manage_messages
            if not message.channel.id in muaf_kanallar and not any(r.id in muaf_roller for r in message.author.roles) and not yonetici:
                if LINK_REGEX.search(message.content):
                    try:
                        await message.delete()
                    except discord.Forbidden:
                        pass
                    uyari = await message.channel.send(embed=discord.Embed(
                        title=" Link Engellendi",
                        description=f"{message.author.mention} Bu kanalda link paylamak yasak!",
                        color=RENKLER["hata"]
                    ))
                    await asyncio.sleep(5)
                    try:
                        await uyari.delete()
                    except discord.NotFound:
                        pass
                    return

        #  Kfr Korumas kontol 
        yasakli_kelimeler = kufur_kelimelerini_al(message.guild.id)
        if yasakli_kelimeler and mesajda_yasakli_kelime_var_mi(message.content, yasakli_kelimeler):
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            uyari = await message.channel.send(embed=discord.Embed(
                title=" Kfr Algland",
                description=f"{message.author.mention} Mesajnzda yasak kelime bulunduu iin silinmitir.",
                color=RENKLER["hata"]
            ))
            await asyncio.sleep(5)
            try:
                await uyari.delete()
            except discord.NotFound:
                pass
            return

    await _prefix_komutlari_isle(message)


# 
#  SLOWMODE
# 

@bot.command(name="slowmode", aliases=["sm", "yavasm"])
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, sure: int = 0):
    if sure < 0 or sure > 21600:
        await ctx.send(" Sre 0-21600 saniye arasnda olmal."); return
    await ctx.channel.edit(slowmode_delay=sure)
    if sure == 0:
        embed = discord.Embed(title=" Yava Mod Kapatld", color=RENKLER["basari"])
    else:
        embed = discord.Embed(title=" Yava Mod Ald", color=RENKLER["mute"])
        embed.add_field(name=" Sre", value=f"{sure} saniye", inline=True)
    embed.add_field(name=" Kanal", value=ctx.channel.mention, inline=True)
    embed.add_field(name=" Yetkili", value=ctx.author.mention, inline=True)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)

@slowmode.error
async def slowmode_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" Kanal ynetme yetkine sahip deilsin.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send(" Kullanm: `.slowmode [saniye]`")


# 
#  DUYURU
# 

@bot.command(name="duyuru", aliases=["announce", "ann"])
@commands.has_permissions(manage_guild=True)
async def duyuru(ctx, kanal: discord.TextChannel = None, *, mesaj: str = None):
    if not mesaj:
        await ctx.send(" Kullanm: `.duyuru #kanal mesajnz`"); return
    hedef = kanal or ctx.channel
    embed = discord.Embed(description=mesaj, color=0xE74C3C, timestamp=datetime.now(timezone.utc))
    embed.set_author(name=f" {ctx.guild.name} Duyurusu", icon_url=ctx.guild.icon.url if ctx.guild.icon else None)
    embed.set_footer(text=f"Duyuran: {ctx.author}")
    await hedef.send("@everyone", embed=embed)
    try: await ctx.message.delete()
    except: pass

@duyuru.error
async def duyuru_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" Sunucu ynetme yetkine sahip deilsin.")


# 
#  SUNUCU STATSTK
# 

@bot.command(name="sunucu", aliases=["server", "serverinfo", "si"])
async def sunucu_bilgi(ctx):
    g = ctx.guild
    insan  = sum(1 for m in g.members if not m.bot)
    botlar = sum(1 for m in g.members if m.bot)
    embed = discord.Embed(title=f" {g.name}", color=0x5865F2, timestamp=datetime.now(timezone.utc))
    if g.icon: embed.set_thumbnail(url=g.icon.url)
    embed.add_field(name=" Sahip",       value=g.owner.mention,                                    inline=True)
    embed.add_field(name=" ID",          value=f"`{g.id}`",                                        inline=True)
    embed.add_field(name=" Kurulu",     value=g.created_at.strftime("%d.%m.%Y"),                  inline=True)
    embed.add_field(name=" Toplam ye",  value=str(g.member_count),                                inline=True)
    embed.add_field(name=" nsan",       value=str(insan),                                         inline=True)
    embed.add_field(name=" Bot",         value=str(botlar),                                        inline=True)
    embed.add_field(name=" Metin Kanal", value=str(len(g.text_channels)),                          inline=True)
    embed.add_field(name=" Ses Kanal",   value=str(len(g.voice_channels)),                         inline=True)
    embed.add_field(name=" Rol",         value=str(len(g.roles) - 1),                             inline=True)
    embed.add_field(name=" Boost",       value=f"{g.premium_subscription_count}  Seviye {g.premium_tier}", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


# 
#  AFK SSTEM
# 

@bot.command(name="afk")
async def afk_cmd(ctx, *, sebep: str = "AFK"):
    afk_kaydet(ctx.guild.id, ctx.author.id, sebep)
    embed = discord.Embed(
        title=" AFK Moduna Geildi",
        description=f"{ctx.author.mention} AFK moduna geti.\n**Sebep:** {sebep}",
        color=RENKLER["bilgi"]
    )
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)
    try:
        await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}"[:32])
    except discord.Forbidden:
        pass


# 
#  EKL SSTEM
# 

import random as _random

@bot.command(name="cekilisbaslat", aliases=["cekilish", "gstart", "giveaway"])
@commands.has_permissions(manage_guild=True)
async def cekilisbaslat(ctx, sure: str = None, kazanan: int = 1, *, odul: str = None):
    if not sure or not odul:
        await ctx.send(" Kullanm: `.cekilisbaslat 1h 1 Nitro`"); return
    birimler = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    try:
        saniye = int(sure[:-1]) * birimler[sure[-1]]
    except (ValueError, KeyError, IndexError):
        await ctx.send(" Geersiz sre. rnek: `10s`, `5m`, `2h`, `1d`"); return
    bitis = datetime.now(timezone.utc) + timedelta(seconds=saniye)
    embed = discord.Embed(
        title=f" EKL  {odul}",
        description=f"Katlmak iin  tepkisini ver!\n\n** Biti:** {bitis.strftime('%d.%m.%Y %H:%M UTC')}\n** Kazanan:** {kazanan} kii\n** dl:** {odul}",
        color=0xFF73FA, timestamp=bitis
    )
    embed.set_footer(text="Biti")
    mesaj = await ctx.send(embed=embed)
    await mesaj.add_reaction("")
    try: await ctx.message.delete()
    except: pass
    await asyncio.sleep(saniye)
    try: mesaj = await ctx.channel.fetch_message(mesaj.id)
    except discord.NotFound: return
    tepki = discord.utils.get(mesaj.reactions, emoji="")
    if not tepki:
        await ctx.send(" Kimse katlmad, ekili iptal."); return
    katilimcilar = [u async for u in tepki.users() if not u.bot]
    if not katilimcilar:
        await ctx.send(" Geerli katlmc yok."); return
    kazananlar  = _random.sample(katilimcilar, min(kazanan, len(katilimcilar)))
    kazanan_str = " ".join(u.mention for u in kazananlar)
    bitis_embed = discord.Embed(
        title=f" EKL SONA ERD  {odul}",
        description=f"** Kazanan:** {kazanan_str}\n** dl:** {odul}\n** Katlmc:** {len(katilimcilar)}",
        color=0xFF73FA, timestamp=datetime.now(timezone.utc)
    )
    await mesaj.edit(embed=bitis_embed)
    await ctx.channel.send(f" Tebrikler {kazanan_str}! **{odul}** kazandnz!")

@cekilisbaslat.error
async def cekilisbaslat_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(" Sunucu ynetme yetkine sahip deilsin.")

@bot.command(name="cekilisbitir", aliases=["gend"])
@commands.has_permissions(manage_guild=True)
async def cekilisbitir(ctx, mesaj_id: int = None):
    if not mesaj_id:
        await ctx.send(" Kullanm: `.cekilisbitir <mesaj_id>`"); return
    try: mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send(" Mesaj bulunamad."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="")
    if not tepki:
        await ctx.send(" Bu mesajda  tepkisi yok."); return
    katilimcilar = [u async for u in tepki.users() if not u.bot]
    if not katilimcilar:
        await ctx.send(" Katlmc yok."); return
    kazanan = _random.choice(katilimcilar)
    await ctx.send(f" Yeni kazanan: {kazanan.mention}!")


#  Ek ekili Komutlar 

@bot.command(name="ekilikatlmc", aliases=["glist", "cekiliskatilimci", "katilimcilar"])
async def cekiliskatilimci(ctx, mesaj_id: int = None):
    """.ekilikatlmc <mesaj_id>  ekili katlmclarn listeler."""
    if not mesaj_id:
        await ctx.send(" Kullanm: `.ekilikatlmc <mesaj_id>`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send(" Mesaj bulunamad."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="")
    katilimcilar = [u async for u in tepki.users() if not u.bot] if tepki else []
    if not katilimcilar:
        await ctx.send(" Henz kimse katlmam."); return
    embed = discord.Embed(
        title=f" ekili Katlmclar  {len(katilimcilar)} kii",
        description="\n".join(f"`{i+1}.` {u.mention}" for i, u in enumerate(katilimcilar[:30])),
        color=0xFF73FA,
        timestamp=datetime.now(timezone.utc)
    )
    if len(katilimcilar) > 30:
        embed.set_footer(text=f"lk 30 gsteriliyor  Toplam: {len(katilimcilar)}")
    else:
        embed.set_footer(text=f"Toplam: {len(katilimcilar)} katlmc")
    await ctx.send(embed=embed)


@bot.command(name="ekilisil", aliases=["gdelete", "cekilissil", "gcancel"])
@commands.has_permissions(manage_guild=True)
async def cekilissil(ctx, mesaj_id: int = None):
    """.ekilisil <mesaj_id>  ekilii iptal eder ve siler."""
    if not mesaj_id:
        await ctx.send(" Kullanm: `.ekilisil <mesaj_id>`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
        await mesaj.delete()
        await ctx.send(embed=discord.Embed(
            title=" ekili ptal Edildi",
            description="ekili mesaj silindi.",
            color=RENKLER["hata"]
        ), delete_after=5)
    except discord.NotFound:
        await ctx.send(" Mesaj bulunamad.")


@bot.command(name="ekiliyenile", aliases=["greroll", "cekilisyenile"])
@commands.has_permissions(manage_guild=True)
async def cekilisyenile(ctx, mesaj_id: int = None, kazanan: int = 1):
    """.ekiliyenile <mesaj_id> [kazanan says]  Yeni kazanan seer."""
    if not mesaj_id:
        await ctx.send(" Kullanm: `.ekiliyenile <mesaj_id> [kazanan says]`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send(" Mesaj bulunamad."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="")
    katilimcilar = [u async for u in tepki.users() if not u.bot] if tepki else []
    if not katilimcilar:
        await ctx.send(" Katlmc yok."); return
    kazananlar = _random.sample(katilimcilar, min(kazanan, len(katilimcilar)))
    kazanan_str = " ".join(u.mention for u in kazananlar)
    embed = discord.Embed(
        title=" ekili Yenilendi!",
        description=f"**Yeni kazanan(lar):** {kazanan_str}",
        color=0xFF73FA,
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)
    await ctx.send(f" Tebrikler {kazanan_str}!")


@bot.command(name="ekilibilgi", aliases=["ginfo", "cekilisbilgi"])
async def cekilisbilgi(ctx, mesaj_id: int = None):
    """.ekilibilgi <mesaj_id>  ekili bilgilerini gsterir."""
    if not mesaj_id:
        await ctx.send(" Kullanm: `.ekilibilgi <mesaj_id>`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send(" Mesaj bulunamad."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="")
    katilimcilar = [u async for u in tepki.users() if not u.bot] if tepki else []
    embed = discord.Embed(
        title=" ekili Bilgileri",
        color=0xFF73FA,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name=" Katlmc", value=str(len(katilimcilar)), inline=True)
    embed.add_field(name=" Oluturma", value=mesaj.created_at.strftime("%d.%m.%Y %H:%M"), inline=True)
    embed.add_field(name=" Mesaj", value=f"[Tkla]({mesaj.jump_url})", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


# 
#  TCKET SSTEM (GELTRLM)
# 

def ticket_ayar_al(guild_id: int) -> dict:
    veri = ayarlari_yukle().get(str(guild_id), {}).get("ticket", {})
    rol_idleri = veri.get("rol_ids")
    if not rol_idleri and veri.get("rol"):
        rol_idleri = [veri.get("rol")]
    veri["rol_ids"] = [rid for rid in (rol_idleri or []) if rid]
    return veri

def ticket_ayar_kaydet(guild_id: int, veri: dict):
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        ayarlar[gk]["ticket"] = veri

    ayarlari_guncelle(_guncelle)

def ticket_sayaci_artir(guild_id: int) -> int:
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        if "ticket" not in ayarlar[gk]:
            ayarlar[gk]["ticket"] = {}
        ayarlar[gk]["ticket"]["sayac"] = ayarlar[gk]["ticket"].get("sayac", 0) + 1
        return ayarlar[gk]["ticket"]["sayac"]

    return ayarlari_guncelle(_guncelle)


def _ticket_sahip_id_kanaldan_al(channel: discord.TextChannel) -> int | None:
    topic = channel.topic or ""
    if " | ID: " not in topic:
        return None
    try:
        kalan = topic.split(" | ID: ", 1)[1]
        return int(kalan.split(" | ", 1)[0].strip())
    except (ValueError, IndexError):
        return None


async def _ticket_transkript_html_olustur(channel: discord.TextChannel) -> io.BytesIO:
    mesajlar = [m async for m in channel.history(limit=None, oldest_first=True)]
    satirlar = []
    for mesaj in mesajlar:
        yazar = html.escape(str(mesaj.author))
        zaman = mesaj.created_at.astimezone(timezone.utc).strftime("%d.%m.%Y %H:%M:%S UTC")
        icerik = html.escape(mesaj.content or "")
        icerik_html = icerik.replace("\n", "<br>")
        ekler = ""
        if mesaj.attachments:
            baglantilar = [f'<a href="{html.escape(a.url)}" target="_blank">{html.escape(a.filename)}</a>' for a in mesaj.attachments]
            ekler = f'<div class="attachments">Ekler: {"  ".join(baglantilar)}</div>'
        if mesaj.embeds and not icerik:
            icerik_html = '<span class="muted">[Embed mesaj]</span>'
        satirlar.append(
            f"""
            <article class="message">
                <div class="avatar"><img src="{html.escape(mesaj.author.display_avatar.url)}" alt="avatar"></div>
                <div class="body">
                    <div class="meta"><strong>{yazar}</strong><span>{zaman}</span></div>
                    <div class="content">{icerik_html or '<span class="muted">[Bos mesaj]</span>'}</div>
                    {ekler}
                </div>
            </article>
            """
        )
    html_icerik = f"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <title>{html.escape(channel.name)} transcript</title>
  <style>
    :root {{ color-scheme: dark; }}
    body {{ margin: 0; font-family: Segoe UI, Arial, sans-serif; background: linear-gradient(180deg, #10131a, #0a0d12); color: #eef2ff; }}
    .wrap {{ max-width: 980px; margin: 0 auto; padding: 32px 20px 60px; }}
    .hero {{ padding: 24px; border: 1px solid #2b3240; border-radius: 20px; background: rgba(18, 24, 34, 0.92); box-shadow: 0 24px 80px rgba(0,0,0,.35); }}
    .hero h1 {{ margin: 0 0 6px; font-size: 28px; }}
    .hero p {{ margin: 0; color: #a9b4c7; }}
    .messages {{ margin-top: 20px; display: grid; gap: 12px; }}
    .message {{ display: grid; grid-template-columns: 56px 1fr; gap: 14px; padding: 16px; border-radius: 18px; background: rgba(17, 22, 31, 0.94); border: 1px solid #232b39; }}
    .avatar img {{ width: 48px; height: 48px; border-radius: 50%; object-fit: cover; }}
    .meta {{ display: flex; gap: 10px; align-items: baseline; flex-wrap: wrap; margin-bottom: 8px; }}
    .meta span {{ color: #90a0b8; font-size: 12px; }}
    .content {{ line-height: 1.6; word-break: break-word; }}
    .attachments {{ margin-top: 10px; color: #9bc1ff; font-size: 14px; }}
    .attachments a {{ color: #8ec5ff; text-decoration: none; }}
    .muted {{ color: #7f8a9b; }}
  </style>
</head>
<body>
  <div class="wrap">
    <section class="hero">
      <h1>#{html.escape(channel.name)} transcript</h1>
      <p>{len(mesajlar)} mesaj  {html.escape(channel.guild.name)}</p>
    </section>
    <section class="messages">
      {''.join(satirlar) if satirlar else '<p class="muted">Bu ticketta mesaj bulunamadi.</p>'}
    </section>
  </div>
</body>
</html>"""
    buffer = io.BytesIO(html_icerik.encode("utf-8"))
    buffer.seek(0)
    return buffer


async def _ticket_kapat_logu_ve_transkript(channel: discord.TextChannel, kapatan: discord.abc.User, log_id: int | None):
    if not log_id:
        return
    log_k = channel.guild.get_channel(log_id)
    if not log_k:
        return
    sahip_id = _ticket_sahip_id_kanaldan_al(channel)
    sahip = channel.guild.get_member(sahip_id) if sahip_id else None
    transcript = await _ticket_transkript_html_olustur(channel)
    dosya = discord.File(transcript, filename=f"{channel.name}-transcript.html")
    e = discord.Embed(
        title="Ticket Kapatildi",
        description=(
            f"**Ticket:** `{channel.name}`\n"
            f"**Sahip:** {sahip.mention if sahip else 'Bilinmiyor'}\n"
            f"**Kapatan:** {kapatan.mention}"
        ),
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    e.set_footer(text="Transcript ekte gonderildi")
    await log_k.send(embed=e, file=dosya)


@bot.command(name="ticketkur", aliases=["ticket-kur"])
@commands.has_permissions(administrator=True)
async def ticket_kur(ctx, kategori: discord.CategoryChannel = None, log: discord.TextChannel = None, *destek_rolleri: discord.Role):
    """
    .ticketkur [kategori] #log-kanal @destek-rol [@destek-rol-2 ...]
    Ticket sistemini kurar.
    """
    if not kategori or not log or not destek_rolleri:
        await ctx.send(embed=kullanim_embedi("`.ticketkur [kategori] #log-kanal @destek-rol [@destek-rol-2 ...]`")); return

    destek_rolleri = list(dict.fromkeys(rol.id for rol in destek_rolleri if rol))
    if not destek_rolleri:
        await ctx.send(embed=hata_embedi("Destek Rol Gerekli", "Ticket sistemi iin en az bir destek rol belirtmelisin."))
        return

    mevcut = ticket_ayar_al(ctx.guild.id)
    mevcut.update({"kategori": kategori.id, "log": log.id, "rol_ids": destek_rolleri, "rol": destek_rolleri[0]})
    ticket_ayar_kaydet(ctx.guild.id, mevcut)

    embed = discord.Embed(title=" Ticket Sistemi Kuruldu", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name=" Kategori",    value=kategori.name,      inline=True)
    embed.add_field(name=" Log",         value=log.mention,         inline=True)
    destek_rol_mentionlari = [ctx.guild.get_role(rid).mention for rid in destek_rolleri if ctx.guild.get_role(rid)]
    embed.add_field(name=" Destek Rolleri", value=", ".join(destek_rol_mentionlari) if destek_rol_mentionlari else "Yok", inline=False)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


@bot.command(name="ticketpanel", aliases=["ticket-panel"])
@commands.has_permissions(administrator=True)
async def ticket_panel(ctx):
    """.ticketpanel  Ticket ama paneli gnderir."""
    ayar = ticket_ayar_al(ctx.guild.id)
    if not ayar.get("kategori"):
        await ctx.send(" nce `.ticketkur` ile sistemi kur."); return

    class TicketView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label=" Ticket A", style=discord.ButtonStyle.primary, custom_id="global_ticket_ac")
        async def ticket_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
            ayar        = ticket_ayar_al(interaction.guild_id)
            kategori    = interaction.guild.get_channel(ayar.get("kategori"))
            destek_rolleri = [interaction.guild.get_role(rid) for rid in ayar.get("rol_ids", [])]
            destek_rolleri = [rol for rol in destek_rolleri if rol]
            log_id      = ayar.get("log")

            if not kategori:
                await interaction.response.send_message(" Kategori bulunamad. `.ticketkur` ile yeniden kur.", ephemeral=True); return

            # Ak ticket var m kontrol et
            for kanal in kategori.text_channels:
                if kanal.topic and str(interaction.user.id) in kanal.topic:
                    await interaction.response.send_message(f" Zaten ak bir ticketn var: {kanal.mention}", ephemeral=True); return

            # Ticket numaras
            sayi = ticket_sayaci_artir(interaction.guild_id)

            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True),
                interaction.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_channels=True),
            }
            for destek_rolu in destek_rolleri:
                overwrites[destek_rolu] = discord.PermissionOverwrite(read_messages=True, send_messages=True)

            ticket_kanal = await kategori.create_text_channel(
                name=f"ticket-{sayi:04d}",
                overwrites=overwrites,
                topic=f"Ticket sahibi: {interaction.user} | ID: {interaction.user.id} | #{sayi}"
            )

            # Ticket kanal view (kapat + talep al)
            class TicketKontrolView(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=None)

                @discord.ui.button(label=" Kapat", style=discord.ButtonStyle.danger, custom_id=f"ticket_kapat_{ticket_kanal.id}")
                async def kapat(self, i2: discord.Interaction, b: discord.ui.Button):
                    await _ticket_kapat_logu_ve_transkript(ticket_kanal, i2.user, log_id)
                    await i2.response.send_message("Ticket kapatlyor...", ephemeral=True)

                    if False and log_id:
                        log_k = i2.guild.get_channel(log_id)
                        if log_k:
                            await log_k.send(embed=discord.Embed(
                                title=" Ticket Kapatld",
                                description=(
                                    f"**Ticket:** `{ticket_kanal.name}`\n"
                                    f"**Sahip:** {interaction.user.mention}\n"
                                    f"**Kapatan:** {i2.user.mention}"
                                ),
                                color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)
                            ))
                    await ticket_kanal.delete(reason=f"{i2.user} tarafndan kapatld")

                @discord.ui.button(label=" ye Ekle", style=discord.ButtonStyle.secondary, custom_id=f"ticket_uyeekle_{ticket_kanal.id}")
                async def uye_ekle(self, i2: discord.Interaction, b: discord.ui.Button):
                    if destek_rolleri and not any(rol in i2.user.roles for rol in destek_rolleri) and not i2.user.guild_permissions.administrator:
                        await i2.response.send_message(" Bu ilem iin destek rol veya ynetici yetkisi gerekli.", ephemeral=True)
                        return
                    await i2.response.send_message("Eklemek istediin kullancy etiketle: (rn: @kullanc)", ephemeral=True)

                    def check(m):
                        return m.author == i2.user and m.channel == ticket_kanal and m.mentions

                    try:
                        yanit = await bot.wait_for("message", check=check, timeout=30)
                        for uye in yanit.mentions:
                            await ticket_kanal.set_permissions(uye, read_messages=True, send_messages=True)
                        await ticket_kanal.send(f" {' '.join(u.mention for u in yanit.mentions)} ticketa eklendi.")
                        await yanit.delete()
                    except asyncio.TimeoutError:
                        pass

                @discord.ui.button(label=" Talep Al", style=discord.ButtonStyle.success, custom_id=f"ticket_talep_{ticket_kanal.id}")
                async def talep_al(self, i2: discord.Interaction, b: discord.ui.Button):
                    if destek_rolleri and not any(rol in i2.user.roles for rol in destek_rolleri) and not i2.user.guild_permissions.administrator:
                        await i2.response.send_message(" Bu ilem iin destek rol gerekli.", ephemeral=True); return
                    await ticket_kanal.edit(topic=f"{ticket_kanal.topic} | Talep: {i2.user}")
                    await i2.response.send_message(f" Ticket {i2.user.mention} tarafndan talep alnd.")

            ac_embed = discord.Embed(
                title=f" Ticket #{sayi:04d}",
                description=(
                    f"Merhaba {interaction.user.mention}!\n"
                    f"Destek ekibimiz en ksa srede yardmc olacak.\n\n"
                    f"Ticket kapatmak iin  butonunu kullan."
                ),
                color=0x57F287, timestamp=datetime.now(timezone.utc)
            )
            ac_embed.set_footer(text=f"Ticket #{sayi:04d}  {zaman_damgasi()}")

            await ticket_kanal.send(
                content=" ".join([interaction.user.mention] + [rol.mention for rol in destek_rolleri]),
                embed=ac_embed,
                view=TicketKontrolView()
            )
            await interaction.response.send_message(f" Ticketn ald: {ticket_kanal.mention}", ephemeral=True)

            if log_id:
                log_k = interaction.guild.get_channel(log_id)
                if log_k:
                    await log_k.send(embed=discord.Embed(
                        title=" Yeni Ticket Ald",
                        description=f"**Aan:** {interaction.user.mention}\n**Kanal:** {ticket_kanal.mention}\n**Numara:** `#{sayi:04d}`",
                        color=RENKLER["giris"], timestamp=datetime.now(timezone.utc)
                    ))

    panel_embed = discord.Embed(
        title=" Destek Merkezi",
        description="Yardm almak iin aadaki butona tkla.\nEkibimiz en ksa srede sana yardmc olacak.",
        color=0x5865F2
    )
    panel_embed.set_footer(text=ctx.guild.name)
    if ctx.guild.icon:
        panel_embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=panel_embed, view=TicketView())
    try: await ctx.message.delete()
    except: pass


@bot.command(name="ticketekle", aliases=["ticket-ekle"])
@commands.has_permissions(manage_channels=True)
async def ticket_ekle(ctx, uye: discord.Member = None):
    """.ticketekle @ye  Ticket kanalna ye ekler."""
    if not uye:
        await ctx.send(" Kullanm: `.ticketekle @ye`"); return
    await ctx.channel.set_permissions(uye, read_messages=True, send_messages=True)
    await ctx.send(embed=discord.Embed(
        description=f" {uye.mention} ticketa eklendi.",
        color=RENKLER["basari"]
    ))


@bot.command(name="ticketcikar", aliases=["ticket-cikar"])
@commands.has_permissions(manage_channels=True)
async def ticket_cikar(ctx, uye: discord.Member = None):
    """.ticketcikar @ye  Ticket kanalndan ye karr."""
    if not uye:
        await ctx.send(" Kullanm: `.ticketcikar @ye`"); return
    await ctx.channel.set_permissions(uye, read_messages=False)
    await ctx.send(embed=discord.Embed(
        description=f" {uye.mention} tickettan karld.",
        color=RENKLER["hata"]
    ))


@bot.command(name="ticketkapat", aliases=["ticket-kapat"])
@commands.has_permissions(manage_channels=True)
async def ticket_kapat(ctx):
    """.ticketkapat  Mevcut ticket kanaln kapatr."""
    if not ctx.channel.name.startswith("ticket-"):
        await ctx.send(" Bu komut sadece ticket kanallarnda kullanlabilir."); return

    ayar   = ticket_ayar_al(ctx.guild.id)
    log_id = ayar.get("log")
    await _ticket_kapat_logu_ve_transkript(ctx.channel, ctx.author, log_id)

    if False and log_id:
        log_k = ctx.guild.get_channel(log_id)
        if log_k:
            await log_k.send(embed=discord.Embed(
                title=" Ticket Kapatld",
                description=f"**Ticket:** `{ctx.channel.name}`\n**Kapatan:** {ctx.author.mention}",
                color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)
            ))
    await ctx.send("Ticket kapatlyor...")
    await asyncio.sleep(2)
    await ctx.channel.delete(reason=f"{ctx.author} tarafndan kapatld")

# 
#  FLASK (RENDER CANLI TUTMAK N)
# 

def ticket_kategori_kanallari(guild: discord.Guild):
    ayar = ticket_ayar_al(guild.id)
    kategori = guild.get_channel(ayar.get("kategori")) if ayar.get("kategori") else None
    if not kategori:
        return None, []
    return kategori, [kanal for kanal in kategori.text_channels if kanal.name.startswith("ticket-")]


@bot.command(name="ticketkonu", aliases=["ticket-konu"])
@commands.has_permissions(manage_channels=True)
async def ticket_konu(ctx, *, konu: str = None):
    if not ctx.channel.name.startswith("ticket-"):
        await ctx.send("Bu komut sadece ticket kanalinda kullanilabilir.")
        return
    if not konu:
        await ctx.send("Kullanim: `.ticketkonu [konu]`")
        return
    await ctx.channel.edit(name=f"ticket-{konu.lower().replace(' ', '-')[:80]}")
    await ctx.send(f"Ticket konusu guncellendi: `{ctx.channel.name}`")


@bot.command(name="ticketlist", aliases=["ticket-list"])
@commands.has_permissions(manage_channels=True)
async def ticket_list(ctx):
    kategori, kanallar = ticket_kategori_kanallari(ctx.guild)
    if not kategori:
        await ctx.send("Once `.ticketkur` ile ticket sistemi kurulmali.")
        return
    if not kanallar:
        await ctx.send("Acik ticket yok.")
        return
    satirlar = [f"{kanal.mention} - `{kanal.name}`" for kanal in kanallar[:20]]
    embed = discord.Embed(title="Acik Ticketlar", description="\n".join(satirlar), color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.set_footer(text=f"Toplam: {len(kanallar)}")
    await ctx.send(embed=embed)


@bot.command(name="ticketsayi", aliases=["ticket-sayi"])
@commands.has_permissions(manage_channels=True)
async def ticket_sayi(ctx):
    kategori, kanallar = ticket_kategori_kanallari(ctx.guild)
    if not kategori:
        await ctx.send("Once `.ticketkur` ile ticket sistemi kurulmali.")
        return
    await ctx.send(f"Aktif ticket sayisi: **{len(kanallar)}**")


@bot.command(name="ticketoncelik", aliases=["ticket-oncelik"])
@commands.has_permissions(manage_channels=True)
async def ticket_oncelik(ctx, seviye: str = None):
    if not ctx.channel.name.startswith("ticket-"):
        await ctx.send("Bu komut sadece ticket kanalinda kullanilabilir.")
        return
    if seviye not in {"dusuk", "orta", "yuksek"}:
        await ctx.send("Kullanim: `.ticketoncelik [dusuk/orta/yuksek]`")
        return
    topic = ctx.channel.topic or ""
    if " | Oncelik:" in topic:
        topic = topic.split(" | Oncelik:")[0]
    await ctx.channel.edit(topic=f"{topic} | Oncelik: {seviye}")
    await ctx.send(f"Ticket onceligi `{seviye}` olarak ayarlandi.")


@bot.command(name="ticketsahip", aliases=["ticket-sahip"])
@commands.has_permissions(manage_channels=True)
async def ticket_sahip(ctx, uye: discord.Member = None):
    if not ctx.channel.name.startswith("ticket-"):
        await ctx.send("Bu komut sadece ticket kanalinda kullanilabilir.")
        return
    if not uye:
        await ctx.send("Kullanim: `.ticketsahip @uye`")
        return
    await ctx.channel.set_permissions(uye, read_messages=True, send_messages=True, attach_files=True)
    topic = ctx.channel.topic or ""
    if " | ID:" in topic:
        ilk = topic.split(" | ID:")[0]
        kalan = topic.split(" | #")[-1] if " | #" in topic else ""
        yeni_topic = f"{ilk.split(':')[0]}: {uye} | ID: {uye.id}"
        if kalan:
            yeni_topic += f" | #{kalan}"
    else:
        yeni_topic = f"Ticket sahibi: {uye} | ID: {uye.id}"
    await ctx.channel.edit(topic=yeni_topic)
    await ctx.send(f"Ticket sahibi {uye.mention} olarak degistirildi.")


@bot.command(name="ticketyeniden", aliases=["ticket-yeniden"])
@commands.has_permissions(manage_channels=True)
async def ticket_yeniden(ctx, uye: discord.Member = None):
    if not uye:
        await ctx.send("Kullanim: `.ticketyeniden @uye`")
        return
    ayar = ticket_ayar_al(ctx.guild.id)
    kategori = ctx.guild.get_channel(ayar.get("kategori")) if ayar.get("kategori") else None
    destek_rolu = ctx.guild.get_role(ayar.get("rol")) if ayar.get("rol") else None
    if not kategori:
        await ctx.send("Once `.ticketkur` ile ticket sistemi kurulmali.")
        return
    sayi = ticket_sayaci_artir(ctx.guild.id)
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        uye: discord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_channels=True),
    }
    if destek_rolu:
        overwrites[destek_rolu] = discord.PermissionOverwrite(read_messages=True, send_messages=True)
    kanal = await kategori.create_text_channel(
        name=f"ticket-{sayi:04d}",
        overwrites=overwrites,
        topic=f"Ticket sahibi: {uye} | ID: {uye.id} | #{sayi}"
    )
    await kanal.send(f"{uye.mention} ticketin yeniden acildi.", view=TicketControlView())
    await ctx.send(f"Yeni ticket olusturuldu: {kanal.mention}")


@bot.command(name="antilink")
@commands.has_permissions(manage_guild=True)
async def antilink(ctx, durum: str = None):
    veri = antilink_durum_al(ctx.guild.id)
    if durum is None:
        durum_yazi = "Acik" if veri.get("aktif") else "Kapali"
        muaf_kanallar = ", ".join(f"<#{kanal_id}>" for kanal_id in veri.get("muaf_kanallar", [])[:10]) or "-"
        muaf_roller = ", ".join(f"<@&{rol_id}>" for rol_id in veri.get("muaf_roller", [])[:10]) or "-"
        embed = discord.Embed(title="Anti-Link Durumu", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
        embed.add_field(name="Durum", value=durum_yazi, inline=True)
        embed.add_field(name="Muaf Kanallar", value=muaf_kanallar, inline=False)
        embed.add_field(name="Muaf Roller", value=muaf_roller, inline=False)
        await ctx.send(embed=embed)
        return

    durum = durum.lower()
    if durum == "ac":
        veri["aktif"] = True
        antilink_kaydet(ctx.guild.id, veri)
        await ctx.send("Anti-link sistemi acildi.")
        return
    if durum == "kapat":
        veri["aktif"] = False
        antilink_kaydet(ctx.guild.id, veri)
        await ctx.send("Anti-link sistemi kapatildi.")
        return
    if durum == "muaf":
        if ctx.message.role_mentions:
            rol = ctx.message.role_mentions[0]
            roller = set(veri.get("muaf_roller", []))
            if rol.id in roller:
                roller.remove(rol.id)
                mesaj = f"{rol.mention} muafiyetten cikarildi."
            else:
                roller.add(rol.id)
                mesaj = f"{rol.mention} muaf role eklendi."
            veri["muaf_roller"] = list(roller)
            antilink_kaydet(ctx.guild.id, veri)
            await ctx.send(mesaj)
            return
        if ctx.message.channel_mentions:
            kanal = ctx.message.channel_mentions[0]
            kanallar = set(veri.get("muaf_kanallar", []))
            if kanal.id in kanallar:
                kanallar.remove(kanal.id)
                mesaj = f"{kanal.mention} muafiyetten cikarildi."
            else:
                kanallar.add(kanal.id)
                mesaj = f"{kanal.mention} muaf kanala eklendi."
            veri["muaf_kanallar"] = list(kanallar)
            antilink_kaydet(ctx.guild.id, veri)
            await ctx.send(mesaj)
            return
        await ctx.send("Kullanim: `.antilink muaf @rol` veya `.antilink muaf #kanal`")
        return

    await ctx.send("Kullanim: `.antilink`, `.antilink ac`, `.antilink kapat`, `.antilink muaf @rol/#kanal`")


def renk_rollari_al(guild_id: int):
    return ayarlari_yukle().get(str(guild_id), {}).get("renk_rollari", [])


def renk_rollari_kaydet(guild_id: int, rol_idleri):
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        ayarlar[gk]["renk_rollari"] = rol_idleri

    ayarlari_guncelle(_guncelle)


def renk_panel_mesajlari_al(guild_id: int):
    return ayarlari_yukle().get(str(guild_id), {}).get("renk_panel_mesajlari", [])


def renk_panel_mesaji_ekle(guild_id: int, channel_id: int, message_id: int):
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        kayitlar = ayarlar[gk].get("renk_panel_mesajlari", [])
        yeni = [k for k in kayitlar if k.get("message_id") != message_id]
        yeni.append({"channel_id": channel_id, "message_id": message_id})
        ayarlar[gk]["renk_panel_mesajlari"] = yeni[-10:]

    ayarlari_guncelle(_guncelle)


def anime_rollari_al(guild_id: int):
    return ayarlari_yukle().get(str(guild_id), {}).get("anime_rollari", [])


def anime_rollari_kaydet(guild_id: int, rol_idleri):
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        ayarlar[gk]["anime_rollari"] = rol_idleri

    ayarlari_guncelle(_guncelle)


def anime_panel_mesajlari_al(guild_id: int):
    return ayarlari_yukle().get(str(guild_id), {}).get("anime_panel_mesajlari", [])


def anime_panel_mesaji_ekle(guild_id: int, channel_id: int, message_id: int):
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        kayitlar = ayarlar[gk].get("anime_panel_mesajlari", [])
        yeni = [k for k in kayitlar if k.get("message_id") != message_id]
        yeni.append({"channel_id": channel_id, "message_id": message_id})
        ayarlar[gk]["anime_panel_mesajlari"] = yeni[-10:]

    ayarlari_guncelle(_guncelle)


ANIME_ROL_ISIMLERI = [
    "   Naruto ", "   Sasuke ", "   Sakura ", "   Kakashi ",
    "   Itachi ", "   Kurama ", "   Luffy ", "   Zoro ",
    "   Nami ", "   Ace ", "   Shanks ", "   Law ",
    "   Robin ", "   Franky ", "   Brook ", "   Sanji ",
    "   Ichigo ", "   Rukia ", "   Aizen ", "   Ulquiorra ",
    "   Goku ", "   Vegeta ", "   Gohan ", "   Broly ",
    "   Beerus ", "   Whis ", "   Eren ", "   Mikasa ",
    "   Armin ", "   Levi ", "   Hange ", "   Reiner ",
    "   Tanjiro ", "   Nezuko ", "   Inosuke ", "   Zenitsu ",
    "   Rengoku ", "   Muichiro ", "   Shinobu ", "   Tengen ",
    "   Gojo ", "   Megumi ", "   Nobara ", "   Sukuna ",
    "   Panda ", "   Maki ", "   Yuta ", "   Geto ",
    "   Lelouch ", "   C.C. ", "   Kallen ", "   Light ",
    "   L ", "   Ryuk ", "   Kira ", "   Hikari ",
    "   Emilia ", "   Rem ", "   Ram ", "   Subaru ",
    "   Zero Two ", "   Hiro ", "   Marin ", "   Gojo Wakana ",
    "   Bocchi ", "   Kita ", "   Nijika ", "   Ryo ",
    "   Senku ", "   Gen ", "   Taiju ", "   Yuzuriha ",
    "   Natsu ", "   Gray ", "   Erza ", "   Happy ",
    "   Kaneki ", "   Touka ", "   Hisoka ", "   Gon ",
    "   Killua ", "   Kurapika ", "   Chrollo ", "   Power ",
    "   Denji ", "   Pochita ", "   Makima ", "   Beam ",
    "   Frieren ", "   Fern ", "   Stark ", "   Himmel ",
    "   Anya ", "   Loid ", "   Yor ", "   Bond ",
    "   Madoka ", "   Homura ", "   Kagome ", "   Inuyasha ",
]


ANIME_ROL_RENKLERI = [
    discord.Color.from_rgb(255, 153, 204),
    discord.Color.from_rgb(153, 204, 255),
    discord.Color.from_rgb(255, 204, 153),
    discord.Color.from_rgb(204, 153, 255),
    discord.Color.from_rgb(153, 255, 204),
    discord.Color.from_rgb(255, 102, 153),
]

# Terminal kodlamasi yuzunden ustteki kaynakta goruntu bozulsa bile,
# asagidaki liste komutlar tarafinda kullanilan net anime adlaridir.
ANIME_ROL_ISIMLERI = [
    "   Naruto ", "   One Piece ", "   Bleach ", "   Dragon Ball ",
    "   Attack on Titan ", "   Demon Slayer ", "   Jujutsu Kaisen ", "   Code Geass ",
    "   Death Note ", "   Re:Zero ", "   Darling in the Franxx ", "   My Dress-Up Darling ",
    "   Bocchi the Rock ", "   Dr. Stone ", "   Fairy Tail ", "   Tokyo Ghoul ",
    "   Hunter x Hunter ", "   Chainsaw Man ", "   Frieren ", "   Spy x Family ",
    "   Madoka Magica ", "   Inuyasha ", "   Your Lie in April ", "   Oshi no Ko ",
    "   Haikyuu ", "   Orange ", "   Horimiya ", "   Kimi ni Todoke ",
    "   Steins;Gate ", "   Violet Evergarden ", "   Black Butler ", "   Fire Force ",
    "   Shield Hero ", "   No Game No Life ", "   Sword Art Online ", "   Wolf's Rain ",
    "   Classroom of the Elite ", "   Land of the Lustrous ", "   The Ancient Magus' Bride ", "   Sailor Moon ",
    "   Kuma Kuma Bear ", "   Food Wars ", "   Forest of Piano ", "   Natsume's Book of Friends ",
    "   The Eminence in Shadow ", "   Summer Time Rendering ", "   Monster ", "   Fate Stay Night ",
    "   A Certain Scientific Railgun ", "   Blue Period ", "   Bungou Stray Dogs ", "   Rose of Versailles ",
    "   Kill la Kill ", "   Free ", "   Angel Beats ", "   Weathering With You ",
    "   Garden of Words ", "   Blend S ", "   Black Clover ", "   Little Witch Academia ",
    "   Yona of the Dawn ", "   Cardcaptor Sakura ", "   Cowboy Bebop ", "   White Album 2 ",
    "   Mashle ", "   Bubble ", "   Astra Lost in Space ", "   Mob Psycho 100 ",
    "   Hell Girl ", "   Beastars ", "   Assassination Classroom ", "   To Your Eternity ",
    "   Noragami ", "   Gintama ", "   Erased ", "   Princess Tutu ",
    "   Komi Can't Communicate ", "   A Sign of Affection ", "   Is the Order a Rabbit ", "   Log Horizon ",
    "   Toriko ", "   Magi ", "   Vinland Saga ", "   The Apothecary Diaries ",
    "   Black Lagoon ", "   Given ", "   Barakamon ", "   Spice and Wolf ",
    "   Love Live ", "   Mawaru Penguindrum ", "   Blue Exorcist ", "   Fruits Basket ",
    "   Jellyfish Can't Swim in the Night ", "   Millennium Actress ", "   Charlotte ", "   The World God Only Knows ",
    "   Revolutionary Girl Utena ", "   Mushishi ", "   Dororo ", "   Parasyte ",
]


class RenkSec(discord.ui.Select):
    def __init__(self, guild_id: int, rol_idleri: list[int]):
        self.guild_id = guild_id
        self.rol_idleri = rol_idleri
        guild = bot.get_guild(guild_id)
        roller = [guild.get_role(rol_id) for rol_id in rol_idleri] if guild else []
        roller = [rol for rol in roller if rol]
        secenekler = [
            discord.SelectOption(
                label=rol.name[:100],
                value=str(rol.id),
                description=f"{len(rol.members)} uye kullaniyor"[:100]
            )
            for rol in roller[:24]
        ]
        secenekler.append(discord.SelectOption(label="Renk Kaldir", value="clear", description="Uzerindeki renk rollerini temizler"))
        super().__init__(
            placeholder="Kendine bir renk rolu sec",
            min_values=1,
            max_values=1,
            options=secenekler,
            custom_id=f"renk_sec_{guild_id}",
        )

    async def callback(self, interaction: discord.Interaction):
        roller = [interaction.guild.get_role(rol_id) for rol_id in self.rol_idleri]
        roller = [rol for rol in roller if rol]
        mevcut_renkler = [rol for rol in roller if rol in interaction.user.roles]
        if mevcut_renkler:
            await interaction.user.remove_roles(*mevcut_renkler, reason="Renk secimi guncellendi")
        if self.values[0] == "clear":
            await interaction.response.send_message("Uzerindeki renk rolleri temizlendi.", ephemeral=True)
            return
        yeni_rol = interaction.guild.get_role(int(self.values[0]))
        if yeni_rol:
            await interaction.user.add_roles(yeni_rol, reason="Renk paneli secimi")
            await interaction.response.send_message(f"Yeni rengin basariyla {yeni_rol.mention} olarak ayarlandi.", ephemeral=True)


class RenkView(discord.ui.View):
    def __init__(self, guild_id: int, rol_idleri: list[int]):
        super().__init__(timeout=None)
        self.add_item(RenkSec(guild_id, rol_idleri))


def _anime_panel_embed_olustur(guild: discord.Guild, rol_idleri: list[int], sayfa: int) -> discord.Embed:
    roller = [guild.get_role(rol_id) for rol_id in rol_idleri]
    roller = [rol for rol in roller if rol]
    baslangic = sayfa * 24
    sayfa_rolleri = roller[baslangic:baslangic + 24]
    liste = "\n".join(f"`{baslangic + i + 1}.` {rol.mention}" for i, rol in enumerate(sayfa_rolleri))
    embed = discord.Embed(
        title="Anime Rol Menusu",
        description="Asagidaki menuden istedigin kadar anime rolu secebilirsin. Rollerin birikir; istersen temizleme butonuyla hepsini tek seferde silebilirsin.",
        color=RENKLER["rol"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Roller", value=liste or "Rol bulunamadi.", inline=False)
    embed.set_footer(text=f"Sayfa {sayfa + 1}/{max(1, (len(roller) + 23) // 24)}  Toplam {len(roller)} anime rolu")
    return embed


class AnimeRolSecPersistent(discord.ui.Select):
    def __init__(self, guild_id: int, rol_idleri: list[int], sayfa: int):
        self.guild_id = guild_id
        self.rol_idleri = rol_idleri
        guild = bot.get_guild(guild_id)
        roller = [guild.get_role(rol_id) for rol_id in rol_idleri] if guild else []
        roller = [rol for rol in roller if rol]
        baslangic = sayfa * 24
        sayfa_rolleri = roller[baslangic:baslangic + 24]
        secenekler = [
            discord.SelectOption(
                label=rol.name[:100],
                value=str(rol.id),
                description=f"{len(rol.members)} uye kullaniyor"[:100]
            )
            for rol in sayfa_rolleri
        ]
        super().__init__(
            placeholder=f"Anime rol(ler)i sec  Sayfa {sayfa + 1}",
            min_values=1,
            max_values=max(1, len(secenekler)),
            options=secenekler,
            custom_id=f"anime_rol_sec_{guild_id}",
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        secilen_roller = [interaction.guild.get_role(int(rol_id)) for rol_id in self.values]
        secilen_roller = [rol for rol in secilen_roller if rol]
        if not secilen_roller:
            await interaction.followup.send("Gecerli bir anime rolu secilmedi.", ephemeral=True)
            return
        for index in range(0, len(secilen_roller), 5):
            parcali = secilen_roller[index:index + 5]
            await interaction.user.add_roles(*parcali, reason="Anime rol paneli secimi")
        await interaction.followup.send(
            f"Anime rollerin eklendi: {', '.join(rol.mention for rol in secilen_roller[:10])}",
            ephemeral=True
        )


class AnimeRolViewPersistent(discord.ui.View):
    def __init__(self, guild_id: int, rol_idleri: list[int], sayfa: int = 0):
        super().__init__(timeout=None)
        self.guild_id = guild_id
        self.rol_idleri = rol_idleri
        self.sayfa = sayfa
        self.sayfa_sayisi = max(1, (len(rol_idleri) + 23) // 24)
        self.add_item(AnimeRolSecPersistent(guild_id, rol_idleri, sayfa))

    @discord.ui.button(label="Onceki", style=discord.ButtonStyle.secondary, custom_id="anime_rol_onceki")
    async def onceki(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        yeni_sayfa = (self.sayfa - 1) % self.sayfa_sayisi
        embed = _anime_panel_embed_olustur(interaction.guild, self.rol_idleri, yeni_sayfa)
        await interaction.message.edit(embed=embed, view=AnimeRolViewPersistent(self.guild_id, self.rol_idleri, yeni_sayfa))

    @discord.ui.button(label="Sonraki", style=discord.ButtonStyle.secondary, custom_id="anime_rol_sonraki")
    async def sonraki(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        yeni_sayfa = (self.sayfa + 1) % self.sayfa_sayisi
        embed = _anime_panel_embed_olustur(interaction.guild, self.rol_idleri, yeni_sayfa)
        await interaction.message.edit(embed=embed, view=AnimeRolViewPersistent(self.guild_id, self.rol_idleri, yeni_sayfa))

    @discord.ui.button(label="Tum Anime Rollerini Temizle", style=discord.ButtonStyle.danger, custom_id="anime_rol_temizle")
    async def temizle(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        roller = [interaction.guild.get_role(rol_id) for rol_id in self.rol_idleri]
        roller = [rol for rol in roller if rol and rol in interaction.user.roles]
        if roller:
            for index in range(0, len(roller), 5):
                parcali = roller[index:index + 5]
                await interaction.user.remove_roles(*parcali, reason="Anime rol paneli temizleme")
        await interaction.followup.send("Uzerindeki tum anime rolleri temizlendi.", ephemeral=True)


@bot.command(name="renkekle", aliases=["renk-ekle"])
@commands.has_permissions(manage_roles=True)
async def renk_ekle(ctx, rol: discord.Role = None):
    if not rol:
        await ctx.send("Kullanim: `.renkekle @rol`")
        return
    roller = renk_rollari_al(ctx.guild.id)
    if rol.id not in roller:
        roller.append(rol.id)
        renk_rollari_kaydet(ctx.guild.id, roller)
    await ctx.send(f"{rol.mention} renk listesine eklendi.")


@bot.command(name="renkcikar", aliases=["renk-cikar"])
@commands.has_permissions(manage_roles=True)
async def renk_cikar(ctx, rol: discord.Role = None):
    if not rol:
        await ctx.send("Kullanim: `.renkcikar @rol`")
        return
    roller = [rol_id for rol_id in renk_rollari_al(ctx.guild.id) if rol_id != rol.id]
    renk_rollari_kaydet(ctx.guild.id, roller)
    await ctx.send(f"{rol.mention} renk listesinden cikarildi.")


@bot.command(name="renklist", aliases=["renk-list"])
async def renk_list(ctx):
    roller = [ctx.guild.get_role(rol_id) for rol_id in renk_rollari_al(ctx.guild.id)]
    roller = [rol.mention for rol in roller if rol]
    await ctx.send("Renk rolleri:\n" + ("\n".join(roller) if roller else "Hic rol eklenmemis."))


@bot.command(name="renkpanel", aliases=["renk-panel"])
@commands.has_permissions(manage_roles=True)
async def renk_panel(ctx):
    roller = [ctx.guild.get_role(rol_id) for rol_id in renk_rollari_al(ctx.guild.id)]
    roller = [rol for rol in roller if rol]
    if not roller:
        await ctx.send("Once `.renkekle @rol` ile renk rolleri eklenmeli.")
        return

    class RenkSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(
                    label=rol.name[:100],
                    value=str(rol.id),
                    description=f"{rol.members.__len__()} uye kullaniyor"[:100]
                )
                for rol in roller[:24]
            ]
            secenekler.append(discord.SelectOption(label="Renk Kaldr", value="clear", description="zerindeki renk rollerini temizler"))
            super().__init__(placeholder="Kendine bir renk rol se", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            mevcut_renkler = [rol for rol in roller if rol in interaction.user.roles]
            if mevcut_renkler:
                await interaction.user.remove_roles(*mevcut_renkler, reason="Renk secimi guncellendi")
            if self.values[0] == "clear":
                await interaction.response.send_message("zerindeki renk rolleri temizlendi.", ephemeral=True)
                return
            yeni_rol = interaction.guild.get_role(int(self.values[0]))
            if yeni_rol:
                await interaction.user.add_roles(yeni_rol, reason="Renk paneli secimi")
                await interaction.response.send_message(f"Yeni rengin baaryla {yeni_rol.mention} olarak ayarland.", ephemeral=True)

    class RenkView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.add_item(RenkSec())

    rol_listesi = "\n".join(f"`{i+1}.` {rol.mention}" for i, rol in enumerate(roller[:12]))
    embed = discord.Embed(
        title="Renk Rol Seim Mens",
        description=(
            "Aadaki menden sunucuda kullanmak istediin renk roln seebilirsin.\n"
            "Yeni bir renk setiinde eski renk rollerin otomatik kaldrlr."
        ),
        color=RENKLER["rol"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Nasl alr?", value="Menden bir renk se.\nstersen `Renk Kaldr` ile tm renk rollerini temizle.", inline=False)
    embed.add_field(name="Kullanlabilir Roller", value=rol_listesi if rol_listesi else "Rol bulunamad.", inline=False)
    embed.set_footer(text=f"Toplam {len(roller)} renk rol  {ctx.guild.name}")
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    mesaj = await ctx.send(embed=embed, view=globals()["RenkView"](ctx.guild.id, [rol.id for rol in roller]))
    renk_panel_mesaji_ekle(ctx.guild.id, ctx.channel.id, mesaj.id)


# 
#  LEVEL + HOSGELDIN SISTEMI (EK BLOK)
# 

@bot.command(name="animerollerikur", aliases=["anime-rolleri-kur"])
@commands.has_permissions(manage_roles=True)
async def anime_rollari_kur(ctx, referans_rol: discord.Role = None):
    if not referans_rol:
        await ctx.send(embed=kullanim_embedi("`.animerollerikur @referans-rol`\nBot anime rollerini belirttigin rolun hemen altina dizer."))
        return
    if referans_rol >= ctx.guild.me.top_role:
        await ctx.send(embed=hata_embedi("Rol Hiyerarsisi Hatasi", "Sectigin referans rol, botun en ust rolunun altinda olmali."))
        return

    olusturulan = []
    toplam_roller = []
    for index, isim in enumerate(ANIME_ROL_ISIMLERI):
        rol = discord.utils.get(ctx.guild.roles, name=isim)
        if rol is None:
            try:
                rol = await ctx.guild.create_role(
                    name=isim,
                    colour=ANIME_ROL_RENKLERI[index % len(ANIME_ROL_RENKLERI)],
                    mentionable=False,
                    reason=f"{ctx.author} tarafindan anime rol paketi kuruldu"
                )
                olusturulan.append(rol)
            except discord.Forbidden:
                await ctx.send(embed=hata_embedi("Rol Olusturma Hatasi", "Botun rol olusturma yetkisi veya rol hiyerarsisi yeterli degil."))
                return
        toplam_roller.append(rol)

    if referans_rol.position <= len([rol for rol in toplam_roller if rol]):
        await ctx.send(embed=hata_embedi("Rol Siralama Hatasi", "Sectigin rol cok asagida. Anime rollerini hemen altina dizmek icin daha yuksek bir referans rol sec."))
        return

    try:
        roller_sirali = sorted([rol for rol in toplam_roller if rol], key=lambda r: r.position, reverse=True)
        konumlar = {rol: referans_rol.position - 1 - index for index, rol in enumerate(roller_sirali)}
        await ctx.guild.edit_role_positions(positions=konumlar)
    except discord.Forbidden:
        await ctx.send(embed=hata_embedi("Rol Siralama Hatasi", "Anime rolleri olustu ama bot bunlari sectigin rolun hemen altina tasiyamadi."))
        return

    anime_rollari_kaydet(ctx.guild.id, [rol.id for rol in toplam_roller if rol])
    embed = discord.Embed(
        title="Anime Rolleri Hazir",
        description=f"Toplam **{len(toplam_roller)}** anime rolu sisteme baglandi.",
        color=RENKLER["rol"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Yeni Acilan", value=str(len(olusturulan)), inline=True)
    embed.add_field(name="Zaten Var Olan", value=str(len(toplam_roller) - len(olusturulan)), inline=True)
    embed.add_field(name="Referans Rol", value=referans_rol.mention, inline=True)
    embed.add_field(name="Ornekler", value="\n".join(rol.name for rol in toplam_roller[:6]) if toplam_roller else "-", inline=False)
    embed.set_footer(text="Secim menusu icin `.animerolpanel` kullan.")
    await ctx.send(embed=embed)


@bot.command(name="animerollerikaldir", aliases=["anime-rolleri-kaldir"])
@commands.has_permissions(manage_roles=True)
async def anime_rollari_kaldir(ctx):
    roller = [ctx.guild.get_role(rol_id) for rol_id in anime_rollari_al(ctx.guild.id)]
    roller = [rol for rol in roller if rol]
    silinen = 0
    for rol in roller:
        try:
            await rol.delete(reason=f"{ctx.author} tarafindan anime rol paketi kaldirildi")
            silinen += 1
        except discord.Forbidden:
            await ctx.send(embed=hata_embedi("Rol Silme Hatasi", "Bazi anime rollerini silmeye yetkim yetmedi."))
            return
    anime_rollari_kaydet(ctx.guild.id, [])
    await ctx.send(embed=discord.Embed(
        title="Anime Rolleri Kaldirildi",
        description=f"Toplam **{silinen}** anime rolu sunucudan silindi.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    ))


@bot.command(name="asagitasi", aliases=["roltasiasagi", "rol-en-asa"])
@commands.has_permissions(manage_roles=True)
async def asagi_tasi(ctx, rol: discord.Role = None):
    if not rol:
        await ctx.send(embed=kullanim_embedi("`.asagitasi @rol`\nEtiketledigin rolu tasinabilecek en alt siraya indirir."))
        return
    if rol >= ctx.guild.me.top_role:
        await ctx.send(embed=hata_embedi("Rol Hiyerarsisi Hatasi", "Bu rol botun en ust rolunden yukarida oldugu icin tasinamaz."))
        return
    try:
        await rol.edit(position=1, reason=f"{ctx.author} tarafindan en alta tasindi")
    except discord.Forbidden:
        await ctx.send(embed=hata_embedi("Rol Tasima Hatasi", "Bu rolu en alta tasimaya yetkim yetmedi."))
        return
    await ctx.send(embed=discord.Embed(
        title="Rol En Alta Tasindi",
        description=f"{rol.mention} rolu tasinabilecek en alt siraya indirildi.",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    ))


@bot.command(name="animerolpanel", aliases=["anime-rol-panel"])
@commands.has_permissions(manage_roles=True)
async def anime_rol_panel(ctx):
    roller = [ctx.guild.get_role(rol_id) for rol_id in anime_rollari_al(ctx.guild.id)]
    roller = [rol for rol in roller if rol]
    if not roller:
        await ctx.send(embed=kullanim_embedi("Once `.animerollerikur` komutunu kullanarak anime rollerini kurmalisin."))
        return

    def anime_panel_embedi(sayfa: int) -> discord.Embed:
        baslangic = sayfa * 24
        sayfa_rolleri = roller[baslangic:baslangic + 24]
        liste = "\n".join(f"`{baslangic + i + 1}.` {rol.mention}" for i, rol in enumerate(sayfa_rolleri))
        embed = discord.Embed(
            title="Anime Rol Menusu",
            description="Asagidaki menuden bir anime rolu sec. Yeni secim yaptiginda eski anime rolun otomatik kaldirilir.",
            color=RENKLER["rol"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="Roller", value=liste or "Rol bulunamadi.", inline=False)
        embed.set_footer(text=f"Sayfa {sayfa + 1}/{max(1, (len(roller) + 23) // 24)}  Toplam {len(roller)} anime rolu")
        return embed

    class AnimeRolSec(discord.ui.Select):
        def __init__(self, sayfa: int):
            baslangic = sayfa * 24
            sayfa_rolleri = roller[baslangic:baslangic + 24]
            secenekler = [
                discord.SelectOption(
                    label=rol.name[:100],
                    value=str(rol.id),
                    description=f"{len(rol.members)} uye kullaniyor"[:100]
                )
                for rol in sayfa_rolleri
            ]
            secenekler.append(discord.SelectOption(label="Anime Rolunu Kaldir", value="clear", description="Uzerindeki anime rollerini temizler"))
            super().__init__(placeholder=f"Anime rolu sec  Sayfa {sayfa + 1}", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            await interaction.response.defer(ephemeral=True)
            mevcut_anime_rolleri = [rol for rol in roller if rol in interaction.user.roles]
            if mevcut_anime_rolleri:
                await interaction.user.remove_roles(*mevcut_anime_rolleri, reason="Anime rol secimi guncellendi")
            if self.values[0] == "clear":
                await interaction.followup.send("Uzerindeki anime rolleri temizlendi.", ephemeral=True)
                return
            secilen = interaction.guild.get_role(int(self.values[0]))
            if secilen:
                await interaction.user.add_roles(secilen, reason="Anime rol paneli secimi")
                await interaction.followup.send(f"Anime rolun basariyla {secilen.mention} olarak ayarlandi.", ephemeral=True)

    class AnimeRolView(discord.ui.View):
        def __init__(self, sayfa: int = 0):
            super().__init__(timeout=99999999999)
            self.sayfa = sayfa
            self.sayfa_sayisi = max(1, (len(roller) + 23) // 24)
            self.add_item(AnimeRolSec(sayfa))

        @discord.ui.button(label="Onceki", style=discord.ButtonStyle.secondary)
        async def onceki(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.defer()
            yeni_sayfa = (self.sayfa - 1) % self.sayfa_sayisi
            await interaction.message.edit(embed=anime_panel_embedi(yeni_sayfa), view=AnimeRolView(yeni_sayfa))

        @discord.ui.button(label="Sonraki", style=discord.ButtonStyle.secondary)
        async def sonraki(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.defer()
            yeni_sayfa = (self.sayfa + 1) % self.sayfa_sayisi
            await interaction.message.edit(embed=anime_panel_embedi(yeni_sayfa), view=AnimeRolView(yeni_sayfa))

    await ctx.send(embed=anime_panel_embedi(0), view=AnimeRolView(0))


bot.remove_command("animerolpanel")


@bot.command(name="animerolpanel", aliases=["anime-rol-panel"])
@commands.has_permissions(manage_roles=True)
async def anime_rol_panel_v2(ctx):
    roller = [ctx.guild.get_role(rol_id) for rol_id in anime_rollari_al(ctx.guild.id)]
    roller = [rol for rol in roller if rol]
    if not roller:
        await ctx.send(embed=kullanim_embedi("Once `.animerollerikur` komutunu kullanarak anime rollerini kurmalisin."))
        return

    def anime_panel_embedi(sayfa: int) -> discord.Embed:
        baslangic = sayfa * 24
        sayfa_rolleri = roller[baslangic:baslangic + 24]
        liste = "\n".join(f"`{baslangic + i + 1}.` {rol.mention}" for i, rol in enumerate(sayfa_rolleri))
        embed = discord.Embed(
            title="Anime Rol Menusu",
            description="Asagidaki menuden istedigin kadar anime rolu secebilirsin. Rollerin birikir; istersen temizleme butonuyla hepsini tek seferde silebilirsin.",
            color=RENKLER["rol"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="Roller", value=liste or "Rol bulunamadi.", inline=False)
        embed.set_footer(text=f"Sayfa {sayfa + 1}/{max(1, (len(roller) + 23) // 24)}  Toplam {len(roller)} anime rolu")
        return embed

    class AnimeRolSecV2(discord.ui.Select):
        def __init__(self, sayfa: int):
            baslangic = sayfa * 24
            sayfa_rolleri = roller[baslangic:baslangic + 24]
            secenekler = [
                discord.SelectOption(
                    label=rol.name[:100],
                    value=str(rol.id),
                    description=f"{len(rol.members)} uye kullaniyor"[:100]
                )
                for rol in sayfa_rolleri
            ]
            super().__init__(placeholder=f"Anime rol(ler)i sec  Sayfa {sayfa + 1}", min_values=1, max_values=max(1, len(secenekler)), options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            await interaction.response.defer(ephemeral=True)
            secilen_roller = [interaction.guild.get_role(int(rol_id)) for rol_id in self.values]
            secilen_roller = [rol for rol in secilen_roller if rol]
            if not secilen_roller:
                await interaction.followup.send("Gecerli bir anime rolu secilmedi.", ephemeral=True)
                return
            for index in range(0, len(secilen_roller), 5):
                parcali = secilen_roller[index:index + 5]
                await interaction.user.add_roles(*parcali, reason="Anime rol paneli secimi")
            await interaction.followup.send(
                f"Anime rollerin eklendi: {', '.join(rol.mention for rol in secilen_roller[:10])}",
                ephemeral=True
            )

    class AnimeRolViewV2(discord.ui.View):
        def __init__(self, sayfa: int = 0):
            super().__init__(timeout=99999999999)
            self.sayfa = sayfa
            self.sayfa_sayisi = max(1, (len(roller) + 23) // 24)
            self.add_item(AnimeRolSecV2(sayfa))

        @discord.ui.button(label="Onceki", style=discord.ButtonStyle.secondary)
        async def onceki(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.defer()
            yeni_sayfa = (self.sayfa - 1) % self.sayfa_sayisi
            await interaction.message.edit(embed=anime_panel_embedi(yeni_sayfa), view=AnimeRolViewV2(yeni_sayfa))

        @discord.ui.button(label="Sonraki", style=discord.ButtonStyle.secondary)
        async def sonraki(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.defer()
            yeni_sayfa = (self.sayfa + 1) % self.sayfa_sayisi
            await interaction.message.edit(embed=anime_panel_embedi(yeni_sayfa), view=AnimeRolViewV2(yeni_sayfa))

        @discord.ui.button(label="Tum Anime Rollerini Temizle", style=discord.ButtonStyle.danger)
        async def temizle(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.defer(ephemeral=True)
            mevcut_anime_rolleri = [rol for rol in roller if rol in interaction.user.roles]
            if mevcut_anime_rolleri:
                for index in range(0, len(mevcut_anime_rolleri), 5):
                    parcali = mevcut_anime_rolleri[index:index + 5]
                    await interaction.user.remove_roles(*parcali, reason="Anime rol paneli temizleme")
            await interaction.followup.send("Uzerindeki tum anime rolleri temizlendi.", ephemeral=True)

    await ctx.send(embed=anime_panel_embedi(0), view=AnimeRolViewV2(0))


import random

_LEVEL_XP_COOLDOWN = {}
_LEVEL_COOLDOWN_SANIYE = 45
_PROFIL_BEKLEYEN = {}
_SES_OTURUMLARI = {}


def _profil_bekleyen_arttir(guild_id: int, user_id: int, mesaj_delta: int = 0, ses_delta: int = 0):
    gk, uk = str(guild_id), str(user_id)
    if gk not in _PROFIL_BEKLEYEN:
        _PROFIL_BEKLEYEN[gk] = {}
    if uk not in _PROFIL_BEKLEYEN[gk]:
        _PROFIL_BEKLEYEN[gk][uk] = {"message_count": 0, "voice_seconds": 0}
    _PROFIL_BEKLEYEN[gk][uk]["message_count"] += int(mesaj_delta)
    _PROFIL_BEKLEYEN[gk][uk]["voice_seconds"] += int(ses_delta)


def _profil_istat_al(guild_id: int, user_id: int) -> dict:
    ayarlar = ayarlari_yukle()
    gk, uk = str(guild_id), str(user_id)
    veri = ayarlar.get(gk, {}).get("profil_istat", {}).get(uk, {})
    sonuc = {
        "message_count": int(veri.get("message_count", 0)),
        "voice_seconds": int(veri.get("voice_seconds", 0)),
    }
    bekleyen = _PROFIL_BEKLEYEN.get(gk, {}).get(uk)
    if bekleyen:
        sonuc["message_count"] += int(bekleyen.get("message_count", 0))
        sonuc["voice_seconds"] += int(bekleyen.get("voice_seconds", 0))
    aktif_baslangic = _SES_OTURUMLARI.get((guild_id, user_id))
    if aktif_baslangic is not None:
        sonuc["voice_seconds"] += max(0, int(time.time() - aktif_baslangic))
    return sonuc


def _profil_bekleyenleri_kaydet():
    if not _PROFIL_BEKLEYEN:
        return

    bekleyen = _PROFIL_BEKLEYEN.copy()
    _PROFIL_BEKLEYEN.clear()

    def _guncelle(ayarlar):
        for gk, kullanicilar in bekleyen.items():
            if gk not in ayarlar:
                ayarlar[gk] = {}
            if "profil_istat" not in ayarlar[gk]:
                ayarlar[gk]["profil_istat"] = {}
            for uk, delta in kullanicilar.items():
                mevcut = ayarlar[gk]["profil_istat"].get(uk, {"message_count": 0, "voice_seconds": 0})
                mevcut["message_count"] = int(mevcut.get("message_count", 0)) + int(delta.get("message_count", 0))
                mevcut["voice_seconds"] = int(mevcut.get("voice_seconds", 0)) + int(delta.get("voice_seconds", 0))
                ayarlar[gk]["profil_istat"][uk] = mevcut

    ayarlari_guncelle(_guncelle)


async def _profil_bekleyenleri_kaydet_dongusu():
    await bot.wait_until_ready()
    while not bot.is_closed():
        try:
            await asyncio.sleep(20)
            await asyncio.to_thread(_profil_bekleyenleri_kaydet)
        except Exception as e:
            print(f"[UYARI] Profil istat kaydetme dongusu: {e}")


def _sureyi_formatla(toplam_saniye: int) -> str:
    toplam_saniye = max(0, int(toplam_saniye))
    saat, kalan = divmod(toplam_saniye, 3600)
    dakika, saniye = divmod(kalan, 60)
    if saat:
        return f"{saat}s {dakika}dk"
    if dakika:
        return f"{dakika}dk {saniye}sn"
    return f"{saniye}sn"


def _toplam_xp_hesapla(level: int, xp: int) -> int:
    toplam = int(xp)
    for l in range(int(level)):
        toplam += _xp_hedef(l)
    return toplam


def _guild_ayar_al(guild_id: int) -> dict:
    return ayarlari_yukle().get(str(guild_id), {})


def _guild_ayar_kismi_kaydet(guild_id: int, key: str, value):
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        ayarlar[gk][key] = value

    ayarlari_guncelle(_guncelle)


def _level_ayar_al(guild_id: int) -> dict:
    veri = _guild_ayar_al(guild_id).get("level_sistemi", {})
    return {
        "kanal_id": veri.get("kanal_id"),
        "mesaj": veri.get("mesaj", "Tebrikler {member_mention}, **{level}. seviye** oldun!"),
        "gif_url": veri.get("gif_url"),
        "rol_odulleri": veri.get("rol_odulleri", {}),
    }


def _level_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "level_sistemi", veri)


def _welcome_ayar_al(guild_id: int) -> dict:
    veri = _guild_ayar_al(guild_id).get("hosgeldin_sistemi", {})
    return {
        "kanal_id": veri.get("kanal_id"),
        "mesaj": veri.get("mesaj", "Aramiza hos geldin {member_mention}! Sunucuda iyi eglenceler."),
        "gif_url": veri.get("gif_url"),
        "rol_ids": veri.get("rol_ids", []),
    }


def _welcome_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "hosgeldin_sistemi", veri)


def _karsilama_ayar_al(guild_id: int) -> dict:
    veri = _guild_ayar_al(guild_id).get("karsilama_sistemi", {})
    return {
        "kanal_id": veri.get("kanal_id"),
        "mesaj": veri.get("mesaj", "Aramza ho geldin {username}. Seninle birlikte {member_count} kiiyiz."),
    }


def _karsilama_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "karsilama_sistemi", veri)


TURKCE_KUFUR_LISTESI = [
    "amk", "aq", "amna", "amina", "amna koyim", "amina koyim", "amna koyaym", "amina koyayim",
    "orospu", "orospu ocuu", "orospu cocugu", "oc", "pi", "pic", "sikik", "sikerim", "sikiyim",
    "siktir", "siktir git", "yarrak", "yarak", "gt", "got", "gtveren", "gotveren", "ibne", "amck",
    "amcik", "pezevenk", "kahpe", "put", "pust", "anan", "anan sikeyim", "anani", "bok", "boktan",
    "salak orospu", "gerizekal", "gerizekali", "pi kurusu", "ebenin", "ebesinin", "gavat", "mallk",
]


def _gifcevap_ayar_al(guild_id: int) -> dict:
    veri = _guild_ayar_al(guild_id).get("gif_cevap", {})
    return {
        "aktif": veri.get("aktif", False),
        "whitelist_ids": veri.get("whitelist_ids", []),
        "kayitlar": veri.get("kayitlar", []),
    }


def _gifcevap_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "gif_cevap", veri)


def _yetkili_kufur_ayar_al(guild_id: int) -> dict:
    veri = _guild_ayar_al(guild_id).get("yetkili_kufur", {})
    return {
        "aktif": veri.get("aktif", False),
        "rol_ids": veri.get("rol_ids", []),
        "limit": int(veri.get("limit", 3) or 3),
        "durumlar": veri.get("durumlar", {}),
    }


def _yetkili_kufur_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "yetkili_kufur", veri)


def _jail_ayar_al(guild_id: int) -> dict:
    veri = _guild_ayar_al(guild_id).get("jail_sistemi", {})
    return {
        "aktif": veri.get("aktif", False),
        "kanal_id": veri.get("kanal_id"),
        "jail_rol_id": veri.get("jail_rol_id"),
        "jail_yetki_rol_id": veri.get("jail_yetki_rol_id"),
        "kayitlar": veri.get("kayitlar", {}),
    }


def _jail_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "jail_sistemi", veri)


def _guvenlik_ayar_al(guild_id: int) -> dict:
    veri = _guild_ayar_al(guild_id).get("guvenlik", {})
    return {
        "aktif": veri.get("aktif", False),
        "log_kanal_id": veri.get("log_kanal_id"),
        "sure_saniye": int(veri.get("sure_saniye", 60) or 60),
        "ban_limit": int(veri.get("ban_limit", 3) or 3),
        "kanal_limit": int(veri.get("kanal_limit", 3) or 3),
        "kanal_sil_limit": int(veri.get("kanal_sil_limit", 3) or 3),
        "rol_ac_limit": int(veri.get("rol_ac_limit", 3) or 3),
        "rol_sil_limit": int(veri.get("rol_sil_limit", 3) or 3),
        "kick_limit": int(veri.get("kick_limit", 3) or 3),
        "whitelist_ids": veri.get("whitelist_ids", []),
        "durumlar": veri.get("durumlar", {}),
    }


def _guvenlik_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "guvenlik", veri)


async def _guvenlik_sorumlu_whitelistte_mi(guild: discord.Guild, sorumlu: discord.Member | discord.User | None, ayar: dict) -> bool:
    if sorumlu is None:
        return False
    whitelist = {int(x) for x in (ayar.get("whitelist_ids", []) or []) if str(x).isdigit()}
    if not whitelist:
        return False
    if sorumlu.id in whitelist:
        return True

    uye = sorumlu if isinstance(sorumlu, discord.Member) else guild.get_member(sorumlu.id)
    if uye is None:
        try:
            uye = await guild.fetch_member(sorumlu.id)
        except discord.HTTPException:
            uye = None
    if uye is None:
        return False
    return any(rol.id in whitelist for rol in uye.roles)


def _guvenlik_log_kanali_al(guild: discord.Guild, ayar: dict) -> discord.TextChannel | None:
    kanal_id = ayar.get("log_kanal_id")
    if kanal_id:
        kanal = guild.get_channel(kanal_id)
        if isinstance(kanal, discord.TextChannel):
            return kanal
    mod_kanal_id = kanal_al(guild.id, "mod_log")
    kanal = guild.get_channel(mod_kanal_id) if mod_kanal_id else None
    return kanal if isinstance(kanal, discord.TextChannel) else None


async def _guvenlik_log_gonder(guild: discord.Guild, ayar: dict, embed: discord.Embed):
    kanal = _guvenlik_log_kanali_al(guild, ayar)
    if kanal:
        try:
            await kanal.send(embed=embed)
        except (discord.Forbidden, discord.HTTPException):
            pass


async def _guvenlik_eylem_isle(
    guild: discord.Guild,
    sorumlu: discord.Member | discord.User | None,
    eylem: str,
    hedef: str,
    limit: int,
):
    if sorumlu is None or getattr(sorumlu, "bot", False):
        return
    if guild.owner_id == sorumlu.id:
        return

    ayar = _guvenlik_ayar_al(guild.id)
    if not ayar.get("aktif"):
        return
    if await _guvenlik_sorumlu_whitelistte_mi(guild, sorumlu, ayar):
        return

    simdi = datetime.now(timezone.utc)
    pencere = max(10, int(ayar.get("sure_saniye", 60)))

    def _guncelle(ayarlar):
        gk = str(guild.id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        guvenlik = ayarlar[gk].setdefault("guvenlik", {})
        durumlar = guvenlik.setdefault("durumlar", {})
        uye_durum = durumlar.setdefault(str(sorumlu.id), {})
        eylem_durum = uye_durum.get(eylem, {})

        baslangic_str = eylem_durum.get("baslangic")
        sayi = int(eylem_durum.get("sayi", 0) or 0)

        if baslangic_str:
            try:
                baslangic = utc_datetime_from_iso(baslangic_str)
            except Exception:
                baslangic = simdi
        else:
            baslangic = simdi

        if (simdi - baslangic).total_seconds() > pencere:
            baslangic = simdi
            sayi = 0

        sayi += 1
        uye_durum[eylem] = {
            "baslangic": baslangic.isoformat(),
            "sayi": sayi,
        }
        return {
            "sayi": sayi,
            "baslangic": baslangic.isoformat(),
        }

    sonuc = ayarlari_guncelle(_guncelle)
    sayi = sonuc["sayi"]
    uyari_verildi = True

    if sayi < limit:
        return

    if not uyari_verildi:
        def _uyari_isaretle(ayarlar):
            gk = str(guild.id)
            guvenlik = ayarlar.setdefault(gk, {}).setdefault("guvenlik", {})
            uye_durum = guvenlik.setdefault("durumlar", {}).setdefault(str(sorumlu.id), {})
            eylem_durum = uye_durum.setdefault(eylem, {})
            eylem_durum["uyari_verildi"] = True

        ayarlari_guncelle(_uyari_isaretle)

        embed = discord.Embed(
            title="Gvenlik Uyars",
            description=(
                f"{sorumlu.mention} kisa surede cok fazla `{eylem}` eylemi yapti.\n"
                f"**Son hedef:** {hedef}\n"
                f"**Durum:** Bir sonraki ihlalde jaile atilacak."
            ),
            color=RENKLER["mute"],
            timestamp=simdi,
        )
        embed.add_field(name="Limit", value=f"{limit} / {pencere}s", inline=True)
        embed.add_field(name="Mevcut", value=str(sayi), inline=True)
        embed.set_footer(text="Sunucu Guvenlik Sistemi")
        await _guvenlik_log_gonder(guild, ayar, embed)
        return

    uye = guild.get_member(sorumlu.id)
    if uye is None:
        try:
            uye = await guild.fetch_member(sorumlu.id)
        except discord.HTTPException:
            uye = None
    if uye is None or guild.owner_id == uye.id:
        return

    jail_basarili, jail_sonuc = await _jail_uygula_dahili(
        guild,
        uye,
        sebep=f"Guvenlik sistemi: tekrarlanan {eylem} limiti asimi",
        uygulayan="Guvenlik sistemi"
    )

    embed = discord.Embed(
        title="Gvenlik Sistemi Tetiklendi",
        description=(
            f"{sorumlu.mention} tekrar `{eylem}` limitini asti.\n"
            f"**Son hedef:** {hedef}\n"
            f"**Sonuc:** {jail_sonuc}"
        ),
        color=RENKLER["hata"],
        timestamp=simdi,
    )
    embed.add_field(name="Limit", value=f"{limit} / {pencere}s", inline=True)
    embed.add_field(name="Mevcut", value=str(sayi), inline=True)
    embed.set_footer(text="Sunucu Guvenlik Sistemi")
    await _guvenlik_log_gonder(guild, ayar, embed)


class TicketControlView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Kapat", style=discord.ButtonStyle.danger, custom_id="ticket_kapat")
    async def kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message("Bu buton sadece ticket kanalinda kullanilabilir.", ephemeral=True)
            return

        ayar = ticket_ayar_al(interaction.guild_id)
        log_id = ayar.get("log")
        await _ticket_kapat_logu_ve_transkript(channel, interaction.user, log_id)
        await interaction.response.send_message("Ticket kapatiliyor...", ephemeral=True)
        await channel.delete(reason=f"{interaction.user} tarafindan kapatildi")

    @discord.ui.button(label="Uye Ekle", style=discord.ButtonStyle.secondary, custom_id="ticket_uyeekle")
    async def uye_ekle(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message("Bu buton sadece ticket kanalinda kullanilabilir.", ephemeral=True)
            return

        ayar = ticket_ayar_al(interaction.guild_id)
        destek_rolleri = [interaction.guild.get_role(rid) for rid in ayar.get("rol_ids", [])]
        destek_rolleri = [rol for rol in destek_rolleri if rol]
        if destek_rolleri and not any(rol in interaction.user.roles for rol in destek_rolleri) and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("Bu islem icin destek rolune veya yonetici yetkisine sahip olmalisin.", ephemeral=True)
            return

        await interaction.response.send_message("Eklemek istedigin kullaniciyi bu kanalda etiketle: @kullanici", ephemeral=True)

        def check(message: discord.Message):
            return message.author == interaction.user and message.channel == channel and message.mentions

        try:
            yanit = await bot.wait_for("message", check=check, timeout=30)
            for uye in yanit.mentions:
                await channel.set_permissions(uye, read_messages=True, send_messages=True)
            await channel.send(f"{' '.join(u.mention for u in yanit.mentions)} tickete eklendi.")
            await yanit.delete()
        except asyncio.TimeoutError:
            await channel.send("Uye ekleme isteginin suresi doldu.", delete_after=5)

    @discord.ui.button(label="Talep Al", style=discord.ButtonStyle.success, custom_id="ticket_talep")
    async def talep_al(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message("Bu buton sadece ticket kanalinda kullanilabilir.", ephemeral=True)
            return

        ayar = ticket_ayar_al(interaction.guild_id)
        destek_rolleri = [interaction.guild.get_role(rid) for rid in ayar.get("rol_ids", [])]
        destek_rolleri = [rol for rol in destek_rolleri if rol]
        if destek_rolleri and not any(rol in interaction.user.roles for rol in destek_rolleri) and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("Bu islem icin destek rolu gerekli.", ephemeral=True)
            return

        yeni_topic = channel.topic or ""
        if " | Talep:" in yeni_topic:
            yeni_topic = yeni_topic.split(" | Talep:")[0]
        await channel.edit(topic=f"{yeni_topic} | Talep: {interaction.user}")
        await interaction.response.send_message(f"Ticket {interaction.user.mention} tarafindan talep alindi.")


class TicketOpenView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Ticket Ac", style=discord.ButtonStyle.primary, custom_id="global_ticket_ac")
    async def ticket_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        ayar = ticket_ayar_al(interaction.guild_id)
        kategori = interaction.guild.get_channel(ayar.get("kategori"))
        destek_rolleri = [interaction.guild.get_role(rid) for rid in ayar.get("rol_ids", [])]
        destek_rolleri = [rol for rol in destek_rolleri if rol]
        log_id = ayar.get("log")

        if not kategori:
            await interaction.response.send_message("Kategori bulunamadi. `.ticketkur` ile yeniden kur.", ephemeral=True)
            return

        for kanal in kategori.text_channels:
            if kanal.topic and str(interaction.user.id) in kanal.topic:
                await interaction.response.send_message(f"Zaten acik bir ticketin var: {kanal.mention}", ephemeral=True)
                return

        sayi = ticket_sayaci_artir(interaction.guild_id)
        bot_member = interaction.guild.me or interaction.guild.default_role
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True),
            bot_member: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_channels=True),
        }
        for destek_rolu in destek_rolleri:
            overwrites[destek_rolu] = discord.PermissionOverwrite(read_messages=True, send_messages=True)

        ticket_kanal = await kategori.create_text_channel(
            name=f"ticket-{sayi:04d}",
            overwrites=overwrites,
            topic=f"Ticket sahibi: {interaction.user} | ID: {interaction.user.id} | #{sayi}"
        )

        ac_embed = discord.Embed(
            title=f"Ticket #{sayi:04d}",
            description=(
                f"Merhaba {interaction.user.mention}!\n"
                f"Destek ekibimiz en kisa surede yardimci olacak.\n\n"
                f"Ticketi kapatmak icin `Kapat` butonunu kullan."
            ),
            color=0x57F287,
            timestamp=datetime.now(timezone.utc)
        )
        ac_embed.set_footer(text=f"Ticket #{sayi:04d}  {zaman_damgasi()}")

        mentionlar = [interaction.user.mention] + [rol.mention for rol in destek_rolleri]
        await ticket_kanal.send(content=" ".join(mentionlar), embed=ac_embed, view=TicketControlView())
        await interaction.response.send_message(f"Ticketin acildi: {ticket_kanal.mention}", ephemeral=True)

        if log_id:
            log_kanali = interaction.guild.get_channel(log_id)
            if log_kanali:
                await log_kanali.send(embed=discord.Embed(
                    title="Yeni Ticket Acildi",
                    description=f"**Acan:** {interaction.user.mention}\n**Kanal:** {ticket_kanal.mention}\n**Numara:** `#{sayi:04d}`",
                    color=RENKLER["giris"],
                    timestamp=datetime.now(timezone.utc)
                ))


try:
    bot.remove_command("ticketpanel")
except Exception:
    pass


@bot.command(name="ticketpanel", aliases=["ticket-panel"])
@commands.has_permissions(administrator=True)
async def ticket_panel_yeni(ctx):
    ayar = ticket_ayar_al(ctx.guild.id)
    if not ayar.get("kategori"):
        await ctx.send("Once `.ticketkur` ile sistemi kur.")
        return

    panel_embed = discord.Embed(
        title="Destek Merkezi",
        description="Yardim almak icin asagidaki butona tikla. Ekibimiz en kisa surede seninle ilgilenecek.",
        color=0x5865F2
    )
    panel_embed.set_footer(text=ctx.guild.name)
    if ctx.guild.icon:
        panel_embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=panel_embed, view=TicketOpenView())


@bot.command(name="butunsistemlerikaldir")
@commands.has_permissions(administrator=True)
async def butun_sistemleri_kaldir(ctx):
    guild_ayarlari_sil(ctx.guild.id)
    await ctx.send(embed=discord.Embed(
        title="Tum Sistemler Kaldirildi",
        description="Bu sunucuya ait kayitli sistem ayarlari tamamen silindi. Gerekirse sistemleri tekrar kurabilirsin.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    ))


def zaman_damgasi() -> str:
    now = datetime.now(timezone.utc)
    return now.strftime(" %d.%m.%Y   %H:%M:%S UTC")


def kullanim_embedi(description: str) -> discord.Embed:
    embed = discord.Embed(
        title="Komut Kullanimi",
        description=description,
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=zaman_damgasi())
    return embed


try:
    bot.remove_command("butunsistemlerikaldir")
except Exception:
    pass


@bot.command(name="spam-koruma-durum")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_durum(ctx):
    ayarlar = ayarlari_yukle()
    spam_ayar = ayarlar.get(str(ctx.guild.id), {}).get("guvenlik_spam_koruma", {})
    muaf_roller = [ctx.guild.get_role(rid) for rid in spam_ayar.get("muaf_roller", [])]
    muaf_roller = [rol.mention for rol in muaf_roller if rol]
    muaf_kanallar = [ctx.guild.get_channel(kid) for kid in spam_ayar.get("muaf_kanallar", [])]
    muaf_kanallar = [kanal.mention for kanal in muaf_kanallar if kanal]

    embed = discord.Embed(
        title=" Spam Koruma Durumu",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Durum", value="Aktif" if spam_ayar.get("aktif") else "Kapali", inline=True)
    embed.add_field(name="Maksimum Ayni Mesaj", value=str(spam_ayar.get("max_ayni_mesaj", 3)), inline=True)
    embed.add_field(name="Zaman Araligi", value=f"{spam_ayar.get('zaman_araligi', 10)} saniye", inline=True)
    embed.add_field(name="Mute Suresi", value=f"{spam_ayar.get('mute_suresi', 300)} saniye", inline=True)
    embed.add_field(name="Muaf Roller", value=", ".join(muaf_roller[:10]) if muaf_roller else "Yok", inline=False)
    embed.add_field(name="Muaf Kanallar", value=", ".join(muaf_kanallar[:10]) if muaf_kanallar else "Yok", inline=False)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


class ButunSistemleriKaldirView(discord.ui.View):
    def __init__(self, sahibi_id: int):
        super().__init__(timeout=60)
        self.sahibi_id = sahibi_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.sahibi_id:
            await interaction.response.send_message("Bu onayi sadece komutu yazan kisi kullanabilir.", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="Evet, Tumunu Kaldir", style=discord.ButtonStyle.danger)
    async def onayla(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild_ayarlari_sil(interaction.guild.id)
        embed = discord.Embed(
            title="Tum Sistemler Kaldirildi",
            description="Sunucuya ait kayitli sistem ayarlari tamamen silindi.",
            color=RENKLER["hata"],
            timestamp=datetime.now(timezone.utc)
        )
        await interaction.response.edit_message(embed=embed, view=None)

    @discord.ui.button(label="Vazgec", style=discord.ButtonStyle.secondary)
    async def vazgec(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Islem Iptal Edildi",
            description="Sistem ayarlari oldugu gibi birakildi.",
            color=RENKLER["bilgi"],
            timestamp=datetime.now(timezone.utc)
        )
        await interaction.response.edit_message(embed=embed, view=None)


@bot.command(name="butunsistemlerikaldir")
@commands.has_permissions(administrator=True)
async def butun_sistemleri_kaldir_onayli(ctx):
    embed = discord.Embed(
        title=" Tum Sistemleri Kaldir",
        description="Bu islem bu sunucudaki kayitli sistem ayarlarini tamamen siler.\nDevam etmek istiyorsan asagidaki butonu kullan.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    await ctx.send(embed=embed, view=ButunSistemleriKaldirView(ctx.author.id))


def _auto_cevap_ayar_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("oto_cevap", {"aktif": True, "kayitlar": []})


def _auto_cevap_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "oto_cevap", veri)


def _sayac_ayar_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("sayac_sistemi", {"aktif": False, "hedef": 0, "kanal_id": None, "mesaj": "Hedefe ulasildi!", "tetiklendi": False})


def _sayac_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "sayac_sistemi", veri)


def _destekistek_ayar_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("destekistek", {"log_kanal_id": None})


def _destekistek_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "destekistek", veri)


def _notlar_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("uye_notlari", {})


def _notlar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "uye_notlari", veri)


def _isim_gecmisi_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("isim_gecmisi", {})


def _isim_gecmisi_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "isim_gecmisi", veri)


def _yasakli_komutlar_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("yasakli_komutlar", {})


def _yasakli_komutlar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "yasakli_komutlar", veri)


def _temprol_ayar_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("temprol", {})


def _temprol_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "temprol", veri)


@bot.check
async def yasakli_komut_kontrolu(ctx):
    if not ctx.guild or not ctx.command:
        return True
    yasakli = _yasakli_komutlar_al(ctx.guild.id)
    kanal_yasak = set(yasakli.get(str(ctx.channel.id), []) or [])
    if ctx.command.name in kanal_yasak and not ctx.author.guild_permissions.administrator:
        raise commands.CheckFailure("Bu komut bu kanalda kapatildi.")
    return True


@bot.listen("on_command_error")
async def yasakli_komut_hatasi(ctx, error):
    if isinstance(error, commands.CheckFailure) and str(error) == "Bu komut bu kanalda kapatildi.":
        await ctx.send(embed=hata_embedi("Komut Kapali", "Bu komut bu kanalda kullanima kapatildi."))


@bot.listen("on_member_update")
async def isim_gecmisi_dinle(onceki: discord.Member, sonraki: discord.Member):
    eski = onceki.display_name
    yeni = sonraki.display_name
    if eski == yeni:
        return
    veri = _isim_gecmisi_al(sonraki.guild.id)
    kayitlar = veri.setdefault(str(sonraki.id), [])
    kayitlar.append({"eski": eski, "yeni": yeni, "zaman": datetime.now(timezone.utc).isoformat()})
    veri[str(sonraki.id)] = kayitlar[-20:]
    _isim_gecmisi_kaydet(sonraki.guild.id, veri)


async def _sayac_kontrol_et(guild: discord.Guild):
    ayar = _sayac_ayar_al(guild.id)
    if not ayar.get("aktif"):
        return
    hedef = int(ayar.get("hedef", 0) or 0)
    if hedef <= 0 or guild.member_count < hedef or ayar.get("tetiklendi"):
        return
    kanal = guild.get_channel(ayar.get("kanal_id")) if ayar.get("kanal_id") else None
    if isinstance(kanal, discord.TextChannel):
        mesaj = str(ayar.get("mesaj") or "Hedefe ulasildi!").replace("{member_count}", str(guild.member_count)).replace("{target}", str(hedef)).replace("{guild}", guild.name)
        await kanal.send(mesaj)
    ayar["tetiklendi"] = True
    _sayac_ayar_kaydet(guild.id, ayar)


@bot.listen("on_member_join")
async def sayac_join(member: discord.Member):
    ayar = _sayac_ayar_al(member.guild.id)
    if ayar.get("tetiklendi") and member.guild.member_count < int(ayar.get("hedef", 0) or 0):
        ayar["tetiklendi"] = False
        _sayac_ayar_kaydet(member.guild.id, ayar)
    await _sayac_kontrol_et(member.guild)


@bot.listen("on_member_remove")
async def sayac_remove(member: discord.Member):
    ayar = _sayac_ayar_al(member.guild.id)
    if ayar.get("tetiklendi") and member.guild.member_count < int(ayar.get("hedef", 0) or 0):
        ayar["tetiklendi"] = False
        _sayac_ayar_kaydet(member.guild.id, ayar)


async def _temprol_dongusu():
    await bot.wait_until_ready()
    while not bot.is_closed():
        try:
            simdi = datetime.now(timezone.utc)
            ayarlar = ayarlari_yukle()
            degisti = False
            for gk, gveri in list(ayarlar.items()):
                temprol = gveri.get("temprol", {})
                kayitlar = temprol.get("kayitlar", [])
                yeni_kayitlar = []
                guild = bot.get_guild(int(gk)) if str(gk).isdigit() else None
                for kayit in kayitlar:
                    bitis = kayit.get("bitis")
                    if not bitis:
                        continue
                    try:
                        bitis_dt = utc_datetime_from_iso(bitis)
                    except Exception:
                        bitis_dt = simdi
                    if guild and bitis_dt <= simdi:
                        uye = guild.get_member(int(kayit.get("uye_id", 0)))
                        rol = guild.get_role(int(kayit.get("rol_id", 0)))
                        if uye and rol and rol in uye.roles:
                            try:
                                await uye.remove_roles(rol, reason="Sureli rol suresi doldu")
                            except Exception:
                                yeni_kayitlar.append(kayit)
                                continue
                        degisti = True
                    else:
                        yeni_kayitlar.append(kayit)
                if kayitlar != yeni_kayitlar:
                    gveri.setdefault("temprol", {})["kayitlar"] = yeni_kayitlar
                    ayarlar[gk] = gveri
                    degisti = True
            if degisti:
                ayarlari_kaydet(ayarlar)
        except Exception as e:
            print(f"[UYARI] Temprol dongusu: {e}")
        await asyncio.sleep(20)


@bot.listen("on_ready")
async def temprol_dongu_baslat():
    if not getattr(bot, "_temprol_dongusu_basladi", False):
        bot._temprol_dongusu_basladi = True
        asyncio.create_task(_temprol_dongusu())


@bot.listen("on_message")
async def oto_cevap_dinle(message: discord.Message):
    if message.author.bot or not message.guild:
        return
    ayar = _auto_cevap_ayar_al(message.guild.id)
    if not ayar.get("aktif", True):
        return
    icerik = message.content.lower()
    for kayit in ayar.get("kayitlar", []):
        anahtar = str(kayit.get("anahtar", "")).lower().strip()
        cevap = str(kayit.get("cevap", "")).strip()
        if anahtar and cevap and anahtar in icerik:
            await message.channel.send(cevap)
            break


@bot.command(name="sunucupanel")
async def sunucu_panel(ctx):
    g = ctx.guild
    embed = discord.Embed(title=" Sunucu Paneli", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Sunucu", value=g.name, inline=True)
    embed.add_field(name="Uye", value=str(g.member_count), inline=True)
    embed.add_field(name="Boost", value=str(g.premium_subscription_count or 0), inline=True)
    embed.add_field(name="Kanal", value=str(len(g.channels)), inline=True)
    embed.add_field(name="Rol", value=str(len(g.roles)), inline=True)
    embed.add_field(name="Kurulus", value=g.created_at.strftime("%d.%m.%Y"), inline=True)
    if g.icon:
        embed.set_thumbnail(url=g.icon.url)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


@bot.command(name="yetkilipanel")
@commands.has_permissions(manage_guild=True)
async def yetkili_panel(ctx):
    ayarlar = ayarlari_yukle().get(str(ctx.guild.id), {})
    warnlar = ayarlar.get("uyarilar", {})
    partnerler = ayarlar.get("yetkili_partnerleri", {})
    satirlar = []
    for uye in ctx.guild.members:
        if uye.bot:
            continue
        if any(p for p, v in uye.guild_permissions if v and p in {"ban_members", "kick_members", "moderate_members", "manage_guild"}):
            warn_sayi = len(warnlar.get(str(uye.id), []))
            partner_sayi = int(partnerler.get(str(uye.id), {}).get("sayi", 0))
            satirlar.append(f" {uye.mention}  Uyari: {warn_sayi}  Partner: {partner_sayi}")
    embed = discord.Embed(title=" Yetkili Paneli", description="\n".join(satirlar[:20]) or "Yetkili bulunamadi.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


@bot.command(name="cezagecmisi")
@commands.has_permissions(manage_guild=True)
async def ceza_gecmisi(ctx, uye: discord.Member = None):
    hedef = uye or (ctx.message.reference.resolved.author if ctx.message.reference and isinstance(ctx.message.reference.resolved, discord.Message) and isinstance(ctx.message.reference.resolved.author, discord.Member) else None)
    if hedef is None:
        await ctx.send(embed=kullanim_embedi(".cezagecmisi @uye"))
        return
    ayarlar = ayarlari_yukle().get(str(ctx.guild.id), {})
    warnlar = ayarlar.get("uyarilar", {}).get(str(hedef.id), [])
    jail_kayit = _jail_ayar_al(ctx.guild.id).get("kayitlar", {}).get(str(hedef.id))
    timeout_var = "Evet" if hedef.timed_out_until and hedef.timed_out_until > datetime.now(timezone.utc) else "Hayir"
    embed = discord.Embed(title=" Ceza Gecmisi", description=f"{hedef.mention} icin kayitlar", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Uyari Sayisi", value=str(len(warnlar)), inline=True)
    embed.add_field(name="Aktif Timeout", value=timeout_var, inline=True)
    embed.add_field(name="Aktif Jail", value="Evet" if jail_kayit else "Hayir", inline=True)
    if warnlar:
        son_warn = "\n".join(f" {k.get('sebep', 'Sebep yok')}" for k in warnlar[-5:])
        embed.add_field(name="Son Uyarilar", value=son_warn[:1024], inline=False)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


@bot.command(name="temprol")
@commands.has_permissions(manage_roles=True)
async def temprol(ctx, uye: discord.Member = None, rol: discord.Role = None, *, arguman: str = ""):
    if not uye or not rol:
        await ctx.send(embed=kullanim_embedi(".temprol @uye @rol 10 dakika"))
        return
    saniye, _ = _turkce_sure_parcala(arguman)
    if saniye <= 0:
        await ctx.send(embed=hata_embedi("Sure Hatasi", "Gecerli bir sure yazmalisin. Ornek: 10 dakika"))
        return
    await uye.add_roles(rol, reason=f"{ctx.author} tarafindan sureli rol verildi")
    veri = _temprol_ayar_al(ctx.guild.id)
    kayitlar = veri.get("kayitlar", [])
    kayitlar.append({"uye_id": uye.id, "rol_id": rol.id, "bitis": (datetime.now(timezone.utc) + timedelta(seconds=saniye)).isoformat()})
    veri["kayitlar"] = kayitlar[-200:]
    _temprol_ayar_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title=" Sureli Rol Verildi", description=f"{uye.mention} kullanicisina {rol.mention} rolu verildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="otocevap")
@commands.has_permissions(manage_guild=True)
async def oto_cevap(ctx, anahtar: str = None, *, cevap: str = None):
    if not anahtar or not cevap:
        await ctx.send(embed=kullanim_embedi(".otocevap merhaba Selam, hos geldin!"))
        return
    ayar = _auto_cevap_ayar_al(ctx.guild.id)
    kayitlar = [k for k in ayar.get("kayitlar", []) if str(k.get("anahtar", "")).lower() != anahtar.lower()]
    kayitlar.append({"anahtar": anahtar, "cevap": cevap})
    ayar["kayitlar"] = kayitlar[-100:]
    ayar["aktif"] = True
    _auto_cevap_kaydet(ctx.guild.id, ayar)
    await ctx.send(embed=discord.Embed(title=" Oto Cevap Kaydedildi", description=f"Anahtar: **{anahtar}**", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="sayac")
@commands.has_permissions(manage_guild=True)
async def sayac(ctx, hedef: int = 0, kanal: discord.TextChannel = None, *, mesaj: str = None):
    if hedef <= 0 or kanal is None:
        await ctx.send(embed=kullanim_embedi(".sayac 500 #kanal Hedefe ulastik! {member_count}/{target}"))
        return
    veri = {"aktif": True, "hedef": hedef, "kanal_id": kanal.id, "mesaj": mesaj or " Seninle birlikte {member_count} kisiyiz! Hedefimiz {target} idi.", "tetiklendi": False}
    _sayac_ayar_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title=" Sayac Ayarlandi", description=f"Hedef: **{hedef}**  Kanal: {kanal.mention}", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


class GenelRolSec(discord.ui.Select):
    def __init__(self, guild_id: int, rol_idleri: list[int]):
        self.rol_idleri = rol_idleri
        guild = bot.get_guild(guild_id)
        roller = [guild.get_role(rid) for rid in rol_idleri] if guild else []
        roller = [r for r in roller if r]
        secenekler = [discord.SelectOption(label=r.name[:100], value=str(r.id), description=f"{len(r.members)} uye") for r in roller[:25]]
        super().__init__(placeholder="Bir rol sec", min_values=1, max_values=max(1, len(secenekler)), options=secenekler)

    async def callback(self, interaction: discord.Interaction):
        roller = [interaction.guild.get_role(int(v)) for v in self.values]
        roller = [r for r in roller if r]
        if roller:
            await interaction.user.add_roles(*roller, reason="Rol menu secimi")
        await interaction.response.send_message("Roller eklendi.", ephemeral=True)


class GenelRolMenuView(discord.ui.View):
    def __init__(self, guild_id: int, rol_idleri: list[int]):
        super().__init__(timeout=None)
        self.add_item(GenelRolSec(guild_id, rol_idleri))


@bot.command(name="rolmenu")
@commands.has_permissions(manage_roles=True)
async def rol_menu(ctx, *roller: discord.Role):
    if not roller:
        await ctx.send(embed=kullanim_embedi(".rolmenu @rol1 @rol2 @rol3"))
        return
    embed = discord.Embed(title=" Rol Menusu", description="Asagidan istedigin rolleri secebilirsin.", color=RENKLER["rol"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Roller", value="\n".join(r.mention for r in roller[:25]), inline=False)
    await ctx.send(embed=embed, view=GenelRolMenuView(ctx.guild.id, [r.id for r in roller]))


@bot.command(name="notekle")
@commands.has_permissions(manage_guild=True)
async def not_ekle(ctx, uye: discord.Member = None, *, not_metni: str = None):
    if not uye or not not_metni:
        await ctx.send(embed=kullanim_embedi(".notekle @uye metin"))
        return
    veri = _notlar_al(ctx.guild.id)
    kayitlar = veri.setdefault(str(uye.id), [])
    kayitlar.append({"yazan": ctx.author.id, "metin": not_metni, "zaman": datetime.now(timezone.utc).isoformat()})
    veri[str(uye.id)] = kayitlar[-20:]
    _notlar_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title=" Uye Notu Eklendi", description=f"{uye.mention} icin not kaydedildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="isimgecmisi")
@commands.has_permissions(manage_guild=True)
async def isim_gecmisi(ctx, uye: discord.Member = None):
    if not uye:
        await ctx.send(embed=kullanim_embedi(".isimgecmisi @uye"))
        return
    veri = _isim_gecmisi_al(ctx.guild.id).get(str(uye.id), [])
    satirlar = [f" {k.get('eski')}  {k.get('yeni')}" for k in veri[-10:]]
    await ctx.send(embed=discord.Embed(title=" Isim Gecmisi", description="\n".join(satirlar) or "Kayit yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="sesistatistik")
async def ses_istatistik(ctx):
    ayarlar = ayarlari_yukle().get(str(ctx.guild.id), {}).get("profil_istat", {})
    satirlar = []
    for uye_id, veri in sorted(ayarlar.items(), key=lambda x: int(x[1].get("voice_seconds", 0)), reverse=True)[:10]:
        uye = ctx.guild.get_member(int(uye_id))
        if uye:
            satirlar.append(f" {uye.mention}  {_sureyi_formatla(int(veri.get('voice_seconds', 0)))}")
    await ctx.send(embed=discord.Embed(title=" Ses Istatistik", description="\n".join(satirlar) or "Kayit yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="mesajistatistik")
async def mesaj_istatistik(ctx):
    ayarlar = ayarlari_yukle().get(str(ctx.guild.id), {}).get("profil_istat", {})
    satirlar = []
    for uye_id, veri in sorted(ayarlar.items(), key=lambda x: int(x[1].get("message_count", 0)), reverse=True)[:10]:
        uye = ctx.guild.get_member(int(uye_id))
        if uye:
            satirlar.append(f" {uye.mention}  {int(veri.get('message_count', 0))} mesaj")
    await ctx.send(embed=discord.Embed(title=" Mesaj Istatistik", description="\n".join(satirlar) or "Kayit yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="kurulumdurum")
@commands.has_permissions(manage_guild=True)
async def kurulum_durum(ctx):
    ticket = ticket_ayar_al(ctx.guild.id)
    level = _level_ayar_al(ctx.guild.id)
    hosgeldin = _welcome_ayar_al(ctx.guild.id)
    karsilama = _karsilama_ayar_al(ctx.guild.id)
    guvenlik = _guvenlik_ayar_al(ctx.guild.id)
    jail = _jail_ayar_al(ctx.guild.id)
    embed = discord.Embed(title=" Kurulum Durumu", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Ticket", value="" if ticket.get("kategori") else "", inline=True)
    embed.add_field(name="Level", value="" if level.get("kanal_id") else "", inline=True)
    embed.add_field(name="Hosgeldin", value="" if hosgeldin.get("kanal_id") else "", inline=True)
    embed.add_field(name="Karsilama", value="" if karsilama.get("kanal_id") else "", inline=True)
    embed.add_field(name="Guvenlik", value="" if guvenlik.get("aktif") else "", inline=True)
    embed.add_field(name="Jail", value="" if jail.get("aktif") else "", inline=True)
    embed.add_field(name="Partner", value="" if partner_kanal_id_al(ctx.guild.id) else "", inline=True)
    embed.add_field(name="Oto Cevap", value="" if _auto_cevap_ayar_al(ctx.guild.id).get("kayitlar") else "", inline=True)
    embed.add_field(name="Spam", value="" if _guild_ayar_al(ctx.guild.id).get("guvenlik_spam_koruma", {}).get("aktif") else "", inline=True)
    await ctx.send(embed=embed)


@bot.command(name="yasakli-komut")
@commands.has_permissions(manage_guild=True)
async def yasakli_komut(ctx, kanal: discord.TextChannel = None, *komutlar):
    if kanal is None or not komutlar:
        await ctx.send(embed=kullanim_embedi(".yasakli-komut #kanal mute ban kick"))
        return
    veri = _yasakli_komutlar_al(ctx.guild.id)
    mevcut = set(veri.get(str(kanal.id), []))
    for komut in komutlar:
        komut = komut.lstrip(".").lower()
        if komut in mevcut:
            mevcut.remove(komut)
        else:
            mevcut.add(komut)
    veri[str(kanal.id)] = sorted(mevcut)
    _yasakli_komutlar_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title=" Yasakli Komutlar Guncellendi", description=f"{kanal.mention} icin: {', '.join(sorted(mevcut)) or 'Yok'}", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


try:
    bot.remove_command("yardim")
    bot.remove_command("help")
    bot.remove_command("yardm")
except Exception:
    pass


@bot.command(name="yardim", aliases=["help", "yardm"])
async def yardim_canli(ctx):
    sahibi_id = ctx.author.id
    kategoriler = {
        " Ayarlar": ["ticketpanel", "ticketkur", "levelkur", "hosgeldinkur", "karsilamakur", "guvenlikkur", "jailkur", "sayac", "kurulumdurum"],
        " Moderasyon": ["ban", "blupbum", "kick", "mute", "unmute", "warn", "uyarlar", "uyarsil", "jail", "unjail", "temprol"],
        " Roller": ["renkpanel", "rolmenu", "animerolpanel", "animerollerikur", "animerollerikaldir", "asagitasi"],
        " Sistemler": ["gifcevap", "otocevap", "spam-koruma-kur", "spam-koruma-durum", "spam-koruma-muaf-rol", "spam-koruma-muaf-kanal", "kufur-kur", "yetkilikufurkur", "yasakli-komut"],
        " Kullanici": ["profil", "sunucu", "sunucupanel", "sesistatistik", "mesajistatistik", "isimgecmisi", "notekle", "cezagecmisi", "yetkilipanel"],
    }

    def ana_embed():
        embed = discord.Embed(
            title=" Blup Komut Menusu",
            description="Canli, renkli ve sade bir yardim menusu.\nAsagidaki menuden kategori secip komutlari inceleyebilirsin.",
            color=0xFF66C4,
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(
            name=" Kategoriler",
            value="\n".join(f"{k}  {len(v)} komut" for k, v in kategoriler.items()),
            inline=False
        )
        embed.add_field(
            name=" Populer Komutlar",
            value="profil  ticketpanel  levelkur  gifcevap  jailkur  kurulumdurum",
            inline=False
        )
        embed.set_footer(text=f"{sum(len(v) for v in kategoriler.values())} komut  {zaman_damgasi()}")
        return embed

    def kategori_embed(baslik: str):
        renkler = [0xFF66C4, 0x5865F2, 0x57F287, 0xFEE75C, 0xED4245]
        komut_listesi = [f" .{k}" for k in kategoriler.get(baslik, [])]
        embed = discord.Embed(
            title=baslik,
            description="\n".join(komut_listesi) or "Komut yok.",
            color=random.choice(renkler),
            timestamp=datetime.now(timezone.utc)
        )
        embed.set_footer(text=zaman_damgasi())
        return embed

    class KategoriSec(discord.ui.Select):
        def __init__(self):
            secenekler = [discord.SelectOption(label=k.replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", "").replace(" ", ""), value=k, description=f"{len(v)} komut", emoji=k.split()[0]) for k, v in kategoriler.items()]
            super().__init__(placeholder="Bir kategori sec", options=secenekler, min_values=1, max_values=1)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            await interaction.response.edit_message(embed=kategori_embed(self.values[0]), view=view)

    class KisaYolSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label="Ana Menu", value="ana", emoji=""),
                discord.SelectOption(label="Moderasyon", value=" Moderasyon", emoji=""),
                discord.SelectOption(label="Sistemler", value=" Sistemler", emoji=""),
            ]
            super().__init__(placeholder="Hizli gecis", options=secenekler, min_values=1, max_values=1)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            if self.values[0] == "ana":
                await interaction.response.edit_message(embed=ana_embed(), view=view)
            else:
                await interaction.response.edit_message(embed=kategori_embed(self.values[0]), view=view)

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.add_item(KategoriSec())
            self.add_item(KisaYolSec())

        async def interaction_check(self, interaction: discord.Interaction) -> bool:
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return False
            return True

    view = HelpView()
    await ctx.send(embed=ana_embed(), view=view)


for _yardim_eski in ("yardim", "help", "yardm"):
    try:
        bot.remove_command(_yardim_eski)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["help", "yardm"])
async def yardim_renkli(ctx):
    sahibi_id = ctx.author.id

    komutlar = {}
    for komut in bot.commands:
        if komut.hidden:
            continue
        ad = komut.name
        if ad in {"yardim", "help", "yardm"}:
            continue
        kategori = "Diger"
        if any(k in ad for k in ["ban", "kick", "mute", "unmute", "warn", "sil", "jail"]):
            kategori = "Moderasyon"
        elif any(k in ad for k in ["ticket", "partner", "level", "hosgeldin", "karsilama", "gifcevap", "guvenlik", "kufur", "antilink", "spam"]):
            kategori = "Sistemler"
        elif any(k in ad for k in ["renk", "anime", "rol"]):
            kategori = "Roller"
        elif any(k in ad for k in ["profil", "afk"]):
            kategori = "Kullanici"
        elif any(k in ad for k in ["log", "uygulama"]):
            kategori = "Ayarlar"
        komutlar.setdefault(kategori, []).append(komut)

    kategori_simgeleri = {
        "Ayarlar": "",
        "Moderasyon": "",
        "Roller": "",
        "Sistemler": "",
        "Kullanici": "",
        "Diger": "",
    }
    kategori_renkleri = {
        "Ayarlar": 0x5865F2,
        "Moderasyon": 0xED4245,
        "Roller": 0xFEE75C,
        "Sistemler": 0x57F287,
        "Kullanici": 0xEB459E,
        "Diger": 0x2ECC71,
    }
    kategori_sirasi = ["Ayarlar", "Moderasyon", "Roller", "Sistemler", "Kullanici", "Diger"]

    def komut_satirlari(kategori: str) -> str:
        liste = sorted(komutlar.get(kategori, []), key=lambda k: k.name)
        return "\n".join(f"{kategori_simgeleri.get(kategori, '')} .{k.name}" for k in liste[:25]) or "Komut bulunamadi."

    def ana_embed():
        embed = discord.Embed(
            title=" Blup Help Menusu",
            description="Kategorileri asagidan secerek komutlari goruntuleyebilirsin.",
            color=0x5865F2,
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(
            name=" Kisa Ozet",
            value="\n".join(
                f"{kategori_simgeleri.get(k, '')} **{k}**  {len(komutlar.get(k, []))} komut"
                for k in kategori_sirasi if komutlar.get(k)
            ),
            inline=False
        )
        embed.add_field(
            name=" Hizli Baslangic",
            value=".profil  .ticketpanel  .levelkur  .gifcevap  .jailkur  .spam-koruma-durum",
            inline=False
        )
        embed.set_footer(text=f"Toplam {sum(len(v) for v in komutlar.values())} komut  {zaman_damgasi()}")
        return embed

    def kategori_embed(kategori: str):
        embed = discord.Embed(
            title=f"{kategori_simgeleri.get(kategori, '')} {kategori} Komutlari",
            description=komut_satirlari(kategori),
            color=kategori_renkleri.get(kategori, 0x5865F2),
            timestamp=datetime.now(timezone.utc)
        )
        embed.set_footer(text=zaman_damgasi())
        return embed

    class KategoriSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label=k, value=k, description=f"{len(komutlar.get(k, []))} komut", emoji=kategori_simgeleri.get(k, ""))
                for k in kategori_sirasi if komutlar.get(k)
            ]
            super().__init__(placeholder="Bir kategori sec", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            await interaction.response.edit_message(embed=kategori_embed(self.values[0]), view=view)

    class YardimMenuSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label="Ana Menu", value="ana", description="Baslangic ekranina don", emoji=""),
                discord.SelectOption(label="Sistemler", value="Sistemler", description="Tum sistem komutlari", emoji=""),
                discord.SelectOption(label="Moderasyon", value="Moderasyon", description="Ceza ve yonetim komutlari", emoji=""),
            ]
            super().__init__(placeholder="Hizli gecis", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            if self.values[0] == "ana":
                await interaction.response.edit_message(embed=ana_embed(), view=view)
                return
            await interaction.response.edit_message(embed=kategori_embed(self.values[0]), view=view)

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.add_item(KategoriSec())
            self.add_item(YardimMenuSec())

        async def interaction_check(self, interaction: discord.Interaction) -> bool:
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return False
            return True

    view = HelpView()
    await ctx.send(embed=ana_embed(), view=view)


def _turkce_sure_parcala(metin: str):
    if not metin:
        return 0, ""
    eslesmeler = list(re.finditer(r"(\d+)\s*(g[u]n|saat|dakika|saniye|sn|dk|g|h|m|s)\b", metin.lower()))
    if not eslesmeler:
        return 0, metin.strip()

    birimler = {
        "g": 86400, "gun": 86400, "gn": 86400,
        "h": 3600, "saat": 3600,
        "m": 60, "dk": 60, "dakika": 60,
        "s": 1, "sn": 1, "saniye": 1,
    }
    toplam = 0
    for eslesme in eslesmeler:
        adet = int(eslesme.group(1))
        birim = eslesme.group(2)
        toplam += adet * birimler.get(birim, 0)

    kalan = re.sub(r"(\d+)\s*(g[u]n|saat|dakika|saniye|sn|dk|g|h|m|s)\b", "", metin, flags=re.IGNORECASE).strip()
    return toplam, kalan


async def _mute_hedef_bul(ctx, uye):
    if uye is not None:
        return uye
    if ctx.message.reference and ctx.message.reference.resolved:
        kaynak = ctx.message.reference.resolved
        if isinstance(kaynak, discord.Message) and isinstance(kaynak.author, discord.Member):
            return kaynak.author
    return None


try:
    bot.remove_command("mute")
except Exception:
    pass


@bot.command(name="mute")
@commands.has_permissions(moderate_members=True)
async def mute_yeni(ctx, uye: discord.Member = None, *, arguman: str = ""):
    hedef = await _mute_hedef_bul(ctx, uye)
    if hedef is None:
        await ctx.send(embed=kullanim_embedi("`.mute @uye 10 dakika sebep`\nveya bir mesaja yanit verip `.mute 10 dakika sebep`"))
        return
    if hedef == ctx.author:
        await ctx.send(embed=hata_embedi("Gecersiz Islem", "Kendini susturamazsin."))
        return
    if hedef.top_role >= ctx.author.top_role:
        await ctx.send(embed=hata_embedi("Yetki Hatasi", "Bu uyeyi susturacak yetkin yok."))
        return

    saniye, kalan_sebep = _turkce_sure_parcala(arguman.strip())
    if saniye <= 0:
        saniye = 2419200
        sure_goster = "28 gun"
        sebep = arguman.strip() if arguman.strip() else "Sebep belirtilmedi"
    else:
        sure_goster = arguman.strip()
        sebep = kalan_sebep if kalan_sebep else "Sebep belirtilmedi"

    if saniye > 2419200:
        await ctx.send(embed=hata_embedi("Sure Hatasi", "Maksimum mute suresi 28 gundur."))
        return

    bitis = datetime.now(timezone.utc) + timedelta(seconds=saniye)
    await hedef.timeout(timedelta(seconds=saniye), reason=f"{ctx.author}: {sebep}")

    embed = mod_embed("Uye Susturuldu", RENKLER["mute"], **{
        "Uye": f"{hedef.mention} `{hedef}`",
        "Sure": sure_goster,
        "Bitis": bitis.strftime("%d.%m.%Y %H:%M UTC"),
        "Sebep": sebep,
        "Yetkili": ctx.author.mention
    })
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mute_log", embed)


def _xp_hedef(level: int) -> int:
    return 5 * (level ** 2) + (50 * level) + 100


def _xp_veri_al(guild_id: int, user_id: int) -> dict:
    ayarlar = ayarlari_yukle()
    gk, uk = str(guild_id), str(user_id)
    if gk not in ayarlar:
        ayarlar[gk] = {}
    if "level_xp" not in ayarlar[gk]:
        ayarlar[gk]["level_xp"] = {}
    if uk not in ayarlar[gk]["level_xp"]:
        ayarlar[gk]["level_xp"][uk] = {"xp": 0, "level": 0}
        ayarlari_kaydet(ayarlar)
    return ayarlar[gk]["level_xp"][uk]


def _xp_veri_kaydet(guild_id: int, user_id: int, veri: dict):
    def _guncelle(ayarlar):
        gk, uk = str(guild_id), str(user_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        if "level_xp" not in ayarlar[gk]:
            ayarlar[gk]["level_xp"] = {}
        ayarlar[gk]["level_xp"][uk] = veri

    ayarlari_guncelle(_guncelle)


def _sablon_doldur(sablon: str, uye: discord.Member, level: int = 0, xp: int = 0) -> str:
    try:
        return sablon.format(
            user=str(uye),
            username=uye.name,
            member=uye.mention,
            uye=uye.mention,
            member_mention=uye.mention,
            user_mention=uye.mention,
            mention=uye.mention,
            level=level,
            xp=xp,
            guild=uye.guild.name,
            guild_name=uye.guild.name,
            member_count=uye.guild.member_count
        )
    except KeyError:
        return sablon.replace("{member}", uye.mention).replace("{user}", str(uye)).replace("{mention}", uye.mention)


def _kanal_id_coz(raw: str) -> int | None:
    ham = (raw or "").strip()
    if not ham:
        return None
    ham = ham.replace("<#", "").replace(">", "").strip()
    return int(ham) if ham.isdigit() else None


def _gecerli_http_url_mu(raw: str) -> bool:
    ham = (raw or "").strip()
    return ham.startswith("http://") or ham.startswith("https://")


def _hosgeldin_icerigi_hazirla(uye: discord.Member, ayar: dict) -> tuple[str, discord.Embed]:
    rol_mentionlari = []
    for rol_id in ayar.get("rol_ids", []):
        rol = uye.guild.get_role(rol_id)
        if rol:
            rol_mentionlari.append(rol.mention)

    ust_metin = uye.mention
    if rol_mentionlari:
        ust_metin += " " + " ".join(rol_mentionlari)

    e = discord.Embed(
        title="Ho Geldin!",
        description=_sablon_doldur(ayar.get("mesaj", "Ho geldin {member_mention}!"), uye),
        color=RENKLER["giris"],
        timestamp=datetime.now(timezone.utc)
    )
    if _gecerli_http_url_mu(ayar.get("gif_url")):
        e.set_image(url=ayar["gif_url"])
    if uye.display_avatar:
        e.set_thumbnail(url=uye.display_avatar.url)
    e.set_footer(text=zaman_damgasi())
    return ust_metin, e


def _karsilama_mesaji_hazirla(uye: discord.Member, ayar: dict) -> str:
    mesaj = _sablon_doldur(
        ayar.get("mesaj", "Aramza ho geldin {username}. Seninle birlikte {member_count} kiiyiz."),
        uye
    )
    return mesaj


def _level_odul_rollerini_coz(guild: discord.Guild, ayar: dict, level: int) -> list[discord.Role]:
    roller = []
    for seviye_str, rol_id in (ayar.get("rol_odulleri", {}) or {}).items():
        try:
            seviye = int(seviye_str)
            rid = int(rol_id)
        except (TypeError, ValueError):
            continue
        if level >= seviye:
            rol = guild.get_role(rid)
            if rol:
                roller.append(rol)
    roller.sort(key=lambda r: r.position)
    return roller


@bot.command(name="seviye", aliases=["level", "rank"])
async def seviye_goster(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    veri = _xp_veri_al(ctx.guild.id, hedef.id)
    seviye = int(veri.get("level", 0))
    xp = int(veri.get("xp", 0))
    hedef_xp = _xp_hedef(seviye)
    e = discord.Embed(title="Seviye Bilgisi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    e.add_field(name="Kullanici", value=hedef.mention, inline=True)
    e.add_field(name="Level", value=str(seviye), inline=True)
    e.add_field(name="XP", value=f"{xp} / {hedef_xp}", inline=True)
    e.set_footer(text=zaman_damgasi())
    await ctx.send(embed=e)


@bot.command(name="levelrol")
@commands.has_permissions(manage_guild=True)
async def level_rol_ayarla(ctx, seviye: int = None, rol: discord.Role = None):
    if seviye is None or rol is None:
        await ctx.send("Kullanim: `.levelrol <seviye> @rol`")
        return
    if seviye < 1:
        await ctx.send("Seviye en az 1 olmali.")
        return
    ayar = _level_ayar_al(ctx.guild.id)
    oduller = dict(ayar.get("rol_odulleri", {}))
    oduller[str(seviye)] = rol.id
    ayar["rol_odulleri"] = oduller
    _level_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(f"Level odulu kaydedildi: **{seviye}. seviye** -> {rol.mention}")


@bot.command(name="levelrolsil")
@commands.has_permissions(manage_guild=True)
async def level_rol_sil(ctx, seviye: int = None):
    if seviye is None:
        await ctx.send("Kullanim: `.levelrolsil <seviye>`")
        return
    ayar = _level_ayar_al(ctx.guild.id)
    oduller = dict(ayar.get("rol_odulleri", {}))
    if str(seviye) not in oduller:
        await ctx.send("Bu seviye icin kayitli bir rol odulu yok.")
        return
    oduller.pop(str(seviye), None)
    ayar["rol_odulleri"] = oduller
    _level_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(f"**{seviye}. seviye** rol odulu silindi.")


@bot.command(name="levelrolleri")
async def level_rolleri_liste(ctx):
    ayar = _level_ayar_al(ctx.guild.id)
    oduller = []
    for seviye_str, rol_id in sorted((ayar.get("rol_odulleri", {}) or {}).items(), key=lambda x: int(x[0])):
        rol = ctx.guild.get_role(int(rol_id))
        if rol:
            oduller.append(f"`{seviye_str}` -> {rol.mention}")
    await ctx.send("Level rol odulleri:\n" + ("\n".join(oduller) if oduller else "Hic rol odulu ayarlanmamis."))


@bot.command(name="profil", aliases=["profile"])
async def profil_goster(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    veri = _xp_veri_al(ctx.guild.id, hedef.id)
    istat = _profil_istat_al(ctx.guild.id, hedef.id)
    tum_xp = _toplam_xp_hesapla(int(veri.get("level", 0)), int(veri.get("xp", 0)))
    tum_xp_veri = ayarlari_yukle().get(str(ctx.guild.id), {}).get("level_xp", {})
    sirali = sorted(
        tum_xp_veri.items(),
        key=lambda item: _toplam_xp_hesapla(int(item[1].get("level", 0)), int(item[1].get("xp", 0))),
        reverse=True
    )
    sira = next((i for i, (uid, _) in enumerate(sirali, 1) if uid == str(hedef.id)), None)
    e = discord.Embed(
        title=f"{hedef.display_name}  Profil",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    e.add_field(name="Seviye", value=f"**{veri.get('level', 0)}**", inline=True)
    e.add_field(name="Toplam XP", value=f"**{tum_xp}**", inline=True)
    e.add_field(name="Siralama", value=f"**#{sira or '-'}**", inline=True)
    e.add_field(name="Mesaj", value=f"**{istat.get('message_count', 0)}**", inline=True)
    e.add_field(name="Ses", value=f"**{_sureyi_formatla(istat.get('voice_seconds', 0))}**", inline=True)
    e.add_field(name="Katilim", value=hedef.joined_at.strftime("%d.%m.%Y %H:%M") if hedef.joined_at else "Bilinmiyor", inline=True)
    if hedef.display_avatar:
        e.set_thumbnail(url=hedef.display_avatar.url)
    e.set_footer(text=f"{ctx.guild.name}  {zaman_damgasi()}")
    await ctx.send(embed=e)


@bot.command(name="hosgeldindurum")
async def hosgeldin_durum(ctx):
    ayar = _welcome_ayar_al(ctx.guild.id)
    kanal = ctx.guild.get_channel(ayar.get("kanal_id")) if ayar.get("kanal_id") else None
    roller = [ctx.guild.get_role(rid) for rid in ayar.get("rol_ids", [])]
    roller = [r.mention for r in roller if r]
    e = discord.Embed(title="Hosgeldin Sistemi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    e.add_field(name="Kanal", value=kanal.mention if kanal else "Ayarlanmamis", inline=False)
    e.add_field(name="Mesaj", value=ayar.get("mesaj", "-"), inline=False)
    e.add_field(name="GIF", value=ayar.get("gif_url") or "Yok", inline=False)
    e.add_field(name="Roller", value=", ".join(roller) if roller else "Yok", inline=False)
    await ctx.send(embed=e)


@bot.command(name="karsilamadurum", aliases=["karlama-durum", "karsilama-durum"])
async def karsilama_durum(ctx):
    ayar = _karsilama_ayar_al(ctx.guild.id)
    kanal = ctx.guild.get_channel(ayar.get("kanal_id")) if ayar.get("kanal_id") else None
    e = discord.Embed(title="Karlama Mesaj Sistemi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    e.add_field(name="Kanal", value=kanal.mention if kanal else "Ayarlanmam", inline=False)
    e.add_field(name="Mesaj", value=ayar.get("mesaj", "-"), inline=False)
    await ctx.send(embed=e)


@bot.command(name="leveldurum")
async def level_durum(ctx):
    ayar = _level_ayar_al(ctx.guild.id)
    kanal = ctx.guild.get_channel(ayar.get("kanal_id")) if ayar.get("kanal_id") else None
    rol_odulleri = []
    for seviye_str, rol_id in sorted((ayar.get("rol_odulleri", {}) or {}).items(), key=lambda x: int(x[0])):
        rol = ctx.guild.get_role(int(rol_id))
        if rol:
            rol_odulleri.append(f"`{seviye_str}` -> {rol.mention}")
    e = discord.Embed(title="Level Sistemi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    e.add_field(name="Kanal", value=kanal.mention if kanal else "Ayarlanmamis", inline=False)
    e.add_field(name="Mesaj", value=ayar.get("mesaj", "-"), inline=False)
    e.add_field(name="GIF", value=ayar.get("gif_url") or "Yok", inline=False)
    e.add_field(name="Rol Odulleri", value="\n".join(rol_odulleri) if rol_odulleri else "Yok", inline=False)
    await ctx.send(embed=e)


@bot.listen("on_member_join")
async def hosgeldin_listener(member: discord.Member):
    ayar = _welcome_ayar_al(member.guild.id)
    kanal_id = ayar.get("kanal_id")
    if not kanal_id:
        return
    kanal = member.guild.get_channel(kanal_id)
    if not isinstance(kanal, discord.TextChannel):
        return

    try:
        mesaj_ust, e = _hosgeldin_icerigi_hazirla(member, ayar)
        await kanal.send(mesaj_ust, embed=e)
    except discord.Forbidden:
        print(f"[UYARI] Hosgeldin mesaji gonderilemedi: yetki yok | guild={member.guild.id} kanal={kanal.id}")
    except Exception as e:
        print(f"[HATA] Hosgeldin listener: {e}")


@bot.listen("on_member_join")
async def karsilama_listener(member: discord.Member):
    ayar = _karsilama_ayar_al(member.guild.id)
    kanal_id = ayar.get("kanal_id")
    if not kanal_id:
        return
    kanal = member.guild.get_channel(kanal_id)
    if not isinstance(kanal, discord.TextChannel):
        return
    try:
        mesaj = _karsilama_mesaji_hazirla(member, ayar)
        dosya = await member.display_avatar.to_file(filename="karsilama-avatar.png") if member.display_avatar else None
        if dosya:
            await kanal.send(mesaj, file=dosya)
        else:
            await kanal.send(mesaj)
    except discord.Forbidden:
        print(f"[UYARI] Karsilama mesaji gonderilemedi: yetki yok | guild={member.guild.id} kanal={kanal.id}")
    except Exception as e:
        print(f"[HATA] Karsilama listener: {e}")


@bot.listen("on_message")
async def level_xp_listener(message: discord.Message):
    if message.author.bot or not message.guild:
        return

    _profil_bekleyen_arttir(message.guild.id, message.author.id, mesaj_delta=1)

    anahtar = (message.guild.id, message.author.id)
    simdi_ts = datetime.now(timezone.utc).timestamp()
    son = _LEVEL_XP_COOLDOWN.get(anahtar, 0)
    if (simdi_ts - son) < _LEVEL_COOLDOWN_SANIYE:
        return
    _LEVEL_XP_COOLDOWN[anahtar] = simdi_ts

    veri = _xp_veri_al(message.guild.id, message.author.id)
    onceki_level = int(veri.get("level", 0))
    yeni_xp = int(veri.get("xp", 0)) + random.randint(8, 15)
    yeni_level = onceki_level

    while yeni_xp >= _xp_hedef(yeni_level):
        yeni_xp -= _xp_hedef(yeni_level)
        yeni_level += 1

    veri["xp"] = yeni_xp
    veri["level"] = yeni_level
    _xp_veri_kaydet(message.guild.id, message.author.id, veri)

    if yeni_level <= onceki_level:
        return

    ayar = _level_ayar_al(message.guild.id)
    odul_rolleri = [rol for rol in _level_odul_rollerini_coz(message.guild, ayar, yeni_level) if rol not in message.author.roles]
    if odul_rolleri:
        try:
            await message.author.add_roles(*odul_rolleri, reason=f"Level odulu: {yeni_level}. seviye")
        except discord.Forbidden:
            pass
        except discord.HTTPException:
            pass

    kanal_id = ayar.get("kanal_id")
    if not kanal_id:
        return
    kanal = message.guild.get_channel(kanal_id)
    if not kanal:
        return

    aciklama = _sablon_doldur(ayar.get("mesaj", ""), message.author, level=yeni_level, xp=yeni_xp)
    e = discord.Embed(
        title="Seviye Atladin!",
        description=aciklama,
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    e.add_field(name="Yeni Level", value=f"**{yeni_level}**", inline=True)
    e.add_field(name="Kalan XP", value=f"**{yeni_xp} / {_xp_hedef(yeni_level)}**", inline=True)
    if odul_rolleri:
        e.add_field(name="Rol Odulu", value=", ".join(rol.mention for rol in odul_rolleri), inline=False)
    if ayar.get("gif_url"):
        e.set_image(url=ayar["gif_url"])
    if message.author.display_avatar:
        e.set_thumbnail(url=message.author.display_avatar.url)
    e.set_footer(text=zaman_damgasi())

    try:
        await kanal.send(message.author.mention, embed=e)
    except discord.Forbidden:
        pass


@bot.command(name="logkurkanal", aliases=["log-kanal-kur", "logkanalkur"])
@commands.has_permissions(manage_guild=True, manage_channels=True)
async def log_kur_kanal_olustur(ctx):
    kategori_ad = "LOG KANALLARI"
    kategori = discord.utils.get(ctx.guild.categories, name=kategori_ad)
    if kategori is None:
        kategori = await ctx.guild.create_category(kategori_ad, reason=f"{ctx.author} tarafindan log kanallari icin olusturuldu")

    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    if gk not in ayarlar:
        ayarlar[gk] = {}

    olusturulanlar = []
    mevcutlar = []

    for tur in LOG_TURLERI.keys():
        kanal_adi = LOG_KANAL_KALIPLARI.get(tur, [tur])[0]
        kanal = discord.utils.get(ctx.guild.text_channels, name=kanal_adi)
        if kanal is None:
            kanal = await ctx.guild.create_text_channel(
                kanal_adi,
                category=kategori,
                reason=f"{ctx.author} tarafindan .logkurkanal komutu ile olusturuldu"
            )
            olusturulanlar.append(kanal.mention)
        else:
            mevcutlar.append(kanal.mention)
            if kanal.category_id != kategori.id:
                try:
                    await kanal.edit(category=kategori, reason="Log kategori duzeni")
                except discord.Forbidden:
                    pass
        ayarlar[gk][tur] = kanal.id

    ayarlari_kaydet(ayarlar)

    e = discord.Embed(
        title="Log Kanallari Hazir",
        description="Eksik log kanallari olusturuldu ve sisteme kaydedildi.",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    e.add_field(name="Olusturulan", value="\n".join(olusturulanlar[:20]) if olusturulanlar else "Yeni kanal olusturulmadi.", inline=False)
    e.add_field(name="Zaten Vardi", value="\n".join(mevcutlar[:20]) if mevcutlar else "Yok", inline=False)
    e.set_footer(text=zaman_damgasi())
    await ctx.send(embed=e)


# 
#  MODAL TABANLI LEVEL / HOSGELDIN KURULUMU
# 

class LevelKurModal(discord.ui.Modal, title="Level Sistemi Kurulumu"):
    kanal_id = discord.ui.TextInput(
        label="Level duyuru kanal ID",
        placeholder="Ornek: 123456789012345678",
        required=True,
        max_length=25
    )
    mesaj = discord.ui.TextInput(
        label="Level atlama mesaji",
        style=discord.TextStyle.paragraph,
        required=True,
        max_length=1000,
        default="Tebrikler {member_mention}, {level}. seviyeye ulastin!"
    )
    gif_url = discord.ui.TextInput(
        label="GIF URL (opsiyonel, bos birak = temizle)",
        required=False,
        max_length=500
    )

    async def on_submit(self, interaction: discord.Interaction):
        kanal_id = _kanal_id_coz(self.kanal_id.value)
        if kanal_id is None:
            await interaction.response.send_message("Gecersiz kanal ID girdin.", ephemeral=True)
            return

        kanal = interaction.guild.get_channel(kanal_id) if interaction.guild else None
        if not isinstance(kanal, discord.TextChannel):
            await interaction.response.send_message("Bu ID ile metin kanali bulunamadi.", ephemeral=True)
            return

        ayar = _level_ayar_al(interaction.guild.id)
        ayar["kanal_id"] = kanal.id
        ayar["mesaj"] = (self.mesaj.value or "").strip()

        gif_raw = (self.gif_url.value or "").strip()
        if gif_raw.lower() in ("", "kapat", "sil", "off", "none"):
            ayar["gif_url"] = None
        else:
            ayar["gif_url"] = gif_raw

        _level_ayar_kaydet(interaction.guild.id, ayar)
        await interaction.response.send_message(
            f"Level sistemi modal ile kaydedildi.\nKanal: {kanal.mention}",
            ephemeral=True
        )

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        try:
            if interaction.response.is_done():
                await interaction.followup.send(f"Level modal hatasi: {error}", ephemeral=True)
            else:
                await interaction.response.send_message(f"Level modal hatasi: {error}", ephemeral=True)
        except Exception:
            pass


class HosgeldinKurModal(discord.ui.Modal, title="Hosgeldin Sistemi Kurulumu"):
    kanal_id = discord.ui.TextInput(
        label="Hosgeldin kanal ID",
        placeholder="Ornek: 123456789012345678",
        required=True,
        max_length=25
    )
    mesaj = discord.ui.TextInput(
        label="Hosgeldin mesaji",
        style=discord.TextStyle.paragraph,
        required=True,
        max_length=1000,
        default="Hos geldin {member_mention}! Keyifli vakit gecirmen dilegiyle."
    )
    gif_url = discord.ui.TextInput(
        label="GIF URL (opsiyonel)",
        required=False,
        max_length=500
    )
    rol_ids = discord.ui.TextInput(
        label="Etiket rol ID'leri (virgulle, opsiyonel)",
        placeholder="123,456,789",
        required=False,
        max_length=300
    )

    async def on_submit(self, interaction: discord.Interaction):
        kanal_id = _kanal_id_coz(self.kanal_id.value)
        if kanal_id is None:
            await interaction.response.send_message("Gecersiz kanal ID girdin.", ephemeral=True)
            return

        kanal = interaction.guild.get_channel(kanal_id) if interaction.guild else None
        if not isinstance(kanal, discord.TextChannel):
            await interaction.response.send_message("Bu ID ile metin kanali bulunamadi.", ephemeral=True)
            return

        rol_listesi = []
        rol_ham = (self.rol_ids.value or "").strip()
        if rol_ham:
            for parca in rol_ham.split(","):
                parca = parca.strip().replace("<@&", "").replace(">", "")
                if not parca:
                    continue
                if parca.isdigit():
                    rid = int(parca)
                    if interaction.guild.get_role(rid):
                        rol_listesi.append(rid)

        ayar = _welcome_ayar_al(interaction.guild.id)
        ayar["kanal_id"] = kanal.id
        ayar["mesaj"] = (self.mesaj.value or "").strip()
        ayar["rol_ids"] = list(dict.fromkeys(rol_listesi))

        gif_raw = (self.gif_url.value or "").strip()
        if gif_raw.lower() in ("", "kapat", "sil", "off", "none"):
            ayar["gif_url"] = None
        else:
            ayar["gif_url"] = gif_raw

        _welcome_ayar_kaydet(interaction.guild.id, ayar)
        await interaction.response.send_message(
            f"Hosgeldin sistemi modal ile kaydedildi.\nKanal: {kanal.mention}",
            ephemeral=True
        )

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        try:
            if interaction.response.is_done():
                await interaction.followup.send(f"Hosgeldin modal hatasi: {error}", ephemeral=True)
            else:
                await interaction.response.send_message(f"Hosgeldin modal hatasi: {error}", ephemeral=True)
        except Exception:
            pass


class KarsilamaKurModal(discord.ui.Modal, title="Karsilama Mesaji Kurulumu"):
    kanal_id = discord.ui.TextInput(
        label="Karsilama kanal ID",
        placeholder="Ornek: 123456789012345678",
        required=True,
        max_length=25
    )
    mesaj = discord.ui.TextInput(
        label="Karsilama metni",
        style=discord.TextStyle.paragraph,
        required=True,
        max_length=1000,
        default="Aramza ho geldin {username}. Seninle birlikte {member_count} kiiyiz."
    )

    async def on_submit(self, interaction: discord.Interaction):
        kanal_id = _kanal_id_coz(self.kanal_id.value)
        if kanal_id is None:
            await interaction.response.send_message("Geersiz kanal ID girdin.", ephemeral=True)
            return

        kanal = interaction.guild.get_channel(kanal_id) if interaction.guild else None
        if not isinstance(kanal, discord.TextChannel):
            await interaction.response.send_message("Bu ID ile metin kanal bulunamad.", ephemeral=True)
            return

        ayar = _karsilama_ayar_al(interaction.guild.id)
        ayar["kanal_id"] = kanal.id
        ayar["mesaj"] = (self.mesaj.value or "").strip()
        _karsilama_ayar_kaydet(interaction.guild.id, ayar)

        await interaction.response.send_message(
            f"Karlama mesaj sistemi kaydedildi.\nKanal: {kanal.mention}",
            ephemeral=True
        )

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        try:
            if interaction.response.is_done():
                await interaction.followup.send(f"Karlama modal hatas: {error}", ephemeral=True)
            else:
                await interaction.response.send_message(f"Karlama modal hatas: {error}", ephemeral=True)
        except Exception:
            pass


class GuvenlikKurModal(discord.ui.Modal, title="Guvenlik Sistemi"):
    log_kanal_id = discord.ui.TextInput(
        label="Log kanal ID",
        placeholder="Ornek: 123456789012345678",
        required=True,
        max_length=25
    )
    sure_saniye = discord.ui.TextInput(
        label="Pencere suresi (sn)",
        placeholder="Ornek: 60",
        required=True,
        default="60",
        max_length=4
    )
    ban_limit = discord.ui.TextInput(
        label="Ban limiti",
        placeholder="Ornek: 3",
        required=True,
        default="3",
        max_length=3
    )
    kanal_limit = discord.ui.TextInput(
        label="Kanal acma limiti",
        placeholder="Ornek: 3",
        required=True,
        default="3",
        max_length=3
    )
    diger_limitler = discord.ui.TextInput(
        label="Kanal silme / rol acma / rol silme / kick",
        placeholder="Ornek: 3,3,3,3",
        required=True,
        default="3,3,3,3",
        max_length=32
    )

    async def on_submit(self, interaction: discord.Interaction):
        try:
            log_kanal_id = int((self.log_kanal_id.value or "").strip())
            sure_saniye = int((self.sure_saniye.value or "").strip())
            ban_limit = int((self.ban_limit.value or "").strip())
            kanal_limit = int((self.kanal_limit.value or "").strip())
            digerler = [int(x.strip()) for x in (self.diger_limitler.value or "").split(",")]
            if len(digerler) != 4:
                raise ValueError
            kanal_sil_limit, rol_ac_limit, rol_sil_limit, kick_limit = digerler
        except ValueError:
            await interaction.response.send_message("Tum alanlara gecerli sayisal degerler girmen gerekiyor. Son alan `3,3,3,3` formatinda olmali.", ephemeral=True)
            return

        if sure_saniye < 10 or sure_saniye > 3600:
            await interaction.response.send_message("Pencere suresi 10 ile 3600 saniye arasinda olmali.", ephemeral=True)
            return
        if min(ban_limit, kanal_limit, kanal_sil_limit, rol_ac_limit, rol_sil_limit, kick_limit) < 1:
            await interaction.response.send_message("Tum limitler en az 1 olmali.", ephemeral=True)
            return

        log_kanal = interaction.guild.get_channel(log_kanal_id) if interaction.guild else None
        if not isinstance(log_kanal, discord.TextChannel):
            await interaction.response.send_message("Bu ID ile metin kanali bulunamadi.", ephemeral=True)
            return

        ayar = _guvenlik_ayar_al(interaction.guild.id)
        ayar.update({
            "aktif": True,
            "log_kanal_id": log_kanal.id,
            "sure_saniye": sure_saniye,
            "ban_limit": ban_limit,
            "kanal_limit": kanal_limit,
            "kanal_sil_limit": kanal_sil_limit,
            "rol_ac_limit": rol_ac_limit,
            "rol_sil_limit": rol_sil_limit,
            "kick_limit": kick_limit,
        })
        _guvenlik_ayar_kaydet(interaction.guild.id, ayar)

        embed = discord.Embed(
            title="Gvenlik Sistemi Kaydedildi",
            description="Sunucu koruma limitleri modal ile baaryla kaydedildi.",
            color=RENKLER["basari"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="Log", value=log_kanal.mention, inline=True)
        embed.add_field(name="Pencere", value=f"{sure_saniye} sn", inline=True)
        embed.add_field(name="Ban", value=str(ban_limit), inline=True)
        embed.add_field(name="Kanal Acma", value=str(kanal_limit), inline=True)
        embed.add_field(name="Kanal Silme", value=str(kanal_sil_limit), inline=True)
        embed.add_field(name="Rol Acma", value=str(rol_ac_limit), inline=True)
        embed.add_field(name="Rol Silme", value=str(rol_sil_limit), inline=True)
        embed.add_field(name="Kick", value=str(kick_limit), inline=True)
        embed.set_footer(text="Limit sayisina ulasildiginda direkt jail uygulanir")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        try:
            if interaction.response.is_done():
                await interaction.followup.send(f"Guvenlik modal hatasi: {error}", ephemeral=True)
            else:
                await interaction.response.send_message(f"Guvenlik modal hatasi: {error}", ephemeral=True)
        except Exception:
            pass


class _KurulumView(discord.ui.View):
    def __init__(self, modal_tipi: str):
        super().__init__(timeout=None)
        self.modal_tipi = modal_tipi

    @discord.ui.button(label="Modal Ac", style=discord.ButtonStyle.primary)
    async def modal_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            if self.modal_tipi == "level":
                await interaction.response.send_modal(LevelKurModal())
            elif self.modal_tipi == "karsilama":
                await interaction.response.send_modal(KarsilamaKurModal())
            elif self.modal_tipi == "guvenlik":
                await interaction.response.send_modal(GuvenlikKurModal())
            else:
                await interaction.response.send_modal(HosgeldinKurModal())
        except Exception as e:
            if not interaction.response.is_done():
                await interaction.response.send_message(f"Modal acilirken hata olustu: {e}", ephemeral=True)
            else:
                await interaction.followup.send(f"Modal acilirken hata olustu: {e}", ephemeral=True)


@bot.command(name="levelkur")
@commands.has_permissions(manage_guild=True)
async def level_kur_modal(ctx):
    e = discord.Embed(
        title="Level Sistemi Kurulumu",
        description="Asagidaki butona tikla, ayarlari modal uzerinden gir.",
        color=RENKLER["bilgi"]
    )
    await ctx.send(embed=e, view=_KurulumView("level"))


@bot.command(name="hosgeldinkur")
@commands.has_permissions(manage_guild=True)
async def hosgeldin_kur_modal(ctx):
    e = discord.Embed(
        title="Hosgeldin Sistemi Kurulumu",
        description="Asagidaki butona tikla, ayarlari modal uzerinden gir.",
        color=RENKLER["bilgi"]
    )
    await ctx.send(embed=e, view=_KurulumView("hosgeldin"))


@bot.command(name="karsilamakur", aliases=["karlama-kur", "karsilama-kur"])
@commands.has_permissions(manage_guild=True)
async def karsilama_kur_modal(ctx):
    e = discord.Embed(
        title="Karlama Mesaj Kurulumu",
        description="Aadaki butona tkla; etiket atmayan karlama mesajn modal zerinden kur.",
        color=RENKLER["bilgi"]
    )
    await ctx.send(embed=e, view=_KurulumView("karsilama"))


@bot.command(name="guvenlikkur", aliases=["gvenlikkur"])
@commands.has_permissions(administrator=True)
async def guvenlik_kur_modal(ctx):
    e = discord.Embed(
        title="Gvenlik Sistemi Kurulumu",
        description=(
            "Asagidaki butona tikla ve limitleri modal uzerinden ayarla.\n"
            "Yazdigin limit sayisina ulasilinca kullanici direkt jaile atilir."
        ),
        color=RENKLER["bilgi"]
    )
    await ctx.send(embed=e, view=_KurulumView("guvenlik"))


@bot.command(name="guvenlikdurum", aliases=["gvenlikdurum"])
@commands.has_permissions(administrator=True)
async def guvenlik_durum(ctx):
    ayar = _guvenlik_ayar_al(ctx.guild.id)
    log_kanal = ctx.guild.get_channel(ayar.get("log_kanal_id")) if ayar.get("log_kanal_id") else None
    whitelist = []
    for hedef_id in ayar.get("whitelist_ids", []) or []:
        uye = ctx.guild.get_member(int(hedef_id)) if str(hedef_id).isdigit() else None
        rol = ctx.guild.get_role(int(hedef_id)) if str(hedef_id).isdigit() else None
        if uye:
            whitelist.append(uye.mention)
        elif rol:
            whitelist.append(rol.mention)
    e = discord.Embed(
        title="Gvenlik Sistemi",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    e.add_field(name="Durum", value="Aktif" if ayar.get("aktif") else "Kapal", inline=True)
    e.add_field(name="Log", value=log_kanal.mention if log_kanal else "Yok", inline=True)
    e.add_field(name="Pencere", value=f"{ayar.get('sure_saniye', 60)} sn", inline=True)
    e.add_field(name="Ban Limiti", value=str(ayar.get("ban_limit", 3)), inline=True)
    e.add_field(name="Kanal Acma", value=str(ayar.get("kanal_limit", 3)), inline=True)
    e.add_field(name="Kanal Silme", value=str(ayar.get("kanal_sil_limit", 3)), inline=True)
    e.add_field(name="Rol Acma", value=str(ayar.get("rol_ac_limit", 3)), inline=True)
    e.add_field(name="Rol Silme", value=str(ayar.get("rol_sil_limit", 3)), inline=True)
    e.add_field(name="Kick", value=str(ayar.get("kick_limit", 3)), inline=True)
    e.add_field(name="Whitelist", value=", ".join(whitelist[:10]) if whitelist else "Yok", inline=False)
    await ctx.send(embed=e)


@bot.command(name="guvenlikkapat", aliases=["gvenlikkapat"])
@commands.has_permissions(administrator=True)
async def guvenlik_kapat(ctx):
    ayar = _guvenlik_ayar_al(ctx.guild.id)
    ayar["aktif"] = False
    _guvenlik_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(embed=discord.Embed(
        title="Gvenlik Sistemi Kapatld",
        description="Sunucu guvenlik limitleri devre disi birakildi.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    ))


@bot.command(name="guvenlikizin", aliases=["gvenlikizin", "guvenlik-whitelist"])
@commands.has_permissions(administrator=True)
async def guvenlik_izin_ekle(ctx, hedef = None):
    if hedef is None:
        await ctx.send("Kullanm: `.guvenlikizin @uye` veya `.guvenlikizin @rol`")
        return
    hedef_obj = None
    if ctx.message.role_mentions:
        hedef_obj = ctx.message.role_mentions[0]
    elif ctx.message.mentions:
        hedef_obj = ctx.message.mentions[0]
    if hedef_obj is None:
        await ctx.send("Ltfen bir ye veya rol etiketle.")
        return
    ayar = _guvenlik_ayar_al(ctx.guild.id)
    whitelist = list(dict.fromkeys((ayar.get("whitelist_ids", []) or []) + [hedef_obj.id]))
    ayar["whitelist_ids"] = whitelist
    _guvenlik_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(embed=discord.Embed(
        title="Whitelist Gncellendi",
        description=f"{hedef_obj.mention} gvenlik whitelist listesine eklendi.",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    ))


@bot.command(name="guvenlikizinsil", aliases=["gvenlikizinsil", "guvenlik-whitelist-sil"])
@commands.has_permissions(administrator=True)
async def guvenlik_izin_sil(ctx, hedef = None):
    if hedef is None:
        await ctx.send("Kullanm: `.guvenlikizinsil @uye` veya `.guvenlikizinsil @rol`")
        return
    hedef_obj = None
    if ctx.message.role_mentions:
        hedef_obj = ctx.message.role_mentions[0]
    elif ctx.message.mentions:
        hedef_obj = ctx.message.mentions[0]
    if hedef_obj is None:
        await ctx.send("Ltfen bir ye veya rol etiketle.")
        return
    ayar = _guvenlik_ayar_al(ctx.guild.id)
    ayar["whitelist_ids"] = [x for x in (ayar.get("whitelist_ids", []) or []) if x != hedef_obj.id]
    _guvenlik_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(embed=discord.Embed(
        title="Whitelist Gncellendi",
        description=f"{hedef_obj.mention} whitelist listesinden karld.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    ))


@bot.command(name="levelmesajtest")
@commands.has_permissions(manage_guild=True)
async def level_mesaj_test(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    ayar = _level_ayar_al(ctx.guild.id)
    aciklama = _sablon_doldur(ayar.get("mesaj", "Tebrikler {member_mention}, {level}. seviye oldun!"), hedef, level=5, xp=42)
    e = discord.Embed(
        title="Seviye Atladin! (Test)",
        description=aciklama,
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    e.add_field(name="Yeni Level", value="**5**", inline=True)
    e.add_field(name="Kalan XP", value="**42 / 475**", inline=True)
    if ayar.get("gif_url"):
        e.set_image(url=ayar["gif_url"])
    if hedef.display_avatar:
        e.set_thumbnail(url=hedef.display_avatar.url)
    e.set_footer(text=zaman_damgasi())
    await ctx.send(hedef.mention, embed=e)


@bot.command(name="hosgeldinmesajtest")
@commands.has_permissions(manage_guild=True)
async def hosgeldin_mesaj_test(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    ayar = _welcome_ayar_al(ctx.guild.id)
    kanal_id = ayar.get("kanal_id")
    kanal = ctx.guild.get_channel(kanal_id) if kanal_id else None

    if not kanal_id:
        await ctx.send("Hogeldin sistemi iin kanal ayarl deil. `.hosgeldinkur` ile nce kurulum yap.")
        return
    if not isinstance(kanal, discord.TextChannel):
        await ctx.send("Ayarl hogeldin kanal bulunamad. `.hosgeldinkur` ile sistemi tekrar kur.")
        return
    try:
        ust_metin, e = _hosgeldin_icerigi_hazirla(hedef, ayar)
        e.title = "Ho Geldin! (Test)"
        await kanal.send(ust_metin, embed=e)
    except discord.Forbidden:
        await ctx.send("Test mesaj gnderilemedi; botun hogeldin kanalnda yazma yetkisi yok.")
        return
    except Exception as e:
        await ctx.send(f"Hogeldin test mesaj oluturulurken hata oldu: {e}")
        return

    await ctx.send(f"Hogeldin test mesaj {kanal.mention} kanalna gnderildi.", delete_after=8)


@bot.command(name="karsilamatest", aliases=["karlama-test", "karsilama-test"])
@commands.has_permissions(manage_guild=True)
async def karsilama_test(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    ayar = _karsilama_ayar_al(ctx.guild.id)
    kanal_id = ayar.get("kanal_id")
    kanal = ctx.guild.get_channel(kanal_id) if kanal_id else None

    if not kanal_id:
        await ctx.send("Karlama sistemi iin kanal ayarl deil. `.karsilamakur` ile nce kurulum yap.")
        return
    if not isinstance(kanal, discord.TextChannel):
        await ctx.send("Ayarl karlama kanal bulunamad. `.karsilamakur` ile sistemi tekrar kur.")
        return

    try:
        mesaj = _karsilama_mesaji_hazirla(hedef, ayar)
        baslikli_mesaj = f"**Karlama Mesaj (Test)**\n{mesaj}"
        dosya = await hedef.display_avatar.to_file(filename="karsilama-avatar.png") if hedef.display_avatar else None
        if dosya:
            await kanal.send(baslikli_mesaj, file=dosya)
        else:
            await kanal.send(baslikli_mesaj)
    except discord.Forbidden:
        await ctx.send("Test mesaj gnderilemedi; botun karlama kanalnda yazma yetkisi yok.")
        return
    except Exception as e:
        await ctx.send(f"Karlama test mesaj oluturulurken hata oldu: {e}")
        return

    await ctx.send(f"Karlama test mesaj {kanal.mention} kanalna gnderildi.", delete_after=8)


#  Partner Koruma Sistemleri 

# Everyone/Here korumas iin veri deposu
_everyone_here_log = {}
# Spam korumas iin veri deposu (mesaj ierikli)
_spam_log = {}

@bot.event
async def on_message(message):
    # Bot mesajlarn ignore et
    if message.author.bot:
        return
    
    # Mevcut event handler'lar altr
    try:
        await bot.process_commands(message)
    except:
        pass
    
    # Genel gvenlik sistemleri
    ayarlar = ayarlari_yukle()
    gk = str(message.guild.id)
    sunucu_ayari = ayarlar.get(gk, {})

    # Partner kanal kontrol
    partner_ch_id = partner_kanal_id_al(message.guild.id)
    if partner_ch_id and message.channel.id == partner_ch_id:
        eslesen = DAVET_REGEX.search(message.content)

        if not eslesen:
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            uyari = await message.channel.send(embed=discord.Embed(
                title=" Geersiz Partner Metni",
                description=f"{message.author.mention} Mesajnzda Discord davet linki bulunamad. Mesajnz silindi.",
                color=RENKLER["hata"]
            ))
            await asyncio.sleep(5)
            try:
                await uyari.delete()
            except discord.NotFound:
                pass
            return

        # Davet kodu al
        davet_kodu = eslesen.group(1)
        partners = partner_verisi_al(message.guild.id)
        simdi = datetime.now(timezone.utc)

        # 1 saat bekleme kontrol
        if davet_kodu in partners:
            son_zaman_str = partners[davet_kodu].get("son_partner")
            if son_zaman_str:
                son_zaman = utc_datetime_from_iso(son_zaman_str)
                gecen = (simdi - son_zaman).total_seconds()
                if gecen < PARTNER_BEKLEME_SURESI:
                    kalan = int(PARTNER_BEKLEME_SURESI - gecen)
                    onceki_id = partners[davet_kodu].get("yapan_id")
                    try:
                        await message.delete()
                    except discord.Forbidden:
                        pass
                    uyari = await message.channel.send(embed=discord.Embed(
                        title=" Bekleme Sresi Dolmad",
                        description=(
                            f"{message.author.mention} Bu sunucuyla tekrar partner yapmak iin\n"
                            f"**{kalan // 60} dakika {kalan % 60} saniye** beklemeniz gerekiyor.\n"
                            f"Son partner: <@{onceki_id}> tarafndan yapld."
                        ),
                        color=RENKLER["mute"]
                    ))
                    await asyncio.sleep(7)
                    try:
                        await uyari.delete()
                    except discord.NotFound:
                        pass
                    return

        # Kaydet
        ilk_satir = message.content.strip().split("\n")[0][:50]
        sunucu_adi = ilk_satir if ilk_satir else "Bilinmiyor"
        kayit = {
            "guild_name": sunucu_adi,
            "guild_id": davet_kodu,
            "yapan": str(message.author),
            "yapan_id": message.author.id,
            "zaman": simdi.isoformat(),
            "son_partner": simdi.isoformat()
        }
        partner_kaydet_db(message.guild.id, davet_kodu, kayit)
        partner_gecmisi_ekle(message.guild.id, {
            "guild_name": sunucu_adi,
            "guild_id": davet_kodu,
            "yapan": str(message.author),
            "yapan_id": message.author.id,
            "zaman": simdi.isoformat(),
        })

        yetkili_partner_sayisi_guncelle(message.guild.id, message.author.id, str(message.author))

        stats = partner_istatistik_hesapla(message.guild.id)
        sira = partner_sira_bul(message.guild.id)
        yetkili_liste = yetkili_siralamasi_al(message.guild.id)
        yetkili_sira = next((i+1 for i, y in enumerate(yetkili_liste) if y["id"] == str(message.author.id)), "?")
        yetkili_toplam = next((y["sayi"] for y in yetkili_liste if y["id"] == str(message.author.id)), 1)

        stats_embed = discord.Embed(
            title=" Yeni Partner Yapld!",
            description=f"{message.author.mention} yeni bir partnerlik yapt!",
            color=0x57F287,
            timestamp=simdi
        )
        stats_embed.add_field(name=" Sunucu Sras", value=f"**#{sira}**", inline=True)
        stats_embed.add_field(name=" Yetkili Sras", value=f"**#{yetkili_sira}** ({yetkili_toplam} partnerlik)", inline=True)
        stats_embed.add_field(
            name=" Zamana Dayal:",
            value=(
                f" Gnlk: **{stats['gunluk']}**\n"
                f" Haftalk: **{stats['haftalik']}**\n"
                f" Aylk: **{stats['aylik']}**"
            ),
            inline=True
        )
        stats_embed.add_field(name=" Toplam", value=f"**{stats['toplam']}**", inline=True)
        stats_embed.set_footer(text=f"{bot.user.name}  Partner Sistemi")
        if message.guild.icon:
            stats_embed.set_thumbnail(url=message.guild.icon.url)
        await message.channel.send(embed=stats_embed)

        log_kanal_id = partner_log_kanali_al(message.guild.id)
        if log_kanal_id:
            log_kanal = message.guild.get_channel(log_kanal_id)
            if log_kanal:
                log_embed = discord.Embed(title=" Partner Logu", color=0x57F287, timestamp=simdi)
                log_embed.add_field(name=" Davet", value=f"`{davet_kodu}`", inline=True)
                log_embed.add_field(name=" Yapan", value=message.author.mention, inline=True)
                log_embed.add_field(name=" Zaman", value=simdi.strftime("%d.%m.%Y %H:%M UTC"), inline=True)
                log_embed.add_field(name=" Toplam", value=str(stats["toplam"]), inline=True)
                log_embed.add_field(name=" Yetkili Toplam", value=str(yetkili_toplam), inline=True)
                log_embed.set_footer(text=zaman_damgasi())
                await log_kanal.send(embed=log_embed)
        return

    # Kfr korumas
    if kufur_kontrol(message.guild.id, message.content):
        try:
            await message.delete()
            
            # Embed uyar gnder
            embed = discord.Embed(
                title=" Kfr Yasak",
                description=f"{message.author.mention} Kfr kullanm yasaktr!",
                color=0xFF6B6B,
                timestamp=datetime.now(timezone.utc)
            )
            await message.channel.send(embed=embed, delete_after=5)
            
            # Log gnder (varsa)
            log_kanal_id = sunucu_ayari.get("guvenlik_log")
            if log_kanal_id:
                log_kanal = message.guild.get_channel(log_kanal_id)
                if log_kanal:
                    embed = discord.Embed(
                        title=" Kfr Kullanm",
                        description=f"{message.author.mention} kullancs kfrl mesaj att.",
                        color=0xFF6B6B,
                        timestamp=datetime.now(timezone.utc)
                    )
                    embed.add_field(name="Kullanc", value=f"{message.author} ({message.author.id})", inline=True)
                    embed.add_field(name="Kanal", value=message.channel.mention, inline=True)
                    embed.add_field(name="Mesaj", value=f"```{message.content[:100]}...```" if len(message.content) > 100 else f"```{message.content}```", inline=False)
                    await log_kanal.send(embed=embed)

            yetkili_kufur = _yetkili_kufur_ayar_al(message.guild.id)
            if yetkili_kufur.get("aktif"):
                hedef_roller = [rol for rol in message.author.roles if rol.id in set(yetkili_kufur.get("rol_ids", []))]
                if hedef_roller:
                    ayarlar = ayarlari_yukle()
                    gk = str(message.guild.id)
                    durumlar = ayarlar.setdefault(gk, {}).setdefault("yetkili_kufur", {}).setdefault("durumlar", {})
                    uye_durum = durumlar.setdefault(str(message.author.id), {"sayi": 0})
                    uye_durum["sayi"] = int(uye_durum.get("sayi", 0)) + 1
                    ayarlari_kaydet(ayarlar)
                    if uye_durum["sayi"] >= int(yetkili_kufur.get("limit", 3)):
                        try:
                            await message.author.remove_roles(*hedef_roller, reason="Yetkili kufur korumasi limiti asildi")
                        except discord.Forbidden:
                            pass
        except discord.Forbidden:
            pass

    gif_ayar = _gifcevap_ayar_al(message.guild.id)
    if gif_ayar.get("aktif"):
        whitelist = set(int(x) for x in (gif_ayar.get("whitelist_ids", []) or []) if str(x).isdigit())
        yetkili_mi = message.author.id in whitelist or any(rol.id in whitelist for rol in getattr(message.author, "roles", []))
        if yetkili_mi:
            icerik = message.content.lower()
            for kayit in gif_ayar.get("kayitlar", []):
                anahtar = str(kayit.get("anahtar", "")).lower().strip()
                if anahtar and anahtar in icerik and kayit.get("gif_url"):
                    await message.channel.send(kayit.get("gif_url"))
                    break

    # Genel spam korumas
    spam_ayar = sunucu_ayari.get("guvenlik_spam_koruma", {})
    if spam_ayar.get("aktif", False):
        muaf_roller = set(spam_ayar.get("muaf_roller", []) or [])
        muaf_kanallar = set(spam_ayar.get("muaf_kanallar", []) or [])
        kullanici_muaf = any(role.id in muaf_roller for role in message.author.roles)
        kanal_muaf = message.channel.id in muaf_kanallar
        if kullanici_muaf or kanal_muaf:
            pass
        else:
            user_id = message.author.id
            now = time.time()
            mesaj_icerik = message.content.strip().lower()
        
            # Kullancnn mesaj gemiini kontrol et
            if user_id not in _spam_log:
                _spam_log[user_id] = []
        
            _spam_log[user_id].append((now, mesaj_icerik))
        
            # Eski mesajlar temizle (1 saatten eski olanlar)
            _spam_log[user_id] = [(t, m) for t, m in _spam_log[user_id] if now - t < 3600]
        
            # Ayn mesaj spam kontrol
            max_ayni_mesaj = spam_ayar.get("max_ayni_mesaj", 3)
            zaman_araligi = spam_ayar.get("zaman_araligi", 10)
        
            # Son zaman aralndaki ayn mesajlar say
            son_mesajlar = [(t, m) for t, m in _spam_log[user_id] if now - t < zaman_araligi]
            ayni_mesaj_sayisi = sum(1 for t, m in son_mesajlar if m == mesaj_icerik)
        
            if ayni_mesaj_sayisi > max_ayni_mesaj:
                try:
                    # Timeout uygula
                    mute_suresi = spam_ayar.get("mute_suresi", 300)  # 5 dakika
                
                    await message.author.timeout(timedelta(seconds=mute_suresi), reason="Ayn mesaj spam korumas - Genel gvenlik")
                
                    # Embed bildirim gnder
                    embed = discord.Embed(
                        title=" Spam Cezas",
                        description=f"{message.author.mention} ayn mesaj tekrarlad iin susturuldu!",
                        color=0xFF9500,
                        timestamp=datetime.now(timezone.utc)
                    )
                    embed.add_field(name="Kullanc", value=f"{message.author} ({message.author.id})", inline=True)
                    embed.add_field(name="Sre", value=f"{mute_suresi//60} dakika", inline=True)
                    embed.add_field(name="Sebep", value=f"{zaman_araligi} saniyede ayn mesaj {ayni_mesaj_sayisi} kez", inline=False)
                    await message.channel.send(embed=embed, delete_after=10)
                
                    # Log gnder
                    log_kanal_id = sunucu_ayari.get("guvenlik_log")
                    if log_kanal_id:
                        log_kanal = message.guild.get_channel(log_kanal_id)
                        if log_kanal:
                            embed = discord.Embed(
                                title=" Spam Cezas",
                                description=f"{message.author.mention} ayn mesaj tekrarlad iin susturuldu.",
                                color=0xFF9500,
                                timestamp=datetime.now(timezone.utc)
                            )
                            embed.add_field(name="Kullanc", value=f"{message.author} ({message.author.id})", inline=True)
                            embed.add_field(name="Sre", value=f"{mute_suresi//60} dakika", inline=True)
                            embed.add_field(name="Sebep", value=f"{zaman_araligi} saniyede ayn mesaj {ayni_mesaj_sayisi} kez", inline=False)
                            embed.add_field(name="Mesaj", value=f"```{message.content[:100]}...```" if len(message.content) > 100 else f"```{message.content}```", inline=False)
                            await log_kanal.send(embed=embed)
                except discord.Forbidden:
                    pass
    
    # Genel link korumas
    link_ayar = sunucu_ayari.get("guvenlik_link_koruma", {})
    if link_ayar.get("aktif", False):
        # Muaf kontrol
        muaf_roller = link_ayar.get("muaf_roller", [])
        muaf_kanallar = link_ayar.get("muaf_kanallar", [])
        
        # Kullanc muaf m?
        kullanici_muaf = any(role.id in muaf_roller for role in message.author.roles)
        
        # Kanal muaf m?
        kanal_muaf = message.channel.id in muaf_kanallar
        
        if not kullanici_muaf and not kanal_muaf:
            # Link kontrol (basit regex)
            import re
            link_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
            if re.search(link_pattern, message.content):
                try:
                    await message.delete()
                    
                    # Embed hata mesaj
                    embed = discord.Embed(
                        title=" Link Paylam Yasak",
                        description=f"{message.author.mention} Link paylam yasaktr!",
                        color=0xFF6B6B,
                        timestamp=datetime.now(timezone.utc)
                    )
                    await message.channel.send(embed=embed, delete_after=5)
                    
                    # Log gnder
                    log_kanal_id = sunucu_ayari.get("guvenlik_log")
                    if log_kanal_id:
                        log_kanal = message.guild.get_channel(log_kanal_id)
                        if log_kanal:
                            embed = discord.Embed(
                                title=" Link Paylam",
                                description=f"{message.author.mention} kullancs link paylat.",
                                color=0xFF6B6B,
                                timestamp=datetime.now(timezone.utc)
                            )
                            embed.add_field(name="Kullanc", value=f"{message.author} ({message.author.id})", inline=True)
                            embed.add_field(name="Kanal", value=message.channel.mention, inline=True)
                            embed.add_field(name="Mesaj", value=f"```{message.content[:100]}...```" if len(message.content) > 100 else f"```{message.content}```", inline=False)
                            await log_kanal.send(embed=embed)
                except discord.Forbidden:
                    pass
    
    #  Genel Gvenlik Komutlar 

#  Modal Snflar 
class SpamModal(discord.ui.Modal, title="Spam Koruma Ayarlari"):
    max_ayni_mesaj = discord.ui.TextInput(
        label="Maksimum Ayn Mesaj",
        placeholder="rn: 3 (10 saniyede ayn mesajdan en fazla 3 kez)",
        style=discord.TextStyle.short,
        required=True,
        default="3"
    )
    zaman_araligi = discord.ui.TextInput(
        label="Zaman Aral (saniye)",
        placeholder="rn: 10",
        style=discord.TextStyle.short,
        required=True,
        default="10"
    )
    mute_suresi = discord.ui.TextInput(
        label="Mute Sresi (saniye)",
        placeholder="rn: 300 (5 dakika)",
        style=discord.TextStyle.short,
        required=True,
        default="300"
    )
    
    async def on_submit(self, interaction: discord.Interaction):
        try:
            max_msg = int(self.max_ayni_mesaj.value)
            zaman = int(self.zaman_araligi.value)
            sure = int(self.mute_suresi.value)
            
            ayarlar = ayarlari_yukle()
            gk = str(interaction.guild.id)
            sunucu_ayari = ayarlar.setdefault(gk, {})
            
            sunucu_ayari["guvenlik_spam_koruma"] = {
                "aktif": True,
                "max_ayni_mesaj": max_msg,
                "zaman_araligi": zaman,
                "mute_suresi": sure,
                "muaf_roller": sunucu_ayari.get("guvenlik_spam_koruma", {}).get("muaf_roller", []),
                "muaf_kanallar": sunucu_ayari.get("guvenlik_spam_koruma", {}).get("muaf_kanallar", []),
            }
            
            ayarlari_kaydet(ayarlar)
            
            embed = discord.Embed(
                title=" Spam Koruma Ayarland",
                description="Spam yapan kullanclara otomatik timeout uygulanacak.",
                color=RENKLER["basari"],
                timestamp=datetime.now(timezone.utc)
            )
            embed.add_field(name="Max Ayn Mesaj", value=f"**{max_msg}** mesaj", inline=True)
            embed.add_field(name="Zaman Aral", value=f"**{zaman}** saniye", inline=True)
            embed.add_field(name="Mute Sresi", value=f"**{sure//60}** dakika", inline=True)
            
            await interaction.response.send_message(embed=embed, ephemeral=True)
            
        except ValueError:
            await interaction.response.send_message("Ltfen tm alanlara geerli saylar girin!", ephemeral=True)

class SpamModalView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label=" Modal A", style=discord.ButtonStyle.primary)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = SpamModal()
        await interaction.response.send_modal(modal)

class LinkModal(discord.ui.Modal, title="Link Koruma Ayarlari"):
    aktif_mi = discord.ui.TextInput(
        label="Link Koruma Aktif? (evet/hayr)",
        placeholder="rn: evet",
        style=discord.TextStyle.short,
        required=True,
        default="evet"
    )
    
    async def on_submit(self, interaction: discord.Interaction):
        ayarlar = ayarlari_yukle()
        gk = str(interaction.guild.id)
        sunucu_ayari = ayarlar.setdefault(gk, {})
        
        if "guvenlik_link_koruma" not in sunucu_ayari:
            sunucu_ayari["guvenlik_link_koruma"] = {}
        
        aktif = self.aktif_mi.value.lower() in ["evet", "aktif", "true", "1", "a"]
        sunucu_ayari["guvenlik_link_koruma"]["aktif"] = aktif
        
        if "muaf_roller" not in sunucu_ayari["guvenlik_link_koruma"]:
            sunucu_ayari["guvenlik_link_koruma"]["muaf_roller"] = []
        if "muaf_kanallar" not in sunucu_ayari["guvenlik_link_koruma"]:
            sunucu_ayari["guvenlik_link_koruma"]["muaf_kanallar"] = []
        
        ayarlari_kaydet(ayarlar)
        
        embed = discord.Embed(
            title=" Link Koruma Ayarland",
            description=f"Link korumas {'aktif' if aktif else 'pasif'} durumuna ayarland.\n\nMuaf roller eklemek iin: `.link-koruma-muaf-rol @rol`\nMuaf kanallar eklemek iin: `.link-koruma-muaf-kanal #kanal`",
            color=RENKLER["basari"] if aktif else RENKLER["hata"],
            timestamp=datetime.now(timezone.utc)
        )
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

class LinkModalView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label=" Modal A", style=discord.ButtonStyle.primary)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = LinkModal()
        await interaction.response.send_modal(modal)


#  Genel Gvenlik Komutlar 

@bot.command(name="spam-koruma-kur")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_kur(ctx):
    """Genel spam korumasn modal ile kurar."""
    await ctx.send("Modal amak iin butona tklayn:", view=SpamModalView())


@bot.command(name="spam-koruma-muaf-rol")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_muaf_rol(ctx, rol: discord.Role = None):
    if not rol:
        await ctx.send("Kullanim: `.spam-koruma-muaf-rol @rol`")
        return
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.setdefault(gk, {})
    spam_ayar = sunucu_ayari.setdefault("guvenlik_spam_koruma", {"aktif": False, "muaf_roller": [], "muaf_kanallar": []})
    muaf_roller = set(spam_ayar.get("muaf_roller", []))
    if rol.id in muaf_roller:
        muaf_roller.remove(rol.id)
        mesaj = f"{rol.mention} spam koruma muafiyetinden cikarildi."
    else:
        muaf_roller.add(rol.id)
        mesaj = f"{rol.mention} spam koruma muaf rol listesine eklendi."
    spam_ayar["muaf_roller"] = list(muaf_roller)
    ayarlari_kaydet(ayarlar)
    await ctx.send(embed=discord.Embed(description=mesaj, color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="spam-koruma-muaf-kanal")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_muaf_kanal(ctx, kanal: discord.TextChannel = None):
    if not kanal:
        await ctx.send("Kullanim: `.spam-koruma-muaf-kanal #kanal`")
        return
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.setdefault(gk, {})
    spam_ayar = sunucu_ayari.setdefault("guvenlik_spam_koruma", {"aktif": False, "muaf_roller": [], "muaf_kanallar": []})
    muaf_kanallar = set(spam_ayar.get("muaf_kanallar", []))
    if kanal.id in muaf_kanallar:
        muaf_kanallar.remove(kanal.id)
        mesaj = f"{kanal.mention} spam koruma muafiyetinden cikarildi."
    else:
        muaf_kanallar.add(kanal.id)
        mesaj = f"{kanal.mention} spam koruma muaf kanal listesine eklendi."
    spam_ayar["muaf_kanallar"] = list(muaf_kanallar)
    ayarlari_kaydet(ayarlar)
    await ctx.send(embed=discord.Embed(description=mesaj, color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))

@bot.command(name="link-koruma-kur")
@commands.has_permissions(manage_guild=True)
async def link_koruma_kur(ctx):
    """Genel link korumasn modal ile kurar."""
    await ctx.send("Modal amak iin butona tklayn:", view=LinkModalView())

@bot.command(name="link-koruma-aktif")
@commands.has_permissions(manage_guild=True)
async def link_koruma_aktif(ctx):
    """Genel link korumasn aktif eder."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.setdefault(gk, {})
    
    if "guvenlik_link_koruma" not in sunucu_ayari:
        sunucu_ayari["guvenlik_link_koruma"] = {}
    
    sunucu_ayari["guvenlik_link_koruma"]["aktif"] = True
    ayarlari_kaydet(ayarlar)
    
    embed = discord.Embed(
        title=" Genel Link Koruma Aktif",
        description="Tm kanallarda link paylam engellendi (muaf olanlar hari).",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    await ctx.send(embed=embed)

@bot.command(name="link-koruma-kapat")
@commands.has_permissions(manage_guild=True)
async def link_koruma_kapat(ctx):
    """Genel link korumasn kapatr."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.setdefault(gk, {})
    
    if "guvenlik_link_koruma" in sunucu_ayari:
        sunucu_ayari["guvenlik_link_koruma"]["aktif"] = False
        ayarlari_kaydet(ayarlar)
    
    embed = discord.Embed(
        title=" Genel Link Koruma Kapatld",
        description="Link paylam serbest brakld.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    await ctx.send(embed=embed)

@bot.command(name="link-koruma-muaf-rol")
@commands.has_permissions(manage_guild=True)
async def link_koruma_muaf_rol(ctx, rol: discord.Role):
    """Link korumasndan muaf rol ekler."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.setdefault(gk, {})
    
    if "guvenlik_link_koruma" not in sunucu_ayari:
        sunucu_ayari["guvenlik_link_koruma"] = {}
    if "muaf_roller" not in sunucu_ayari["guvenlik_link_koruma"]:
        sunucu_ayari["guvenlik_link_koruma"]["muaf_roller"] = []
    
    if rol.id not in sunucu_ayari["guvenlik_link_koruma"]["muaf_roller"]:
        sunucu_ayari["guvenlik_link_koruma"]["muaf_roller"].append(rol.id)
        ayarlari_kaydet(ayarlar)
        
        embed = discord.Embed(
            title=" Muaf Rol Eklendi",
            description=f"{rol.mention} rol link korumasndan muaf tutuldu.",
            color=RENKLER["basari"],
            timestamp=datetime.now(timezone.utc)
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu rol zaten muaf listesinde!")

@bot.command(name="link-koruma-muaf-kanal")
@commands.has_permissions(manage_guild=True)
async def link_koruma_muaf_kanal(ctx, kanal: discord.TextChannel):
    """Link korumasndan muaf kanal ekler."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.setdefault(gk, {})
    
    if "guvenlik_link_koruma" not in sunucu_ayari:
        sunucu_ayari["guvenlik_link_koruma"] = {}
    if "muaf_kanallar" not in sunucu_ayari["guvenlik_link_koruma"]:
        sunucu_ayari["guvenlik_link_koruma"]["muaf_kanallar"] = []
    
    if kanal.id not in sunucu_ayari["guvenlik_link_koruma"]["muaf_kanallar"]:
        sunucu_ayari["guvenlik_link_koruma"]["muaf_kanallar"].append(kanal.id)
        ayarlari_kaydet(ayarlar)
        
        embed = discord.Embed(
            title=" Muaf Kanal Eklendi",
            description=f"{kanal.mention} kanal link korumasndan muaf tutuldu.",
            color=RENKLER["basari"],
            timestamp=datetime.now(timezone.utc)
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu kanal zaten muaf listesinde!")

@bot.command(name="link-koruma-durum")
@commands.has_permissions(manage_guild=True)
async def link_koruma_durum(ctx):
    """Genel link koruma durumunu gsterir."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.get(gk, {})
    link_ayar = sunucu_ayari.get("guvenlik_link_koruma", {})
    
    embed = discord.Embed(
        title=" Genel Link Koruma Durumu",
        color=0x5865F2,
        timestamp=datetime.now(timezone.utc)
    )
    
    durum = " Aktif" if link_ayar.get("aktif", False) else " Pasif"
    embed.add_field(name="Durum", value=durum, inline=True)
    
    muaf_roller = link_ayar.get("muaf_roller", [])
    muaf_kanallar = link_ayar.get("muaf_kanallar", [])
    
    if muaf_roller:
        roller_text = "\n".join([f"<@&{rid}>" for rid in muaf_roller[:5]])
        if len(muaf_roller) > 5:
            roller_text += f"\n...ve {len(muaf_roller)-5} rol daha"
        embed.add_field(name=" Muaf Roller", value=roller_text or "Yok", inline=False)
    
    if muaf_kanallar:
        kanallar_text = "\n".join([f"<#{kid}>" for kid in muaf_kanallar[:5]])
        if len(muaf_kanallar) > 5:
            kanallar_text += f"\n...ve {len(muaf_kanallar)-5} kanal daha"
        embed.add_field(name=" Muaf Kanallar", value=kanallar_text or "Yok", inline=False)
    
    await ctx.send(embed=embed)


bot.remove_command("kufur-temizle")


@bot.command(name="kufur-temizle")
@commands.has_permissions(administrator=True)
async def kufur_temizle_v2(ctx):
    guild_key = str(ctx.guild.id)
    ayarlar = ayarlari_yukle()
    if guild_key not in ayarlar or not ayarlar[guild_key].get("yasakli_kelimeler"):
        await ctx.send("Bu sunucuda zaten kfr korumas ayarlanmam.")
        return
    ayarlar[guild_key]["yasakli_kelimeler"] = []
    ayarlari_kaydet(ayarlar)
    await ctx.send(embed=discord.Embed(
        title="Kufur Korumas Temizlendi",
        description="Tum yasak kelimeler silindi ve kufur korumasi kapatildi.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    ))


class GifCevapModal(discord.ui.Modal, title="GIF Cevap Kurulumu"):
    anahtar = discord.ui.TextInput(label="Anahtar Kelime", placeholder="ornek: gnaydn", required=True, max_length=100)
    gif_url = discord.ui.TextInput(label="GIF URL", placeholder="https://...", required=True, max_length=500)
    whitelist = discord.ui.TextInput(label="Whitelist IDleri", placeholder="uye/rol idlerini virgul ile yaz", required=True, max_length=500)

    async def on_submit(self, interaction: discord.Interaction):
        whitelist_ids = [int(x.strip()) for x in str(self.whitelist).split(",") if x.strip().isdigit()]
        if not whitelist_ids:
            await interaction.response.send_message("Gecerli whitelist ID'leri girmelisin.", ephemeral=True)
            return
        ayar = _gifcevap_ayar_al(interaction.guild.id)
        kayitlar = [k for k in ayar.get("kayitlar", []) if k.get("anahtar") != str(self.anahtar).strip().lower()]
        kayitlar.append({
            "anahtar": str(self.anahtar).strip().lower(),
            "gif_url": str(self.gif_url).strip(),
        })
        ayar["aktif"] = True
        ayar["whitelist_ids"] = list(dict.fromkeys((ayar.get("whitelist_ids", []) or []) + whitelist_ids))
        ayar["kayitlar"] = kayitlar
        _gifcevap_ayar_kaydet(interaction.guild.id, ayar)
        await interaction.response.send_message("GIF cevap kaydedildi.", ephemeral=True)


@bot.command(name="gifcevap")
@commands.has_permissions(manage_guild=True)
async def gif_cevap_kur(ctx):
    class _View(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=300)

        @discord.ui.button(label="GIF Cevap Kur", style=discord.ButtonStyle.primary)
        async def ac(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_modal(GifCevapModal())

    await ctx.send(embed=discord.Embed(title="GIF Cevap Sistemi", description="Butona basip anahtar kelime + gif + whitelist ayarlayabilirsin.", color=RENKLER["bilgi"]), view=_View())


@bot.command(name="gifcevapdurum")
@commands.has_permissions(manage_guild=True)
async def gif_cevap_durum(ctx):
    ayar = _gifcevap_ayar_al(ctx.guild.id)
    embed = discord.Embed(title="GIF Cevap Durumu", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Durum", value="Aktif" if ayar.get("aktif") else "Kapali", inline=True)
    embed.add_field(name="Kayit", value=str(len(ayar.get("kayitlar", []))), inline=True)
    whitelist = ", ".join(f"`{x}`" for x in ayar.get("whitelist_ids", [])[:10]) or "Yok"
    embed.add_field(name="Whitelist", value=whitelist, inline=False)
    kayitlar = "\n".join(f"`{k.get('anahtar')}` -> {k.get('gif_url')}" for k in ayar.get("kayitlar", [])[:10]) or "Yok"
    embed.add_field(name="Anahtarlar", value=kayitlar[:1024], inline=False)
    await ctx.send(embed=embed)


@bot.command(name="gifcevapkapat")
@commands.has_permissions(manage_guild=True)
async def gif_cevap_kapat(ctx):
    _gifcevap_ayar_kaydet(ctx.guild.id, {"aktif": False, "whitelist_ids": [], "kayitlar": []})
    await ctx.send(embed=discord.Embed(title="GIF Cevap Kapatildi", description="Tum gif cevap kayitlari ve whitelist temizlendi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="levelkapat")
@commands.has_permissions(manage_guild=True)
async def level_kapat(ctx):
    _level_ayar_kaydet(ctx.guild.id, {"kanal_id": None, "mesaj": "Tebrikler {member_mention}, **{level}. seviye** oldun!", "gif_url": None, "rol_odulleri": {}})
    await ctx.send(embed=discord.Embed(title="Level Sistemi Kapatildi", description="Level sistemi bu sunucuda devre disi birakildi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="hosgeldinkapat")
@commands.has_permissions(manage_guild=True)
async def hosgeldin_kapat(ctx):
    _welcome_ayar_kaydet(ctx.guild.id, {"kanal_id": None, "mesaj": "Aramiza hos geldin {member_mention}! Sunucuda iyi eglenceler.", "gif_url": None, "rol_ids": []})
    await ctx.send(embed=discord.Embed(title="Hosgeldin Sistemi Kapatildi", description="Hosgeldin mesaji sistemi devre disi birakildi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="karsilamakapat")
@commands.has_permissions(manage_guild=True)
async def karsilama_kapat(ctx):
    _karsilama_ayar_kaydet(ctx.guild.id, {"kanal_id": None, "mesaj": "Aramiza hos geldin {username}. Seninle birlikte {member_count} kisiyiz."})
    await ctx.send(embed=discord.Embed(title="Karsilama Sistemi Kapatildi", description="Etiket atmayan karsilama sistemi kapatildi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


class YetkiliKufurModal(discord.ui.Modal, title="Yetkili Kufur Koruma"):
    rol_ids = discord.ui.TextInput(label="Yetkili Rol IDleri", placeholder="rol idlerini virgul ile yaz", required=True, max_length=500)
    limit = discord.ui.TextInput(label="Limit", placeholder="ornek: 3", required=True, max_length=5, default="3")

    async def on_submit(self, interaction: discord.Interaction):
        rol_ids = [int(x.strip()) for x in str(self.rol_ids).split(",") if x.strip().isdigit()]
        limit = int((str(self.limit).strip() or "3"))
        if not rol_ids:
            await interaction.response.send_message("En az bir yetkili rol ID'si gerekli.", ephemeral=True)
            return
        _yetkili_kufur_ayar_kaydet(interaction.guild.id, {"aktif": True, "rol_ids": rol_ids, "limit": max(1, limit), "durumlar": {}})
        await interaction.response.send_message("Yetkili kufur korumasi kaydedildi.", ephemeral=True)


@bot.command(name="yetkilikufurkur")
@commands.has_permissions(administrator=True)
async def yetkili_kufur_kur(ctx):
    class _View(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=300)

        @discord.ui.button(label="Yetkili Kufur Modalini Ac", style=discord.ButtonStyle.primary)
        async def ac(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_modal(YetkiliKufurModal())

    await ctx.send(embed=discord.Embed(title="Yetkili Kufur Koruma", description="Butona basip yetkili rolleri ve limiti ayarla.", color=RENKLER["bilgi"]), view=_View())


@bot.command(name="yetkilikufurkapat")
@commands.has_permissions(administrator=True)
async def yetkili_kufur_kapat(ctx):
    _yetkili_kufur_ayar_kaydet(ctx.guild.id, {"aktif": False, "rol_ids": [], "limit": 3, "durumlar": {}})
    await ctx.send(embed=discord.Embed(title="Yetkili Kufur Koruma Kapatildi", description="Yetkili kufur takip sistemi sifirlandi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="yetkilikufurdurum")
@commands.has_permissions(administrator=True)
async def yetkili_kufur_durum(ctx):
    ayar = _yetkili_kufur_ayar_al(ctx.guild.id)
    roller = ", ".join(f"<@&{rid}>" for rid in ayar.get("rol_ids", [])[:10]) or "Yok"
    await ctx.send(embed=discord.Embed(
        title="Yetkili Kufur Durumu",
        description=f"Durum: {'Aktif' if ayar.get('aktif') else 'Kapali'}\nLimit: {ayar.get('limit', 3)}",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    ).add_field(name="Yetkili Roller", value=roller, inline=False))


class JailKurModal(discord.ui.Modal, title="Jail Sistemi Kurulumu"):
    kanal = discord.ui.TextInput(label="Jail Kanal ID", placeholder="kanal id", required=True, max_length=30)
    yetki_rol = discord.ui.TextInput(label="Jail Yetki Rol ID", placeholder="jail yapabilecek rol id", required=True, max_length=30)

    async def on_submit(self, interaction: discord.Interaction):
        kanal_id = int((str(self.kanal).strip() or "0"))
        yetki_rol_id = int((str(self.yetki_rol).strip() or "0"))
        kanal = interaction.guild.get_channel(kanal_id)
        yetki_rol = interaction.guild.get_role(yetki_rol_id)
        if not isinstance(kanal, discord.TextChannel) or yetki_rol is None:
            await interaction.response.send_message("Gecerli kanal ve jail yetki rolu girmelisin.", ephemeral=True)
            return
        jail_rol = discord.utils.get(interaction.guild.roles, name="JAIL")
        if jail_rol is None:
            jail_rol = await interaction.guild.create_role(name="JAIL", colour=discord.Color.from_rgb(120, 72, 32), reason="Jail sistemi icin otomatik olusturuldu")
        await interaction.response.defer(ephemeral=True, thinking=True)
        await _jail_altyapi_hazirla(interaction.guild, jail_rol, kanal)
        ayar = _jail_ayar_al(interaction.guild.id)
        ayar.update({"aktif": True, "kanal_id": kanal.id, "jail_rol_id": jail_rol.id, "jail_yetki_rol_id": yetki_rol.id, "kayitlar": ayar.get("kayitlar", {})})
        _jail_ayar_kaydet(interaction.guild.id, ayar)
        await interaction.followup.send(f"Jail sistemi kaydedildi. Kanal: {kanal.mention}  Jail Rol: {jail_rol.mention}", ephemeral=True)


def _jail_yetkili_mi(uye: discord.Member, guild_id: int) -> bool:
    ayar = _jail_ayar_al(guild_id)
    yetki_rol_id = ayar.get("jail_yetki_rol_id")
    return bool(yetki_rol_id and any(rol.id == yetki_rol_id for rol in uye.roles))


async def _jail_altyapi_hazirla(guild: discord.Guild, jail_rol: discord.Role, jail_kanal: discord.TextChannel):
    for kanal in guild.channels:
        try:
            if kanal.id == jail_kanal.id:
                await kanal.set_permissions(
                    jail_rol,
                    view_channel=True,
                    send_messages=True,
                    read_message_history=True,
                    attach_files=True,
                    reason="Jail sistemi kurulumu"
                )
            else:
                kwargs = {
                    "view_channel": False,
                    "send_messages": False,
                    "add_reactions": False,
                    "attach_files": False,
                    "read_message_history": False,
                    "reason": "Jail sistemi kurulumu",
                }
                if isinstance(kanal, discord.VoiceChannel):
                    kwargs["connect"] = False
                    kwargs["speak"] = False
                await kanal.set_permissions(jail_rol, **kwargs)
        except Exception:
            pass


async def _jail_uygula_dahili(guild: discord.Guild, uye: discord.Member, sebep: str, uygulayan: str = "Sistem"):
    ayar = _jail_ayar_al(guild.id)
    jail_rol = guild.get_role(ayar.get("jail_rol_id")) if ayar.get("jail_rol_id") else None
    jail_kanal = guild.get_channel(ayar.get("kanal_id")) if ayar.get("kanal_id") else None

    if not ayar.get("aktif") or jail_rol is None or not isinstance(jail_kanal, discord.TextChannel):
        return False, "Jail sistemi kurulu degil."

    eski_roller = [rol.id for rol in uye.roles if rol != guild.default_role and rol != jail_rol]
    kayitlar = ayar.get("kayitlar", {})
    kayitlar[str(uye.id)] = {
        "rol_ids": eski_roller,
        "sebep": sebep,
        "zaman": datetime.now(timezone.utc).isoformat()
    }
    ayar["kayitlar"] = kayitlar
    _jail_ayar_kaydet(guild.id, ayar)

    try:
        await uye.edit(roles=[jail_rol], reason=f"{uygulayan} tarafindan jail: {sebep}")
    except (discord.Forbidden, discord.HTTPException):
        return False, "Rol hiyerarsisi veya yetki nedeniyle jail uygulanamadi."

    return True, "Kullanici jaile atildi."


@bot.command(name="jailkur")
@commands.has_permissions(manage_guild=True)
async def jail_kur(ctx):
    class _View(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=300)

        @discord.ui.button(label="Jail Sistemini Kur", style=discord.ButtonStyle.primary)
        async def ac(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_modal(JailKurModal())

    await ctx.send(embed=discord.Embed(title="Jail Sistemi", description="Butona basip jail kanalini ve jail yetki rolunu sec.", color=RENKLER["bilgi"]), view=_View())


@bot.command(name="jailkapat")
@commands.has_permissions(administrator=True)
async def jail_kapat(ctx):
    _jail_ayar_kaydet(ctx.guild.id, {"aktif": False, "kanal_id": None, "jail_rol_id": None, "jail_yetki_rol_id": None, "kayitlar": {}})
    await ctx.send(embed=discord.Embed(title="Jail Sistemi Kapatildi", description="Jail ayarlari kapatildi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="jail")
async def jail_uygula(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    if not uye:
        await ctx.send(embed=kullanim_embedi("`.jail @uye [sebep]`"))
        return
    if not _jail_yetkili_mi(ctx.author, ctx.guild.id):
        await ctx.send(embed=hata_embedi("Yetki Hatasi", "Bu komut icin jail yetki rolune sahip olmalisin."))
        return
    ayar = _jail_ayar_al(ctx.guild.id)
    jail_rol = ctx.guild.get_role(ayar.get("jail_rol_id")) if ayar.get("jail_rol_id") else None
    jail_kanal = ctx.guild.get_channel(ayar.get("kanal_id")) if ayar.get("kanal_id") else None
    if not ayar.get("aktif") or jail_rol is None or not isinstance(jail_kanal, discord.TextChannel):
        await ctx.send(embed=hata_embedi("Jail Sistemi Hazir Degil", "Once `.jailkur` ile sistemi kurmalisin."))
        return
    basarili, sonuc_mesaji = await _jail_uygula_dahili(ctx.guild, uye, sebep, uygulayan=str(ctx.author))
    if not basarili:
        await ctx.send(embed=hata_embedi("Jail Basarisiz", sonuc_mesaji))
        return
    await ctx.send(embed=discord.Embed(title="Uye Jailleendi", description=f"{uye.mention} jailleendi.\nSebep: {sebep}", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="unjail")
async def unjail_uygula(ctx, uye: discord.Member = None):
    if not uye:
        await ctx.send(embed=kullanim_embedi("`.unjail @uye`"))
        return
    if not _jail_yetkili_mi(ctx.author, ctx.guild.id):
        await ctx.send(embed=hata_embedi("Yetki Hatasi", "Bu komut icin jail yetki rolune sahip olmalisin."))
        return
    ayar = _jail_ayar_al(ctx.guild.id)
    kayit = ayar.get("kayitlar", {}).get(str(uye.id))
    if not kayit:
        await ctx.send(embed=hata_embedi("Kayit Bulunamadi", "Bu uye icin kayitli jail verisi yok."))
        return
    roller = [ctx.guild.get_role(rid) for rid in kayit.get("rol_ids", [])]
    roller = [rol for rol in roller if rol]
    await uye.edit(roles=roller, reason=f"{ctx.author} tarafindan jail kaldirildi")
    ayar["kayitlar"].pop(str(uye.id), None)
    _jail_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(embed=discord.Embed(title="Jail Kaldirildi", description=f"{uye.mention} icin onceki roller geri verildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="rolidler", aliases=["rolid", "rollerid"])
async def rol_idleri(ctx):
    roller = ctx.message.role_mentions
    if not roller:
        await ctx.send(embed=kullanim_embedi("`.rolidler @rol1 @rol2 @rol3`"))
        return
    metin = ", ".join(str(rol.id) for rol in roller)
    await ctx.send(f"`{metin}`")


for _eski in ("yardim", "help", "yardm", "ban"):
    try:
        bot.remove_command(_eski)
    except Exception:
        pass


def _komut_sahibi_degisebilir_mi(interaction: discord.Interaction, sahibi_id: int) -> bool:
    return interaction.user.id == sahibi_id


@bot.command(name="yardim", aliases=["yardm", "help"])
async def yardim_final(ctx):
    komutlar = _yardim_komutlarini_topla()
    sistem_haritasi = _yardim_sistem_haritasi()
    sahibi_id = ctx.author.id

    def temel_embed(baslik: str, aciklama: str) -> discord.Embed:
        embed = discord.Embed(
            title=f"Komut Paneli  {baslik}",
            description=aciklama,
            color=0x20253A,
            timestamp=datetime.now(timezone.utc)
        )
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
            embed.set_author(name=f"{ctx.guild.name} Komutlar", icon_url=ctx.guild.icon.url)
        else:
            embed.set_author(name=f"{ctx.guild.name} Komutlar")
        embed.set_footer(text=f"Toplam {sum(len(v) for v in komutlar.values())} komut  Secici menu aktif")
        return embed

    def ana_embed():
        embed = temel_embed("Ana Menu", "Asagidaki secicilerle kategorileri ve sistemleri gezebilirsin.")
        kategori_ozet = [f" **{kategori}** `({len(kayitlar)})`" for kategori, kayitlar in komutlar.items() if kayitlar]
        embed.add_field(name="Kategoriler", value="\n".join(kategori_ozet[:8]) or "-", inline=True)
        sistem_ozet = []
        for sistem, adlar in sistem_haritasi.items():
            sayi = sum(1 for liste in komutlar.values() for kayit in liste if kayit["ad"] in adlar)
            sistem_ozet.append(f" **{sistem}** `({sayi})`")
        embed.add_field(name="Sistemler", value="\n".join(sistem_ozet[:9]) or "-", inline=True)
        embed.add_field(name="Hizli Baslangic", value="`.profil`\n`.ticketpanel`\n`.levelkur`\n`.gifcevap`\n`.jailkur`", inline=False)
        return embed

    def kategori_embed(kategori: str):
        kayitlar = komutlar.get(kategori, [])
        embed = temel_embed(kategori, "Bu kategorideki tum komutlar asagida listeleniyor.")
        for i, parca in enumerate(_yardim_parcalari(_yardim_komut_metni(kayitlar))[:6]):
            embed.add_field(name=f"Liste {i + 1}", value=parca, inline=False)
        return embed

    def sistem_embed(sistem: str):
        adlar = sistem_haritasi.get(sistem, set())
        kayitlar = []
        for liste in komutlar.values():
            kayitlar.extend([kayit for kayit in liste if kayit["ad"] in adlar])
        kayitlar.sort(key=lambda x: x["gosterim"])
        embed = temel_embed(f"{sistem} Sistemi", f"{sistem} ile ilgili tum komutlar burada.")
        for i, parca in enumerate(_yardim_parcalari(_yardim_komut_metni(kayitlar))[:6]):
            embed.add_field(name=f"Liste {i + 1}", value=parca, inline=False)
        return embed

    class KategoriSec(discord.ui.Select):
        def __init__(self):
            secenekler = [discord.SelectOption(label=kategori, value=kategori, description=f"{len(kayitlar)} komut") for kategori, kayitlar in komutlar.items() if kayitlar]
            super().__init__(placeholder="Kategoriler", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if not _komut_sahibi_degisebilir_mi(interaction, sahibi_id):
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            await interaction.response.edit_message(embed=kategori_embed(self.values[0]), view=view)

    class SistemSec(discord.ui.Select):
        def __init__(self):
            secenekler = [discord.SelectOption(label=sistem, value=sistem, description="Sistem komutlarini gosterir") for sistem in sistem_haritasi]
            super().__init__(placeholder="Sistemler", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if not _komut_sahibi_degisebilir_mi(interaction, sahibi_id):
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            await interaction.response.edit_message(embed=sistem_embed(self.values[0]), view=view)

    class MenuSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label="Ana Menu", value="ana", description="Ozet ekrana don"),
                discord.SelectOption(label="Tum Komutlar", value="tum", description="Tum aktif komutlari tek listede goster"),
            ]
            super().__init__(placeholder="Yardim Menusu", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if not _komut_sahibi_degisebilir_mi(interaction, sahibi_id):
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            if self.values[0] == "ana":
                await interaction.response.edit_message(embed=ana_embed(), view=view)
                return
            tum = []
            for kategori in ["Ayarlar", "Moderasyon", "Roller", "Sistemler", "Kullanici", "Eglence", "Slash", "Diger"]:
                tum.extend(komutlar.get(kategori, []))
            tum.sort(key=lambda x: x["gosterim"])
            embed = temel_embed("Tum Komutlar", "Koddaki tum aktif komutlar burada listeleniyor.")
            for i, parca in enumerate(_yardim_parcalari(_yardim_komut_metni(tum), limit=850)[:8]):
                embed.add_field(name=f"Liste {i + 1}", value=parca, inline=False)
            await interaction.response.edit_message(embed=embed, view=view)

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.add_item(KategoriSec())
            self.add_item(SistemSec())
            self.add_item(MenuSec())

        async def interaction_check(self, interaction: discord.Interaction) -> bool:
            if not _komut_sahibi_degisebilir_mi(interaction, sahibi_id):
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return False
            return True

        @discord.ui.button(label="Ana Menu", style=discord.ButtonStyle.secondary, row=3)
        async def ana(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.edit_message(embed=ana_embed(), view=self)

    view = HelpView()
    await ctx.send(embed=ana_embed(), view=view)


@bot.command(name="ban", aliases=["blupbum"])
@commands.has_permissions(ban_members=True)
async def ban_final(ctx, hedef: str = None, *, sebep: str = "Sebep belirtilmedi"):
    if hedef is None and ctx.message.reference and ctx.message.reference.message_id:
        try:
            referans = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            if referans:
                hedef = str(referans.author.id)
        except Exception:
            hedef = None

    if hedef is None:
        await ctx.send(embed=kullanim_embedi("`.ban @uye [sebep]`, `.ban <id> [sebep]` veya bir mesaja yanit verip `.ban [sebep]`"))
        return

    hedef_id = None
    hedef_uye = None
    if ctx.message.mentions:
        hedef_uye = ctx.message.mentions[0]
        hedef_id = hedef_uye.id
    elif str(hedef).isdigit():
        hedef_id = int(str(hedef))
        hedef_uye = ctx.guild.get_member(hedef_id)
    else:
        hedef_uye = discord.utils.find(lambda m: str(m) == hedef or m.name == hedef, ctx.guild.members)
        hedef_id = hedef_uye.id if hedef_uye else None

    if hedef_id is None:
        await ctx.send(embed=hata_embedi("Gecersiz Hedef", "Banlanacak kullaniciyi mention, isim veya ID ile belirtmelisin."))
        return
    if hedef_id == ctx.author.id:
        await ctx.send(embed=hata_embedi("Islem Engellendi", "Kendini banlayamazsin."))
        return
    if hedef_uye is not None:
        if hedef_uye.top_role >= ctx.author.top_role and ctx.author != ctx.guild.owner:
            await ctx.send(embed=hata_embedi("Yetki Yetersiz", "Bu uyeyi banlayacak yetkin yok."))
            return
        if hedef_uye.top_role >= ctx.guild.me.top_role:
            await ctx.send(embed=hata_embedi("Bot Yetkisi Yetersiz", "Bot bu uyeyi rol hiyerarsisi nedeniyle banlayamiyor."))
            return

    try:
        await ctx.guild.ban(discord.Object(id=hedef_id), reason=f"{ctx.author} tarafindan: {sebep}", delete_message_seconds=0)
    except discord.Forbidden:
        await ctx.send(embed=hata_embedi("Ban Basarisiz", "Botun ban yetkisi veya rol hiyerarsisi yetersiz."))
        return
    except discord.HTTPException as e:
        await ctx.send(embed=hata_embedi("Ban Basarisiz", f"Discord ban istegini reddetti: {e}"))
        return

    hedef_yazi = hedef_uye.mention if hedef_uye else f"`{hedef_id}`"
    embed = mod_embed(" Uye Banlandi", RENKLER["ban"], **{
        " Hedef": hedef_yazi,
        " Sebep": sebep,
        " Yetkili": ctx.author.mention
    })
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "ban_log", embed)


for _eski_help in ("yardim", "help", "yardm"):
    try:
        bot.remove_command(_eski_help)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardm", "help"])
async def yardim_sade(ctx):
    komutlar = _yardim_komutlarini_topla()
    sistem_haritasi = _yardim_sistem_haritasi()
    sahibi_id = ctx.author.id

    def temel_embed(baslik: str, aciklama: str) -> discord.Embed:
        embed = discord.Embed(
            title=f"Komut Paneli | {baslik}",
            description=aciklama,
            color=0x23283B,
            timestamp=datetime.now(timezone.utc)
        )
        if ctx.guild.icon:
            embed.set_author(name=f"{ctx.guild.name} Komutlar", icon_url=ctx.guild.icon.url)
            embed.set_thumbnail(url=ctx.guild.icon.url)
        else:
            embed.set_author(name=f"{ctx.guild.name} Komutlar")
        embed.set_footer(text=f"Toplam {sum(len(v) for v in komutlar.values())} komut")
        return embed

    def ana_embed():
        embed = temel_embed("Ana Menu", "Daha temiz bir gorunum icin menuyu kisalttim. Kategori veya sistem secip direkt ilgili komutlari gor.")
        kategori_ozet = [f"**{kategori}** {len(kayitlar)}" for kategori, kayitlar in komutlar.items() if kayitlar]
        sistem_ozet = []
        for sistem, adlar in sistem_haritasi.items():
            sayi = sum(1 for liste in komutlar.values() for kayit in liste if kayit["ad"] in adlar)
            sistem_ozet.append(f"**{sistem}** {sayi}")
        embed.add_field(name="Kategoriler", value="  ".join(kategori_ozet[:8]) or "-", inline=False)
        embed.add_field(name="Sistemler", value="  ".join(sistem_ozet[:7]) or "-", inline=False)
        embed.add_field(name="Hizli Baslangic", value=".profil  .ticketpanel  .levelkur  .gifcevap  .jailkur", inline=False)
        return embed

    def detay_embed(baslik: str, kayitlar: list[dict], aciklama: str):
        embed = temel_embed(baslik, aciklama)
        parcalar = _yardim_parcalari(_yardim_komut_metni(kayitlar), limit=700)
        for i, parca in enumerate(parcalar[:3]):
            embed.add_field(name=f"Komutlar {i + 1}", value=parca, inline=False)
        return embed

    class KategoriSec(discord.ui.Select):
        def __init__(self):
            secenekler = [discord.SelectOption(label=kategori, value=kategori, description=f"{len(kayitlar)} komut") for kategori, kayitlar in komutlar.items() if kayitlar]
            super().__init__(placeholder="Kategoriler", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            await interaction.response.edit_message(embed=detay_embed(self.values[0], komutlar.get(self.values[0], []), "Bu kategorideki komutlar."), view=view)

    class SistemSec(discord.ui.Select):
        def __init__(self):
            secenekler = [discord.SelectOption(label=sistem, value=sistem, description="Sistem komutlarini gosterir") for sistem in sistem_haritasi]
            super().__init__(placeholder="Sistemler", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            kayitlar = []
            for liste in komutlar.values():
                kayitlar.extend([kayit for kayit in liste if kayit["ad"] in sistem_haritasi.get(self.values[0], set())])
            kayitlar.sort(key=lambda x: x["gosterim"])
            await interaction.response.edit_message(embed=detay_embed(f"{self.values[0]} Sistemi", kayitlar, "Bu sistemle ilgili komutlar."), view=view)

    class MenuSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label="Ana Menu", value="ana", description="Ozet ekrana don"),
                discord.SelectOption(label="Tum Komutlar", value="tum", description="Tum aktif komutlari listeler"),
            ]
            super().__init__(placeholder="Yardim Menusu", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            if self.values[0] == "ana":
                await interaction.response.edit_message(embed=ana_embed(), view=view)
                return
            tum = []
            for kategori in ["Ayarlar", "Moderasyon", "Roller", "Sistemler", "Kullanici", "Eglence", "Slash", "Diger"]:
                tum.extend(komutlar.get(kategori, []))
            tum.sort(key=lambda x: x["gosterim"])
            await interaction.response.edit_message(embed=detay_embed("Tum Komutlar", tum, "Aktif komutlar tek listede."), view=view)

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.add_item(KategoriSec())
            self.add_item(SistemSec())
            self.add_item(MenuSec())

        async def interaction_check(self, interaction: discord.Interaction) -> bool:
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return False
            return True

        @discord.ui.button(label="Ana Menu", style=discord.ButtonStyle.secondary, row=3)
        async def ana(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.edit_message(embed=ana_embed(), view=self)

    view = HelpView()
    await ctx.send(embed=ana_embed(), view=view)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot alyor"

def run_flask():
    port = int(os.environ.get("PORT", 10000))  # Render iin 10000
    app.run(host="0.0.0.0", port=port)

Thread(target=run_flask).start()


if __name__ == "__main__":
    pass


for _eski_help2 in ("yardim", "help", "yardm"):
    try:
        bot.remove_command(_eski_help2)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardm", "help"])
async def yardim_marpel_stili(ctx):
    komutlar = _yardim_komutlarini_topla()
    sistem_haritasi = _yardim_sistem_haritasi()
    sahibi_id = ctx.author.id

    kategori_sirasi = ["Ayarlar", "Moderasyon", "Roller", "Sistemler", "Kullanici", "Eglence", "Slash", "Diger"]
    kategori_etiketleri = {
        "Ayarlar": "m:ayarlar",
        "Moderasyon": "m:mod",
        "Roller": "m:roller",
        "Sistemler": "m:extra",
        "Kullanici": "m:kullanici",
        "Eglence": "m:elence",
        "Slash": "m:slash",
        "Diger": "m:komutlar",
    }
    kategori_renkleri = {
        "Ayarlar": "",
        "Moderasyon": "",
        "Roller": "",
        "Sistemler": "",
        "Kullanici": "",
        "Eglence": "",
        "Slash": "",
        "Diger": "",
    }
    sistem_gosterimleri = {
        "Log": " log",
        "Ticket": " destek",
        "Partner": " partner",
        "Level": " /rank",
        "Hosgeldin": " karlama",
        "Guvenlik": " koruma",
        "Rol Panelleri": " roller",
        "Eglence": " ekili",
        "Moderasyon": " mod",
    }
    kullanici_sistemleri = [
        " profil",
        " seviye",
        " afk",
        " sunucu",
        " ekili",
        " gifcevap",
        " jail",
        " rolidler",
    ]

    def temel_embed(title_text: str, description: str = "") -> discord.Embed:
        embed = discord.Embed(
            title=title_text,
            description=description,
            color=0x1B1930,
            timestamp=datetime.now(timezone.utc)
        )
        if ctx.guild.icon:
            embed.set_author(name="Marpel Komutlar", icon_url=ctx.guild.icon.url)
            embed.set_thumbnail(url=ctx.guild.icon.url)
        else:
            embed.set_author(name="Marpel Komutlar")
        embed.set_footer(text=f"Toplam {sum(len(v) for v in komutlar.values())} komut  {zaman_damgasi()}")
        return embed

    def ana_embed():
        embed = temel_embed("Marpel Komutlar")
        kategori_satirlari = []
        toplam = sum(len(v) for v in komutlar.values())
        kategori_satirlari.append(f" **m:komutlar** ({toplam})")
        for kategori in kategori_sirasi:
            if komutlar.get(kategori):
                kategori_satirlari.append(f"{kategori_renkleri.get(kategori, '')} **{kategori_etiketleri.get(kategori, kategori.lower())}** ({len(komutlar[kategori])})")
        embed.add_field(name=" Kategoriler", value="\n".join(kategori_satirlari[:6]), inline=True)
        embed.add_field(name="", value="", inline=True)

        sol = []
        for sistem in ["Eglence", "Guvenlik", "Log", "Ticket", "Rol Panelleri"]:
            if sistem in sistem_gosterimleri:
                sol.append(sistem_gosterimleri[sistem])
        sag = kullanici_sistemleri
        embed.add_field(name=" Sistemler", value="\n".join(sol[:8]), inline=True)
        embed.add_field(name=" Kullanc Sistemleri", value="\n".join(sag[:8]), inline=True)
        return embed

    def detay_embed(baslik: str, kayitlar: list[dict], aciklama: str):
        embed = temel_embed(f"Marpel Komutlar", aciklama)
        embed.add_field(name=baslik, value="\n\n".join(_yardim_parcalari(_yardim_komut_metni(kayitlar), limit=850)[:3]) or "Komut bulunamadi.", inline=False)
        return embed

    class KategoriSec(discord.ui.Select):
        def __init__(self):
            secenekler = []
            tum = sum(len(v) for v in komutlar.values())
            secenekler.append(discord.SelectOption(label="Tm Komutlar", value="__tum__", description=f"{tum} komut"))
            for kategori in kategori_sirasi:
                if komutlar.get(kategori):
                    secenekler.append(discord.SelectOption(
                        label=kategori,
                        value=kategori,
                        description=f"{len(komutlar[kategori])} komut",
                        emoji=""
                    ))
            super().__init__(placeholder="Kategoriler", min_values=1, max_values=1, options=secenekler, row=1)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            if self.values[0] == "__tum__":
                tum = []
                for kategori in kategori_sirasi + ["Diger"]:
                    tum.extend(komutlar.get(kategori, []))
                tum.sort(key=lambda x: x["gosterim"])
                await interaction.response.edit_message(embed=detay_embed("Tm Komutlar", tum, "Sunucudaki tm aktif komutlar."), view=view)
                return
            await interaction.response.edit_message(embed=detay_embed(self.values[0], komutlar.get(self.values[0], []), "Setiin kategorideki komutlar."), view=view)

    class SistemSec(discord.ui.Select):
        def __init__(self):
            secenekler = [discord.SelectOption(label=sistem, value=sistem, description="Sistem komutlarini gosterir", emoji="") for sistem in sistem_haritasi]
            super().__init__(placeholder="Sistemler", min_values=1, max_values=1, options=secenekler, row=2)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            kayitlar = []
            for liste in komutlar.values():
                kayitlar.extend([kayit for kayit in liste if kayit["ad"] in sistem_haritasi.get(self.values[0], set())])
            kayitlar.sort(key=lambda x: x["gosterim"])
            await interaction.response.edit_message(embed=detay_embed(f"{self.values[0]} Sistemi", kayitlar, "Setiin sistemle ilgili komutlar."), view=view)

    class YardimMenuSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label="Ana Men", value="ana", description="lk grnm a"),
                discord.SelectOption(label="Hzl Balang", value="hizli", description="En sk kullanlan komutlar"),
            ]
            super().__init__(placeholder="Yardm Mens", min_values=1, max_values=1, options=secenekler, row=3)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            if self.values[0] == "ana":
                await interaction.response.edit_message(embed=ana_embed(), view=view)
                return
            hizli = [
                {"gosterim": ".profil", "aciklama": "Profil ve seviye durumunu gosterir.", "aliases": []},
                {"gosterim": ".ticketpanel", "aciklama": "Ticket paneli gonderir.", "aliases": []},
                {"gosterim": ".levelkur", "aciklama": "Level sistemini modal ile kurar.", "aliases": []},
                {"gosterim": ".gifcevap", "aciklama": "Whitelistli gif cevap sistemi kurar.", "aliases": []},
                {"gosterim": ".jailkur", "aciklama": "Jail sistemini modal ile kurar.", "aliases": []},
            ]
            await interaction.response.edit_message(embed=detay_embed("Hzl Balang", hizli, "En sk kullanlan kurulum komutlar."), view=view)

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.add_item(KategoriSec())
            self.add_item(SistemSec())
            self.add_item(YardimMenuSec())

        async def interaction_check(self, interaction: discord.Interaction) -> bool:
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return False
            return True

    view = HelpView()
    await ctx.send(embed=ana_embed(), view=view)


try:
    bot.remove_command("animerolpanel")
except Exception:
    pass


@bot.command(name="animerolpanel", aliases=["anime-rol-panel"])
@commands.has_permissions(manage_roles=True)
async def anime_rol_panel_kalici(ctx):
    rol_idleri = [rol_id for rol_id in anime_rollari_al(ctx.guild.id) if ctx.guild.get_role(rol_id)]
    if not rol_idleri:
        await ctx.send(embed=kullanim_embedi("Once `.animerollerikur` komutunu kullanarak anime rollerini kurmalisin."))
        return
    mesaj = await ctx.send(
        embed=_anime_panel_embed_olustur(ctx.guild, rol_idleri, 0),
        view=AnimeRolViewPersistent(ctx.guild.id, rol_idleri, 0)
    )
    anime_panel_mesaji_ekle(ctx.guild.id, ctx.channel.id, mesaj.id)


async def _guvenlik_eylem_isle(
    guild: discord.Guild,
    sorumlu: discord.Member | discord.User | None,
    eylem: str,
    hedef: str,
    limit: int,
):
    if sorumlu is None or getattr(sorumlu, "bot", False):
        return
    if guild.owner_id == sorumlu.id:
        return

    ayar = _guvenlik_ayar_al(guild.id)
    if not ayar.get("aktif"):
        return
    if await _guvenlik_sorumlu_whitelistte_mi(guild, sorumlu, ayar):
        return

    simdi = datetime.now(timezone.utc)
    pencere = max(10, int(ayar.get("sure_saniye", 60)))

    def _guncelle(ayarlar):
        gk = str(guild.id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        guvenlik = ayarlar[gk].setdefault("guvenlik", {})
        durumlar = guvenlik.setdefault("durumlar", {})
        uye_durum = durumlar.setdefault(str(sorumlu.id), {})
        eylem_durum = uye_durum.get(eylem, {})

        baslangic_str = eylem_durum.get("baslangic")
        sayi = int(eylem_durum.get("sayi", 0) or 0)

        if baslangic_str:
            try:
                baslangic = utc_datetime_from_iso(baslangic_str)
            except Exception:
                baslangic = simdi
        else:
            baslangic = simdi

        if (simdi - baslangic).total_seconds() > pencere:
            baslangic = simdi
            sayi = 0

        sayi += 1
        uye_durum[eylem] = {
            "baslangic": baslangic.isoformat(),
            "sayi": sayi,
        }
        return {"sayi": sayi}

    sonuc = ayarlari_guncelle(_guncelle)
    sayi = int((sonuc or {}).get("sayi", 0) or 0)
    if sayi < limit:
        return

    uye = guild.get_member(sorumlu.id)
    if uye is None:
        try:
            uye = await guild.fetch_member(sorumlu.id)
        except discord.HTTPException:
            uye = None
    if uye is None or guild.owner_id == uye.id:
        return

    jail_basarili, jail_sonuc = await _jail_uygula_dahili(
        guild,
        uye,
        sebep=f"Guvenlik sistemi: tekrarlanan {eylem} limiti asimi",
        uygulayan="Guvenlik sistemi"
    )

    embed = discord.Embed(
        title="Guvenlik Sistemi Tetiklendi",
        description=(
            f"{sorumlu.mention} `{eylem}` limiti olan **{limit}** sayisina ulasti.\n"
            f"**Son hedef:** {hedef}\n"
            f"**Sonuc:** {jail_sonuc}"
        ),
        color=RENKLER["hata"] if jail_basarili else RENKLER["mute"],
        timestamp=simdi,
    )
    embed.add_field(name="Pencere", value=f"{pencere} saniye", inline=True)
    embed.add_field(name="Mevcut", value=str(sayi), inline=True)
    embed.set_footer(text="Sunucu Guvenlik Sistemi")
    await _guvenlik_log_gonder(guild, ayar, embed)


for _yardim_sil in ("yardim", "yardm", "help"):
    try:
        bot.remove_command(_yardim_sil)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardm", "help"])
async def yardim_final_renkli(ctx):
    sahibi_id = ctx.author.id

    kategoriler = {
        " Ayarlar": [
            "ticketkur", "ticketpanel", "levelkur", "hosgeldinkur", "karsilamakur",
            "guvenlikkur", "jailkur", "sayac", "kurulumdurum", "butunsistemlerikaldir"
        ],
        " Moderasyon": [
            "ban", "blupbum", "kick", "mute", "unmute", "warn", "uyarlar",
            "uyarsil", "jail", "unjail", "temprol", "kanalkilit", "kanalac"
        ],
        " Roller": [
            "renkpanel", "rolmenu", "animerolpanel", "animerollerikur",
            "animerollerikaldir", "asagitasi", "rolidler"
        ],
        " Sistemler": [
            "gifcevap", "otocevap", "spam-koruma-kur", "spam-koruma-durum",
            "spam-koruma-muaf-rol", "spam-koruma-muaf-kanal", "kufur-kur",
            "yetkilikufurkur", "yasakli-komut", "link-koruma-kur"
        ],
        " Bilgi": [
            "profil", "sunucu", "sunucupanel", "sesistatistik", "mesajistatistik",
            "isimgecmisi", "notekle", "notlar", "notsil", "cezagecmisi",
            "yetkilipanel", "komutbilgi", "avatar", "banner", "say"
        ],
        " Extra": [
            "duyurupanel", "destekistek", "partnerpuan", "leaderboard",
            "emojiekle", "herkese-rol", "herkesten-rol", "sunucukural"
        ],
    }

    def _filtreli_komutlar(adlar):
        mevcut = []
        for ad in adlar:
            if bot.get_command(ad):
                mevcut.append(ad)
        return mevcut

    kategoriler = {k: _filtreli_komutlar(v) for k, v in kategoriler.items()}
    renkler = [0xFF66C4, 0x5865F2, 0x57F287, 0xFEE75C, 0xEB459E, 0xED4245]

    def ana_embed():
        embed = discord.Embed(
            title=" Blup Komut Mens",
            description="Daha canl, daha sade ve daha rahat okunur bir yardm ekran.\nAadan kategori seerek komutlar grntleyebilirsin.",
            color=0xFF66C4,
            timestamp=datetime.now(timezone.utc)
        )
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.add_field(
            name=" Kategoriler",
            value="\n".join(f"{kategori}  **{len(komutlar)}** komut" for kategori, komutlar in kategoriler.items() if komutlar),
            inline=False
        )
        embed.add_field(
            name=" Hzl Balang",
            value="profil  ticketpanel  levelkur  gifcevap  jailkur  kurulumdurum",
            inline=False
        )
        embed.add_field(
            name=" Not",
            value="Bu mende kod yazs grnm yok; komutlar normal yaz dzeninde gsterilir.",
            inline=False
        )
        embed.set_footer(text=f"Toplam {sum(len(v) for v in kategoriler.values())} komut  {zaman_damgasi()}")
        return embed

    def kategori_embed(kategori):
        komutlar = kategoriler.get(kategori, [])
        embed = discord.Embed(
            title=f"{kategori}",
            description="\n".join(f" .{komut}" for komut in komutlar) or "Komut bulunamadi.",
            color=random.choice(renkler),
            timestamp=datetime.now(timezone.utc)
        )
        embed.set_footer(text=zaman_damgasi())
        return embed

    class KategoriSec(discord.ui.Select):
        def __init__(self):
            secenekler = []
            for kategori, komutlar in kategoriler.items():
                if not komutlar:
                    continue
                parcalar = kategori.split(" ", 1)
                emoji = parcalar[0]
                label = parcalar[1] if len(parcalar) > 1 else kategori
                secenekler.append(discord.SelectOption(
                    label=label,
                    value=kategori,
                    description=f"{len(komutlar)} komut",
                    emoji=emoji
                ))
            super().__init__(placeholder="Bir kategori se", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu meny sadece komutu yazan kii kullanabilir.", ephemeral=True)
                return
            await interaction.response.edit_message(embed=kategori_embed(self.values[0]), view=view)

    class HizliSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label="Ana Men", value="ana", description="Balang ekranna dn", emoji=""),
                discord.SelectOption(label="Moderasyon", value=" Moderasyon", description="Ceza komutlar", emoji=""),
                discord.SelectOption(label="Sistemler", value=" Sistemler", description="Kurulum komutlar", emoji=""),
                discord.SelectOption(label="Bilgi", value=" Bilgi", description="statistik ve bilgi komutlar", emoji=""),
            ]
            super().__init__(placeholder="Hzl gei", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu meny sadece komutu yazan kii kullanabilir.", ephemeral=True)
                return
            if self.values[0] == "ana":
                await interaction.response.edit_message(embed=ana_embed(), view=view)
            else:
                await interaction.response.edit_message(embed=kategori_embed(self.values[0]), view=view)

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.add_item(KategoriSec())
            self.add_item(HizliSec())

        async def interaction_check(self, interaction: discord.Interaction) -> bool:
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu meny sadece komutu yazan kii kullanabilir.", ephemeral=True)
                return False
            return True

    view = HelpView()
    await ctx.send(embed=ana_embed(), view=view)


def _otorol_ayar_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("otorol", {"rol_id": None, "aktif": False})


def _otorol_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "otorol", veri)


def _partner_puan_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("partner_puan", {})


def _partner_puan_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "partner_puan", veri)


@bot.listen("on_member_join")
async def otorol_dagit(member: discord.Member):
    ayar = _otorol_ayar_al(member.guild.id)
    if not ayar.get("aktif") or not ayar.get("rol_id"):
        return
    rol = member.guild.get_role(int(ayar.get("rol_id")))
    if rol:
        try:
            await member.add_roles(rol, reason="Otorol sistemi")
        except Exception:
            pass


@bot.command(name="notlar")
@commands.has_permissions(manage_guild=True)
async def notlar(ctx, uye: discord.Member = None):
    if not uye:
        await ctx.send(embed=kullanim_embedi(".notlar @uye"))
        return
    veri = _notlar_al(ctx.guild.id).get(str(uye.id), [])
    satirlar = []
    for kayit in veri[-10:]:
        yazan = ctx.guild.get_member(int(kayit.get("yazan", 0)))
        satirlar.append(f" **{yazan.display_name if yazan else 'Bilinmiyor'}:** {kayit.get('metin', '')}")
    embed = discord.Embed(title=" Uye Notlari", description="\n".join(satirlar) or "Kayitli not yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    await ctx.send(embed=embed)


@bot.command(name="notsil")
@commands.has_permissions(manage_guild=True)
async def notsil(ctx, uye: discord.Member = None):
    if not uye:
        await ctx.send(embed=kullanim_embedi(".notsil @uye"))
        return
    veri = _notlar_al(ctx.guild.id)
    veri.pop(str(uye.id), None)
    _notlar_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title=" Uye Notlari Silindi", description=f"{uye.mention} icin notlar temizlendi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="cezasil")
@commands.has_permissions(manage_guild=True)
async def ceza_sil(ctx, uye: discord.Member = None):
    if not uye:
        await ctx.send(embed=kullanim_embedi(".cezasil @uye"))
        return
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    if gk in ayarlar and "uyarilar" in ayarlar[gk]:
        ayarlar[gk]["uyarilar"].pop(str(uye.id), None)
        ayarlari_kaydet(ayarlar)
    await ctx.send(embed=discord.Embed(title=" Ceza Gecmisi Temizlendi", description=f"{uye.mention} icin warn kayitlari temizlendi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="otorol")
@commands.has_permissions(manage_roles=True)
async def otorol(ctx, rol: discord.Role = None):
    if not rol:
        ayar = _otorol_ayar_al(ctx.guild.id)
        aktif_rol = ctx.guild.get_role(int(ayar.get("rol_id", 0))) if ayar.get("rol_id") else None
        await ctx.send(embed=discord.Embed(title=" Otorol Durumu", description=f"Aktif: {'Evet' if ayar.get('aktif') else 'Hayir'}\nRol: {aktif_rol.mention if aktif_rol else 'Yok'}", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))
        return
    _otorol_ayar_kaydet(ctx.guild.id, {"rol_id": rol.id, "aktif": True})
    await ctx.send(embed=discord.Embed(title=" Otorol Ayarlandi", description=f"Yeni gelenlere {rol.mention} verilecek.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="yetkiver")
@commands.has_permissions(manage_roles=True)
async def yetki_ver(ctx, uye: discord.Member = None, rol: discord.Role = None):
    if not uye or not rol:
        await ctx.send(embed=kullanim_embedi(".yetkiver @uye @rol"))
        return
    await uye.add_roles(rol, reason=f"{ctx.author} tarafindan yetki verildi")
    await ctx.send(embed=discord.Embed(title=" Yetki Verildi", description=f"{uye.mention} kullanicisina {rol.mention} verildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="yetkial")
@commands.has_permissions(manage_roles=True)
async def yetki_al(ctx, uye: discord.Member = None, rol: discord.Role = None):
    if not uye or not rol:
        await ctx.send(embed=kullanim_embedi(".yetkial @uye @rol"))
        return
    await uye.remove_roles(rol, reason=f"{ctx.author} tarafindan yetki alindi")
    await ctx.send(embed=discord.Embed(title=" Yetki Alindi", description=f"{uye.mention} kullanicisindan {rol.mention} alindi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="komutbilgi")
async def komut_bilgi(ctx, komut_adi: str = None):
    if not komut_adi:
        await ctx.send(embed=kullanim_embedi(".komutbilgi mute"))
        return
    komut = bot.get_command(komut_adi.lower())
    if not komut:
        await ctx.send(embed=hata_embedi("Komut Bulunamadi", "Bu isimle kayitli bir komut yok."))
        return
    embed = discord.Embed(title=" Komut Bilgisi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Komut", value=f".{komut.name}", inline=True)
    embed.add_field(name="Kisa Aciklama", value=komut.help or "Aciklama yok.", inline=False)
    embed.add_field(name="Aliaslar", value=", ".join(komut.aliases) if komut.aliases else "Yok", inline=False)
    await ctx.send(embed=embed)


@bot.command(name="avatar")
async def avatar(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    embed = discord.Embed(title=" Avatar", description=f"{hedef.mention} kullanicisinin avatar", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.set_image(url=hedef.display_avatar.url)
    await ctx.send(embed=embed)


@bot.command(name="banner")
async def banner(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    kullanici = await bot.fetch_user(hedef.id)
    embed = discord.Embed(title=" Banner", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    if kullanici.banner:
        embed.set_image(url=kullanici.banner.url)
        embed.description = f"{hedef.mention} kullanicisinin banneri"
    else:
        embed.description = "Bu kullanicinin banneri yok."
    await ctx.send(embed=embed)


@bot.command(name="sunucukural")
@commands.has_permissions(manage_guild=True)
async def sunucu_kural(ctx, *, metin: str = None):
    if not metin:
        await ctx.send(embed=kullanim_embedi(".sunucukural Kurallari buraya yaz"))
        return
    embed = discord.Embed(title=" Sunucu Kurallari", description=metin, color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    await ctx.send(embed=embed)


@bot.command(name="duyurupanel")
@commands.has_permissions(manage_guild=True)
async def duyuru_panel(ctx, *, metin: str = None):
    if not metin:
        await ctx.send(embed=kullanim_embedi(".duyurupanel Bugun etkinlik var!"))
        return
    embed = discord.Embed(title=" Duyuru", description=metin, color=RENKLER["basari"], timestamp=datetime.now(timezone.utc))
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=embed)


@bot.command(name="destekistek")
async def destek_istek(ctx, *, metin: str = None):
    if not metin:
        await ctx.send(embed=kullanim_embedi(".destekistek Yardim lazim"))
        return
    ayar = _destekistek_ayar_al(ctx.guild.id)
    log_kanal = ctx.guild.get_channel(int(ayar.get("log_kanal_id") or 0)) if ayar.get("log_kanal_id") else None

    kullanici_embed = discord.Embed(
        title="Destek Istegin Alindi",
        description="Mesajin yetkililere iletildi. En kisa surede donus yapilacak.",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc),
    )
    kullanici_embed.add_field(name="Mesaj", value=metin[:1024], inline=False)
    if log_kanal:
        kullanici_embed.add_field(name="Log Kanali", value=log_kanal.mention, inline=True)
    await ctx.send(embed=kullanici_embed)

    if log_kanal:
        log_embed = discord.Embed(
            title="Yeni Destek Istegi",
            description="Bir kullanici destek istegi gonderdi.",
            color=RENKLER["bilgi"],
            timestamp=datetime.now(timezone.utc),
        )
        log_embed.add_field(name="Kullanici", value=f"{ctx.author.mention}\n`{ctx.author}`", inline=True)
        log_embed.add_field(name="Kullanici ID", value=str(ctx.author.id), inline=True)
        log_embed.add_field(name="Kanal", value=ctx.channel.mention, inline=True)
        log_embed.add_field(name="Sunucu", value=ctx.guild.name, inline=True)
        log_embed.add_field(name="Mesaj ID", value=str(ctx.message.id), inline=True)
        log_embed.add_field(name="Zaman", value=zaman_damgasi(), inline=True)
        log_embed.add_field(name="Icerik", value=metin[:1024], inline=False)
        log_embed.add_field(name="Mesaja Git", value=f"[Tikla]({ctx.message.jump_url})", inline=False)
        log_embed.set_thumbnail(url=ctx.author.display_avatar.url)
        await log_kanal.send(embed=log_embed)


@bot.command(name="destekistek-log", help="Destek istekleri icin log kanali ayarlar.")
@commands.has_permissions(manage_guild=True)
async def destekistek_log(ctx, kanal: discord.TextChannel = None):
    if not kanal:
        ayar = _destekistek_ayar_al(ctx.guild.id)
        aktif = ctx.guild.get_channel(int(ayar.get("log_kanal_id") or 0)) if ayar.get("log_kanal_id") else None
        await ctx.send(embed=discord.Embed(title="Destek Istek Logu", description=aktif.mention if aktif else "Ayarlanmamis", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))
        return
    _destekistek_ayar_kaydet(ctx.guild.id, {"log_kanal_id": kanal.id})
    await ctx.send(embed=discord.Embed(title="Destek Istek Logu Ayarlandi", description=f"Yeni destek istekleri {kanal.mention} kanalina gidecek.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="partnerpuan")
@commands.has_permissions(manage_guild=True)
async def partner_puan(ctx, uye: discord.Member = None, puan: int = None):
    if not uye or puan is None:
        await ctx.send(embed=kullanim_embedi(".partnerpuan @uye 10"))
        return
    veri = _partner_puan_al(ctx.guild.id)
    veri[str(uye.id)] = int(veri.get(str(uye.id), 0)) + int(puan)
    _partner_puan_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title=" Partner Puani Guncellendi", description=f"{uye.mention} kullanicisinin puani `{veri[str(uye.id)]}` oldu.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="leaderboard")
async def leaderboard(ctx):
    ayarlar = ayarlari_yukle().get(str(ctx.guild.id), {})
    profil = ayarlar.get("profil_istat", {})
    puanlar = _partner_puan_al(ctx.guild.id)
    satirlar = []
    for uye_id, veri in profil.items():
        uye = ctx.guild.get_member(int(uye_id))
        if uye:
            mesaj = int(veri.get("message_count", 0))
            ses = int(veri.get("voice_seconds", 0))
            puan = int(puanlar.get(str(uye.id), 0))
            toplam = mesaj + (ses // 60) + (puan * 10)
            satirlar.append((toplam, f" {uye.mention}  Puan: {toplam}  Mesaj: {mesaj}  Ses: {_sureyi_formatla(ses)}  Partner: {puan}"))
    satirlar.sort(key=lambda x: x[0], reverse=True)
    embed = discord.Embed(title=" Leaderboard", description="\n".join(s[1] for s in satirlar[:10]) or "Veri yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    await ctx.send(embed=embed)


@bot.command(name="emojiekle")
@commands.has_permissions(manage_emojis=True)
async def emoji_ekle(ctx, ad: str = None, url: str = None):
    if not ad or not url:
        await ctx.send(embed=kullanim_embedi(".emojiekle gulucuk https://...png"))
        return
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                veri = await resp.read()
        emoji = await ctx.guild.create_custom_emoji(name=ad[:32], image=veri, reason=f"{ctx.author} tarafindan eklendi")
        await ctx.send(embed=discord.Embed(title=" Emoji Eklendi", description=f"{emoji} basariyla eklendi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))
    except Exception as e:
        await ctx.send(embed=hata_embedi("Emoji Eklenemedi", str(e)))


@bot.command(name="kanalkilit")
@commands.has_permissions(manage_channels=True)
async def kanal_kilit(ctx, kanal: discord.TextChannel = None):
    hedef = kanal or ctx.channel
    await hedef.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(embed=discord.Embed(title=" Kanal Kilitlendi", description=f"{hedef.mention} kilitlendi.", color=RENKLER["mute"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="kanalac")
@commands.has_permissions(manage_channels=True)
async def kanal_ac(ctx, kanal: discord.TextChannel = None):
    hedef = kanal or ctx.channel
    await hedef.set_permissions(ctx.guild.default_role, send_messages=None)
    await ctx.send(embed=discord.Embed(title=" Kanal Acildi", description=f"{hedef.mention} tekrar acildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="herkese-rol")
@commands.has_permissions(manage_roles=True)
async def herkese_rol(ctx, rol: discord.Role = None):
    if not rol:
        await ctx.send(embed=kullanim_embedi(".herkese-rol @rol"))
        return
    sayi = 0
    for uye in ctx.guild.members:
        if not uye.bot and rol not in uye.roles:
            try:
                await uye.add_roles(rol, reason=f"{ctx.author} tarafindan herkese rol")
                sayi += 1
            except Exception:
                pass
    await ctx.send(embed=discord.Embed(title=" Herkese Rol Verildi", description=f"{sayi} uyeye {rol.mention} verildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="herkesten-rol")
@commands.has_permissions(manage_roles=True)
async def herkesten_rol(ctx, rol: discord.Role = None):
    if not rol:
        await ctx.send(embed=kullanim_embedi(".herkesten-rol @rol"))
        return
    sayi = 0
    for uye in ctx.guild.members:
        if rol in uye.roles:
            try:
                await uye.remove_roles(rol, reason=f"{ctx.author} tarafindan herkesten rol")
                sayi += 1
            except Exception:
                pass
    await ctx.send(embed=discord.Embed(title=" Herkesten Rol Alindi", description=f"{sayi} uyeden {rol.mention} alindi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="say")
async def say_cmd(ctx):
    g = ctx.guild
    ses = sum(1 for u in g.members if u.voice and u.voice.channel)
    aktif = sum(1 for u in g.members if u.status != discord.Status.offline)
    embed = discord.Embed(title=" Say", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Toplam Uye", value=str(g.member_count), inline=True)
    embed.add_field(name="Aktif", value=str(aktif), inline=True)
    embed.add_field(name="Seste", value=str(ses), inline=True)
    embed.add_field(name="Bot", value=str(sum(1 for u in g.members if u.bot)), inline=True)
    embed.add_field(name="Insan", value=str(sum(1 for u in g.members if not u.bot)), inline=True)
    await ctx.send(embed=embed)


@bot.command(name="rolbilgi")
async def rol_bilgi(ctx, rol: discord.Role = None):
    if not rol:
        await ctx.send(embed=kullanim_embedi(".rolbilgi @rol"))
        return
    embed = discord.Embed(title=" Rol Bilgisi", color=rol.color if rol.color.value else RENKLER["rol"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Rol", value=rol.mention, inline=True)
    embed.add_field(name="ID", value=str(rol.id), inline=True)
    embed.add_field(name="Uye Sayisi", value=str(len(rol.members)), inline=True)
    embed.add_field(name="Renk", value=str(rol.color), inline=True)
    embed.add_field(name="Pozisyon", value=str(rol.position), inline=True)
    await ctx.send(embed=embed)


@bot.command(name="kanalbilgi")
async def kanal_bilgi(ctx, kanal: discord.abc.GuildChannel = None):
    hedef = kanal or ctx.channel
    embed = discord.Embed(title=" Kanal Bilgisi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Ad", value=hedef.name, inline=True)
    embed.add_field(name="ID", value=str(hedef.id), inline=True)
    embed.add_field(name="Tur", value=type(hedef).__name__, inline=True)
    if getattr(hedef, "category", None):
        embed.add_field(name="Kategori", value=hedef.category.name, inline=True)
    await ctx.send(embed=embed)


@bot.command(name="kullanicibilgi")
async def kullanici_bilgi(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    embed = discord.Embed(title=" Kullanici Bilgisi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Kullanici", value=f"{hedef.mention} `{hedef}`", inline=False)
    embed.add_field(name="ID", value=str(hedef.id), inline=True)
    embed.add_field(name="Katildi", value=hedef.joined_at.strftime("%d.%m.%Y") if hedef.joined_at else "-", inline=True)
    embed.add_field(name="Hesap Acilis", value=hedef.created_at.strftime("%d.%m.%Y"), inline=True)
    embed.add_field(name="En Yuksek Rol", value=hedef.top_role.mention if hedef.top_role else "-", inline=True)
    embed.set_thumbnail(url=hedef.display_avatar.url)
    await ctx.send(embed=embed)


@bot.command(name="ping")
async def ping_cmd(ctx):
    ms = round(bot.latency * 1000)
    renk = RENKLER["basari"] if ms < 150 else RENKLER["mute"] if ms < 300 else RENKLER["hata"]
    await ctx.send(embed=discord.Embed(title=" Pong", description=f"Gecikme: **{ms}ms**", color=renk, timestamp=datetime.now(timezone.utc)))


def _yardim_final_haritasi():
    return {
        "Ayarlar": {"emoji": "", "komutlar": ["kurulumdurum", "butunsistemlerikaldir", "uygulamakomutkapat", "otorol", "sunucukural", "duyurupanel", "sayac", "yasakli-komut"]},
        "Moderasyon": {"emoji": "", "komutlar": ["ban", "blupbum", "kick", "mute", "unmute", "jail", "unjail", "cezagecmisi", "cezasil", "kanalkilit", "kanalac"]},
        "Roller": {"emoji": "", "komutlar": ["renkpanel", "animerolpanel", "animerollerikur", "animerollerikaldir", "rolmenu", "levelrol", "levelrolsil", "levelrolleri", "yetkiver", "yetkial", "temprol", "herkese-rol", "herkesten-rol", "rolbilgi", "asagitasi", "rolidler"]},
        "Sistemler": {"emoji": "", "komutlar": ["ticketpanel", "ticketkur", "partner-kur", "partner-kapat", "partnerpuan", "gifcevap", "gifcevapkapat", "gifcevapdurum", "otocevap", "jailkur", "jailkapat", "guvenlikkur", "guvenlikkapat", "guvenlikdurum", "kufur-kur", "kufur-kapat", "kufur-listele", "yetkilikufurkur", "yetkilikufurkapat", "yetkilikufurdurum", "spam-koruma-durum", "hosgeldinkur", "hosgeldinkapat", "karsilamakur", "karsilamakapat", "levelkur", "levelkapat"]},
        "Kullanici": {"emoji": "", "komutlar": ["profil", "avatar", "banner", "kullanicibilgi", "isimgecmisi", "notekle", "notlar", "notsil", "destekistek"]},
        "Bilgi": {"emoji": "", "komutlar": ["sunucupanel", "yetkilipanel", "sesistatistik", "mesajistatistik", "leaderboard", "say", "kanalbilgi", "komutbilgi", "ping"]},
        "Diger": {"emoji": "", "komutlar": []},
    }


def _yardim_final_topla():
    harita = _yardim_final_haritasi()
    tum_komutlar = {komut.name: komut for komut in bot.commands if not komut.hidden}
    kullanilanlar = set()
    sonuc = {}
    for kategori, veri in harita.items():
        secilenler = []
        for ad in veri["komutlar"]:
            komut = tum_komutlar.get(ad)
            if komut:
                secilenler.append(komut)
                kullanilanlar.add(ad)
        sonuc[kategori] = {"emoji": veri["emoji"], "komutlar": secilenler}
    sonuc["Diger"]["komutlar"] = sorted([komut for ad, komut in tum_komutlar.items() if ad not in kullanilanlar], key=lambda k: k.name)
    return sonuc


def _yardim_aciklama(komut):
    aciklama = (komut.help or "").strip()
    return aciklama if aciklama else "Bu komut hazir."


def _yardim_sayfalari(komutlar, parca=12):
    satirlar = [f" **.{komut.name}** - {_yardim_aciklama(komut)}" for komut in komutlar] or ["Bu bolumde gorunur komut yok."]
    return ["\n".join(satirlar[i:i + parca]) for i in range(0, len(satirlar), parca)] or ["Bu bolumde gorunur komut yok."]


def _yardim_ana_embed(istek_sahibi):
    kategoriler = _yardim_final_topla()
    toplam = sum(len(v["komutlar"]) for v in kategoriler.values())
    embed = discord.Embed(title=" Komut Menusu", description="Canli, duzgun ve daha renkli bir yardim menusu. Asagidan kategori secip direkt istedigin komutlara gec.", color=0xF7C948, timestamp=datetime.now(timezone.utc))
    embed.add_field(name=" Kategoriler", value="\n".join(f"**{kategori}**: {len(veri['komutlar'])}" for kategori, veri in kategoriler.items() if veri["komutlar"]) or "Komut bulunamadi.", inline=True)
    embed.add_field(name=" Hizli Baslangic", value=" `.renkpanel`\n `.ticketpanel`\n `.levelkur`\n `.gifcevap`\n `.jailkur`\n `.komutbilgi mute`", inline=True)
    embed.add_field(name=" Ipuclari", value="Menuler sadece komutu yazan kisi tarafindan kullanilir.\n`.komutbilgi komutadi` ile detay gorebilirsin.\nToplam komut sayisi dinamik hesaplanir.", inline=False)
    embed.set_footer(text=f"{istek_sahibi} tarafindan acildi  Toplam {toplam} komut")
    return embed


def _yardim_kategori_embed(kategori, veri, sayfa):
    renkler = {"Ayarlar": 0x7ED957, "Moderasyon": 0xFF6B6B, "Roller": 0x6BCBFF, "Sistemler": 0xC77DFF, "Kullanici": 0xF9C74F, "Bilgi": 0x4D96FF, "Diger": 0xB8B8D1}
    sayfalar = _yardim_sayfalari(veri["komutlar"])
    embed = discord.Embed(title=f"{veri['emoji']} {kategori} Komutlari", description=sayfalar[sayfa], color=renkler.get(kategori, 0xF7C948), timestamp=datetime.now(timezone.utc))
    embed.add_field(name=" Komut", value=str(len(veri["komutlar"])), inline=True)
    embed.add_field(name=" Sayfa", value=f"{sayfa + 1}/{len(sayfalar)}", inline=True)
    embed.add_field(name=" Ekstra", value="`.komutbilgi komutadi`", inline=True)
    return embed


class YardimKategoriSec(discord.ui.Select):
    def __init__(self, sahip_id):
        self.sahip_id = sahip_id
        kategoriler = _yardim_final_topla()
        options = [
            discord.SelectOption(label=kategori, description=f"{len(veri['komutlar'])} komut", value=kategori)
            for kategori, veri in kategoriler.items()
            if veri["komutlar"]
        ]
        super().__init__(placeholder="Kategori sec", min_values=1, max_values=1, options=options, custom_id="yardim_final_kategori")

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.sahip_id:
            await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
            return
        self.view.aktif_kategori = self.values[0]
        self.view.sayfa = 0
        await interaction.response.edit_message(embed=self.view.mevcut_embed(), view=self.view)


class YardimSayfaButon(discord.ui.Button):
    def __init__(self, sahip_id, ileri=False):
        self.sahip_id = sahip_id
        self.ileri = ileri
        super().__init__(style=discord.ButtonStyle.secondary, label="Sonraki" if ileri else "Onceki", emoji="" if ileri else "", custom_id=f"yardim_final_{'ileri' if ileri else 'geri'}")

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.sahip_id:
            await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
            return
        if not self.view.aktif_kategori:
            await interaction.response.send_message("Once bir kategori sec.", ephemeral=True)
            return
        veri = _yardim_final_topla()[self.view.aktif_kategori]
        toplam = len(_yardim_sayfalari(veri["komutlar"]))
        self.view.sayfa = (self.view.sayfa + (1 if self.ileri else -1)) % toplam
        await interaction.response.edit_message(embed=self.view.mevcut_embed(), view=self.view)


class YardimAnaMenuButon(discord.ui.Button):
    def __init__(self, sahip_id):
        self.sahip_id = sahip_id
        super().__init__(style=discord.ButtonStyle.primary, label="Ana Menu", emoji="", custom_id="yardim_final_ana")

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.sahip_id:
            await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
            return
        self.view.aktif_kategori = None
        self.view.sayfa = 0
        await interaction.response.edit_message(embed=self.view.mevcut_embed(), view=self.view)


class YardimFinalView(discord.ui.View):
    def __init__(self, sahip_id, sahip_etiket):
        super().__init__(timeout=300)
        self.sahip_id = sahip_id
        self.sahip_etiket = sahip_etiket
        self.aktif_kategori = None
        self.sayfa = 0
        self.add_item(YardimKategoriSec(sahip_id))
        self.add_item(YardimSayfaButon(sahip_id, ileri=False))
        self.add_item(YardimSayfaButon(sahip_id, ileri=True))
        self.add_item(YardimAnaMenuButon(sahip_id))

    def mevcut_embed(self):
        if not self.aktif_kategori:
            return _yardim_ana_embed(self.sahip_etiket)
        veri = _yardim_final_topla()[self.aktif_kategori]
        return _yardim_kategori_embed(self.aktif_kategori, veri, self.sayfa)


for _yardim_sil in ("yardim", "yardm", "help", "komutlar"):
    try:
        bot.remove_command(_yardim_sil)
    except Exception:
        pass


async def _yardim_gonder(ctx):
    view = YardimFinalView(ctx.author.id, str(ctx.author))
    await ctx.send(embed=view.mevcut_embed(), view=view)


@bot.command(name="yardim", aliases=["yardm"], help="Renkli komut menusunu gosterir.")
async def yardim_final_gercek(ctx):
    await _yardim_gonder(ctx)


@bot.command(name="help", help="Renkli komut menusunu gosterir.")
async def help_final_gercek(ctx):
    await _yardim_gonder(ctx)


@bot.command(name="komutlar", help="Renkli komut menusunu gosterir.")
async def komutlar_final_gercek(ctx):
    await _yardim_gonder(ctx)


if __name__ == "__main__":
    pass


def _help_kategori_komutlari():
    tum = {c.name: c for c in bot.commands if not c.hidden}
    return {
        "Ayarlar": ["kurulumdurum", "butunsistemlerikaldir", "uygulamakomutkapat", "otorol", "sunucukural", "duyurupanel", "sayac", "sayac-kapat", "yasakli-komut", "rollog", "destekistek-log"],
        "Moderasyon": ["ban", "blupbum", "kick", "mute", "unmute", "jail", "unjail", "cezagecmisi", "cezasil", "cezapanel", "yetkiceza", "kanalkilit", "kanalac"],
        "Roller": ["renkpanel", "animerolpanel", "animerollerikur", "animerollerikaldir", "rolmenu", "levelrol", "yetkiver", "yetkial", "temprol", "roldagit", "roltemizle", "herkese-rol", "herkesten-rol", "rolbilgi", "asagitasi", "rolidler", "rozetver", "rozetal", "profil-arka-plan"],
        "Sistemler": ["ticketpanel", "ticketkur", "partner-kur", "partner-kapat", "partnerpuan", "gifcevap", "gifcevapkapat", "gifcevapdurum", "otocevap", "otocevap-kapat", "jailkur", "jailkapat", "guvenlikkur", "guvenlikkapat", "guvenlikdurum", "kufur-kur", "kufur-kapat", "kufur-listele", "yetkilikufurkur", "yetkilikufurkapat", "yetkilikufurdurum", "spam-koruma-durum", "hosgeldinkur", "hosgeldinkapat", "karsilamakur", "karsilamakapat", "levelkur", "levelkapat", "basvuru-panel", "itiraz-panel", "afis", "ses-kanal-ac", "ozeloda"],
        "Kullanici": ["profil", "seviye", "ship", "avatar", "banner", "kullanicibilgi", "isimgecmisi", "notekle", "notlar", "notsil", "not-temizle", "destekistek", "welcome-say", "kimnezaman"],
        "Bilgi": ["sunucupanel", "yetkilipanel", "seviyetop", "sesistatistik", "mesajistatistik", "leaderboard", "say", "kanalbilgi", "komutbilgi", "ping"],
    }, tum


def _help_kategori_emoji(kategori: str) -> str:
    return {
        "Ayarlar": "🌈",
        "Moderasyon": "🛡️",
        "Roller": "🎨",
        "Sistemler": "⚙️",
        "Kullanici": "👤",
        "Bilgi": "📚",
    }.get(kategori, "✨")


def _help_ana_embed(ctx):
    kategoriler, tum = _help_kategori_komutlari()
    embed = discord.Embed(
        title="Komut Menusu",
        description="Asagidaki acilir menuden bir kategori sec.",
        color=0xF7C948,
        timestamp=datetime.now(timezone.utc),
    )
    embed.add_field(
        name="Kategoriler",
        value="\n".join(f"{_help_kategori_emoji(ad)} **{ad}**: {sum(1 for k in komutlar if k in tum)}" for ad, komutlar in kategoriler.items()),
        inline=True,
    )
    embed.add_field(
        name="Hizli Baslangic",
        value="`.renkpanel`\n`.ticketpanel`\n`.levelkur`\n`.gifcevap`\n`.jailkur`\n`.komutbilgi mute`",
        inline=True,
    )
    embed.set_footer(text=f"{ctx.author} tarafindan acildi")
    return embed


def _help_kategori_embed(kategori):
    kategoriler, tum = _help_kategori_komutlari()
    satirlar = []
    for ad in kategoriler.get(kategori, []):
        komut = tum.get(ad)
        if komut:
            aciklama = (komut.help or "Bu komut hazir.").strip()
            satirlar.append(f"• **.{komut.name}** - {aciklama}")
    embed = discord.Embed(
        title=f"{_help_kategori_emoji(kategori)} {kategori} Komutlari",
        description="\n".join(satirlar[:20]) or "Bu kategoride komut yok.",
        color=0x4D96FF,
        timestamp=datetime.now(timezone.utc),
    )
    return embed


class BasitHelpSelect(discord.ui.Select):
    def __init__(self, sahip_id):
        self.sahip_id = sahip_id
        kategoriler, tum = _help_kategori_komutlari()
        options = [
            discord.SelectOption(label=ad, description=f"{sum(1 for k in komutlar if k in tum)} komut", value=ad, emoji=_help_kategori_emoji(ad))
            for ad, komutlar in kategoriler.items()
        ]
        super().__init__(placeholder="Kategori sec", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.sahip_id:
            await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
            return
        await interaction.response.edit_message(embed=_help_kategori_embed(self.values[0]), view=self.view)


class BasitHelpAnaButton(discord.ui.Button):
    def __init__(self, sahip_id, ctx):
        self.sahip_id = sahip_id
        self.ctx = ctx
        super().__init__(style=discord.ButtonStyle.primary, label="Ana Menu")

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.sahip_id:
            await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
            return
        await interaction.response.edit_message(embed=_help_ana_embed(self.ctx), view=self.view)


class BasitHelpView(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=300)
        self.add_item(BasitHelpSelect(ctx.author.id))
        self.add_item(BasitHelpAnaButton(ctx.author.id, ctx))


for _help_temizle in ("yardim", "yardm", "help", "komutlar"):
    try:
        bot.remove_command(_help_temizle)
    except Exception:
        pass


async def _basit_help_gonder(ctx):
    await ctx.send(embed=_help_ana_embed(ctx), view=BasitHelpView(ctx))


@bot.command(name="yardim", aliases=["yardm"])
async def yardim_basit(ctx):
    await _basit_help_gonder(ctx)


@bot.command(name="help")
async def help_basit(ctx):
    await _basit_help_gonder(ctx)


@bot.command(name="komutlar")
async def komutlar_basit(ctx):
    await _basit_help_gonder(ctx)


def _rozetler_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("profil_rozetleri", {})


def _rozetler_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "profil_rozetleri", veri)


def _profil_tema_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("profil_tema", {})


def _profil_tema_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "profil_tema", veri)


def _basvuru_ayar_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("basvuru_paneli", {"aktif": False, "log_kanal_id": None})


def _basvuru_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "basvuru_paneli", veri)


def _itiraz_ayar_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("itiraz_paneli", {"aktif": False, "log_kanal_id": None})


def _itiraz_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "itiraz_paneli", veri)


def _rollog_ayar_al(guild_id: int) -> dict:
    return _guild_ayar_al(guild_id).get("rol_log_ozel", {"kanal_id": None})


def _rollog_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "rol_log_ozel", veri)


class BasvuruModal(discord.ui.Modal, title="Basvuru Formu"):
    yas = discord.ui.TextInput(label="Yas", required=True, max_length=20)
    deneyim = discord.ui.TextInput(label="Deneyim", required=True, style=discord.TextStyle.paragraph, max_length=500)
    neden = discord.ui.TextInput(label="Neden sen?", required=True, style=discord.TextStyle.paragraph, max_length=500)

    def __init__(self, guild_id: int):
        super().__init__()
        self.guild_id = guild_id

    async def on_submit(self, interaction: discord.Interaction):
        ayar = _basvuru_ayar_al(self.guild_id)
        log_kanal = interaction.guild.get_channel(int(ayar.get("log_kanal_id") or 0))
        if not log_kanal:
            await interaction.response.send_message("Basvuru log kanali bulunamadi.", ephemeral=True)
            return
        embed = discord.Embed(title="Basvuru Geldi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
        embed.add_field(name="Kullanici", value=f"{interaction.user.mention} ({interaction.user.id})", inline=False)
        embed.add_field(name="Yas", value=str(self.yas), inline=True)
        embed.add_field(name="Deneyim", value=str(self.deneyim)[:1024], inline=False)
        embed.add_field(name="Neden", value=str(self.neden)[:1024], inline=False)
        await log_kanal.send(embed=embed)
        await interaction.response.send_message("Basvurun gonderildi.", ephemeral=True)


class BasvuruView(discord.ui.View):
    def __init__(self, guild_id: int):
        super().__init__(timeout=None)
        self.guild_id = guild_id

    @discord.ui.button(label="Basvuru Yap", style=discord.ButtonStyle.primary, custom_id="basvuru_yap_btn")
    async def basvuru_yap(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(BasvuruModal(self.guild_id))


class ItirazModal(discord.ui.Modal, title="Ceza Itirazi"):
    ceza = discord.ui.TextInput(label="Ceza Turu", required=True, max_length=100)
    aciklama = discord.ui.TextInput(label="Itiraz Aciklamasi", required=True, style=discord.TextStyle.paragraph, max_length=700)

    def __init__(self, guild_id: int):
        super().__init__()
        self.guild_id = guild_id

    async def on_submit(self, interaction: discord.Interaction):
        ayar = _itiraz_ayar_al(self.guild_id)
        log_kanal = interaction.guild.get_channel(int(ayar.get("log_kanal_id") or 0))
        if not log_kanal:
            await interaction.response.send_message("Itiraz log kanali bulunamadi.", ephemeral=True)
            return
        embed = discord.Embed(title="Ceza Itirazi", color=RENKLER["mute"], timestamp=datetime.now(timezone.utc))
        embed.add_field(name="Kullanici", value=f"{interaction.user.mention} ({interaction.user.id})", inline=False)
        embed.add_field(name="Ceza", value=str(self.ceza), inline=True)
        embed.add_field(name="Aciklama", value=str(self.aciklama)[:1024], inline=False)
        await log_kanal.send(embed=embed)
        await interaction.response.send_message("Itirazin gonderildi.", ephemeral=True)


class ItirazView(discord.ui.View):
    def __init__(self, guild_id: int):
        super().__init__(timeout=None)
        self.guild_id = guild_id

    @discord.ui.button(label="Itiraz Gonder", style=discord.ButtonStyle.secondary, custom_id="itiraz_yap_btn")
    async def itiraz_yap(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ItirazModal(self.guild_id))


@bot.command(name="afis", help="Hazir afis/duyuru embedi yollar.")
@commands.has_permissions(manage_guild=True)
async def afis(ctx, baslik: str = None, *, metin: str = None):
    if not baslik or not metin:
        await ctx.send(embed=kullanim_embedi(".afis Baslik metin"))
        return
    embed = discord.Embed(title=baslik, description=metin, color=0xF7C948, timestamp=datetime.now(timezone.utc))
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=embed)


@bot.command(name="roldagit", help="Belirli role sahip herkese baska rol verir.")
@commands.has_permissions(manage_roles=True)
async def roldagit(ctx, kaynak_rol: discord.Role = None, verilecek_rol: discord.Role = None):
    if not kaynak_rol or not verilecek_rol:
        await ctx.send(embed=kullanim_embedi(".roldagit @kaynakRol @verilecekRol"))
        return
    sayi = 0
    for uye in kaynak_rol.members:
        if verilecek_rol not in uye.roles:
            try:
                await uye.add_roles(verilecek_rol, reason=f"{ctx.author} tarafindan roldagit")
                sayi += 1
            except Exception:
                pass
    await ctx.send(embed=discord.Embed(title="Rol Dagitildi", description=f"{sayi} uyeye {verilecek_rol.mention} verildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="roltemizle", help="Belirli role sahip herkesten baska rolu alir.")
@commands.has_permissions(manage_roles=True)
async def roltemizle(ctx, kaynak_rol: discord.Role = None, alinacak_rol: discord.Role = None):
    if not kaynak_rol or not alinacak_rol:
        await ctx.send(embed=kullanim_embedi(".roltemizle @kaynakRol @alinacakRol"))
        return
    sayi = 0
    for uye in kaynak_rol.members:
        if alinacak_rol in uye.roles:
            try:
                await uye.remove_roles(alinacak_rol, reason=f"{ctx.author} tarafindan roltemizle")
                sayi += 1
            except Exception:
                pass
    await ctx.send(embed=discord.Embed(title="Rol Temizlendi", description=f"{sayi} uyeden {alinacak_rol.mention} alindi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="cezapanel", help="Sunucunun ceza ozetini gosterir.")
@commands.has_permissions(manage_guild=True)
async def cezapanel(ctx):
    ayar = ayarlari_yukle().get(str(ctx.guild.id), {})
    warnlar = ayar.get("uyarilar", {})
    toplam_warn = sum(len(v) for v in warnlar.values())
    jail_ayar = _jail_ayar_al(ctx.guild.id)
    jail_rol = ctx.guild.get_role(int(jail_ayar.get("rol_id") or 0)) if jail_ayar.get("rol_id") else None
    jailde = len(jail_rol.members) if jail_rol else 0
    ban_sayi = 0
    async for _ in ctx.guild.bans(limit=1000):
        ban_sayi += 1
    embed = discord.Embed(title="Ceza Paneli", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Toplam Uyari", value=str(toplam_warn), inline=True)
    embed.add_field(name="Jaildeki Uye", value=str(jailde), inline=True)
    embed.add_field(name="Sunucu Bani", value=str(ban_sayi), inline=True)
    await ctx.send(embed=embed)


@bot.command(name="yetkiceza", help="Yetkililerin son ceza hareketlerini listeler.")
@commands.has_permissions(view_audit_log=True)
async def yetkiceza(ctx):
    sayac = {}
    async for entry in ctx.guild.audit_logs(limit=50):
        if entry.action in {discord.AuditLogAction.ban, discord.AuditLogAction.kick, discord.AuditLogAction.member_update} and entry.user:
            sayac[str(entry.user)] = sayac.get(str(entry.user), 0) + 1
    satirlar = [f"• **{k}** - {v} islem" for k, v in sorted(sayac.items(), key=lambda x: x[1], reverse=True)[:10]]
    await ctx.send(embed=discord.Embed(title="Yetkili Ceza Ozeti", description="\n".join(satirlar) or "Kayit bulunamadi.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="basvuru-panel", help="Basvuru paneli kurar.")
@commands.has_permissions(manage_guild=True)
async def basvuru_panel(ctx, log_kanal: discord.TextChannel = None):
    if not log_kanal:
        await ctx.send(embed=kullanim_embedi(".basvuru-panel #log"))
        return
    _basvuru_ayar_kaydet(ctx.guild.id, {"aktif": True, "log_kanal_id": log_kanal.id})
    view = BasvuruView(ctx.guild.id)
    bot.add_view(view)
    await ctx.send(embed=discord.Embed(title="Basvuru Paneli", description="Basvuru yapmak icin asagidaki butonu kullan.", color=RENKLER["bilgi"]), view=view)


@bot.command(name="itiraz-panel", help="Ceza itiraz paneli kurar.")
@commands.has_permissions(manage_guild=True)
async def itiraz_panel(ctx, log_kanal: discord.TextChannel = None):
    if not log_kanal:
        await ctx.send(embed=kullanim_embedi(".itiraz-panel #log"))
        return
    _itiraz_ayar_kaydet(ctx.guild.id, {"aktif": True, "log_kanal_id": log_kanal.id})
    view = ItirazView(ctx.guild.id)
    bot.add_view(view)
    await ctx.send(embed=discord.Embed(title="Itiraz Paneli", description="Itiraz gondermek icin asagidaki butonu kullan.", color=RENKLER["mute"]), view=view)


@bot.command(name="sayac-kapat", help="Sayac sistemini kapatir.")
@commands.has_permissions(manage_guild=True)
async def sayac_kapat(ctx):
    _sayac_ayar_kaydet(ctx.guild.id, {"aktif": False, "hedef": 0, "kanal_id": None, "mesaj": "Hedefe ulasildi!", "tetiklendi": False})
    await ctx.send(embed=discord.Embed(title="Sayac Kapatildi", description="Sayac sistemi kapatildi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="otocevap-kapat", help="Yazi tabanli otocevabi kapatir.")
@commands.has_permissions(manage_guild=True)
async def otocevap_kapat(ctx):
    _auto_cevap_kaydet(ctx.guild.id, {})
    await ctx.send(embed=discord.Embed(title="Otocevap Kapatildi", description="Tum otocevaplar temizlendi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="not-temizle", help="Uyenin tum notlarini temizler.")
@commands.has_permissions(manage_guild=True)
async def not_temizle(ctx, uye: discord.Member = None):
    if not uye:
        await ctx.send(embed=kullanim_embedi(".not-temizle @uye"))
        return
    veri = _notlar_al(ctx.guild.id)
    veri.pop(str(uye.id), None)
    _notlar_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title="Notlar Temizlendi", description=f"{uye.mention} icin tum notlar silindi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="rollog", help="Rol hareketleri icin ozel log kanali ayarlar.")
@commands.has_permissions(manage_guild=True)
async def rollog(ctx, kanal: discord.TextChannel = None):
    if not kanal:
        ayar = _rollog_ayar_al(ctx.guild.id)
        aktif = ctx.guild.get_channel(int(ayar.get("kanal_id") or 0)) if ayar.get("kanal_id") else None
        await ctx.send(embed=discord.Embed(title="Rol Log Durumu", description=aktif.mention if aktif else "Ayarlanmamis", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))
        return
    _rollog_ayar_kaydet(ctx.guild.id, {"kanal_id": kanal.id})
    await ctx.send(embed=discord.Embed(title="Rol Log Ayarlandi", description=f"Rol hareketleri {kanal.mention} kanalina gidecek.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="ses-kanal-ac", help="Hazir bir ses kanali acar.")
@commands.has_permissions(manage_channels=True)
async def ses_kanal_ac(ctx, *, ad: str = None):
    if not ad:
        await ctx.send(embed=kullanim_embedi(".ses-kanal-ac Ozel Oda"))
        return
    kanal = await ctx.guild.create_voice_channel(ad, reason=f"{ctx.author} tarafindan olusturuldu")
    await ctx.send(embed=discord.Embed(title="Ses Kanali Acildi", description=kanal.mention if hasattr(kanal, 'mention') else kanal.name, color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="ozeloda", help="Kullanan kisi icin ozel ses odasi acar.")
async def ozeloda(ctx, *, ad: str = None):
    if not ctx.author.voice or not ctx.author.voice.channel:
        await ctx.send(embed=hata_embedi("Ses Kanalinda Degilsin", "Bu komutu kullanmak icin once bir ses kanalinda olmalisin."))
        return
    oda_adi = ad or f"{ctx.author.display_name} Ozel Oda"
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False, connect=False),
        ctx.author: discord.PermissionOverwrite(view_channel=True, connect=True, speak=True, manage_channels=True),
        ctx.guild.me: discord.PermissionOverwrite(view_channel=True, connect=True, speak=True, manage_channels=True),
    }
    kanal = await ctx.guild.create_voice_channel(oda_adi, overwrites=overwrites, reason=f"{ctx.author} icin ozel oda")
    await ctx.author.move_to(kanal)
    await ctx.send(embed=discord.Embed(title="Ozel Oda Acildi", description=f"{kanal.name} hazirlandi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="rozetver", help="Kullaniciya profil rozeti verir.")
@commands.has_permissions(manage_guild=True)
async def rozetver(ctx, uye: discord.Member = None, *, rozet: str = None):
    if not uye or not rozet:
        await ctx.send(embed=kullanim_embedi(".rozetver @uye Yardimsever"))
        return
    veri = _rozetler_al(ctx.guild.id)
    liste = veri.get(str(uye.id), [])
    if rozet not in liste:
        liste.append(rozet)
    veri[str(uye.id)] = liste
    _rozetler_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title="Rozet Verildi", description=f"{uye.mention} kullanicisina `{rozet}` rozeti verildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="rozetal", help="Kullanicidan profil rozeti alir.")
@commands.has_permissions(manage_guild=True)
async def rozetal(ctx, uye: discord.Member = None, *, rozet: str = None):
    if not uye or not rozet:
        await ctx.send(embed=kullanim_embedi(".rozetal @uye Yardimsever"))
        return
    veri = _rozetler_al(ctx.guild.id)
    liste = veri.get(str(uye.id), [])
    liste = [r for r in liste if r.lower() != rozet.lower()]
    veri[str(uye.id)] = liste
    _rozetler_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title="Rozet Alindi", description=f"{uye.mention} kullanicisindan `{rozet}` rozeti alindi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="profil-arka-plan", help="Profil komutu icin tema belirler.")
@commands.has_permissions(manage_guild=True)
async def profil_arka_plan(ctx, uye: discord.Member = None, *, tema: str = None):
    if not uye or not tema:
        await ctx.send(embed=kullanim_embedi(".profil-arka-plan @uye Sakura"))
        return
    veri = _profil_tema_al(ctx.guild.id)
    veri[str(uye.id)] = tema
    _profil_tema_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title="Profil Temasi Ayarlandi", description=f"{uye.mention} icin tema `{tema}` oldu.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="welcome-say", help="Son katilan uyeleri listeler.")
async def welcome_say(ctx):
    uyeler = sorted([m for m in ctx.guild.members if not m.bot], key=lambda m: m.joined_at or datetime.now(timezone.utc), reverse=True)[:10]
    satirlar = [f"• {u.mention} - {(u.joined_at.strftime('%d.%m.%Y %H:%M') if u.joined_at else '-')}" for u in uyeler]
    await ctx.send(embed=discord.Embed(title="Son Katilan Uyeler", description="\n".join(satirlar) or "Uye yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="kimnezaman", help="Kullanicinin zaman cizelgesini gosterir.")
async def kimnezaman(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    ayar = ayarlari_yukle().get(str(ctx.guild.id), {})
    warnlar = ayar.get("uyarilar", {}).get(str(hedef.id), [])
    rozetler = _rozetler_al(ctx.guild.id).get(str(hedef.id), [])
    tema = _profil_tema_al(ctx.guild.id).get(str(hedef.id), "Yok")
    embed = discord.Embed(title="Kim Ne Zaman", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Kullanici", value=f"{hedef.mention} ({hedef.id})", inline=False)
    embed.add_field(name="Hesap Acilis", value=hedef.created_at.strftime("%d.%m.%Y %H:%M"), inline=True)
    embed.add_field(name="Sunucu Katilim", value=hedef.joined_at.strftime("%d.%m.%Y %H:%M") if hedef.joined_at else "-", inline=True)
    embed.add_field(name="Uyari", value=str(len(warnlar)), inline=True)
    embed.add_field(name="Rozetler", value=", ".join(rozetler[:10]) if rozetler else "Yok", inline=False)
    embed.add_field(name="Profil Temasi", value=tema, inline=True)
    await ctx.send(embed=embed)


for _detay_sil in (
    "profil",
    "seviye",
    "level",
    "rank",
    "seviyetop",
    "sunucupanel",
    "yetkilipanel",
    "avatar",
    "banner",
    "rolbilgi",
    "kanalbilgi",
    "kullanicibilgi",
    "sesistatistik",
    "mesajistatistik",
    "leaderboard",
    "say",
):
    try:
        bot.remove_command(_detay_sil)
    except Exception:
        pass


def _detayli_tarih(dt: datetime | None) -> str:
    if not dt:
        return "Bilinmiyor"
    try:
        return dt.astimezone().strftime("%d.%m.%Y %H:%M")
    except Exception:
        return dt.strftime("%d.%m.%Y %H:%M")


def _kisa_sayi(deger: int) -> str:
    deger = int(deger)
    if deger >= 1_000_000:
        return f"{deger / 1_000_000:.1f}M".replace(".0", "")
    if deger >= 1_000:
        return f"{deger / 1_000:.1f}K".replace(".0", "")
    return str(deger)


def _rol_listesi_kisa(roller: list[discord.Role], limit: int = 12) -> str:
    filtreli = [r.mention for r in sorted(roller, key=lambda r: r.position, reverse=True) if not r.is_default()]
    if not filtreli:
        return "Yok"
    if len(filtreli) <= limit:
        return ", ".join(filtreli)
    kalan = len(filtreli) - limit
    return ", ".join(filtreli[:limit]) + f" ve {kalan} rol daha"


def _uye_rozet_metin(guild_id: int, user_id: int) -> str:
    rozetler = _rozetler_al(guild_id).get(str(user_id), [])
    if not rozetler:
        return "Yok"
    return ", ".join(str(r) for r in rozetler[:8])


def _profil_embed_olustur(hedef: discord.Member) -> discord.Embed:
    xp_veri = _xp_veri_al(hedef.guild.id, hedef.id)
    profil = _profil_istat_al(hedef.guild.id, hedef.id)
    ayarlar = ayarlari_yukle().get(str(hedef.guild.id), {})
    tum_xp_veri = ayarlar.get("level_xp", {})
    toplam_xp = _toplam_xp_hesapla(int(xp_veri.get("level", 0)), int(xp_veri.get("xp", 0)))
    siralama = sorted(
        tum_xp_veri.items(),
        key=lambda item: _toplam_xp_hesapla(int(item[1].get("level", 0)), int(item[1].get("xp", 0))),
        reverse=True,
    )
    sira = next((index for index, (uye_id, _) in enumerate(siralama, start=1) if uye_id == str(hedef.id)), None)
    warnlar = ayarlar.get("uyarilar", {}).get(str(hedef.id), [])
    tema = _profil_tema_al(hedef.guild.id).get(str(hedef.id), "Varsayilan")
    level = int(xp_veri.get("level", 0))
    xp = int(xp_veri.get("xp", 0))
    hedef_xp = _xp_hedef(level)

    embed = discord.Embed(
        title=f"{hedef.display_name} Profil Karti",
        description=f"{hedef.mention} icin detayli uye ozeti",
        color=hedef.color if hedef.color.value else RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc),
    )
    embed.add_field(name="Level", value=f"**{level}**", inline=True)
    embed.add_field(name="XP", value=f"**{xp} / {hedef_xp}**", inline=True)
    embed.add_field(name="Seviye Sirasi", value=f"**#{sira or '-'}**", inline=True)
    embed.add_field(name="Toplam XP", value=f"**{_kisa_sayi(toplam_xp)}**", inline=True)
    embed.add_field(name="Mesaj", value=f"**{_kisa_sayi(profil.get('message_count', 0))}**", inline=True)
    embed.add_field(name="Ses", value=f"**{_sureyi_formatla(int(profil.get('voice_seconds', 0)))}**", inline=True)
    embed.add_field(name="Warn", value=f"**{len(warnlar)}**", inline=True)
    embed.add_field(name="Tema", value=f"**{tema}**", inline=True)
    embed.add_field(name="Rozetler", value=_uye_rozet_metin(hedef.guild.id, hedef.id), inline=False)
    embed.add_field(name="Roller", value=_rol_listesi_kisa(hedef.roles), inline=False)
    embed.add_field(name="Hesap Acilis", value=_detayli_tarih(hedef.created_at), inline=True)
    embed.add_field(name="Sunucu Katilim", value=_detayli_tarih(hedef.joined_at), inline=True)
    embed.add_field(name="Durum", value="Timeout Var" if hedef.timed_out_until and hedef.timed_out_until > datetime.now(timezone.utc) else "Normal", inline=True)
    if hedef.display_avatar:
        embed.set_thumbnail(url=hedef.display_avatar.url)
    embed.set_footer(text=f"{hedef} | ID: {hedef.id}")
    return embed


@bot.command(name="profil", help="Detayli profil kartini gosterir.")
async def profil_detayli(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    await ctx.send(embed=_profil_embed_olustur(hedef))


@bot.command(name="seviye", aliases=["level", "rank"], help="Detayli seviye kartini gosterir.")
async def seviye_detayli(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    await ctx.send(embed=_profil_embed_olustur(hedef))


@bot.command(name="seviyetop", help="Sunucunun seviye siralamasini gosterir.")
async def seviyetop(ctx):
    tum_xp_veri = ayarlari_yukle().get(str(ctx.guild.id), {}).get("level_xp", {})
    siralama = sorted(
        tum_xp_veri.items(),
        key=lambda item: _toplam_xp_hesapla(int(item[1].get("level", 0)), int(item[1].get("xp", 0))),
        reverse=True,
    )
    satirlar = []
    for index, (uye_id, veri) in enumerate(siralama[:15], start=1):
        uye = ctx.guild.get_member(int(uye_id))
        if not uye:
            continue
        toplam_xp = _toplam_xp_hesapla(int(veri.get("level", 0)), int(veri.get("xp", 0)))
        profil = _profil_istat_al(ctx.guild.id, uye.id)
        satirlar.append(
            f"**#{index}** {uye.mention}\n"
            f"Level: **{int(veri.get('level', 0))}** | Toplam XP: **{_kisa_sayi(toplam_xp)}** | "
            f"Mesaj: **{_kisa_sayi(profil.get('message_count', 0))}**"
        )
    embed = discord.Embed(
        title="Seviye Top",
        description="\n\n".join(satirlar) or "Henuz level verisi yok.",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc),
    )
    embed.set_footer(text=f"Toplam kayitli uye: {len(tum_xp_veri)}")
    await ctx.send(embed=embed)


@bot.command(name="sunucupanel", help="Sunucunun detayli ozetini gosterir.")
async def sunucupanel_detayli(ctx):
    g = ctx.guild
    uyeler = [m for m in g.members if not m.bot]
    botlar = [m for m in g.members if m.bot]
    metin_kanal = len(g.text_channels)
    ses_kanal = len(g.voice_channels)
    kategori = len(g.categories)
    aktif_seste = sum(1 for m in uyeler if m.voice and m.voice.channel)
    embed = discord.Embed(
        title=f"{g.name} Sunucu Paneli",
        description="Sunucuya ait genel ozet ve canli istatistikler",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc),
    )
    embed.add_field(name="Uye Dagilimi", value=f"Toplam: **{g.member_count}**\nGercek: **{len(uyeler)}**\nBot: **{len(botlar)}**", inline=True)
    embed.add_field(name="Kanal Dagilimi", value=f"Metin: **{metin_kanal}**\nSes: **{ses_kanal}**\nKategori: **{kategori}**", inline=True)
    embed.add_field(name="Sunucu Bilgisi", value=f"Rol: **{len(g.roles)}**\nEmoji: **{len(g.emojis)}**\nBoost: **{g.premium_subscription_count or 0}**", inline=True)
    embed.add_field(name="Aktiflik", value=f"Seste Olan: **{aktif_seste}**\nOwner: {g.owner.mention if g.owner else 'Yok'}", inline=True)
    embed.add_field(name="Kurulus", value=_detayli_tarih(g.created_at), inline=True)
    embed.add_field(name="AFK Kanali", value=g.afk_channel.mention if g.afk_channel else "Yok", inline=True)
    if g.icon:
        embed.set_thumbnail(url=g.icon.url)
    embed.set_footer(text=f"Sunucu ID: {g.id}")
    await ctx.send(embed=embed)


@bot.command(name="yetkilipanel", help="Yetkililerin detayli ozetini gosterir.")
@commands.has_permissions(manage_guild=True)
async def yetkilipanel_detayli(ctx):
    ayarlar = ayarlari_yukle().get(str(ctx.guild.id), {})
    warnlar = ayarlar.get("uyarilar", {})
    partnerler = ayarlar.get("yetkili_partnerleri", {})
    satirlar = []
    for uye in ctx.guild.members:
        if uye.bot:
            continue
        perms = uye.guild_permissions
        if perms.administrator or perms.ban_members or perms.kick_members or perms.moderate_members or perms.manage_guild:
            profil = _profil_istat_al(ctx.guild.id, uye.id)
            satirlar.append(
                (
                    uye,
                    f"{uye.mention}\n"
                    f"Warn: **{len(warnlar.get(str(uye.id), []))}** | "
                    f"Partner: **{int(partnerler.get(str(uye.id), {}).get('sayi', 0))}** | "
                    f"Mesaj: **{_kisa_sayi(profil.get('message_count', 0))}** | "
                    f"Ses: **{_sureyi_formatla(int(profil.get('voice_seconds', 0)))}**"
                ),
            )
    satirlar.sort(key=lambda item: item[0].top_role.position, reverse=True)
    embed = discord.Embed(
        title="Yetkili Paneli",
        description="\n\n".join(metin for _, metin in satirlar[:12]) or "Yetkili bulunamadi.",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc),
    )
    embed.set_footer(text=f"Toplam yetkili: {len(satirlar)}")
    await ctx.send(embed=embed)


@bot.command(name="avatar", help="Kullanicinin buyuk avatarini gosterir.")
async def avatar_detayli(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    embed = discord.Embed(
        title=f"{hedef.display_name} Avatar",
        description=f"[Avatar linki]({hedef.display_avatar.url})",
        color=hedef.color if hedef.color.value else RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc),
    )
    embed.set_image(url=hedef.display_avatar.url)
    embed.set_footer(text=f"{hedef} | ID: {hedef.id}")
    await ctx.send(embed=embed)


@bot.command(name="banner", help="Kullanicinin bannerini gosterir.")
async def banner_detayli(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    try:
        kullanici = await bot.fetch_user(hedef.id)
    except Exception:
        kullanici = hedef
    banner = getattr(kullanici, "banner", None)
    if not banner:
        await ctx.send(embed=hata_embedi("Banner Yok", f"{hedef.mention} kullanicisinda banner bulunmuyor."))
        return
    embed = discord.Embed(
        title=f"{hedef.display_name} Banner",
        description=f"[Banner linki]({banner.url})",
        color=hedef.color if hedef.color.value else RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc),
    )
    embed.set_image(url=banner.url)
    embed.set_footer(text=f"{hedef} | ID: {hedef.id}")
    await ctx.send(embed=embed)


@bot.command(name="rolbilgi", help="Rol hakkinda detayli bilgi verir.")
async def rolbilgi_detayli(ctx, rol: discord.Role = None):
    if not rol:
        await ctx.send(embed=kullanim_embedi(".rolbilgi @rol"))
        return
    izinler = [ad.replace("_", " ").title() for ad, aktif in rol.permissions if aktif]
    embed = discord.Embed(
        title=f"Rol Bilgisi - {rol.name}",
        color=rol.color if rol.color.value else RENKLER["rol"],
        timestamp=datetime.now(timezone.utc),
    )
    embed.add_field(name="ID", value=f"`{rol.id}`", inline=True)
    embed.add_field(name="Pozisyon", value=str(rol.position), inline=True)
    embed.add_field(name="Uye Sayisi", value=str(len(rol.members)), inline=True)
    embed.add_field(name="Hex Renk", value=str(rol.color), inline=True)
    embed.add_field(name="Ayrica Goster", value="Evet" if rol.hoist else "Hayir", inline=True)
    embed.add_field(name="Etiketlenebilir", value="Evet" if rol.mentionable else "Hayir", inline=True)
    embed.add_field(name="Olusturulma", value=_detayli_tarih(rol.created_at), inline=False)
    embed.add_field(name="Izinler", value=", ".join(izinler[:20]) if izinler else "Ozel izin yok", inline=False)
    embed.add_field(name="Uyeler", value=_rol_listesi_kisa(rol.members, limit=10), inline=False)
    await ctx.send(embed=embed)


@bot.command(name="kanalbilgi", help="Kanal hakkinda detayli bilgi verir.")
async def kanalbilgi_detayli(ctx, kanal: discord.abc.GuildChannel = None):
    hedef = kanal or ctx.channel
    kategori = hedef.category.name if getattr(hedef, "category", None) else "Yok"
    embed = discord.Embed(
        title=f"Kanal Bilgisi - {hedef.name}",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc),
    )
    embed.add_field(name="ID", value=f"`{hedef.id}`", inline=True)
    embed.add_field(name="Tur", value=type(hedef).__name__.replace("Channel", ""), inline=True)
    embed.add_field(name="Kategori", value=kategori, inline=True)
    embed.add_field(name="Pozisyon", value=str(getattr(hedef, "position", "-")), inline=True)
    embed.add_field(name="NSFW", value="Evet" if getattr(hedef, "is_nsfw", lambda: False)() else "Hayir", inline=True)
    embed.add_field(name="Olusturulma", value=_detayli_tarih(hedef.created_at), inline=True)
    if isinstance(hedef, discord.TextChannel):
        embed.add_field(name="Yavas Mod", value=f"{hedef.slowmode_delay} sn", inline=True)
        embed.add_field(name="Konu", value=hedef.topic or "Yok", inline=False)
    if isinstance(hedef, discord.VoiceChannel):
        embed.add_field(name="Bitrate", value=str(hedef.bitrate), inline=True)
        embed.add_field(name="Limit", value=str(hedef.user_limit or 0), inline=True)
    await ctx.send(embed=embed)


@bot.command(name="kullanicibilgi", help="Kullanici hakkinda detayli bilgi verir.")
async def kullanicibilgi_detayli(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    profil = _profil_istat_al(ctx.guild.id, hedef.id)
    embed = discord.Embed(
        title=f"Kullanici Bilgisi - {hedef.display_name}",
        description=f"{hedef.mention} icin detayli uye bilgisi",
        color=hedef.color if hedef.color.value else RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc),
    )
    embed.add_field(name="Kullanici", value=f"{hedef} \n`{hedef.id}`", inline=False)
    embed.add_field(name="Takma Ad", value=hedef.nick or "Yok", inline=True)
    embed.add_field(name="En Ust Rol", value=hedef.top_role.mention if hedef.top_role else "Yok", inline=True)
    embed.add_field(name="Bot", value="Evet" if hedef.bot else "Hayir", inline=True)
    embed.add_field(name="Hesap Acilis", value=_detayli_tarih(hedef.created_at), inline=True)
    embed.add_field(name="Sunucu Katilim", value=_detayli_tarih(hedef.joined_at), inline=True)
    embed.add_field(name="Roller", value=str(max(0, len(hedef.roles) - 1)), inline=True)
    embed.add_field(name="Mesaj", value=_kisa_sayi(profil.get("message_count", 0)), inline=True)
    embed.add_field(name="Ses", value=_sureyi_formatla(int(profil.get("voice_seconds", 0))), inline=True)
    embed.add_field(name="Rozetler", value=_uye_rozet_metin(ctx.guild.id, hedef.id), inline=True)
    embed.add_field(name="Rol Listesi", value=_rol_listesi_kisa(hedef.roles), inline=False)
    if hedef.display_avatar:
        embed.set_thumbnail(url=hedef.display_avatar.url)
    embed.set_footer(text=f"Sunucu icin kayitli uye: {ctx.guild.member_count}")
    await ctx.send(embed=embed)


@bot.command(name="sesistatistik", help="En aktif ses kullanicilarini gosterir.")
async def sesistatistik_detayli(ctx):
    ayarlar = ayarlari_yukle().get(str(ctx.guild.id), {}).get("profil_istat", {})
    satirlar = []
    for index, (uye_id, veri) in enumerate(sorted(ayarlar.items(), key=lambda x: int(x[1].get("voice_seconds", 0)), reverse=True)[:15], start=1):
        uye = ctx.guild.get_member(int(uye_id))
        if uye:
            satirlar.append(f"**#{index}** {uye.mention} - **{_sureyi_formatla(int(veri.get('voice_seconds', 0)))}**")
    embed = discord.Embed(title="Ses Istatistikleri", description="\n".join(satirlar) or "Kayit yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    await ctx.send(embed=embed)


@bot.command(name="mesajistatistik", help="En cok mesaj atan kullanicilari gosterir.")
async def mesajistatistik_detayli(ctx):
    ayarlar = ayarlari_yukle().get(str(ctx.guild.id), {}).get("profil_istat", {})
    satirlar = []
    for index, (uye_id, veri) in enumerate(sorted(ayarlar.items(), key=lambda x: int(x[1].get("message_count", 0)), reverse=True)[:15], start=1):
        uye = ctx.guild.get_member(int(uye_id))
        if uye:
            satirlar.append(f"**#{index}** {uye.mention} - **{_kisa_sayi(int(veri.get('message_count', 0)))} mesaj**")
    embed = discord.Embed(title="Mesaj Istatistikleri", description="\n".join(satirlar) or "Kayit yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    await ctx.send(embed=embed)


@bot.command(name="leaderboard", help="Mesaj, ses ve level karmasi siralamayi gosterir.")
async def leaderboard_detayli(ctx):
    ayarlar = ayarlari_yukle().get(str(ctx.guild.id), {})
    tum_xp_veri = ayarlar.get("level_xp", {})
    profil_veri = ayarlar.get("profil_istat", {})
    puanlar = []
    for uye_id, xp_veri in tum_xp_veri.items():
        uye = ctx.guild.get_member(int(uye_id))
        if not uye:
            continue
        profil = _profil_istat_al(ctx.guild.id, int(uye_id))
        toplam_xp = _toplam_xp_hesapla(int(xp_veri.get("level", 0)), int(xp_veri.get("xp", 0)))
        puan = toplam_xp + int(profil.get("message_count", 0)) * 2 + int(profil.get("voice_seconds", 0) // 60)
        puanlar.append((uye, puan, xp_veri, profil))
    puanlar.sort(key=lambda item: item[1], reverse=True)
    satirlar = []
    for index, (uye, puan, xp_veri, profil) in enumerate(puanlar[:15], start=1):
        satirlar.append(
            f"**#{index}** {uye.mention}\n"
            f"Puan: **{_kisa_sayi(puan)}** | Level: **{int(xp_veri.get('level', 0))}** | "
            f"Mesaj: **{_kisa_sayi(profil.get('message_count', 0))}** | Ses: **{_sureyi_formatla(int(profil.get('voice_seconds', 0)))}**"
        )
    embed = discord.Embed(title="Genel Leaderboard", description="\n\n".join(satirlar) or "Kayit yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    await ctx.send(embed=embed)


@bot.command(name="say", help="Sunucu say bilgilerini detayli gosterir.")
async def say_detayli(ctx):
    g = ctx.guild
    insanlar = len([m for m in g.members if not m.bot])
    botlar = len([m for m in g.members if m.bot])
    cevrimici = len([m for m in g.members if m.status != discord.Status.offline])
    seste = len([m for m in g.members if m.voice and m.voice.channel])
    boostlu = g.premium_subscription_count or 0
    embed = discord.Embed(title="Sunucu Say Bilgisi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Toplam Uye", value=str(g.member_count), inline=True)
    embed.add_field(name="Gercek Uye", value=str(insanlar), inline=True)
    embed.add_field(name="Bot", value=str(botlar), inline=True)
    embed.add_field(name="Cevrimici", value=str(cevrimici), inline=True)
    embed.add_field(name="Seste", value=str(seste), inline=True)
    embed.add_field(name="Boost", value=str(boostlu), inline=True)
    await ctx.send(embed=embed)


try:
    bot.remove_command("ship")
except Exception:
    pass


async def _ship_avatar_gorseli_al(uye: discord.abc.User) -> Image.Image:
    def _indir():
        avatar_asset = uye.display_avatar
        try:
            avatar_asset = avatar_asset.with_size(256).with_format("png")
        except Exception:
            try:
                avatar_asset = avatar_asset.replace(size=256, format="png")
            except Exception:
                avatar_asset = uye.display_avatar
        with urllib.request.urlopen(avatar_asset.url, timeout=15) as resp:
            return resp.read()

    veri = await asyncio.to_thread(_indir)
    avatar = Image.open(io.BytesIO(veri)).convert("RGBA").resize((220, 220))
    maske = Image.new("L", (220, 220), 0)
    draw = ImageDraw.Draw(maske)
    draw.rounded_rectangle((0, 0, 219, 219), radius=28, fill=255)
    sonuc = ImageOps.fit(avatar, (220, 220), centering=(0.5, 0.5)).convert("RGBA")
    sonuc.putalpha(maske)
    return sonuc


def _ship_yuzde_hesapla(uye1_id: int, uye2_id: int, rastgele: bool = False) -> int:
    if rastgele:
        return _random.randint(1, 100)
    kucuk, buyuk = sorted([int(uye1_id), int(uye2_id)])
    tohum = f"{kucuk}:{buyuk}:{datetime.now(YEREL_SAAT_DILIMI).strftime('%Y-%m-%d')}"
    return (sum(ord(ch) for ch in tohum) % 81) + 20


def _ship_yorum(yuzde: int) -> str:
    if yuzde >= 98:
        return "En iyi ship, direkt nikah masasi."
    if yuzde >= 90:
        return "Asiri iyi, kalpler bosuna atmiyor."
    if yuzde >= 75:
        return "Fena degil, enerji baya tutuyor."
    if yuzde >= 55:
        return "Olur gibi, biraz daha zorlanir."
    if yuzde >= 35:
        return "Eh iste, biraz karisik."
    return "Kac, bu ship biraz fazla riskli."


async def _ship_kart_olustur(uye1: discord.Member, uye2: discord.Member, yuzde: int) -> io.BytesIO:
    avatar1 = await _ship_avatar_gorseli_al(uye1)
    avatar2 = await _ship_avatar_gorseli_al(uye2)

    tuval = Image.new("RGBA", (960, 420), (60, 8, 18, 255))
    draw = ImageDraw.Draw(tuval)
    font_buyuk = ImageFont.load_default()
    font_kucuk = ImageFont.load_default()

    for i in range(420):
        ton = int(50 + (i / 420) * 90)
        draw.line((0, i, 960, i), fill=(110 + ton, 8, 20 + ton // 4, 255))

    for x in range(40, 930, 70):
        draw.ellipse((x, 18, x + 12, 30), fill=(255, 210, 220, 140))
    draw.rounded_rectangle((24, 24, 936, 396), radius=32, outline=(255, 120, 140, 255), width=6, fill=(92, 6, 16, 230))
    draw.rounded_rectangle((70, 110, 310, 350), radius=28, outline=(255, 110, 110, 255), width=5, fill=(70, 10, 20, 255))
    draw.rounded_rectangle((650, 110, 890, 350), radius=28, outline=(255, 110, 110, 255), width=5, fill=(70, 10, 20, 255))
    draw.rounded_rectangle((405, 105, 555, 355), radius=30, outline=(255, 130, 130, 255), width=5, fill=(120, 15, 28, 255))
    draw.rounded_rectangle((426, 120, 534, 325), radius=18, outline=(255, 180, 190, 255), width=3, fill=(96, 10, 24, 255))

    tuval.alpha_composite(avatar1, (80, 120))
    tuval.alpha_composite(avatar2, (660, 120))

    isim1 = uye1.display_name[:16]
    isim2 = uye2.display_name[:16]
    draw.text((105, 70), isim1, fill=(255, 240, 240, 255), font=font_buyuk)
    draw.text((685, 70), isim2, fill=(255, 240, 240, 255), font=font_buyuk)

    kalp_dolum = int((190 * max(0, min(100, yuzde))) / 100)
    draw.rounded_rectangle((442, 320 - kalp_dolum, 518, 320), radius=14, fill=(255, 173, 181, 255))
    draw.rounded_rectangle((442, 130, 518, 320), radius=14, outline=(255, 205, 210, 255), width=3)
    draw.text((445, 286), f"{yuzde}%", fill=(255, 255, 255, 255), font=font_buyuk)
    draw.text((453, 72), "LOVE", fill=(255, 225, 225, 255), font=font_kucuk)

    for index in range(5):
        y = 124 + index * 40
        aktif = index < max(1, round(yuzde / 20))
        renk = (255, 90, 120, 255) if aktif else (255, 220, 220, 120)
        draw.ellipse((360, y, 376, y + 16), fill=renk)
        draw.ellipse((372, y, 388, y + 16), fill=renk)
        draw.polygon([(360, y + 8), (388, y + 8), (374, y + 28)], fill=renk)
        draw.ellipse((565, y, 581, y + 16), fill=renk)
        draw.ellipse((577, y, 593, y + 16), fill=renk)
        draw.polygon([(565, y + 8), (593, y + 8), (579, y + 28)], fill=renk)

    yorum = _ship_yorum(yuzde)
    draw.text((40, 30), "PREMIUM SHIP", fill=(255, 235, 235, 255), font=font_buyuk)
    draw.text((40, 378), yorum[:72], fill=(255, 230, 230, 255), font=font_kucuk)

    buffer = io.BytesIO()
    tuval.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


async def _ship_mesaji_gonder(hedef, uye1: discord.Member, uye2: discord.Member, yuzde: int, sahip_id: int):
    kart = await _ship_kart_olustur(uye1, uye2, yuzde)
    dosya = discord.File(fp=kart, filename="ship.png")
    embed = discord.Embed(
        title="Ship Sonucu",
        description=f"{uye1.mention} x {uye2.mention}\n**Uyum:** `{yuzde}%`\n{_ship_yorum(yuzde)}",
        color=RENKLER["uyari"],
        timestamp=datetime.now(timezone.utc),
    )
    embed.set_image(url="attachment://ship.png")
    embed.set_footer(text=zaman_damgasi())
    await hedef.send(embed=embed, file=dosya, view=ShipView(sahip_id, uye1.id, uye2.id))


class ShipView(discord.ui.View):
    def __init__(self, sahip_id: int, uye1_id: int, uye2_id: int):
        super().__init__(timeout=300)
        self.sahip_id = sahip_id
        self.uye1_id = uye1_id
        self.uye2_id = uye2_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.sahip_id:
            await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="Tekrar Shiple", style=discord.ButtonStyle.primary)
    async def reroll(self, interaction: discord.Interaction, button: discord.ui.Button):
        uye1 = interaction.guild.get_member(self.uye1_id) if interaction.guild else None
        uye2 = interaction.guild.get_member(self.uye2_id) if interaction.guild else None
        if not uye1 or not uye2:
            await interaction.response.send_message("Uyeler bulunamadi.", ephemeral=True)
            return
        await interaction.response.defer()
        yeni_yuzde = _ship_yuzde_hesapla(uye1.id, uye2.id, rastgele=True)
        kart = await _ship_kart_olustur(uye1, uye2, yeni_yuzde)
        dosya = discord.File(fp=kart, filename="ship.png")
        embed = discord.Embed(
            title="Ship Sonucu",
            description=f"{uye1.mention} x {uye2.mention}\n**Uyum:** `{yeni_yuzde}%`\n{_ship_yorum(yeni_yuzde)}",
            color=RENKLER["uyari"],
            timestamp=datetime.now(timezone.utc),
        )
        embed.set_image(url="attachment://ship.png")
        embed.set_footer(text=zaman_damgasi())
        await interaction.message.edit(embed=embed, attachments=[dosya], view=self)

    @discord.ui.button(label="Sil", style=discord.ButtonStyle.danger)
    async def sil(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        try:
            await interaction.message.delete()
        except Exception:
            pass


@bot.command(name="ship", help="Iki kisi icin resimli ship sonucu olusturur.")
async def ship(ctx, uye1: discord.Member = None, uye2: discord.Member = None):
    try:
        if not uye1 and not uye2:
            adaylar = [m for m in ctx.guild.members if not m.bot and m.id != ctx.author.id]
            if adaylar:
                uye1 = ctx.author
                uye2 = _random.choice(adaylar)
        if not uye1 and ctx.message.reference and isinstance(ctx.message.reference.resolved, discord.Message):
            hedef_yazar = ctx.message.reference.resolved.author
            if isinstance(hedef_yazar, discord.Member):
                uye1 = ctx.author
                uye2 = hedef_yazar
        if uye1 and not uye2:
            uye2 = ctx.author if uye1.id != ctx.author.id else None
        if not uye1 or not uye2:
            await ctx.send(embed=kullanim_embedi(".ship @uye1 @uye2"))
            return
        async with ctx.typing():
            yuzde = _ship_yuzde_hesapla(uye1.id, uye2.id)
            kart = await _ship_kart_olustur(uye1, uye2, yuzde)
        dosya = discord.File(fp=kart, filename="ship.png")
        embed = discord.Embed(
            title="Ship Sonucu",
            description=f"{uye1.mention} x {uye2.mention}\n**Uyum:** `{yuzde}%`\n{_ship_yorum(yuzde)}",
            color=RENKLER["uyari"],
            timestamp=datetime.now(timezone.utc),
        )
        embed.set_image(url="attachment://ship.png")
        embed.set_footer(text=zaman_damgasi())
        await ctx.send(embed=embed, file=dosya, view=ShipView(ctx.author.id, uye1.id, uye2.id))
    except Exception as e:
        print(f"[HATA] ship komutu: {e}")
        await ctx.send(embed=hata_embedi("Ship Hatasi", f"Ship karti olusturulurken hata oldu: `{e}`"))


if __name__ == "__main__":
    bot.run(BOT_TOKEN)
