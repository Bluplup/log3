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
            except (discord.HTTPException, discord.NotFound):
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


intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.presences = True
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

    @discord.ui.button(label="🤖 Otomatik Log Kanalları Oluştur", style=discord.ButtonStyle.success, custom_id="log_oto_olustur")
    async def oto_olustur(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Kanal/kategori oluşturmak zaman alabileceğinden (3sn interaction limiti) önce defer ediyoruz.
        await interaction.response.defer(ephemeral=True, thinking=True)

        guild = interaction.guild

        if not guild.me.guild_permissions.manage_channels:
            await interaction.followup.send(
                embed=error_embed("Yetki Eksik", "Botun kanal/kategori oluşturabilmesi için **Kanalları Yönet** iznine ihtiyacı var."),
                ephemeral=True
            )
            return

        try:
            # En alttaki kategori olacak şekilde pozisyon veriyoruz.
            kategori = await guild.create_category(
                name="📁 log-kanallari",
                position=len(guild.categories),
                overwrites={
                    guild.default_role: discord.PermissionOverwrite(view_channel=False),
                    guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True, manage_channels=True),
                },
                reason=f"{interaction.user} tarafından otomatik log kurulumu"
            )
        except discord.Forbidden:
            await interaction.followup.send(
                embed=error_embed("Kategori Oluşturulamadı", "Botun kategori oluşturma izni yok."),
                ephemeral=True
            )
            return
        except discord.HTTPException as exc:
            await interaction.followup.send(
                embed=error_embed("Kategori Oluşturulamadı", short(exc)),
                ephemeral=True
            )
            return

        olusturulan = 0
        hata = 0
        for tur in LOG_TURLERI:
            kanal_adi = tur.replace("_", "-")
            try:
                yeni_kanal = await guild.create_text_channel(
                    name=kanal_adi,
                    category=kategori,
                    reason=f"{interaction.user} tarafından otomatik log kurulumu"
                )
                kanal_kaydet(guild.id, tur, yeni_kanal.id)
                olusturulan += 1
            except (discord.Forbidden, discord.HTTPException):
                hata += 1

        e = embed(
            "🔹 Otomatik Log Kanalları Oluşturuldu!",
            f"**Kategori:** {kategori.mention if hasattr(kategori, 'mention') else kategori.name}\n"
            f"✅ **Oluşturulan Log Kanalı:** `{olusturulan}`\n"
            f"⚠️ **Başarısız:** `{hata}`\n\n"
            "Tüm log türleri bu yeni kanallara yönlendirilecek şekilde aktifleştirildi.",
            MAVI
        )
        await interaction.followup.send(embed=e, ephemeral=True)

    @discord.ui.button(label="📊 Mevcut Durumu Göster", style=discord.ButtonStyle.secondary, custom_id="log_durum_goster")
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
        "İsterseniz **⚡ Varsayılan Otomatik Yükle** butonuna basarak sunucunun önceden tanınan log kanallarını anında aktifleştirebilirsiniz.\n\n"
        "Ya da **🤖 Otomatik Log Kanalları Oluştur** butonuna basarak en alta yeni bir kategori ve içine tüm log kanallarını otomatik oluşturup aktifleştirebilirsiniz!",
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
    await ctx.send(embed=e, view=KufurKurulumView(ctx.author.id))


@bot.command(name="kufur-kapat", aliases=["küfür-kapat"])
@commands.has_permissions(manage_guild=True)
async def kufur_kapat(ctx):
    set_guild_section(ctx.guild.id, "kufur_koruma", {"aktif": False, "kelimeler": []})
    await ctx.send(embed=embed("🔹 Küfür Koruması Kapatıldı", "Küfür engelleme sistemi devre dışı bırakıldı.", MAVI))


# ==========================================
# 3. LİNK KORUMASI (MODAL VE VIEW)
# ==========================================

class LinkKurulumModal(discord.ui.Modal, title="Link Koruması Yapılandırma"):
    def __init__(self, current_data: dict):
        super().__init__()
        self.muaf_roller = discord.ui.TextInput(
            label="Muaf Roller (Virgülle Ayrılmış)",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564569446944949, @Yönetim",
            default=", ".join(str(r) for r in current_data.get("muaf_roller", [])),
            required=False
        )
        self.add_item(self.muaf_roller)

        self.muaf_kanallar = discord.ui.TextInput(
            label="Muaf Kanallar (Virgülle Ayrılmış)",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564647704137879, #duyuru",
            default=", ".join(str(c) for c in current_data.get("muaf_kanallar", [])),
            required=False
        )
        self.add_item(self.muaf_kanallar)

    async def on_submit(self, interaction: discord.Interaction):
        roller = [parse_id(r) for r in self.muaf_roller.value.split(",") if parse_id(r)]
        kanallar = [parse_id(c) for c in self.muaf_kanallar.value.split(",") if parse_id(c)]

        data = {
            "aktif": True,
            "muaf_roller": roller,
            "muaf_kanallar": kanallar
        }
        set_guild_section(interaction.guild_id, "link_koruma", data)
        await interaction.response.send_message(
            embed=embed("🔹 Link Koruması Aktif!", f"Link engelleme sistemi aktif edildi.\n**Muaf Roller:** `{len(roller)}` adet\n**Muaf Kanallar:** `{len(kanallar)}` adet", MAVI),
            ephemeral=True
        )


class LinkKurulumView(discord.ui.View):
    def __init__(self, author_id: int):
        super().__init__(timeout=180)
        self.author_id = author_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message(embed=error_embed("Yetki Hatası", "Bu paneli yalnızca komutu çalıştıran yönetici kullanabilir."), ephemeral=True)
            return False
        return True

    @discord.ui.button(label="⚙️ İzinleri Ayarla ve Kur (Modal)", style=discord.ButtonStyle.primary, custom_id="link_modal_ac")
    async def modal_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        current_data = guild_section(interaction.guild_id, "link_koruma", {})
        await interaction.response.send_modal(LinkKurulumModal(current_data))

    @discord.ui.button(label="❌ Korumayı Kapat", style=discord.ButtonStyle.danger, custom_id="link_kapat_btn")
    async def korumayi_kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        ayar = guild_section(interaction.guild_id, "link_koruma", {})
        ayar["aktif"] = False
        set_guild_section(interaction.guild_id, "link_koruma", ayar)
        await interaction.response.send_message(embed=embed("🔹 Link Koruması Kapatıldı", "Sistem devre dışı bırakıldı.", MAVI), ephemeral=True)


@bot.command(name="link-kur", aliases=["linkkur", "link-koruma-kur", "antilink"])
@commands.has_permissions(manage_guild=True)
async def link_kur(ctx):
    """Link korumasını Modal form ile kurar."""
    link = guild_section(ctx.guild.id, "link_koruma", {})
    durum = "Aktif" if link.get("aktif") else "Devre Dışı"
    e = embed(
        "🔹 Link Koruması Kurulum Paneli",
        f"**Mevcut Durum:** `{durum}`\n\n"
        "Aşağıdaki **⚙️ İzinleri Ayarla ve Kur (Modal)** butonuna basarak reklam/link korumasını aktif edebilir, muaf tutulacak rol ve kanalları belirleyebilirsiniz!",
        MAVI
    )
    await ctx.send(embed=e, view=LinkKurulumView(ctx.author.id))


@bot.command(name="link-koruma-kapat")
@commands.has_permissions(manage_guild=True)
async def link_koruma_kapat(ctx):
    ayar = guild_section(ctx.guild.id, "link_koruma", {})
    ayar["aktif"] = False
    set_guild_section(ctx.guild.id, "link_koruma", ayar)
    await ctx.send(embed=embed("🔹 Link Koruması Kapatıldı", "Link koruma sistemi kapatıldı.", MAVI))


