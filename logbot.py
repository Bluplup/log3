import asyncio
import json
import os
import random
import re
import threading
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import discord
from discord.ext import commands
from flask import Flask, jsonify


BASE_DIR = Path(__file__).resolve().parent
SETTINGS_FILE = BASE_DIR / "settings.json"

TOKEN = os.getenv("DISCORD_TOKEN") or os.getenv("BOT_TOKEN") or "BURAYA_BOT_TOKEN_YAZ"
PREFIX = os.getenv("BOT_PREFIX", ".")

if not TOKEN or TOKEN == "BURAYA_BOT_TOKEN_YAZ":
    raise ValueError("DISCORD_TOKEN veya BOT_TOKEN env ayarla ya da logbot.py icindeki token alanini doldur.")


# Tüm Embed Renkleri Pembe (Hot Pink)
PEMBE = 0xFF69B4

RENK = {
    "basari": PEMBE,
    "hata": PEMBE,
    "bilgi": PEMBE,
    "uyari": PEMBE,
    "mod": PEMBE,
    "mute": PEMBE,
}

LOG_TURLERI = {
    "ban_log": "Ban / Unban Logu",
    "mute_log": "Mute / Susturma Logu",
    "mod_log": "Moderasyon Logu",
    "rol_log": "Rol Değişiklikleri Logu",
    "mesaj_log": "Mesaj İşlemleri Logu",
    "giris_cikis": "Giriş / Çıkış Logu",
    "ses_log": "Ses Kanalları Logu",
    "kanal_log": "Kanal İşlemleri Logu",
    "davet_log": "Davet Logu",
}

VARSAYILAN_LOG_KANALLARI = {
    "ban_log": 1484564146111647917,
    "mute_log": 1484564329549267104,
    "mod_log": 1484564481257508874,
    "rol_log": 1484564569446944949,
    "mesaj_log": 1484564647704137879,
    "kanal_log": 1484565700969496606,
    "ses_log": 1484564774648938496,
    "davet_log": 1484564912486355106,
}

KUFUR_KELIMELERI = {
    "amk", "aq", "oc", "orospu", "pic", "piç", "siktir", "yarrak", "yarak", "got", "göt", "ibne",
    "kahpe", "gavat", "pezevenk", "mal", "salak",
}

LINK_REGEX = re.compile(r"(https?://|www\.|discord\.gg/|discord\.com/invite/)", re.I)
URL_REGEX = re.compile(r"(https?://\S+)", re.I)

settings_lock = threading.RLock()
settings_cache = None


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def timestamp() -> str:
    return utc_now().strftime("%d.%m.%Y %H:%M UTC")


def load_settings() -> dict:
    global settings_cache
    with settings_lock:
        if settings_cache is not None:
            return json.loads(json.dumps(settings_cache))
        if not SETTINGS_FILE.exists():
            settings_cache = {}
            save_settings(settings_cache)
            return {}
        try:
            with SETTINGS_FILE.open("r", encoding="utf-8") as f:
                settings_cache = json.load(f)
        except json.JSONDecodeError:
            settings_cache = {}
        return json.loads(json.dumps(settings_cache))


def save_settings(data: dict) -> None:
    global settings_cache
    with settings_lock:
        SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
        tmp = SETTINGS_FILE.with_suffix(".json.tmp")
        with tmp.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, SETTINGS_FILE)
        settings_cache = json.loads(json.dumps(data))


def update_settings(func):
    with settings_lock:
        data = load_settings()
        result = func(data)
        save_settings(data)
        return result


def guild_data(guild_id: int) -> dict:
    data = load_settings()
    return data.setdefault(str(guild_id), {})


def guild_section(guild_id: int, key: str, default):
    return guild_data(guild_id).get(key, default)


def set_guild_section(guild_id: int, key: str, value) -> None:
    def edit(data):
        data.setdefault(str(guild_id), {})[key] = value
    update_settings(edit)


def embed(title: str, description: str = "", color: int = PEMBE) -> discord.Embed:
    e = discord.Embed(title=title, description=description, color=PEMBE, timestamp=utc_now())
    e.set_footer(text=timestamp())
    return e


def error_embed(title: str, description: str) -> discord.Embed:
    return embed(title, description, PEMBE)


def usage_embed(text: str) -> discord.Embed:
    return embed("Kullanım Rehberi", text, PEMBE)


def short(text: str, limit: int = 1024) -> str:
    text = str(text or "")
    return text if len(text) <= limit else text[: limit - 3] + "..."


def parse_duration(text: str | None, default_seconds: int = 600) -> int:
    """Varsayılan olarak 600 saniye (10 dakika) döner."""
    if not text:
        return default_seconds
    text = text.strip().lower()
    match = re.fullmatch(r"(\d+)(s|sn|m|dk|h|sa|d|g)?", text)
    if not match:
        raise ValueError("Geçersiz süre biçimi")
    value = int(match.group(1))
    unit = match.group(2) or "m"
    multipliers = {"s": 1, "sn": 1, "m": 60, "dk": 60, "h": 3600, "sa": 3600, "d": 86400, "g": 86400}
    return max(1, min(value * multipliers[unit], 28 * 86400))


def format_duration(seconds: int) -> str:
    seconds = int(seconds)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    parts = []
    if days:
        parts.append(f"{days} gün")
    if hours:
        parts.append(f"{hours} saat")
    if minutes:
        parts.append(f"{minutes} dk")
    if seconds or not parts:
        parts.append(f"{seconds} sn")
    return " ".join(parts)


def role_guard(ctx: commands.Context, target: discord.Member) -> str | None:
    if target.id == ctx.author.id:
        return "Kendiniz üzerinde bu işlemi yapamazsınız."
    if ctx.guild.owner_id != ctx.author.id and target.top_role >= ctx.author.top_role:
        return "Bu üye sizinle aynı veya daha yüksek bir rolde olduğu için işlem yapamazsınız."
    if target.top_role >= ctx.guild.me.top_role:
        return "Botun rolü hedef üyeden yüksek olmadığı için işlem gerçekleştirilemedi."
    return None


def kanal_al(guild_id: int, tur: str) -> int | None:
    data = guild_data(guild_id)
    return data.get(tur) or VARSAYILAN_LOG_KANALLARI.get(tur)


def kanal_kaydet(guild_id: int, tur: str, kanal_id: int) -> None:
    def edit(data):
        data.setdefault(str(guild_id), {})[tur] = kanal_id
    update_settings(edit)


def kanal_sil(guild_id: int, tur: str) -> None:
    def edit(data):
        data.setdefault(str(guild_id), {}).pop(tur, None)
    update_settings(edit)


async def log_gonder(guild: discord.Guild, tur: str, log_embed: discord.Embed) -> None:
    kanal_id = kanal_al(guild.id, tur)
    if not kanal_id:
        return
    kanal = guild.get_channel(int(kanal_id))
    if not isinstance(kanal, discord.TextChannel):
        return
    try:
        await kanal.send(embed=log_embed)
    except (discord.Forbidden, discord.HTTPException):
        pass


async def audit_user(guild: discord.Guild, action: discord.AuditLogAction, target=None):
    try:
        async for entry in guild.audit_logs(limit=6, action=action):
            if target is None:
                return entry.user
            entry_target_id = getattr(getattr(entry, "target", None), "id", None)
            if entry_target_id == getattr(target, "id", None):
                return entry.user
    except (discord.Forbidden, discord.HTTPException):
        return None
    return None


async def hedef_uye_bul(ctx: commands.Context, *args):
    """
    Tüm moderasyon komutları için gelişmiş hedef bulucu:
    1. Yanıtlanan mesaja (reply) bakar.
    2. Etiketlenen kullanıcıya (mention) bakar.
    3. Argümanlar içindeki ID veya Kullanıcı Adı'na bakar.
    Döndürür: (target, kalan_arguman_listesi)
    """
    args_list = list(args)

    # 1. Yanıt (Reply) kontrolü
    if ctx.message.reference and ctx.message.reference.message_id:
        try:
            ref_msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            if ref_msg and ref_msg.author:
                return ref_msg.author, args_list
        except (discord.HTTPException, discord.NotFound):
            pass

    # 2. Mention (Etiket) kontrolü
    if ctx.message.mentions:
        target = ctx.message.mentions[0]
        remaining = [a for a in args_list if not (a.startswith("<@") and a.endswith(">"))]
        return target, remaining

    # 3. Argüman içi ID veya Kullanıcı Adı
    if args_list:
        first_arg = str(args_list[0]).strip()
        clean_id = re.sub(r"\D", "", first_arg)
        if clean_id and len(clean_id) >= 17:
            member = ctx.guild.get_member(int(clean_id))
            if member:
                return member, args_list[1:]
            try:
                fetched = await ctx.guild.fetch_member(int(clean_id))
                return fetched, args_list[1:]
            except (discord.HTTPException, discord.NotFound):
                return discord.Object(id=int(clean_id)), args_list[1:]

        found = discord.utils.find(
            lambda m: m.name.lower() == first_arg.lower() or str(m).lower() == first_arg.lower() or getattr(m, "display_name", "").lower() == first_arg.lower(),
            ctx.guild.members
        )
        if found:
            return found, args_list[1:]

    return None, args_list


intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.bans = True
intents.messages = True
intents.message_content = True
intents.voice_states = True
intents.invites = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, case_insensitive=True, help_command=None)


@bot.command(name="logkur", aliases=["log-kurulum"])
@commands.has_permissions(manage_guild=True)
async def logkur(ctx):
    sayi = 0
    for key in LOG_TURLERI:
        kanal_id = VARSAYILAN_LOG_KANALLARI.get(key)
        if kanal_id:
            kanal_kaydet(ctx.guild.id, key, kanal_id)
            sayi += 1
    await ctx.send(embed=embed("🌸 Otomatik Log Kurulumu", f"**{sayi}** varsayılan log kanalı başarıyla kaydedildi.", PEMBE))


@bot.command(name="log-kur", aliases=["logayarla"])
@commands.has_permissions(manage_guild=True)
async def log_kur(ctx, tur: str = None, kanal: discord.TextChannel = None):
    if tur is None or kanal is None:
        turler = ", ".join(f"`{key}`" for key in LOG_TURLERI)
        await ctx.send(embed=usage_embed(f"`{PREFIX}log-kur <tür> #kanal`\n\nGeçerli Türler: {turler}"))
        return
    tur = tur.strip().lower()
    if tur not in LOG_TURLERI:
        await ctx.send(embed=error_embed("Geçersiz Log Türü", f"`{tur}` desteklenmiyor. `{PREFIX}log-durum` ile türleri görebilirsiniz."))
        return
    kanal_kaydet(ctx.guild.id, tur, kanal.id)
    await ctx.send(embed=embed("🌸 Log Kanalı Ayarlandı", f"**{LOG_TURLERI[tur]}** logları {kanal.mention} kanalına yönlendirildi.", PEMBE))


@bot.command(name="log-kaldir", aliases=["logkaldir"])
@commands.has_permissions(manage_guild=True)
async def log_kaldir(ctx, tur: str = None):
    if tur is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}log-kaldir <tür>`"))
        return
    tur = tur.strip().lower()
    if tur not in LOG_TURLERI:
        await ctx.send(embed=error_embed("Geçersiz Log Türü", f"`{tur}` desteklenmiyor."))
        return
    kanal_sil(ctx.guild.id, tur)
    await ctx.send(embed=embed("🌸 Log Kapatıldı", f"**{LOG_TURLERI[tur]}** için log gönderimi kapatıldı.", PEMBE))


@bot.command(name="log-durum", aliases=["logdurum"])
@commands.has_permissions(manage_guild=True)
async def log_durum(ctx):
    data = guild_data(ctx.guild.id)
    e = embed("🌸 Log Ayarları Durumu", f"**{ctx.guild.name}** sunucusu aktif log yapılandırması:", PEMBE)
    for key, name in LOG_TURLERI.items():
        kanal_id = data.get(key) or VARSAYILAN_LOG_KANALLARI.get(key)
        kanal = ctx.guild.get_channel(int(kanal_id)) if kanal_id else None
        e.add_field(name=f"{name}\n`{key}`", value=kanal.mention if kanal else "Devre Dışı", inline=True)
    await ctx.send(embed=e)


@bot.command(name="ban", aliases=["blupbum", "yasakla"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, *args):
    target, remaining = await hedef_uye_bul(ctx, *args)
    if target is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}ban @üye [sebep]`, `{PREFIX}ban <id> [sebep]` veya bir mesaja yanıt verip `{PREFIX}ban [sebep]`"))
        return

    if isinstance(target, discord.Member):
        guard = role_guard(ctx, target)
        if guard:
            await ctx.send(embed=error_embed("İşlem Engellendi", guard))
            return

    if getattr(target, "id", None) == ctx.author.id:
        await ctx.send(embed=error_embed("İşlem Engellendi", "Kendinizi banlayamazsınız."))
        return

    sebep = " ".join(remaining) if remaining else "Sebep belirtilmedi"
    try:
        await ctx.guild.ban(discord.Object(id=target.id), reason=f"{ctx.author}: {sebep}", delete_message_seconds=0)
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Ban Başarısız", "Botun ban yetkisi veya rol sırası yetersiz."))
        return
    except discord.HTTPException as exc:
        await ctx.send(embed=error_embed("Ban Başarısız", short(exc)))
        return

    target_text = target.mention if isinstance(target, discord.Member) else f"`{target.id}`"
    e = embed("🌸 Üye Banlandı", f"**Hedef:** {target_text}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", PEMBE)
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "ban_log", e)


@bot.command(name="unban", aliases=["yasakkaldır"])
@commands.has_permissions(ban_members=True)
async def unban(ctx, kullanici_id: str = None, *, sebep: str = "Sebep belirtilmedi"):
    if kullanici_id is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}unban <kullanici_id> [sebep]`"))
        return
    clean_id = re.sub(r"\D", "", kullanici_id)
    if not clean_id:
        await ctx.send(embed=error_embed("Geçersiz ID", "Lütfen geçerli bir kullanıcı ID'si girin."))
        return
    target_id = int(clean_id)
    try:
        await ctx.guild.unban(discord.Object(id=target_id), reason=f"{ctx.author}: {sebep}")
    except discord.NotFound:
        await ctx.send(embed=error_embed("Bulunamadı", "Bu ID ban listesinde bulunamadı."))
        return
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Unban Başarısız", "Botun ban kaldırma yetkisi yok."))
        return
    e = embed("🌸 Ban Kaldırıldı", f"**Kullanıcı ID:** `{target_id}`\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", PEMBE)
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "ban_log", e)


@bot.command(name="kick", aliases=["at"])
@commands.has_permissions(kick_members=True)
async def kick(ctx, *args):
    target, remaining = await hedef_uye_bul(ctx, *args)
    if target is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}kick @üye [sebep]` veya mesaja yanıt verip `{PREFIX}kick [sebep]`"))
        return

    if not isinstance(target, discord.Member):
        try:
            target = await ctx.guild.fetch_member(target.id)
        except (discord.HTTPException, AttributeError):
            await ctx.send(embed=error_embed("İşlem Başarısız", "Üye bu sunucuda bulunamadı."))
            return

    guard = role_guard(ctx, target)
    if guard:
        await ctx.send(embed=error_embed("İşlem Engellendi", guard))
        return

    sebep = " ".join(remaining) if remaining else "Sebep belirtilmedi"
    try:
        await target.kick(reason=f"{ctx.author}: {sebep}")
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Kick Başarısız", "Botun yetkisi veya rol sırası yetersiz."))
        return

    e = embed("🌸 Üye Atıldı (Kick)", f"**Hedef:** {target.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", PEMBE)
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mod_log", e)


