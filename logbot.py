"""
Discord Log Botu - discord.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kanal ID'lerini kod içine yazmak gerekmez!
Tüm ayarlar Discord komutlarıyla yapılır ve
settings.json dosyasına otomatik kaydedilir.

Gereksinimler:
    pip install discord.py

Komutlar (Slash komutları):
    /log-kur <tür> <kanal>     → Belirli bir log türü için kanal atar
    /log-kaldır <tür>          → Belirli bir log türünü devre dışı bırakır
    /log-durum                 → Tüm log kanallarını listeler
    /log-sifirla               → Tüm ayarları siler
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
from threading import Thread, RLock
import time

# ─────────────────────────────────────────
#  AYARLAR
# ─────────────────────────────────────────

# Token environment variable'dan okunur
# Render: Dashboard → Environment → BOT_TOKEN ekle
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
# Bu surece ozel ID (loglarda / Mongo heartbeat — baska yerde calisan kopyayi ayirt etmek icin)
BOT_INSTANCE_ID = secrets.token_hex(8)
_ayar_dosya_kilidi = RLock()
_supabase_disabled_until = 0.0
_supabase_fail_count = 0
_ayar_cache_veri = None
_ayar_cache_zaman = 0.0
_AYAR_CACHE_TTL = float(os.environ.get("SETTINGS_CACHE_TTL", "8"))
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
    True  -> Bu süreç prefix komutunu çalıştırmalı (kilit alındı).
    False -> Başka bir süreç / bot aynı mesaj için kilidi zaten aldı.
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
            "Sunucuda iki ayri Discord BOT UYGULAMASI varsa her ikisi de cevap verir — fazla botu sunucudan at veya tek bot kullan."
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
    return supabase_aktif_mi() or _upstash_kilit_env_var_mi()


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
                            f"  ℹ️  Coklu-surec izleme: harici surec izleme pasif — baska yerde calisan kopyayi "
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
                        f"  ⚠️  {len(aktif)} AYRI SUREC (son ~2dk) — cift mesaj normal: "
                        f"{' | '.join(ozet)}"
                    )
                elif ilk_uyarni:
                    print(
                        f"  ✅ Coklu-surec izleme: Mongo'da son 2 dk icinde yalniz bu instance kayitli "
                        f"({BOT_INSTANCE_ID[:10]}..)"
                    )
                    ilk_uyarni = False
        except Exception as e:
            print(f"  [UYARI] Instance izleme dongusu: {e}")
        await asyncio.sleep(75)

# ─────────────────────────────────────────
#  SABİT LOG KANALLARI (deploy'dan etkilenmez)
#  Kod güncellendiğinde settings.json silinse bile
#  bu ID'ler otomatik olarak yeniden yüklenir.
# ─────────────────────────────────────────
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

# Partner kanalı ID'si (partner textinin atıldığı kanal)
# Değiştirmek istersen buraya yaz
DEFAULT_PARTNER_TEXT_KANALI = 1396219864279945397
DEFAULT_PARTNER_LOG_KANALI  = 1484813767253430363

# ── Sabit Log Kanalları ──────────────────────────────────────────
# Bu kanallar her deploy sonrası otomatik yüklenir.
# Değiştirmek istersen buradan düzenle.
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

# Desteklenen log türleri ve açıklamaları
LOG_TURLERI = {
    "ban_log":      "🔨 Ban / Unban logları",
    "mute_log":     "🔇 Mute logları",
    "mod_log":      "🛡️ Genel moderasyon logları",
    "rol_log":      "🎭 Rol değişiklik logları",
    "mesaj_log":    "✉️ Mesaj silme/düzenleme logları",
    "giris_cikis":  "🚪 Üye giriş/çıkış logları",
    "ses_log":      "🔊 Ses kanalı logları",
    "kanal_log":    "📁 Kanal oluşturma/silme logları",
    "davet_log":    "✉️ Davet logları",
}

# Otomatik log kurulumunda aranacak kanal adÄ± kalÄ±plarÄ±
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

# ─────────────────────────────────────────
#  AYAR YÖNETİMİ (settings.json)
# ─────────────────────────────────────────

def ayarlari_yukle() -> dict:
    """
    Önce Supabase'ten, yoksa yerel fallback dosyasından ayarları okur.
    Yapı: { "guild_id": { "log_turu": kanal_id, ... }, ... }
    Dosya yoksa boş dict döndürür.
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
    Varsayılan log kanallarını settings.json'a yazar.
    Her bot başlangıcında çağrılır — mevcut ayarların üzerine yazmaz,
    sadece eksik olanları tamamlar.
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
    """Tüm ayarları önce Supabase'e, o yoksa yerel dosyaya yazar."""
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
    Belirli bir sunucu ve log türü için kayıtlı kanal ID'sini döndürür.
    Kayıtlı değilse None döndürür.
    """
    ayarlar = ayarlari_yukle()
    return ayarlar.get(str(guild_id), {}).get(tur)


def kanal_kaydet(guild_id: int, tur: str, kanal_id: int):
    """Bir log türü için kanal ID'sini settings.json'a kaydeder."""
    with _ayar_dosya_kilidi:
        ayarlar = ayarlari_yukle()
        guild_key = str(guild_id)
        if guild_key not in ayarlar:
            ayarlar[guild_key] = {}
        ayarlar[guild_key][tur] = kanal_id
        ayarlari_kaydet(ayarlar)


def kanal_sil(guild_id: int, tur: str):
    """Bir log türünün kanal kaydını siler (devre dışı bırakır)."""
    with _ayar_dosya_kilidi:
        ayarlar = ayarlari_yukle()
        guild_key = str(guild_id)
        if guild_key in ayarlar and tur in ayarlar[guild_key]:
            del ayarlar[guild_key][tur]
            ayarlari_kaydet(ayarlar)


def guild_ayarlari_sil(guild_id: int):
    """Bir sunucunun tüm log ayarlarını tamamen siler."""
    with _ayar_dosya_kilidi:
        ayarlar = ayarlari_yukle()
        guild_key = str(guild_id)
        if guild_key in ayarlar:
            del ayarlar[guild_key]
            ayarlari_kaydet(ayarlar)


# ─────────────────────────────────────────
#  BOT KURULUMU
# ─────────────────────────────────────────

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
    """Aynı Discord mesajı için başka bir bot süreci prefix komutunu zaten işledi."""


@bot.check
async def prefix_komut_mesaj_kilidi(ctx: commands.Context):
    """Opsiyonel dagitik kilit: PREFIX_CMD_LOCK=1 (cift bot) — varsayilan kapali, hiz icin."""
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


# ─────────────────────────────────────────
#  YARDIMCI FONKSİYONLAR
# ─────────────────────────────────────────

async def log_gonder(guild: discord.Guild, tur: str, embed: discord.Embed):
    """
    settings.json'dan ilgili log kanalını bulup embed gönderir.
    Kanal ayarlanmamışsa veya bulunamazsa sessizce geçer.
    """
    kanal_id = kanal_al(guild.id, tur)
    if not kanal_id:
        return  # Bu log türü için kanal ayarlanmamış

    kanal = guild.get_channel(kanal_id)
    if not kanal:
        return  # Kanal daha sonra silinmiş olabilir

    try:
        await kanal.send(embed=embed)
    except discord.Forbidden:
        print(f"[HATA] '{tur}' kanalına yazma izni yok.")
    except discord.HTTPException as e:
        print(f"[HATA] Log gönderilemedi: {e}")


def utc_datetime_from_iso(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def zaman_damgasi() -> str:
    now = datetime.now(timezone.utc)
    return now.strftime("📅 %d.%m.%Y — ⏰ %H:%M:%S UTC")


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
        title="Komut Kullanımı",
        description=description,
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=zaman_damgasi())
    return embed


class TicketControlView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="ðŸ”’ Kapat", style=discord.ButtonStyle.danger, custom_id="ticket_kapat")
    async def kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message("âŒ Bu buton sadece ticket kanalÄ±nda kullanÄ±labilir.", ephemeral=True)
            return

        ayar = ticket_ayar_al(interaction.guild_id)
        log_id = ayar.get("log")
        await _ticket_kapat_logu_ve_transkript(channel, interaction.user, log_id)
        if False and log_id:
            log_kanali = interaction.guild.get_channel(log_id)
            if log_kanali:
                await log_kanali.send(embed=discord.Embed(
                    title="ðŸ”’ Ticket KapatÄ±ldÄ±",
                    description=f"**Ticket:** `{channel.name}`\n**Kapatan:** {interaction.user.mention}",
                    color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)
                ))

        await interaction.response.send_message("Ticket kapatÄ±lÄ±yor...", ephemeral=True)
        await channel.delete(reason=f"{interaction.user} tarafÄ±ndan kapatÄ±ldÄ±")

    @discord.ui.button(label="ðŸ‘¥ Ãœye Ekle", style=discord.ButtonStyle.secondary, custom_id="ticket_uyeekle")
    async def uye_ekle(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message("âŒ Bu buton sadece ticket kanalÄ±nda kullanÄ±labilir.", ephemeral=True)
            return

        await interaction.response.send_message("Eklemek istediÄŸin kullanÄ±cÄ±yÄ± bu kanalda etiketle: @kullanÄ±cÄ±", ephemeral=True)

        def check(message: discord.Message):
            return message.author == interaction.user and message.channel == channel and message.mentions

        try:
            yanit = await bot.wait_for("message", check=check, timeout=30)
            for uye in yanit.mentions:
                await channel.set_permissions(uye, read_messages=True, send_messages=True)
            await channel.send(f"âœ… {' '.join(u.mention for u in yanit.mentions)} ticketa eklendi.")
            await yanit.delete()
        except asyncio.TimeoutError:
            await channel.send("â³ KullanÄ±cÄ± ekleme isteÄŸinin sÃ¼resi doldu.", delete_after=5)

    @discord.ui.button(label="ðŸ“‹ Talep Al", style=discord.ButtonStyle.success, custom_id="ticket_talep")
    async def talep_al(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message("âŒ Bu buton sadece ticket kanalÄ±nda kullanÄ±labilir.", ephemeral=True)
            return

        ayar = ticket_ayar_al(interaction.guild_id)
        destek_rolu = interaction.guild.get_role(ayar.get("rol"))
        if destek_rolu and destek_rolu not in interaction.user.roles and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("âŒ Bu iÅŸlem iÃ§in destek rolÃ¼ gerekli.", ephemeral=True)
            return

        yeni_topic = channel.topic or ""
        if " | Talep:" in yeni_topic:
            yeni_topic = yeni_topic.split(" | Talep:")[0]
        await channel.edit(topic=f"{yeni_topic} | Talep: {interaction.user}")
        await interaction.response.send_message(f"âœ… Ticket {interaction.user.mention} tarafÄ±ndan talep alÄ±ndÄ±.")


class TicketOpenView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="ðŸŽ« Ticket AÃ§", style=discord.ButtonStyle.primary, custom_id="global_ticket_ac")
    async def ticket_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        ayar = ticket_ayar_al(interaction.guild_id)
        kategori = interaction.guild.get_channel(ayar.get("kategori"))
        destek_rolu = interaction.guild.get_role(ayar.get("rol"))
        log_id = ayar.get("log")

        if not kategori:
            await interaction.response.send_message("âŒ Kategori bulunamadÄ±. `.ticketkur` ile yeniden kur.", ephemeral=True)
            return

        for kanal in kategori.text_channels:
            if kanal.topic and str(interaction.user.id) in kanal.topic:
                await interaction.response.send_message(f"âŒ Zaten aÃ§Ä±k bir ticketÄ±n var: {kanal.mention}", ephemeral=True)
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
            title=f"ðŸŽ« Ticket #{sayi:04d}",
            description=(
                f"Merhaba {interaction.user.mention}!\n"
                f"Destek ekibimiz en kÄ±sa sÃ¼rede yardÄ±mcÄ± olacak.\n\n"
                f"TicketÄ± kapatmak iÃ§in ðŸ”’ butonunu kullan."
            ),
            color=0x57F287, timestamp=datetime.now(timezone.utc)
        )
        ac_embed.set_footer(text=f"Ticket #{sayi:04d} â€¢ {zaman_damgasi()}")

        await ticket_kanal.send(
            content=f"{interaction.user.mention}{(' ' + destek_rolu.mention) if destek_rolu else ''}",
            embed=ac_embed,
            view=TicketControlView()
        )
        await interaction.response.send_message(f"âœ… TicketÄ±n aÃ§Ä±ldÄ±: {ticket_kanal.mention}", ephemeral=True)

        if log_id:
            log_kanali = interaction.guild.get_channel(log_id)
            if log_kanali:
                await log_kanali.send(embed=discord.Embed(
                    title="ðŸŽ« Yeni Ticket AÃ§Ä±ldÄ±",
                    description=f"**AÃ§an:** {interaction.user.mention}\n**Kanal:** {ticket_kanal.mention}\n**Numara:** `#{sayi:04d}`",
                    color=RENKLER["giris"], timestamp=datetime.now(timezone.utc)
                ))


async def audit_log_bul(guild: discord.Guild, eylem: discord.AuditLogAction, hedef=None):
    """Audit log üzerinden en son işlemi yapan kişiyi bulur."""
    try:
        async for log in guild.audit_logs(limit=5, action=eylem):
            if hedef is None or log.target.id == hedef.id:
                return log.user
    except discord.Forbidden:
        pass
    return None


def izin_adi_getir(perm_adi: str) -> str:
    """İngilizce izin adını Türkçeye çevirir. Bilinmeyenler aynen döndürülür."""
    ceviriler = {
        "administrator":            "⚡ Yönetici",
        "manage_guild":             "🏠 Sunucuyu Yönet",
        "manage_roles":             "🎭 Rolleri Yönet",
        "manage_channels":          "📁 Kanalları Yönet",
        "manage_messages":          "✉️ Mesajları Yönet",
        "manage_nicknames":         "✏️ Takma Adları Yönet",
        "manage_webhooks":          "🔗 Webhook'ları Yönet",
        "manage_expressions":       "😄 İfadeleri Yönet",
        "manage_threads":           "🧵 Konuları Yönet",
        "kick_members":             "👢 Üye At",
        "ban_members":              "🔨 Üye Banla",
        "moderate_members":         "🔇 Üyeleri Sustur",
        "view_audit_log":           "📋 Denetim Günlüğünü Gör",
        "view_guild_insights":      "📊 Sunucu İçgörülerini Gör",
        "send_messages":            "💬 Mesaj Gönder",
        "send_tts_messages":        "🔊 TTS Mesajı Gönder",
        "embed_links":              "🔗 Link Önizlemesi",
        "attach_files":             "📎 Dosya Ekle",
        "read_message_history":     "📜 Mesaj Geçmişini Oku",
        "mention_everyone":         "📣 @everyone Etiketle",
        "use_external_emojis":      "😎 Harici Emoji Kullan",
        "use_external_stickers":    "🖼️ Harici Çıkartma Kullan",
        "add_reactions":            "👍 Tepki Ekle",
        "use_slash_commands":       "🤖 Slash Komutlarını Kullan",
        "connect":                  "🔌 Ses Kanalına Bağlan",
        "speak":                    "🎙️ Konuş",
        "stream":                   "📡 Yayın Yap",
        "use_voice_activation":     "🎤 Sesle Etkinleştir",
        "mute_members":             "🔇 Üyeleri Sustur (Ses)",
        "deafen_members":           "🔕 Üyeleri Sağırlaştır",
        "move_members":             "↔️ Üyeleri Taşı",
        "priority_speaker":         "🎖️ Öncelikli Konuşmacı",
        "create_instant_invite":    "✉️ Anında Davet Oluştur",
        "change_nickname":          "📝 Takma Ad Değiştir",
        "view_channel":             "👁️ Kanalı Gör",
        "request_to_speak":         "✋ Konuşma İsteği",
        "use_embedded_activities":  "🎮 Aktiviteleri Kullan",
        "send_messages_in_threads": "🧵 Konularda Mesaj Gönder",
        "create_public_threads":    "📢 Herkese Açık Konu Oluştur",
        "create_private_threads":   "🔒 Özel Konu Oluştur",
    }
    return ceviriler.get(perm_adi, f"🔧 {perm_adi.replace('_', ' ').title()}")


def izin_farklarini_bul(eski: discord.Permissions, yeni: discord.Permissions):
    """
    İki Permissions nesnesi arasındaki farkları hesaplar.

    Mantık:
        - Her izin True/False değeri taşır.
        - Eski ve yeni değerleri karşılaştırarak:
            * False → True  : izin EKLENDİ
            * True  → False : izin KALDIRILDI
        - Değişmeyenler atlanır.

    Döndürür:
        eklenenler   : list[str] — eklenen izinlerin Türkçe isimleri
        kaldirlanlar : list[str] — kaldırılan izinlerin Türkçe isimleri
    """
    eklenenler   = []
    kaldirlanlar = []

    # discord.Permissions.__iter__() → (izin_adı, bool) çiftleri döndürür
    eski_dict = dict(eski)
    yeni_dict = dict(yeni)

    for perm_adi in eski_dict:
        eski_deger = eski_dict[perm_adi]
        yeni_deger = yeni_dict.get(perm_adi, False)

        if eski_deger == yeni_deger:
            continue  # Değişiklik yok, atla

        ad = izin_adi_getir(perm_adi)

        if not eski_deger and yeni_deger:
            eklenenler.append(ad)       # False → True: eklendi
        elif eski_deger and not yeni_deger:
            kaldirlanlar.append(ad)     # True → False: kaldırıldı

    return eklenenler, kaldirlanlar


# ─────────────────────────────────────────
#  SLASH KOMUTLARI — LOG AYARLARI
# ─────────────────────────────────────────

# Slash komutlarında açılır menü için seçenek listesi
LOG_TUR_SECENEKLERI = [
    app_commands.Choice(name=aciklama, value=tur)
    for tur, aciklama in LOG_TURLERI.items()
]


@bot.tree.command(name="log-kur", description="Bir log türü için kanal atar")
@app_commands.describe(
    tur="Hangi log türü için kanal ayarlıyorsunuz?",
    kanal="Logların gönderileceği metin kanalı"
)
@app_commands.choices(tur=LOG_TUR_SECENEKLERI)
@app_commands.checks.has_permissions(manage_guild=True)
async def log_kur(
    interaction: discord.Interaction,
    tur: app_commands.Choice[str],
    kanal: discord.TextChannel
):
    """
    Belirli bir log türü için kanal atar ve settings.json'a kaydeder.
    Sadece 'Sunucuyu Yönet' iznine sahip kişiler kullanabilir.
    """

    # Bota kanalda yazma izni var mı?
    if not kanal.permissions_for(interaction.guild.me).send_messages:
        embed = discord.Embed(
            title="❌ Yetki Hatası",
            description=f"{kanal.mention} kanalına mesaj gönderemiyorum.\nKanal izinlerimi kontrol edin.",
            color=RENKLER["hata"]
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    # Ayarı kaydet
    kanal_kaydet(interaction.guild_id, tur.value, kanal.id)

    # ── Sana özel onay mesajı (sadece sen görürsün) ──
    onay_embed = discord.Embed(
        title="✅ Log Kanalı Ayarlandı",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    onay_embed.add_field(name="📋 Log Türü", value=tur.name,      inline=True)
    onay_embed.add_field(name="📍 Kanal",    value=kanal.mention, inline=True)
    onay_embed.set_footer(text=f"Ayarlayan: {interaction.user} • {zaman_damgasi()}")
    await interaction.response.send_message(embed=onay_embed, ephemeral=True)

    # ── Log kanalına bilgilendirme mesajı ─────────────
    kanal_embed = discord.Embed(
        title="🔔 Log Kanalı Aktif",
        description=f"Bu kanal **{tur.name}** için log kanalı olarak ayarlandı.\nArtık ilgili olaylar buraya düşecek.",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    kanal_embed.add_field(name="⚙️ Ayarlayan", value=interaction.user.mention, inline=True)
    kanal_embed.set_footer(text=zaman_damgasi())
    await kanal.send(embed=kanal_embed)


@bot.tree.command(name="log-kaldir", description="Bir log türünü devre dışı bırakır")
@app_commands.describe(tur="Devre dışı bırakılacak log türü")
@app_commands.choices(tur=LOG_TUR_SECENEKLERI)
@app_commands.checks.has_permissions(manage_guild=True)
async def log_kaldir(
    interaction: discord.Interaction,
    tur: app_commands.Choice[str]
):
    """Belirtilen log türünün kanal kaydını siler ve o logu durdurur."""

    mevcut = kanal_al(interaction.guild_id, tur.value)
    if not mevcut:
        embed = discord.Embed(
            title="⚠️ Zaten Devre Dışı",
            description=f"**{tur.name}** için zaten bir kanal ayarlanmamış.",
            color=RENKLER["bilgi"]
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    kanal_sil(interaction.guild_id, tur.value)

    embed = discord.Embed(
        title="🗑️ Log Kanalı Kaldırıldı",
        description=f"**{tur.name}** artık log göndermeyecek.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=f"Kaldıran: {interaction.user}")
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name="log-durum", description="Tüm log kanallarını ve durumlarını gösterir")
@app_commands.checks.has_permissions(manage_guild=True)
async def log_durum(interaction: discord.Interaction):
    """
    Bu sunucudaki tüm log türlerini ve atanmış kanallarını listeler.
    Kanal ayarlanmamışsa '🔴 Deaktif' olarak gösterilir.
    """
    ayarlar = ayarlari_yukle().get(str(interaction.guild_id), {})

    embed = discord.Embed(
        title="📋 Log Sistemi Durumu",
        description=f"**{interaction.guild.name}** sunucusundaki log ayarları",
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
            durum = kanal.mention if kanal else "⚠️ Kanal Silinmiş"
        else:
            durum = "🔴 Deaktif"

        satir = f"**{aciklama}**\n╰ {durum}"

        if tur in mod_turleri:
            mod_satirlar.append(satir)
        else:
            genel_satirlar.append(satir)

    if mod_satirlar:
        embed.add_field(
            name="🛡️ Moderasyon Logları",
            value="\n\n".join(mod_satirlar),
            inline=False
        )
    if genel_satirlar:
        embed.add_field(
            name="📁 Genel Loglar",
            value="\n\n".join(genel_satirlar),
            inline=False
        )

    aktif = len([t for t in LOG_TURLERI if t in ayarlar])
    embed.set_footer(text=f"{aktif}/{len(LOG_TURLERI)} log türü aktif • {zaman_damgasi()}")

    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name="log-sifirla", description="Bu sunucunun tüm log ayarlarını siler")
@app_commands.checks.has_permissions(administrator=True)
async def log_sifirla(interaction: discord.Interaction):
    """
    Onay butonlu mesaj göstererek tüm log ayarlarını sıfırlar.
    Sadece 'Yönetici' iznine sahip kişiler kullanabilir.
    """

    class OnayView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=30)

        @discord.ui.button(label="Evet, Sıfırla", style=discord.ButtonStyle.danger, emoji="⚠️")
        async def onayla(self, btn_i: discord.Interaction, button: discord.ui.Button):
            guild_ayarlari_sil(btn_i.guild_id)
            embed = discord.Embed(
                title="🗑️ Tüm Log Ayarları Silindi",
                description="Bu sunucuya ait tüm log kanalı kayıtları kaldırıldı.",
                color=RENKLER["hata"]
            )
            await btn_i.response.edit_message(embed=embed, view=None)

        @discord.ui.button(label="İptal", style=discord.ButtonStyle.secondary, emoji="✖️")
        async def iptal(self, btn_i: discord.Interaction, button: discord.ui.Button):
            embed = discord.Embed(
                title="✅ İptal Edildi",
                description="Sıfırlama işlemi iptal edildi, ayarlar korundu.",
                color=RENKLER["basari"]
            )
            await btn_i.response.edit_message(embed=embed, view=None)

    embed = discord.Embed(
        title="⚠️ Emin misiniz?",
        description="Bu işlem tüm log kanalı ayarlarını **kalıcı olarak** silecek.\nGeri alınamaz!",
        color=RENKLER["hata"]
    )
    await interaction.response.send_message(embed=embed, view=OnayView(), ephemeral=True)


# ─────────────────────────────────────────
#  KÜFÜR KORUMASI
# ─────────────────────────────────────────

class KufurKorumasıModal(discord.ui.Modal, title="Küfür Koruması Ayarları"):
    """Yasak kelimeleri yapılandırmak için modal."""
    
    yasakli_kelimeler = discord.ui.TextInput(
        label="Yasak Kelimeler (virgül ile ayırınız)",
        placeholder="örnek: kelime1, kelime2, kelime3",
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
                    title="❌ Hata",
                    description="Lütfen en az bir kelime girin.",
                    color=RENKLER["hata"]
                ),
                ephemeral=True
            )
            return
        
        # Kelimeleri virgül ile ayır ve temizle
        kelimeler = [k.strip().lower() for k in metin.split(",") if k.strip()]
        
        if not kelimeler:
            await interaction.response.send_message(
                embed=discord.Embed(
                    title="❌ Hata",
                    description="Lütfen geçerli kelimeler girin.",
                    color=RENKLER["hata"]
                ),
                ephemeral=True
            )
            return
        
        # Ayarlara kaydet
        kufur_kelimelerini_kaydet(interaction.guild_id, kelimeler)
        
        await interaction.response.send_message(
            embed=discord.Embed(
                title="✅ Küfür Koruması Ayarlandı",
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
    """Sunucuya ait yasak kelimeleri döndürür."""
    ayarlar = ayarlari_yukle()
    return ayarlar.get(str(guild_id), {}).get("yasakli_kelimeler", [])

def kufur_kontrol(guild_id: int, mesaj: str) -> bool:
    """Mesajda tam olarak yasaklı kelime var mı kontrol eder, noktalama işaretlerini göz ardı eder."""
    yasakli_kelimeler = kufur_kelimelerini_al(guild_id)
    if not yasakli_kelimeler:
        return False
    
    mesaj_temiz = mesaj.lower()
    # Kelimeleri ayırırken noktalama işaretlerini göz ardı et
    mesaj_kelimeleri = re.findall(r'\b\w+\b', mesaj_temiz)
    
    for kelime in mesaj_kelimeleri:
        if kelime in yasakli_kelimeler:
            return True
    return False


def mesajda_yasakli_kelime_var_mi(mesaj: str, yasakli_kelimeler: list[str]) -> bool:
    """
    Mesajda yasak kelime olup olmadığını kontrol eder.
    Kısmi eşleşmeleri de bulur (örnek: 'test' yazarken 'testt' de bulur).
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
    Modal açarak küfür koruması için yasak kelimeleri yapılandırır.
    Kelimeleri virgül ile ayırarak girin.
    """
    await ctx.send("Modal açmak için butona tıklayın:", view=KufurModalView())


@bot.command(name="kufur-durum")
@commands.has_permissions(manage_guild=True)
async def kufur_durum(ctx):
    """Şu anda tanımlı olan yasak kelimeleri ve sayılarını gösterir."""
    kelimeler = kufur_kelimelerini_al(ctx.guild.id)
    
    if not kelimeler:
        embed = discord.Embed(
            title="ℹ️ Küfür Koruması",
            description="Bu sunucuda henüz yasak kelime tanımlanmamış.\n`.kufur-kur` komutu ile ayarla!",
            color=RENKLER["bilgi"]
        )
    else:
        # Kelimeleri gruplara ayır (Discord mesaj limiti için)
        kelimeler_str = ", ".join(kelimeler[:50])  # İlk 50 göster
        if len(kelimeler) > 50:
            kelimeler_str += f", ... ve {len(kelimeler) - 50} kelime daha"
        
        embed = discord.Embed(
            title="🛡️ Küfür Koruması Aktif",
            description=f"**Toplam Yasak Kelime:** {len(kelimeler)}",
            color=RENKLER["basari"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(
            name="📋 Yasak Kelimeler",
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
    """Tüm yasak kelimeleri siler ve küfür korumasını kapatır."""
    
    if ctx.guild.id not in _kufur_kelimeler:
        await ctx.send("Bu sunucuda zaten küfür koruması ayarlanmamış.")
        return
    
    del _kufur_kelimeler[ctx.guild.id]
    kufur_kelimelerini_kaydet()
    
    embed = discord.Embed(
        title="🗑️ Küfür Koruması Temizlendi",
        description="Tüm yasak kelimeler silindi ve küfür koruması kapatıldı.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=f"İşlemi yapan: {ctx.author}")
    
    await ctx.send(embed=embed)


# Kufur Modal View
class KufurModalView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label="🛡️ Modal Aç", style=discord.ButtonStyle.primary)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = KufurKorumasıModal()
        await interaction.response.send_modal(modal)


@bot.command(name="blubpatlat")
@commands.has_permissions(ban_members=True)
async def blubpatlat(ctx):
    """Sunucudaki tüm üyeleri banlar."""
    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.send("Botun üyeleri banlama yetkisi yok!")
        return
    
    await ctx.send("Tüm üyeler banlanıyor... Bu işlem uzun sürebilir!")
    
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
        title="⚡ Blubpatlat Tamamlandı",
        color=0xFF6B6B,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="✅ Banlanan Üye", value=f"**{ban_sayisi}** kişi", inline=True)
    embed.add_field(name="❌ Banlanamayan", value=f"**{hata_sayisi}** kişi", inline=True)
    embed.add_field(name="👥 Toplam Üye", value=f"**{len(ctx.guild.members)}** kişi", inline=True)
    embed.set_footer(text=f"İşlemi yapan: {ctx.author}")
    
    await ctx.send(embed=embed)


@bot.command(name="blupblup")
@commands.has_permissions(manage_roles=True)
async def blupblup(ctx, yeni_isim: str):
    """İsminde 'blup' geçen herkesin ismini değiştirir."""
    if not ctx.guild.me.guild_permissions.manage_nicknames:
        await ctx.send("Botun isim değiştirme yetkisi yok!")
        return
    
    await ctx.send("İsimlerinde 'blup' aranıyor...")
    
    degistirilen = 0
    hata_sayisi = 0
    
    for member in ctx.guild.members:
        if member.bot:
            continue
        
        # Komutu yazanı hariç tut
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
        title="🔄 Blupblup İşlemi Tamamlandı",
        color=0x5865F2,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="✅ Değiştirilen Üye", value=f"**{degistirilen}** kişi", inline=True)
    embed.add_field(name="❌ Değiştirilemeyen", value=f"**{hata_sayisi}** kişi", inline=True)
    embed.add_field(name="👥 Toplam Üye", value=f"**{len(ctx.guild.members)}** kişi", inline=True)
    embed.add_field(name="📝 Yeni İsim", value=f"**{yeni_isim}**", inline=False)
    embed.add_field(name="📝 Not", value=f"**{ctx.author}** hariç tutuldu", inline=False)
    embed.set_footer(text=f"İşlemi yapan: {ctx.author}")
    
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
            title="❌ Yetersiz Yetki",
            description="Bu komutu kullanmak için **Sunucuyu Yönet** iznine ihtiyacınız var.",
            color=RENKLER["hata"]
        )
        await ctx.send(embed=embed)


# ─────────────────────────────────────────
#  OLAYLAR — MODERASYON LOGLARI
# ─────────────────────────────────────────

@bot.event
async def on_member_ban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_log_bul(guild, discord.AuditLogAction.ban, hedef=user)
    embed = discord.Embed(
        title="Üye Banlandı",
        description=f"{user.mention} sunucudan yasaklandı.",
        color=RENKLER["ban"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Kullanıcı", value=f"`{user}`", inline=True)
    embed.add_field(name="Kullanıcı ID", value=f"`{user.id}`", inline=True)
    embed.add_field(name="İşlemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(guild, "ban_log", embed)
    await _guvenlik_eylem_isle(guild, sorumlu, "ban", f"{user} ({user.id})", _guvenlik_ayar_al(guild.id).get("ban_limit", 3))


@bot.event
async def on_member_unban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_log_bul(guild, discord.AuditLogAction.unban, hedef=user)
    embed = discord.Embed(
        title="Ban Kaldırıldı",
        description=f"{user.mention} yeniden sunucuya katılabilir.",
        color=RENKLER["unban"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Kullanıcı", value=f"`{user}`", inline=True)
    embed.add_field(name="Kullanıcı ID", value=f"`{user.id}`", inline=True)
    embed.add_field(name="İşlemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(guild, "ban_log", embed)


@bot.event
async def on_member_join(member: discord.Member):
    embed = discord.Embed(title="🎉 Yeni Üye Katıldı", color=RENKLER["giris"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="👤 Kullanıcı",       value=f"{member.mention} `{member}`",         inline=True)
    embed.add_field(name="📅 Hesap Oluşturma", value=member.created_at.strftime("%d.%m.%Y"), inline=True)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(member.guild, "giris_cikis", embed)


@bot.event
async def on_member_remove(member: discord.Member):
    await asyncio.sleep(1)
    sorumlu = await audit_log_bul(member.guild, discord.AuditLogAction.kick, hedef=member)

    if sorumlu:
        embed = discord.Embed(
            title="Üye Atıldı",
            description=f"{member.mention} sunucudan atıldı.",
            color=RENKLER["mute"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="Kullanıcı", value=f"`{member}`", inline=True)
        embed.add_field(name="Kullanıcı ID", value=f"`{member.id}`", inline=True)
        embed.add_field(name="İşlemi Yapan", value=sorumlu.mention, inline=True)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(member.guild, "mod_log", embed)
        await _guvenlik_eylem_isle(member.guild, sorumlu, "kick", f"{member} ({member.id})", _guvenlik_ayar_al(member.guild.id).get("kick_limit", 3))
    else:
        embed = discord.Embed(
            title="Üye Ayrıldı",
            description=f"{member.mention} sunucudan ayrıldı.",
            color=RENKLER["cikis"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="Kullanıcı", value=f"`{member}`", inline=True)
        embed.add_field(name="Kullanıcı ID", value=f"`{member.id}`", inline=True)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(member.guild, "giris_cikis", embed)


# ─────────────────────────────────────────
#  OLAYLAR — ROL İZİN DEĞİŞİKLİĞİ LOGU
# ─────────────────────────────────────────

@bot.event
async def on_guild_role_update(onceki: discord.Role, sonraki: discord.Role):
    """
    Bir rol güncellendiğinde tetiklenir.

    İzin değişikliklerini tespit eder:
        1. izin_farklarini_bul() ile eklenen/kaldırılan izinleri hesaplar.
        2. Audit log'dan değişikliği yapan kişiyi bulur.
        3. Estetik bir embed oluşturup rol_log kanalına gönderir.
    """

    # ── 1. İzin farklarını hesapla ──────────────────────────
    eklenenler, kaldirlanlar = izin_farklarini_bul(onceki.permissions, sonraki.permissions)

    # İzin değişikliği yoksa diğer değişiklikleri kontrol et (isim, renk vb.)
    if not eklenenler and not kaldirlanlar:
        degisiklikler = []
        if onceki.name  != sonraki.name:  degisiklikler.append(f"📝 İsim: `{onceki.name}` → `{sonraki.name}`")
        if onceki.color != sonraki.color: degisiklikler.append(f"🎨 Renk: `{onceki.color}` → `{sonraki.color}`")
        if onceki.hoist != sonraki.hoist: degisiklikler.append(f"📌 Ayrı Göster: `{onceki.hoist}` → `{sonraki.hoist}`")

        if not degisiklikler:
            return  # Hiçbir değişiklik yok

        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.role_update, hedef=sonraki)
        embed = discord.Embed(
            title=f"🎭 Rol Güncellendi — {sonraki.name}",
            color=sonraki.color.value or RENKLER["rol"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="🔄 Değişiklikler",  value="\n".join(degisiklikler),                     inline=False)
        embed.add_field(name="🛡️ İşlemi Yapan",   value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "rol_log", embed)
        return

    # ── 2. Audit log'dan sorumluyu bul ──────────────────────
    await asyncio.sleep(0.5)  # Audit log'un güncellenmesi için kısa bekleme
    sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.role_update, hedef=sonraki)

    # ── 3. İzin değişikliği embedini oluştur ────────────────
    embed = discord.Embed(
        title=f"🔐 Rol İzinleri Değişti — {sonraki.name}",
        description=(
            f"**{sonraki.mention}** rolünün izinleri güncellendi.\n"
            f"**{len(eklenenler)}** izin eklendi · **{len(kaldirlanlar)}** izin kaldırıldı."
        ),
        color=RENKLER["izin"],
        timestamp=datetime.now(timezone.utc)
    )

    # Eklenen izinler (yeşil ✅)
    if eklenenler:
        embed.add_field(
            name="✅ Eklenen İzinler",
            value="\n".join(f"`+` {izin}" for izin in eklenenler),
            inline=True
        )

    # Kaldırılan izinler (kırmızı ❌)
    if kaldirlanlar:
        embed.add_field(
            name="❌ Kaldırılan İzinler",
            value="\n".join(f"`-` {izin}" for izin in kaldirlanlar),
            inline=True
        )

    # İki sütun varsa hizalama için boş alan
    if eklenenler and kaldirlanlar:
        embed.add_field(name="\u200b", value="\u200b", inline=True)

    # Toplam izin sayısı özeti
    eski_toplam = sum(1 for _, v in onceki.permissions if v)
    yeni_toplam = sum(1 for _, v in sonraki.permissions if v)
    fark = yeni_toplam - eski_toplam

    embed.add_field(
        name="📊 İzin Özeti",
        value=(
            f"Önceki: `{eski_toplam}` aktif\n"
            f"Şimdiki: `{yeni_toplam}` aktif\n"
            f"Fark: `{'+' if fark >= 0 else ''}{fark}`"
        ),
        inline=True
    )
    embed.add_field(name="🛡️ Yapan",  value=sorumlu.mention if sorumlu else "⚠️ Bilinmiyor", inline=True)
    embed.add_field(name="🆔 Rol ID", value=f"`{sonraki.id}`",                                inline=True)
    embed.set_footer(text=zaman_damgasi())

    await log_gonder(sonraki.guild, "rol_log", embed)


# ─────────────────────────────────────────
#  OLAYLAR — MESAJ LOGLARI
# ─────────────────────────────────────────

@bot.event
async def on_message_delete(message: discord.Message):
    if message.author.bot:
        return

    embed = discord.Embed(
        title="Mesaj Silindi",
        description="Bir mesaj kanaldan kaldırıldı.",
        color=RENKLER["mesaj"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Yazar", value=f"{message.author.mention} • `{message.author.id}`", inline=True)
    embed.add_field(name="Kanal", value=message.channel.mention, inline=True)
    embed.add_field(name="Mesaj ID", value=f"`{message.id}`", inline=True)
    embed.add_field(name="İçerik", value=message.content[:1024] or "*[Boş mesaj veya sadece medya]*", inline=False)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(message.guild, "mesaj_log", embed)


@bot.event
async def on_message_edit(onceki: discord.Message, sonraki: discord.Message):
    if onceki.author.bot or onceki.content == sonraki.content:
        return

    embed = discord.Embed(
        title="Mesaj Düzenlendi",
        description=f"[Mesaja git]({sonraki.jump_url})",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Yazar", value=f"{sonraki.author.mention} • `{sonraki.author.id}`", inline=True)
    embed.add_field(name="Kanal", value=sonraki.channel.mention, inline=True)
    embed.add_field(name="Mesaj ID", value=f"`{sonraki.id}`", inline=True)
    embed.add_field(name="Eski Mesaj", value=onceki.content[:512] or "—", inline=False)
    embed.add_field(name="Yeni Mesaj", value=sonraki.content[:512] or "—", inline=False)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(sonraki.guild, "mesaj_log", embed)


# ─────────────────────────────────────────
#  OLAYLAR — SES KANALI LOGLARI
# ─────────────────────────────────────────

@bot.event
async def on_voice_state_update(member: discord.Member, onceki: discord.VoiceState, sonraki: discord.VoiceState):
    if onceki.channel == sonraki.channel:
        return  # Mute/deafen gibi değişiklikleri loglama

    anahtar = (member.guild.id, member.id)
    simdi_ts = time.time()
    baslangic = _SES_OTURUMLARI.get(anahtar)
    if onceki.channel is not None and baslangic is not None:
        _profil_bekleyen_arttir(member.guild.id, member.id, ses_delta=max(0, int(simdi_ts - baslangic)))
        _SES_OTURUMLARI.pop(anahtar, None)
    if sonraki.channel is not None:
        _SES_OTURUMLARI[anahtar] = simdi_ts

    embed = discord.Embed(color=RENKLER["ses"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="👤 Üye", value=f"{member.mention} `{member}`", inline=False)

    if onceki.channel is None:
        embed.title = "🔊 Ses Kanalına Katıldı"
        embed.add_field(name="📍 Kanal", value=sonraki.channel.mention, inline=True)
    elif sonraki.channel is None:
        embed.title = "🔇 Ses Kanalından Ayrıldı"
        embed.add_field(name="📍 Kanal", value=onceki.channel.mention, inline=True)
    else:
        embed.title = "↔️ Ses Kanalı Değiştirildi"
        embed.add_field(name="⬅️ Önceki", value=onceki.channel.mention, inline=True)
        embed.add_field(name="➡️ Yeni",   value=sonraki.channel.mention, inline=True)

    embed.set_footer(text=zaman_damgasi())
    await log_gonder(member.guild, "ses_log", embed)


# ─────────────────────────────────────────
#  OLAYLAR — TIMEOUT (ZAMAN ASIMI) LOGU
# ─────────────────────────────────────────

@bot.event
async def on_member_update(onceki: discord.Member, sonraki: discord.Member):
    """
    Bu event hem rol değişikliklerini hem de timeout değişikliklerini yakalar.
    İkisini birden burada handle ediyoruz.

    NOT: Rol değişikliği için yukarıda ayrı bir on_member_update var,
    ama discord.py'de aynı event'i iki kez tanımlayamazsınız.
    Bu yüzden rol + timeout kontrolü tek fonksiyonda birleştirildi.
    Eğer önceki on_member_update varsa onu SİLİP bununla DEĞİŞTİRİN.
    """

    # ── Timeout (Zaman Aşımı) Kontrolü ──────────────────────
    # timed_out_until: None ise timeout yok, datetime ise aktif timeout
    eski_timeout = onceki.timed_out_until
    yeni_timeout = sonraki.timed_out_until

    if eski_timeout != yeni_timeout:
        await asyncio.sleep(0.5)
        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.member_update, hedef=sonraki)

        if yeni_timeout is not None:
            # Timeout uygulandı
            bitis = yeni_timeout.strftime("%d.%m.%Y %H:%M UTC")
            embed = discord.Embed(
                title="🔇 Zaman Aşımı Uygulandı (Timeout)",
                color=RENKLER["mute"],
                timestamp=datetime.now(timezone.utc)
            )
            embed.add_field(name="👤 Üye",            value=f"{sonraki.mention} `{sonraki}`",                inline=True)
            embed.add_field(name="🛡️ İşlemi Yapan",   value=sorumlu.mention if sorumlu else "⚠️ Bilinmiyor", inline=True)
            embed.add_field(name="⏰ Bitiş Zamanı",   value=f"`{bitis}`",                                    inline=False)
            embed.set_thumbnail(url=sonraki.display_avatar.url)
            embed.set_footer(text=zaman_damgasi())
            await log_gonder(sonraki.guild, "mute_log", embed)

        else:
            # Timeout kaldırıldı (erken veya süre doldu)
            embed = discord.Embed(
                title="🔊 Zaman Aşımı Kaldırıldı",
                color=RENKLER["unban"],
                timestamp=datetime.now(timezone.utc)
            )
            embed.add_field(name="👤 Üye",           value=f"{sonraki.mention} `{sonraki}`",                inline=True)
            embed.add_field(name="🛡️ İşlemi Yapan",  value=sorumlu.mention if sorumlu else "⚠️ Otomatik",  inline=True)
            embed.set_thumbnail(url=sonraki.display_avatar.url)
            embed.set_footer(text=zaman_damgasi())
            await log_gonder(sonraki.guild, "mute_log", embed)

    # ── Rol Değişikliği Kontrolü ─────────────────────────────
    eski_roller = set(onceki.roles)
    yeni_roller = set(sonraki.roles)

    eklenen_roller   = yeni_roller - eski_roller
    cikarilan_roller = eski_roller - yeni_roller

    if not eklenen_roller and not cikarilan_roller:
        return

    await asyncio.sleep(0.5)
    sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.member_role_update, hedef=sonraki)

    if eklenen_roller:
        embed = discord.Embed(title="🟢 Üyeye Rol Eklendi", color=RENKLER["giris"], timestamp=datetime.now(timezone.utc))
        embed.add_field(name="👤 Üye",           value=f"{sonraki.mention} `{sonraki}`",                inline=True)
        embed.add_field(name="🛡️ İşlemi Yapan",  value=sorumlu.mention if sorumlu else "⚠️ Bilinmiyor", inline=True)
        embed.add_field(
            name=f"➕ Eklenen Rol{'ler' if len(eklenen_roller) > 1 else ''}",
            value="\n".join(r.mention for r in eklenen_roller),
            inline=False
        )
        embed.set_thumbnail(url=sonraki.display_avatar.url)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "rol_log", embed)

    if cikarilan_roller:
        embed = discord.Embed(title="🔴 Üyeden Rol Çıkarıldı", color=RENKLER["cikis"], timestamp=datetime.now(timezone.utc))
        embed.add_field(name="👤 Üye",           value=f"{sonraki.mention} `{sonraki}`",                inline=True)
        embed.add_field(name="🛡️ İşlemi Yapan",  value=sorumlu.mention if sorumlu else "⚠️ Bilinmiyor", inline=True)
        embed.add_field(
            name=f"➖ Çıkarılan Rol{'ler' if len(cikarilan_roller) > 1 else ''}",
            value="\n".join(r.mention for r in cikarilan_roller),
            inline=False
        )
        embed.set_thumbnail(url=sonraki.display_avatar.url)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "rol_log", embed)


# ─────────────────────────────────────────
#  OLAYLAR — DAVETİYE LOGLARI
# ─────────────────────────────────────────

@bot.event
async def on_invite_create(invite: discord.Invite):
    """Yeni bir davet bağlantısı oluşturulduğunda tetiklenir."""
    embed = discord.Embed(
        title="Yeni Davet Oluşturuldu",
        description="Sunucuda yeni bir davet bağlantısı üretildi.",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Oluşturan", value=invite.inviter.mention if invite.inviter else "Bilinmiyor", inline=True)
    embed.add_field(name="Kanal", value=invite.channel.mention if invite.channel else "—", inline=True)
    embed.add_field(name="Davet Kodu", value=f"`{invite.code}`", inline=True)

    # Kullanım limiti: 0 = sınırsız
    kullanim = str(invite.max_uses) if invite.max_uses else "Sınırsız"
    embed.add_field(name="Kullanım Limiti", value=kullanim, inline=True)

    # Süre: 0 = hiç dolmaz
    if invite.max_age:
        sure = f"{invite.max_age // 3600} saat" if invite.max_age >= 3600 else f"{invite.max_age // 60} dakika"
    else:
        sure = "Süresiz"
    embed.add_field(name="Geçerlilik", value=sure, inline=True)
    embed.add_field(name="URL", value=f"discord.gg/{invite.code}", inline=True)

    embed.set_footer(text=zaman_damgasi())
    await log_gonder(invite.guild, "davet_log", embed)


@bot.event
async def on_invite_delete(invite: discord.Invite):
    """Bir davet bağlantısı silindiğinde tetiklenir."""
    embed = discord.Embed(
        title="Davet Silindi",
        description="Bir davet bağlantısı kaldırıldı.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Davet Kodu", value=f"`{invite.code}`", inline=True)
    embed.add_field(name="Kanal", value=invite.channel.mention if invite.channel else "—", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(invite.guild, "davet_log", embed)


# ─────────────────────────────────────────
#  OLAYLAR — KANAL LOGLARI
# ─────────────────────────────────────────

@bot.event
async def on_guild_channel_create(kanal: discord.abc.GuildChannel):
    """Yeni bir kanal oluşturulduğunda tetiklenir."""
    sorumlu = await audit_log_bul(kanal.guild, discord.AuditLogAction.channel_create, hedef=kanal)

    # Kanal türünü belirle
    tur_simge = {
        discord.TextChannel:     "💬 Metin Kanalı",
        discord.VoiceChannel:    "🔊 Ses Kanalı",
        discord.CategoryChannel: "📁 Kategori",
        discord.ForumChannel:    "📋 Forum Kanalı",
        discord.StageChannel:    "🎙️ Sahne Kanalı",
    }.get(type(kanal), "📌 Kanal")

    embed = discord.Embed(
        title="Kanal Oluşturuldu",
        description=f"Yeni bir kanal açıldı: **{kanal.name}**",
        color=RENKLER["giris"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Kanal", value=kanal.mention if hasattr(kanal, "mention") else f"`{kanal.name}`", inline=True)
    embed.add_field(name="Tür", value=tur_simge, inline=True)
    embed.add_field(name="İşlemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.add_field(name="Kanal ID", value=f"`{kanal.id}`", inline=True)

    # Kategorisi varsa göster
    if hasattr(kanal, "category") and kanal.category:
        embed.add_field(name="Kategori", value=kanal.category.name, inline=True)

    embed.set_footer(text=zaman_damgasi())
    await log_gonder(kanal.guild, "kanal_log", embed)
    await _guvenlik_eylem_isle(kanal.guild, sorumlu, "kanal_acma", f"{kanal.name} ({kanal.id})", _guvenlik_ayar_al(kanal.guild.id).get("kanal_limit", 3))


@bot.event
async def on_guild_channel_delete(kanal: discord.abc.GuildChannel):
    """Bir kanal silindiğinde tetiklenir."""
    sorumlu = await audit_log_bul(kanal.guild, discord.AuditLogAction.channel_delete, hedef=kanal)

    tur_simge = {
        discord.TextChannel:     "💬 Metin Kanalı",
        discord.VoiceChannel:    "🔊 Ses Kanalı",
        discord.CategoryChannel: "📁 Kategori",
        discord.ForumChannel:    "📋 Forum Kanalı",
        discord.StageChannel:    "🎙️ Sahne Kanalı",
    }.get(type(kanal), "📌 Kanal")

    embed = discord.Embed(
        title="Kanal Silindi",
        description=f"Bir kanal kaldırıldı: **{kanal.name}**",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Kanal", value=f"`{kanal.name}`", inline=True)
    embed.add_field(name="Tür", value=tur_simge, inline=True)
    embed.add_field(name="İşlemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
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
        title="Rol Oluşturuldu",
        description=f"Yeni rol: {rol.mention}",
        color=RENKLER["giris"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Rol", value=rol.mention, inline=True)
    embed.add_field(name="ID", value=f"`{rol.id}`", inline=True)
    embed.add_field(name="İşlemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.add_field(name="Renk", value=str(rol.color), inline=True)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(rol.guild, "rol_log", embed)
    await _guvenlik_eylem_isle(rol.guild, sorumlu, "rol_acma", f"{rol.name} ({rol.id})", _guvenlik_ayar_al(rol.guild.id).get("rol_ac_limit", 3))


@bot.event
async def on_guild_role_delete(rol: discord.Role):
    sorumlu = await audit_log_bul(rol.guild, discord.AuditLogAction.role_delete, hedef=rol)

    embed = discord.Embed(
        title="Rol Silindi",
        description=f"Kaldırılan rol: **{rol.name}**",
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
    İki kanal arasındaki izin (overwrite) farklarını bulur.

    Kanal izinleri rol/üye bazlı OverwriteType nesneleridir.
    Her overwrite'ın allow ve deny listeleri karşılaştırılır:
        - Yeni eklenmiş overwrite  → o rol/üye için yeni izin ayarı yapılmış
        - Silinmiş overwrite       → o rol/üye için izin ayarı kaldırılmış
        - Değişmiş overwrite       → allow/deny değerleri farklılaşmış

    Döndürür:
        list[str] — okunabilir değişiklik satırları
    """
    satirlar = []

    eski_ow = dict(onceki.overwrites)   # {rol/üye: PermissionOverwrite}
    yeni_ow = dict(sonraki.overwrites)

    tum_hedefler = set(eski_ow) | set(yeni_ow)

    for hedef in tum_hedefler:
        eski = eski_ow.get(hedef)
        yeni = yeni_ow.get(hedef)

        hedef_adi = f"@{hedef.name}" if hasattr(hedef, 'name') else str(hedef)

        if eski is None and yeni is not None:
            # Yeni overwrite eklendi
            izinler = [izin_adi_getir(p) for p, v in iter(yeni) if v is not None]
            satirlar.append(f"➕ **{hedef_adi}** için izin ayarı eklendi")

        elif eski is not None and yeni is None:
            # Overwrite tamamen silindi
            satirlar.append(f"➖ **{hedef_adi}** için izin ayarı kaldırıldı")

        else:
            # Her iki tarafta da var, farkları bul
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
                    eklenen_izinler.append(ad)       # ✅ İzin verildi
                elif yeni_deger is False and eski_deger is not False:
                    reddedilen_izinler.append(ad)    # ❌ İzin reddedildi
                elif yeni_deger is None:
                    if eski_deger is True:
                        kaldirilan_izinler.append(ad)   # ✅ kaldırıldı → nötr
                    elif eski_deger is False:
                        red_kaldirilan.append(ad)       # ❌ kaldırıldı → nötr

            if any([eklenen_izinler, kaldirilan_izinler, reddedilen_izinler, red_kaldirilan]):
                satirlar.append(f"🔧 **{hedef_adi}** izinleri değişti:")
                if eklenen_izinler:
                    satirlar.append("  `✅` " + ", ".join(eklenen_izinler))
                if reddedilen_izinler:
                    satirlar.append("  `❌` " + ", ".join(reddedilen_izinler))
                if kaldirilan_izinler:
                    satirlar.append("  `↩️` Nötre alındı: " + ", ".join(kaldirilan_izinler))
                if red_kaldirilan:
                    satirlar.append("  `↩️` Red kaldırıldı: " + ", ".join(red_kaldirilan))

    return satirlar