# ==========================================
# 4. SPAM KORUMASI (MODAL VE VIEW)
# ==========================================

class SpamKurulumModal(discord.ui.Modal, title="Spam Koruması Yapılandırma"):
    def __init__(self, current_data: dict):
        super().__init__()
        self.max_mesaj = discord.ui.TextInput(
            label="Maksimum Mesaj Limiti",
            style=discord.TextStyle.short,
            placeholder="Örn: 5",
            default=str(current_data.get("max_mesaj", 5)),
            required=True
        )
        self.add_item(self.max_mesaj)

        self.saniye = discord.ui.TextInput(
            label="Bekleme Süresi (Saniye)",
            style=discord.TextStyle.short,
            placeholder="Örn: 8",
            default=str(current_data.get("saniye", 8)),
            required=True
        )
        self.add_item(self.saniye)

        self.mute_saniye = discord.ui.TextInput(
            label="Cezalandırma Süresi (Örn: 300s, 10m, 1h)",
            style=discord.TextStyle.short,
            placeholder="Örn: 300 veya 10m",
            default=str(current_data.get("mute_saniye", 300)),
            required=True
        )
        self.add_item(self.mute_saniye)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            m_limit = max(2, int(re.sub(r"\D", "", self.max_mesaj.value) or 5))
            sec = max(3, int(re.sub(r"\D", "", self.saniye.value) or 8))
            m_sec = parse_duration(self.mute_saniye.value, 300)
        except ValueError:
            await interaction.response.send_message(embed=error_embed("Hatalı Girdi", "Lütfen geçerli sayı ve zaman süreleri yazın."), ephemeral=True)
            return

        ayar = {
            "aktif": True,
            "max_mesaj": m_limit,
            "saniye": sec,
            "mute_saniye": m_sec,
            "muaf_roller": [],
            "muaf_kanallar": []
        }
        set_guild_section(interaction.guild_id, "spam_koruma", ayar)
        await interaction.response.send_message(
            embed=embed("🔹 Spam Koruması Aktif!", f"**{sec}** saniyede **{m_limit}** mesaj sınırını aşan kullanıcılara **{format_duration(m_sec)}** timeout verilecek.", MAVI),
            ephemeral=True
        )


class SpamKurulumView(discord.ui.View):
    def __init__(self, author_id: int):
        super().__init__(timeout=180)
        self.author_id = author_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message(embed=error_embed("Yetki Hatası", "Bu paneli yalnızca komutu çalıştıran yönetici kullanabilir."), ephemeral=True)
            return False
        return True

    @discord.ui.button(label="⚙️ Limitleri Ayarla ve Kur (Modal)", style=discord.ButtonStyle.primary, custom_id="spam_modal_ac")
    async def modal_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        current_data = guild_section(interaction.guild_id, "spam_koruma", {})
        await interaction.response.send_modal(SpamKurulumModal(current_data))

    @discord.ui.button(label="❌ Korumayı Kapat", style=discord.ButtonStyle.danger, custom_id="spam_kapat_btn")
    async def korumayi_kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        ayar = guild_section(interaction.guild_id, "spam_koruma", {})
        ayar["aktif"] = False
        set_guild_section(interaction.guild_id, "spam_koruma", ayar)
        await interaction.response.send_message(embed=embed("🔹 Spam Koruması Kapatıldı", "Spam engelleme sistemi kapatıldı.", MAVI), ephemeral=True)


@bot.command(name="spam-kur", aliases=["spamkur", "spam-koruma-kur"])
@commands.has_permissions(manage_guild=True)
async def spam_kur(ctx):
    """Spam korumasını Modal form ile kurar."""
    spam = guild_section(ctx.guild.id, "spam_koruma", {})
    durum = "Aktif" if spam.get("aktif") else "Devre Dışı"
    e = embed(
        "🔹 Spam Koruması Kurulum Paneli",
        f"**Mevcut Durum:** `{durum}`\n\n"
        "Aşağıdaki **⚙️ Limitleri Ayarla ve Kur (Modal)** butonuna basarak spam koruması sürelerini ve ceza sürelerini kolayca yapılandırabilirsiniz!",
        MAVI
    )
    await ctx.send(embed=e, view=SpamKurulumView(ctx.author.id))


@bot.command(name="spam-koruma-kapat")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_kapat(ctx):
    ayar = guild_section(ctx.guild.id, "spam_koruma", {})
    ayar["aktif"] = False
    set_guild_section(ctx.guild.id, "spam_koruma", ayar)
    await ctx.send(embed=embed("🔹 Spam Koruması Kapatıldı", "Spam engelleme sistemi kapatıldı.", MAVI))


# ==========================================
# 5. JAİL SİSTEMİ (MODAL VE VIEW)
# ==========================================

class JailKurulumModal(discord.ui.Modal, title="Jail Sistemi Yapılandırma"):
    def __init__(self, current_data: dict):
        super().__init__()
        self.kanal_id = discord.ui.TextInput(
            label="Jail Mahkeme Kanal ID veya #kanal",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564647704137879 veya #jail-kanali",
            default=str(current_data.get("kanal_id") or ""),
            required=True
        )
        self.add_item(self.kanal_id)

        self.yetki_rol_id = discord.ui.TextInput(
            label="Jail Yetkilisi Rol ID veya @rol",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564569446944949 veya @JailYetkilisi",
            default=str(current_data.get("yetki_rol_id") or ""),
            required=True
        )
        self.add_item(self.yetki_rol_id)

    async def on_submit(self, interaction: discord.Interaction):
        cid = parse_id(self.kanal_id.value)
        rid = parse_id(self.yetki_rol_id.value)

        if not cid or not rid:
            await interaction.response.send_message(embed=error_embed("Hatalı Girdi", "Lütfen geçerli kanal ve yetkili rol ID'si girin."), ephemeral=True)
            return

        kanal = interaction.guild.get_channel(cid)
        yetki_rol = interaction.guild.get_role(rid)

        if not kanal or not yetki_rol:
            await interaction.response.send_message(embed=error_embed("Bulunamadı", "Belirtilen kanal veya rol sunucuda bulunamadı."), ephemeral=True)
            return

        # Kanal izinlerini ayarlamak (aşağıda tüm kanallar için tek tek) zaman alabilir ve
        # 3 saniyelik interaction limitini aşıp "Etkileşim başarısız oldu" hatasına yol açabilir.
        # Bu yüzden önce defer ediyoruz, işlemleri sonra yapıp followup ile cevap veriyoruz.
        await interaction.response.defer(ephemeral=True, thinking=True)

        jail_rol = discord.utils.get(interaction.guild.roles, name="JAIL")
        if jail_rol is None:
            try:
                jail_rol = await interaction.guild.create_role(name="JAIL", reason="Jail sistemi kurulumu")
            except discord.Forbidden:
                await interaction.followup.send(embed=error_embed("Rol Oluşturulamadı", "Botun rol oluşturma yetkisi yok."), ephemeral=True)
                return

        ayar = guild_section(interaction.guild_id, "jail_sistemi", {"kayitlar": {}})
        ayar.update({
            "aktif": True,
            "kanal_id": kanal.id,
            "jail_rol_id": jail_rol.id,
            "yetki_rol_id": yetki_rol.id,
            "kayitlar": ayar.get("kayitlar", {})
        })
        set_guild_section(interaction.guild_id, "jail_sistemi", ayar)

        # Kanalların izinlerini ayarla
        hata_sayisi = 0
        for ch in interaction.guild.channels:
            try:
                if ch.id == kanal.id:
                    await ch.set_permissions(jail_rol, view_channel=True, send_messages=True, read_message_history=True)
                elif isinstance(ch, discord.VoiceChannel):
                    await ch.set_permissions(jail_rol, view_channel=False, connect=False, speak=False)
                else:
                    await ch.set_permissions(jail_rol, view_channel=False, send_messages=False, read_message_history=False)
            except (discord.Forbidden, discord.HTTPException):
                hata_sayisi += 1

        aciklama = f"**Jail Kanalı:** {kanal.mention}\n**Jail Rolü:** {jail_rol.mention}\n**Yetkili Rolü:** {yetki_rol.mention}"
        if hata_sayisi:
            aciklama += f"\n\n⚠️ `{hata_sayisi}` kanalda izin ayarlanamadı (bot yetkisi/rol sırası kontrol edin)."

        await interaction.followup.send(
            embed=embed("🔹 Jail Sistemi Aktif Edildi!", aciklama, MAVI),
            ephemeral=True
        )