@bot.command(name="mute", aliases=["timeout", "sustur"])
@commands.has_permissions(moderate_members=True)
async def mute(ctx, *args):
    target, remaining = await hedef_uye_bul(ctx, *args)
    if target is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}mute @üye [süre] [sebep]`\n`{PREFIX}mute <id> [süre] [sebep]` veya mesaja yanıt verip `{PREFIX}mute [süre] [sebep]`\n*(Süre belirtilmezse otomatik **10 dakika** uygulanır)*"))
        return

    if not isinstance(target, discord.Member):
        try:
            target = await ctx.guild.fetch_member(target.id)
        except (discord.HTTPException, AttributeError):
            await ctx.send(embed=error_embed("Susturma Başarısız", "Kullanıcı bu sunucuda bulunamadı."))
            return

    guard = role_guard(ctx, target)
    if guard:
        await ctx.send(embed=error_embed("İşlem Engellendi", guard))
        return

    seconds = 600  # Otomatik Varsayılan 10 Dakika (600 saniye)
    sebep = "Sebep belirtilmedi"

    if remaining:
        try:
            seconds = parse_duration(remaining[0])
            if len(remaining) > 1:
                sebep = " ".join(remaining[1:])
        except ValueError:
            seconds = 600
            sebep = " ".join(remaining)

    until = utc_now() + timedelta(seconds=seconds)
    try:
        await target.timeout(until, reason=f"{ctx.author}: {sebep}")
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Mute Başarısız", "Botun timeout yetkisi veya rol sırası yetersiz."))
        return
    except discord.HTTPException as exc:
        await ctx.send(embed=error_embed("Mute Başarısız", short(exc)))
        return

    e = embed(
        "🌸 Üye Susturuldu",
        f"**Hedef:** {target.mention}\n**Süre:** {format_duration(seconds)}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}",
        PEMBE
    )
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mute_log", e)


@bot.command(name="unmute", aliases=["susturmakaldır", "timeout-kaldır"])
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, *args):
    target, remaining = await hedef_uye_bul(ctx, *args)
    if target is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}unmute @üye [sebep]` veya mesaja yanıt verip `{PREFIX}unmute [sebep]`"))
        return

    if not isinstance(target, discord.Member):
        try:
            target = await ctx.guild.fetch_member(target.id)
        except (discord.HTTPException, AttributeError):
            await ctx.send(embed=error_embed("İşlem Başarısız", "Üye bu sunucuda bulunamadı."))
            return

    sebep = " ".join(remaining) if remaining else "Sebep belirtilmedi"
    try:
        await target.timeout(None, reason=f"{ctx.author}: {sebep}")
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Unmute Başarısız", "Botun yetkisi yetersiz."))
        return
    except discord.HTTPException as exc:
        await ctx.send(embed=error_embed("Unmute Başarısız", short(exc)))
        return

    e = embed("🌸 Mute Kaldırıldı", f"**Hedef:** {target.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", PEMBE)
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mute_log", e)


@bot.command(name="sil", aliases=["temizle", "purge"])
@commands.has_permissions(manage_messages=True)
async def sil(ctx, adet: int = 5):
    adet = max(1, min(adet, 100))
    deleted = await ctx.channel.purge(limit=adet + 1)
    msg = await ctx.send(embed=embed("🌸 Mesajlar Silindi", f"**{max(0, len(deleted) - 1)}** adet mesaj başarıyla temizlendi.", PEMBE))
    await asyncio.sleep(4)
    try:
        await msg.delete()
    except discord.HTTPException:
        pass


def warnings_get(guild_id: int) -> dict:
    return guild_section(guild_id, "warnings", {})


@bot.command(name="warn", aliases=["uyar"])
@commands.has_permissions(manage_messages=True)
async def warn(ctx, *args):
    target, remaining = await hedef_uye_bul(ctx, *args)
    if target is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}warn @üye [sebep]` veya mesaja yanıt verip `{PREFIX}warn [sebep]`"))
        return

    if not isinstance(target, discord.Member):
        try:
            target = await ctx.guild.fetch_member(target.id)
        except (discord.HTTPException, AttributeError):
            await ctx.send(embed=error_embed("İşlem Başarısız", "Üye bu sunucuda bulunamadı."))
            return

    sebep = " ".join(remaining) if remaining else "Sebep belirtilmedi"

    def edit(data):
        g = data.setdefault(str(ctx.guild.id), {})
        warnings = g.setdefault("warnings", {})
        kayitlar = warnings.setdefault(str(target.id), [])
        kayitlar.append({"sebep": sebep, "yetkili": ctx.author.id, "zaman": utc_now().isoformat()})
        return len(kayitlar)

    count = update_settings(edit)
    e = embed("🌸 Üye Uyarıldı", f"**Hedef:** {target.mention}\n**Toplam Uyarı:** `{count}`\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", PEMBE)
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mod_log", e)


@bot.command(name="uyarlar", aliases=["warnings", "uyarılar"])
async def uyarlar(ctx, *args):
    target, _ = await hedef_uye_bul(ctx, *args)
    target = target or ctx.author
    if not isinstance(target, discord.Member):
        target = ctx.author

    kayitlar = warnings_get(ctx.guild.id).get(str(target.id), [])
    if not kayitlar:
        await ctx.send(embed=embed("🌸 Uyarı Kaydı Yok", f"{target.mention} için kayıtlı herhangi bir uyarı bulunmuyor.", PEMBE))
        return

    e = embed("🌸 Uyarı Listesi", f"{target.mention} için toplam **{len(kayitlar)}** uyarı kaydı mevcut.", PEMBE)
    for i, item in enumerate(kayitlar[-10:], start=max(1, len(kayitlar) - 9)):
        yetkili = item.get("yetkili", "Bilinmiyor") if isinstance(item, dict) else "Bilinmiyor"
        sebep = item.get("sebep", item) if isinstance(item, dict) else item
        e.add_field(name=f"Uyarı #{i}", value=f"**Sebep:** {short(sebep, 300)}\n**Yetkili:** <@{yetkili}>", inline=False)
    await ctx.send(embed=e)


@bot.command(name="uyarsil", aliases=["uyarısil", "clearwarns"])
@commands.has_permissions(manage_messages=True)
async def uyarsil(ctx, *args):
    target, _ = await hedef_uye_bul(ctx, *args)
    if target is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}uyarsil @üye` veya mesaja yanıt verip `{PREFIX}uyarsil`"))
        return

    def edit(data):
        data.setdefault(str(ctx.guild.id), {}).setdefault("warnings", {}).pop(str(target.id), None)
    update_settings(edit)
    await ctx.send(embed=embed("🌸 Uyarılar Temizlendi", f"{getattr(target, 'mention', str(target))} için tüm uyarı geçmişi silindi.", PEMBE))


@bot.command(name="lock", aliases=["kilit"])
@commands.has_permissions(manage_channels=True)
async def lock(ctx, kanal: discord.TextChannel = None):
    kanal = kanal or ctx.channel
    await kanal.set_permissions(ctx.guild.default_role, send_messages=False, reason=f"{ctx.author} kanalı kilitledi")
    await ctx.send(embed=embed("🌸 Kanal Kilitlendi", f"{kanal.mention} mesaj gönderimine kapatıldı.", PEMBE))


@bot.command(name="unlock", aliases=["kilitac", "kilitaç"])
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, kanal: discord.TextChannel = None):
    kanal = kanal or ctx.channel
    await kanal.set_permissions(ctx.guild.default_role, send_messages=None, reason=f"{ctx.author} kanalı açtı")
    await ctx.send(embed=embed("🌸 Kanal Açıldı", f"{kanal.mention} tekrar mesaj gönderimine açıldı.", PEMBE))


@bot.command(name="slowmode", aliases=["sm", "yavaşmod"])
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, sure: int = 0):
    sure = max(0, min(sure, 21600))
    await ctx.channel.edit(slowmode_delay=sure, reason=f"{ctx.author} yavaş mod ayarladı")
    await ctx.send(embed=embed("🌸 Yavaş Mod Ayarlandı", f"Bu kanaldaki yavaş mod bekleme süresi **{sure} saniye** olarak ayarlandı.", PEMBE))


@bot.command(name="duyuru", aliases=["announce"])
@commands.has_permissions(manage_messages=True)
async def duyuru(ctx, kanal: discord.TextChannel = None, *, mesaj: str = None):
    if kanal is None or mesaj is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}duyuru #kanal mesaj [gif/resim linki]`"))
        return
    image_url = None
    image_match = URL_REGEX.search(mesaj)
    if image_match:
        image_url = image_match.group(1)
        mesaj = mesaj.replace(image_url, "").strip()
    e = embed("📢 Duyuru", mesaj or "Yeni duyuru", PEMBE)
    if ctx.guild.icon:
        e.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
    else:
        e.set_author(name=ctx.guild.name)
    if image_url:
        e.set_image(url=image_url)
    if ctx.author.display_avatar:
        e.set_footer(text=f"Duyuran: {ctx.author} | {timestamp()}", icon_url=ctx.author.display_avatar.url)
    await kanal.send(embed=e)
    await ctx.send(embed=embed("🌸 Duyuru Gönderildi", f"Duyuru başarıyla {kanal.mention} kanalına yayınlandı.", PEMBE))


@bot.command(name="kufur-kur", aliases=["küfür-kur"])
@commands.has_permissions(manage_guild=True)
async def kufur_kur(ctx, *, kelimeler: str = None):
    liste = [k.strip().lower() for k in kelimeler.split(",")] if kelimeler else sorted(KUFUR_KELIMELERI)
    set_guild_section(ctx.guild.id, "kufur_koruma", {"aktif": True, "kelimeler": liste})
    await ctx.send(embed=embed("🌸 Küfür Koruması Aktif", f"Toplam **{len(liste)}** filtre kelimesi ile küfür engelleme aktif edildi.", PEMBE))


