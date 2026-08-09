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


RENK = {
    "basari": 0x2ECC71,
    "hata": 0xE74C3C,
    "bilgi": 0x3498DB,
    "uyari": 0xF1C40F,
    "mod": 0x9B59B6,
    "mute": 0xE67E22,
}

LOG_TURLERI = {
    "ban_log": "Ban / Unban",
    "mute_log": "Mute / Timeout",
    "mod_log": "Moderasyon",
    "rol_log": "Rol Degisiklikleri",
    "mesaj_log": "Mesaj Islemleri",
    "giris_cikis": "Giris / Cikis",
    "ses_log": "Ses Kanallari",
    "kanal_log": "Kanal Islemleri",
    "davet_log": "Davetler",
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
    "amk", "aq", "oc", "orospu", "pic", "siktir", "yarrak", "yarak", "got", "ibne",
    "kahpe", "gavat", "pezevenk", "mal", "salak",
}

LINK_REGEX = re.compile(r"(https?://|www\.|discord\.gg/|discord\.com/invite/)", re.I)

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


def embed(title: str, description: str = "", color: int = RENK["bilgi"]) -> discord.Embed:
    e = discord.Embed(title=title, description=description, color=color, timestamp=utc_now())
    e.set_footer(text=timestamp())
    return e


def error_embed(title: str, description: str) -> discord.Embed:
    return embed(title, description, RENK["hata"])


def usage_embed(text: str) -> discord.Embed:
    return embed("Kullanim", text, RENK["uyari"])


def short(text: str, limit: int = 1024) -> str:
    text = str(text or "")
    return text if len(text) <= limit else text[: limit - 3] + "..."


def parse_duration(text: str | None, default_seconds: int = 3600) -> int:
    if not text:
        return default_seconds
    text = text.strip().lower()
    match = re.fullmatch(r"(\d+)(s|sn|m|dk|h|sa|d|g)?", text)
    if not match:
        raise ValueError("Gecersiz sure")
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
        parts.append(f"{days}g")
    if hours:
        parts.append(f"{hours}sa")
    if minutes:
        parts.append(f"{minutes}dk")
    if seconds or not parts:
        parts.append(f"{seconds}sn")
    return " ".join(parts)


def role_guard(ctx: commands.Context, target: discord.Member) -> str | None:
    if target.id == ctx.author.id:
        return "Kendin uzerinde bu islemi yapamazsin."
    if ctx.guild.owner_id != ctx.author.id and target.top_role >= ctx.author.top_role:
        return "Bu uye seninle ayni/ust rolde oldugu icin islem yapamazsin."
    if target.top_role >= ctx.guild.me.top_role:
        return "Botun rolu hedef uyeden yuksek degil."
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
    await ctx.send(embed=embed("Log Kurulumu", f"{sayi} varsayilan log kanali kaydedildi.", RENK["basari"]))


@bot.command(name="log-kur", aliases=["logayarla"])
@commands.has_permissions(manage_guild=True)
async def log_kur(ctx, tur: str = None, kanal: discord.TextChannel = None):
    if tur is None or kanal is None:
        turler = ", ".join(f"`{key}`" for key in LOG_TURLERI)
        await ctx.send(embed=usage_embed(f"`{PREFIX}log-kur <tur> #kanal`\n\nTurler: {turler}"))
        return
    tur = tur.strip().lower()
    if tur not in LOG_TURLERI:
        await ctx.send(embed=error_embed("Gecersiz Log Turu", f"`{tur}` desteklenmiyor. `{PREFIX}log-durum` ile turleri gorebilirsin."))
        return
    kanal_kaydet(ctx.guild.id, tur, kanal.id)
    await ctx.send(embed=embed("Log Kanali Ayarlandi", f"**{LOG_TURLERI[tur]}** loglari {kanal.mention} kanalina gidecek.", RENK["basari"]))