class JailKurulumView(discord.ui.View):
    def __init__(self, author_id: int):
        super().__init__(timeout=180)
        self.author_id = author_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message(embed=error_embed("Yetki Hatası", "Bu paneli yalnızca komutu çalıştıran yönetici kullanabilir."), ephemeral=True)
            return False
        return True

    @discord.ui.button(label="⚙️ Jail Sistemini Kur (Modal)", style=discord.ButtonStyle.primary, custom_id="jail_modal_ac")
    async def modal_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        current_data = guild_section(interaction.guild_id, "jail_sistemi", {})
        await interaction.response.send_modal(JailKurulumModal(current_data))

    @discord.ui.button(label="❌ Sistemi Kapat", style=discord.ButtonStyle.danger, custom_id="jail_kapat_btn")
    async def sistemi_kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        set_guild_section(interaction.guild_id, "jail_sistemi", {"aktif": False, "kayitlar": {}})
        await interaction.response.send_message(embed=embed("🔹 Jail Sistemi Kapatıldı", "Jail sistemi devre dışı bırakıldı.", MAVI), ephemeral=True)


@bot.command(name="jailkur", aliases=["jail-kur"])
@commands.has_permissions(manage_guild=True)
async def jailkur(ctx):
    """Jail sistemini Modal form ile kurar."""
    jail_data = guild_section(ctx.guild.id, "jail_sistemi", {})
    durum = "Aktif" if jail_data.get("aktif") else "Devre Dışı"
    e = embed(
        "🔹 Jail Sistemi Kurulum Paneli",
        f"**Mevcut Durum:** `{durum}`\n\n"
        "Aşağıdaki **⚙️ Jail Sistemini Kur (Modal)** butonuna basarak hapishane kanalını ve yetkili rolünü pop-up form penceresinden saniyeler içinde ayarlayabilirsiniz!",
        MAVI
    )
    await ctx.send(embed=e, view=JailKurulumView(ctx.author.id))


# ==========================================
# 6. TİCKET (BİLET) SİSTEMİ (MODAL VE VIEW)
# ==========================================

class TicketKurulumModal(discord.ui.Modal, title="Ticket Sistemi Yapılandırma"):
    def __init__(self, current_data: dict):
        super().__init__()
        self.kategori_id = discord.ui.TextInput(
            label="Ticket Kategorisi ID",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484565700969496606",
            default=str(current_data.get("kategori_id") or ""),
            required=True
        )
        self.add_item(self.kategori_id)

        self.log_kanal_id = discord.ui.TextInput(
            label="Ticket Log Kanal ID (İsteğe Bağlı)",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564481257508874 veya #ticket-log",
            default=str(current_data.get("log_kanal_id") or ""),
            required=False
        )
        self.add_item(self.log_kanal_id)

        self.destek_rol_id = discord.ui.TextInput(
            label="Destek Ekibi Rol ID (İsteğe Bağlı)",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564569446944949 veya @Destek",
            default=str(current_data.get("destek_rol_id") or ""),
            required=False
        )
        self.add_item(self.destek_rol_id)

    async def on_submit(self, interaction: discord.Interaction):
        kat_id = parse_id(self.kategori_id.value)
        log_id = parse_id(self.log_kanal_id.value)
        destek_id = parse_id(self.destek_rol_id.value)

        if not kat_id:
            await interaction.response.send_message(embed=error_embed("Hatalı Girdi", "Lütfen geçerli bir Kategori ID'si girin."), ephemeral=True)
            return

        kategori = interaction.guild.get_channel(kat_id)
        if not isinstance(kategori, discord.CategoryChannel):
            await interaction.response.send_message(embed=error_embed("Bulunamadı", "Belirtilen Kategori ID'si sunucuda bulunamadı."), ephemeral=True)
            return

        set_guild_section(interaction.guild_id, "ticket_sistemi", {
            "kategori_id": kat_id,
            "log_kanal_id": log_id,
            "destek_rol_id": destek_id
        })

        log_kanal = interaction.guild.get_channel(log_id) if log_id else None
        destek_rol = interaction.guild.get_role(destek_id) if destek_id else None

        await interaction.response.send_message(
            embed=embed("🔹 Ticket Sistemi Yapılandırıldı!", f"**Kategori:** {kategori.name}\n**Log:** {log_kanal.mention if log_kanal else 'Yok'}\n**Destek Rolü:** {destek_rol.mention if destek_rol else 'Yok'}\n\nArtık `{PREFIX}ticketpanel` komutunu kullanarak kanala ticket butonunu gönderebilirsiniz!", MAVI),
            ephemeral=True
        )


class TicketKurulumView(discord.ui.View):
    def __init__(self, author_id: int):
        super().__init__(timeout=180)
        self.author_id = author_id

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message(embed=error_embed("Yetki Hatası", "Bu paneli yalnızca komutu çalıştıran yönetici kullanabilir."), ephemeral=True)
            return False
        return True

    @discord.ui.button(label="⚙️ Ticket Sistemini Kur (Modal)", style=discord.ButtonStyle.primary, custom_id="ticket_modal_ac")
    async def modal_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        current_data = guild_section(interaction.guild_id, "ticket_sistemi", {})
        await interaction.response.send_modal(TicketKurulumModal(current_data))

    @discord.ui.button(label="📌 Destek Panelini Buraya Gönder", style=discord.ButtonStyle.success, custom_id="ticket_paneli_gonder")
    async def paneli_gonder(self, interaction: discord.Interaction, button: discord.ui.Button):
        ayar = guild_section(interaction.guild_id, "ticket_sistemi", {})
        if not ayar.get("kategori_id"):
            await interaction.response.send_message(embed=error_embed("Sistem Hazır Değil", "Önce '⚙️ Ticket Sistemini Kur' butonundan ayarlarınızı kaydedin."), ephemeral=True)
            return
        await interaction.channel.send(
            embed=embed("🔹 Destek Talebi Paneli", "Destek ekibimizle iletişime geçmek için aşağıdaki butona tıklayarak ticket oluşturabilirsiniz.", MAVI),
            view=TicketView()
        )
        await interaction.response.send_message(embed=embed("🔹 Panel Gönderildi", f"Destek talebi paneli {interaction.channel.mention} kanalında oluşturuldu.", MAVI), ephemeral=True)


@bot.command(name="ticketkur", aliases=["ticket-kur"])
@commands.has_permissions(manage_guild=True)
async def ticketkur(ctx):
    """Ticket sistemini Modal form ile kurar."""
    ticket_data = guild_section(ctx.guild.id, "ticket_sistemi", {})
    durum = "Kuruldu" if ticket_data.get("kategori_id") else "Henüz Kurulmadı"
    e = embed(
        "🔹 Ticket Sistemi Kurulum Paneli",
        f"**Mevcut Durum:** `{durum}`\n\n"
        "Aşağıdaki **⚙️ Ticket Sistemini Kur (Modal)** butonuna basarak kategori ID, log kanalı ve destek rolünü pop-up form penceresinde kolayca ayarlayabilirsiniz!",
        MAVI
    )
    await ctx.send(embed=e, view=TicketKurulumView(ctx.author.id))