@bot.command(name="kufur-kapat", aliases=["küfür-kapat"])
@commands.has_permissions(manage_guild=True)
async def kufur_kapat(ctx):
    set_guild_section(ctx.guild.id, "kufur_koruma", {"aktif": False, "kelimeler": []})
    await ctx.send(embed=embed("🌸 Küfür Koruması Kapatıldı", "Küfür engelleme sistemi devre dışı bırakıldı.", PEMBE))


@bot.command(name="link-koruma-aktif", aliases=["antilink"])
@commands.has_permissions(manage_guild=True)
async def link_koruma_aktif(ctx):
    ayar = guild_section(ctx.guild.id, "link_koruma", {"muaf_roller": [], "muaf_kanallar": []})
    ayar["aktif"] = True
    set_guild_section(ctx.guild.id, "link_koruma", ayar)
    await ctx.send(embed=embed("🌸 Link Koruması Aktif", "İzinli rol/kanallar haricindeki tüm linkler otomatik silinecek.", PEMBE))


@bot.command(name="link-koruma-kapat")
@commands.has_permissions(manage_guild=True)
async def link_koruma_kapat(ctx):
    ayar = guild_section(ctx.guild.id, "link_koruma", {})
    ayar["aktif"] = False
    set_guild_section(ctx.guild.id, "link_koruma", ayar)
    await ctx.send(embed=embed("🌸 Link Koruması Kapatıldı", "Link koruma sistemi kapatıldı.", PEMBE))


@bot.command(name="link-koruma-muaf-rol")
@commands.has_permissions(manage_guild=True)
async def link_muaf_rol(ctx, rol: discord.Role = None):
    if rol is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}link-koruma-muaf-rol @rol`"))
        return
    ayar = guild_section(ctx.guild.id, "link_koruma", {"aktif": False, "muaf_roller": [], "muaf_kanallar": []})
    roller = set(ayar.get("muaf_roller", []))
    if rol.id in roller:
        roller.remove(rol.id)
        durum = "çıkarıldı"
    else:
        roller.add(rol.id)
        durum = "eklendi"
    ayar["muaf_roller"] = list(roller)
    set_guild_section(ctx.guild.id, "link_koruma", ayar)
    await ctx.send(embed=embed("🌸 Muaf Rol Güncellendi", f"{rol.mention} muaf rol listesine {durum}.", PEMBE))


@bot.command(name="link-koruma-muaf-kanal")
@commands.has_permissions(manage_guild=True)
async def link_muaf_kanal(ctx, kanal: discord.TextChannel = None):
    if kanal is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}link-koruma-muaf-kanal #kanal`"))
        return
    ayar = guild_section(ctx.guild.id, "link_koruma", {"aktif": False, "muaf_roller": [], "muaf_kanallar": []})
    kanallar = set(ayar.get("muaf_kanallar", []))
    if kanal.id in kanallar:
        kanallar.remove(kanal.id)
        durum = "çıkarıldı"
    else:
        kanallar.add(kanal.id)
        durum = "eklendi"
    ayar["muaf_kanallar"] = list(kanallar)
    set_guild_section(ctx.guild.id, "link_koruma", ayar)
    await ctx.send(embed=embed("🌸 Muaf Kanal Güncellendi", f"{kanal.mention} muaf kanal listesine {durum}.", PEMBE))


@bot.command(name="spam-koruma-kur")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_kur(ctx, max_mesaj: int = 5, saniye: int = 8, mute_saniye: int = 300):
    ayar = {"aktif": True, "max_mesaj": max(2, max_mesaj), "saniye": max(3, saniye), "mute_saniye": max(10, mute_saniye), "muaf_roller": [], "muaf_kanallar": []}
    set_guild_section(ctx.guild.id, "spam_koruma", ayar)
    await ctx.send(embed=embed("🌸 Spam Koruması Aktif", f"{ayar['saniye']} saniyede {ayar['max_mesaj']} mesaj sınırını aşanlara **{format_duration(ayar['mute_saniye'])}** timeout verilecek.", PEMBE))


@bot.command(name="spam-koruma-kapat")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_kapat(ctx):
    ayar = guild_section(ctx.guild.id, "spam_koruma", {})
    ayar["aktif"] = False
    set_guild_section(ctx.guild.id, "spam_koruma", ayar)
    await ctx.send(embed=embed("🌸 Spam Koruması Kapatıldı", "Spam engelleme sistemi kapatıldı.", PEMBE))


@bot.command(name="spam-koruma-durum")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_durum(ctx):
    ayar = guild_section(ctx.guild.id, "spam_koruma", {})
    durum = "Aktif" if ayar.get("aktif") else "Devre Dışı"
    await ctx.send(embed=embed("🌸 Spam Koruma Durumu", f"**Durum:** {durum}\n**Limit:** `{ayar.get('max_mesaj', 5)}` mesaj / `{ayar.get('saniye', 8)}` saniye", PEMBE))


@bot.command(name="jailkur")
@commands.has_permissions(manage_guild=True)
async def jailkur(ctx, kanal: discord.TextChannel = None, yetki_rol: discord.Role = None):
    if kanal is None or yetki_rol is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}jailkur #jail-kanali @jail-yetki-rolu`"))
        return
    jail_rol = discord.utils.get(ctx.guild.roles, name="JAIL")
    if jail_rol is None:
        jail_rol = await ctx.guild.create_role(name="JAIL", reason="Jail sistemi kurulumu")
    ayar = guild_section(ctx.guild.id, "jail_sistemi", {"kayitlar": {}})
    ayar.update({"aktif": True, "kanal_id": kanal.id, "jail_rol_id": jail_rol.id, "yetki_rol_id": yetki_rol.id, "kayitlar": ayar.get("kayitlar", {})})
    set_guild_section(ctx.guild.id, "jail_sistemi", ayar)
    for ch in ctx.guild.channels:
        try:
            if ch.id == kanal.id:
                await ch.set_permissions(jail_rol, view_channel=True, send_messages=True, read_message_history=True)
            elif isinstance(ch, discord.VoiceChannel):
                await ch.set_permissions(jail_rol, view_channel=False, connect=False, speak=False)
            else:
                await ch.set_permissions(jail_rol, view_channel=False, send_messages=False, read_message_history=False)
        except Exception:
            pass
    await ctx.send(embed=embed("🌸 Jail Sistemi Kuruldu", f"**Jail Kanalı:** {kanal.mention}\n**Jail Rolü:** {jail_rol.mention}\n**Yetkili Rolü:** {yetki_rol.mention}", PEMBE))


def jail_yetkili(member: discord.Member) -> bool:
    ayar = guild_section(member.guild.id, "jail_sistemi", {})
    yetki_rol_id = ayar.get("yetki_rol_id")
    return member.guild_permissions.administrator or any(r.id == yetki_rol_id for r in member.roles)


@bot.command(name="jail", aliases=["hapis"])
async def jail(ctx, *args):
    target, remaining = await hedef_uye_bul(ctx, *args)
    if target is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}jail @üye [sebep]` veya mesaja yanıt verip `{PREFIX}jail [sebep]`"))
        return

    if not jail_yetkili(ctx.author):
        await ctx.send(embed=error_embed("Yetki Hatası", "Bu komut için jail yetki rolüne sahip olmalısınız."))
        return

    if not isinstance(target, discord.Member):
        try:
            target = await ctx.guild.fetch_member(target.id)
        except (discord.HTTPException, AttributeError):
            await ctx.send(embed=error_embed("İşlem Başarısız", "Üye bu sunucuda bulunamadı."))
            return

    guard = role_guard(ctx, target)
    if guard:
        await ctx.send(embed=error_embed("İşlem Engellendi", guard))
        return

    ayar = guild_section(ctx.guild.id, "jail_sistemi", {})
    jail_rol = ctx.guild.get_role(int(ayar.get("jail_rol_id") or 0))
    if not ayar.get("aktif") or jail_rol is None:
        await ctx.send(embed=error_embed("Jail Hazır Değil", f"Önce `{PREFIX}jailkur #kanal @rol` komutunu çalıştırın."))
        return

    sebep = " ".join(remaining) if remaining else "Sebep belirtilmedi"
    eski_roller = [r.id for r in target.roles if r != ctx.guild.default_role and r.id != jail_rol.id]
    try:
        await target.edit(roles=[jail_rol], reason=f"{ctx.author}: {sebep}")
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Jail Başarısız", "Botun rol sırası yetersiz."))
        return

    ayar.setdefault("kayitlar", {})[str(target.id)] = {"roller": eski_roller, "sebep": sebep, "yetkili": ctx.author.id, "zaman": utc_now().isoformat()}
    set_guild_section(ctx.guild.id, "jail_sistemi", ayar)
    e = embed("🌸 Üye Jaile Atıldı", f"**Hedef:** {target.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", PEMBE)
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mod_log", e)