@bot.command(name="log-kaldir", aliases=["logkaldir"])
@commands.has_permissions(manage_guild=True)
async def log_kaldir(ctx, tur: str = None):
    if tur is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}log-kaldir <tur>`"))
        return
    tur = tur.strip().lower()
    if tur not in LOG_TURLERI:
        await ctx.send(embed=error_embed("Gecersiz Log Turu", f"`{tur}` desteklenmiyor."))
        return
    kanal_sil(ctx.guild.id, tur)
    await ctx.send(embed=embed("Log Kapatildi", f"**{LOG_TURLERI[tur]}** artik log gondermeyecek.", RENK["uyari"]))


@bot.command(name="log-durum", aliases=["logdurum"])
@commands.has_permissions(manage_guild=True)
async def log_durum(ctx):
    data = guild_data(ctx.guild.id)
    e = embed("Log Durumu", f"{ctx.guild.name} log ayarlari", RENK["bilgi"])
    for key, name in LOG_TURLERI.items():
        kanal_id = data.get(key) or VARSAYILAN_LOG_KANALLARI.get(key)
        kanal = ctx.guild.get_channel(int(kanal_id)) if kanal_id else None
        e.add_field(name=f"{name}\n`{key}`", value=kanal.mention if kanal else "Kapali", inline=True)
    await ctx.send(embed=e)


async def hedef_bul(ctx: commands.Context, hedef: str | None):
    if ctx.message.reference and ctx.message.reference.message_id and not hedef:
        try:
            msg = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            return msg.author
        except discord.HTTPException:
            return None
    if ctx.message.mentions:
        return ctx.message.mentions[0]
    if hedef and str(hedef).isdigit():
        member = ctx.guild.get_member(int(hedef))
        if member:
            return member
        try:
            return await ctx.guild.fetch_member(int(hedef))
        except discord.HTTPException:
            return discord.Object(id=int(hedef))
    if hedef:
        return discord.utils.find(lambda m: m.name.lower() == hedef.lower() or str(m).lower() == hedef.lower(), ctx.guild.members)
    return None


@bot.command(name="ban", aliases=["blupbum"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, hedef: str = None, *, sebep: str = "Sebep belirtilmedi"):
    target = await hedef_bul(ctx, hedef)
    if target is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}ban @uye [sebep]`, `{PREFIX}ban <id> [sebep]` veya mesaja yanit verip `{PREFIX}ban [sebep]`"))
        return
    if isinstance(target, discord.Member):
        guard = role_guard(ctx, target)
        if guard:
            await ctx.send(embed=error_embed("Islem Engellendi", guard))
            return
    if getattr(target, "id", None) == ctx.author.id:
        await ctx.send(embed=error_embed("Islem Engellendi", "Kendini banlayamazsin."))
        return
    try:
        await ctx.guild.ban(discord.Object(id=target.id), reason=f"{ctx.author}: {sebep}", delete_message_seconds=0)
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Ban Basarisiz", "Botun ban yetkisi veya rol sirasi yetersiz."))
        return
    except discord.HTTPException as exc:
        await ctx.send(embed=error_embed("Ban Basarisiz", short(exc)))
        return
    target_text = target.mention if isinstance(target, discord.Member) else f"`{target.id}`"
    e = embed("Uye Banlandi", f"**Hedef:** {target_text}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", RENK["hata"])
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "ban_log", e)


@bot.command(name="unban")
@commands.has_permissions(ban_members=True)
async def unban(ctx, kullanici_id: int = None, *, sebep: str = "Sebep belirtilmedi"):
    if kullanici_id is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}unban <kullanici_id> [sebep]`"))
        return
    try:
        await ctx.guild.unban(discord.Object(id=kullanici_id), reason=f"{ctx.author}: {sebep}")
    except discord.NotFound:
        await ctx.send(embed=error_embed("Bulunamadi", "Bu ID ban listesinde yok."))
        return
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Unban Basarisiz", "Botun ban kaldirma yetkisi yok."))
        return
    e = embed("Ban Kaldirildi", f"**Kullanici ID:** `{kullanici_id}`\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", RENK["basari"])
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "ban_log", e)


@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    if uye is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}kick @uye [sebep]`"))
        return
    guard = role_guard(ctx, uye)
    if guard:
        await ctx.send(embed=error_embed("Islem Engellendi", guard))
        return
    try:
        await uye.kick(reason=f"{ctx.author}: {sebep}")
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Kick Basarisiz", "Botun yetkisi veya rol sirasi yetersiz."))
        return
    e = embed("Uye Atildi", f"**Hedef:** {uye.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", RENK["hata"])
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mod_log", e)


@bot.command(name="mute", aliases=["timeout"])
@commands.has_permissions(moderate_members=True)
async def mute(ctx, uye: discord.Member = None, sure: str = "1h", *, sebep: str = "Sebep belirtilmedi"):
    if uye is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}mute @uye [10m/1h/1d] [sebep]`"))
        return
    guard = role_guard(ctx, uye)
    if guard:
        await ctx.send(embed=error_embed("Islem Engellendi", guard))
        return
    try:
        seconds = parse_duration(sure, 3600)
    except ValueError:
        sebep = f"{sure} {sebep}".strip()
        seconds = 3600
    until = utc_now() + timedelta(seconds=seconds)
    try:
        await uye.timeout(until, reason=f"{ctx.author}: {sebep}")
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Mute Basarisiz", "Botun timeout yetkisi veya rol sirasi yetersiz."))
        return
    e = embed("Uye Susturuldu", f"**Hedef:** {uye.mention}\n**Sure:** {format_duration(seconds)}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", RENK["mute"])
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mute_log", e)


@bot.command(name="unmute")
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    if uye is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}unmute @uye [sebep]`"))
        return
    try:
        await uye.timeout(None, reason=f"{ctx.author}: {sebep}")
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Unmute Basarisiz", "Botun yetkisi yetersiz."))
        return
    e = embed("Mute Kaldirildi", f"**Hedef:** {uye.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", RENK["basari"])
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mute_log", e)


@bot.command(name="sil", aliases=["temizle", "purge"])
@commands.has_permissions(manage_messages=True)
async def sil(ctx, adet: int = 5):
    adet = max(1, min(adet, 100))
    deleted = await ctx.channel.purge(limit=adet + 1)
    msg = await ctx.send(embed=embed("Mesajlar Silindi", f"**{max(0, len(deleted) - 1)}** mesaj silindi.", RENK["basari"]))
    await asyncio.sleep(4)
    try:
        await msg.delete()
    except discord.HTTPException:
        pass