# ==========================================
# MODERASYON VE GENEL BOT KOMUTLARI
# ==========================================

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
    e = embed("🔹 Üye Banlandı", f"**Hedef:** {target_text}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", MAVI)
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
    e = embed("🔹 Ban Kaldırıldı", f"**Kullanıcı ID:** `{target_id}`\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", MAVI)
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

    e = embed("🔹 Üye Atıldı (Kick)", f"**Hedef:** {target.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", MAVI)
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
        "🔹 Üye Susturuldu",
        f"**Hedef:** {target.mention}\n**Süre:** {format_duration(seconds)}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}",
        MAVI
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

    e = embed("🔹 Mute Kaldırıldı", f"**Hedef:** {target.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", MAVI)
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mute_log", e)


@bot.command(name="sil", aliases=["temizle", "purge"])
@commands.has_permissions(manage_messages=True)
async def sil(ctx, adet: int = 5):
    adet = max(1, min(adet, 100))
    deleted = await ctx.channel.purge(limit=adet + 1)
    msg = await ctx.send(embed=embed("🔹 Mesajlar Silindi", f"**{max(0, len(deleted) - 1)}** adet mesaj başarıyla temizlendi.", MAVI))
    await asyncio.sleep(4)
    try:
        await msg.delete()
    except discord.HTTPException:
        pass