@bot.command(name="unjail", aliases=["hapiskaldır"])
async def unjail(ctx, *args):
    target, remaining = await hedef_uye_bul(ctx, *args)
    if target is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}unjail @üye` veya mesaja yanıt verip `{PREFIX}unjail`"))
        return

    if not jail_yetkili(ctx.author):
        await ctx.send(embed=error_embed("Yetki Hatası", "Bu komut için jail yetki rolüne sahip olmalısınız."))
        return

    if not isinstance(target, discord.Member):
        try:
            target = await ctx.guild.fetch_member(target.id)
        except (discord.HTTPException, AttributeError):
            await ctx.send(embed=error_embed("İşlem Başarısız", "Üye bu sunucuda bulunamadı."))
            return

    ayar = guild_section(ctx.guild.id, "jail_sistemi", {})
    kayit = ayar.get("kayitlar", {}).get(str(target.id))
    if not kayit:
        await ctx.send(embed=error_embed("Kayıt Bulunamadı", "Bu üye için jail kaydı bulunamadı."))
        return

    roller = [ctx.guild.get_role(int(rid)) for rid in kayit.get("roller", [])]
    roller = [r for r in roller if r and r < ctx.guild.me.top_role]
    try:
        await target.edit(roles=roller, reason=f"{ctx.author} jail kaldırdı")
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Unjail Başarısız", "Botun rol sırası yetersiz."))
        return

    ayar["kayitlar"].pop(str(target.id), None)
    set_guild_section(ctx.guild.id, "jail_sistemi", ayar)
    e = embed("🌸 Jail Kaldırıldı", f"{target.mention} için eski roller başarıyla iade edildi.", PEMBE)
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mod_log", e)


@bot.command(name="jailkapat")
@commands.has_permissions(administrator=True)
async def jailkapat(ctx):
    set_guild_section(ctx.guild.id, "jail_sistemi", {"aktif": False, "kayitlar": {}})
    await ctx.send(embed=embed("🌸 Jail Sistemi Kapatıldı", "Jail ayarları temizlendi ve devre dışı bırakıldı.", PEMBE))


def afk_data(guild_id: int) -> dict:
    return guild_section(guild_id, "afk_users", {})


@bot.command(name="afk")
async def afk(ctx, *, sebep: str = "AFK"):
    old_nick = ctx.author.nick
    def edit(data):
        afks = data.setdefault(str(ctx.guild.id), {}).setdefault("afk_users", {})
        afks[str(ctx.author.id)] = {"sebep": sebep, "old_nick": old_nick, "since": utc_now().isoformat()}
    update_settings(edit)
    if not ctx.author.display_name.startswith("[AFK]"):
        try:
            await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}"[:32], reason="AFK modu")
        except discord.Forbidden:
            pass
    await ctx.send(embed=embed("🌸 AFK Modu Açıldı", f"{ctx.author.mention} artık AFK modunda.\n**Sebep:** {sebep}", PEMBE))


async def afk_cikar(message: discord.Message, kayit: dict):
    old_nick = kayit.get("old_nick")
    try:
        await message.author.edit(nick=old_nick, reason="AFK modu kapandı")
    except discord.Forbidden:
        pass
    def edit(data):
        data.setdefault(str(message.guild.id), {}).setdefault("afk_users", {}).pop(str(message.author.id), None)
    update_settings(edit)
    await message.channel.send(embed=embed("🌸 AFK Modu Kapandı", f"{message.author.mention}, tekrar hoş geldiniz! AFK modundan çıktınız.", PEMBE))


class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Destek Talebi Aç 🎫", style=discord.ButtonStyle.primary, custom_id="ticket_ac")
    async def ticket_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        ayar = guild_section(interaction.guild_id, "ticket_sistemi", {})
        kategori = interaction.guild.get_channel(int(ayar.get("kategori_id") or 0))
        log_kanal = interaction.guild.get_channel(int(ayar.get("log_kanal_id") or 0))
        if not isinstance(kategori, discord.CategoryChannel):
            await interaction.response.send_message(embed=error_embed("Ticket Hazır Değil", "Ticket kategorisi ayarlanmamış."), ephemeral=True)
            return
        for ch in kategori.text_channels:
            if ch.topic == f"ticket-owner:{interaction.user.id}":
                await interaction.response.send_message(embed=error_embed("Zaten Açık Talebiniz Var", f"Aktif talebiniz bulunuyor: {ch.mention}"), ephemeral=True)
                return
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True),
            interaction.guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True, manage_channels=True),
        }
        destek_rol = interaction.guild.get_role(int(ayar.get("destek_rol_id") or 0))
        if destek_rol:
            overwrites[destek_rol] = discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
        kanal = await kategori.create_text_channel(name=f"ticket-{interaction.user.name}"[:90], topic=f"ticket-owner:{interaction.user.id}", overwrites=overwrites)
        await kanal.send(embed=embed("🌸 Destek Talebi Oluşturuldu", f"{interaction.user.mention}, destek ekibimiz en kısa sürede ilgilenecektir.", PEMBE), view=TicketCloseView())
        await interaction.response.send_message(embed=embed("🌸 Ticket Açıldı", f"Destek kanalınız oluşturuldu: {kanal.mention}", PEMBE), ephemeral=True)
        if isinstance(log_kanal, discord.TextChannel):
            await log_kanal.send(embed=embed("🌸 Ticket Oluşturuldu", f"**Üye:** {interaction.user.mention}\n**Kanal:** {kanal.mention}", PEMBE))


class TicketCloseView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Ticket Kapat 🔒", style=discord.ButtonStyle.danger, custom_id="ticket_kapat")
    async def ticket_kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not isinstance(interaction.channel, discord.TextChannel) or not interaction.channel.name.startswith("ticket-"):
            await interaction.response.send_message(embed=error_embed("Geçersiz Kanal", "Bu buton yalnızca ticket kanallarında çalışır."), ephemeral=True)
            return
        await interaction.response.send_message(embed=embed("🌸 Ticket Kapatılıyor", "Bu kanal 5 saniye içinde silinecektir.", PEMBE))
        await asyncio.sleep(5)
        await interaction.channel.delete(reason=f"{interaction.user} ticket kapattı")


@bot.command(name="ticketkur", aliases=["ticket-kur"])
@commands.has_permissions(manage_guild=True)
async def ticketkur(ctx, kategori: discord.CategoryChannel = None, log: discord.TextChannel = None, destek_rol: discord.Role = None):
    if kategori is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}ticketkur <kategori> [log-kanalı] [destek-rolü]`"))
        return
    set_guild_section(ctx.guild.id, "ticket_sistemi", {"kategori_id": kategori.id, "log_kanal_id": log.id if log else None, "destek_rol_id": destek_rol.id if destek_rol else None})
    await ctx.send(embed=embed("🌸 Ticket Sistemi Kuruldu", f"**Kategori:** {kategori.name}\n**Log:** {log.mention if log else 'Yok'}\n**Destek Rolü:** {destek_rol.mention if destek_rol else 'Yok'}", PEMBE))


@bot.command(name="ticketpanel", aliases=["ticket-panel"])
@commands.has_permissions(manage_guild=True)
async def ticketpanel(ctx):
    await ctx.send(embed=embed("🌸 Destek Talebi Paneli", "Destek ekibimizle iletişime geçmek için aşağıdaki butona tıklayarak ticket oluşturabilirsiniz.", PEMBE), view=TicketView())


@bot.command(name="ticketkapat", aliases=["ticket-kapat"])
async def ticketkapat(ctx):
    if not ctx.channel.name.startswith("ticket-"):
        await ctx.send(embed=error_embed("Geçersiz Kanal", "Bu komut yalnızca ticket kanallarında kullanılabilir."))
        return
    await ctx.send(embed=embed("🌸 Ticket Kapatılıyor", "Kanal 5 saniye içinde silinecektir.", PEMBE))
    await asyncio.sleep(5)
    await ctx.channel.delete(reason=f"{ctx.author} ticket kapattı")