def warnings_get(guild_id: int) -> dict:
    return guild_section(guild_id, "warnings", {})


@bot.command(name="warn")
@commands.has_permissions(manage_messages=True)
async def warn(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    if uye is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}warn @uye [sebep]`"))
        return
    def edit(data):
        g = data.setdefault(str(ctx.guild.id), {})
        warnings = g.setdefault("warnings", {})
        kayitlar = warnings.setdefault(str(uye.id), [])
        kayitlar.append({"sebep": sebep, "yetkili": ctx.author.id, "zaman": utc_now().isoformat()})
        return len(kayitlar)
    count = update_settings(edit)
    e = embed("Uye Uyarildi", f"**Hedef:** {uye.mention}\n**Toplam Uyari:** `{count}`\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", RENK["uyari"])
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mod_log", e)


@bot.command(name="uyarlar", aliases=["warnings", "uyarilar"])
async def uyarlar(ctx, uye: discord.Member = None):
    uye = uye or ctx.author
    kayitlar = warnings_get(ctx.guild.id).get(str(uye.id), [])
    if not kayitlar:
        await ctx.send(embed=embed("Uyari Yok", f"{uye.mention} icin kayitli uyari yok.", RENK["basari"]))
        return
    e = embed("Uyari Listesi", f"{uye.mention} icin **{len(kayitlar)}** uyari.", RENK["uyari"])
    for i, item in enumerate(kayitlar[-10:], start=max(1, len(kayitlar) - 9)):
        yetkili = item.get("yetkili", "Bilinmiyor") if isinstance(item, dict) else "Bilinmiyor"
        sebep = item.get("sebep", item) if isinstance(item, dict) else item
        e.add_field(name=f"#{i}", value=f"Sebep: {short(sebep, 300)}\nYetkili: <@{yetkili}>", inline=False)
    await ctx.send(embed=e)


@bot.command(name="uyarsil", aliases=["uyarisil", "clearwarns"])
@commands.has_permissions(manage_messages=True)
async def uyarsil(ctx, uye: discord.Member = None):
    if uye is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}uyarsil @uye`"))
        return
    def edit(data):
        data.setdefault(str(ctx.guild.id), {}).setdefault("warnings", {}).pop(str(uye.id), None)
    update_settings(edit)
    await ctx.send(embed=embed("Uyarilar Silindi", f"{uye.mention} icin tum uyarilar temizlendi.", RENK["basari"]))


@bot.command(name="lock", aliases=["kilit"])
@commands.has_permissions(manage_channels=True)
async def lock(ctx, kanal: discord.TextChannel = None):
    kanal = kanal or ctx.channel
    await kanal.set_permissions(ctx.guild.default_role, send_messages=False, reason=f"{ctx.author} kanal kilitledi")
    await ctx.send(embed=embed("Kanal Kilitlendi", f"{kanal.mention} yazmaya kapatildi.", RENK["uyari"]))


@bot.command(name="unlock", aliases=["kilitac"])
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, kanal: discord.TextChannel = None):
    kanal = kanal or ctx.channel
    await kanal.set_permissions(ctx.guild.default_role, send_messages=None, reason=f"{ctx.author} kanal acti")
    await ctx.send(embed=embed("Kanal Acildi", f"{kanal.mention} tekrar yazmaya acildi.", RENK["basari"]))


@bot.command(name="slowmode", aliases=["sm"])
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, sure: int = 0):
    sure = max(0, min(sure, 21600))
    await ctx.channel.edit(slowmode_delay=sure, reason=f"{ctx.author} slowmode ayarladi")
    await ctx.send(embed=embed("Slowmode Ayarlandi", f"Bu kanalda yavas mod **{sure} saniye** oldu.", RENK["basari"]))


@bot.command(name="duyuru", aliases=["announce"])
@commands.has_permissions(manage_messages=True)
async def duyuru(ctx, kanal: discord.TextChannel = None, *, mesaj: str = None):
    if kanal is None or mesaj is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}duyuru #kanal mesaj [gif/resim linki]`"))
        return
    image_url = None
    image_match = re.search(r"(https?://\S+\.(?:gif|png|jpe?g|webp)(?:\?\S*)?)", mesaj, re.I)
    if image_match:
        image_url = image_match.group(1)
        mesaj = mesaj.replace(image_url, "").strip()
    e = embed("Duyuru", mesaj or "Yeni duyuru", RENK["mod"])
    if ctx.guild.icon:
        e.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
    else:
        e.set_author(name=ctx.guild.name)
    if image_url:
        e.set_image(url=image_url)
    if ctx.author.display_avatar:
        e.set_footer(text=f"Duyuran: {ctx.author} | {timestamp()}", icon_url=ctx.author.display_avatar.url)
    await kanal.send(embed=e)
    await ctx.send(embed=embed("Duyuru Gonderildi", f"Duyuru {kanal.mention} kanalina gonderildi.", RENK["basari"]))