@bot.event
async def on_guild_channel_update(onceki: discord.abc.GuildChannel, sonraki: discord.abc.GuildChannel):
    """
    Bir kanalın adı, ayarları veya izinleri değiştiğinde tetiklenir.
    Genel değişiklikler ve izin (overwrite) değişiklikleri ayrı embedler olarak gönderilir.
    """

    # ── 1. Genel ayar değişiklikleri ────────────────────────
    degisiklikler = []

    if onceki.name != sonraki.name:
        degisiklikler.append(f"📝 İsim: `{onceki.name}` → `{sonraki.name}`")

    if isinstance(onceki, discord.TextChannel) and isinstance(sonraki, discord.TextChannel):
        if onceki.topic != sonraki.topic:
            eski = onceki.topic or "*(boş)*"
            yeni = sonraki.topic or "*(boş)*"
            degisiklikler.append(f"📋 Konu: `{eski}` → `{yeni}`")
        if onceki.slowmode_delay != sonraki.slowmode_delay:
            degisiklikler.append(f"🐢 Yavaş Mod: `{onceki.slowmode_delay}sn` → `{sonraki.slowmode_delay}sn`")
        if onceki.nsfw != sonraki.nsfw:
            degisiklikler.append(f"🔞 NSFW: `{onceki.nsfw}` → `{sonraki.nsfw}`")

    if degisiklikler:
        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.channel_update, hedef=sonraki)
        embed = discord.Embed(
            title="✏️ Kanal Güncellendi",
            color=RENKLER["bilgi"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="📍 Kanal",         value=sonraki.mention,                                        inline=True)
        embed.add_field(name="🛡️ İşlemi Yapan",  value=sorumlu.mention if sorumlu else "⚠️ Bilinmiyor",        inline=True)
        embed.add_field(name="🔄 Değişiklikler", value="\n".join(degisiklikler),                                inline=False)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "kanal_log", embed)

    # ── 2. İzin (overwrite) değişiklikleri ──────────────────
    izin_satirlari = kanal_izin_farklarini_bul(onceki, sonraki)

    if izin_satirlari:
        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.overwrite_update, hedef=sonraki)

        # Discord embed field değeri max 1024 karakter, uzunsa böl
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
            title="🔐 Kanal İzinleri Değişti",
            color=RENKLER["izin"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="📍 Kanal",        value=sonraki.mention,                                        inline=True)
        embed.add_field(name="🛡️ İşlemi Yapan", value=sorumlu.mention if sorumlu else "⚠️ Bilinmiyor",        inline=True)

        for i, parca in enumerate(parcalar):
            embed.add_field(
                name="🔄 Değişiklikler" if i == 0 else "\u200b",
                value=parca,
                inline=False
            )

        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "kanal_log", embed)