@bot.command(name="ticketekle", aliases=["ticket-ekle"])
async def ticketekle(ctx, *args):
    target, _ = await hedef_uye_bul(ctx, *args)
    if target is None or not isinstance(target, discord.Member):
        await ctx.send(embed=usage_embed(f"`{PREFIX}ticketekle @üye`"))
        return
    await ctx.channel.set_permissions(target, view_channel=True, send_messages=True, read_message_history=True)
    await ctx.send(embed=embed("🌸 Üye Eklendi", f"{target.mention} tickete eklendi.", PEMBE))


@bot.command(name="ticketcikar", aliases=["ticket-çıkar"])
async def ticketcikar(ctx, *args):
    target, _ = await hedef_uye_bul(ctx, *args)
    if target is None or not isinstance(target, discord.Member):
        await ctx.send(embed=usage_embed(f"`{PREFIX}ticketcikar @üye`"))
        return
    await ctx.channel.set_permissions(target, overwrite=None)
    await ctx.send(embed=embed("🌸 Üye Çıkarıldı", f"{target.mention} ticketten çıkarıldı.", PEMBE))


GIVEAWAY_EMOJI = "🎉"
giveaway_tasks = {}


def giveaway_get(guild_id: int) -> dict:
    return guild_section(guild_id, "giveaways", {})


def giveaway_set(guild_id: int, message_id: int, data: dict | None) -> None:
    def edit(settings):
        g = settings.setdefault(str(guild_id), {})
        giveaways = g.setdefault("giveaways", {})
        if data is None:
            giveaways.pop(str(message_id), None)
        else:
            giveaways[str(message_id)] = data
    update_settings(edit)


async def giveaway_finish(guild_id: int, channel_id: int, message_id: int, forced: bool = False):
    guild = bot.get_guild(guild_id)
    if guild is None:
        return
    channel = guild.get_channel(channel_id)
    if not isinstance(channel, discord.TextChannel):
        return
    data = giveaway_get(guild_id).get(str(message_id))
    if not data:
        return
    try:
        msg = await channel.fetch_message(message_id)
    except discord.HTTPException:
        giveaway_set(guild_id, message_id, None)
        return
    reaction = discord.utils.get(msg.reactions, emoji=GIVEAWAY_EMOJI)
    users = [u async for u in reaction.users() if not u.bot] if reaction else []
    winners_count = max(1, int(data.get("winners", 1)))
    winners = random.sample(users, min(winners_count, len(users))) if users else []
    winners_text = " ".join(u.mention for u in winners) if winners else "Kazanan Yok"
    end_embed = embed("🎉 ÇEKİLİŞ BİTTİ 🎉", f"**Ödül:** {data.get('prize')}\n**Kazanan:** {winners_text}\n**Toplam Katılımcı:** {len(users)}", PEMBE)
    if data.get("gif_url"):
        end_embed.set_image(url=data["gif_url"])
    try:
        await msg.edit(embed=end_embed)
    except discord.HTTPException:
        pass
    giveaway_set(guild_id, message_id, None)
    if winners:
        await channel.send(embed=embed("🌸 Tebrikler!", f"{winners_text}\n**{data.get('prize')}** kazandınız!", PEMBE))
    elif forced:
        await channel.send(embed=embed("🌸 Çekiliş Sonlandırıldı", "Katılımcı olmadığı için kazanan seçilemedi.", PEMBE))


async def giveaway_wait(guild_id: int, channel_id: int, message_id: int, ends_at: str):
    try:
        end_time = datetime.fromisoformat(ends_at)
        delay = max(0, (end_time - utc_now()).total_seconds())
        await asyncio.sleep(delay)
        await giveaway_finish(guild_id, channel_id, message_id)
    finally:
        giveaway_tasks.pop((guild_id, message_id), None)


def schedule_giveaway(guild_id: int, channel_id: int, message_id: int, ends_at: str):
    key = (guild_id, message_id)
    old = giveaway_tasks.get(key)
    if old:
        old.cancel()
    giveaway_tasks[key] = asyncio.create_task(giveaway_wait(guild_id, channel_id, message_id, ends_at))


@bot.command(name="gstart", aliases=["giveaway", "cekilisbaslat", "çekilişbaşlat"])
@commands.has_permissions(manage_guild=True)
async def gstart(ctx, sure: str = None, kazanan: int = 1, *, odul_veya_gif: str = None):
    """
    Çekiliş başlatır ve GIF / Görsel linki sorar.
    İster adım adım: .gstart
    İster tek satırda: .gstart 10m 1 Nitro https://media.giphy.com/...gif
    """
    gif_url = None
    odul = None

    # Eğer argüman verilmemişse adımlı / interaktif kurulum:
    if sure is None:
        def check(m):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        try:
            # 1. Süre sor
            msg1 = await ctx.send(embed=embed("🌸 Çekiliş Kurulumu (1/4)", "Çekiliş süresi nedir? (Örn: `10m`, `1h`, `1d`)\nİptal etmek için `iptal` yazın.", PEMBE))
            res1 = await bot.wait_for("message", check=check, timeout=60.0)
            if res1.content.lower() in ["iptal", "cancel"]:
                await ctx.send(embed=embed("🌸 İşlem İptal Edildi", "Çekiliş kurulumu iptal edildi.", PEMBE))
                return
            sure = res1.content.strip()
            parse_duration(sure)

            # 2. Kazanan sayısı sor
            msg2 = await ctx.send(embed=embed("🌸 Çekiliş Kurulumu (2/4)", "Kaç kazanan olacak? (Örn: `1`)", PEMBE))
            res2 = await bot.wait_for("message", check=check, timeout=60.0)
            kazanan = max(1, int(re.sub(r"\D", "", res2.content) or 1))

            # 3. Ödül sor
            msg3 = await ctx.send(embed=embed("🌸 Çekiliş Kurulumu (3/4)", "Çekiliş ödülü nedir? (Örn: `Discord Nitro`)", PEMBE))
            res3 = await bot.wait_for("message", check=check, timeout=60.0)
            odul = res3.content.strip()

            # 4. GIF / Görsel linki sor
            msg4 = await ctx.send(embed=embed("🌸 Çekiliş Kurulumu (4/4)", "Çekiliş için GIF veya Görsel linki gönderin:\n*(Görsel eklemek istemiyorsanız **pas** veya **yok** yazın)*", PEMBE))
            res4 = await bot.wait_for("message", check=check, timeout=60.0)
            if res4.content.strip().lower() not in ["pas", "yok", "none", "no"]:
                found_url = URL_REGEX.search(res4.content.strip())
                if found_url:
                    gif_url = found_url.group(1)

        except asyncio.TimeoutError:
            await ctx.send(embed=error_embed("Zaman Aşımı", "Süre dolduğu için çekiliş kurulumu iptal edildi."))
            return
        except ValueError:
            await ctx.send(embed=error_embed("Geçersiz Girdi", "Geçersiz süre veya sayı girdiniz. Çekiliş iptal edildi."))
            return
    else:
        # Argümanlı kullanım:
        if odul_veya_gif is None:
            await ctx.send(embed=usage_embed(f"`{PREFIX}gstart 10m 1 Nitro [gif_linki]` veya sadece `{PREFIX}gstart` yazarak adım adım başlatabilirsiniz."))
            return

        found_url = URL_REGEX.search(odul_veya_gif)
        if found_url:
            gif_url = found_url.group(1)
            odul = odul_veya_gif.replace(gif_url, "").strip()
        else:
            odul = odul_veya_gif.strip()

        # Eğer GIF verilmemişse soralım:
        if not gif_url:
            def check_gif(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            await ctx.send(embed=embed("🌸 Çekiliş GIF Linki", "Çekiliş için bir GIF / Görsel linki eklemek ister misiniz?\n*(İstemiyorsanız **pas** yazın, 15 saniye sonra otomatik geçilir)*", PEMBE))
            try:
                gif_res = await bot.wait_for("message", check=check_gif, timeout=15.0)
                if gif_res.content.strip().lower() not in ["pas", "yok", "none", "no"]:
                    g_match = URL_REGEX.search(gif_res.content.strip())
                    if g_match:
                        gif_url = g_match.group(1)
            except asyncio.TimeoutError:
                pass

    if not odul:
        odul = "Sürpriz Ödül"

    try:
        seconds = parse_duration(sure)
    except ValueError:
        await ctx.send(embed=error_embed("Geçersiz Süre", "Örnek süreler: `30s`, `10m`, `2h`, `1d`."))
        return

    ends_at = utc_now() + timedelta(seconds=seconds)
    e = embed(
        "🎉 ÇEKİLİŞ BAŞLADI 🎉",
        f"**Ödül:** {odul}\n**Kazanan Sayısı:** {kazanan}\n**Bitiş:** <t:{int(ends_at.timestamp())}:R>\n**Düzenleyen:** {ctx.author.mention}\n\nKatılmak için aşağıdaki {GIVEAWAY_EMOJI} tepkisine basın!",
        PEMBE
    )
    if gif_url:
        e.set_image(url=gif_url)

    msg = await ctx.send(embed=e)
    await msg.add_reaction(GIVEAWAY_EMOJI)

    giveaway_set(
        ctx.guild.id,
        msg.id,
        {
            "channel_id": ctx.channel.id,
            "prize": odul,
            "winners": max(1, kazanan),
            "ends_at": ends_at.isoformat(),
            "host_id": ctx.author.id,
            "gif_url": gif_url
        }
    )
    schedule_giveaway(ctx.guild.id, ctx.channel.id, msg.id, ends_at.isoformat())


@bot.command(name="gend", aliases=["cekilisbitir", "çekilişbitir"])
@commands.has_permissions(manage_guild=True)
async def gend(ctx, mesaj_id: int = None):
    if mesaj_id is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}gend <mesaj_id>`"))
        return
    await giveaway_finish(ctx.guild.id, ctx.channel.id, mesaj_id, forced=True)


@bot.command(name="greroll", aliases=["cekilisyenile", "çekilişyenile"])
@commands.has_permissions(manage_guild=True)
async def greroll(ctx, mesaj_id: int = None, kazanan: int = 1):
    if mesaj_id is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}greroll <mesaj_id> [kazanan_sayisi]`"))
        return
    try:
        msg = await ctx.channel.fetch_message(mesaj_id)
    except discord.HTTPException:
        await ctx.send(embed=error_embed("Mesaj Bulunamadı", "Çekiliş mesajı bulunamadı."))
        return
    reaction = discord.utils.get(msg.reactions, emoji=GIVEAWAY_EMOJI)
    users = [u async for u in reaction.users() if not u.bot] if reaction else []
    if not users:
        await ctx.send(embed=error_embed("Katılımcı Yok", "Yeni kazanan seçecek katılımcı bulunmuyor."))
        return
    winners = random.sample(users, min(max(1, kazanan), len(users)))
    await ctx.send(embed=embed("🌸 Çekiliş Yenilendi", f"Yeni Kazanan: {' '.join(u.mention for u in winners)}", PEMBE))