@bot.command(name="kufur-kur")
@commands.has_permissions(manage_guild=True)
async def kufur_kur(ctx, *, kelimeler: str = None):
    liste = [k.strip().lower() for k in kelimeler.split(",")] if kelimeler else sorted(KUFUR_KELIMELERI)
    set_guild_section(ctx.guild.id, "kufur_koruma", {"aktif": True, "kelimeler": liste})
    await ctx.send(embed=embed("Kufur Koruma Aktif", f"**{len(liste)}** kelime ile koruma acildi.", RENK["basari"]))


@bot.command(name="kufur-kapat")
@commands.has_permissions(manage_guild=True)
async def kufur_kapat(ctx):
    set_guild_section(ctx.guild.id, "kufur_koruma", {"aktif": False, "kelimeler": []})
    await ctx.send(embed=embed("Kufur Koruma Kapali", "Kufur korumasi kapatildi.", RENK["uyari"]))


@bot.command(name="link-koruma-aktif", aliases=["antilink"])
@commands.has_permissions(manage_guild=True)
async def link_koruma_aktif(ctx):
    ayar = guild_section(ctx.guild.id, "link_koruma", {"muaf_roller": [], "muaf_kanallar": []})
    ayar["aktif"] = True
    set_guild_section(ctx.guild.id, "link_koruma", ayar)
    await ctx.send(embed=embed("Link Koruma Aktif", "Linkler muaf roller/kanallar haricinde silinecek.", RENK["basari"]))


@bot.command(name="link-koruma-kapat")
@commands.has_permissions(manage_guild=True)
async def link_koruma_kapat(ctx):
    ayar = guild_section(ctx.guild.id, "link_koruma", {})
    ayar["aktif"] = False
    set_guild_section(ctx.guild.id, "link_koruma", ayar)
    await ctx.send(embed=embed("Link Koruma Kapali", "Link korumasi kapatildi.", RENK["uyari"]))


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
        durum = "cikarildi"
    else:
        roller.add(rol.id)
        durum = "eklendi"
    ayar["muaf_roller"] = list(roller)
    set_guild_section(ctx.guild.id, "link_koruma", ayar)
    await ctx.send(embed=embed("Muaf Rol Guncellendi", f"{rol.mention} muaf rol listesine {durum}.", RENK["bilgi"]))


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
        durum = "cikarildi"
    else:
        kanallar.add(kanal.id)
        durum = "eklendi"
    ayar["muaf_kanallar"] = list(kanallar)
    set_guild_section(ctx.guild.id, "link_koruma", ayar)
    await ctx.send(embed=embed("Muaf Kanal Guncellendi", f"{kanal.mention} muaf kanal listesine {durum}.", RENK["bilgi"]))


@bot.command(name="spam-koruma-kur")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_kur(ctx, max_mesaj: int = 5, saniye: int = 8, mute_saniye: int = 300):
    ayar = {"aktif": True, "max_mesaj": max(2, max_mesaj), "saniye": max(3, saniye), "mute_saniye": max(10, mute_saniye), "muaf_roller": [], "muaf_kanallar": []}
    set_guild_section(ctx.guild.id, "spam_koruma", ayar)
    await ctx.send(embed=embed("Spam Koruma Aktif", f"{ayar['saniye']} saniyede {ayar['max_mesaj']} mesaj ustu timeout: {format_duration(ayar['mute_saniye'])}.", RENK["basari"]))


@bot.command(name="spam-koruma-kapat")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_kapat(ctx):
    ayar = guild_section(ctx.guild.id, "spam_koruma", {})
    ayar["aktif"] = False
    set_guild_section(ctx.guild.id, "spam_koruma", ayar)
    await ctx.send(embed=embed("Spam Koruma Kapali", "Spam korumasi kapatildi.", RENK["uyari"]))


@bot.command(name="spam-koruma-durum")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_durum(ctx):
    ayar = guild_section(ctx.guild.id, "spam_koruma", {})
    durum = "Aktif" if ayar.get("aktif") else "Kapali"
    await ctx.send(embed=embed("Spam Koruma Durumu", f"Durum: **{durum}**\nLimit: `{ayar.get('max_mesaj', 5)}` mesaj / `{ayar.get('saniye', 8)}` saniye", RENK["bilgi"]))


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
    await ctx.send(embed=embed("Jail Sistemi Kuruldu", f"Jail kanali: {kanal.mention}\nJail rolu: {jail_rol.mention}\nYetki rolu: {yetki_rol.mention}", RENK["basari"]))


def jail_yetkili(member: discord.Member) -> bool:
    ayar = guild_section(member.guild.id, "jail_sistemi", {})
    yetki_rol_id = ayar.get("yetki_rol_id")
    return member.guild_permissions.administrator or any(r.id == yetki_rol_id for r in member.roles)