# ─────────────────────────────────────────
#  BOT HAZIR OLAYI
# ─────────────────────────────────────────


@bot.event
async def on_command_error(ctx, error):
    """CommandNotFound ve diğer bilinen hataları sessizce geçer."""
    if isinstance(error, commands.CommandNotFound):
        return  # Bilinmeyen komutları yoksay
    if isinstance(error, PrefixMesajCiftKopya):
        return  # Çift bot süreci: ikinci kopya sessizce yoksayılır
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=hata_embedi("Yetki Hatası", "Bu komutu kullanmak için gerekli yetkiye sahip değilsin."))
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("Üye Bulunamadı", "Belirttiğin üye bulunamadı veya sunucuda değil."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("Eksik parametre girdin. Detaylı komut listesi için `.yardım` kullanabilirsin."))


@bot.event
async def on_ready():
    # Slash komutlarını Discord'a senkronize et
    try:
        synced = await bot.tree.sync()
        print(f"  ✅ {len(synced)} slash komutu senkronize edildi.")
    except Exception as e:
        print(f"  ❌ Komut senkronizasyonu başarısız: {e}")

    # ── Sabit log kanallarını settings.json'a yükle ──────────
    # Her bot başladığında DEFAULT_LOG_KANALLARI settings.json'a yazılır.
    # Böylece deploy sonrası settings.json silinse bile kanallar kaybolmaz.
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
    print("  ✅ Kanallar yüklendi.")

    print("━" * 52)
    print(f"  🤖 Bot    : {bot.user} ({bot.user.id})")
    print(f"  🖥️  Surec  : {' | '.join(_bot_surec_log_satirlari())}")
    print(f"  📡 Sunucu : {len(bot.guilds)} adet")
    print(f"  ⚙️  Ayarlar: Supabase={'acik' if supabase_aktif_mi() else 'kapali'} | DosyaFallback={AYAR_DOSYASI}")
    print("━" * 52)
    print("  Kullanılabilir slash komutları:")
    print("    /log-kur <tür> <kanal>  → Kanal ata")
    print("    /log-kaldir <tür>       → Logu kapat")
    print("    /log-durum              → Durumu gör")
    print("    /log-sifirla            → Tümünü sil")
    print("━" * 52)

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="sunucu loglarını 👁️"
        )
    )

    if not getattr(bot, "_coklu_surec_izleme_baslatildi", False):
        bot._coklu_surec_izleme_baslatildi = True
        asyncio.create_task(_bot_coklu_surec_izleme_dongusu())
    if not getattr(bot, "_profil_kaydetme_dongusu_baslatildi", False):
        bot._profil_kaydetme_dongusu_baslatildi = True
        asyncio.create_task(_profil_bekleyenleri_kaydet_dongusu())


# ═══════════════════════════════════════════════════════════════
#  PARTNER SİSTEMİ
# ═══════════════════════════════════════════════════════════════
#
#  Veri yapısı (settings.json içinde):
#  {
#    "guild_id": {
#      "partner_log": kanal_id,          ← partner log kanalı
#      "partners": {
#        "hedef_guild_id": {
#          "guild_name": "Sunucu Adı",
#          "guild_id": 123,
#          "yapan": "kullanici#0000",
#          "yapan_id": 123,
#          "zaman": "2026-03-20T16:00:00",  ← ISO format
#          "son_partner": "2026-03-20T16:00:00"
#        }
#      }
#    }
#  }
# ───────────────────────────────────────────────────────────────

PARTNER_BEKLEME_SURESI = 3600  # saniye (1 saat)


def partner_verisi_al(guild_id: int) -> dict:
    """Bu sunucunun partner verisini döndürür."""
    ayarlar = ayarlari_yukle()
    return ayarlar.get(str(guild_id), {}).get("partners", {})


def partner_gecmisi_al(guild_id: int) -> list[dict]:
    """Bu sunucunun partner işlem geçmişini döndürür."""
    ayarlar = ayarlari_yukle()
    gecmis = ayarlar.get(str(guild_id), {}).get("partner_gecmisi", [])
    return gecmis if isinstance(gecmis, list) else []


def partner_kaydet_db(guild_id: int, hedef_guild_id: int, veri: dict):
    """Bir partner kaydını settings.json'a yazar."""
    def _guncelle(ayarlar):
        guild_key = str(guild_id)
        if guild_key not in ayarlar:
            ayarlar[guild_key] = {}
        if "partners" not in ayarlar[guild_key]:
            ayarlar[guild_key]["partners"] = {}
        ayarlar[guild_key]["partners"][str(hedef_guild_id)] = veri

    ayarlari_guncelle(_guncelle)


def partner_gecmisi_ekle(guild_id: int, veri: dict):
    """Partner işlemini geçmiş listesine ekler."""
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
    """Partner log kanalını kaydeder."""
    def _guncelle(ayarlar):
        guild_key = str(guild_id)
        if guild_key not in ayarlar:
            ayarlar[guild_key] = {}
        ayarlar[guild_key]["partner_log"] = kanal_id

    ayarlari_guncelle(_guncelle)


def partner_log_kanali_al(guild_id: int):
    """Partner log kanalı ID'sini döndürür. Settings yoksa sabit değeri kullanır."""
    kayitli = ayarlari_yukle().get(str(guild_id), {}).get("partner_log")
    return kayitli if kayitli else DEFAULT_PARTNER_LOG_KANALI


def partner_istatistik_hesapla(guild_id: int) -> dict:
    """
    Günlük, haftalık, aylık ve toplam partner sayısını hesaplar.

    Mantık:
        - Her partner kaydındaki 'zaman' alanı ISO format datetime'dır.
        - Şu anki zamandan farkı hesaplayarak hangi periyoda girdiğini belirleriz.
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
    Bu sunucunun toplam partner sayısına göre sıralamasını döndürür.
    Tüm sunucuların toplam partner sayılarını karşılaştırır.
    """
    ayarlar = ayarlari_yukle()
    sayilar = []

    for gid, veri in ayarlar.items():
        if "partners" in veri:
            sayilar.append((gid, len(veri["partners"])))

    # Büyükten küçüğe sırala
    sayilar.sort(key=lambda x: x[1], reverse=True)

    for i, (gid, _) in enumerate(sayilar, 1):
        if gid == str(guild_id):
            return i
    return 1




# ── Partner Slash Komutları & Mesaj Kontrolü ─────────────────────

def partner_kanal_id_al(guild_id: int):
    """Partner text kanalı ID'sini döndürür. Settings yoksa sabit değeri kullanır."""
    kayitli = ayarlari_yukle().get(str(guild_id), {}).get("partner_kanal")
    return kayitli if kayitli else DEFAULT_PARTNER_TEXT_KANALI

def partner_log_kanali_al_v2(guild_id: int):
    """Partner log kanalı ID'sini döndürür. Settings yoksa sabit değeri kullanır."""
    kayitli = ayarlari_yukle().get(str(guild_id), {}).get("partner_log")
    return kayitli if kayitli else DEFAULT_PARTNER_LOG_KANALI

def partner_kanal_id_kaydet(guild_id: int, kanal_id: int):
    """Partner text kanalını kaydeder."""
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        ayarlar[gk]["partner_kanal"] = kanal_id

    ayarlari_guncelle(_guncelle)

def yetkili_partner_sayisi_guncelle(guild_id: int, yetkili_id: int, yetkili_adi: str):
    """
    Yetkili bazlı partner sayacını günceller.
    Her partnerlik yapıldığında ilgili yetkilinin sayısını 1 artırır.
    Yapı: ayarlar[guild_id]["yetkili_partnerleri"][yetkili_id] = {"ad": ..., "sayi": ...}
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
    Yetkilileri partner sayısına göre büyükten küçüğe sıralar.
    Döndürür: [{"id": ..., "ad": ..., "sayi": ...}, ...]
    """
    ayarlar = ayarlari_yukle()
    veri = ayarlar.get(str(guild_id), {}).get("yetkili_partnerleri", {})
    liste = [{"id": kid, "ad": v["ad"], "sayi": v["sayi"]} for kid, v in veri.items()]
    liste.sort(key=lambda x: x["sayi"], reverse=True)
    return liste


# ── Partner Prefix Komutları ─────────────────────────────────────

@bot.command(name="partner-kur")
@commands.has_permissions(manage_guild=True)
async def partner_kur(ctx, text_kanal: discord.TextChannel = None, log_kanal: discord.TextChannel = None):
    """
    .partner-kur #text-kanal #log-kanal
    Partner text ve log kanallarını ayarlar.
    """
    if not text_kanal or not log_kanal:
        await ctx.send(embed=kullanim_embedi("`.partner-kur #text-kanal #log-kanal`"))
        return

    partner_kanal_id_kaydet(ctx.guild.id, text_kanal.id)
    partner_log_kanali_kaydet(ctx.guild.id, log_kanal.id)

    embed = discord.Embed(title="✅ Partner Kanalları Ayarlandı", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="📢 Partner Text", value=text_kanal.mention, inline=True)
    embed.add_field(name="📋 Partner Log",  value=log_kanal.mention,  inline=True)
    embed.set_footer(text=f"Ayarlayan: {ctx.author}")
    await ctx.send(embed=embed)
    await text_kanal.send(embed=discord.Embed(
        title="🤝 Partner Kanalı Aktif",
        description="Bu kanal partner text kanalı olarak ayarlandı.\nDavet linki içermeyen mesajlar otomatik silinecek.",
        color=RENKLER["basari"]
    ))
    await log_kanal.send(embed=discord.Embed(
        title="📋 Partner Log Kanalı Aktif",
        description="Partner logları bu kanala gönderilecek.",
        color=RENKLER["basari"]
    ))


@bot.command(name="partner-kapat", aliases=["partner-off", "partnerkapat"])
@commands.has_permissions(manage_guild=True)
async def partner_kapat(ctx):
    """.partner-kapat — Partner sisteminin kanal ayarlarini kapatir."""
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
    """.partner-istatistik — Sunucunun partner istatistiklerini gösterir."""
    stats = partner_istatistik_hesapla(ctx.guild.id)
    sira  = partner_sira_bul(ctx.guild.id)

    embed = discord.Embed(
        title="📊 Partner İstatistikleri",
        description=f"**{ctx.guild.name}** sunucusunun partner verileri",
        color=0x57F287,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="📊 Sıralaman", value=f"**#{sira}**", inline=False)
    embed.add_field(
        name="🕐 Zamana Dayalı:",
        value=(
            f"› Günlük: **{stats['gunluk']}**\n"
            f"› Haftalık: **{stats['haftalik']}**\n"
            f"› Aylık: **{stats['aylik']}**"
        ),
        inline=True
    )
    embed.add_field(name="• Toplam", value=f"**{stats['toplam']}**", inline=True)
    embed.set_footer(text=f"{ctx.bot.user.name} • Partner Sistemi • {zaman_damgasi()}")
    await ctx.send(embed=embed)


@bot.command(name="partner-top", aliases=["p-top", "ptop"])
@commands.has_permissions(manage_guild=True)
async def partner_top(ctx):
    """.partner-top — Yetkililerin partner sıralamasını gösterir."""
    sıralama = yetkili_siralamasi_al(ctx.guild.id)

    if not sıralama:
        await ctx.send(embed=discord.Embed(
            title="📋 Partner Sıralaması",
            description="Henüz hiç partnerlik kaydı yok.",
            color=RENKLER["bilgi"]
        ))
        return

    madalyalar = ["🥇", "🥈", "🥉"]
    satirlar = []
    for i, yetkili in enumerate(sıralama[:20], 1):
        madalya = madalyalar[i-1] if i <= 3 else f"`{i}.`"
        satirlar.append(f"{madalya} <@{yetkili['id']}> — **{yetkili['sayi']}** partnerlik")

    embed = discord.Embed(
        title="🏆 Partner Sıralaması",
        description="\n".join(satirlar),
        color=0xF1C40F,
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=f"Toplam {len(sıralama)} yetkili • {zaman_damgasi()}")
    await ctx.send(embed=embed)


