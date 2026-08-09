import asyncio
import json
import os
import random
import re
import threading
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import aiofiles
import discord
from discord.ext import commands
from flask import Flask, jsonify


BASE_DIR = Path(__file__).resolve().parent
SETTINGS_FILE = BASE_DIR / "settings.json"

TOKEN = os.getenv("DISCORD_TOKEN") or os.getenv("BOT_TOKEN") or "BURAYA_BOT_TOKEN_YAZ"
PREFIX = os.getenv("BOT_PREFIX", ".")

if not TOKEN or TOKEN == "BURAYA_BOT_TOKEN_YAZ":
    raise ValueError("DISCORD_TOKEN veya BOT_TOKEN env ayarla ya da logbot.py icindeki token alanini doldur.")


# Tüm Embed Renkleri Mavi (Dodger Blue / Royal Blue)
MAVI = 0x3498DB

RENK = {
    "basari": MAVI,
    "hata": MAVI,
    "bilgi": MAVI,
    "uyari": MAVI,
    "mod": MAVI,
    "mute": MAVI,
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


def embed(title: str, description: str = "", color: int = MAVI) -> discord.Embed:
    e = discord.Embed(title=title, description=description, color=MAVI, timestamp=utc_now())
    e.set_footer(text=timestamp())
    return e


def error_embed(title: str, description: str) -> discord.Embed:
    return embed(title, description, MAVI)


def usage_embed(text: str) -> discord.Embed:
    return embed("Kullanım Rehberi", text, MAVI)


def short(text: str, limit: int = 1024) -> str:
    text = str(text or "")
    return text if len(text) <= limit else text[: limit - 3] + "..."


def parse_id(val: str) -> int | None:
    clean = re.sub(r"\D", "", str(val or ""))
    return int(clean) if clean and len(clean) >= 15 else None


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
            except (discord.HTTPException, NotFound):
                return discord.Object(id=int(clean_id)), args_list[1:]

        found = discord.utils.find(
            lambda m: m.name.lower() == first_arg.lower() or str(m).lower() == first_arg.lower() or getattr(m, "display_name", "").lower() == first_arg.lower(),
            ctx.guild.members
        )
        if found:
            return found, args_list[1:]

    return None, args_list


def format_welcome_text(text: str, member: discord.Member, role_id: str | None = None, is_dis_mesaj: bool = False) -> str:
    """Hoş geldin mesajlarındaki değişkenleri değiştirir. Rol etiketi SADECE dış mesajda (is_dis_mesaj=True) işlenir."""
    if not text:
        return ""
    created_at = member.created_at.strftime("%d.%m.%Y")

    clean_role_id = re.sub(r"\D", "", str(role_id or ""))
    role_mention = f"<@&{clean_role_id}>" if clean_role_id else ""

    replacements = {
        "{uye}": member.mention,
        "{uye_etiket}": member.mention,
        "{uye_adi}": member.name,
        "{uye_id}": str(member.id),
        "{sunucu}": member.guild.name,
        "{sunucu_adi}": member.guild.name,
        "{uye_sayisi}": str(member.guild.member_count),
        "{hesap_tarihi}": created_at,
    }

    if is_dis_mesaj:
        replacements["{rol}"] = role_mention
        replacements["{rol_etiket}"] = role_mention
    else:
        replacements["{rol}"] = ""
        replacements["{rol_etiket}"] = ""

    for key, val in replacements.items():
        text = text.replace(key, val)

    # Rol etiketi SADECE dış mesajda (is_dis_mesaj=True) etiket olarak eklenir!
    if is_dis_mesaj and role_mention and role_mention not in text:
        text = f"{text} {role_mention}".strip()

    return text


# ==========================================
# TRANSCRIPT FONKSİYONU
# ==========================================

async def create_transcript(channel: discord.TextChannel, ticket_owner: discord.Member, closer: discord.Member):
    """Ticket kanalındaki tüm mesajları HTML transkript olarak oluşturur."""
    messages = []
    async for msg in channel.history(limit=None, oldest_first=True):
        messages.append(msg)
    
    if not messages:
        return None
    
    # HTML şablonu
    html_template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ticket Transkript - {channel_name}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #36393f;
            color: #dcddde;
            padding: 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: #2f3136;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }}
        .header {{
            background: #202225;
            padding: 25px 30px;
            border-bottom: 2px solid #1a1b1e;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }}
        .header h1 {{
            font-size: 24px;
            color: #ffffff;
            font-weight: 600;
        }}
        .header .info {{
            color: #b9bbbe;
            font-size: 14px;
        }}
        .header .info span {{
            color: #dcddde;
            font-weight: 500;
        }}
        .messages {{
            padding: 20px 30px;
        }}
        .message {{
            display: flex;
            padding: 8px 0;
            border-bottom: 1px solid rgba(255,255,255,0.03);
            gap: 16px;
            align-items: flex-start;
        }}
        .message:last-child {{
            border-bottom: none;
        }}
        .message .avatar {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            flex-shrink: 0;
            background: #5865f2;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            color: #ffffff;
            font-size: 16px;
            text-transform: uppercase;
        }}
        .message .avatar.bot {{
            background: #3ba55c;
        }}
        .message .content {{
            flex: 1;
            min-width: 0;
        }}
        .message .author {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .message .author .name {{
            font-weight: 600;
            color: #ffffff;
            font-size: 15px;
        }}
        .message .author .timestamp {{
            color: #72767d;
            font-size: 12px;
        }}
        .message .author .badge {{
            background: #5865f2;
            color: #ffffff;
            font-size: 10px;
            padding: 1px 8px;
            border-radius: 10px;
            font-weight: 500;
        }}
        .message .author .badge.bot-badge {{
            background: #3ba55c;
        }}
        .message .text {{
            color: #dcddde;
            font-size: 15px;
            word-wrap: break-word;
            margin-top: 2px;
        }}
        .message .text .embed {{
            background: #2f3136;
            border-left: 4px solid #5865f2;
            padding: 10px 14px;
            border-radius: 4px;
            margin-top: 6px;
        }}
        .message .text .embed-title {{
            font-weight: 600;
            color: #ffffff;
        }}
        .message .text .embed-desc {{
            color: #dcddde;
            margin-top: 4px;
        }}
        .footer {{
            background: #202225;
            padding: 15px 30px;
            text-align: center;
            color: #72767d;
            font-size: 13px;
            border-top: 2px solid #1a1b1e;
        }}
        .footer a {{
            color: #5865f2;
            text-decoration: none;
        }}
        .footer a:hover {{
            text-decoration: underline;
        }}
        .message .text a {{
            color: #00aaff;
            text-decoration: none;
        }}
        .message .text a:hover {{
            text-decoration: underline;
        }}
        @media (max-width: 600px) {{
            .messages {{
                padding: 12px 15px;
            }}
            .header {{
                padding: 15px 20px;
            }}
            .header h1 {{
                font-size: 18px;
            }}
            .message .avatar {{
                width: 32px;
                height: 32px;
                font-size: 12px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <h1>📜 Ticket Transkripti</h1>
                <div class="info">
                    <span>Kanal:</span> #{channel_name} &bull; 
                    <span>Oluşturan:</span> {ticket_owner} &bull; 
                    <span>Kapatan:</span> {closer}
                </div>
            </div>
            <div class="info">
                <span>Mesaj Sayısı:</span> {message_count} &bull; 
                <span>Tarih:</span> {date}
            </div>
        </div>
        <div class="messages">
            {messages_html}
        </div>
        <div class="footer">
            Transkript oluşturulma tarihi: {date} &bull; 
            <a href="#">LogBot Ticket Sistemi</a>
        </div>
    </div>
</body>
</html>"""
    
    messages_html = ""
    for msg in messages:
        is_bot = msg.author.bot
        avatar_letter = msg.author.display_name[0].upper() if msg.author.display_name else "?"
        avatar_class = "bot" if is_bot else ""
        badge = '<span class="badge bot-badge">BOT</span>' if is_bot else ''
        
        # Mesaj içeriğini temizle ve kaçış karakterlerini dönüştür
        content = msg.content or ""
        content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        
        # Embed varsa göster
        embed_html = ""
        if msg.embeds:
            for embed_obj in msg.embeds:
                embed_title = embed_obj.title or ""
                embed_desc = embed_obj.description or ""
                embed_html += f'''
                <div class="embed">
                    <div class="embed-title">{embed_title}</div>
                    <div class="embed-desc">{embed_desc}</div>
                </div>
                '''
        
        # Ek dosyalar (attachment)
        attachment_html = ""
        if msg.attachments:
            for att in msg.attachments:
                if att.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                    attachment_html += f'<div><a href="{att.url}" target="_blank">🖼️ {att.filename}</a></div>'
                else:
                    attachment_html += f'<div><a href="{att.url}" target="_blank">📎 {att.filename}</a></div>'
        
        timestamp = msg.created_at.strftime("%d.%m.%Y %H:%M")
        
        messages_html += f'''
        <div class="message">
            <div class="avatar {avatar_class}">{avatar_letter}</div>
            <div class="content">
                <div class="author">
                    <span class="name">{msg.author.display_name}</span>
                    <span class="timestamp">{timestamp}</span>
                    {badge}
                </div>
                <div class="text">
                    {content}
                    {embed_html}
                    {attachment_html}
                </div>
            </div>
        </div>
        '''
    
    # HTML'i doldur
    html_content = html_template.format(
        channel_name=channel.name,
        ticket_owner=ticket_owner.display_name,
        closer=closer.display_name,
        message_count=len(messages),
        date=datetime.now().strftime("%d.%m.%Y %H:%M"),
        messages_html=messages_html
    )
    
    return html_content


intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.bans = True
intents.messages = True
intents.message_content = True
intents.voice_states = True
intents.invites = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, case_insensitive=True, help_command=None)


# ==========================================
# 1. LOG SİSTEMİ (MODAL VE VIEW)
# ==========================================

class LogKurulumModal(discord.ui.Modal, title="Log Kanalları Yapılandırma"):
    def __init__(self, current_data: dict):
        super().__init__()
        self.ban_log = discord.ui.TextInput(
            label="Ban / Unban Log Kanal ID veya #kanal",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564146111647917 veya #ban-log",
            default=str(current_data.get("ban_log") or VARSAYILAN_LOG_KANALLARI.get("ban_log", "")),
            required=False
        )
        self.add_item(self.ban_log)

        self.mute_log = discord.ui.TextInput(
            label="Mute / Susturma Log Kanal ID",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564329549267104 veya #mute-log",
            default=str(current_data.get("mute_log") or VARSAYILAN_LOG_KANALLARI.get("mute_log", "")),
            required=False
        )
        self.add_item(self.mute_log)

        self.mod_log = discord.ui.TextInput(
            label="Moderasyon Log Kanal ID",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564481257508874 veya #mod-log",
            default=str(current_data.get("mod_log") or VARSAYILAN_LOG_KANALLARI.get("mod_log", "")),
            required=False
        )
        self.add_item(self.mod_log)

        self.rol_log = discord.ui.TextInput(
            label="Rol Log Kanal ID",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564569446944949 veya #rol-log",
            default=str(current_data.get("rol_log") or VARSAYILAN_LOG_KANALLARI.get("rol_log", "")),
            required=False
        )
        self.add_item(self.rol_log)

        self.mesaj_log = discord.ui.TextInput(
            label="Mesaj / Ses Log Kanal ID",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564647704137879 veya #mesaj-log",
            default=str(current_data.get("mesaj_log") or VARSAYILAN_LOG_KANALLARI.get("mesaj_log", "")),
            required=False
        )
        self.add_item(self.mesaj_log)

    async def on_submit(self, interaction: discord.Interaction):
        fields = {
            "ban_log": self.ban_log.value,
            "mute_log": self.mute_log.value,
            "mod_log": self.mod_log.value,
            "rol_log": self.rol_log.value,
            "mesaj_log": self.mesaj_log.value
        }
        sayac = 0
        for tur, val in fields.items():
            cid = parse_id(val)
            if cid:
                kanal_kaydet(interaction.guild_id, tur, cid)
                sayac += 1
        await interaction.response.send_message(
            embed=embed("🔹 Log Kanalları Kaydedildi!", f"**{sayac}** adet log kanalı başarıyla güncellendi.", MAVI),
            ephemeral=True
        )


class LogKurulumView(discord.ui.View):
    def __init__(self, author_id: int):
        super().__init__(timeout=180)
        self.author_id = author_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message(embed=error_embed("Yetki Hatası", "Bu paneli yalnızca komutu çalıştıran yönetici kullanabilir."), ephemeral=True)
            return False
        return True

    @discord.ui.button(label="⚙️ Log Kanallarını Ayarla (Modal)", style=discord.ButtonStyle.primary, custom_id="log_modal_ac")
    async def modal_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        current_data = guild_data(interaction.guild_id)
        await interaction.response.send_modal(LogKurulumModal(current_data))

    @discord.ui.button(label="⚡ Varsayılan Otomatik Yükle", style=discord.ButtonStyle.secondary, custom_id="log_varsayilan_yukle")
    async def varsayilan_yukle(self, interaction: discord.Interaction, button: discord.ui.Button):
        sayi = 0
        for key in LOG_TURLERI:
            kanal_id = VARSAYILAN_LOG_KANALLARI.get(key)
            if kanal_id:
                kanal_kaydet(interaction.guild_id, key, kanal_id)
                sayi += 1
        await interaction.response.send_message(embed=embed("🔹 Otomatik Log Kurulumu", f"**{sayi}** varsayılan log kanalı kaydedildi.", MAVI), ephemeral=True)

    @discord.ui.button(label="📊 Mevcut Durumu Göster", style=discord.ButtonStyle.success, custom_id="log_durum_goster")
    async def durum_goster(self, interaction: discord.Interaction, button: discord.ui.Button):
        data = guild_data(interaction.guild_id)
        e = embed("🔹 Log Ayarları Durumu", f"**{interaction.guild.name}** aktif log yapılandırması:", MAVI)
        for key, name in LOG_TURLERI.items():
            kanal_id = data.get(key) or VARSAYILAN_LOG_KANALLARI.get(key)
            kanal = interaction.guild.get_channel(int(kanal_id)) if kanal_id else None
            e.add_field(name=f"{name}\n`{key}`", value=kanal.mention if kanal else "Devre Dışı", inline=True)
        await interaction.response.send_message(embed=e, ephemeral=True)


@bot.command(name="log-kur", aliases=["logkur", "logayarla", "log-kurulum"])
@commands.has_permissions(manage_guild=True)
async def log_kur(ctx):
    """Log sistemini Modal (pop-up form) penceresi ile kurar."""
    e = embed(
        "🔹 Log Sistemleri Kurulum Paneli",
        "Aşağıdaki **⚙️ Log Kanallarını Ayarla (Modal)** butonuna basarak tüm log kanallarınızı pop-up form penceresinde tek tek veya topluca ayarlayabilirsiniz!\n\n"
        "İsterseniz **⚡ Varsayılan Otomatik Yükle** butonuna basarak sunucunun önceden tanınan log kanallarını anında aktifleştirebilirsiniz.",
        MAVI
    )
    await ctx.send(embed=e, view=LogKurulumView(ctx.author.id))


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
    await ctx.send(embed=embed("🔹 Log Kapatıldı", f"**{LOG_TURLERI[tur]}** için log gönderimi kapatıldı.", MAVI))


@bot.command(name="log-durum", aliases=["logdurum"])
@commands.has_permissions(manage_guild=True)
async def log_durum(ctx):
    data = guild_data(ctx.guild.id)
    e = embed("🔹 Log Ayarları Durumu", f"**{ctx.guild.name}** sunucusu aktif log yapılandırması:", MAVI)
    for key, name in LOG_TURLERI.items():
        kanal_id = data.get(key) or VARSAYILAN_LOG_KANALLARI.get(key)
        kanal = ctx.guild.get_channel(int(kanal_id)) if kanal_id else None
        e.add_field(name=f"{name}\n`{key}`", value=kanal.mention if kanal else "Devre Dışı", inline=True)
    await ctx.send(embed=e)


# ==========================================
# 2. KÜFÜR KORUMASI (MODAL VE VIEW)
# ==========================================

class KufurKurulumModal(discord.ui.Modal, title="Küfür Koruması Yapılandırma"):
    def __init__(self, current_words: list):
        super().__init__()
        default_text = ", ".join(current_words) if current_words else ", ".join(sorted(KUFUR_KELIMELERI))
        self.kelimeler = discord.ui.TextInput(
            label="Filtrelenecek Kelimeler (Virgülle Ayrılmış)",
            style=discord.TextStyle.paragraph,
            placeholder="amk, aq, orospi...",
            default=default_text,
            required=True,
            max_length=2000
        )
        self.add_item(self.kelimeler)

    async def on_submit(self, interaction: discord.Interaction):
        liste = [k.strip().lower() for k in self.kelimeler.value.split(",") if k.strip()]
        set_guild_section(interaction.guild_id, "kufur_koruma", {"aktif": True, "kelimeler": liste})
        await interaction.response.send_message(
            embed=embed("🔹 Küfür Koruması Aktif!", f"Toplam **{len(liste)}** kelime filtre listesine kaydedildi ve koruma aktif edildi.", MAVI),
            ephemeral=True
        )


class KufurKurulumView(discord.ui.View):
    def __init__(self, author_id: int):
        super().__init__(timeout=180)
        self.author_id = author_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message(embed=error_embed("Yetki Hatası", "Bu paneli yalnızca komutu çalıştıran yönetici kullanabilir."), ephemeral=True)
            return False
        return True

    @discord.ui.button(label="⚙️ Kelimeleri Düzenle ve Kur (Modal)", style=discord.ButtonStyle.primary, custom_id="kufur_modal_ac")
    async def modal_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        kufur = guild_section(interaction.guild_id, "kufur_koruma", {})
        await interaction.response.send_modal(KufurKurulumModal(kufur.get("kelimeler", [])))

    @discord.ui.button(label="❌ Korumayı Kapat", style=discord.ButtonStyle.danger, custom_id="kufur_kapat_btn")
    async def korumayi_kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        set_guild_section(interaction.guild_id, "kufur_koruma", {"aktif": False, "kelimeler": []})
        await interaction.response.send_message(embed=embed("🔹 Küfür Koruması Kapatıldı", "Sistem devre dışı bırakıldı.", MAVI), ephemeral=True)


@bot.command(name="kufur-kur", aliases=["küfür-kur", "kufurkur", "küfürkur"])
@commands.has_permissions(manage_guild=True)
async def kufur_kur(ctx):
    """Küfür korumasını Modal form ile kurar."""
    kufur = guild_section(ctx.guild.id, "kufur_koruma", {})
    durum = "Aktif" if kufur.get("aktif") else "Devre Dışı"
    e = embed(
        "🔹 Küfür Koruması Kurulum Paneli",
        f"**Mevcut Durum:** `{durum}`\n\n"
        "Aşağıdaki **⚙️ Kelimeleri Düzenle ve Kur (Modal)** butonuna basarak engellenecek küfür kelimelerini pop-up form penceresinden dilediğiniz gibi düzenleyebilir ve aktif edebilirsiniz!",
        MAVI
    )
    await ctx.send(embed=e, view=