@bot.command(name="jail")
async def jail(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    if uye is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}jail @uye [sebep]`"))
        return
    if not jail_yetkili(ctx.author):
        await ctx.send(embed=error_embed("Yetki Hatasi", "Bu komut icin jail yetki rolune sahip olmalisin."))
        return
    guard = role_guard(ctx, uye)
    if guard:
        await ctx.send(embed=error_embed("Islem Engellendi", guard))
        return
    ayar = guild_section(ctx.guild.id, "jail_sistemi", {})
    jail_rol = ctx.guild.get_role(int(ayar.get("jail_rol_id") or 0))
    if not ayar.get("aktif") or jail_rol is None:
        await ctx.send(embed=error_embed("Jail Hazir Degil", f"Once `{PREFIX}jailkur #kanal @rol` kullan."))
        return
    eski_roller = [r.id for r in uye.roles if r != ctx.guild.default_role and r.id != jail_rol.id]
    try:
        await uye.edit(roles=[jail_rol], reason=f"{ctx.author}: {sebep}")
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Jail Basarisiz", "Botun rol sirasi yetersiz."))
        return
    ayar.setdefault("kayitlar", {})[str(uye.id)] = {"roller": eski_roller, "sebep": sebep, "yetkili": ctx.author.id, "zaman": utc_now().isoformat()}
    set_guild_section(ctx.guild.id, "jail_sistemi", ayar)
    e = embed("Uye Jaile Atildi", f"**Hedef:** {uye.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", RENK["hata"])
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mod_log", e)


@bot.command(name="unjail")
async def unjail(ctx, uye: discord.Member = None):
    if uye is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}unjail @uye`"))
        return
    if not jail_yetkili(ctx.author):
        await ctx.send(embed=error_embed("Yetki Hatasi", "Bu komut icin jail yetki rolune sahip olmalisin."))
        return
    ayar = guild_section(ctx.guild.id, "jail_sistemi", {})
    kayit = ayar.get("kayitlar", {}).get(str(uye.id))
    if not kayit:
        await ctx.send(embed=error_embed("Kayit Yok", "Bu uye icin jail kaydi bulunamadi."))
        return
    roller = [ctx.guild.get_role(int(rid)) for rid in kayit.get("roller", [])]
    roller = [r for r in roller if r and r < ctx.guild.me.top_role]
    try:
        await uye.edit(roles=roller, reason=f"{ctx.author} jail kaldirdi")
    except discord.Forbidden:
        await ctx.send(embed=error_embed("Unjail Basarisiz", "Botun rol sirasi yetersiz."))
        return
    ayar["kayitlar"].pop(str(uye.id), None)
    set_guild_section(ctx.guild.id, "jail_sistemi", ayar)
    e = embed("Jail Kaldirildi", f"{uye.mention} icin eski roller geri verildi.", RENK["basari"])
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mod_log", e)


@bot.command(name="jailkapat")
@commands.has_permissions(administrator=True)
async def jailkapat(ctx):
    set_guild_section(ctx.guild.id, "jail_sistemi", {"aktif": False, "kayitlar": {}})
    await ctx.send(embed=embed("Jail Sistemi Kapatildi", "Jail ayarlari temizlendi.", RENK["uyari"]))


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
    await ctx.send(embed=embed("AFK Modu Acildi", f"{ctx.author.mention} artik AFK.\n**Sebep:** {sebep}", RENK["bilgi"]))


async def afk_cikar(message: discord.Message, kayit: dict):
    old_nick = kayit.get("old_nick")
    try:
        await message.author.edit(nick=old_nick, reason="AFK modu kapandi")
    except discord.Forbidden:
        pass
    def edit(data):
        data.setdefault(str(message.guild.id), {}).setdefault("afk_users", {}).pop(str(message.author.id), None)
    update_settings(edit)
    await message.channel.send(embed=embed("AFK Modu Kapandi", f"{message.author.mention}, tekrar hos geldin. AFK modundan ciktin.", RENK["basari"]))


class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Ticket Ac", style=discord.ButtonStyle.primary, custom_id="ticket_ac")
    async def ticket_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        ayar = guild_section(interaction.guild_id, "ticket_sistemi", {})
        kategori = interaction.guild.get_channel(int(ayar.get("kategori_id") or 0))
        log_kanal = interaction.guild.get_channel(int(ayar.get("log_kanal_id") or 0))
        if not isinstance(kategori, discord.CategoryChannel):
            await interaction.response.send_message(embed=error_embed("Ticket Hazir Degil", "Ticket kategorisi bulunamadi."), ephemeral=True)
            return
        for ch in kategori.text_channels:
            if ch.topic == f"ticket-owner:{interaction.user.id}":
                await interaction.response.send_message(embed=error_embed("Zaten Acik", f"Zaten acik ticketin var: {ch.mention}"), ephemeral=True)
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
        await kanal.send(embed=embed("Ticket Acildi", f"{interaction.user.mention}, destek ekibi birazdan ilgilenecek.", RENK["basari"]), view=TicketCloseView())
        await interaction.response.send_message(embed=embed("Ticket Acildi", kanal.mention, RENK["basari"]), ephemeral=True)
        if isinstance(log_kanal, discord.TextChannel):
            await log_kanal.send(embed=embed("Ticket Acildi", f"Uye: {interaction.user.mention}\nKanal: {kanal.mention}", RENK["bilgi"]))


class TicketCloseView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Ticket Kapat", style=discord.ButtonStyle.danger, custom_id="ticket_kapat")
    async def ticket_kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not isinstance(interaction.channel, discord.TextChannel) or not interaction.channel.name.startswith("ticket-"):
            await interaction.response.send_message(embed=error_embed("Gecersiz Kanal", "Bu buton sadece ticket kanalinda kullanilir."), ephemeral=True)
            return
        await interaction.response.send_message(embed=embed("Ticket Kapatiliyor", "Kanal 5 saniye icinde silinecek.", RENK["uyari"]))
        await asyncio.sleep(5)
        await interaction.channel.delete(reason=f"{interaction.user} ticket kapatti")


@bot.command(name="ticketkur", aliases=["ticket-kur"])
@commands.has_permissions(manage_guild=True)
async def ticketkur(ctx, kategori: discord.CategoryChannel = None, log: discord.TextChannel = None, destek_rol: discord.Role = None):
    if kategori is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}ticketkur <kategori> [log-kanali] [destek-rolu]`"))
        return
    set_guild_section(ctx.guild.id, "ticket_sistemi", {"kategori_id": kategori.id, "log_kanal_id": log.id if log else None, "destek_rol_id": destek_rol.id if destek_rol else None})
    await ctx.send(embed=embed("Ticket Sistemi Kuruldu", f"Kategori: **{kategori.name}**\nLog: {log.mention if log else 'Yok'}\nDestek: {destek_rol.mention if destek_rol else 'Yok'}", RENK["basari"]))