@bot.command(name="partner-liste", aliases=["p-liste", "pliste"])
@commands.has_permissions(manage_guild=True)
async def partner_liste(ctx):
    """.partner-liste — Tüm partner sunucularını listeler."""
    partners = partner_verisi_al(ctx.guild.id)
    if not partners:
        await ctx.send(embed=discord.Embed(
            title="📋 Partner Listesi",
            description="Henüz hiç partner kaydı yok.",
            color=RENKLER["bilgi"]
        ))
        return

    satirlar = []
    for i, (gid, p) in enumerate(partners.items(), 1):
        try:
            zaman = datetime.fromisoformat(p["zaman"]).strftime("%d.%m.%Y")
        except Exception:
            zaman = "—"
        satirlar.append(f"`{i}.` **{p['guild_name']}** — {zaman} — <@{p['yapan_id']}>")

    # Sayfalama — her sayfada 10 partner
    sayfalar = [satirlar[i:i+10] for i in range(0, len(satirlar), 10)]

    class SayfaView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=60)
            self.sayfa = 0

        def embed_olustur(self):
            e = discord.Embed(
                title=f"📋 Partner Listesi — Toplam {len(partners)}",
                description="\n".join(sayfalar[self.sayfa]),
                color=0x57F287,
                timestamp=datetime.now(timezone.utc)
            )
            e.set_footer(text=f"Sayfa {self.sayfa+1}/{len(sayfalar)} • {zaman_damgasi()}")
            return e

        @discord.ui.button(label="◀", style=discord.ButtonStyle.secondary)
        async def geri(self, interaction: discord.Interaction, button: discord.ui.Button):
            if self.sayfa > 0:
                self.sayfa -= 1
            await interaction.response.edit_message(embed=self.embed_olustur(), view=self)

        @discord.ui.button(label="▶", style=discord.ButtonStyle.secondary)
        async def ileri(self, interaction: discord.Interaction, button: discord.ui.Button):
            if self.sayfa < len(sayfalar) - 1:
                self.sayfa += 1
            await interaction.response.edit_message(embed=self.embed_olustur(), view=self)

    view = SayfaView()
    await ctx.send(embed=view.embed_olustur(), view=view if len(sayfalar) > 1 else None)