@bot.command(name="glist", aliases=["katilimcilar", "çekilişkatılımcı"])
async def glist(ctx, mesaj_id: int = None):
    if mesaj_id is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}glist <mesaj_id>`"))
        return
    try:
        msg = await ctx.channel.fetch_message(mesaj_id)
    except discord.HTTPException:
        await ctx.send(embed=error_embed("Mesaj Bulunamadı", "Çekiliş mesajı bulunamadı."))
        return
    reaction = discord.utils.get(msg.reactions, emoji=GIVEAWAY_EMOJI)
    users = [u async for u in reaction.users() if not u.bot] if reaction else []
    text = "\n".join(f"`{i}.` {u.mention}" for i, u in enumerate(users[:30], 1)) or "Katılımcı yok."
    await ctx.send(embed=embed("🌸 Çekiliş Katılımcıları", text, PEMBE))


@bot.command(name="gdelete", aliases=["gcancel", "cekilissil", "çekilişsil"])
@commands.has_permissions(manage_guild=True)
async def gdelete(ctx, mesaj_id: int = None):
    if mesaj_id is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}gdelete <mesaj_id>`"))
        return
    try:
        msg = await ctx.channel.fetch_message(mesaj_id)
        await msg.delete()
    except discord.HTTPException:
        pass
    giveaway_set(ctx.guild.id, mesaj_id, None)
    await ctx.send(embed=embed("🌸 Çekiliş İptal Edildi", "Çekiliş mesajı ve kaydı başarıyla silindi.", PEMBE))


@bot.command(name="ginfo", aliases=["cekilisbilgi", "çekilişbilgi"])
async def ginfo(ctx, mesaj_id: int = None):
    if mesaj_id is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}ginfo <mesaj_id>`"))
        return
    data = giveaway_get(ctx.guild.id).get(str(mesaj_id))
    if not data:
        await ctx.send(embed=error_embed("Kayıt Bulunamadı", "Bu mesaj ID'si için aktif çekiliş kaydı bulunamadı."))
        return
    end_time = datetime.fromisoformat(data["ends_at"])
    e = embed("🌸 Çekiliş Bilgisi", f"**Ödül:** {data.get('prize')}\n**Kazanan:** {data.get('winners')}\n**Bitiş:** <t:{int(end_time.timestamp())}:R>", PEMBE)
    if data.get("gif_url"):
        e.set_image(url=data["gif_url"])
    await ctx.send(embed=e)


@bot.command(name="avatar")
async def avatar(ctx, *args):
    target, _ = await hedef_uye_bul(ctx, *args)
    target = target or ctx.author
    if not isinstance(target, discord.Member):
        target = ctx.author

    e = embed("🌸 Profil Resmi / Avatar", f"{target.mention} için avatar görüntüsü:", PEMBE)
    e.set_image(url=target.display_avatar.url)
    await ctx.send(embed=e)


@bot.command(name="sunucu", aliases=["serverinfo"])
async def sunucu(ctx):
    g = ctx.guild
    e = embed("🌸 Sunucu Bilgileri", f"**{g.name}** sunucusu genel istatistikleri:", PEMBE)
    e.add_field(name="👥 Üye Sayısı", value=str(g.member_count), inline=True)
    e.add_field(name="💬 Kanal Sayısı", value=str(len(g.channels)), inline=True)
    e.add_field(name="🎭 Rol Sayısı", value=str(len(g.roles)), inline=True)
    e.add_field(name="📅 Kuruluş Tarihi", value=g.created_at.strftime("%d.%m.%Y %H:%M"), inline=True)
    if g.icon:
        e.set_thumbnail(url=g.icon.url)
    await ctx.send(embed=e)


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(embed=embed("🌸 Pong!", f"Gecikme süresi: `{round(bot.latency * 1000)}ms`", PEMBE))


async def gelismis_yardim(ctx):
    e = embed("🌸 LogBot Komut Rehberi 🌸", "Tüm moderasyon, koruma ve sistem komutları aşağıda listelenmiştir.", PEMBE)
    e.add_field(name="🛡️ Moderasyon", value="`ban`, `unban`, `kick`, `mute`, `unmute`, `sil`, `warn`, `uyarlar`, `uyarsil`, `jail`, `unjail`, `lock`, `unlock`, `slowmode`", inline=False)
    e.add_field(name="🔒 Koruma Sistemleri", value="`kufur-kur`, `kufur-kapat`, `link-koruma-aktif`, `link-koruma-kapat`, `spam-koruma-kur`, `spam-koruma-kapat`, `spam-koruma-durum`", inline=False)
    e.add_field(name="🎉 Çekiliş & Bilet & Sistem", value="`gstart`, `gend`, `greroll`, `glist`, `gdelete`, `ginfo`, `ticketkur`, `ticketpanel`, `ticketkapat`, `afk`, `logkur`, `log-kur`, `log-kaldir`, `log-durum`", inline=False)
    e.add_field(name="📢 Duyuru", value=f"`{PREFIX}duyuru #kanal mesaj [gif-linki]`", inline=False)
    await ctx.send(embed=e)


@bot.command(name="yardim", aliases=["yardım", "help", "komutlar"])
async def yardim(ctx):
    await gelismis_yardim(ctx)