@bot.command(name="ticketpanel", aliases=["ticket-panel"])
@commands.has_permissions(manage_guild=True)
async def ticketpanel(ctx):
    await ctx.send(embed=embed("Destek Talebi", "Ticket acmak icin asagidaki butona bas.", RENK["bilgi"]), view=TicketView())


@bot.command(name="ticketkapat", aliases=["ticket-kapat"])
async def ticketkapat(ctx):
    if not ctx.channel.name.startswith("ticket-"):
        await ctx.send(embed=error_embed("Gecersiz Kanal", "Bu komut sadece ticket kanalinda kullanilir."))
        return
    await ctx.send(embed=embed("Ticket Kapatiliyor", "Kanal 5 saniye icinde silinecek.", RENK["uyari"]))
    await asyncio.sleep(5)
    await ctx.channel.delete(reason=f"{ctx.author} ticket kapatti")


@bot.command(name="ticketekle", aliases=["ticket-ekle"])
async def ticketekle(ctx, uye: discord.Member = None):
    if uye is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}ticketekle @uye`"))
        return
    await ctx.channel.set_permissions(uye, view_channel=True, send_messages=True, read_message_history=True)
    await ctx.send(embed=embed("Uye Eklendi", f"{uye.mention} tickete eklendi.", RENK["basari"]))


@bot.command(name="ticketcikar", aliases=["ticket-cikar"])
async def ticketcikar(ctx, uye: discord.Member = None):
    if uye is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}ticketcikar @uye`"))
        return
    await ctx.channel.set_permissions(uye, overwrite=None)
    await ctx.send(embed=embed("Uye Cikarildi", f"{uye.mention} ticketten cikarildi.", RENK["uyari"]))


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
    winners_text = " ".join(u.mention for u in winners) if winners else "Kazanan yok"
    end_embed = embed("Cekilis Bitti", f"**Odul:** {data.get('prize')}\n**Kazanan:** {winners_text}\n**Katilimci:** {len(users)}", RENK["mod"])
    try:
        await msg.edit(embed=end_embed)
    except discord.HTTPException:
        pass
    giveaway_set(guild_id, message_id, None)
    if winners:
        await channel.send(embed=embed("Tebrikler", f"{winners_text}\n**{data.get('prize')}** kazandiniz.", RENK["basari"]))
    elif forced:
        await channel.send(embed=embed("Cekilis Bitirildi", "Katilimci olmadigi icin kazanan secilemedi.", RENK["uyari"]))


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
async def gstart(ctx, sure: str = None, kazanan: int = 1, *, odul: str = None):
    if sure is None or odul is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}gstart 10m 1 Nitro`\nCekilisler nokta prefix ile calisir."))
        return
    try:
        seconds = parse_duration(sure)
    except ValueError:
        await ctx.send(embed=error_embed("Gecersiz Sure", "Ornek sureler: `30s`, `10m`, `2h`, `1d`."))
        return
    ends_at = utc_now() + timedelta(seconds=seconds)
    e = embed("Cekilis Basladi", f"**Odul:** {odul}\n**Kazanan:** {kazanan}\n**Bitis:** <t:{int(ends_at.timestamp())}:R>\n**Komut:** `{PREFIX}gstart`\n\nKatilmak icin {GIVEAWAY_EMOJI} tepkisine bas.", RENK["mod"])
    msg = await ctx.send(embed=e)
    await msg.add_reaction(GIVEAWAY_EMOJI)
    giveaway_set(ctx.guild.id, msg.id, {"channel_id": ctx.channel.id, "prize": odul, "winners": max(1, kazanan), "ends_at": ends_at.isoformat(), "host_id": ctx.author.id})
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
        await ctx.send(embed=usage_embed(f"`{PREFIX}greroll <mesaj_id> [kazanan]`"))
        return
    try:
        msg = await ctx.channel.fetch_message(mesaj_id)
    except discord.HTTPException:
        await ctx.send(embed=error_embed("Mesaj Yok", "Cekilis mesaji bulunamadi."))
        return
    reaction = discord.utils.get(msg.reactions, emoji=GIVEAWAY_EMOJI)
    users = [u async for u in reaction.users() if not u.bot] if reaction else []
    if not users:
        await ctx.send(embed=error_embed("Katilimci Yok", "Yeni kazanan secilecek katilimci yok."))
        return
    winners = random.sample(users, min(max(1, kazanan), len(users)))
    await ctx.send(embed=embed("Cekilis Yenilendi", f"Yeni kazanan: {' '.join(u.mention for u in winners)}", RENK["basari"]))


@bot.command(name="glist", aliases=["katilimcilar", "çekilişkatılımcı"])
async def glist(ctx, mesaj_id: int = None):
    if mesaj_id is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}glist <mesaj_id>`"))
        return
    try:
        msg = await ctx.channel.fetch_message(mesaj_id)
    except discord.HTTPException:
        await ctx.send(embed=error_embed("Mesaj Yok", "Cekilis mesaji bulunamadi."))
        return
    reaction = discord.utils.get(msg.reactions, emoji=GIVEAWAY_EMOJI)
    users = [u async for u in reaction.users() if not u.bot] if reaction else []
    text = "\n".join(f"`{i}.` {u.mention}" for i, u in enumerate(users[:30], 1)) or "Katilimci yok."
    await ctx.send(embed=embed("Cekilis Katilimcilari", text, RENK["bilgi"]))


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
    await ctx.send(embed=embed("Cekilis Iptal Edildi", "Cekilis mesaji silindi veya kaydi temizlendi.", RENK["uyari"]))