@bot.command(name="herkeserol", aliases=["herkese-rol", "herkeserolekle", "herkese-rol-ver"])
@commands.has_permissions(manage_roles=True)
async def herkeserol(ctx, rol: discord.Role = None):
    """
    Sunucudaki tüm üyelere (botlar hariç) belirtilen rolü ekler.
    Kullanım: .herkeserol @rol
    """
    if rol is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}herkeserol @rol` veya `{PREFIX}herkeserol <rol_id>`"))
        return

    if rol >= ctx.guild.me.top_role:
        await ctx.send(embed=error_embed("Rol Sırası Hatası", "Bu rol botun en yüksek rolünden eşit veya üstte olduğu için verilemez."))
        return

    status_msg = await ctx.send(embed=embed("🔹 Herkese Rol Veriliyor", f"{rol.mention} rolü sunucudaki tüm üyelere veriliyor, lütfen bekleyin...", MAVI))

    eklenen = 0
    zaten_var = 0
    hata = 0

    for member in ctx.guild.members:
        if member.bot:
            continue
        if rol in member.roles:
            zaten_var += 1
            continue
        try:
            await member.add_roles(rol, reason=f"{ctx.author} tarafından toplu rol verme işlemi yapıldı.")
            eklenen += 1
            await asyncio.sleep(0.3)
        except (discord.Forbidden, discord.HTTPException):
            hata += 1

    e = embed("🔹 Toplu Rol Verme Tamamlandı", f"**Hedef Rol:** {rol.mention}\n\n✅ **Başarıyla Eklenen:** `{eklenen}` üye\nℹ️ **Zaten Rolü Olan:** `{zaten_var}` üye\n⚠️ **Başarısız / Hata:** `{hata}`", MAVI)
    try:
        await status_msg.edit(embed=e)
    except discord.HTTPException:
        await ctx.send(embed=e)
    await log_gonder(ctx.guild, "rol_log", e)


@bot.command(name="herkeserolsil", aliases=["herkese-rol-sil", "herkeserolkaldir"])
@commands.has_permissions(manage_roles=True)
async def herkeserolsil(ctx, rol: discord.Role = None):
    """
    Sunucudaki tüm üyelerden (botlar hariç) belirtilen rolü kaldırır.
    Kullanım: .herkeserolsil @rol
    """
    if rol is None:
        await ctx.send(embed=usage_embed(f"`{PREFIX}herkeserolsil @rol` veya `{PREFIX}herkeserolsil <rol_id>`"))
        return

    if rol >= ctx.guild.me.top_role:
        await ctx.send(embed=error_embed("Rol Sırası Hatası", "Bu rol botun en yüksek rolünden eşit veya üstte olduğu için alınamaz."))
        return

    status_msg = await ctx.send(embed=embed("🔹 Herkesten Rol Kaldırılıyor", f"{rol.mention} rolü tüm üyelerden alınıyor, lütfen bekleyin...", MAVI))

    silinen = 0
    yoktu = 0
    hata = 0

    for member in ctx.guild.members:
        if member.bot:
            continue
        if rol not in member.roles:
            yoktu += 1
            continue
        try:
            await member.remove_roles(rol, reason=f"{ctx.author} tarafından toplu rol alma işlemi yapıldı.")
            silinen += 1
            await asyncio.sleep(0.3)
        except (discord.Forbidden, discord.HTTPException):
            hata += 1

    e = embed("🔹 Toplu Rol Alma Tamamlandı", f"**Hedef Rol:** {rol.mention}\n\n✅ **Başarıyla Alınan:** `{silinen}` üye\nℹ️ **Zaten Rolü Olmayan:** `{yoktu}` üye\n⚠️ **Başarısız / Hata:** `{hata}`", MAVI)
    try:
        await status_msg.edit(embed=e)
    except discord.HTTPException:
        await ctx.send(embed=e)
    await log_gonder(ctx.guild, "rol_log", e)


# ==========================================
# HOŞ GELDİN SİSTEMİ (MODAL VE VIEW)
# ==========================================

DEFAULT_HOSGELDIN_DIS_MESAJ = "HOŞ GELDİNN {uye_etiket}"
DEFAULT_HOSGELDIN_BASLIK = "MIORIYE HOOŞGELDIN!! 🍙"
DEFAULT_HOSGELDIN_ACIKLAMA = (
    "💕 **Aramıza hoş geldin, güzel insan!** Buraya kadar geldiysen artık bizdensin... 😜 Umarım **{sunucu}** ortamımızda güzel vakit geçirir, bol bol sohbet eder ve harika anılar biriktirirsin. 👁️‍🗨️\n\n"
    "💖 ✨ **Sunucuda seni neler bekliyor?**\n"
    "┊\n"
    "💬 **#sohbet** — Yabancılık çekmeyeceğin toxiclikten uzak samimi ortamımızda sohbet edebilirsin!! 🍥\n"
    "┊\n"
    "📖 **#kurallar** — Daha iyi bir ortam için kuralları okumayı ihmal etme!! 🍥\n"
    "┊\n"
    "🎉 **#çekiliş** — Etkinliklere katılıp eğlenmek ve güzel anılar biriktirmek istiyorsan burası tam senin için!! 🍥\n"
    "┊\n"
    "**{sunucu}** halkına tekrardan hoş geldin!! 🍙"
)


class HosgeldinModal(discord.ui.Modal, title="Hoş Geldin Mesajı Özelleştir"):
    def __init__(self, channel: discord.TextChannel, current_data: dict):
        super().__init__()
        self.channel = channel

        self.dis_mesaj = discord.ui.TextInput(
            label="Dış Mesaj (Etiketli)",
            style=discord.TextStyle.short,
            placeholder="Örn: HOŞ GELDİNN {uye_etiket} {rol_etiket}",
            default=current_data.get("dis_mesaj") or DEFAULT_HOSGELDIN_DIS_MESAJ,
            required=False,
            max_length=200
        )
        self.add_item(self.dis_mesaj)

        self.rol_id = discord.ui.TextInput(
            label="Dış Mesaj Rol ID (İsteğe Bağlı)",
            style=discord.TextStyle.short,
            placeholder="Örn: 1484564569446944949",
            default=current_data.get("rol_id") or "",
            required=False,
            max_length=30
        )
        self.add_item(self.rol_id)

        self.baslik = discord.ui.TextInput(
            label="Embed Başlığı",
            style=discord.TextStyle.short,
            placeholder="Örn: MIORIYE HOOŞGELDIN!! 🍙",
            default=current_data.get("baslik") or DEFAULT_HOSGELDIN_BASLIK,
            required=False,
            max_length=256
        )
        self.add_item(self.baslik)

        self.aciklama = discord.ui.TextInput(
            label="Embed Açıklaması ({uye}, {sunucu} vb)",
            style=discord.TextStyle.paragraph,
            placeholder="💕 Aramıza hoş geldin {uye}! {sunucu} halkına katıldın...",
            default=current_data.get("aciklama") or DEFAULT_HOSGELDIN_ACIKLAMA,
            required=False,
            max_length=2000
        )
        self.add_item(self.aciklama)

        self.resim_url = discord.ui.TextInput(
            label="Banner / GIF URL (İsteğe Bağlı)",
            style=discord.TextStyle.short,
            placeholder="https://media.giphy.com/...gif",
            default=current_data.get("resim_url") or "",
            required=False,
            max_length=500
        )
        self.add_item(self.resim_url)

    async def on_submit(self, interaction: discord.Interaction):
        data = guild_section(interaction.guild_id, "hosgeldin_sistemi", {})
        data.update({
            "aktif": True,
            "kanal_id": self.channel.id,
            "dis_mesaj": self.dis_mesaj.value.strip(),
            "rol_id": self.rol_id.value.strip(),
            "baslik": self.baslik.value.strip(),
            "aciklama": self.aciklama.value.strip(),
            "resim_url": self.resim_url.value.strip()
        })
        set_guild_section(interaction.guild_id, "hosgeldin_sistemi", data)

        dis_mesaj = format_welcome_text(data["dis_mesaj"], interaction.user, data["rol_id"], is_dis_mesaj=True)
        baslik = format_welcome_text(data["baslik"], interaction.user, data["rol_id"], is_dis_mesaj=False)
        aciklama = format_welcome_text(data["aciklama"], interaction.user, data["rol_id"], is_dis_mesaj=False)

        e = embed(baslik or "Aramıza Hoş Geldin!", aciklama, MAVI)
        if data["resim_url"]:
            e.set_image(url=data["resim_url"])
        if interaction.user.display_avatar:
            e.set_thumbnail(url=interaction.user.display_avatar.url)

        confirm_embed = embed("🔹 Hoş Geldin Sistemi Kaydedildi!", f"Tüm ayarlarınız başarıyla kaydedildi ve {self.channel.mention} kanalında aktif edildi.\n\n**Canlı Önizleme Aşağıdadır:**", MAVI)

        await interaction.response.send_message(embed=confirm_embed, ephemeral=True)
        if dis_mesaj:
            await interaction.followup.send(content=dis_mesaj, embed=e, ephemeral=True)
        else:
            await interaction.followup.send(embed=e, ephemeral=True)


class HosgeldinKurulumView(discord.ui.View):
    def __init__(self, author_id: int, channel: discord.TextChannel):
        super().__init__(timeout=180)
        self.author_id = author_id
        self.channel = channel

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user.id != self.author_id:
            await interaction.response.send_message(embed=error_embed("Yetki Hatası", "Bu butonları yalnızca komutu çalıştıran yönetici kullanabilir."), ephemeral=True)
            return False
        return True

    @discord.ui.button(label="⚙️ Formu Aç ve Kur (Modal)", style=discord.ButtonStyle.primary, custom_id="hosgeldin_modal_ac")
    async def modal_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        current_data = guild_section(interaction.guild_id, "hosgeldin_sistemi", {})
        modal = HosgeldinModal(channel=self.channel, current_data=current_data)
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="🧪 Canlı Test Et", style=discord.ButtonStyle.secondary, custom_id="hosgeldin_test_et")
    async def test_et(self, interaction: discord.Interaction, button: discord.ui.Button):
        data = guild_section(interaction.guild_id, "hosgeldin_sistemi", {})
        if not data.get("aktif"):
            await interaction.response.send_message(embed=error_embed("Sistem Pasif", "Önce '⚙️ Formu Aç ve Kur' butonuna basarak ayarlarınızı kaydedin."), ephemeral=True)
            return

        dis_mesaj = format_welcome_text(data.get("dis_mesaj") or DEFAULT_HOSGELDIN_DIS_MESAJ, interaction.user, data.get("rol_id"), is_dis_mesaj=True)
        baslik = format_welcome_text(data.get("baslik") or DEFAULT_HOSGELDIN_BASLIK, interaction.user, data.get("rol_id"), is_dis_mesaj=False)
        aciklama = format_welcome_text(data.get("aciklama") or DEFAULT_HOSGELDIN_ACIKLAMA, interaction.user, data.get("rol_id"), is_dis_mesaj=False)
        resim_url = data.get("resim_url")

        e = embed(baslik, aciklama, MAVI)
        if resim_url:
            e.set_image(url=resim_url)
        if interaction.user.display_avatar:
            e.set_thumbnail(url=interaction.user.display_avatar.url)

        await interaction.response.send_message(embed=embed("🔹 Canlı Test Mesajı Gönderildi", f"Test mesajı {interaction.channel.mention} kanalında yayınlandı:", MAVI), ephemeral=True)
        if dis_mesaj:
            await interaction.channel.send(content=dis_mesaj, embed=e)
        else:
            await interaction.channel.send(embed=e)

    @discord.ui.button(label="❌ Sistemi Kapat", style=discord.ButtonStyle.danger, custom_id="hosgeldin_sistem_kapat")
    async def sistem_kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        data = guild_section(interaction.guild_id, "hosgeldin_sistemi", {})
        data["aktif"] = False
        set_guild_section(interaction.guild_id, "hosgeldin_sistemi", data)
        await interaction.response.send_message(embed=embed("🔹 Hoş Geldin Sistemi Kapatıldı", "Sistem devre dışı bırakıldı.", MAVI), ephemeral=True)


@bot.command(name="hosgeldin-kur", aliases=["hoşgeldin-kur", "hosgeldinkur", "hoşgeldinkur", "welcome-setup"])
@commands.has_permissions(manage_guild=True)
async def hosgeldin_kur(ctx, kanal: discord.TextChannel = None):
    """
    Tek komut ve Modal (Pop-up Form) penceresi ile Hoş Geldin Sistemini kurar ve özelleştirir.
    Kullanım: .hosgeldin-kur [#kanal]
    """
    target_channel = kanal or ctx.channel
    data = guild_section(ctx.guild.id, "hosgeldin_sistemi", {})
    durum_metni = "Aktif" if data.get("aktif") else "Henüz Kurulmadı / Devre Dışı"

    e = embed(
        "🔹 Gelişmiş Hoş Geldin Kurulum Formu",
        f"**Seçilen Kanal:** {target_channel.mention}\n**Mevcut Durum:** `{durum_metni}`\n\n"
        "Aşağıdaki **⚙️ Formu Aç ve Kur (Modal)** butonuna basarak tüm metinleri, sadece dış mesajda etiketlenecek rolü, başlığı ve GIF görselini pop-up form penceresinde kolayca ayarlayabilirsiniz!\n\n"
        "**Formda Kullanabileceğiniz Değişkenler:**\n"
        "`{uye}` veya `{uye_etiket}` ➔ Üye Etiketi\n"
        "`{rol}` veya `{rol_etiket}` ➔ Etiketlenecek Rol *(Sadece Dış Mesajda)*\n"
        "`{uye_adi}` ➔ Üye Kullanıcı Adı\n"
        "`{sunucu}` ➔ Sunucu Adı\n"
        "`{uye_sayisi}` ➔ Toplam Üye Sayısı\n"
        "`{hesap_tarihi}` ➔ Hesap Açılış Tarihi",
        MAVI
    )

    await ctx.send(embed=e, view=HosgeldinKurulumView(author_id=ctx.author.id, channel=target_channel))


@bot.command(name="otorol", aliases=["oto-rol", "otomatikrol"])
@commands.has_permissions(manage_roles=True)
async def otorol(ctx, rol: discord.Role = None):
    """Sunucuya yeni katılan üyelere otomatik rol verir."""
    if rol is None:
        set_guild_section(ctx.guild.id, "otorol_id", None)
        await ctx.send(embed=embed("🔹 Otorol Kapatıldı", "Giriş yapan üyelere otomatik rol verilmesi kapatıldı.", MAVI))
        return
    set_guild_section(ctx.guild.id, "otorol_id", rol.id)
    await ctx.send(embed=embed("🔹 Otorol Ayarlandı", f"Sunucuya yeni katılan üyelere otomatik olarak {rol.mention} rolü verilecek.", MAVI))


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
    e = embed("🔹 Üye Uyarıldı", f"**Hedef:** {target.mention}\n**Toplam Uyarı:** `{count}`\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", MAVI)
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
        await ctx.send(embed=embed("🔹 Uyarı Kaydı Yok", f"{target.mention} için kayıtlı herhangi bir uyarı bulunmuyor.", MAVI))
        return

    e = embed("🔹 Uyarı Listesi", f"{target.mention} için toplam **{len(kayitlar)}** uyarı kaydı mevcut.", MAVI)
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
    await ctx.send(embed=embed("🔹 Uyarılar Temizlendi", f"{getattr(target, 'mention', str(target))} için tüm uyarı geçmişi silindi.", MAVI))


@bot.command(name="lock", aliases=["kilit"])
@commands.has_permissions(manage_channels=True)
async def lock(ctx, kanal: discord.TextChannel = None):
    kanal = kanal or ctx.channel
    await kanal.set_permissions(ctx.guild.default_role, send_messages=False, reason=f"{ctx.author} kanalı kilitledi")
    await ctx.send(embed=embed("🔹 Kanal Kilitlendi", f"{kanal.mention} mesaj gönderimine kapatıldı.", MAVI))


@bot.command(name="unlock", aliases=["kilitac", "kilitaç"])
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, kanal: discord.TextChannel = None):
    kanal = kanal or ctx.channel
    await kanal.set_permissions(ctx.guild.default_role, send_messages=None, reason=f"{ctx.author} kanalı açtı")
    await ctx.send(embed=embed("🔹 Kanal Açıldı", f"{kanal.mention} tekrar mesaj gönderimine açıldı.", MAVI))


@bot.command(name="slowmode", aliases=["sm", "yavaşmod"])
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, sure: int = 0):
    sure = max(0, min(sure, 21600))
    await ctx.channel.edit(slowmode_delay=sure, reason=f"{ctx.author} yavaş mod ayarladı")
    await ctx.send(embed=embed("🔹 Yavaş Mod Ayarlandı", f"Bu kanaldaki yavaş mod bekleme süresi **{sure} saniye** olarak ayarlandı.", MAVI))


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
    e = embed("📢 Duyuru", mesaj or "Yeni duyuru", MAVI)
    if ctx.guild.icon:
        e.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
    else:
        e.set_author(name=ctx.guild.name)
    if image_url:
        e.set_image(url=image_url)
    if ctx.author.display_avatar:
        e.set_footer(text=f"Duyuran: {ctx.author} | {timestamp()}", icon_url=ctx.author.display_avatar.url)
    await kanal.send(embed=e)
    await ctx.send(embed=embed("🔹 Duyuru Gönderildi", f"Duyuru başarıyla {kanal.mention} kanalına yayınlandı.", MAVI))


# ==========================================
# ÇEKİLİŞ VE AFK KOMUTLARI
# ==========================================

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
        await ctx.send(embed=error_embed("Jail Hazır Değil", f"Önce `{PREFIX}jailkur` komutunu çalıştırarak kurulum yapın."))
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
    e = embed("🔹 Üye Jaile Atıldı", f"**Hedef:** {target.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", MAVI)
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
    e = embed("🔹 Jail Kaldırıldı", f"{target.mention} için eski roller başarıyla iade edildi.", MAVI)
    await ctx.send(embed=e)
    await log_gonder(ctx.guild, "mod_log", e)


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
    await ctx.send(embed=embed("🔹 AFK Modu Açıldı", f"{ctx.author.mention} artık AFK modunda.\n**Sebep:** {sebep}", MAVI))


async def afk_cikar(message: discord.Message, kayit: dict):
    old_nick = kayit.get("old_nick")
    try:
        await message.author.edit(nick=old_nick, reason="AFK modu kapandı")
    except discord.Forbidden:
        pass
    def edit(data):
        data.setdefault(str(message.guild.id), {}).setdefault("afk_users", {}).pop(str(message.author.id), None)
    update_settings(edit)
    await message.channel.send(embed=embed("🔹 AFK Modu Kapandı", f"{message.author.mention}, tekrar hoş geldiniz! AFK modundan çıktınız.", MAVI))


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
        await kanal.send(embed=embed("🔹 Destek Talebi Oluşturuldu", f"{interaction.user.mention}, destek ekibimiz en kısa sürede ilgilenecektir.", MAVI), view=TicketCloseView())
        await interaction.response.send_message(embed=embed("🔹 Ticket Açıldı", f"Destek kanalınız oluşturuldu: {kanal.mention}", MAVI), ephemeral=True)
        if isinstance(log_kanal, discord.TextChannel):
            await log_kanal.send(embed=embed("🔹 Ticket Oluşturuldu", f"**Üye:** {interaction.user.mention}\n**Kanal:** {kanal.mention}", MAVI))


class TicketCloseView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Ticket Kapat 🔒", style=discord.ButtonStyle.danger, custom_id="ticket_kapat")
    async def ticket_kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not isinstance(interaction.channel, discord.TextChannel) or not interaction.channel.name.startswith("ticket-"):
            await interaction.response.send_message(embed=error_embed("Geçersiz Kanal", "Bu buton yalnızca ticket kanallarında çalışır."), ephemeral=True)
            return
        await interaction.response.send_message(embed=embed("🔹 Ticket Kapatılıyor", "Bu kanal 5 saniye içinde silinecektir.", MAVI))
        await asyncio.sleep(5)
        await interaction.channel.delete(reason=f"{interaction.user} ticket kapattı")


@bot.command(name="ticketpanel", aliases=["ticket-panel"])
@commands.has_permissions(manage_guild=True)
async def ticketpanel(ctx):
    await ctx.send(embed=embed("🔹 Destek Talebi Paneli", "Destek ekibimizle iletişime geçmek için aşağıdaki butona tıklayarak ticket oluşturabilirsiniz.", MAVI), view=TicketView())


@bot.command(name="ticketkapat", aliases=["ticket-kapat"])
async def ticketkapat(ctx):
    if not ctx.channel.name.startswith("ticket-"):
        await ctx.send(embed=error_embed("Geçersiz Kanal", "Bu komut yalnızca ticket kanallarında kullanılabilir."))
        return
    await ctx.send(embed=embed("🔹 Ticket Kapatılıyor", "Kanal 5 saniye içinde silinecektir.", MAVI))
    await asyncio.sleep(5)
    await ctx.channel.delete(reason=f"{ctx.author} ticket kapattı")


@bot.command(name="ticketekle", aliases=["ticket-ekle"])
async def ticketekle(ctx, *args):
    target, _ = await hedef_uye_bul(ctx, *args)
    if target is None or not isinstance(target, discord.Member):
        await ctx.send(embed=usage_embed(f"`{PREFIX}ticketekle @üye`"))
        return
    await ctx.channel.set_permissions(target, view_channel=True, send_messages=True, read_message_history=True)
    await ctx.send(embed=embed("🔹 Üye Eklendi", f"{target.mention} tickete eklendi.", MAVI))


@bot.command(name="ticketcikar", aliases=["ticket-çıkar"])
async def ticketcikar(ctx, *args):
    target, _ = await hedef_uye_bul(ctx, *args)
    if target is None or not isinstance(target, discord.Member):
        await ctx.send(embed=usage_embed(f"`{PREFIX}ticketcikar @üye`"))
        return
    await ctx.channel.set_permissions(target, overwrite=None)
    await ctx.send(embed=embed("🔹 Üye Çıkarıldı", f"{target.mention} ticketten çıkarıldı.", MAVI))


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
    end_embed = embed("🎉 ÇEKİLİŞ BİTTİ 🎉", f"**Ödül:** {data.get('prize')}\n**Kazanan:** {winners_text}\n**Toplam Katılımcı:** {len(users)}", MAVI)
    if data.get("gif_url"):
        end_embed.set_image(url=data["gif_url"])
    try:
        await msg.edit(embed=end_embed)
    except discord.HTTPException:
        pass
    giveaway_set(guild_id, message_id, None)
    if winners:
        await channel.send(embed=embed("🔹 Tebrikler!", f"{winners_text}\n**{data.get('prize')}** kazandınız!", MAVI))
    elif forced:
        await channel.send(embed=embed("🔹 Çekiliş Sonlandırıldı", "Katılımcı olmadığı için kazanan seçilemedi.", MAVI))


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
            msg1 = await ctx.send(embed=embed("🔹 Çekiliş Kurulumu (1/4)", "Çekiliş süresi nedir? (Örn: `10m`, `1h`, `1d`)\nİptal etmek için `iptal` yazın.", MAVI))
            res1 = await bot.wait_for("message", check=check, timeout=60.0)
            if res1.content.lower() in ["iptal", "cancel"]:
                await ctx.send(embed=embed("🔹 İşlem İptal Edildi", "Çekiliş kurulumu iptal edildi.", MAVI))
                return
            sure = res1.content.strip()
            parse_duration(sure)

            # 2. Kazanan sayısı sor
            msg2 = await ctx.send(embed=embed("🔹 Çekiliş Kurulumu (2/4)", "Kaç kazanan olacak? (Örn: `1`)", MAVI))
            res2 = await bot.wait_for("message", check=check, timeout=60.0)
            kazanan = max(1, int(re.sub(r"\D", "", res2.content) or 1))

            # 3. Ödül sor
            msg3 = await ctx.send(embed=embed("🔹 Çekiliş Kurulumu (3/4)", "Çekiliş ödülü nedir? (Örn: `Discord Nitro`)", MAVI))
            res3 = await bot.wait_for("message", check=check, timeout=60.0)
            odul = res3.content.strip()

            # 4. GIF / Görsel linki sor
            msg4 = await ctx.send(embed=embed("🔹 Çekiliş Kurulumu (4/4)", "Çekiliş için GIF veya Görsel linki gönderin:\n*(Görsel eklemek istemiyorsanız **pas** veya **yok** yazın)*", MAVI))
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

            await ctx.send(embed=embed("🔹 Çekiliş GIF Linki", "Çekiliş için bir GIF / Görsel linki eklemek ister misiniz?\n*(İstemiyorsanız **pas** yazın, 15 saniye sonra otomatik geçilir)*", MAVI))
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
        MAVI
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
    await ctx.send(embed=embed("🔹 Çekiliş Yenilendi", f"Yeni Kazanan: {' '.join(u.mention for u in winners)}", MAVI))


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
    await ctx.send(embed=embed("🔹 Çekiliş Katılımcıları", text, MAVI))


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
    await ctx.send(embed=embed("🔹 Çekiliş İptal Edildi", "Çekiliş mesajı ve kaydı başarıyla silindi.", MAVI))


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
    e = embed("🔹 Çekiliş Bilgisi", f"**Ödül:** {data.get('prize')}\n**Kazanan:** {data.get('winners')}\n**Bitiş:** <t:{int(end_time.timestamp())}:R>", MAVI)
    if data.get("gif_url"):
        e.set_image(url=data["gif_url"])
    await ctx.send(embed=e)


@bot.command(name="avatar")
async def avatar(ctx, *args):
    target, _ = await hedef_uye_bul(ctx, *args)
    target = target or ctx.author
    if not isinstance(target, discord.Member):
        target = ctx.author

    e = embed("🔹 Profil Resmi / Avatar", f"{target.mention} için avatar görüntüsü:", MAVI)
    e.set_image(url=target.display_avatar.url)
    await ctx.send(embed=e)


@bot.command(name="sunucu", aliases=["serverinfo"])
async def sunucu(ctx):
    g = ctx.guild

    toplam_uye = g.member_count
    botlar = sum(1 for m in g.members if m.bot)
    kisiler = toplam_uye - botlar
    online = sum(1 for m in g.members if m.status != discord.Status.offline and not m.bot)

    seste_olanlar = sum(len(vc.members) for vc in g.voice_channels)
    aktif_ses_kanali = sum(1 for vc in g.voice_channels if len(vc.members) > 0)

    tag_alanlar = 0
    for m in g.members:
        pg = getattr(m, "primary_guild", None)
        if pg and getattr(pg, "identity_enabled", False) and getattr(pg, "identity_guild_id", None) == g.id:
            tag_alanlar += 1

    metin_kanal = len(g.text_channels)
    ses_kanal = len(g.voice_channels)
    kategori = len(g.categories)

    e = embed("🔹 Sunucu Bilgileri", f"**{g.name}** sunucusu genel istatistikleri:", MAVI)
    e.add_field(name="👥 Toplam Üye", value=str(toplam_uye), inline=True)
    e.add_field(name="🙋 Kişi Sayısı", value=str(kisiler), inline=True)
    e.add_field(name="🤖 Bot Sayısı", value=str(botlar), inline=True)
    e.add_field(name="🟢 Çevrimiçi Üye", value=str(online), inline=True)
    e.add_field(name="🔊 Seste Olan Kişi", value=str(seste_olanlar), inline=True)
    e.add_field(name="📡 Aktif Ses Kanalı", value=f"{aktif_ses_kanali} / {ses_kanal}", inline=True)
    e.add_field(name="🏷️ Sunucu Etiketi Almış", value=str(tag_alanlar), inline=True)
    e.add_field(name="💬 Metin Kanalı", value=str(metin_kanal), inline=True)
    e.add_field(name="📁 Kategori Sayısı", value=str(kategori), inline=True)
    e.add_field(name="🎭 Rol Sayısı", value=str(len(g.roles)), inline=True)
    e.add_field(name="📅 Kuruluş Tarihi", value=g.created_at.strftime("%d.%m.%Y %H:%M"), inline=True)
    if g.owner:
        e.add_field(name="👑 Sunucu Sahibi", value=g.owner.mention, inline=True)
    e.add_field(name="🚀 Boost Seviyesi", value=f"Seviye {g.premium_tier} ({g.premium_subscription_count} boost)", inline=True)
    if g.icon:
        e.set_thumbnail(url=g.icon.url)
    await ctx.send(embed=e)


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(embed=embed("🔹 Pong!", f"Gecikme süresi: `{round(bot.latency * 1000)}ms`", MAVI))


async def gelismis_yardim(ctx):
    e = embed("🔹 LogBot Komut Rehberi 🔹", "Tüm sistemler Modal (Pop-up Form) kurulumu ile 100% interaktiftir.", MAVI)
    e.add_field(name="⚙️ Modal (Form) Kurulum Komutları", value="`hosgeldin-kur`, `log-kur`, `kufur-kur`, `link-kur`, `spam-kur`, `jailkur`, `ticketkur`", inline=False)
    e.add_field(name="🛡️ Moderasyon & Rol Yönetimi", value="`ban`, `unban`, `kick`, `mute`, `unmute`, `sil`, `warn`, `uyarlar`, `uyarsil`, `jail`, `unjail`, `lock`, `unlock`, `slowmode`, `herkeserol`, `herkeserolsil`, `otorol`", inline=False)
    e.add_field(name="🔒 Koruma & Güvenlik Kapatma", value="`kufur-kapat`, `link-koruma-kapat`, `spam-koruma-kapat`", inline=False)
    e.add_field(name="🎉 Çekiliş & Bilet & Genel", value="`gstart`, `gend`, `greroll`, `glist`, `gdelete`, `ginfo`, `ticketpanel`, `ticketkapat`, `afk`, `duyuru`, `say`", inline=False)
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
            await message.channel.send(embed=embed("🔹 Bu Üye Şu An AFK", f"{member.mention} şu anda AFK modunda.\n**Sebep:** {kayit.get('sebep', 'AFK')}{since_text}", MAVI))

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
            e = error_embed("🔹 Küfür Engellendi", f"{message.author.mention}, bu sunucuda küfür kullanımı yasaktır.")
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
            e = error_embed("🔹 Link Engellendi", f"{message.author.mention}, bu kanalda link paylaşılması yasaktır.")
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
            e = embed("🔹 Spam Cezası", f"{message.author.mention} spam nedeniyle **{format_duration(seconds)}** boyunca susturuldu.", MAVI)
            await message.channel.send(embed=e, delete_after=10)
            await log_gonder(message.guild, "mute_log", e)
            spam_cache[key] = []


@bot.event
async def on_member_ban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_user(guild, discord.AuditLogAction.ban, user)
    e = embed("🔹 Ban Logu", f"**Kullanıcı:** {user} (`{user.id}`)\n**Yetkili:** {sorumlu.mention if sorumlu else 'Bilinmiyor'}", MAVI)
    await log_gonder(guild, "ban_log", e)


@bot.event
async def on_member_unban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_user(guild, discord.AuditLogAction.unban, user)
    e = embed("🔹 Unban Logu", f"**Kullanıcı:** {user} (`{user.id}`)\n**Yetkili:** {sorumlu.mention if sorumlu else 'Bilinmiyor'}", MAVI)
    await log_gonder(guild, "ban_log", e)


@bot.event
async def on_member_join(member: discord.Member):
    # Log gönderimi
    await log_gonder(member.guild, "giris_cikis", embed("🔹 Üye Katıldı", f"{member.mention} sunucuya katıldı.\n**Kullanıcı ID:** `{member.id}`", MAVI))

    # Otomatik Rol
    otorol_id = guild_section(member.guild.id, "otorol_id", None)
    if otorol_id:
        rol = member.guild.get_role(int(otorol_id))
        if rol and rol < member.guild.me.top_role:
            try:
                await member.add_roles(rol, reason="Otomatik rol verme (Otorol)")
            except (discord.Forbidden, discord.HTTPException):
                pass

    # Hoş Geldin Mesajı Gönderimi
    hosgeldin = guild_section(member.guild.id, "hosgeldin_sistemi", {})
    if hosgeldin.get("aktif"):
        kanal_id = hosgeldin.get("kanal_id")
        if kanal_id:
            kanal = member.guild.get_channel(int(kanal_id))
            if isinstance(kanal, discord.TextChannel):
                dis_mesaj = format_welcome_text(hosgeldin.get("dis_mesaj") or DEFAULT_HOSGELDIN_DIS_MESAJ, member, hosgeldin.get("rol_id"), is_dis_mesaj=True)
                baslik = format_welcome_text(hosgeldin.get("baslik") or DEFAULT_HOSGELDIN_BASLIK, member, hosgeldin.get("rol_id"), is_dis_mesaj=False)
                aciklama = format_welcome_text(hosgeldin.get("aciklama") or DEFAULT_HOSGELDIN_ACIKLAMA, member, hosgeldin.get("rol_id"), is_dis_mesaj=False)
                resim_url = hosgeldin.get("resim_url")

                e = embed(baslik, aciklama, MAVI)
                if resim_url:
                    e.set_image(url=resim_url)
                if member.display_avatar:
                    e.set_thumbnail(url=member.display_avatar.url)

                try:
                    if dis_mesaj:
                        await kanal.send(content=dis_mesaj, embed=e)
                    else:
                        await kanal.send(embed=e)
                except (discord.Forbidden, discord.HTTPException):
                    pass


@bot.event
async def on_member_remove(member: discord.Member):
    await log_gonder(member.guild, "giris_cikis", embed("🔹 Üye Ayrıldı", f"**{member}** sunucudan ayrıldı.\n**Kullanıcı ID:** `{member.id}`", MAVI))


@bot.event
async def on_message_delete(message: discord.Message):
    if message.author.bot or not message.guild:
        return
    e = embed("🔹 Mesaj Silindi", f"**Kullanıcı:** {message.author.mention}\n**Kanal:** {message.channel.mention}\n**Silinen Mesaj:** {short(message.content or 'İçerik yok', 900)}", MAVI)
    await log_gonder(message.guild, "mesaj_log", e)


@bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    if before.author.bot or not before.guild or before.content == after.content:
        return
    e = embed("🔹 Mesaj Düzenlendi", f"**Kullanıcı:** {before.author.mention}\n**Kanal:** {before.channel.mention}\n**Önce:** {short(before.content, 450)}\n**Sonra:** {short(after.content, 450)}", MAVI)
    await log_gonder(before.guild, "mesaj_log", e)


@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    if before.timed_out_until != after.timed_out_until:
        if after.timed_out_until:
            e = embed("🔹 Timeout Verildi", f"**Üye:** {after.mention}\n**Bitiş:** <t:{int(after.timed_out_until.timestamp())}:R>", MAVI)
        else:
            e = embed("🔹 Timeout Kaldırıldı", f"**Üye:** {after.mention}", MAVI)
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
        await log_gonder(after.guild, "rol_log", embed("🔹 Rol Değişikliği", f"**Üye:** {after.mention}\n{text}", MAVI))


@bot.event
async def on_guild_channel_create(channel):
    await log_gonder(channel.guild, "kanal_log", embed("🔹 Kanal Oluşturuldu", f"**Kanal:** {channel.mention if hasattr(channel, 'mention') else channel.name}", MAVI))


@bot.event
async def on_guild_channel_delete(channel):
    await log_gonder(channel.guild, "kanal_log", embed("🔹 Kanal Silindi", f"**Kanal İsmi:** {channel.name}", MAVI))


@bot.event
async def on_guild_role_create(role: discord.Role):
    await log_gonder(role.guild, "rol_log", embed("🔹 Rol Oluşturuldu", f"**Rol:** {role.mention}", MAVI))


@bot.event
async def on_guild_role_delete(role: discord.Role):
    await log_gonder(role.guild, "rol_log", embed("🔹 Rol Silindi", f"**Rol İsmi:** {role.name}", MAVI))


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
    await log_gonder(member.guild, "ses_log", embed("🔹 Ses Logu", text, MAVI))


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