@bot.command(name="partner-sifirla", aliases=["p-sifirla"])
@commands.has_permissions(administrator=True)
async def partner_sifirla(ctx):
    """.partner-sifirla — Tüm partner kayıtlarını siler (onay butonu ile)."""

    class OnayView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=30)

        @discord.ui.button(label="✅ Evet, Sıfırla", style=discord.ButtonStyle.danger)
        async def onayla(self, interaction: discord.Interaction, button: discord.ui.Button):
            ayarlar = ayarlari_yukle()
            gk = str(interaction.guild_id)
            if gk in ayarlar:
                ayarlar[gk].pop("partners", None)
                ayarlar[gk].pop("partner_gecmisi", None)
                ayarlar[gk].pop("yetkili_partnerleri", None)
                ayarlari_kaydet(ayarlar)
            await interaction.response.edit_message(embed=discord.Embed(
                title="🗑️ Partner Kayıtları Silindi",
                description="Tüm partner kayıtları ve yetkili sıralaması silindi.",
                color=RENKLER["hata"]
            ), view=None)

        @discord.ui.button(label="✖️ İptal", style=discord.ButtonStyle.secondary)
        async def iptal(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.edit_message(embed=discord.Embed(
                title="✅ İptal Edildi",
                description="İşlem iptal edildi, kayıtlar korundu.",
                color=RENKLER["basari"]
            ), view=None)

    await ctx.send(embed=discord.Embed(
        title="⚠️ Emin misiniz?",
        description="Tüm partner kayıtları ve yetkili sıralaması **kalıcı olarak** silinecek!",
        color=RENKLER["hata"]
    ), view=OnayView())





# ═══════════════════════════════════════════════════════════════
#  MODERASYON KOMUTLARI (Prefix: !)
# ═══════════════════════════════════════════════════════════════

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
    """Standart moderasyon embed'i oluşturur."""
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


# ── !ban ────────────────────────────────────────────────────────
@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    """.ban @üye [sebep]"""
    uye = await hedef_uye_bul(ctx, uye)
    if uye is None:
        await ctx.send(embed=kullanim_embedi("`.ban @uye [sebep]` veya bir mesaja yanit verip `.ban [sebep]`"))
        return
    if uye == ctx.author:
        await ctx.send("❌ Kendinizi banlayamazsınız."); return
    if uye.top_role >= ctx.author.top_role:
        await ctx.send("❌ Bu üyeyi banlayacak yetkiniz yok."); return

    await uye.ban(reason=f"{ctx.author} tarafından: {sebep}", delete_message_seconds=0)

    embed = mod_embed("🔨 Üye Banlandı", RENKLER["ban"],
        **{"👤 Üye": f"{uye.mention} `{uye}`",
           "📝 Sebep": sebep,
           "🛡️ Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "ban_log", embed)

    try:
        await uye.send(embed=discord.Embed(
            title="🔨 Sunucudan Banlandınız",
            description=f"**{ctx.guild.name}** sunucusundan banlandınız.\n**Sebep:** {sebep}",
            color=RENKLER["ban"]
        ))
    except discord.Forbidden:
        pass


@ban.error
async def ban_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Ban yetkine sahip değilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("Üye Bulunamadı", "Belirttiğin üye bulunamadı veya sunucuda değil."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("`.ban @üye [sebep]`"))


# ── !unban ───────────────────────────────────────────────────────
@bot.command(name="unban")
@commands.has_permissions(ban_members=True)
async def unban(ctx, kullanici_id: int, *, sebep: str = "Sebep belirtilmedi"):
    """.unban <kullanıcı_id> [sebep]"""
    try:
        kullanici = await bot.fetch_user(kullanici_id)
        await ctx.guild.unban(kullanici, reason=f"{ctx.author} tarafından: {sebep}")

        embed = mod_embed("✅ Ban Kaldırıldı", RENKLER["unban"],
            **{"👤 Kullanıcı": f"`{kullanici}`",
               "📝 Sebep": sebep,
               "🛡️ Yetkili": ctx.author.mention})
        await ctx.send(embed=embed)
        await log_gonder(ctx.guild, "ban_log", embed)

    except discord.NotFound:
        await ctx.send("❌ Bu ID'ye sahip banlı bir kullanıcı bulunamadı.")


@unban.error
async def unban_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Ban yetkine sahip değilsin.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("📌 Kullanım: ``.unban <kullanıcı_id> [sebep]`")


# ── !kick ────────────────────────────────────────────────────────
@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    uye = await hedef_uye_bul(ctx, uye)
    if uye is None:
        await ctx.send(embed=kullanim_embedi("`.kick @uye [sebep]` veya bir mesaja yanit verip `.kick [sebep]`"))
        return
    """.kick @üye [sebep]"""
    if uye == ctx.author:
        await ctx.send("❌ Kendinizi atamazsınız."); return
    if uye.top_role >= ctx.author.top_role:
        await ctx.send("❌ Bu üyeyi atacak yetkiniz yok."); return

    await uye.kick(reason=f"{ctx.author} tarafından: {sebep}")

    embed = mod_embed("👢 Üye Atıldı", RENKLER["mute"],
        **{"👤 Üye": f"{uye.mention} `{uye}`",
           "📝 Sebep": sebep,
           "🛡️ Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mod_log", embed)

    try:
        await uye.send(embed=discord.Embed(
            title="👢 Sunucudan Atıldınız",
            description=f"**{ctx.guild.name}** sunucusundan atıldınız.\n**Sebep:** {sebep}",
            color=RENKLER["mute"]
        ))
    except discord.Forbidden:
        pass


@kick.error
async def kick_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Kick yetkine sahip değilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("Üye Bulunamadı", "Belirttiğin üye bulunamadı veya sunucuda değil."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("`.kick @üye [sebep]`"))


# ── .mute (timeout) ──────────────────────────────────────────────
@bot.command(name="mute")
@commands.has_permissions(moderate_members=True)
async def mute(ctx, uye: discord.Member, *, arguman: str = ""):
    """
    .mute @üye [süre] [sebep]
    Tüm argümanları tek string olarak alır, sonra parse eder.
    Böylece .mute @üye, .mute @üye sebep, .mute @üye 10m sebep hepsi çalışır.
    """
    if uye == ctx.author:
        await ctx.send("❌ Kendinizi susturamassınız."); return
    if uye.top_role >= ctx.author.top_role:
        await ctx.send("❌ Bu üyeyi susturacak yetkiniz yok."); return

    birimler = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    parcalar = arguman.strip().split()

    # İlk kelime süre formatında mı? (örn: 10m, 2h, 1d, 30s)
    if parcalar and parcalar[0][-1] in birimler and parcalar[0][:-1].isdigit():
        sure_str = parcalar[0]
        saniye = int(sure_str[:-1]) * birimler[sure_str[-1]]
        sebep = " ".join(parcalar[1:]) if len(parcalar) > 1 else "Sebep belirtilmedi"
        sure_goster = sure_str
        if saniye > 2419200:
            await ctx.send("❌ Maksimum süre 28 gündür."); return
    else:
        # Süre yok → tüm argüman sebep, süresiz mute
        saniye = 2419200
        sure_goster = "Süresiz"
        sebep = arguman.strip() if arguman.strip() else "Sebep belirtilmedi"

    bitis = datetime.now(timezone.utc) + timedelta(seconds=saniye)
    await uye.timeout(timedelta(seconds=saniye), reason=f"{ctx.author}: {sebep}")

    embed = mod_embed("🔇 Üye Susturuldu", RENKLER["mute"],
        **{"👤 Üye": f"{uye.mention} `{uye}`",
           "⏱️ Süre": sure_goster,
           "⏰ Bitiş": bitis.strftime("%d.%m.%Y %H:%M UTC"),
           "📝 Sebep": sebep,
           "🛡️ Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mute_log", embed)


@mute.error
async def mute_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Timeout yetkine sahip değilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("Üye Bulunamadı", "Belirttiğin üye bulunamadı veya sunucuda değil."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("`.mute @üye [süre] [sebep]`"))


# ── !unmute ──────────────────────────────────────────────────────
@bot.command(name="unmute")
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, uye: discord.Member, *, sebep: str = "Sebep belirtilmedi"):
    """.unmute @üye [sebep]"""
    await uye.timeout(None, reason=f"{ctx.author}: {sebep}")

    embed = mod_embed("🔊 Timeout Kaldırıldı", RENKLER["unban"],
        **{"👤 Üye": f"{uye.mention} `{uye}`",
           "📝 Sebep": sebep,
           "🛡️ Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mute_log", embed)


@unmute.error
async def unmute_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Timeout kaldırma yetkine sahip değilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("❌ Üye bulunamadı.")


# ── !sil ─────────────────────────────────────────────────────────
@bot.command(name="sil")
@commands.has_permissions(manage_messages=True)
async def sil(ctx, adet: int = 5):
    """.sil [adet] — Belirtilen sayıda mesajı siler (max 100)"""
    if adet < 1 or adet > 100:
        await ctx.send("❌ 1 ile 100 arasında bir sayı girin."); return

    await ctx.message.delete()
    silinen = await ctx.channel.purge(limit=adet)

    bilgi = await ctx.send(embed=discord.Embed(
        title="🗑️ Mesajlar Silindi",
        description=f"**{len(silinen)}** mesaj silindi.",
        color=RENKLER["mesaj"]
    ))
    await asyncio.sleep(3)
    await bilgi.delete()


@sil.error
async def sil_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Mesaj silme yetkine sahip değilsin.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("📌 Kullanım: ``.sil [adet]`")


# ── !warn ────────────────────────────────────────────────────────
@bot.command(name="warn")
@commands.has_permissions(manage_messages=True)
async def warn(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    uye = await hedef_uye_bul(ctx, uye)
    if uye is None:
        await ctx.send("Kullanim: `.warn @uye [sebep]` veya bir mesaja yanit verip `.warn [sebep]`")
        return
    """.warn @üye [sebep] — Üyeye uyarı verir ve settings.json'a kaydeder."""
    # Uyarıyı kaydet
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

    embed = mod_embed(f"⚠️ Uyarı Verildi ({toplam}. uyarı)", RENKLER["mesaj"],
        **{"👤 Üye": f"{uye.mention} `{uye}`",
           "📝 Sebep": sebep,
           "🔢 Toplam Uyarı": str(toplam),
           "🛡️ Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mod_log", embed)

    try:
        await uye.send(embed=discord.Embed(
            title="⚠️ Uyarı Aldınız",
            description=f"**{ctx.guild.name}** sunucusunda uyarıldınız.\n**Sebep:** {sebep}\n**Toplam uyarı:** {toplam}",
            color=RENKLER["mesaj"]
        ))
    except discord.Forbidden:
        pass


@warn.error
async def warn_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Uyarı verme yetkine sahip değilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("❌ Üye bulunamadı.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("📌 Kullanım: ``.warn @üye [sebep]`")


# ── !uyarılar ────────────────────────────────────────────────────
@bot.command(name="uyarılar", aliases=["warnings", "uyarilar"])
@commands.has_permissions(manage_messages=True)
async def uyarilar(ctx, uye: discord.Member):
    """.uyarılar @üye — Üyenin uyarı geçmişini gösterir."""
    ayarlar = ayarlari_yukle()
    liste = ayarlar.get(str(ctx.guild.id), {}).get("uyarilar", {}).get(str(uye.id), [])

    if not liste:
        await ctx.send(embed=discord.Embed(
            title=f"📋 {uye.display_name} — Uyarı Yok",
            description="Bu üyenin hiç uyarısı bulunmuyor.",
            color=RENKLER["bilgi"]
        ))
        return

    embed = discord.Embed(
        title=f"⚠️ {uye.display_name} — {len(liste)} Uyarı",
        color=RENKLER["mesaj"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_thumbnail(url=uye.display_avatar.url)

    for i, u in enumerate(liste[-10:], 1):  # Son 10 uyarı
        try:
            zaman = datetime.fromisoformat(u["zaman"]).strftime("%d.%m.%Y %H:%M")
        except Exception:
            zaman = "—"
        embed.add_field(
            name=f"#{i} — {zaman}",
            value=f"**Sebep:** {u['sebep']}\n**Yetkili:** {u['yetkili']}",
            inline=False
        )

    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


@uyarilar.error
async def uyarilar_hata(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("❌ Üye bulunamadı.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("📌 Kullanım: ``.uyarılar @üye`")


# ── !uyarısil ────────────────────────────────────────────────────
@bot.command(name="uyarısil", aliases=["uyarisil", "clearwarns"])
@commands.has_permissions(manage_guild=True)
async def uyari_sil(ctx, uye: discord.Member):
    """.uyarısil @üye — Üyenin tüm uyarılarını siler."""
    ayarlar = ayarlari_yukle()
    guild_key = str(ctx.guild.id)
    uye_key = str(uye.id)

    if guild_key in ayarlar and "uyarilar" in ayarlar[guild_key] and uye_key in ayarlar[guild_key]["uyarilar"]:
        del ayarlar[guild_key]["uyarilar"][uye_key]
        ayarlari_kaydet(ayarlar)
        await ctx.send(embed=discord.Embed(
            title="✅ Uyarılar Silindi",
            description=f"{uye.mention} adlı üyenin tüm uyarıları silindi.",
            color=RENKLER["basari"]
        ))
    else:
        await ctx.send(f"❌ {uye.mention} adlı üyenin zaten uyarısı yok.")


# ── !yardım ──────────────────────────────────────────────────────
async def gelismis_yardim(ctx):
    def ana_embed():
        e = discord.Embed(title="Komut Rehberi", description="Bir kategori sec.", color=0x5865F2, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Kategoriler", value="Moderasyon\nPartner\nEglence\nAraclar", inline=False)
        e.set_footer(text=f"{ctx.guild.name} • {zaman_damgasi()}")
        if ctx.guild.icon:
            e.set_thumbnail(url=ctx.guild.icon.url)
        return e

    def mod_kategori():
        e = discord.Embed(title="Moderasyon", color=0xE74C3C, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Uye", value="`.ban @uye [sebep]` ┗ Banlar\n`.unban <id> [sebep]` ┗ Ban kaldirir\n`.kick @uye [sebep]` ┗ Atar\n`.mute @uye [sure] [sebep]` ┗ Susturur\n`.unmute @uye` ┗ Kaldirir", inline=False)
        e.add_field(name="Kanal & Mesaj", value="`.sil [adet]` ┗ Mesaj siler (max 100)\n`.slowmode [sn]` ┗ Yavas mod\n`.duyuru #kanal mesaj` ┗ Duyuru gonderir", inline=False)
        e.add_field(name="Uyari", value="`.warn @uye [sebep]` ┗ Verir\n`.uyarilar @uye` ┗ Gosterir\n`.uyarisil @uye` ┗ Temizler\nMesaja yanit verip `.ban/.kick/.warn` kullanabilirsin.", inline=False)
        return e

    def partner_kategori():
        e = discord.Embed(title="Partner Sistemi", color=0x57F287, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Komutlar", value="`.partner-kur #text #log` ┗ Kanallari ayarlar\n`.partner-istatistik` ┗ Istatistikler\n`.partner-top` ┗ Siralama\n`.partner-liste` ┗ Sunucu listesi\n`.partner-sifirla` ┗ Sifirlar", inline=False)
        e.add_field(name="Nasil calisir?", value="Yetkili kanala partner textini atar\nBot davet linkini kontrol eder\nLink yoksa siler, varsa kaydeder\nAyni sunucu ile 1 saat bekleme var", inline=False)
        return e

    def eglence_kategori():
        e = discord.Embed(title="Eglence & Bilgi", color=0xF1C40F, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Cekilis", value="`.cekilisbaslat [sure] [kisi] [odul]` ┗ Baslatir\n`.cekilisbitir <id>` ┗ Erken bitirir\n`.cekilisyenile <id> [kisi]` ┗ Yeni kazanan\n`.cekiliskatilimci <id>` ┗ Katilimcilari listeler\n`.cekilisbilgi <id>` ┗ Bilgi gosterir\n`.cekilissil <id>` ┗ Iptal eder", inline=False)
        e.add_field(name="AFK", value="`.afk [sebep]` ┗ AFK moduna girer\n┗ Mesaj atinca otomatik cikar\n┗ Etiketlenince AFK bildirilir", inline=False)
        e.add_field(name="Bilgi", value="`.sunucu` ┗ Sunucu istatistikleri", inline=False)
        return e

    def araclar_kategori():
        e = discord.Embed(title="Araclar & Sistemler", color=0x9B59B6, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Ticket - Yonetim", value="`.ticketkur [kategori] #log @rol` ┗ Kurar\n`.ticketpanel` ┗ Panel gonderir\n`.ticketkapat` ┗ Ticketi kapatir\n`.ticketekle @uye` ┗ Uye ekler\n`.ticketcikar @uye` ┗ Uye cikarir", inline=False)
        e.add_field(name="Ticket - Ozellikler", value="`.ticketkonu [konu]` ┗ Konu ayarlar\n`.ticketlist` ┗ Acik ticketlari listeler\n`.ticketsayi` ┗ Toplam ticket sayisi\n`.ticketoncelik [dusuk/orta/yuksek]` ┗ Oncelik belirler\n`.ticketsahip @uye` ┗ Sahibi degistirir\n`.ticketyeniden @uye` ┗ Yeniden acar", inline=False)
        e.add_field(name="Anti-Link", value="`.antilink` ┗ Durum gosterir\n`.antilink ac` ┗ Acar\n`.antilink kapat` ┗ Kapatir\n`.antilink muaf @rol/#kanal` ┗ Muafiyet ekler/kaldirir", inline=False)
        e.add_field(name="Renk Sistemi", value="`.renkekle @rol` ┗ Menuye rol ekler\n`.renkcikar @rol` ┗ Menuden rol cikarir\n`.renklist` ┗ Listedeki rolleri gosterir\n`.renkpanel` ┗ Secim paneli gonderir", inline=False)
        e.add_field(name="Log Sistemi", value="`.logkur` ┗ Otomatik kanal tarar\n`.logkurkanal` ┗ Eksik log kanallarini olusturur\n`/log-kur` · `/log-kaldir` · `/log-durum` · `/log-sifirla`", inline=False)
        e.add_field(name="Level Sistemi", value="`.levelkur` ┗ Modal ile kurulum\n`.levelrol <seviye> @rol` ┗ Rol odulu ekler\n`.levelrolsil <seviye>` ┗ Rol odulunu siler\n`.levelrolleri` ┗ Odulleri listeler\n`.levelmesajtest [@uye]`\n`.leveldurum` · `.seviye [@uye]`", inline=False)
        e.add_field(name="Hosgeldin Sistemi", value="`.hosgeldinkur` ┗ Modal ile kurulum\n`.hosgeldindurum` ┗ Ayarlari gosterir\n`.hosgeldinmesajtest [@uye]`", inline=False)
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
        e.add_field(name="Hizli Baslangic", value="`.profil` • `.ticketpanel` • `.levelkur` • `.hosgeldinkur`", inline=False)
        e.set_footer(text=f"{ctx.guild.name} • Yardim Menusu")
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
        e.add_field(name="Ticket", value="`.ticketkur [kategori] #log @rol`\n`.ticketpanel`\n`.ticketkapat` · `.ticketekle` · `.ticketcikar`\n`.ticketkonu` · `.ticketlist` · `.ticketsayi`\n`.ticketoncelik` · `.ticketsahip` · `.ticketyeniden`", inline=False)
        e.add_field(name="Log", value="`.logkur`\n`.logkurkanal`\n`/log-kur` · `/log-kaldir`\n`/log-durum` · `/log-sifirla`", inline=False)
        e.add_field(name="Level", value="`.levelkur`\n`.levelrol <seviye> @rol`\n`.levelrolsil <seviye>`\n`.levelrolleri`\n`.levelmesajtest [@uye]`\n`.leveldurum` · `.seviye [@uye]`", inline=False)
        e.add_field(name="Hosgeldin", value="`.hosgeldinkur`\n`.hosgeldindurum`\n`.hosgeldinmesajtest [@uye]`\n`.karsilamakur`\n`.karsilamadurum`\n`.karsilamatest [@uye]`", inline=False)
        e.add_field(name="Diger", value="`.antilink`\n`.antilink ac`\n`.antilink kapat`\n`.antilink muaf @rol/#kanal`\n`.renkekle @rol` · `.renkcikar @rol`\n`.renklist` · `.renkpanel`", inline=False)
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
        e.set_footer(text=f"{ctx.guild.name} • {zaman_damgasi()}")
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
        e.add_field(name="Ticket", value="`.ticketkur [kategori] #log @rol [@rol2 ...]`\n`.ticketpanel`\n`.ticketkapat` • `.ticketekle` • `.ticketcikar`\n`.ticketkonu` • `.ticketlist` • `.ticketsayi`\n`.ticketoncelik` • `.ticketsahip` • `.ticketyeniden`", inline=False)
        e.add_field(name="Log", value="`.logkur`\n`.logkurkanal`\n`/log-kur` • `/log-kaldir`\n`/log-durum` • `/log-sifirla`", inline=False)
        e.add_field(name="Level", value="`.levelkur`\n`.levelrol <seviye> @rol`\n`.levelrolsil <seviye>`\n`.levelrolleri`\n`.levelmesajtest [@uye]`\n`.leveldurum` • `.seviye [@uye]`", inline=False)
        e.add_field(name="Hosgeldin", value="`.hosgeldinkur`\n`.hosgeldindurum`\n`.hosgeldinmesajtest [@uye]`", inline=False)
        e.add_field(name="🛡️ Guvenlik Sistemleri", value="`.spam-koruma-kur` ┗ Modal ile spam koruma ayarları\n`.link-koruma-kur` ┗ Modal ile link koruma ayarları\n`.link-koruma-muaf-rol @rol` ┗ Link muaf rol ekle\n`.link-koruma-muaf-kanal #kanal` ┗ Link muaf kanal ekle\n`.link-koruma-durum` ┗ Link koruma durumu", inline=False)
        e.add_field(name="Diger Sistemler", value="`.antilink`\n`.antilink ac`\n`.antilink kapat`\n`.antilink muaf @rol/#kanal`\n`.renkekle @rol` • `.renkcikar @rol`\n`.renklist` • `.renkpanel`\n`.guvenlikkur` • `.guvenlikdurum`\n`.guvenlikizin @uye/@rol` • `.guvenlikizinsil @uye/@rol`", inline=False)
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

# ─────────────────────────────────────────
#  BOTU BAŞLAT
# ─────────────────────────────────────────

    def mod_embed():
        e = discord.Embed(title="🛡️ Moderasyon", color=0xE74C3C, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Üye", value="`.ban @üye [sebep]` ┗ Banlar\n`.unban <id> [sebep]` ┗ Ban kaldırır\n`.kick @üye [sebep]` ┗ Atar\n`.mute @üye [süre] [sebep]` ┗ Susturur · boş=kalıcı\n`.unmute @üye` ┗ Kaldırır", inline=False)
        e.add_field(name="Kanal & Mesaj", value="`.sil [adet]` ┗ Mesaj siler (max 100)\n`.slowmode [sn]` ┗ Yavaş mod · 0=kapat\n`.duyuru #kanal mesaj` ┗ Duyuru gönderir", inline=False)
        e.add_field(name="Uyarı", value="`.warn @üye [sebep]` ┗ Verir\n`.uyarılar @üye` ┗ Gösterir\n`.uyarısil @üye` ┗ Temizler", inline=False)
        return e

    def partner_embed():
        e = discord.Embed(title="🤝 Partner Sistemi", color=0x57F287, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Komutlar", value="`.partner-kur #text #log` ┗ Kanalları ayarlar\n`.partner-istatistik` ┗ İstatistikler\n`.partner-top` ┗ 🥇🥈🥉 Sıralama\n`.partner-liste` ┗ Sunucu listesi\n`.partner-sifirla` ┗ Sıfırlar", inline=False)
        e.add_field(name="Nasıl çalışır?", value="Yetkili kanala partner textini atar\nBot davet linkini kontrol eder\nLink yoksa siler · Var ise kaydeder\nAynı sunucu ile 1 saat bekleme var", inline=False)
        return e

    def eglence_embed():
        e = discord.Embed(title="🎉 Eğlence & Bilgi", color=0xF1C40F, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Çekiliş", value="`.cekilisbaslat [süre] [kişi] [ödül]` ┗ Başlatır\n`.cekilisbitir <mesaj_id>` ┗ Erken bitirir", inline=False)
        e.add_field(name="AFK", value="`.afk [sebep]` ┗ AFK moduna girer\n┗ Mesaj atınca otomatik çıkar\n┗ Etiketlenince AFK bildirilir", inline=False)
        e.add_field(name="Bilgi", value="`.sunucu` ┗ Sunucu istatistikleri", inline=False)
        return e

    def araclar_embed():
        e = discord.Embed(title="🔧 Araçlar & Sistemler", color=0x9B59B6, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Ticket", value="`.ticketkur [kategori] #log @rol` ┗ Kurar\n`.ticketpanel` ┗ Panel gönderir", inline=False)
        e.add_field(name="Anti-Link", value="`.antilink` ┗ Durum\n`.antilink ac` ┗ Açar\n`.antilink kapat` ┗ Kapatır\n`.antilink muaf @rol/#kanal` ┗ Muafiyet", inline=False)
        e.add_field(name="Log Sistemi", value="`.logkur` · `.logkurkanal`\n`/log-kur` · `/log-kaldir` · `/log-durum` · `/log-sifirla`", inline=False)
        e.add_field(name="Level Sistemi", value="`.levelkur` · `.levelrol` · `.levelrolsil` · `.levelrolleri`\n`.levelmesajtest` · `.leveldurum` · `.seviye`", inline=False)
        e.add_field(name="Hosgeldin Sistemi", value="`.hosgeldinkur` · `.hosgeldindurum` · `.hosgeldinmesajtest`", inline=False)
        e.add_field(name="🛡️ Guvenlik Sistemleri", value="`.spam-koruma-kur` ┗ Modal ile spam koruma ayarları\n`.link-koruma-kur` ┗ Modal ile link koruma ayarları\n`.link-koruma-muaf-rol @rol` ┗ Link muaf rol ekle\n`.link-koruma-muaf-kanal #kanal` ┗ Link muaf kanal ekle\n`.link-koruma-durum` ┗ Link koruma durumu", inline=False)
        return e

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=60)

        @discord.ui.button(label="🛡️ Moderasyon", style=discord.ButtonStyle.danger)
        async def btn_mod(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=mod_embed(), view=self)

        @discord.ui.button(label="🤝 Partner", style=discord.ButtonStyle.success)
        async def btn_partner(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=partner_embed(), view=self)

        @discord.ui.button(label="🎉 Eğlence", style=discord.ButtonStyle.primary)
        async def btn_eglence(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=eglence_embed(), view=self)

        @discord.ui.button(label="🔧 Araçlar", style=discord.ButtonStyle.secondary)
        async def btn_araclar(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=araclar_embed(), view=self)

        @discord.ui.button(label="🏠 Ana Menü", style=discord.ButtonStyle.secondary, row=1)
        async def btn_ana(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=ana_embed(), view=self)

    await ctx.send(embed=ana_embed(), view=HelpView())


# ─────────────────────────────────────────
#  BOTU BAŞLAT
# ─────────────────────────────────────────




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
        "Moderasyon": {"ban", "unban", "kick", "mute", "unmute", "sil", "warn", "uyarılar", "uyarısil", "slowmode", "duyuru", "jail", "unjail"},
        "Roller": {"renkekle", "renkcikar", "renklist", "renkpanel", "animerollerikur", "animerollerikaldir", "animerolpanel", "asagitasi", "levelrol", "levelrolsil", "levelrolleri"},
        "Sistemler": {"ticketekle", "ticketcikar", "ticketkapat", "ticketkonu", "ticketlist", "ticketsayi", "ticketoncelik", "ticketsahip", "ticketyeniden", "hosgeldindurum", "hosgeldinmesajtest", "karsilamadurum", "karsilamatest", "leveldurum", "levelmesajtest"},
        "Kullanici": {"profil", "seviye", "sunucu", "afk", "partner-istatistik", "partner-top", "partner-liste", "partner-sifirla"},
        "Eglence": {"cekilisbaslat", "cekilisbitir", "çekilişkatılımcı", "çekilişsil", "çekilişyenile", "çekilişbilgi"},
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
        "Eglence": {"cekilisbaslat", "cekilisbitir", "çekilişkatılımcı", "çekilişsil", "çekilişyenile", "çekilişbilgi", "afk"},
        "Moderasyon": {"ban", "unban", "kick", "mute", "unmute", "sil", "warn", "uyarılar", "uyarısil", "slowmode", "duyuru"},
    }


def _yardim_komutlarini_topla():
    prefix_komutlar = {}
    for komut in bot.commands:
        if komut.hidden or komut.name in {"yardÄ±m", "yardim", "help"}:
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


for _eski in ("yardim", "help", "yardÄ±m"):
    try:
        bot.remove_command(_eski)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardım", "help"])
async def yardim(ctx):
    await gelismis_yardim_v3(ctx)

# ── AFK yardımcı fonksiyonlar ────────────────────────────────────

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

# ── Anti-link yardımcı fonksiyonlar ─────────────────────────────

def antilink_durum_al(guild_id: int) -> dict:
    return ayarlari_yukle().get(str(guild_id), {}).get("antilink", {"aktif": False, "muaf_roller": [], "muaf_kanallar": []})

def antilink_kaydet(guild_id: int, veri: dict):
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        ayarlar[gk]["antilink"] = veri

    ayarlari_guncelle(_guncelle)

# ─────────────────────────────────────────
#  PARTNER KANALI — MESAJ KONTROLÜ
# ─────────────────────────────────────────

import re
DAVET_REGEX = re.compile(r"(?:https?://)?(?:discord\.(?:gg|com)|discordapp\.com)/(?:invite/)?([a-zA-Z0-9_-]+)")
@bot.event
async def on_message(message: discord.Message):
    """
    Partner kanalı mesaj kontrolü + AFK + Anti-link + prefix komutları
    """
    if message.author.bot:
        await _prefix_komutlari_isle(message)
        return

    if message.guild:
        # ── Partner kanalı kontrolü ──────────────────────────
        partner_ch_id = partner_kanal_id_al(message.guild.id)
        if partner_ch_id and message.channel.id == partner_ch_id:
            eslesen = DAVET_REGEX.search(message.content)

            if not eslesen:
                try:
                    await message.delete()
                except discord.Forbidden:
                    pass
                uyari = await message.channel.send(embed=discord.Embed(
                    title="❌ Geçersiz Partner Metni",
                    description=f"{message.author.mention} Mesajınızda Discord davet linki bulunamadı. Mesajınız silindi.",
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

            # 1 saat bekleme kontrolü
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
                            title="⏳ Bekleme Süresi Dolmadı",
                            description=(
                                f"{message.author.mention} Bu sunucuyla tekrar partner yapmak için\n"
                                f"**{kalan // 60} dakika {kalan % 60} saniye** beklemeniz gerekiyor.\n"
                                f"Son partner: <@{onceki_id}> tarafından yapıldı."
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
                title="🤝 Yeni Partner Yapıldı!",
                description=f"{message.author.mention} yeni bir partnerlik yaptı!",
                color=0x57F287,
                timestamp=simdi
            )
            stats_embed.add_field(name="📊 Sunucu Sırası",  value=f"**#{sira}**",                              inline=True)
            stats_embed.add_field(name="👤 Yetkili Sırası", value=f"**#{yetkili_sira}** ({yetkili_toplam} partnerlik)", inline=True)
            stats_embed.add_field(
                name="🕐 Zamana Dayalı:",
                value=(
                    f"› Günlük: **{stats['gunluk']}**\n"
                    f"› Haftalık: **{stats['haftalik']}**\n"
                    f"› Aylık: **{stats['aylik']}**"
                ),
                inline=True
            )
            stats_embed.add_field(name="• Toplam", value=f"**{stats['toplam']}**", inline=True)
            stats_embed.set_footer(text=f"{bot.user.name} • Partner Sistemi")
            if message.guild.icon:
                stats_embed.set_thumbnail(url=message.guild.icon.url)
            await message.channel.send(embed=stats_embed)

            log_kanal_id = partner_log_kanali_al(message.guild.id)
            if log_kanal_id:
                log_kanal = message.guild.get_channel(log_kanal_id)
                if log_kanal:
                    log_embed = discord.Embed(title="📋 Partner Logu", color=0x57F287, timestamp=simdi)
                    log_embed.add_field(name="🔗 Davet",          value=f"`{davet_kodu}`",                       inline=True)
                    log_embed.add_field(name="👤 Yapan",          value=message.author.mention,                  inline=True)
                    log_embed.add_field(name="📅 Zaman",          value=simdi.strftime("%d.%m.%Y %H:%M UTC"),    inline=True)
                    log_embed.add_field(name="📊 Toplam",         value=str(stats["toplam"]),                    inline=True)
                    log_embed.add_field(name="👤 Yetkili Toplamı", value=str(yetkili_toplam),                   inline=True)
                    log_embed.set_footer(text=zaman_damgasi())
                    await log_kanal.send(embed=log_embed)
            return

        # ── AFK kontrolü ─────────────────────────────────────
        afk_veri = afk_al(message.guild.id, message.author.id)
        if afk_veri and not message.content.startswith(".afk"):
            afk_sil(message.guild.id, message.author.id)
            zaman_afk = utc_datetime_from_iso(afk_veri["zaman"])
            dk = int((datetime.now(timezone.utc) - zaman_afk).total_seconds() // 60)
            uyari = await message.channel.send(embed=discord.Embed(
                title="👋 AFK Modundan Çıkıldı",
                description=f"{message.author.mention} AFK modundan çıktı! ({dk} dakika AFK'daydı)",
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

        # Etiketlenen kişi AFK mı?
        for etiket in message.mentions:
            afk_bilgi = afk_al(message.guild.id, etiket.id)
            if afk_bilgi:
                await message.channel.send(embed=discord.Embed(
                    description=f"💤 {etiket.mention} şu an AFK — **{afk_bilgi['sebep']}**",
                    color=RENKLER["bilgi"]
                ), delete_after=8)

        # ── Anti-link kontrolü ───────────────────────────────
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
                        title="🔗 Link Engellendi",
                        description=f"{message.author.mention} Bu kanalda link paylaşmak yasak!",
                        color=RENKLER["hata"]
                    ))
                    await asyncio.sleep(5)
                    try:
                        await uyari.delete()
                    except discord.NotFound:
                        pass
                    return

        # ── Küfür Koruması kontolü ──────────────────────────
        yasakli_kelimeler = kufur_kelimelerini_al(message.guild.id)
        if yasakli_kelimeler and mesajda_yasakli_kelime_var_mi(message.content, yasakli_kelimeler):
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            uyari = await message.channel.send(embed=discord.Embed(
                title="🛡️ Küfür Algılandı",
                description=f"{message.author.mention} Mesajınızda yasak kelime bulunduğu için silinmiştir.",
                color=RENKLER["hata"]
            ))
            await asyncio.sleep(5)
            try:
                await uyari.delete()
            except discord.NotFound:
                pass
            return

    await _prefix_komutlari_isle(message)


# ═══════════════════════════════════════════════════════════════
#  SLOWMODE
# ═══════════════════════════════════════════════════════════════

@bot.command(name="slowmode", aliases=["sm", "yavasm"])
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, sure: int = 0):
    if sure < 0 or sure > 21600:
        await ctx.send("❌ Süre 0-21600 saniye arasında olmalı."); return
    await ctx.channel.edit(slowmode_delay=sure)
    if sure == 0:
        embed = discord.Embed(title="✅ Yavaş Mod Kapatıldı", color=RENKLER["basari"])
    else:
        embed = discord.Embed(title="🐢 Yavaş Mod Açıldı", color=RENKLER["mute"])
        embed.add_field(name="⏱️ Süre", value=f"{sure} saniye", inline=True)
    embed.add_field(name="📍 Kanal", value=ctx.channel.mention, inline=True)
    embed.add_field(name="🛡️ Yetkili", value=ctx.author.mention, inline=True)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)

@slowmode.error
async def slowmode_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Kanal yönetme yetkine sahip değilsin.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("📌 Kullanım: `.slowmode [saniye]`")


# ═══════════════════════════════════════════════════════════════
#  DUYURU
# ═══════════════════════════════════════════════════════════════

@bot.command(name="duyuru", aliases=["announce", "ann"])
@commands.has_permissions(manage_guild=True)
async def duyuru(ctx, kanal: discord.TextChannel = None, *, mesaj: str = None):
    if not mesaj:
        await ctx.send("📌 Kullanım: `.duyuru #kanal mesajınız`"); return
    hedef = kanal or ctx.channel
    embed = discord.Embed(description=mesaj, color=0xE74C3C, timestamp=datetime.now(timezone.utc))
    embed.set_author(name=f"📢 {ctx.guild.name} Duyurusu", icon_url=ctx.guild.icon.url if ctx.guild.icon else None)
    embed.set_footer(text=f"Duyuran: {ctx.author}")
    await hedef.send("@everyone", embed=embed)
    try: await ctx.message.delete()
    except: pass

@duyuru.error
async def duyuru_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Sunucu yönetme yetkine sahip değilsin.")


# ═══════════════════════════════════════════════════════════════
#  SUNUCU İSTATİSTİK
# ═══════════════════════════════════════════════════════════════

@bot.command(name="sunucu", aliases=["server", "serverinfo", "si"])
async def sunucu_bilgi(ctx):
    g = ctx.guild
    insan  = sum(1 for m in g.members if not m.bot)
    botlar = sum(1 for m in g.members if m.bot)
    embed = discord.Embed(title=f"📊 {g.name}", color=0x5865F2, timestamp=datetime.now(timezone.utc))
    if g.icon: embed.set_thumbnail(url=g.icon.url)
    embed.add_field(name="👑 Sahip",       value=g.owner.mention,                                    inline=True)
    embed.add_field(name="🆔 ID",          value=f"`{g.id}`",                                        inline=True)
    embed.add_field(name="📅 Kuruluş",     value=g.created_at.strftime("%d.%m.%Y"),                  inline=True)
    embed.add_field(name="👥 Toplam Üye",  value=str(g.member_count),                                inline=True)
    embed.add_field(name="🧑 İnsan",       value=str(insan),                                         inline=True)
    embed.add_field(name="🤖 Bot",         value=str(botlar),                                        inline=True)
    embed.add_field(name="💬 Metin Kanal", value=str(len(g.text_channels)),                          inline=True)
    embed.add_field(name="🔊 Ses Kanal",   value=str(len(g.voice_channels)),                         inline=True)
    embed.add_field(name="🎭 Rol",         value=str(len(g.roles) - 1),                             inline=True)
    embed.add_field(name="🚀 Boost",       value=f"{g.premium_subscription_count} · Seviye {g.premium_tier}", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


# ═══════════════════════════════════════════════════════════════
#  AFK SİSTEMİ
# ═══════════════════════════════════════════════════════════════

@bot.command(name="afk")
async def afk_cmd(ctx, *, sebep: str = "AFK"):
    afk_kaydet(ctx.guild.id, ctx.author.id, sebep)
    embed = discord.Embed(
        title="😴 AFK Moduna Geçildi",
        description=f"{ctx.author.mention} AFK moduna geçti.\n**Sebep:** {sebep}",
        color=RENKLER["bilgi"]
    )
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)
    try:
        await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}"[:32])
    except discord.Forbidden:
        pass


# ═══════════════════════════════════════════════════════════════
#  ÇEKİLİŞ SİSTEMİ
# ═══════════════════════════════════════════════════════════════

import random as _random

@bot.command(name="cekilisbaslat", aliases=["cekilish", "gstart", "giveaway"])
@commands.has_permissions(manage_guild=True)
async def cekilisbaslat(ctx, sure: str = None, kazanan: int = 1, *, odul: str = None):
    if not sure or not odul:
        await ctx.send("📌 Kullanım: `.cekilisbaslat 1h 1 Nitro`"); return
    birimler = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    try:
        saniye = int(sure[:-1]) * birimler[sure[-1]]
    except (ValueError, KeyError, IndexError):
        await ctx.send("❌ Geçersiz süre. Örnek: `10s`, `5m`, `2h`, `1d`"); return
    bitis = datetime.now(timezone.utc) + timedelta(seconds=saniye)
    embed = discord.Embed(
        title=f"🎉 ÇEKİLİŞ — {odul}",
        description=f"Katılmak için 🎉 tepkisini ver!\n\n**⏰ Bitiş:** {bitis.strftime('%d.%m.%Y %H:%M UTC')}\n**🏆 Kazanan:** {kazanan} kişi\n**🎁 Ödül:** {odul}",
        color=0xFF73FA, timestamp=bitis
    )
    embed.set_footer(text="Bitiş")
    mesaj = await ctx.send(embed=embed)
    await mesaj.add_reaction("🎉")
    try: await ctx.message.delete()
    except: pass
    await asyncio.sleep(saniye)
    try: mesaj = await ctx.channel.fetch_message(mesaj.id)
    except discord.NotFound: return
    tepki = discord.utils.get(mesaj.reactions, emoji="🎉")
    if not tepki:
        await ctx.send("❌ Kimse katılmadı, çekiliş iptal."); return
    katilimcilar = [u async for u in tepki.users() if not u.bot]
    if not katilimcilar:
        await ctx.send("❌ Geçerli katılımcı yok."); return
    kazananlar  = _random.sample(katilimcilar, min(kazanan, len(katilimcilar)))
    kazanan_str = " ".join(u.mention for u in kazananlar)
    bitis_embed = discord.Embed(
        title=f"🎊 ÇEKİLİŞ SONA ERDİ — {odul}",
        description=f"**🏆 Kazanan:** {kazanan_str}\n**🎁 Ödül:** {odul}\n**👥 Katılımcı:** {len(katilimcilar)}",
        color=0xFF73FA, timestamp=datetime.now(timezone.utc)
    )
    await mesaj.edit(embed=bitis_embed)
    await ctx.channel.send(f"🎉 Tebrikler {kazanan_str}! **{odul}** kazandınız!")

@cekilisbaslat.error
async def cekilisbaslat_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Sunucu yönetme yetkine sahip değilsin.")

@bot.command(name="cekilisbitir", aliases=["gend"])
@commands.has_permissions(manage_guild=True)
async def cekilisbitir(ctx, mesaj_id: int = None):
    if not mesaj_id:
        await ctx.send("📌 Kullanım: `.cekilisbitir <mesaj_id>`"); return
    try: mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send("❌ Mesaj bulunamadı."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="🎉")
    if not tepki:
        await ctx.send("❌ Bu mesajda 🎉 tepkisi yok."); return
    katilimcilar = [u async for u in tepki.users() if not u.bot]
    if not katilimcilar:
        await ctx.send("❌ Katılımcı yok."); return
    kazanan = _random.choice(katilimcilar)
    await ctx.send(f"🎉 Yeni kazanan: {kazanan.mention}!")


# ── Ek Çekiliş Komutları ────────────────────────────────────────

@bot.command(name="çekilişkatılımcı", aliases=["glist", "cekiliskatilimci", "katilimcilar"])
async def cekiliskatilimci(ctx, mesaj_id: int = None):
    """.çekilişkatılımcı <mesaj_id> — Çekiliş katılımcılarını listeler."""
    if not mesaj_id:
        await ctx.send("📌 Kullanım: `.çekilişkatılımcı <mesaj_id>`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send("❌ Mesaj bulunamadı."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="🎉")
    katilimcilar = [u async for u in tepki.users() if not u.bot] if tepki else []
    if not katilimcilar:
        await ctx.send("❌ Henüz kimse katılmamış."); return
    embed = discord.Embed(
        title=f"🎉 Çekiliş Katılımcıları — {len(katilimcilar)} kişi",
        description="\n".join(f"`{i+1}.` {u.mention}" for i, u in enumerate(katilimcilar[:30])),
        color=0xFF73FA,
        timestamp=datetime.now(timezone.utc)
    )
    if len(katilimcilar) > 30:
        embed.set_footer(text=f"İlk 30 gösteriliyor · Toplam: {len(katilimcilar)}")
    else:
        embed.set_footer(text=f"Toplam: {len(katilimcilar)} katılımcı")
    await ctx.send(embed=embed)


@bot.command(name="çekilişsil", aliases=["gdelete", "cekilissil", "gcancel"])
@commands.has_permissions(manage_guild=True)
async def cekilissil(ctx, mesaj_id: int = None):
    """.çekilişsil <mesaj_id> — Çekilişi iptal eder ve siler."""
    if not mesaj_id:
        await ctx.send("📌 Kullanım: `.çekilişsil <mesaj_id>`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
        await mesaj.delete()
        await ctx.send(embed=discord.Embed(
            title="🗑️ Çekiliş İptal Edildi",
            description="Çekiliş mesajı silindi.",
            color=RENKLER["hata"]
        ), delete_after=5)
    except discord.NotFound:
        await ctx.send("❌ Mesaj bulunamadı.")


@bot.command(name="çekilişyenile", aliases=["greroll", "cekilisyenile"])
@commands.has_permissions(manage_guild=True)
async def cekilisyenile(ctx, mesaj_id: int = None, kazanan: int = 1):
    """.çekilişyenile <mesaj_id> [kazanan sayısı] — Yeni kazanan seçer."""
    if not mesaj_id:
        await ctx.send("📌 Kullanım: `.çekilişyenile <mesaj_id> [kazanan sayısı]`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send("❌ Mesaj bulunamadı."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="🎉")
    katilimcilar = [u async for u in tepki.users() if not u.bot] if tepki else []
    if not katilimcilar:
        await ctx.send("❌ Katılımcı yok."); return
    kazananlar = _random.sample(katilimcilar, min(kazanan, len(katilimcilar)))
    kazanan_str = " ".join(u.mention for u in kazananlar)
    embed = discord.Embed(
        title="🎊 Çekiliş Yenilendi!",
        description=f"**Yeni kazanan(lar):** {kazanan_str}",
        color=0xFF73FA,
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)
    await ctx.send(f"🎉 Tebrikler {kazanan_str}!")


@bot.command(name="çekilişbilgi", aliases=["ginfo", "cekilisbilgi"])
async def cekilisbilgi(ctx, mesaj_id: int = None):
    """.çekilişbilgi <mesaj_id> — Çekiliş bilgilerini gösterir."""
    if not mesaj_id:
        await ctx.send("📌 Kullanım: `.çekilişbilgi <mesaj_id>`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send("❌ Mesaj bulunamadı."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="🎉")
    katilimcilar = [u async for u in tepki.users() if not u.bot] if tepki else []
    embed = discord.Embed(
        title="📊 Çekiliş Bilgileri",
        color=0xFF73FA,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="👥 Katılımcı", value=str(len(katilimcilar)), inline=True)
    embed.add_field(name="📅 Oluşturma", value=mesaj.created_at.strftime("%d.%m.%Y %H:%M"), inline=True)
    embed.add_field(name="🔗 Mesaj", value=f"[Tıkla]({mesaj.jump_url})", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


# ═══════════════════════════════════════════════════════════════
#  TİCKET SİSTEMİ (GELİŞTİRİLMİŞ)
# ═══════════════════════════════════════════════════════════════

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
            ekler = f'<div class="attachments">Ekler: {" • ".join(baglantilar)}</div>'
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
      <p>{len(mesajlar)} mesaj • {html.escape(channel.guild.name)}</p>
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
    .ticketkur [kategori] #log-kanal @destek-rolü [@destek-rolü-2 ...]
    Ticket sistemini kurar.
    """
    if not kategori or not log or not destek_rolleri:
        await ctx.send(embed=kullanim_embedi("`.ticketkur [kategori] #log-kanal @destek-rolü [@destek-rolü-2 ...]`")); return

    destek_rolleri = list(dict.fromkeys(rol.id for rol in destek_rolleri if rol))
    if not destek_rolleri:
        await ctx.send(embed=hata_embedi("Destek Rolü Gerekli", "Ticket sistemi için en az bir destek rolü belirtmelisin."))
        return

    mevcut = ticket_ayar_al(ctx.guild.id)
    mevcut.update({"kategori": kategori.id, "log": log.id, "rol_ids": destek_rolleri, "rol": destek_rolleri[0]})
    ticket_ayar_kaydet(ctx.guild.id, mevcut)

    embed = discord.Embed(title="✅ Ticket Sistemi Kuruldu", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="📁 Kategori",    value=kategori.name,      inline=True)
    embed.add_field(name="📋 Log",         value=log.mention,         inline=True)
    destek_rol_mentionlari = [ctx.guild.get_role(rid).mention for rid in destek_rolleri if ctx.guild.get_role(rid)]
    embed.add_field(name="🛡️ Destek Rolleri", value=", ".join(destek_rol_mentionlari) if destek_rol_mentionlari else "Yok", inline=False)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


@bot.command(name="ticketpanel", aliases=["ticket-panel"])
@commands.has_permissions(administrator=True)
async def ticket_panel(ctx):
    """.ticketpanel — Ticket açma paneli gönderir."""
    ayar = ticket_ayar_al(ctx.guild.id)
    if not ayar.get("kategori"):
        await ctx.send("❌ Önce `.ticketkur` ile sistemi kur."); return

    class TicketView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label="🎫 Ticket Aç", style=discord.ButtonStyle.primary, custom_id="global_ticket_ac")
        async def ticket_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
            ayar        = ticket_ayar_al(interaction.guild_id)
            kategori    = interaction.guild.get_channel(ayar.get("kategori"))
            destek_rolleri = [interaction.guild.get_role(rid) for rid in ayar.get("rol_ids", [])]
            destek_rolleri = [rol for rol in destek_rolleri if rol]
            log_id      = ayar.get("log")

            if not kategori:
                await interaction.response.send_message("❌ Kategori bulunamadı. `.ticketkur` ile yeniden kur.", ephemeral=True); return

            # Açık ticket var mı kontrol et
            for kanal in kategori.text_channels:
                if kanal.topic and str(interaction.user.id) in kanal.topic:
                    await interaction.response.send_message(f"❌ Zaten açık bir ticketın var: {kanal.mention}", ephemeral=True); return

            # Ticket numarası
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

            # Ticket kanalı view (kapat + talep al)
            class TicketKontrolView(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=None)

                @discord.ui.button(label="🔒 Kapat", style=discord.ButtonStyle.danger, custom_id=f"ticket_kapat_{ticket_kanal.id}")
                async def kapat(self, i2: discord.Interaction, b: discord.ui.Button):
                    await _ticket_kapat_logu_ve_transkript(ticket_kanal, i2.user, log_id)
                    await i2.response.send_message("Ticket kapatılıyor...", ephemeral=True)

                    if False and log_id:
                        log_k = i2.guild.get_channel(log_id)
                        if log_k:
                            await log_k.send(embed=discord.Embed(
                                title="🔒 Ticket Kapatıldı",
                                description=(
                                    f"**Ticket:** `{ticket_kanal.name}`\n"
                                    f"**Sahip:** {interaction.user.mention}\n"
                                    f"**Kapatan:** {i2.user.mention}"
                                ),
                                color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)
                            ))
                    await ticket_kanal.delete(reason=f"{i2.user} tarafından kapatıldı")

                @discord.ui.button(label="👥 Üye Ekle", style=discord.ButtonStyle.secondary, custom_id=f"ticket_uyeekle_{ticket_kanal.id}")
                async def uye_ekle(self, i2: discord.Interaction, b: discord.ui.Button):
                    if destek_rolleri and not any(rol in i2.user.roles for rol in destek_rolleri) and not i2.user.guild_permissions.administrator:
                        await i2.response.send_message("❌ Bu işlem için destek rolü veya yönetici yetkisi gerekli.", ephemeral=True)
                        return
                    await i2.response.send_message("Eklemek istediğin kullanıcıyı etiketle: (örn: @kullanıcı)", ephemeral=True)

                    def check(m):
                        return m.author == i2.user and m.channel == ticket_kanal and m.mentions

                    try:
                        yanit = await bot.wait_for("message", check=check, timeout=30)
                        for uye in yanit.mentions:
                            await ticket_kanal.set_permissions(uye, read_messages=True, send_messages=True)
                        await ticket_kanal.send(f"✅ {' '.join(u.mention for u in yanit.mentions)} ticketa eklendi.")
                        await yanit.delete()
                    except asyncio.TimeoutError:
                        pass

                @discord.ui.button(label="📋 Talep Al", style=discord.ButtonStyle.success, custom_id=f"ticket_talep_{ticket_kanal.id}")
                async def talep_al(self, i2: discord.Interaction, b: discord.ui.Button):
                    if destek_rolleri and not any(rol in i2.user.roles for rol in destek_rolleri) and not i2.user.guild_permissions.administrator:
                        await i2.response.send_message("❌ Bu işlem için destek rolü gerekli.", ephemeral=True); return
                    await ticket_kanal.edit(topic=f"{ticket_kanal.topic} | Talep: {i2.user}")
                    await i2.response.send_message(f"✅ Ticket {i2.user.mention} tarafından talep alındı.")

            ac_embed = discord.Embed(
                title=f"🎫 Ticket #{sayi:04d}",
                description=(
                    f"Merhaba {interaction.user.mention}!\n"
                    f"Destek ekibimiz en kısa sürede yardımcı olacak.\n\n"
                    f"Ticketı kapatmak için 🔒 butonunu kullan."
                ),
                color=0x57F287, timestamp=datetime.now(timezone.utc)
            )
            ac_embed.set_footer(text=f"Ticket #{sayi:04d} • {zaman_damgasi()}")

            await ticket_kanal.send(
                content=" ".join([interaction.user.mention] + [rol.mention for rol in destek_rolleri]),
                embed=ac_embed,
                view=TicketKontrolView()
            )
            await interaction.response.send_message(f"✅ Ticketın açıldı: {ticket_kanal.mention}", ephemeral=True)

            if log_id:
                log_k = interaction.guild.get_channel(log_id)
                if log_k:
                    await log_k.send(embed=discord.Embed(
                        title="🎫 Yeni Ticket Açıldı",
                        description=f"**Açan:** {interaction.user.mention}\n**Kanal:** {ticket_kanal.mention}\n**Numara:** `#{sayi:04d}`",
                        color=RENKLER["giris"], timestamp=datetime.now(timezone.utc)
                    ))

    panel_embed = discord.Embed(
        title="🎫 Destek Merkezi",
        description="Yardım almak için aşağıdaki butona tıkla.\nEkibimiz en kısa sürede sana yardımcı olacak.",
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
    """.ticketekle @üye — Ticket kanalına üye ekler."""
    if not uye:
        await ctx.send("📌 Kullanım: `.ticketekle @üye`"); return
    await ctx.channel.set_permissions(uye, read_messages=True, send_messages=True)
    await ctx.send(embed=discord.Embed(
        description=f"✅ {uye.mention} ticketa eklendi.",
        color=RENKLER["basari"]
    ))


@bot.command(name="ticketcikar", aliases=["ticket-cikar"])
@commands.has_permissions(manage_channels=True)
async def ticket_cikar(ctx, uye: discord.Member = None):
    """.ticketcikar @üye — Ticket kanalından üye çıkarır."""
    if not uye:
        await ctx.send("📌 Kullanım: `.ticketcikar @üye`"); return
    await ctx.channel.set_permissions(uye, read_messages=False)
    await ctx.send(embed=discord.Embed(
        description=f"✅ {uye.mention} tickettan çıkarıldı.",
        color=RENKLER["hata"]
    ))


@bot.command(name="ticketkapat", aliases=["ticket-kapat"])
@commands.has_permissions(manage_channels=True)
async def ticket_kapat(ctx):
    """.ticketkapat — Mevcut ticket kanalını kapatır."""
    if not ctx.channel.name.startswith("ticket-"):
        await ctx.send("❌ Bu komut sadece ticket kanallarında kullanılabilir."); return

    ayar   = ticket_ayar_al(ctx.guild.id)
    log_id = ayar.get("log")
    await _ticket_kapat_logu_ve_transkript(ctx.channel, ctx.author, log_id)

    if False and log_id:
        log_k = ctx.guild.get_channel(log_id)
        if log_k:
            await log_k.send(embed=discord.Embed(
                title="🔒 Ticket Kapatıldı",
                description=f"**Ticket:** `{ctx.channel.name}`\n**Kapatan:** {ctx.author.mention}",
                color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)
            ))
    await ctx.send("Ticket kapatılıyor...")
    await asyncio.sleep(2)
    await ctx.channel.delete(reason=f"{ctx.author} tarafından kapatıldı")

# ─────────────────────────────────────────
#  FLASK (RENDER CANLI TUTMAK İÇİN)
# ─────────────────────────────────────────

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
    "꒰꒰ 🍥 ˊˎ Naruto ꒱", "꒰꒰ 🔥 ˊˎ Sasuke ꒱", "꒰꒰ 🌸 ˊˎ Sakura ꒱", "꒰꒰ ⚡ ˊˎ Kakashi ꒱",
    "꒰꒰ 🌙 ˊˎ Itachi ꒱", "꒰꒰ 🦊 ˊˎ Kurama ꒱", "꒰꒰ 🍖 ˊˎ Luffy ꒱", "꒰꒰ 🗡️ ˊˎ Zoro ꒱",
    "꒰꒰ 🍊 ˊˎ Nami ꒱", "꒰꒰ 🔥 ˊˎ Ace ꒱", "꒰꒰ 👒 ˊˎ Shanks ꒱", "꒰꒰ 🌀 ˊˎ Law ꒱",
    "꒰꒰ 🕊️ ˊˎ Robin ꒱", "꒰꒰ ⚙️ ˊˎ Franky ꒱", "꒰꒰ 🎻 ˊˎ Brook ꒱", "꒰꒰ ☁️ ˊˎ Sanji ꒱",
    "꒰꒰ 🍓 ˊˎ Ichigo ꒱", "꒰꒰ ❄️ ˊˎ Rukia ꒱", "꒰꒰ 🌌 ˊˎ Aizen ꒱", "꒰꒰ 🖤 ˊˎ Ulquiorra ꒱",
    "꒰꒰ 🐉 ˊˎ Goku ꒱", "꒰꒰ 💥 ˊˎ Vegeta ꒱", "꒰꒰ 🌟 ˊˎ Gohan ꒱", "꒰꒰ ☄️ ˊˎ Broly ꒱",
    "꒰꒰ 🐈 ˊˎ Beerus ꒱", "꒰꒰ ⏳ ˊˎ Whis ꒱", "꒰꒰ 🩸 ˊˎ Eren ꒱", "꒰꒰ 🪽 ˊˎ Mikasa ꒱",
    "꒰꒰ 🛡️ ˊˎ Armin ꒱", "꒰꒰ 🌧️ ˊˎ Levi ꒱", "꒰꒰ 🐺 ˊˎ Hange ꒱", "꒰꒰ 🌋 ˊˎ Reiner ꒱",
    "꒰꒰ ⚔️ ˊˎ Tanjiro ꒱", "꒰꒰ 🌸 ˊˎ Nezuko ꒱", "꒰꒰ 🐗 ˊˎ Inosuke ꒱", "꒰꒰ ⚡ ˊˎ Zenitsu ꒱",
    "꒰꒰ 🔥 ˊˎ Rengoku ꒱", "꒰꒰ 🌫️ ˊˎ Muichiro ꒱", "꒰꒰ 🦋 ˊˎ Shinobu ꒱", "꒰꒰ 💎 ˊˎ Tengen ꒱",
    "꒰꒰ 🩵 ˊˎ Gojo ꒱", "꒰꒰ 🐺 ˊˎ Megumi ꒱", "꒰꒰ 🌺 ˊˎ Nobara ꒱", "꒰꒰ 👑 ˊˎ Sukuna ꒱",
    "꒰꒰ 🐼 ˊˎ Panda ꒱", "꒰꒰ 🎀 ˊˎ Maki ꒱", "꒰꒰ 🗝️ ˊˎ Yuta ꒱", "꒰꒰ 🌀 ˊˎ Geto ꒱",
    "꒰꒰ 🎭 ˊˎ Lelouch ꒱", "꒰꒰ ♟️ ˊˎ C.C. ꒱", "꒰꒰ 🌹 ˊˎ Kallen ꒱", "꒰꒰ 👁️ ˊˎ Light ꒱",
    "꒰꒰ 🍎 ˊˎ L ꒱", "꒰꒰ 📓 ˊˎ Ryuk ꒱", "꒰꒰ 🎻 ˊˎ Kira ꒱", "꒰꒰ 🌠 ˊˎ Hikari ꒱",
    "꒰꒰ 💫 ˊˎ Emilia ꒱", "꒰꒰ 🖤 ˊˎ Rem ꒱", "꒰꒰ 💙 ˊˎ Ram ꒱", "꒰꒰ ⌛ ˊˎ Subaru ꒱",
    "꒰꒰ 🌼 ˊˎ Zero Two ꒱", "꒰꒰ 🔺 ˊˎ Hiro ꒱", "꒰꒰ 🌊 ˊˎ Marin ꒱", "꒰꒰ 🎨 ˊˎ Gojo Wakana ꒱",
    "꒰꒰ 🎵 ˊˎ Bocchi ꒱", "꒰꒰ 🎸 ˊˎ Kita ꒱", "꒰꒰ 🥁 ˊˎ Nijika ꒱", "꒰꒰ 🎼 ˊˎ Ryo ꒱",
    "꒰꒰ 🧪 ˊˎ Senku ꒱", "꒰꒰ 🐒 ˊˎ Gen ꒱", "꒰꒰ 🪨 ˊˎ Taiju ꒱", "꒰꒰ 🌿 ˊˎ Yuzuriha ꒱",
    "꒰꒰ 🌈 ˊˎ Natsu ꒱", "꒰꒰ ❄️ ˊˎ Gray ꒱", "꒰꒰ ❤️ ˊˎ Erza ꒱", "꒰꒰ 🐱 ˊˎ Happy ꒱",
    "꒰꒰ 🧣 ˊˎ Kaneki ꒱", "꒰꒰ ☕ ˊˎ Touka ꒱", "꒰꒰ 🕷️ ˊˎ Hisoka ꒱", "꒰꒰ 🎣 ˊˎ Gon ꒱",
    "꒰꒰ ⚡ ˊˎ Killua ꒱", "꒰꒰ 🔗 ˊˎ Kurapika ꒱", "꒰꒰ 🃏 ˊˎ Chrollo ꒱", "꒰꒰ 🌻 ˊˎ Power ꒱",
    "꒰꒰ 🔪 ˊˎ Denji ꒱", "꒰꒰ 🐶 ˊˎ Pochita ꒱", "꒰꒰ 🩸 ˊˎ Makima ꒱", "꒰꒰ 🦈 ˊˎ Beam ꒱",
    "꒰꒰ 🌺 ˊˎ Frieren ꒱", "꒰꒰ 🪄 ˊˎ Fern ꒱", "꒰꒰ ⚔️ ˊˎ Stark ꒱", "꒰꒰ 🧭 ˊˎ Himmel ꒱",
    "꒰꒰ 💤 ˊˎ Anya ꒱", "꒰꒰ 🕶️ ˊˎ Loid ꒱", "꒰꒰ 🌹 ˊˎ Yor ꒱", "꒰꒰ 🐕 ˊˎ Bond ꒱",
    "꒰꒰ 🌌 ˊˎ Madoka ꒱", "꒰꒰ 🎀 ˊˎ Homura ꒱", "꒰꒰ 🍡 ˊˎ Kagome ꒱", "꒰꒰ 🐺 ˊˎ Inuyasha ꒱",
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
    "꒰꒰ 🍥 ˊˎ Naruto ꒱", "꒰꒰ ☁️ ˊˎ One Piece ꒱", "꒰꒰ 🍓 ˊˎ Bleach ꒱", "꒰꒰ 🐉 ˊˎ Dragon Ball ꒱",
    "꒰꒰ 🪽 ˊˎ Attack on Titan ꒱", "꒰꒰ ⚔️ ˊˎ Demon Slayer ꒱", "꒰꒰ 🩵 ˊˎ Jujutsu Kaisen ꒱", "꒰꒰ 🎭 ˊˎ Code Geass ꒱",
    "꒰꒰ 📓 ˊˎ Death Note ꒱", "꒰꒰ 💫 ˊˎ Re:Zero ꒱", "꒰꒰ 🌼 ˊˎ Darling in the Franxx ꒱", "꒰꒰ 🌊 ˊˎ My Dress-Up Darling ꒱",
    "꒰꒰ 🎵 ˊˎ Bocchi the Rock ꒱", "꒰꒰ 🧪 ˊˎ Dr. Stone ꒱", "꒰꒰ 🌈 ˊˎ Fairy Tail ꒱", "꒰꒰ 🧣 ˊˎ Tokyo Ghoul ꒱",
    "꒰꒰ 🎣 ˊˎ Hunter x Hunter ꒱", "꒰꒰ 🔪 ˊˎ Chainsaw Man ꒱", "꒰꒰ 🌺 ˊˎ Frieren ꒱", "꒰꒰ 💤 ˊˎ Spy x Family ꒱",
    "꒰꒰ 🌌 ˊˎ Madoka Magica ꒱", "꒰꒰ 🍡 ˊˎ Inuyasha ꒱", "꒰꒰ 🎻 ˊˎ Your Lie in April ꒱", "꒰꒰ 🎤 ˊˎ Oshi no Ko ꒱",
    "꒰꒰ 🏐 ˊˎ Haikyuu ꒱", "꒰꒰ 🧡 ˊˎ Orange ꒱", "꒰꒰ 💌 ˊˎ Horimiya ꒱", "꒰꒰ 🌸 ˊˎ Kimi ni Todoke ꒱",
    "꒰꒰ 🪐 ˊˎ Steins;Gate ꒱", "꒰꒰ 🦋 ˊˎ Violet Evergarden ꒱", "꒰꒰ 🥀 ˊˎ Black Butler ꒱", "꒰꒰ 🔥 ˊˎ Fire Force ꒱",
    "꒰꒰ 🛡️ ˊˎ Shield Hero ꒱", "꒰꒰ 🎲 ˊˎ No Game No Life ꒱", "꒰꒰ 🌠 ˊˎ Sword Art Online ꒱", "꒰꒰ 🐺 ˊˎ Wolf's Rain ꒱",
    "꒰꒰ 🧩 ˊˎ Classroom of the Elite ꒱", "꒰꒰ 💎 ˊˎ Land of the Lustrous ꒱", "꒰꒰ 🌿 ˊˎ The Ancient Magus' Bride ꒱", "꒰꒰ 🌙 ˊˎ Sailor Moon ꒱",
    "꒰꒰ 🧸 ˊˎ Kuma Kuma Bear ꒱", "꒰꒰ 🍰 ˊˎ Food Wars ꒱", "꒰꒰ 🎹 ˊˎ Forest of Piano ꒱", "꒰꒰ 🐈 ˊˎ Natsume's Book of Friends ꒱",
    "꒰꒰ 👑 ˊˎ The Eminence in Shadow ꒱", "꒰꒰ 🌻 ˊˎ Summer Time Rendering ꒱", "꒰꒰ 🧠 ˊˎ Monster ꒱", "꒰꒰ 🏹 ˊˎ Fate Stay Night ꒱",
    "꒰꒰ ⚡ ˊˎ A Certain Scientific Railgun ꒱", "꒰꒰ 🎨 ˊˎ Blue Period ꒱", "꒰꒰ 📚 ˊˎ Bungou Stray Dogs ꒱", "꒰꒰ 🌹 ˊˎ Rose of Versailles ꒱",
    "꒰꒰ 🧵 ˊˎ Kill la Kill ꒱", "꒰꒰ 🧊 ˊˎ Free ꒱", "꒰꒰ 🕊️ ˊˎ Angel Beats ꒱", "꒰꒰ 🌧️ ˊˎ Weathering With You ꒱",
    "꒰꒰ ☂️ ˊˎ Garden of Words ꒱", "꒰꒰ ☕ ˊˎ Blend S ꒱", "꒰꒰ 🍀 ˊˎ Black Clover ꒱", "꒰꒰ 🧙 ˊˎ Little Witch Academia ꒱",
    "꒰꒰ 🌼 ˊˎ Yona of the Dawn ꒱", "꒰꒰ 🎀 ˊˎ Cardcaptor Sakura ꒱", "꒰꒰ 🚬 ˊˎ Cowboy Bebop ꒱", "꒰꒰ 🤍 ˊˎ White Album 2 ꒱",
    "꒰꒰ 🪄 ˊˎ Mashle ꒱", "꒰꒰ 🫧 ˊˎ Bubble ꒱", "꒰꒰ 🛰️ ˊˎ Astra Lost in Space ꒱", "꒰꒰ 💥 ˊˎ Mob Psycho 100 ꒱",
    "꒰꒰ 🕯️ ˊˎ Hell Girl ꒱", "꒰꒰ 🐾 ˊˎ Beastars ꒱", "꒰꒰ 🎯 ˊˎ Assassination Classroom ꒱", "꒰꒰ 🌍 ˊˎ To Your Eternity ꒱",
    "꒰꒰ 🍭 ˊˎ Noragami ꒱", "꒰꒰ 🛸 ˊˎ Gintama ꒱", "꒰꒰ 🕰️ ˊˎ Erased ꒱", "꒰꒰ 🪶 ˊˎ Princess Tutu ꒱",
    "꒰꒰ 🧶 ˊˎ Komi Can't Communicate ꒱", "꒰꒰ 🌺 ˊˎ A Sign of Affection ꒱", "꒰꒰ 🐇 ˊˎ Is the Order a Rabbit ꒱", "꒰꒰ 🎮 ˊˎ Log Horizon ꒱",
    "꒰꒰ 🍜 ˊˎ Toriko ꒱", "꒰꒰ ✨ ˊˎ Magi ꒱", "꒰꒰ 🧭 ˊˎ Vinland Saga ꒱", "꒰꒰ 🔮 ˊˎ The Apothecary Diaries ꒱",
    "꒰꒰ 🏴 ˊˎ Black Lagoon ꒱", "꒰꒰ 🥁 ˊˎ Given ꒱", "꒰꒰ 🌤️ ˊˎ Barakamon ꒱", "꒰꒰ 🦊 ˊˎ Spice and Wolf ꒱",
    "꒰꒰ 🌟 ˊˎ Love Live ꒱", "꒰꒰ 🐧 ˊˎ Mawaru Penguindrum ꒱", "꒰꒰ 🍥 ˊˎ Blue Exorcist ꒱", "꒰꒰ 💐 ˊˎ Fruits Basket ꒱",
    "꒰꒰ 🪼 ˊˎ Jellyfish Can't Swim in the Night ꒱", "꒰꒰ 🎬 ˊˎ Millennium Actress ꒱", "꒰꒰ 🐦 ˊˎ Charlotte ꒱", "꒰꒰ 🕹️ ˊˎ The World God Only Knows ꒱",
    "꒰꒰ 🌹 ˊˎ Revolutionary Girl Utena ꒱", "꒰꒰ 🌱 ˊˎ Mushishi ꒱", "꒰꒰ 🍁 ˊˎ Dororo ꒱", "꒰꒰ 🩶 ˊˎ Parasyte ꒱",
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
    embed.set_footer(text=f"Sayfa {sayfa + 1}/{max(1, (len(roller) + 23) // 24)} • Toplam {len(roller)} anime rolu")
    return embed


class AnimeRolSecPersistent(discord.ui.Select):
    def __init__(self, guild_id: int, rol_idleri: list[int], sayfa: int):
        self.guild_id = guild_id
        self.rol_idleri = rol_idleri
        self.sayfa = sayfa
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
            placeholder=f"Anime rol(ler)i sec • Sayfa {sayfa + 1}",
            min_values=1,
            max_values=max(1, len(secenekler)),
            options=secenekler,
            custom_id=f"anime_rol_sec_{guild_id}_{sayfa}",
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
            secenekler.append(discord.SelectOption(label="Renk Kaldır", value="clear", description="Üzerindeki renk rollerini temizler"))
            super().__init__(placeholder="Kendine bir renk rolü seç", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            mevcut_renkler = [rol for rol in roller if rol in interaction.user.roles]
            if mevcut_renkler:
                await interaction.user.remove_roles(*mevcut_renkler, reason="Renk secimi guncellendi")
            if self.values[0] == "clear":
                await interaction.response.send_message("Üzerindeki renk rolleri temizlendi.", ephemeral=True)
                return
            yeni_rol = interaction.guild.get_role(int(self.values[0]))
            if yeni_rol:
                await interaction.user.add_roles(yeni_rol, reason="Renk paneli secimi")
                await interaction.response.send_message(f"Yeni rengin başarıyla {yeni_rol.mention} olarak ayarlandı.", ephemeral=True)

    class RenkView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.add_item(RenkSec())

    rol_listesi = "\n".join(f"`{i+1}.` {rol.mention}" for i, rol in enumerate(roller[:12]))
    embed = discord.Embed(
        title="Renk Rolü Seçim Menüsü",
        description=(
            "Aşağıdaki menüden sunucuda kullanmak istediğin renk rolünü seçebilirsin.\n"
            "Yeni bir renk seçtiğinde eski renk rollerin otomatik kaldırılır."
        ),
        color=RENKLER["rol"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Nasıl Çalışır?", value="Menüden bir renk seç.\nİstersen `Renk Kaldır` ile tüm renk rollerini temizle.", inline=False)
    embed.add_field(name="Kullanılabilir Roller", value=rol_listesi if rol_listesi else "Rol bulunamadı.", inline=False)
    embed.set_footer(text=f"Toplam {len(roller)} renk rolü • {ctx.guild.name}")
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    mesaj = await ctx.send(embed=embed, view=globals()["RenkView"](ctx.guild.id, [rol.id for rol in roller]))
    renk_panel_mesaji_ekle(ctx.guild.id, ctx.channel.id, mesaj.id)


# ═══════════════════════════════════════════════════════════════
#  LEVEL + HOSGELDIN SISTEMI (EK BLOK)
# ═══════════════════════════════════════════════════════════════

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
        embed.set_footer(text=f"Sayfa {sayfa + 1}/{max(1, (len(roller) + 23) // 24)} • Toplam {len(roller)} anime rolu")
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
            super().__init__(placeholder=f"Anime rolu sec • Sayfa {sayfa + 1}", min_values=1, max_values=1, options=secenekler)

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
        embed.set_footer(text=f"Sayfa {sayfa + 1}/{max(1, (len(roller) + 23) // 24)} • Toplam {len(roller)} anime rolu")
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
            super().__init__(placeholder=f"Anime rol(ler)i sec • Sayfa {sayfa + 1}", min_values=1, max_values=max(1, len(secenekler)), options=secenekler)

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
        "mesaj": veri.get("mesaj", "Aramıza hoş geldin {username}. Seninle birlikte {member_count} kişiyiz."),
    }


def _karsilama_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "karsilama_sistemi", veri)


TURKCE_KUFUR_LISTESI = [
    "amk", "aq", "amına", "amina", "amına koyim", "amina koyim", "amına koyayım", "amina koyayim",
    "orospu", "orospu çocuğu", "orospu cocugu", "oc", "piç", "pic", "sikik", "sikerim", "sikiyim",
    "siktir", "siktir git", "yarrak", "yarak", "göt", "got", "götveren", "gotveren", "ibne", "amcık",
    "amcik", "pezevenk", "kahpe", "puşt", "pust", "ananı", "ananı sikeyim", "anani", "bok", "boktan",
    "salak orospu", "gerizekalı", "gerizekali", "piç kurusu", "ebenin", "ebesinin", "gavat", "mallık",
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
    uyari_verildi = sonuc["uyari_verildi"]

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
            title="Güvenlik Uyarısı",
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
        title="Güvenlik Sistemi Tetiklendi",
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
        title="Hoş Geldin!",
        description=_sablon_doldur(ayar.get("mesaj", "Hoş geldin {member_mention}!"), uye),
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
        ayar.get("mesaj", "Aramıza hoş geldin {username}. Seninle birlikte {member_count} kişiyiz."),
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
        title=f"{hedef.display_name} • Profil",
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
    e.set_footer(text=f"{ctx.guild.name} • {zaman_damgasi()}")
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


@bot.command(name="karsilamadurum", aliases=["karşılama-durum", "karsilama-durum"])
async def karsilama_durum(ctx):
    ayar = _karsilama_ayar_al(ctx.guild.id)
    kanal = ctx.guild.get_channel(ayar.get("kanal_id")) if ayar.get("kanal_id") else None
    e = discord.Embed(title="Karşılama Mesajı Sistemi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    e.add_field(name="Kanal", value=kanal.mention if kanal else "Ayarlanmamış", inline=False)
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


# ─────────────────────────────────────────
#  MODAL TABANLI LEVEL / HOSGELDIN KURULUMU
# ─────────────────────────────────────────

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
        default="Aramıza hoş geldin {username}. Seninle birlikte {member_count} kişiyiz."
    )

    async def on_submit(self, interaction: discord.Interaction):
        kanal_id = _kanal_id_coz(self.kanal_id.value)
        if kanal_id is None:
            await interaction.response.send_message("Geçersiz kanal ID girdin.", ephemeral=True)
            return

        kanal = interaction.guild.get_channel(kanal_id) if interaction.guild else None
        if not isinstance(kanal, discord.TextChannel):
            await interaction.response.send_message("Bu ID ile metin kanalı bulunamadı.", ephemeral=True)
            return

        ayar = _karsilama_ayar_al(interaction.guild.id)
        ayar["kanal_id"] = kanal.id
        ayar["mesaj"] = (self.mesaj.value or "").strip()
        _karsilama_ayar_kaydet(interaction.guild.id, ayar)

        await interaction.response.send_message(
            f"Karşılama mesajı sistemi kaydedildi.\nKanal: {kanal.mention}",
            ephemeral=True
        )

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        try:
            if interaction.response.is_done():
                await interaction.followup.send(f"Karşılama modal hatası: {error}", ephemeral=True)
            else:
                await interaction.response.send_message(f"Karşılama modal hatası: {error}", ephemeral=True)
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
            title="Güvenlik Sistemi Kaydedildi",
            description="Sunucu koruma limitleri modal ile başarıyla kaydedildi.",
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


@bot.command(name="karsilamakur", aliases=["karşılama-kur", "karsilama-kur"])
@commands.has_permissions(manage_guild=True)
async def karsilama_kur_modal(ctx):
    e = discord.Embed(
        title="Karşılama Mesajı Kurulumu",
        description="Aşağıdaki butona tıkla; etiket atmayan karşılama mesajını modal üzerinden kur.",
        color=RENKLER["bilgi"]
    )
    await ctx.send(embed=e, view=_KurulumView("karsilama"))


@bot.command(name="guvenlikkur", aliases=["güvenlikkur"])
@commands.has_permissions(administrator=True)
async def guvenlik_kur_modal(ctx):
    e = discord.Embed(
        title="Güvenlik Sistemi Kurulumu",
        description=(
            "Asagidaki butona tikla ve limitleri modal uzerinden ayarla.\n"
            "Yazdigin limit sayisina ulasilinca kullanici direkt jaile atilir."
        ),
        color=RENKLER["bilgi"]
    )
    await ctx.send(embed=e, view=_KurulumView("guvenlik"))


@bot.command(name="guvenlikdurum", aliases=["güvenlikdurum"])
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
        title="Güvenlik Sistemi",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    e.add_field(name="Durum", value="Aktif" if ayar.get("aktif") else "Kapalı", inline=True)
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


@bot.command(name="guvenlikkapat", aliases=["güvenlikkapat"])
@commands.has_permissions(administrator=True)
async def guvenlik_kapat(ctx):
    ayar = _guvenlik_ayar_al(ctx.guild.id)
    ayar["aktif"] = False
    _guvenlik_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(embed=discord.Embed(
        title="Güvenlik Sistemi Kapatıldı",
        description="Sunucu guvenlik limitleri devre disi birakildi.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    ))


@bot.command(name="guvenlikizin", aliases=["güvenlikizin", "guvenlik-whitelist"])
@commands.has_permissions(administrator=True)
async def guvenlik_izin_ekle(ctx, hedef = None):
    if hedef is None:
        await ctx.send("Kullanım: `.guvenlikizin @uye` veya `.guvenlikizin @rol`")
        return
    hedef_obj = None
    if ctx.message.role_mentions:
        hedef_obj = ctx.message.role_mentions[0]
    elif ctx.message.mentions:
        hedef_obj = ctx.message.mentions[0]
    if hedef_obj is None:
        await ctx.send("Lütfen bir üye veya rol etiketle.")
        return
    ayar = _guvenlik_ayar_al(ctx.guild.id)
    whitelist = list(dict.fromkeys((ayar.get("whitelist_ids", []) or []) + [hedef_obj.id]))
    ayar["whitelist_ids"] = whitelist
    _guvenlik_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(embed=discord.Embed(
        title="Whitelist Güncellendi",
        description=f"{hedef_obj.mention} güvenlik whitelist listesine eklendi.",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    ))


@bot.command(name="guvenlikizinsil", aliases=["güvenlikizinsil", "guvenlik-whitelist-sil"])
@commands.has_permissions(administrator=True)
async def guvenlik_izin_sil(ctx, hedef = None):
    if hedef is None:
        await ctx.send("Kullanım: `.guvenlikizinsil @uye` veya `.guvenlikizinsil @rol`")
        return
    hedef_obj = None
    if ctx.message.role_mentions:
        hedef_obj = ctx.message.role_mentions[0]
    elif ctx.message.mentions:
        hedef_obj = ctx.message.mentions[0]
    if hedef_obj is None:
        await ctx.send("Lütfen bir üye veya rol etiketle.")
        return
    ayar = _guvenlik_ayar_al(ctx.guild.id)
    ayar["whitelist_ids"] = [x for x in (ayar.get("whitelist_ids", []) or []) if x != hedef_obj.id]
    _guvenlik_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(embed=discord.Embed(
        title="Whitelist Güncellendi",
        description=f"{hedef_obj.mention} whitelist listesinden çıkarıldı.",
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
        await ctx.send("Hoşgeldin sistemi için kanal ayarlı değil. `.hosgeldinkur` ile önce kurulum yap.")
        return
    if not isinstance(kanal, discord.TextChannel):
        await ctx.send("Ayarlı hoşgeldin kanalı bulunamadı. `.hosgeldinkur` ile sistemi tekrar kur.")
        return
    try:
        ust_metin, e = _hosgeldin_icerigi_hazirla(hedef, ayar)
        e.title = "Hoş Geldin! (Test)"
        await kanal.send(ust_metin, embed=e)
    except discord.Forbidden:
        await ctx.send("Test mesajı gönderilemedi; botun hoşgeldin kanalında yazma yetkisi yok.")
        return
    except Exception as e:
        await ctx.send(f"Hoşgeldin test mesajı oluşturulurken hata oldu: {e}")
        return

    await ctx.send(f"Hoşgeldin test mesajı {kanal.mention} kanalına gönderildi.", delete_after=8)


@bot.command(name="karsilamatest", aliases=["karşılama-test", "karsilama-test"])
@commands.has_permissions(manage_guild=True)
async def karsilama_test(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    ayar = _karsilama_ayar_al(ctx.guild.id)
    kanal_id = ayar.get("kanal_id")
    kanal = ctx.guild.get_channel(kanal_id) if kanal_id else None

    if not kanal_id:
        await ctx.send("Karşılama sistemi için kanal ayarlı değil. `.karsilamakur` ile önce kurulum yap.")
        return
    if not isinstance(kanal, discord.TextChannel):
        await ctx.send("Ayarlı karşılama kanalı bulunamadı. `.karsilamakur` ile sistemi tekrar kur.")
        return

    try:
        mesaj = _karsilama_mesaji_hazirla(hedef, ayar)
        baslikli_mesaj = f"**Karşılama Mesajı (Test)**\n{mesaj}"
        dosya = await hedef.display_avatar.to_file(filename="karsilama-avatar.png") if hedef.display_avatar else None
        if dosya:
            await kanal.send(baslikli_mesaj, file=dosya)
        else:
            await kanal.send(baslikli_mesaj)
    except discord.Forbidden:
        await ctx.send("Test mesajı gönderilemedi; botun karşılama kanalında yazma yetkisi yok.")
        return
    except Exception as e:
        await ctx.send(f"Karşılama test mesajı oluşturulurken hata oldu: {e}")
        return

    await ctx.send(f"Karşılama test mesajı {kanal.mention} kanalına gönderildi.", delete_after=8)


# ── Partner Koruma Sistemleri ─────────────────────────────────────

# Everyone/Here koruması için veri deposu
_everyone_here_log = {}
# Spam koruması için veri deposu (mesaj içerikli)
_spam_log = {}

@bot.event
async def on_message(message):
    # Bot mesajlarını ignore et
    if message.author.bot:
        return
    
    # Mevcut event handler'ları çalıştır
    try:
        await bot.process_commands(message)
    except:
        pass
    
    # Genel güvenlik sistemleri
    ayarlar = ayarlari_yukle()
    gk = str(message.guild.id)
    sunucu_ayari = ayarlar.get(gk, {})

    # Partner kanalı kontrolü
    partner_ch_id = partner_kanal_id_al(message.guild.id)
    if partner_ch_id and message.channel.id == partner_ch_id:
        eslesen = DAVET_REGEX.search(message.content)

        if not eslesen:
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            uyari = await message.channel.send(embed=discord.Embed(
                title="❌ Geçersiz Partner Metni",
                description=f"{message.author.mention} Mesajınızda Discord davet linki bulunamadı. Mesajınız silindi.",
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

        # 1 saat bekleme kontrolü
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
                        title="⏳ Bekleme Süresi Dolmadı",
                        description=(
                            f"{message.author.mention} Bu sunucuyla tekrar partner yapmak için\n"
                            f"**{kalan // 60} dakika {kalan % 60} saniye** beklemeniz gerekiyor.\n"
                            f"Son partner: <@{onceki_id}> tarafından yapıldı."
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
            title="🤝 Yeni Partner Yapıldı!",
            description=f"{message.author.mention} yeni bir partnerlik yaptı!",
            color=0x57F287,
            timestamp=simdi
        )
        stats_embed.add_field(name="📊 Sunucu Sırası", value=f"**#{sira}**", inline=True)
        stats_embed.add_field(name="👤 Yetkili Sırası", value=f"**#{yetkili_sira}** ({yetkili_toplam} partnerlik)", inline=True)
        stats_embed.add_field(
            name="🕐 Zamana Dayalı:",
            value=(
                f"› Günlük: **{stats['gunluk']}**\n"
                f"› Haftalık: **{stats['haftalik']}**\n"
                f"› Aylık: **{stats['aylik']}**"
            ),
            inline=True
        )
        stats_embed.add_field(name="• Toplam", value=f"**{stats['toplam']}**", inline=True)
        stats_embed.set_footer(text=f"{bot.user.name} • Partner Sistemi")
        if message.guild.icon:
            stats_embed.set_thumbnail(url=message.guild.icon.url)
        await message.channel.send(embed=stats_embed)

        log_kanal_id = partner_log_kanali_al(message.guild.id)
        if log_kanal_id:
            log_kanal = message.guild.get_channel(log_kanal_id)
            if log_kanal:
                log_embed = discord.Embed(title="📋 Partner Logu", color=0x57F287, timestamp=simdi)
                log_embed.add_field(name="🔗 Davet", value=f"`{davet_kodu}`", inline=True)
                log_embed.add_field(name="👤 Yapan", value=message.author.mention, inline=True)
                log_embed.add_field(name="📅 Zaman", value=simdi.strftime("%d.%m.%Y %H:%M UTC"), inline=True)
                log_embed.add_field(name="📊 Toplam", value=str(stats["toplam"]), inline=True)
                log_embed.add_field(name="👤 Yetkili Toplamı", value=str(yetkili_toplam), inline=True)
                log_embed.set_footer(text=zaman_damgasi())
                await log_kanal.send(embed=log_embed)
        return

    # Küfür koruması
    if kufur_kontrol(message.guild.id, message.content):
        try:
            await message.delete()
            
            # Embed uyarı gönder
            embed = discord.Embed(
                title="🚫 Küfür Yasak",
                description=f"{message.author.mention} Küfür kullanımı yasaktır!",
                color=0xFF6B6B,
                timestamp=datetime.now(timezone.utc)
            )
            await message.channel.send(embed=embed, delete_after=5)
            
            # Log gönder (varsa)
            log_kanal_id = sunucu_ayari.get("guvenlik_log")
            if log_kanal_id:
                log_kanal = message.guild.get_channel(log_kanal_id)
                if log_kanal:
                    embed = discord.Embed(
                        title="🚫 Küfür Kullanımı",
                        description=f"{message.author.mention} kullanıcısı küfürlü mesaj attı.",
                        color=0xFF6B6B,
                        timestamp=datetime.now(timezone.utc)
                    )
                    embed.add_field(name="Kullanıcı", value=f"{message.author} ({message.author.id})", inline=True)
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

    # Genel spam koruması
    spam_ayar = sunucu_ayari.get("guvenlik_spam_koruma", {})
    if spam_ayar.get("aktif", False):
        user_id = message.author.id
        now = time.time()
        mesaj_icerik = message.content.strip().lower()
        
        # Kullanıcının mesaj geçmişini kontrol et
        if user_id not in _spam_log:
            _spam_log[user_id] = []
        
        _spam_log[user_id].append((now, mesaj_icerik))
        
        # Eski mesajları temizle (1 saatten eski olanlar)
        _spam_log[user_id] = [(t, m) for t, m in _spam_log[user_id] if now - t < 3600]
        
        # Aynı mesaj spam kontrolü
        max_ayni_mesaj = spam_ayar.get("max_ayni_mesaj", 3)
        zaman_araligi = spam_ayar.get("zaman_araligi", 10)
        
        # Son zaman aralığındaki aynı mesajları say
        son_mesajlar = [(t, m) for t, m in _spam_log[user_id] if now - t < zaman_araligi]
        ayni_mesaj_sayisi = sum(1 for t, m in son_mesajlar if m == mesaj_icerik)
        
        if ayni_mesaj_sayisi > max_ayni_mesaj:
            try:
                # Timeout uygula
                mute_suresi = spam_ayar.get("mute_suresi", 300)  # 5 dakika
                
                await message.author.timeout(timedelta(seconds=mute_suresi), reason="Aynı mesaj spam koruması - Genel güvenlik")
                
                # Embed bildirim gönder
                embed = discord.Embed(
                    title="🔇 Spam Cezası",
                    description=f"{message.author.mention} aynı mesajı tekrarladığı için susturuldu!",
                    color=0xFF9500,
                    timestamp=datetime.now(timezone.utc)
                )
                embed.add_field(name="Kullanıcı", value=f"{message.author} ({message.author.id})", inline=True)
                embed.add_field(name="Süre", value=f"{mute_suresi//60} dakika", inline=True)
                embed.add_field(name="Sebep", value=f"{zaman_araligi} saniyede aynı mesaj {ayni_mesaj_sayisi} kez", inline=False)
                await message.channel.send(embed=embed, delete_after=10)
                
                # Log gönder
                log_kanal_id = sunucu_ayari.get("guvenlik_log")
                if log_kanal_id:
                    log_kanal = message.guild.get_channel(log_kanal_id)
                    if log_kanal:
                        embed = discord.Embed(
                            title="🔇 Spam Cezası",
                            description=f"{message.author.mention} aynı mesajı tekrarladığı için susturuldu.",
                            color=0xFF9500,
                            timestamp=datetime.now(timezone.utc)
                        )
                        embed.add_field(name="Kullanıcı", value=f"{message.author} ({message.author.id})", inline=True)
                        embed.add_field(name="Süre", value=f"{mute_suresi//60} dakika", inline=True)
                        embed.add_field(name="Sebep", value=f"{zaman_araligi} saniyede aynı mesaj {ayni_mesaj_sayisi} kez", inline=False)
                        embed.add_field(name="Mesaj", value=f"```{message.content[:100]}...```" if len(message.content) > 100 else f"```{message.content}```", inline=False)
                        await log_kanal.send(embed=embed)
            except discord.Forbidden:
                pass
    
    # Genel link koruması
    link_ayar = sunucu_ayari.get("guvenlik_link_koruma", {})
    if link_ayar.get("aktif", False):
        # Muaf kontrolü
        muaf_roller = link_ayar.get("muaf_roller", [])
        muaf_kanallar = link_ayar.get("muaf_kanallar", [])
        
        # Kullanıcı muaf mı?
        kullanici_muaf = any(role.id in muaf_roller for role in message.author.roles)
        
        # Kanal muaf mı?
        kanal_muaf = message.channel.id in muaf_kanallar
        
        if not kullanici_muaf and not kanal_muaf:
            # Link kontrolü (basit regex)
            import re
            link_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
            if re.search(link_pattern, message.content):
                try:
                    await message.delete()
                    
                    # Embed hata mesajı
                    embed = discord.Embed(
                        title="🚫 Link Paylaşımı Yasak",
                        description=f"{message.author.mention} Link paylaşımı yasaktır!",
                        color=0xFF6B6B,
                        timestamp=datetime.now(timezone.utc)
                    )
                    await message.channel.send(embed=embed, delete_after=5)
                    
                    # Log gönder
                    log_kanal_id = sunucu_ayari.get("guvenlik_log")
                    if log_kanal_id:
                        log_kanal = message.guild.get_channel(log_kanal_id)
                        if log_kanal:
                            embed = discord.Embed(
                                title="🚫 Link Paylaşımı",
                                description=f"{message.author.mention} kullanıcısı link paylaştı.",
                                color=0xFF6B6B,
                                timestamp=datetime.now(timezone.utc)
                            )
                            embed.add_field(name="Kullanıcı", value=f"{message.author} ({message.author.id})", inline=True)
                            embed.add_field(name="Kanal", value=message.channel.mention, inline=True)
                            embed.add_field(name="Mesaj", value=f"```{message.content[:100]}...```" if len(message.content) > 100 else f"```{message.content}```", inline=False)
                            await log_kanal.send(embed=embed)
                except discord.Forbidden:
                    pass
    
    # ── Genel Güvenlik Komutları ─────────────────────────────────────

# ── Modal Sınıfları ─────────────────────────────────────
class SpamModal(discord.ui.Modal, title="Spam Koruma Ayarları"):
    max_ayni_mesaj = discord.ui.TextInput(
        label="Maksimum Aynı Mesaj",
        placeholder="Örn: 3 (10 saniyede aynı mesajdan en fazla 3 kez)",
        style=discord.TextStyle.short,
        required=True,
        default="3"
    )
    zaman_araligi = discord.ui.TextInput(
        label="Zaman Aralığı (saniye)",
        placeholder="Örn: 10",
        style=discord.TextStyle.short,
        required=True,
        default="10"
    )
    mute_suresi = discord.ui.TextInput(
        label="Mute Süresi (saniye)",
        placeholder="Örn: 300 (5 dakika)",
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
                "mute_suresi": sure
            }
            
            ayarlari_kaydet(ayarlar)
            
            embed = discord.Embed(
                title="✅ Spam Koruma Ayarlandı",
                description="Spam yapan kullanıcılara otomatik timeout uygulanacak.",
                color=RENKLER["basari"],
                timestamp=datetime.now(timezone.utc)
            )
            embed.add_field(name="Max Aynı Mesaj", value=f"**{max_msg}** mesaj", inline=True)
            embed.add_field(name="Zaman Aralığı", value=f"**{zaman}** saniye", inline=True)
            embed.add_field(name="Mute Süresi", value=f"**{sure//60}** dakika", inline=True)
            
            await interaction.response.send_message(embed=embed, ephemeral=True)
            
        except ValueError:
            await interaction.response.send_message("Lütfen tüm alanlara geçerli sayılar girin!", ephemeral=True)

class SpamModalView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label="🛡️ Modal Aç", style=discord.ButtonStyle.primary)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = SpamModal()
        await interaction.response.send_modal(modal)

class LinkModal(discord.ui.Modal, title="Link Koruma Ayarları"):
    aktif_mi = discord.ui.TextInput(
        label="Link Koruma Aktif? (evet/hayır)",
        placeholder="Örn: evet",
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
        
        aktif = self.aktif_mi.value.lower() in ["evet", "aktif", "true", "1", "aç"]
        sunucu_ayari["guvenlik_link_koruma"]["aktif"] = aktif
        
        if "muaf_roller" not in sunucu_ayari["guvenlik_link_koruma"]:
            sunucu_ayari["guvenlik_link_koruma"]["muaf_roller"] = []
        if "muaf_kanallar" not in sunucu_ayari["guvenlik_link_koruma"]:
            sunucu_ayari["guvenlik_link_koruma"]["muaf_kanallar"] = []
        
        ayarlari_kaydet(ayarlar)
        
        embed = discord.Embed(
            title="✅ Link Koruma Ayarlandı",
            description=f"Link koruması {'aktif' if aktif else 'pasif'} durumuna ayarlandı.\n\nMuaf roller eklemek için: `.link-koruma-muaf-rol @rol`\nMuaf kanallar eklemek için: `.link-koruma-muaf-kanal #kanal`",
            color=RENKLER["basari"] if aktif else RENKLER["hata"],
            timestamp=datetime.now(timezone.utc)
        )
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

class LinkModalView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label="🔗 Modal Aç", style=discord.ButtonStyle.primary)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = LinkModal()
        await interaction.response.send_modal(modal)


# ── Genel Güvenlik Komutları ─────────────────────────────────────

@bot.command(name="spam-koruma-kur")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_kur(ctx):
    """Genel spam korumasını modal ile kurar."""
    await ctx.send("Modal açmak için butona tıklayın:", view=SpamModalView())

@bot.command(name="link-koruma-kur")
@commands.has_permissions(manage_guild=True)
async def link_koruma_kur(ctx):
    """Genel link korumasını modal ile kurar."""
    await ctx.send("Modal açmak için butona tıklayın:", view=LinkModalView())

@bot.command(name="link-koruma-aktif")
@commands.has_permissions(manage_guild=True)
async def link_koruma_aktif(ctx):
    """Genel link korumasını aktif eder."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.setdefault(gk, {})
    
    if "guvenlik_link_koruma" not in sunucu_ayari:
        sunucu_ayari["guvenlik_link_koruma"] = {}
    
    sunucu_ayari["guvenlik_link_koruma"]["aktif"] = True
    ayarlari_kaydet(ayarlar)
    
    embed = discord.Embed(
        title="✅ Genel Link Koruma Aktif",
        description="Tüm kanallarda link paylaşımı engellendi (muaf olanlar hariç).",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    await ctx.send(embed=embed)

@bot.command(name="link-koruma-kapat")
@commands.has_permissions(manage_guild=True)
async def link_koruma_kapat(ctx):
    """Genel link korumasını kapatır."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.setdefault(gk, {})
    
    if "guvenlik_link_koruma" in sunucu_ayari:
        sunucu_ayari["guvenlik_link_koruma"]["aktif"] = False
        ayarlari_kaydet(ayarlar)
    
    embed = discord.Embed(
        title="❌ Genel Link Koruma Kapatıldı",
        description="Link paylaşımı serbest bırakıldı.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    await ctx.send(embed=embed)

@bot.command(name="link-koruma-muaf-rol")
@commands.has_permissions(manage_guild=True)
async def link_koruma_muaf_rol(ctx, rol: discord.Role):
    """Link korumasından muaf rol ekler."""
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
            title="✅ Muaf Rol Eklendi",
            description=f"{rol.mention} rolü link korumasından muaf tutuldu.",
            color=RENKLER["basari"],
            timestamp=datetime.now(timezone.utc)
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu rol zaten muaf listesinde!")

@bot.command(name="link-koruma-muaf-kanal")
@commands.has_permissions(manage_guild=True)
async def link_koruma_muaf_kanal(ctx, kanal: discord.TextChannel):
    """Link korumasından muaf kanal ekler."""
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
            title="✅ Muaf Kanal Eklendi",
            description=f"{kanal.mention} kanalı link korumasından muaf tutuldu.",
            color=RENKLER["basari"],
            timestamp=datetime.now(timezone.utc)
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu kanal zaten muaf listesinde!")

@bot.command(name="link-koruma-durum")
@commands.has_permissions(manage_guild=True)
async def link_koruma_durum(ctx):
    """Genel link koruma durumunu gösterir."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.get(gk, {})
    link_ayar = sunucu_ayari.get("guvenlik_link_koruma", {})
    
    embed = discord.Embed(
        title="🔗 Genel Link Koruma Durumu",
        color=0x5865F2,
        timestamp=datetime.now(timezone.utc)
    )
    
    durum = "✅ Aktif" if link_ayar.get("aktif", False) else "❌ Pasif"
    embed.add_field(name="Durum", value=durum, inline=True)
    
    muaf_roller = link_ayar.get("muaf_roller", [])
    muaf_kanallar = link_ayar.get("muaf_kanallar", [])
    
    if muaf_roller:
        roller_text = "\n".join([f"<@&{rid}>" for rid in muaf_roller[:5]])
        if len(muaf_roller) > 5:
            roller_text += f"\n...ve {len(muaf_roller)-5} rol daha"
        embed.add_field(name="🎭 Muaf Roller", value=roller_text or "Yok", inline=False)
    
    if muaf_kanallar:
        kanallar_text = "\n".join([f"<#{kid}>" for kid in muaf_kanallar[:5]])
        if len(muaf_kanallar) > 5:
            kanallar_text += f"\n...ve {len(muaf_kanallar)-5} kanal daha"
        embed.add_field(name="📢 Muaf Kanallar", value=kanallar_text or "Yok", inline=False)
    
    await ctx.send(embed=embed)


bot.remove_command("kufur-temizle")


@bot.command(name="kufur-temizle")
@commands.has_permissions(administrator=True)
async def kufur_temizle_v2(ctx):
    guild_key = str(ctx.guild.id)
    ayarlar = ayarlari_yukle()
    if guild_key not in ayarlar or not ayarlar[guild_key].get("yasakli_kelimeler"):
        await ctx.send("Bu sunucuda zaten küfür koruması ayarlanmamış.")
        return
    ayarlar[guild_key]["yasakli_kelimeler"] = []
    ayarlari_kaydet(ayarlar)
    await ctx.send(embed=discord.Embed(
        title="Kufur Koruması Temizlendi",
        description="Tum yasak kelimeler silindi ve kufur korumasi kapatildi.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    ))


class GifCevapModal(discord.ui.Modal, title="GIF Cevap Kurulumu"):
    anahtar = discord.ui.TextInput(label="Anahtar Kelime", placeholder="ornek: günaydın", required=True, max_length=100)
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
        ayar = _jail_ayar_al(interaction.guild.id)
        ayar.update({"aktif": True, "kanal_id": kanal.id, "jail_rol_id": jail_rol.id, "jail_yetki_rol_id": yetki_rol.id, "kayitlar": ayar.get("kayitlar", {})})
        _jail_ayar_kaydet(interaction.guild.id, ayar)
        await interaction.response.send_message(f"Jail sistemi kaydedildi. Kanal: {kanal.mention} • Jail Rol: {jail_rol.mention}", ephemeral=True)


def _jail_yetkili_mi(uye: discord.Member, guild_id: int) -> bool:
    ayar = _jail_ayar_al(guild_id)
    yetki_rol_id = ayar.get("jail_yetki_rol_id")
    return bool(yetki_rol_id and any(rol.id == yetki_rol_id for rol in uye.roles))


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

    for kanal in guild.channels:
        try:
            await kanal.set_permissions(uye, view_channel=False, send_messages=False, reason="Jail sistemi")
        except Exception:
            pass
    try:
        await jail_kanal.set_permissions(uye, view_channel=True, send_messages=True, read_message_history=True, reason="Jail sistemi")
    except Exception:
        pass

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
    for kanal in ctx.guild.channels:
        try:
            await kanal.set_permissions(uye, overwrite=None, reason="Jail kaldirildi")
        except Exception:
            pass
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


for _eski in ("yardim", "help", "yardım", "ban"):
    try:
        bot.remove_command(_eski)
    except Exception:
        pass


def _komut_sahibi_degisebilir_mi(interaction: discord.Interaction, sahibi_id: int) -> bool:
    return interaction.user.id == sahibi_id


@bot.command(name="yardim", aliases=["yardım", "help"])
async def yardim_final(ctx):
    komutlar = _yardim_komutlarini_topla()
    sistem_haritasi = _yardim_sistem_haritasi()
    sahibi_id = ctx.author.id

    def temel_embed(baslik: str, aciklama: str) -> discord.Embed:
        embed = discord.Embed(
            title=f"Komut Paneli • {baslik}",
            description=aciklama,
            color=0x20253A,
            timestamp=datetime.now(timezone.utc)
        )
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
            embed.set_author(name=f"{ctx.guild.name} Komutlar", icon_url=ctx.guild.icon.url)
        else:
            embed.set_author(name=f"{ctx.guild.name} Komutlar")
        embed.set_footer(text=f"Toplam {sum(len(v) for v in komutlar.values())} komut • Secici menu aktif")
        return embed

    def ana_embed():
        embed = temel_embed("Ana Menu", "Asagidaki secicilerle kategorileri ve sistemleri gezebilirsin.")
        kategori_ozet = [f"• **{kategori}** `({len(kayitlar)})`" for kategori, kayitlar in komutlar.items() if kayitlar]
        embed.add_field(name="Kategoriler", value="\n".join(kategori_ozet[:8]) or "-", inline=True)
        sistem_ozet = []
        for sistem, adlar in sistem_haritasi.items():
            sayi = sum(1 for liste in komutlar.values() for kayit in liste if kayit["ad"] in adlar)
            sistem_ozet.append(f"• **{sistem}** `({sayi})`")
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
    embed = mod_embed("🔨 Uye Banlandi", RENKLER["ban"], **{
        "👤 Hedef": hedef_yazi,
        "📝 Sebep": sebep,
        "🛡️ Yetkili": ctx.author.mention
    })
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "ban_log", embed)


for _eski_help in ("yardim", "help", "yardım"):
    try:
        bot.remove_command(_eski_help)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardım", "help"])
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
        embed.add_field(name="Kategoriler", value=" • ".join(kategori_ozet[:8]) or "-", inline=False)
        embed.add_field(name="Sistemler", value=" • ".join(sistem_ozet[:7]) or "-", inline=False)
        embed.add_field(name="Hizli Baslangic", value=".profil • .ticketpanel • .levelkur • .gifcevap • .jailkur", inline=False)
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
    return "Bot çalışıyor"

def run_flask():
    port = int(os.environ.get("PORT", 10000))  # Render için 10000
    app.run(host="0.0.0.0", port=port)

Thread(target=run_flask).start()


if __name__ == "__main__":
    bot.run(BOT_TOKEN)


for _eski_help2 in ("yardim", "help", "yardım"):
    try:
        bot.remove_command(_eski_help2)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardım", "help"])
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
        "Eglence": "m:eğlence",
        "Slash": "m:slash",
        "Diger": "m:komutlar",
    }
    kategori_renkleri = {
        "Ayarlar": "⬛",
        "Moderasyon": "🟩",
        "Roller": "🟥",
        "Sistemler": "🟦",
        "Kullanici": "🟪",
        "Eglence": "🟨",
        "Slash": "🟧",
        "Diger": "🌈",
    }
    sistem_gosterimleri = {
        "Log": "🧾 log",
        "Ticket": "🎟 destek",
        "Partner": "🤝 partner",
        "Level": "⚙ /rank",
        "Hosgeldin": "🎉 karşılama",
        "Guvenlik": "🛡 koruma",
        "Rol Panelleri": "🎨 roller",
        "Eglence": "🎊 çekiliş",
        "Moderasyon": "🔨 mod",
    }
    kullanici_sistemleri = [
        "👤 profil",
        "📊 seviye",
        "🌙 afk",
        "🏠 sunucu",
        "🎁 çekiliş",
        "🖼 gifcevap",
        "🔒 jail",
        "🧹 rolidler",
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
        embed.set_footer(text=f"Toplam {sum(len(v) for v in komutlar.values())} komut • {zaman_damgasi()}")
        return embed

    def ana_embed():
        embed = temel_embed("Marpel Komutlar")
        kategori_satirlari = []
        toplam = sum(len(v) for v in komutlar.values())
        kategori_satirlari.append(f"🌈 **m:komutlar** ({toplam})")
        for kategori in kategori_sirasi:
            if komutlar.get(kategori):
                kategori_satirlari.append(f"{kategori_renkleri.get(kategori, '▫️')} **{kategori_etiketleri.get(kategori, kategori.lower())}** ({len(komutlar[kategori])})")
        embed.add_field(name="📋 Kategoriler", value="\n".join(kategori_satirlari[:6]), inline=True)
        embed.add_field(name="👑", value="ㅤ", inline=True)

        sol = []
        for sistem in ["Eglence", "Guvenlik", "Log", "Ticket", "Rol Panelleri"]:
            if sistem in sistem_gosterimleri:
                sol.append(sistem_gosterimleri[sistem])
        sag = kullanici_sistemleri
        embed.add_field(name="🛠 Sistemler", value="\n".join(sol[:8]), inline=True)
        embed.add_field(name="👥 Kullanıcı Sistemleri", value="\n".join(sag[:8]), inline=True)
        return embed

    def detay_embed(baslik: str, kayitlar: list[dict], aciklama: str):
        embed = temel_embed(f"Marpel Komutlar", aciklama)
        embed.add_field(name=baslik, value="\n\n".join(_yardim_parcalari(_yardim_komut_metni(kayitlar), limit=850)[:3]) or "Komut bulunamadi.", inline=False)
        return embed

    class KategoriSec(discord.ui.Select):
        def __init__(self):
            secenekler = []
            tum = sum(len(v) for v in komutlar.values())
            secenekler.append(discord.SelectOption(label="Tüm Komutlar", value="__tum__", description=f"{tum} komut"))
            for kategori in kategori_sirasi:
                if komutlar.get(kategori):
                    secenekler.append(discord.SelectOption(
                        label=kategori,
                        value=kategori,
                        description=f"{len(komutlar[kategori])} komut",
                        emoji="📁"
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
                await interaction.response.edit_message(embed=detay_embed("Tüm Komutlar", tum, "Sunucudaki tüm aktif komutlar."), view=view)
                return
            await interaction.response.edit_message(embed=detay_embed(self.values[0], komutlar.get(self.values[0], []), "Seçtiğin kategorideki komutlar."), view=view)

    class SistemSec(discord.ui.Select):
        def __init__(self):
            secenekler = [discord.SelectOption(label=sistem, value=sistem, description="Sistem komutlarini gosterir", emoji="⚙️") for sistem in sistem_haritasi]
            super().__init__(placeholder="Sistemler", min_values=1, max_values=1, options=secenekler, row=2)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            kayitlar = []
            for liste in komutlar.values():
                kayitlar.extend([kayit for kayit in liste if kayit["ad"] in sistem_haritasi.get(self.values[0], set())])
            kayitlar.sort(key=lambda x: x["gosterim"])
            await interaction.response.edit_message(embed=detay_embed(f"{self.values[0]} Sistemi", kayitlar, "Seçtiğin sistemle ilgili komutlar."), view=view)

    class YardimMenuSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label="Ana Menü", value="ana", description="İlk görünümü aç"),
                discord.SelectOption(label="Hızlı Başlangıç", value="hizli", description="En sık kullanılan komutlar"),
            ]
            super().__init__(placeholder="Yardım Menüsü", min_values=1, max_values=1, options=secenekler, row=3)

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
            await interaction.response.edit_message(embed=detay_embed("Hızlı Başlangıç", hizli, "En sık kullanılan kurulum komutları."), view=view)

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