@bot.command(name="ginfo", aliases=["cekilisbilgi", "çekilişbilgi"])
async def ginfo(ctx, mesaj_id: int = None):
    if mesaj_id is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}ginfo <mesaj_id>`"))
        return
    data = giveaway_get(ctx.guild.id).get(str(mesaj_id))
    if not data:
        await ctx.send(embed=error_embed("Kayit Yok", "Bu mesaj ID'si icin aktif cekilis kaydi yok."))
        return
    end_time = datetime.fromisoformat(data["ends_at"])
    await ctx.send(embed=embed("Cekilis Bilgisi", f"**Odul:** {data.get('prize')}\n**Kazanan:** {data.get('winners')}\n**Bitis:** <t:{int(end_time.timestamp())}:R>", RENK["bilgi"]))


@bot.command(name="avatar")
async def avatar(ctx, uye: discord.Member = None):
    uye = uye or ctx.author
    e = embed("Avatar", f"{uye.mention} avatar linki", RENK["bilgi"])
    e.set_image(url=uye.display_avatar.url)
    await ctx.send(embed=e)


@bot.command(name="sunucu", aliases=["serverinfo"])
async def sunucu(ctx):
    g = ctx.guild
    e = embed("Sunucu Bilgisi", g.name, RENK["bilgi"])
    e.add_field(name="Uyeler", value=str(g.member_count), inline=True)
    e.add_field(name="Kanallar", value=str(len(g.channels)), inline=True)
    e.add_field(name="Roller", value=str(len(g.roles)), inline=True)
    e.add_field(name="Kurulus", value=g.created_at.strftime("%d.%m.%Y"), inline=True)
    if g.icon:
        e.set_thumbnail(url=g.icon.url)
    await ctx.send(embed=e)


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(embed=embed("Pong", f"Gecikme: `{round(bot.latency * 1000)}ms`", RENK["basari"]))


@bot.command(name="yardim", aliases=["yardım", "help", "komutlar"])
async def yardim(ctx):
    e = embed("Komutlar", "Temiz moderasyon surumu aktif.", RENK["bilgi"])
    e.add_field(name="Moderasyon", value="`ban`, `unban`, `kick`, `mute`, `unmute`, `sil`, `warn`, `uyarlar`, `uyarsil`, `jail`, `unjail`, `lock`, `unlock`, `slowmode`", inline=False)
    e.add_field(name="Koruma", value="`kufur-kur`, `kufur-kapat`, `link-koruma-aktif`, `link-koruma-kapat`, `spam-koruma-kur`, `spam-koruma-kapat`, `spam-koruma-durum`", inline=False)
    e.add_field(name="Sistem", value="`ticketkur`, `ticketpanel`, `ticketkapat`, `afk`, `gstart`, `gend`, `greroll`, `glist`, `gdelete`, `ginfo`, `logkur`, `log-kur`, `log-kaldir`, `log-durum`", inline=False)
    e.add_field(name="Duyuru", value=f"`{PREFIX}duyuru #kanal mesaj gif-linki`", inline=False)
    await ctx.send(embed=e)


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
                    since_text = f"\n**AFK olma zamani:** <t:{int(datetime.fromisoformat(since).timestamp())}:R>"
                except Exception:
                    pass
            await message.channel.send(embed=embed("Bu Uye AFK", f"{member.mention} su anda AFK.\n**Sebep:** {kayit.get('sebep', 'AFK')}{since_text}", RENK["uyari"]))

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
            e = error_embed("Kufur Engellendi", f"{message.author.mention}, kufur kullanimi yasak.")
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
            e = error_embed("Link Engellendi", f"{message.author.mention}, bu kanalda link paylasamazsin.")
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
                await message.author.timeout(utc_now() + timedelta(seconds=seconds), reason="Spam koruma")
            except discord.HTTPException:
                pass
            e = embed("Spam Cezasi", f"{message.author.mention} spam nedeniyle **{format_duration(seconds)}** susturuldu.", RENK["mute"])
            await message.channel.send(embed=e, delete_after=10)
            await log_gonder(message.guild, "mute_log", e)
            spam_cache[key] = []