spam_cache: dict[tuple[int, int], list[float]] = {}


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot or message.guild is None:
        return

    content = message.content or ""
    lower = content.lower()
    is_afk_command = lower.startswith(f"{PREFIX}afk")

    afks = afk_data(message.guild.id)
    author_afk = afks.get(str(message.author.id))
    if author_afk and not is_afk_command:
        await afk_cikar(message, author_afk)

    for member in message.mentions:
        kayit = afks.get(str(member.id))
        if kayit and member.id != message.author.id:
            since = kayit.get("since")
            since_text = ""
            if since:
                try:
                    since_text = f"\n**AFK Olma Zamanı:** <t:{int(datetime.fromisoformat(since).timestamp())}:R>"
                except Exception:
                    pass
            await message.channel.send(embed=embed("🌸 Bu Üye Şu An AFK", f"{member.mention} şu anda AFK modunda.\n**Sebep:** {kayit.get('sebep', 'AFK')}{since_text}", PEMBE))

    await bot.process_commands(message)

    if message.author.guild_permissions.manage_messages:
        return

    data = guild_data(message.guild.id)

    kufur = data.get("kufur_koruma", {})
    if kufur.get("aktif"):
        kelimeler = set(kufur.get("kelimeler") or KUFUR_KELIMELERI)
        temiz = re.sub(r"[^a-zA-Z0-9ğüşöçıİĞÜŞÖÇ ]", " ", lower)
        if any(re.search(rf"\b{re.escape(k)}\b", temiz) for k in kelimeler if k):
            try:
                await message.delete()
            except discord.HTTPException:
                pass
            e = error_embed("🌸 Küfür Engellendi", f"{message.author.mention}, bu sunucuda küfür kullanımı yasaktır.")
            await message.channel.send(embed=e, delete_after=6)
            await log_gonder(message.guild, "mod_log", e)
            return

    link = data.get("link_koruma", {})
    if link.get("aktif"):
        muaf_rol = any(r.id in set(link.get("muaf_roller", [])) for r in message.author.roles)
        muaf_kanal = message.channel.id in set(link.get("muaf_kanallar", []))
        if not muaf_rol and not muaf_kanal and LINK_REGEX.search(content):
            try:
                await message.delete()
            except discord.HTTPException:
                pass
            e = error_embed("🌸 Link Engellendi", f"{message.author.mention}, bu kanalda link paylaşılması yasaktır.")
            await message.channel.send(embed=e, delete_after=6)
            await log_gonder(message.guild, "mod_log", e)
            return

    spam = data.get("spam_koruma", {})
    if spam.get("aktif"):
        key = (message.guild.id, message.author.id)
        now = time.monotonic()
        window = max(3, int(spam.get("saniye", 8)))
        spam_cache[key] = [t for t in spam_cache.get(key, []) if now - t <= window]
        spam_cache[key].append(now)
        if len(spam_cache[key]) > int(spam.get("max_mesaj", 5)):
            seconds = int(spam.get("mute_saniye", 300))
            try:
                await message.author.timeout(utc_now() + timedelta(seconds=seconds), reason="Spam koruması")
            except discord.HTTPException:
                pass
            e = embed("🌸 Spam Cezası", f"{message.author.mention} spam nedeniyle **{format_duration(seconds)}** boyunca susturuldu.", PEMBE)
            await message.channel.send(embed=e, delete_after=10)
            await log_gonder(message.guild, "mute_log", e)
            spam_cache[key] = []


@bot.event
async def on_member_ban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_user(guild, discord.AuditLogAction.ban, user)
    e = embed("🌸 Ban Logu", f"**Kullanıcı:** {user} (`{user.id}`)\n**Yetkili:** {sorumlu.mention if sorumlu else 'Bilinmiyor'}", PEMBE)
    await log_gonder(guild, "ban_log", e)


@bot.event
async def on_member_unban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_user(guild, discord.AuditLogAction.unban, user)
    e = embed("🌸 Unban Logu", f"**Kullanıcı:** {user} (`{user.id}`)\n**Yetkili:** {sorumlu.mention if sorumlu else 'Bilinmiyor'}", PEMBE)
    await log_gonder(guild, "ban_log", e)


@bot.event
async def on_member_join(member: discord.Member):
    await log_gonder(member.guild, "giris_cikis", embed("🌸 Üye Katıldı", f"{member.mention} sunucuya katıldı.\n**Kullanıcı ID:** `{member.id}`", PEMBE))


@bot.event
async def on_member_remove(member: discord.Member):
    await log_gonder(member.guild, "giris_cikis", embed("🌸 Üye Ayrıldı", f"**{member}** sunucudan ayrıldı.\n**Kullanıcı ID:** `{member.id}`", PEMBE))


@bot.event
async def on_message_delete(message: discord.Message):
    if message.author.bot or not message.guild:
        return
    e = embed("🌸 Mesaj Silindi", f"**Kullanıcı:** {message.author.mention}\n**Kanal:** {message.channel.mention}\n**Silinen Mesaj:** {short(message.content or 'İçerik yok', 900)}", PEMBE)
    await log_gonder(message.guild, "mesaj_log", e)


@bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    if before.author.bot or not before.guild or before.content == after.content:
        return
    e = embed("🌸 Mesaj Düzenlendi", f"**Kullanıcı:** {before.author.mention}\n**Kanal:** {before.channel.mention}\n**Önce:** {short(before.content, 450)}\n**Sonra:** {short(after.content, 450)}", PEMBE)
    await log_gonder(before.guild, "mesaj_log", e)


@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    if before.timed_out_until != after.timed_out_until:
        if after.timed_out_until:
            e = embed("🌸 Timeout Verildi", f"**Üye:** {after.mention}\n**Bitiş:** <t:{int(after.timed_out_until.timestamp())}:R>", PEMBE)
        else:
            e = embed("🌸 Timeout Kaldırıldı", f"**Üye:** {after.mention}", PEMBE)
        await log_gonder(after.guild, "mute_log", e)
    old_roles = set(before.roles)
    new_roles = set(after.roles)
    if old_roles != new_roles:
        added = new_roles - old_roles
        removed = old_roles - new_roles
        text = ""
        if added:
            text += "Eklenen: " + ", ".join(r.mention for r in added) + "\n"
        if removed:
            text += "Alınan: " + ", ".join(r.mention for r in removed)
        await log_gonder(after.guild, "rol_log", embed("🌸 Rol Değişikliği", f"**Üye:** {after.mention}\n{text}", PEMBE))


@bot.event
async def on_guild_channel_create(channel):
    await log_gonder(channel.guild, "kanal_log", embed("🌸 Kanal Oluşturuldu", f"**Kanal:** {channel.mention if hasattr(channel, 'mention') else channel.name}", PEMBE))


@bot.event
async def on_guild_channel_delete(channel):
    await log_gonder(channel.guild, "kanal_log", embed("🌸 Kanal Silindi", f"**Kanal İsmi:** {channel.name}", PEMBE))


@bot.event
async def on_guild_role_create(role: discord.Role):
    await log_gonder(role.guild, "rol_log", embed("🌸 Rol Oluşturuldu", f"**Rol:** {role.mention}", PEMBE))


@bot.event
async def on_guild_role_delete(role: discord.Role):
    await log_gonder(role.guild, "rol_log", embed("🌸 Rol Silindi", f"**Rol İsmi:** {role.name}", PEMBE))


@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    if before.channel == after.channel:
        return
    if before.channel is None and after.channel is not None:
        text = f"{member.mention} {after.channel.mention} ses kanalına giriş yaptı."
    elif before.channel is not None and after.channel is None:
        text = f"{member.mention} {before.channel.mention} ses kanalından ayrıldı."
    else:
        text = f"{member.mention} {before.channel.mention} ➔ {after.channel.mention} kanalına geçiş yaptı."
    await log_gonder(member.guild, "ses_log", embed("🌸 Ses Logu", text, PEMBE))


@bot.event
async def on_ready():
    if not getattr(bot, "_ready_once", False):
        bot.add_view(TicketView())
        bot.add_view(TicketCloseView())
        for guild in bot.guilds:
            for message_id, data in giveaway_get(guild.id).items():
                try:
                    schedule_giveaway(guild.id, int(data["channel_id"]), int(message_id), data["ends_at"])
                except Exception:
                    continue
        try:
            bot.tree.clear_commands(guild=None)
            await bot.tree.sync()
        except discord.HTTPException:
            pass
        bot._ready_once = True
    print(f"[BOT] Giriş yapıldı: {bot.user} | Prefix: {PREFIX} | Settings: {SETTINGS_FILE}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=error_embed("Yetki Hatası", "Bu komutu kullanmak için gerekli yetkiye sahip değilsiniz."))
        return
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send(embed=error_embed("Bot Yetkisi Eksik", "Botun bu işlemi yapabilmesi için gerekli izinleri eksik."))
        return
    if isinstance(error, commands.BadArgument):
        await ctx.send(embed=error_embed("Geçersiz Argüman", "Komuttaki üye, rol, kanal veya sayı biçimi hatalı."))
        return
    await ctx.send(embed=error_embed("Komut Çalıştırma Hatası", short(error)))
    raise error


app = Flask(__name__)


@app.route("/")
def home():
    return "LogBot aktif."


@app.route("/health")
def health():
    return jsonify({"status": "ok", "bot": str(bot.user) if bot.user else None})


def run_bot():
    bot.run(TOKEN)


if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