@bot.event
async def on_member_ban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_user(guild, discord.AuditLogAction.ban, user)
    e = embed("Ban Logu", f"**Kullanici:** {user} (`{user.id}`)\n**Yetkili:** {sorumlu.mention if sorumlu else 'Bilinmiyor'}", RENK["hata"])
    await log_gonder(guild, "ban_log", e)


@bot.event
async def on_member_unban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_user(guild, discord.AuditLogAction.unban, user)
    e = embed("Unban Logu", f"**Kullanici:** {user} (`{user.id}`)\n**Yetkili:** {sorumlu.mention if sorumlu else 'Bilinmiyor'}", RENK["basari"])
    await log_gonder(guild, "ban_log", e)


@bot.event
async def on_member_join(member: discord.Member):
    await log_gonder(member.guild, "giris_cikis", embed("Uye Katildi", f"{member.mention} sunucuya katildi.\nID: `{member.id}`", RENK["basari"]))


@bot.event
async def on_member_remove(member: discord.Member):
    await log_gonder(member.guild, "giris_cikis", embed("Uye Ayrildi", f"{member} sunucudan ayrildi.\nID: `{member.id}`", RENK["uyari"]))


@bot.event
async def on_message_delete(message: discord.Message):
    if message.author.bot or not message.guild:
        return
    e = embed("Mesaj Silindi", f"**Kullanici:** {message.author.mention}\n**Kanal:** {message.channel.mention}\n**Mesaj:** {short(message.content or 'Icerik yok', 900)}", RENK["uyari"])
    await log_gonder(message.guild, "mesaj_log", e)


@bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    if before.author.bot or not before.guild or before.content == after.content:
        return
    e = embed("Mesaj Duzenlendi", f"**Kullanici:** {before.author.mention}\n**Kanal:** {before.channel.mention}\n**Once:** {short(before.content, 450)}\n**Sonra:** {short(after.content, 450)}", RENK["bilgi"])
    await log_gonder(before.guild, "mesaj_log", e)


@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    if before.timed_out_until != after.timed_out_until:
        if after.timed_out_until:
            e = embed("Timeout Verildi", f"**Uye:** {after.mention}\n**Bitis:** <t:{int(after.timed_out_until.timestamp())}:R>", RENK["mute"])
        else:
            e = embed("Timeout Kaldirildi", f"**Uye:** {after.mention}", RENK["basari"])
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
            text += "Alinan: " + ", ".join(r.mention for r in removed)
        await log_gonder(after.guild, "rol_log", embed("Rol Degisikligi", f"**Uye:** {after.mention}\n{text}", RENK["mod"]))


@bot.event
async def on_guild_channel_create(channel):
    await log_gonder(channel.guild, "kanal_log", embed("Kanal Olusturuldu", f"**Kanal:** {channel.mention if hasattr(channel, 'mention') else channel.name}", RENK["basari"]))


@bot.event
async def on_guild_channel_delete(channel):
    await log_gonder(channel.guild, "kanal_log", embed("Kanal Silindi", f"**Kanal:** {channel.name}", RENK["hata"]))


@bot.event
async def on_guild_role_create(role: discord.Role):
    await log_gonder(role.guild, "rol_log", embed("Rol Olusturuldu", f"**Rol:** {role.mention}", RENK["basari"]))


@bot.event
async def on_guild_role_delete(role: discord.Role):
    await log_gonder(role.guild, "rol_log", embed("Rol Silindi", f"**Rol:** {role.name}", RENK["hata"]))


@bot.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    if before.channel == after.channel:
        return
    if before.channel is None and after.channel is not None:
        text = f"{member.mention} {after.channel.mention} kanalina girdi."
    elif before.channel is not None and after.channel is None:
        text = f"{member.mention} {before.channel.mention} kanalindan cikti."
    else:
        text = f"{member.mention} {before.channel.mention} -> {after.channel.mention}"
    await log_gonder(member.guild, "ses_log", embed("Ses Logu", text, RENK["bilgi"]))


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
    print(f"[BOT] Giris yapildi: {bot.user} | Prefix: {PREFIX} | Settings: {SETTINGS_FILE}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=error_embed("Yetki Hatasi", "Bu komutu kullanmak icin yeterli yetkin yok."))
        return
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send(embed=error_embed("Bot Yetkisi Eksik", "Botun bu islem icin gerekli yetkisi yok."))
        return
    if isinstance(error, commands.BadArgument):
        await ctx.send(embed=error_embed("Gecersiz Arguman", "Komuttaki uye/rol/kanal veya sayi hatali."))
        return
    await ctx.send(embed=error_embed("Komut Hatasi", short(error)))
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
