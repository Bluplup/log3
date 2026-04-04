"""
Discord Log Botu - discord.py
ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â
Kanal ID'lerini kod iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ine yazmak gerekmez!
TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m ayarlar Discord komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±yla yapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r ve
settings.json dosyasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na otomatik kaydedilir.

Gereksinimler:
    pip install discord.py

Komutlar (Slash komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±):
    /log-kur <tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r> <kanal>     ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Belirli bir log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in kanal atar
    /log-kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r <tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r>          ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Belirli bir log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ devre dÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rakÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r
    /log-durum                 ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m log kanallarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± listeler
    /log-sifirla               ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± siler
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

# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  AYARLAR
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

# Token environment variable'dan okunur
# Render: Dashboard ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Environment ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ BOT_TOKEN ekle
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
# Bu surece ozel ID (loglarda / Mongo heartbeat ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â baska yerde calisan kopyayi ayirt etmek icin)
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
    True  -> Bu sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼reÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ prefix komutunu ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§alÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rmalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± (kilit alÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±).
    False -> BaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ka bir sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼reÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ / bot aynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± mesaj iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in kilidi zaten aldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.
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
            "Sunucuda iki ayri Discord BOT UYGULAMASI varsa her ikisi de cevap verir ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â fazla botu sunucudan at veya tek bot kullan."
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
                            f"  ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¹ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â  Coklu-surec izleme: harici surec izleme pasif ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â baska yerde calisan kopyayi "
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
                        f"  ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â  {len(aktif)} AYRI SUREC (son ~2dk) ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â cift mesaj normal: "
                        f"{' | '.join(ozet)}"
                    )
                elif ilk_uyarni:
                    print(
                        f"  ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Coklu-surec izleme: Mongo'da son 2 dk icinde yalniz bu instance kayitli "
                        f"({BOT_INSTANCE_ID[:10]}..)"
                    )
                    ilk_uyarni = False
        except Exception as e:
            print(f"  [UYARI] Instance izleme dongusu: {e}")
        await asyncio.sleep(75)

# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  SABÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°T LOG KANALLARI (deploy'dan etkilenmez)
#  Kod gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ncellendiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸inde settings.json silinse bile
#  bu ID'ler otomatik olarak yeniden yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼klenir.
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
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

# Partner kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ID'si (partner textinin atÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kanal)
# DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tirmek istersen buraya yaz
DEFAULT_PARTNER_TEXT_KANALI = 1396219864279945397
DEFAULT_PARTNER_LOG_KANALI  = 1484813767253430363

# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Sabit Log KanallarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
# Bu kanallar her deploy sonrasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± otomatik yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼klenir.
# DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tirmek istersen buradan dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼zenle.
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

# Desteklenen log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rleri ve aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±klamalarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±
LOG_TURLERI = {
    "ban_log":      "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨ Ban / Unban loglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
    "mute_log":     "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ Mute loglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
    "mod_log":      "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Genel moderasyon loglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
    "rol_log":      "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â­ Rol deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklik loglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
    "mesaj_log":    "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Mesaj silme/dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼zenleme loglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
    "giris_cikis":  "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Âª ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye giriÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸/ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±kÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ loglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
    "ses_log":      "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â  Ses kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± loglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
    "kanal_log":    "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Kanal oluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turma/silme loglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
    "davet_log":    "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Davet loglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
}

# Otomatik log kurulumunda aranacak kanal adÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â± kalÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±plarÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±
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

# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  AYAR YÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“NETÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°MÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â° (settings.json)
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

def ayarlari_yukle() -> dict:
    """
    ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“nce Supabase'ten, yoksa yerel fallback dosyasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± okur.
    YapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±: { "guild_id": { "log_turu": kanal_id, ... }, ... }
    Dosya yoksa boÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ dict dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r.
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
    VarsayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lan log kanallarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± settings.json'a yazar.
    Her bot baÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸langÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nda ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§aÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â mevcut ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼zerine yazmaz,
    sadece eksik olanlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± tamamlar.
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
    """TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nce Supabase'e, o yoksa yerel dosyaya yazar."""
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
    Belirli bir sunucu ve log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in kayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±tlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kanal ID'sini dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r.
    KayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±tlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilse None dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r.
    """
    ayarlar = ayarlari_yukle()
    return ayarlar.get(str(guild_id), {}).get(tur)


def kanal_kaydet(guild_id: int, tur: str, kanal_id: int):
    """Bir log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in kanal ID'sini settings.json'a kaydeder."""
    with _ayar_dosya_kilidi:
        ayarlar = ayarlari_yukle()
        guild_key = str(guild_id)
        if guild_key not in ayarlar:
            ayarlar[guild_key] = {}
        ayarlar[guild_key][tur] = kanal_id
        ayarlari_kaydet(ayarlar)


def kanal_sil(guild_id: int, tur: str):
    """Bir log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼n kanal kaydÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± siler (devre dÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rakÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r)."""
    with _ayar_dosya_kilidi:
        ayarlar = ayarlari_yukle()
        guild_key = str(guild_id)
        if guild_key in ayarlar and tur in ayarlar[guild_key]:
            del ayarlar[guild_key][tur]
            ayarlari_kaydet(ayarlar)


def guild_ayarlari_sil(guild_id: int):
    """Bir sunucunun tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m log ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± tamamen siler."""
    with _ayar_dosya_kilidi:
        ayarlar = ayarlari_yukle()
        guild_key = str(guild_id)
        if guild_key in ayarlar:
            del ayarlar[guild_key]
            ayarlari_kaydet(ayarlar)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  BOT KURULUMU
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

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
    """AynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Discord mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in baÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ka bir bot sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼reci prefix komutunu zaten iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ledi."""


@bot.check
async def prefix_komut_mesaj_kilidi(ctx: commands.Context):
    """Opsiyonel dagitik kilit: PREFIX_CMD_LOCK=1 (cift bot) ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â varsayilan kapali, hiz icin."""
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


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  YARDIMCI FONKSÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°YONLAR
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

async def log_gonder(guild: discord.Guild, tur: str, embed: discord.Embed):
    """
    settings.json'dan ilgili log kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bulup embed gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderir.
    Kanal ayarlanmamÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸sa veya bulunamazsa sessizce geÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§er.
    """
    kanal_id = kanal_al(guild.id, tur)
    if not kanal_id:
        return  # Bu log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in kanal ayarlanmamÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸

    kanal = guild.get_channel(kanal_id)
    if not kanal:
        return  # Kanal daha sonra silinmiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ olabilir

    try:
        await kanal.send(embed=embed)
    except discord.Forbidden:
        print(f"[HATA] '{tur}' kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na yazma izni yok.")
    except discord.HTTPException as e:
        print(f"[HATA] Log gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderilemedi: {e}")


def utc_datetime_from_iso(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def zaman_damgasi() -> str:
    now = datetime.now(timezone.utc)
    return now.strftime("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ %d.%m.%Y ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â° %H:%M:%S UTC")


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
        title="Komut KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        description=description,
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=zaman_damgasi())
    return embed


class TicketControlView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ Kapat", style=discord.ButtonStyle.danger, custom_id="ticket_kapat")
    async def kapat(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message("ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Bu buton sadece ticket kanalÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±nda kullanÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±labilir.", ephemeral=True)
            return

        ayar = ticket_ayar_al(interaction.guild_id)
        log_id = ayar.get("log")
        await _ticket_kapat_logu_ve_transkript(channel, interaction.user, log_id)
        if False and log_id:
            log_kanali = interaction.guild.get_channel(log_id)
            if log_kanali:
                await log_kanali.send(embed=discord.Embed(
                    title="ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ Ticket KapatÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±ldÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±",
                    description=f"**Ticket:** `{channel.name}`\n**Kapatan:** {interaction.user.mention}",
                    color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)
                ))

        await interaction.response.send_message("Ticket kapatÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±lÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±yor...", ephemeral=True)
        await channel.delete(reason=f"{interaction.user} tarafÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±ndan kapatÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±ldÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±")

    @discord.ui.button(label="ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¹Ã…â€œÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¥ ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œye Ekle", style=discord.ButtonStyle.secondary, custom_id="ticket_uyeekle")
    async def uye_ekle(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message("ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Bu buton sadece ticket kanalÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±nda kullanÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±labilir.", ephemeral=True)
            return

        await interaction.response.send_message("Eklemek istediÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸in kullanÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±cÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±yÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â± bu kanalda etiketle: @kullanÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±cÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±", ephemeral=True)

        def check(message: discord.Message):
            return message.author == interaction.user and message.channel == channel and message.mentions

        try:
            yanit = await bot.wait_for("message", check=check, timeout=30)
            for uye in yanit.mentions:
                await channel.set_permissions(uye, read_messages=True, send_messages=True)
            await channel.send(f"ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¦ {' '.join(u.mention for u in yanit.mentions)} ticketa eklendi.")
            await yanit.delete()
        except asyncio.TimeoutError:
            await channel.send("ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³ KullanÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±cÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â± ekleme isteÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸inin sÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¼resi doldu.", delete_after=5)

    @discord.ui.button(label="ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¹ Talep Al", style=discord.ButtonStyle.success, custom_id="ticket_talep")
    async def talep_al(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if not isinstance(channel, discord.TextChannel) or not channel.name.startswith("ticket-"):
            await interaction.response.send_message("ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Bu buton sadece ticket kanalÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±nda kullanÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±labilir.", ephemeral=True)
            return

        ayar = ticket_ayar_al(interaction.guild_id)
        destek_rolu = interaction.guild.get_role(ayar.get("rol"))
        if destek_rolu and destek_rolu not in interaction.user.roles and not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Bu iÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸lem iÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§in destek rolÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¼ gerekli.", ephemeral=True)
            return

        yeni_topic = channel.topic or ""
        if " | Talep:" in yeni_topic:
            yeni_topic = yeni_topic.split(" | Talep:")[0]
        await channel.edit(topic=f"{yeni_topic} | Talep: {interaction.user}")
        await interaction.response.send_message(f"ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¦ Ticket {interaction.user.mention} tarafÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±ndan talep alÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±ndÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±.")


class TicketOpenView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â½ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â« Ticket AÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§", style=discord.ButtonStyle.primary, custom_id="global_ticket_ac")
    async def ticket_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
        ayar = ticket_ayar_al(interaction.guild_id)
        kategori = interaction.guild.get_channel(ayar.get("kategori"))
        destek_rolu = interaction.guild.get_role(ayar.get("rol"))
        log_id = ayar.get("log")

        if not kategori:
            await interaction.response.send_message("ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Kategori bulunamadÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±. `.ticketkur` ile yeniden kur.", ephemeral=True)
            return

        for kanal in kategori.text_channels:
            if kanal.topic and str(interaction.user.id) in kanal.topic:
                await interaction.response.send_message(f"ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Zaten aÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±k bir ticketÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±n var: {kanal.mention}", ephemeral=True)
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
            title=f"ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â½ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â« Ticket #{sayi:04d}",
            description=(
                f"Merhaba {interaction.user.mention}!\n"
                f"Destek ekibimiz en kÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±sa sÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¼rede yardÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±mcÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â± olacak.\n\n"
                f"TicketÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â± kapatmak iÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§in ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ butonunu kullan."
            ),
            color=0x57F287, timestamp=datetime.now(timezone.utc)
        )
        ac_embed.set_footer(text=f"Ticket #{sayi:04d} ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")

        await ticket_kanal.send(
            content=f"{interaction.user.mention}{(' ' + destek_rolu.mention) if destek_rolu else ''}",
            embed=ac_embed,
            view=TicketControlView()
        )
        await interaction.response.send_message(f"ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¦ TicketÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±n aÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±ldÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±: {ticket_kanal.mention}", ephemeral=True)

        if log_id:
            log_kanali = interaction.guild.get_channel(log_id)
            if log_kanali:
                await log_kanali.send(embed=discord.Embed(
                    title="ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â½ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â« Yeni Ticket AÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±ldÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±",
                    description=f"**AÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â§an:** {interaction.user.mention}\n**Kanal:** {ticket_kanal.mention}\n**Numara:** `#{sayi:04d}`",
                    color=RENKLER["giris"], timestamp=datetime.now(timezone.utc)
                ))


async def audit_log_bul(guild: discord.Guild, eylem: discord.AuditLogAction, hedef=None):
    """Audit log ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼zerinden en son iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi yapan kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iyi bulur."""
    try:
        async for log in guild.audit_logs(limit=5, action=eylem):
            if hedef is None or log.target.id == hedef.id:
                return log.user
    except discord.Forbidden:
        pass
    return None


def izin_adi_getir(perm_adi: str) -> str:
    """ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ngilizce izin adÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rkÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§eye ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§evirir. Bilinmeyenler aynen dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼lÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r."""
    ceviriler = {
        "administrator":            "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¡ YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶netici",
        "manage_guild":             "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â  Sunucuyu YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶net",
        "manage_roles":             "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â­ Rolleri YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶net",
        "manage_channels":          "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â KanallarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶net",
        "manage_messages":          "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â MesajlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶net",
        "manage_nicknames":         "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Takma AdlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶net",
        "manage_webhooks":          "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Webhook'larÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶net",
        "manage_expressions":       "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¹Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°fadeleri YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶net",
        "manage_threads":           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Âµ KonularÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶net",
        "kick_members":             "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¢ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye At",
        "ban_members":              "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye Banla",
        "moderate_members":         "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“yeleri Sustur",
        "view_audit_log":           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Denetim GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nlÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶r",
        "view_guild_insights":      "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Sunucu ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼lerini GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶r",
        "send_messages":            "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¬ Mesaj GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nder",
        "send_tts_messages":        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â  TTS MesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nder",
        "embed_links":              "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Link ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“nizlemesi",
        "attach_files":             "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Dosya Ekle",
        "read_message_history":     "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬Å“ Mesaj GeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§miÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ini Oku",
        "mention_everyone":         "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â£ @everyone Etiketle",
        "use_external_emojis":      "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¹Ã…â€œÃƒâ€šÃ‚Â Harici Emoji Kullan",
        "use_external_stickers":    "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¼ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Harici ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±kartma Kullan",
        "add_reactions":            "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â Tepki Ekle",
        "use_slash_commands":       "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ Slash KomutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Kullan",
        "connect":                  "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Ses KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na BaÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸lan",
        "speak":                    "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â KonuÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸",
        "stream":                   "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¡ YayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n Yap",
        "use_voice_activation":     "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¤ Sesle EtkinleÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tir",
        "mute_members":             "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“yeleri Sustur (Ses)",
        "deafen_members":           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“yeleri SaÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rlaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r",
        "move_members":             "ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“yeleri TaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        "priority_speaker":         "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ncelikli KonuÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸macÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        "create_instant_invite":    "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â AnÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nda Davet OluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tur",
        "change_nickname":          "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Takma Ad DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tir",
        "view_channel":             "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶r",
        "request_to_speak":         "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ KonuÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ma ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°steÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸i",
        "use_embedded_activities":  "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â® Aktiviteleri Kullan",
        "send_messages_in_threads": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Âµ Konularda Mesaj GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nder",
        "create_public_threads":    "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¢ Herkese AÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k Konu OluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tur",
        "create_private_threads":   "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“zel Konu OluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tur",
    }
    return ceviriler.get(perm_adi, f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â§ {perm_adi.replace('_', ' ').title()}")


def izin_farklarini_bul(eski: discord.Permissions, yeni: discord.Permissions):
    """
    ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ki Permissions nesnesi arasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndaki farklarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± hesaplar.

    MantÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k:
        - Her izin True/False deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸eri taÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r.
        - Eski ve yeni deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸erleri karÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±laÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rarak:
            * False ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ True  : izin EKLENDÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°
            * True  ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ False : izin KALDIRILDI
        - DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸meyenler atlanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r.

    DÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r:
        eklenenler   : list[str] ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â eklenen izinlerin TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rkÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§e isimleri
        kaldirlanlar : list[str] ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lan izinlerin TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rkÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§e isimleri
    """
    eklenenler   = []
    kaldirlanlar = []

    # discord.Permissions.__iter__() ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ (izin_adÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±, bool) ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§iftleri dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r
    eski_dict = dict(eski)
    yeni_dict = dict(yeni)

    for perm_adi in eski_dict:
        eski_deger = eski_dict[perm_adi]
        yeni_deger = yeni_dict.get(perm_adi, False)

        if eski_deger == yeni_deger:
            continue  # DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklik yok, atla

        ad = izin_adi_getir(perm_adi)

        if not eski_deger and yeni_deger:
            eklenenler.append(ad)       # False ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ True: eklendi
        elif eski_deger and not yeni_deger:
            kaldirlanlar.append(ad)     # True ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ False: kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±

    return eklenenler, kaldirlanlar


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  SLASH KOMUTLARI ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â LOG AYARLARI
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

# Slash komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nda aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r menÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in seÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§enek listesi
LOG_TUR_SECENEKLERI = [
    app_commands.Choice(name=aciklama, value=tur)
    for tur, aciklama in LOG_TURLERI.items()
]


@bot.tree.command(name="log-kur", description="Bir log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in kanal atar")
@app_commands.describe(
    tur="Hangi log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in kanal ayarlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±yorsunuz?",
    kanal="LoglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderileceÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸i metin kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±"
)
@app_commands.choices(tur=LOG_TUR_SECENEKLERI)
@app_commands.checks.has_permissions(manage_guild=True)
async def log_kur(
    interaction: discord.Interaction,
    tur: app_commands.Choice[str],
    kanal: discord.TextChannel
):
    """
    Belirli bir log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in kanal atar ve settings.json'a kaydeder.
    Sadece 'Sunucuyu YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶net' iznine sahip kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iler kullanabilir.
    """

    # Bota kanalda yazma izni var mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±?
    if not kanal.permissions_for(interaction.guild.me).send_messages:
        embed = discord.Embed(
            title="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Yetki HatasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
            description=f"{kanal.mention} kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na mesaj gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderemiyorum.\nKanal izinlerimi kontrol edin.",
            color=RENKLER["hata"]
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    # AyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kaydet
    kanal_kaydet(interaction.guild_id, tur.value, kanal.id)

    # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Sana ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶zel onay mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± (sadece sen gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rsÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼n) ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
    onay_embed = discord.Embed(
        title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Log KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± AyarlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    onay_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Log TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼", value=tur.name,      inline=True)
    onay_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Kanal",    value=kanal.mention, inline=True)
    onay_embed.set_footer(text=f"Ayarlayan: {interaction.user} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")
    await interaction.response.send_message(embed=onay_embed, ephemeral=True)

    # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Log kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na bilgilendirme mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
    kanal_embed = discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Log KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Aktif",
        description=f"Bu kanal **{tur.name}** iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in log kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± olarak ayarlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.\nArtÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k ilgili olaylar buraya dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ecek.",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    kanal_embed.add_field(name="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Ayarlayan", value=interaction.user.mention, inline=True)
    kanal_embed.set_footer(text=zaman_damgasi())
    await kanal.send(embed=kanal_embed)


@bot.tree.command(name="log-kaldir", description="Bir log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ devre dÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rakÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r")
@app_commands.describe(tur="Devre dÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rakÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lacak log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼")
@app_commands.choices(tur=LOG_TUR_SECENEKLERI)
@app_commands.checks.has_permissions(manage_guild=True)
async def log_kaldir(
    interaction: discord.Interaction,
    tur: app_commands.Choice[str]
):
    """Belirtilen log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼n kanal kaydÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± siler ve o logu durdurur."""

    mevcut = kanal_al(interaction.guild_id, tur.value)
    if not mevcut:
        embed = discord.Embed(
            title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Zaten Devre DÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
            description=f"**{tur.name}** iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in zaten bir kanal ayarlanmamÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸.",
            color=RENKLER["bilgi"]
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    kanal_sil(interaction.guild_id, tur.value)

    embed = discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Log KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        description=f"**{tur.name}** artÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k log gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndermeyecek.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=f"KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ran: {interaction.user}")
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name="log-durum", description="TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m log kanallarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ve durumlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶sterir")
@app_commands.checks.has_permissions(manage_guild=True)
async def log_durum(interaction: discord.Interaction):
    """
    Bu sunucudaki tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rlerini ve atanmÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ kanallarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± listeler.
    Kanal ayarlanmamÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸sa 'Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´ Deaktif' olarak gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶sterilir.
    """
    ayarlar = ayarlari_yukle().get(str(interaction.guild_id), {})

    embed = discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Log Sistemi Durumu",
        description=f"**{interaction.guild.name}** sunucusundaki log ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
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
            durum = kanal.mention if kanal else "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Kanal SilinmiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸"
        else:
            durum = "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´ Deaktif"

        satir = f"**{aciklama}**\nÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â° {durum}"

        if tur in mod_turleri:
            mod_satirlar.append(satir)
        else:
            genel_satirlar.append(satir)

    if mod_satirlar:
        embed.add_field(
            name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Moderasyon LoglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
            value="\n\n".join(mod_satirlar),
            inline=False
        )
    if genel_satirlar:
        embed.add_field(
            name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Genel Loglar",
            value="\n\n".join(genel_satirlar),
            inline=False
        )

    aktif = len([t for t in LOG_TURLERI if t in ayarlar])
    embed.set_footer(text=f"{aktif}/{len(LOG_TURLERI)} log tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ aktif ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")

    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name="log-sifirla", description="Bu sunucunun tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m log ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± siler")
@app_commands.checks.has_permissions(administrator=True)
async def log_sifirla(interaction: discord.Interaction):
    """
    Onay butonlu mesaj gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶stererek tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m log ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±fÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rlar.
    Sadece 'YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶netici' iznine sahip kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iler kullanabilir.
    """

    class OnayView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=30)

        @discord.ui.button(label="Evet, SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±fÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rla", style=discord.ButtonStyle.danger, emoji="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â")
        async def onayla(self, btn_i: discord.Interaction, button: discord.ui.Button):
            guild_ayarlari_sil(btn_i.guild_id)
            embed = discord.Embed(
                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m Log AyarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Silindi",
                description="Bu sunucuya ait tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m log kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±tlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
                color=RENKLER["hata"]
            )
            await btn_i.response.edit_message(embed=embed, view=None)

        @discord.ui.button(label="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ptal", style=discord.ButtonStyle.secondary, emoji="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â")
        async def iptal(self, btn_i: discord.Interaction, button: discord.ui.Button):
            embed = discord.Embed(
                title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ptal Edildi",
                description="SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±fÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rlama iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi iptal edildi, ayarlar korundu.",
                color=RENKLER["basari"]
            )
            await btn_i.response.edit_message(embed=embed, view=None)

    embed = discord.Embed(
        title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Emin misiniz?",
        description="Bu iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lem tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m log kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± **kalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± olarak** silecek.\nGeri alÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±namaz!",
        color=RENKLER["hata"]
    )
    await interaction.response.send_message(embed=embed, view=OnayView(), ephemeral=True)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  KÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“FÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“R KORUMASI
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

class KufurKorumasiModal(discord.ui.Modal, title="Kufur Korumasi Ayarlari"):
    """Yasak kelimeleri yapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±landÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rmak iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in modal."""
    
    yasakli_kelimeler = discord.ui.TextInput(
        label="Yasak Kelimeler (virgÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼l ile ayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z)",
        placeholder="ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶rnek: kelime1, kelime2, kelime3",
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
                    title="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Hata",
                    description="LÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼tfen en az bir kelime girin.",
                    color=RENKLER["hata"]
                ),
                ephemeral=True
            )
            return
        
        # Kelimeleri virgÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼l ile ayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r ve temizle
        kelimeler = [k.strip().lower() for k in metin.split(",") if k.strip()]
        
        if not kelimeler:
            await interaction.response.send_message(
                embed=discord.Embed(
                    title="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Hata",
                    description="LÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼tfen geÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§erli kelimeler girin.",
                    color=RENKLER["hata"]
                ),
                ephemeral=True
            )
            return
        
        # Ayarlara kaydet
        kufur_kelimelerini_kaydet(interaction.guild_id, kelimeler)
        
        await interaction.response.send_message(
            embed=discord.Embed(
                title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ KÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r KorumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± AyarlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
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
    """Sunucuya ait yasak kelimeleri dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r."""
    ayarlar = ayarlari_yukle()
    return ayarlar.get(str(guild_id), {}).get("yasakli_kelimeler", [])

def kufur_kontrol(guild_id: int, mesaj: str) -> bool:
    """Mesajda tam olarak yasaklÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kelime var mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kontrol eder, noktalama iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸aretlerini gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶z ardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± eder."""
    yasakli_kelimeler = kufur_kelimelerini_al(guild_id)
    if not yasakli_kelimeler:
        return False
    
    mesaj_temiz = mesaj.lower()
    # Kelimeleri ayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rken noktalama iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸aretlerini gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶z ardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± et
    mesaj_kelimeleri = re.findall(r'\b\w+\b', mesaj_temiz)
    
    for kelime in mesaj_kelimeleri:
        if kelime in yasakli_kelimeler:
            return True
    return False


def mesajda_yasakli_kelime_var_mi(mesaj: str, yasakli_kelimeler: list[str]) -> bool:
    """
    Mesajda yasak kelime olup olmadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kontrol eder.
    KÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±smi eÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸leÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸meleri de bulur (ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶rnek: 'test' yazarken 'testt' de bulur).
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
    Modal aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§arak kÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in yasak kelimeleri yapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±landÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r.
    Kelimeleri virgÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼l ile ayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rarak girin.
    """
    await ctx.send("Modal aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§mak iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in butona tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±klayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n:", view=KufurModalView())


@bot.command(name="kufur-durum")
@commands.has_permissions(manage_guild=True)
async def kufur_durum(ctx):
    """ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Âu anda tanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± olan yasak kelimeleri ve sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±larÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶sterir."""
    kelimeler = kufur_kelimelerini_al(ctx.guild.id)
    
    if not kelimeler:
        embed = discord.Embed(
            title="ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¹ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â KÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r KorumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
            description="Bu sunucuda henÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼z yasak kelime tanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mlanmamÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸.\n`.kufur-kur` komutu ile ayarla!",
            color=RENKLER["bilgi"]
        )
    else:
        # Kelimeleri gruplara ayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r (Discord mesaj limiti iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in)
        kelimeler_str = ", ".join(kelimeler[:50])  # ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°lk 50 gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ster
        if len(kelimeler) > 50:
            kelimeler_str += f", ... ve {len(kelimeler) - 50} kelime daha"
        
        embed = discord.Embed(
            title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â KÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r KorumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Aktif",
            description=f"**Toplam Yasak Kelime:** {len(kelimeler)}",
            color=RENKLER["basari"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(
            name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Yasak Kelimeler",
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
    """TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m yasak kelimeleri siler ve kÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r."""
    
    if ctx.guild.id not in _kufur_kelimeler:
        await ctx.send("Bu sunucuda zaten kÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ayarlanmamÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸.")
        return
    
    del _kufur_kelimeler[ctx.guild.id]
    kufur_kelimelerini_kaydet()
    
    embed = discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â KÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r KorumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Temizlendi",
        description="TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m yasak kelimeler silindi ve kÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=f"ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi yapan: {ctx.author}")
    
    await ctx.send(embed=embed)


# Kufur Modal View
class KufurModalView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Modal AÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§", style=discord.ButtonStyle.primary)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = KufurKorumasiModal()
        await interaction.response.send_modal(modal)


@bot.command(name="blubpatlat")
@commands.has_permissions(ban_members=True)
async def blubpatlat(ctx):
    """Sunucudaki tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yeleri banlar."""
    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.send("Botun ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yeleri banlama yetkisi yok!")
        return
    
    await ctx.send("TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yeler banlanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±yor... Bu iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lem uzun sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rebilir!")
    
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
        title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¡ Blubpatlat TamamlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        color=0xFF6B6B,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Banlanan ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye", value=f"**{ban_sayisi}** kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i", inline=True)
    embed.add_field(name="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Banlanamayan", value=f"**{hata_sayisi}** kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i", inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¥ Toplam ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye", value=f"**{len(ctx.guild.members)}** kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i", inline=True)
    embed.set_footer(text=f"ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi yapan: {ctx.author}")
    
    await ctx.send(embed=embed)


@bot.command(name="blupblup")
@commands.has_permissions(manage_roles=True)
async def blupblup(ctx, yeni_isim: str):
    """ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°sminde 'blup' geÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§en herkesin ismini deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tirir."""
    if not ctx.guild.me.guild_permissions.manage_nicknames:
        await ctx.send("Botun isim deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tirme yetkisi yok!")
        return
    
    await ctx.send("ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°simlerinde 'blup' aranÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±yor...")
    
    degistirilen = 0
    hata_sayisi = 0
    
    for member in ctx.guild.members:
        if member.bot:
            continue
        
        # Komutu yazanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± hariÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ tut
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
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Blupblup ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi TamamlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        color=0x5865F2,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tirilen ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye", value=f"**{degistirilen}** kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i", inline=True)
    embed.add_field(name="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tirilemeyen", value=f"**{hata_sayisi}** kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i", inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¥ Toplam ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye", value=f"**{len(ctx.guild.members)}** kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i", inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Yeni ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°sim", value=f"**{yeni_isim}**", inline=False)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Not", value=f"**{ctx.author}** hariÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ tutuldu", inline=False)
    embed.set_footer(text=f"ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi yapan: {ctx.author}")
    
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
            title="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Yetersiz Yetki",
            description="Bu komutu kullanmak iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in **Sunucuyu YÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶net** iznine ihtiyacÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z var.",
            color=RENKLER["hata"]
        )
        await ctx.send(embed=embed)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  OLAYLAR ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â MODERASYON LOGLARI
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

@bot.event
async def on_member_ban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_log_bul(guild, discord.AuditLogAction.ban, hedef=user)
    embed = discord.Embed(
        title="ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye BanlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        description=f"{user.mention} sunucudan yasaklandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
        color=RENKLER["ban"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"`{user}`", inline=True)
    embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ID", value=f"`{user.id}`", inline=True)
    embed.add_field(name="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(guild, "ban_log", embed)
    await _guvenlik_eylem_isle(guild, sorumlu, "ban", f"{user} ({user.id})", _guvenlik_ayar_al(guild.id).get("ban_limit", 3))


@bot.event
async def on_member_unban(guild: discord.Guild, user: discord.User):
    sorumlu = await audit_log_bul(guild, discord.AuditLogAction.unban, hedef=user)
    embed = discord.Embed(
        title="Ban KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        description=f"{user.mention} yeniden sunucuya katÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±labilir.",
        color=RENKLER["unban"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"`{user}`", inline=True)
    embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ID", value=f"`{user.id}`", inline=True)
    embed.add_field(name="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(guild, "ban_log", embed)


@bot.event
async def on_member_join(member: discord.Member):
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° Yeni ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye KatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", color=RENKLER["giris"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",       value=f"{member.mention} `{member}`",         inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Hesap OluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turma", value=member.created_at.strftime("%d.%m.%Y"), inline=True)
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(member.guild, "giris_cikis", embed)


@bot.event
async def on_member_remove(member: discord.Member):
    await asyncio.sleep(1)
    sorumlu = await audit_log_bul(member.guild, discord.AuditLogAction.kick, hedef=member)

    if sorumlu:
        embed = discord.Embed(
            title="ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye AtÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
            description=f"{member.mention} sunucudan atÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
            color=RENKLER["mute"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"`{member}`", inline=True)
        embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ID", value=f"`{member.id}`", inline=True)
        embed.add_field(name="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan", value=sorumlu.mention, inline=True)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(member.guild, "mod_log", embed)
        await _guvenlik_eylem_isle(member.guild, sorumlu, "kick", f"{member} ({member.id})", _guvenlik_ayar_al(member.guild.id).get("kick_limit", 3))
    else:
        embed = discord.Embed(
            title="ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye AyrÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
            description=f"{member.mention} sunucudan ayrÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
            color=RENKLER["cikis"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"`{member}`", inline=True)
        embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ID", value=f"`{member.id}`", inline=True)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(member.guild, "giris_cikis", embed)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  OLAYLAR ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ROL ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ZÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°N DEÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚ÂÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°KLÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â° LOGU
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

@bot.event
async def on_guild_role_update(onceki: discord.Role, sonraki: discord.Role):
    """
    Bir rol gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ncellendiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸inde tetiklenir.

    ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zin deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ikliklerini tespit eder:
        1. izin_farklarini_bul() ile eklenen/kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lan izinleri hesaplar.
        2. Audit log'dan deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ikliÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸i yapan kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iyi bulur.
        3. Estetik bir embed oluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turup rol_log kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderir.
    """

    # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ 1. ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zin farklarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± hesapla ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
    eklenenler, kaldirlanlar = izin_farklarini_bul(onceki.permissions, sonraki.permissions)

    # ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zin deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ikliÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸i yoksa diÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸er deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklikleri kontrol et (isim, renk vb.)
    if not eklenenler and not kaldirlanlar:
        degisiklikler = []
        if onceki.name  != sonraki.name:  degisiklikler.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°sim: `{onceki.name}` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ `{sonraki.name}`")
        if onceki.color != sonraki.color: degisiklikler.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨ Renk: `{onceki.color}` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ `{sonraki.color}`")
        if onceki.hoist != sonraki.hoist: degisiklikler.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ AyrÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ster: `{onceki.hoist}` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ `{sonraki.hoist}`")

        if not degisiklikler:
            return  # HiÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§bir deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklik yok

        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.role_update, hedef=sonraki)
        embed = discord.Embed(
            title=f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â­ Rol GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ncellendi ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â {sonraki.name}",
            color=sonraki.color.value or RENKLER["rol"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklikler",  value="\n".join(degisiklikler),                     inline=False)
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan",   value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "rol_log", embed)
        return

    # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ 2. Audit log'dan sorumluyu bul ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
    await asyncio.sleep(0.5)  # Audit log'un gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ncellenmesi iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in kÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sa bekleme
    sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.role_update, hedef=sonraki)

    # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ 3. ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zin deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ikliÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸i embedini oluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tur ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
    embed = discord.Embed(
        title=f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Rol ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zinleri DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ti ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â {sonraki.name}",
        description=(
            f"**{sonraki.mention}** rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼n izinleri gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ncellendi.\n"
            f"**{len(eklenenler)}** izin eklendi ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· **{len(kaldirlanlar)}** izin kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±."
        ),
        color=RENKLER["izin"],
        timestamp=datetime.now(timezone.utc)
    )

    # Eklenen izinler (yeÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸il ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦)
    if eklenenler:
        embed.add_field(
            name="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Eklenen ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zinler",
            value="\n".join(f"`+` {izin}" for izin in eklenenler),
            inline=True
        )

    # KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lan izinler (kÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rmÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±zÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢)
    if kaldirlanlar:
        embed.add_field(
            name="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lan ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zinler",
            value="\n".join(f"`-` {izin}" for izin in kaldirlanlar),
            inline=True
        )

    # ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ki sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼tun varsa hizalama iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in boÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ alan
    if eklenenler and kaldirlanlar:
        embed.add_field(name="\u200b", value="\u200b", inline=True)

    # Toplam izin sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶zeti
    eski_toplam = sum(1 for _, v in onceki.permissions if v)
    yeni_toplam = sum(1 for _, v in sonraki.permissions if v)
    fark = yeni_toplam - eski_toplam

    embed.add_field(
        name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zin ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“zeti",
        value=(
            f"ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“nceki: `{eski_toplam}` aktif\n"
            f"ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Âimdiki: `{yeni_toplam}` aktif\n"
            f"Fark: `{'+' if fark >= 0 else ''}{fark}`"
        ),
        inline=True
    )
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Yapan",  value=sorumlu.mention if sorumlu else "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Bilinmiyor", inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Rol ID", value=f"`{sonraki.id}`",                                inline=True)
    embed.set_footer(text=zaman_damgasi())

    await log_gonder(sonraki.guild, "rol_log", embed)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  OLAYLAR ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â MESAJ LOGLARI
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

@bot.event
async def on_message_delete(message: discord.Message):
    if message.author.bot:
        return

    embed = discord.Embed(
        title="Mesaj Silindi",
        description="Bir mesaj kanaldan kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
        color=RENKLER["mesaj"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Yazar", value=f"{message.author.mention} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `{message.author.id}`", inline=True)
    embed.add_field(name="Kanal", value=message.channel.mention, inline=True)
    embed.add_field(name="Mesaj ID", value=f"`{message.id}`", inline=True)
    embed.add_field(name="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§erik", value=message.content[:1024] or "*[BoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ mesaj veya sadece medya]*", inline=False)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(message.guild, "mesaj_log", embed)


@bot.event
async def on_message_edit(onceki: discord.Message, sonraki: discord.Message):
    if onceki.author.bot or onceki.content == sonraki.content:
        return

    embed = discord.Embed(
        title="Mesaj DÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼zenlendi",
        description=f"[Mesaja git]({sonraki.jump_url})",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Yazar", value=f"{sonraki.author.mention} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `{sonraki.author.id}`", inline=True)
    embed.add_field(name="Kanal", value=sonraki.channel.mention, inline=True)
    embed.add_field(name="Mesaj ID", value=f"`{sonraki.id}`", inline=True)
    embed.add_field(name="Eski Mesaj", value=onceki.content[:512] or "ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â", inline=False)
    embed.add_field(name="Yeni Mesaj", value=sonraki.content[:512] or "ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â", inline=False)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(sonraki.guild, "mesaj_log", embed)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  OLAYLAR ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â SES KANALI LOGLARI
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

@bot.event
async def on_voice_state_update(member: discord.Member, onceki: discord.VoiceState, sonraki: discord.VoiceState):
    if onceki.channel == sonraki.channel:
        return  # Mute/deafen gibi deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklikleri loglama

    anahtar = (member.guild.id, member.id)
    simdi_ts = time.time()
    baslangic = _SES_OTURUMLARI.get(anahtar)
    if onceki.channel is not None and baslangic is not None:
        _profil_bekleyen_arttir(member.guild.id, member.id, ses_delta=max(0, int(simdi_ts - baslangic)))
        _SES_OTURUMLARI.pop(anahtar, None)
    if sonraki.channel is not None:
        _SES_OTURUMLARI[anahtar] = simdi_ts

    embed = discord.Embed(color=RENKLER["ses"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye", value=f"{member.mention} `{member}`", inline=False)

    if onceki.channel is None:
        embed.title = "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â  Ses KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na KatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±"
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Kanal", value=sonraki.channel.mention, inline=True)
    elif sonraki.channel is None:
        embed.title = "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ Ses KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan AyrÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±"
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Kanal", value=onceki.channel.mention, inline=True)
    else:
        embed.title = "ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Ses KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tirildi"
        embed.add_field(name="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“nceki", value=onceki.channel.mention, inline=True)
        embed.add_field(name="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Yeni",   value=sonraki.channel.mention, inline=True)

    embed.set_footer(text=zaman_damgasi())
    await log_gonder(member.guild, "ses_log", embed)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  OLAYLAR ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â TIMEOUT (ZAMAN ASIMI) LOGU
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

@bot.event
async def on_member_update(onceki: discord.Member, sonraki: discord.Member):
    """
    Bu event hem rol deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ikliklerini hem de timeout deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ikliklerini yakalar.
    ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°kisini birden burada handle ediyoruz.

    NOT: Rol deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ikliÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸i iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in yukarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±da ayrÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bir on_member_update var,
    ama discord.py'de aynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± event'i iki kez tanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mlayamazsÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z.
    Bu yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼zden rol + timeout kontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ tek fonksiyonda birleÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tirildi.
    EÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸er ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nceki on_member_update varsa onu SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°LÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°P bununla DEÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚ÂTÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°RÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°N.
    """

    # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Timeout (Zaman AÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±) KontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
    # timed_out_until: None ise timeout yok, datetime ise aktif timeout
    eski_timeout = onceki.timed_out_until
    yeni_timeout = sonraki.timed_out_until

    if eski_timeout != yeni_timeout:
        await asyncio.sleep(0.5)
        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.member_update, hedef=sonraki)

        if yeni_timeout is not None:
            # Timeout uygulandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±
            bitis = yeni_timeout.strftime("%d.%m.%Y %H:%M UTC")
            embed = discord.Embed(
                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ Zaman AÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± UygulandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± (Timeout)",
                color=RENKLER["mute"],
                timestamp=datetime.now(timezone.utc)
            )
            embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye",            value=f"{sonraki.mention} `{sonraki}`",                inline=True)
            embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan",   value=sorumlu.mention if sorumlu else "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Bilinmiyor", inline=True)
            embed.add_field(name="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â° BitiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ ZamanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",   value=f"`{bitis}`",                                    inline=False)
            embed.set_thumbnail(url=sonraki.display_avatar.url)
            embed.set_footer(text=zaman_damgasi())
            await log_gonder(sonraki.guild, "mute_log", embed)

        else:
            # Timeout kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± (erken veya sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re doldu)
            embed = discord.Embed(
                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â  Zaman AÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                color=RENKLER["unban"],
                timestamp=datetime.now(timezone.utc)
            )
            embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye",           value=f"{sonraki.mention} `{sonraki}`",                inline=True)
            embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan",  value=sorumlu.mention if sorumlu else "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Otomatik",  inline=True)
            embed.set_thumbnail(url=sonraki.display_avatar.url)
            embed.set_footer(text=zaman_damgasi())
            await log_gonder(sonraki.guild, "mute_log", embed)

    # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Rol DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ikliÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸i KontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
    eski_roller = set(onceki.roles)
    yeni_roller = set(sonraki.roles)

    eklenen_roller   = yeni_roller - eski_roller
    cikarilan_roller = eski_roller - yeni_roller

    if not eklenen_roller and not cikarilan_roller:
        return

    await asyncio.sleep(0.5)
    sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.member_role_update, hedef=sonraki)

    if eklenen_roller:
        embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¢ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“yeye Rol Eklendi", color=RENKLER["giris"], timestamp=datetime.now(timezone.utc))
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye",           value=f"{sonraki.mention} `{sonraki}`",                inline=True)
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan",  value=sorumlu.mention if sorumlu else "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Bilinmiyor", inline=True)
        embed.add_field(
            name=f"ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢ Eklenen Rol{'ler' if len(eklenen_roller) > 1 else ''}",
            value="\n".join(r.mention for r in eklenen_roller),
            inline=False
        )
        embed.set_thumbnail(url=sonraki.display_avatar.url)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "rol_log", embed)

    if cikarilan_roller:
        embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â´ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“yeden Rol ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±karÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", color=RENKLER["cikis"], timestamp=datetime.now(timezone.utc))
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye",           value=f"{sonraki.mention} `{sonraki}`",                inline=True)
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan",  value=sorumlu.mention if sorumlu else "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Bilinmiyor", inline=True)
        embed.add_field(
            name=f"ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±karÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lan Rol{'ler' if len(cikarilan_roller) > 1 else ''}",
            value="\n".join(r.mention for r in cikarilan_roller),
            inline=False
        )
        embed.set_thumbnail(url=sonraki.display_avatar.url)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "rol_log", embed)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  OLAYLAR ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â DAVETÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°YE LOGLARI
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

@bot.event
async def on_invite_create(invite: discord.Invite):
    """Yeni bir davet baÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸lantÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± oluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turulduÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸unda tetiklenir."""
    embed = discord.Embed(
        title="Yeni Davet OluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turuldu",
        description="Sunucuda yeni bir davet baÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸lantÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼retildi.",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="OluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turan", value=invite.inviter.mention if invite.inviter else "Bilinmiyor", inline=True)
    embed.add_field(name="Kanal", value=invite.channel.mention if invite.channel else "ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â", inline=True)
    embed.add_field(name="Davet Kodu", value=f"`{invite.code}`", inline=True)

    # KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m limiti: 0 = sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rsÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z
    kullanim = str(invite.max_uses) if invite.max_uses else "SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rsÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z"
    embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m Limiti", value=kullanim, inline=True)

    # SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re: 0 = hiÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ dolmaz
    if invite.max_age:
        sure = f"{invite.max_age // 3600} saat" if invite.max_age >= 3600 else f"{invite.max_age // 60} dakika"
    else:
        sure = "SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼resiz"
    embed.add_field(name="GeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§erlilik", value=sure, inline=True)
    embed.add_field(name="URL", value=f"discord.gg/{invite.code}", inline=True)

    embed.set_footer(text=zaman_damgasi())
    await log_gonder(invite.guild, "davet_log", embed)


@bot.event
async def on_invite_delete(invite: discord.Invite):
    """Bir davet baÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸lantÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± silindiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸inde tetiklenir."""
    embed = discord.Embed(
        title="Davet Silindi",
        description="Bir davet baÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸lantÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Davet Kodu", value=f"`{invite.code}`", inline=True)
    embed.add_field(name="Kanal", value=invite.channel.mention if invite.channel else "ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(invite.guild, "davet_log", embed)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  OLAYLAR ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â KANAL LOGLARI
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

@bot.event
async def on_guild_channel_create(kanal: discord.abc.GuildChannel):
    """Yeni bir kanal oluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turulduÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸unda tetiklenir."""
    sorumlu = await audit_log_bul(kanal.guild, discord.AuditLogAction.channel_create, hedef=kanal)

    # Kanal tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ belirle
    tur_simge = {
        discord.TextChannel:     "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¬ Metin KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        discord.VoiceChannel:    "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â  Ses KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        discord.CategoryChannel: "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Kategori",
        discord.ForumChannel:    "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Forum KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        discord.StageChannel:    "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Sahne KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
    }.get(type(kanal), "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ Kanal")

    embed = discord.Embed(
        title="Kanal OluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turuldu",
        description=f"Yeni bir kanal aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±: **{kanal.name}**",
        color=RENKLER["giris"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Kanal", value=kanal.mention if hasattr(kanal, "mention") else f"`{kanal.name}`", inline=True)
    embed.add_field(name="TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r", value=tur_simge, inline=True)
    embed.add_field(name="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.add_field(name="Kanal ID", value=f"`{kanal.id}`", inline=True)

    # Kategorisi varsa gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ster
    if hasattr(kanal, "category") and kanal.category:
        embed.add_field(name="Kategori", value=kanal.category.name, inline=True)

    embed.set_footer(text=zaman_damgasi())
    await log_gonder(kanal.guild, "kanal_log", embed)
    await _guvenlik_eylem_isle(kanal.guild, sorumlu, "kanal_acma", f"{kanal.name} ({kanal.id})", _guvenlik_ayar_al(kanal.guild.id).get("kanal_limit", 3))


@bot.event
async def on_guild_channel_delete(kanal: discord.abc.GuildChannel):
    """Bir kanal silindiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸inde tetiklenir."""
    sorumlu = await audit_log_bul(kanal.guild, discord.AuditLogAction.channel_delete, hedef=kanal)

    tur_simge = {
        discord.TextChannel:     "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¬ Metin KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        discord.VoiceChannel:    "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â  Ses KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        discord.CategoryChannel: "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Kategori",
        discord.ForumChannel:    "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Forum KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        discord.StageChannel:    "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Sahne KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
    }.get(type(kanal), "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ Kanal")

    embed = discord.Embed(
        title="Kanal Silindi",
        description=f"Bir kanal kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±: **{kanal.name}**",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Kanal", value=f"`{kanal.name}`", inline=True)
    embed.add_field(name="TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r", value=tur_simge, inline=True)
    embed.add_field(name="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
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
        title="Rol OluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turuldu",
        description=f"Yeni rol: {rol.mention}",
        color=RENKLER["giris"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Rol", value=rol.mention, inline=True)
    embed.add_field(name="ID", value=f"`{rol.id}`", inline=True)
    embed.add_field(name="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan", value=sorumlu.mention if sorumlu else "Bilinmiyor", inline=True)
    embed.add_field(name="Renk", value=str(rol.color), inline=True)
    embed.set_footer(text=zaman_damgasi())
    await log_gonder(rol.guild, "rol_log", embed)
    await _guvenlik_eylem_isle(rol.guild, sorumlu, "rol_acma", f"{rol.name} ({rol.id})", _guvenlik_ayar_al(rol.guild.id).get("rol_ac_limit", 3))


@bot.event
async def on_guild_role_delete(rol: discord.Role):
    sorumlu = await audit_log_bul(rol.guild, discord.AuditLogAction.role_delete, hedef=rol)

    embed = discord.Embed(
        title="Rol Silindi",
        description=f"KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lan rol: **{rol.name}**",
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
    ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ki kanal arasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndaki izin (overwrite) farklarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bulur.

    Kanal izinleri rol/ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye bazlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± OverwriteType nesneleridir.
    Her overwrite'ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n allow ve deny listeleri karÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±laÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r:
        - Yeni eklenmiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ overwrite  ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ o rol/ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in yeni izin ayarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± yapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lmÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸
        - SilinmiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ overwrite       ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ o rol/ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in izin ayarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lmÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸
        - DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸miÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ overwrite       ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ allow/deny deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸erleri farklÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±laÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸

    DÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r:
        list[str] ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â okunabilir deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklik satÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±
    """
    satirlar = []

    eski_ow = dict(onceki.overwrites)   # {rol/ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye: PermissionOverwrite}
    yeni_ow = dict(sonraki.overwrites)

    tum_hedefler = set(eski_ow) | set(yeni_ow)

    for hedef in tum_hedefler:
        eski = eski_ow.get(hedef)
        yeni = yeni_ow.get(hedef)

        hedef_adi = f"@{hedef.name}" if hasattr(hedef, 'name') else str(hedef)

        if eski is None and yeni is not None:
            # Yeni overwrite eklendi
            izinler = [izin_adi_getir(p) for p, v in iter(yeni) if v is not None]
            satirlar.append(f"ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢ **{hedef_adi}** iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in izin ayarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± eklendi")

        elif eski is not None and yeni is None:
            # Overwrite tamamen silindi
            satirlar.append(f"ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ **{hedef_adi}** iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in izin ayarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±")

        else:
            # Her iki tarafta da var, farklarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bul
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
                    eklenen_izinler.append(ad)       # ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zin verildi
                elif yeni_deger is False and eski_deger is not False:
                    reddedilen_izinler.append(ad)    # ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zin reddedildi
                elif yeni_deger is None:
                    if eski_deger is True:
                        kaldirilan_izinler.append(ad)   # ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶tr
                    elif eski_deger is False:
                        red_kaldirilan.append(ad)       # ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶tr

            if any([eklenen_izinler, kaldirilan_izinler, reddedilen_izinler, red_kaldirilan]):
                satirlar.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â§ **{hedef_adi}** izinleri deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ti:")
                if eklenen_izinler:
                    satirlar.append("  `ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦` " + ", ".join(eklenen_izinler))
                if reddedilen_izinler:
                    satirlar.append("  `ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢` " + ", ".join(reddedilen_izinler))
                if kaldirilan_izinler:
                    satirlar.append("  `ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Ãƒâ€šÃ‚Â©ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â` NÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶tre alÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±: " + ", ".join(kaldirilan_izinler))
                if red_kaldirilan:
                    satirlar.append("  `ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Ãƒâ€šÃ‚Â©ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â` Red kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±: " + ", ".join(red_kaldirilan))

    return satirlar


@bot.event
async def on_guild_channel_update(onceki: discord.abc.GuildChannel, sonraki: discord.abc.GuildChannel):
    """
    Bir kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n adÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±, ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± veya izinleri deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸inde tetiklenir.
    Genel deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklikler ve izin (overwrite) deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklikleri ayrÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± embedler olarak gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderilir.
    """

    # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ 1. Genel ayar deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklikleri ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
    degisiklikler = []

    if onceki.name != sonraki.name:
        degisiklikler.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°sim: `{onceki.name}` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ `{sonraki.name}`")

    if isinstance(onceki, discord.TextChannel) and isinstance(sonraki, discord.TextChannel):
        if onceki.topic != sonraki.topic:
            eski = onceki.topic or "*(boÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸)*"
            yeni = sonraki.topic or "*(boÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸)*"
            degisiklikler.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Konu: `{eski}` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ `{yeni}`")
        if onceki.slowmode_delay != sonraki.slowmode_delay:
            degisiklikler.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¢ YavaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ Mod: `{onceki.slowmode_delay}sn` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ `{sonraki.slowmode_delay}sn`")
        if onceki.nsfw != sonraki.nsfw:
            degisiklikler.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â NSFW: `{onceki.nsfw}` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ `{sonraki.nsfw}`")

    if degisiklikler:
        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.channel_update, hedef=sonraki)
        embed = discord.Embed(
            title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Kanal GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ncellendi",
            color=RENKLER["bilgi"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Kanal",         value=sonraki.mention,                                        inline=True)
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan",  value=sorumlu.mention if sorumlu else "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Bilinmiyor",        inline=True)
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklikler", value="\n".join(degisiklikler),                                inline=False)
        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "kanal_log", embed)

    # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ 2. ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zin (overwrite) deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklikleri ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
    izin_satirlari = kanal_izin_farklarini_bul(onceki, sonraki)

    if izin_satirlari:
        sorumlu = await audit_log_bul(sonraki.guild, discord.AuditLogAction.overwrite_update, hedef=sonraki)

        # Discord embed field deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸eri max 1024 karakter, uzunsa bÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶l
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
            title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Kanal ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°zinleri DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ti",
            color=RENKLER["izin"],
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Kanal",        value=sonraki.mention,                                        inline=True)
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemi Yapan", value=sorumlu.mention if sorumlu else "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Bilinmiyor",        inline=True)

        for i, parca in enumerate(parcalar):
            embed.add_field(
                name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â DeÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iklikler" if i == 0 else "\u200b",
                value=parca,
                inline=False
            )

        embed.set_footer(text=zaman_damgasi())
        await log_gonder(sonraki.guild, "kanal_log", embed)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  BOT HAZIR OLAYI
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬


@bot.event
async def on_command_error(ctx, error):
    """CommandNotFound ve diÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸er bilinen hatalarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± sessizce geÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§er."""
    if isinstance(error, commands.CommandNotFound):
        return  # Bilinmeyen komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± yoksay
    if isinstance(error, PrefixMesajCiftKopya):
        return  # ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ift bot sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼reci: ikinci kopya sessizce yoksayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=hata_embedi("Yetki HatasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", "Bu komutu kullanmak iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in gerekli yetkiye sahip deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilsin."))
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye BulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", "BelirttiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸in ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± veya sunucuda deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸il."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("Eksik parametre girdin. DetaylÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± komut listesi iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in `.yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m` kullanabilirsin."))


@bot.event
async def on_ready():
    # Slash komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Discord'a senkronize et
    try:
        synced = await bot.tree.sync()
        print(f"  ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ {len(synced)} slash komutu senkronize edildi.")
    except Exception as e:
        print(f"  ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Komut senkronizasyonu baÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸arÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z: {e}")

    # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Sabit log kanallarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± settings.json'a yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼kle ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
    # Her bot baÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ladÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nda DEFAULT_LOG_KANALLARI settings.json'a yazÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r.
    # BÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ylece deploy sonrasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± settings.json silinse bile kanallar kaybolmaz.
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
    print("  ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Kanallar yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼klendi.")

    print("ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â" * 52)
    print(f"  Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ Bot    : {bot.user} ({bot.user.id})")
    print(f"  Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¥ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â  Surec  : {' | '.join(_bot_surec_log_satirlari())}")
    print(f"  Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¡ Sunucu : {len(bot.guilds)} adet")
    print(f"  ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â  Ayarlar: Supabase={'acik' if supabase_aktif_mi() else 'kapali'} | DosyaFallback={AYAR_DOSYASI}")
    print("ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â" * 52)
    print("  KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±labilir slash komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±:")
    print("    /log-kur <tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r> <kanal>  ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Kanal ata")
    print("    /log-kaldir <tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r>       ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Logu kapat")
    print("    /log-durum              ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Durumu gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶r")
    print("    /log-sifirla            ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ sil")
    print("ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â" * 52)

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="sunucu loglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â"
        )
    )

    if not getattr(bot, "_coklu_surec_izleme_baslatildi", False):
        bot._coklu_surec_izleme_baslatildi = True
        asyncio.create_task(_bot_coklu_surec_izleme_dongusu())
    if not getattr(bot, "_profil_kaydetme_dongusu_baslatildi", False):
        bot._profil_kaydetme_dongusu_baslatildi = True
        asyncio.create_task(_profil_bekleyenleri_kaydet_dongusu())


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â
#  PARTNER SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°STEMÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â
#
#  Veri yapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± (settings.json iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§inde):
#  {
#    "guild_id": {
#      "partner_log": kanal_id,          ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Ãƒâ€šÃ‚Â partner log kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±
#      "partners": {
#        "hedef_guild_id": {
#          "guild_name": "Sunucu AdÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
#          "guild_id": 123,
#          "yapan": "kullanici#0000",
#          "yapan_id": 123,
#          "zaman": "2026-03-20T16:00:00",  ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Ãƒâ€šÃ‚Â ISO format
#          "son_partner": "2026-03-20T16:00:00"
#        }
#      }
#    }
#  }
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

PARTNER_BEKLEME_SURESI = 3600  # saniye (1 saat)


def partner_verisi_al(guild_id: int) -> dict:
    """Bu sunucunun partner verisini dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r."""
    ayarlar = ayarlari_yukle()
    return ayarlar.get(str(guild_id), {}).get("partners", {})


def partner_gecmisi_al(guild_id: int) -> list[dict]:
    """Bu sunucunun partner iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lem geÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§miÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ini dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r."""
    ayarlar = ayarlari_yukle()
    gecmis = ayarlar.get(str(guild_id), {}).get("partner_gecmisi", [])
    return gecmis if isinstance(gecmis, list) else []


def partner_kaydet_db(guild_id: int, hedef_guild_id: int, veri: dict):
    """Bir partner kaydÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± settings.json'a yazar."""
    def _guncelle(ayarlar):
        guild_key = str(guild_id)
        if guild_key not in ayarlar:
            ayarlar[guild_key] = {}
        if "partners" not in ayarlar[guild_key]:
            ayarlar[guild_key]["partners"] = {}
        ayarlar[guild_key]["partners"][str(hedef_guild_id)] = veri

    ayarlari_guncelle(_guncelle)


def partner_gecmisi_ekle(guild_id: int, veri: dict):
    """Partner iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lemini geÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§miÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ listesine ekler."""
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
    """Partner log kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kaydeder."""
    def _guncelle(ayarlar):
        guild_key = str(guild_id)
        if guild_key not in ayarlar:
            ayarlar[guild_key] = {}
        ayarlar[guild_key]["partner_log"] = kanal_id

    ayarlari_guncelle(_guncelle)


def partner_log_kanali_al(guild_id: int):
    """Partner log kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ID'sini dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r. Settings yoksa sabit deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸eri kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r."""
    kayitli = ayarlari_yukle().get(str(guild_id), {}).get("partner_log")
    return kayitli if kayitli else DEFAULT_PARTNER_LOG_KANALI


def partner_istatistik_hesapla(guild_id: int) -> dict:
    """
    GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nlÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼k, haftalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k, aylÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k ve toplam partner sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± hesaplar.

    MantÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k:
        - Her partner kaydÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndaki 'zaman' alanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ISO format datetime'dÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r.
        - ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Âu anki zamandan farkÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± hesaplayarak hangi periyoda girdiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ini belirleriz.
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
    Bu sunucunun toplam partner sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶re sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ralamasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r.
    TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m sunucularÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n toplam partner sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±larÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± karÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±laÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r.
    """
    ayarlar = ayarlari_yukle()
    sayilar = []

    for gid, veri in ayarlar.items():
        if "partners" in veri:
            sayilar.append((gid, len(veri["partners"])))

    # BÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼kten kÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸e sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rala
    sayilar.sort(key=lambda x: x[1], reverse=True)

    for i, (gid, _) in enumerate(sayilar, 1):
        if gid == str(guild_id):
            return i
    return 1




# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Partner Slash KomutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± & Mesaj KontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

def partner_kanal_id_al(guild_id: int):
    """Partner text kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ID'sini dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r. Settings yoksa sabit deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸eri kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r."""
    kayitli = ayarlari_yukle().get(str(guild_id), {}).get("partner_kanal")
    return kayitli if kayitli else DEFAULT_PARTNER_TEXT_KANALI

def partner_log_kanali_al_v2(guild_id: int):
    """Partner log kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ID'sini dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r. Settings yoksa sabit deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸eri kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r."""
    kayitli = ayarlari_yukle().get(str(guild_id), {}).get("partner_log")
    return kayitli if kayitli else DEFAULT_PARTNER_LOG_KANALI

def partner_kanal_id_kaydet(guild_id: int, kanal_id: int):
    """Partner text kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kaydeder."""
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        ayarlar[gk]["partner_kanal"] = kanal_id

    ayarlari_guncelle(_guncelle)

def yetkili_partner_sayisi_guncelle(guild_id: int, yetkili_id: int, yetkili_adi: str):
    """
    Yetkili bazlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± partner sayacÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nceller.
    Her partnerlik yapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nda ilgili yetkilinin sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± 1 artÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r.
    YapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±: ayarlar[guild_id]["yetkili_partnerleri"][yetkili_id] = {"ad": ..., "sayi": ...}
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
    Yetkilileri partner sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶re bÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼kten kÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸e sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ralar.
    DÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r: [{"id": ..., "ad": ..., "sayi": ...}, ...]
    """
    ayarlar = ayarlari_yukle()
    veri = ayarlar.get(str(guild_id), {}).get("yetkili_partnerleri", {})
    liste = [{"id": kid, "ad": v["ad"], "sayi": v["sayi"]} for kid, v in veri.items()]
    liste.sort(key=lambda x: x["sayi"], reverse=True)
    return liste


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Partner Prefix KomutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

@bot.command(name="partner-kur")
@commands.has_permissions(manage_guild=True)
async def partner_kur(ctx, text_kanal: discord.TextChannel = None, log_kanal: discord.TextChannel = None):
    """
    .partner-kur #text-kanal #log-kanal
    Partner text ve log kanallarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ayarlar.
    """
    if not text_kanal or not log_kanal:
        await ctx.send(embed=kullanim_embedi("`.partner-kur #text-kanal #log-kanal`"))
        return

    partner_kanal_id_kaydet(ctx.guild.id, text_kanal.id)
    partner_log_kanali_kaydet(ctx.guild.id, log_kanal.id)

    embed = discord.Embed(title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Partner KanallarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± AyarlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¢ Partner Text", value=text_kanal.mention, inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Partner Log",  value=log_kanal.mention,  inline=True)
    embed.set_footer(text=f"Ayarlayan: {ctx.author}")
    await ctx.send(embed=embed)
    await text_kanal.send(embed=discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤Ãƒâ€šÃ‚Â Partner KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Aktif",
        description="Bu kanal partner text kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± olarak ayarlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.\nDavet linki iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ermeyen mesajlar otomatik silinecek.",
        color=RENKLER["basari"]
    ))
    await log_kanal.send(embed=discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Partner Log KanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Aktif",
        description="Partner loglarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bu kanala gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderilecek.",
        color=RENKLER["basari"]
    ))


@bot.command(name="partner-kapat", aliases=["partner-off", "partnerkapat"])
@commands.has_permissions(manage_guild=True)
async def partner_kapat(ctx):
    """.partner-kapat ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Partner sisteminin kanal ayarlarini kapatir."""
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
    """.partner-istatistik ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Sunucunun partner istatistiklerini gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶sterir."""
    stats = partner_istatistik_hesapla(ctx.guild.id)
    sira  = partner_sira_bul(ctx.guild.id)

    embed = discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Partner ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°statistikleri",
        description=f"**{ctx.guild.name}** sunucusunun partner verileri",
        color=0x57F287,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ralaman", value=f"**#{sira}**", inline=False)
    embed.add_field(
        name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â Zamana DayalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±:",
        value=(
            f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Âº GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nlÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼k: **{stats['gunluk']}**\n"
            f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Âº HaftalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k: **{stats['haftalik']}**\n"
            f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Âº AylÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k: **{stats['aylik']}**"
        ),
        inline=True
    )
    embed.add_field(name="ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Toplam", value=f"**{stats['toplam']}**", inline=True)
    embed.set_footer(text=f"{ctx.bot.user.name} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Partner Sistemi ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")
    await ctx.send(embed=embed)


@bot.command(name="partner-top", aliases=["p-top", "ptop"])
@commands.has_permissions(manage_guild=True)
async def partner_top(ctx):
    """.partner-top ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Yetkililerin partner sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ralamasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶sterir."""
    siralama = yetkili_siralamasi_al(ctx.guild.id)

    if not siralama:
        await ctx.send(embed=discord.Embed(
            title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Partner SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ralamasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
            description="HenÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼z hiÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ partnerlik kaydÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± yok.",
            color=RENKLER["bilgi"]
        ))
        return

    madalyalar = ["Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¥ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡", "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¥Ãƒâ€¹Ã¢â‚¬Â ", "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¥ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°"]
    satirlar = []
    for i, yetkili in enumerate(siralama[:20], 1):
        madalya = madalyalar[i-1] if i <= 3 else f"`{i}.`"
        satirlar.append(f"{madalya} <@{yetkili['id']}> ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â **{yetkili['sayi']}** partnerlik")

    embed = discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â  Partner SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ralamasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        description="\n".join(satirlar),
        color=0xF1C40F,
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=f"Toplam {len(siralama)} yetkili â€¢ {zaman_damgasi()}")
    await ctx.send(embed=embed)


@bot.command(name="partner-liste", aliases=["p-liste", "pliste"])
@commands.has_permissions(manage_guild=True)
async def partner_liste(ctx):
    """.partner-liste ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m partner sunucularÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± listeler."""
    partners = partner_verisi_al(ctx.guild.id)
    if not partners:
        await ctx.send(embed=discord.Embed(
            title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Partner Listesi",
            description="HenÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼z hiÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ partner kaydÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± yok.",
            color=RENKLER["bilgi"]
        ))
        return

    satirlar = []
    for i, (gid, p) in enumerate(partners.items(), 1):
        try:
            zaman = datetime.fromisoformat(p["zaman"]).strftime("%d.%m.%Y")
        except Exception:
            zaman = "ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â"
        satirlar.append(f"`{i}.` **{p['guild_name']}** ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â {zaman} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â <@{p['yapan_id']}>")

    # Sayfalama ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â her sayfada 10 partner
    sayfalar = [satirlar[i:i+10] for i in range(0, len(satirlar), 10)]

    class SayfaView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=60)
            self.sayfa = 0

        def embed_olustur(self):
            e = discord.Embed(
                title=f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Partner Listesi ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Toplam {len(partners)}",
                description="\n".join(sayfalar[self.sayfa]),
                color=0x57F287,
                timestamp=datetime.now(timezone.utc)
            )
            e.set_footer(text=f"Sayfa {self.sayfa+1}/{len(sayfalar)} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")
            return e

        @discord.ui.button(label="ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬", style=discord.ButtonStyle.secondary)
        async def geri(self, interaction: discord.Interaction, button: discord.ui.Button):
            if self.sayfa > 0:
                self.sayfa -= 1
            await interaction.response.edit_message(embed=self.embed_olustur(), view=self)

        @discord.ui.button(label="ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¶", style=discord.ButtonStyle.secondary)
        async def ileri(self, interaction: discord.Interaction, button: discord.ui.Button):
            if self.sayfa < len(sayfalar) - 1:
                self.sayfa += 1
            await interaction.response.edit_message(embed=self.embed_olustur(), view=self)

    view = SayfaView()
    await ctx.send(embed=view.embed_olustur(), view=view if len(sayfalar) > 1 else None)


@bot.command(name="partner-sifirla", aliases=["p-sifirla"])
@commands.has_permissions(administrator=True)
async def partner_sifirla(ctx):
    """.partner-sifirla ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m partner kayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±tlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± siler (onay butonu ile)."""

    class OnayView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=30)

        @discord.ui.button(label="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Evet, SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±fÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rla", style=discord.ButtonStyle.danger)
        async def onayla(self, interaction: discord.Interaction, button: discord.ui.Button):
            ayarlar = ayarlari_yukle()
            gk = str(interaction.guild_id)
            if gk in ayarlar:
                ayarlar[gk].pop("partners", None)
                ayarlar[gk].pop("partner_gecmisi", None)
                ayarlar[gk].pop("yetkili_partnerleri", None)
                ayarlari_kaydet(ayarlar)
            await interaction.response.edit_message(embed=discord.Embed(
                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Partner KayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±tlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Silindi",
                description="TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m partner kayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±tlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ve yetkili sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ralamasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± silindi.",
                color=RENKLER["hata"]
            ), view=None)

        @discord.ui.button(label="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ptal", style=discord.ButtonStyle.secondary)
        async def iptal(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.edit_message(embed=discord.Embed(
                title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ptal Edildi",
                description="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lem iptal edildi, kayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±tlar korundu.",
                color=RENKLER["basari"]
            ), view=None)

    await ctx.send(embed=discord.Embed(
        title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Emin misiniz?",
        description="TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m partner kayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±tlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ve yetkili sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ralamasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± **kalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± olarak** silinecek!",
        color=RENKLER["hata"]
    ), view=OnayView())





# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â
#  MODERASYON KOMUTLARI (Prefix: !)
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â

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
    """Standart moderasyon embed'i oluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turur."""
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


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ !ban ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    """.ban @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sebep]"""
    uye = await hedef_uye_bul(ctx, uye)
    if uye is None:
        await ctx.send(embed=kullanim_embedi("`.ban @uye [sebep]` veya bir mesaja yanit verip `.ban [sebep]`"))
        return
    if uye == ctx.author:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Kendinizi banlayamazsÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z."); return
    if uye.top_role >= ctx.author.top_role:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Bu ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yeyi banlayacak yetkiniz yok."); return

    await uye.ban(reason=f"{ctx.author} tarafÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan: {sebep}", delete_message_seconds=0)

    embed = mod_embed("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye BanlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", RENKLER["ban"],
        **{"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye": f"{uye.mention} `{uye}`",
           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Sebep": sebep,
           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "ban_log", embed)

    try:
        await uye.send(embed=discord.Embed(
            title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨ Sunucudan BanlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z",
            description=f"**{ctx.guild.name}** sunucusundan banlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z.\n**Sebep:** {sebep}",
            color=RENKLER["ban"]
        ))
    except discord.Forbidden:
        pass


@ban.error
async def ban_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Ban yetkine sahip deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye BulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", "BelirttiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸in ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± veya sunucuda deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸il."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("`.ban @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sebep]`"))


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ !unban ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
@bot.command(name="unban")
@commands.has_permissions(ban_members=True)
async def unban(ctx, kullanici_id: int, *, sebep: str = "Sebep belirtilmedi"):
    """.unban <kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±_id> [sebep]"""
    try:
        kullanici = await bot.fetch_user(kullanici_id)
        await ctx.guild.unban(kullanici, reason=f"{ctx.author} tarafÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan: {sebep}")

        embed = mod_embed("ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Ban KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", RENKLER["unban"],
            **{"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±": f"`{kullanici}`",
               "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Sebep": sebep,
               "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Yetkili": ctx.author.mention})
        await ctx.send(embed=embed)
        await log_gonder(ctx.guild, "ban_log", embed)

    except discord.NotFound:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Bu ID'ye sahip banlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bir kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.")


@unban.error
async def unban_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Ban yetkine sahip deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilsin.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: ``.unban <kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±_id> [sebep]`")


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ !kick ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    uye = await hedef_uye_bul(ctx, uye)
    if uye is None:
        await ctx.send(embed=kullanim_embedi("`.kick @uye [sebep]` veya bir mesaja yanit verip `.kick [sebep]`"))
        return
    """.kick @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sebep]"""
    if uye == ctx.author:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Kendinizi atamazsÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z."); return
    if uye.top_role >= ctx.author.top_role:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Bu ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yeyi atacak yetkiniz yok."); return

    await uye.kick(reason=f"{ctx.author} tarafÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan: {sebep}")

    embed = mod_embed("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¢ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye AtÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", RENKLER["mute"],
        **{"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye": f"{uye.mention} `{uye}`",
           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Sebep": sebep,
           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mod_log", embed)

    try:
        await uye.send(embed=discord.Embed(
            title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¢ Sunucudan AtÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z",
            description=f"**{ctx.guild.name}** sunucusundan atÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z.\n**Sebep:** {sebep}",
            color=RENKLER["mute"]
        ))
    except discord.Forbidden:
        pass


@kick.error
async def kick_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Kick yetkine sahip deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye BulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", "BelirttiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸in ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± veya sunucuda deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸il."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("`.kick @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sebep]`"))


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ .mute (timeout) ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
@bot.command(name="mute")
@commands.has_permissions(moderate_members=True)
async def mute(ctx, uye: discord.Member, *, arguman: str = ""):
    """
    .mute @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re] [sebep]
    TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m argÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼manlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± tek string olarak alÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r, sonra parse eder.
    BÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶ylece .mute @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye, .mute @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye sebep, .mute @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye 10m sebep hepsi ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§alÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r.
    """
    if uye == ctx.author:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Kendinizi susturamassÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z."); return
    if uye.top_role >= ctx.author.top_role:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Bu ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yeyi susturacak yetkiniz yok."); return

    birimler = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    parcalar = arguman.strip().split()

    # ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°lk kelime sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re formatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nda mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±? (ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶rn: 10m, 2h, 1d, 30s)
    if parcalar and parcalar[0][-1] in birimler and parcalar[0][:-1].isdigit():
        sure_str = parcalar[0]
        saniye = int(sure_str[:-1]) * birimler[sure_str[-1]]
        sebep = " ".join(parcalar[1:]) if len(parcalar) > 1 else "Sebep belirtilmedi"
        sure_goster = sure_str
        if saniye > 2419200:
            await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Maksimum sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re 28 gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ndÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r."); return
    else:
        # SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re yok ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m argÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼man sebep, sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼resiz mute
        saniye = 2419200
        sure_goster = "SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼resiz"
        sebep = arguman.strip() if arguman.strip() else "Sebep belirtilmedi"

    bitis = datetime.now(timezone.utc) + timedelta(seconds=saniye)
    await uye.timeout(timedelta(seconds=saniye), reason=f"{ctx.author}: {sebep}")

    embed = mod_embed("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye Susturuldu", RENKLER["mute"],
        **{"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye": f"{uye.mention} `{uye}`",
           "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re": sure_goster,
           "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â° BitiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸": bitis.strftime("%d.%m.%Y %H:%M UTC"),
           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Sebep": sebep,
           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mute_log", embed)


@mute.error
async def mute_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Timeout yetkine sahip deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=hata_embedi("ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye BulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", "BelirttiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸in ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± veya sunucuda deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸il."))
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=kullanim_embedi("`.mute @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re] [sebep]`"))


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ !unmute ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
@bot.command(name="unmute")
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, uye: discord.Member, *, sebep: str = "Sebep belirtilmedi"):
    """.unmute @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sebep]"""
    await uye.timeout(None, reason=f"{ctx.author}: {sebep}")

    embed = mod_embed("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â  Timeout KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", RENKLER["unban"],
        **{"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye": f"{uye.mention} `{uye}`",
           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Sebep": sebep,
           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mute_log", embed)


@unmute.error
async def unmute_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Timeout kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rma yetkine sahip deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.")


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ !sil ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
@bot.command(name="sil")
@commands.has_permissions(manage_messages=True)
async def sil(ctx, adet: int = 5):
    """.sil [adet] ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Belirtilen sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±da mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± siler (max 100)"""
    if adet < 1 or adet > 100:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ 1 ile 100 arasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nda bir sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± girin."); return

    await ctx.message.delete()
    silinen = await ctx.channel.purge(limit=adet)

    bilgi = await ctx.send(embed=discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Mesajlar Silindi",
        description=f"**{len(silinen)}** mesaj silindi.",
        color=RENKLER["mesaj"]
    ))
    await asyncio.sleep(3)
    await bilgi.delete()


@sil.error
async def sil_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Mesaj silme yetkine sahip deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilsin.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: ``.sil [adet]`")


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ !warn ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
@bot.command(name="warn")
@commands.has_permissions(manage_messages=True)
async def warn(ctx, uye: discord.Member = None, *, sebep: str = "Sebep belirtilmedi"):
    uye = await hedef_uye_bul(ctx, uye)
    if uye is None:
        await ctx.send("Kullanim: `.warn @uye [sebep]` veya bir mesaja yanit verip `.warn [sebep]`")
        return
    """.warn @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sebep] ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“yeye uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± verir ve settings.json'a kaydeder."""
    # UyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±yÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kaydet
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

    embed = mod_embed(f"ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â UyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Verildi ({toplam}. uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±)", RENKLER["mesaj"],
        **{"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye": f"{uye.mention} `{uye}`",
           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Sebep": sebep,
           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¢ Toplam UyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±": str(toplam),
           "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Yetkili": ctx.author.mention})
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "mod_log", embed)

    try:
        await uye.send(embed=discord.Embed(
            title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â UyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± AldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z",
            description=f"**{ctx.guild.name}** sunucusunda uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z.\n**Sebep:** {sebep}\n**Toplam uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±:** {toplam}",
            color=RENKLER["mesaj"]
        ))
    except discord.Forbidden:
        pass


@warn.error
async def warn_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ UyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± verme yetkine sahip deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilsin.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: ``.warn @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sebep]`")


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ !uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lar ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
@bot.command(name="uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lar", aliases=["warnings", "uyarilar"])
@commands.has_permissions(manage_messages=True)
async def uyarilar(ctx, uye: discord.Member):
    """.uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lar @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“yenin uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± geÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§miÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ini gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶sterir."""
    ayarlar = ayarlari_yukle()
    liste = ayarlar.get(str(ctx.guild.id), {}).get("uyarilar", {}).get(str(uye.id), [])

    if not liste:
        await ctx.send(embed=discord.Embed(
            title=f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ {uye.display_name} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â UyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Yok",
            description="Bu ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yenin hiÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bulunmuyor.",
            color=RENKLER["bilgi"]
        ))
        return

    embed = discord.Embed(
        title=f"ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â {uye.display_name} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â {len(liste)} UyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        color=RENKLER["mesaj"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_thumbnail(url=uye.display_avatar.url)

    for i, u in enumerate(liste[-10:], 1):  # Son 10 uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±
        try:
            zaman = datetime.fromisoformat(u["zaman"]).strftime("%d.%m.%Y %H:%M")
        except Exception:
            zaman = "ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â"
        embed.add_field(
            name=f"#{i} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â {zaman}",
            value=f"**Sebep:** {u['sebep']}\n**Yetkili:** {u['yetkili']}",
            inline=False
        )

    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


@uyarilar.error
async def uyarilar_hata(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: ``.uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lar @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye`")


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ !uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sil ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
@bot.command(name="uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sil", aliases=["uyarisil", "clearwarns"])
@commands.has_permissions(manage_guild=True)
async def uyari_sil(ctx, uye: discord.Member):
    """.uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sil @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“yenin tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±larÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± siler."""
    ayarlar = ayarlari_yukle()
    guild_key = str(ctx.guild.id)
    uye_key = str(uye.id)

    if guild_key in ayarlar and "uyarilar" in ayarlar[guild_key] and uye_key in ayarlar[guild_key]["uyarilar"]:
        del ayarlar[guild_key]["uyarilar"][uye_key]
        ayarlari_kaydet(ayarlar)
        await ctx.send(embed=discord.Embed(
            title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ UyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lar Silindi",
            description=f"{uye.mention} adlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yenin tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±larÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± silindi.",
            color=RENKLER["basari"]
        ))
    else:
        await ctx.send(f"ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ {uye.mention} adlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yenin zaten uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± yok.")


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ !yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
async def gelismis_yardim(ctx):
    def ana_embed():
        e = discord.Embed(title="Komut Rehberi", description="Bir kategori sec.", color=0x5865F2, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Kategoriler", value="Moderasyon\nPartner\nEglence\nAraclar", inline=False)
        e.set_footer(text=f"{ctx.guild.name} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")
        if ctx.guild.icon:
            e.set_thumbnail(url=ctx.guild.icon.url)
        return e

    def mod_kategori():
        e = discord.Embed(title="Moderasyon", color=0xE74C3C, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Uye", value="`.ban @uye [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Banlar\n`.unban <id> [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Ban kaldirir\n`.kick @uye [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Atar\n`.mute @uye [sure] [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Susturur\n`.unmute @uye` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Kaldirir", inline=False)
        e.add_field(name="Kanal & Mesaj", value="`.sil [adet]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Mesaj siler (max 100)\n`.slowmode [sn]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Yavas mod\n`.duyuru #kanal mesaj` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Duyuru gonderir", inline=False)
        e.add_field(name="Uyari", value="`.warn @uye [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Verir\n`.uyarilar @uye` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Gosterir\n`.uyarisil @uye` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Temizler\nMesaja yanit verip `.ban/.kick/.warn` kullanabilirsin.", inline=False)
        return e

    def partner_kategori():
        e = discord.Embed(title="Partner Sistemi", color=0x57F287, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Komutlar", value="`.partner-kur #text #log` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Kanallari ayarlar\n`.partner-istatistik` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Istatistikler\n`.partner-top` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Siralama\n`.partner-liste` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Sunucu listesi\n`.partner-sifirla` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Sifirlar", inline=False)
        e.add_field(name="Nasil calisir?", value="Yetkili kanala partner textini atar\nBot davet linkini kontrol eder\nLink yoksa siler, varsa kaydeder\nAyni sunucu ile 1 saat bekleme var", inline=False)
        return e

    def eglence_kategori():
        e = discord.Embed(title="Eglence & Bilgi", color=0xF1C40F, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Cekilis", value="`.cekilisbaslat [sure] [kisi] [odul]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Baslatir\n`.cekilisbitir <id>` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Erken bitirir\n`.cekilisyenile <id> [kisi]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Yeni kazanan\n`.cekiliskatilimci <id>` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Katilimcilari listeler\n`.cekilisbilgi <id>` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Bilgi gosterir\n`.cekilissil <id>` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Iptal eder", inline=False)
        e.add_field(name="AFK", value="`.afk [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â AFK moduna girer\nÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Mesaj atinca otomatik cikar\nÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Etiketlenince AFK bildirilir", inline=False)
        e.add_field(name="Bilgi", value="`.sunucu` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Sunucu istatistikleri", inline=False)
        return e

    def araclar_kategori():
        e = discord.Embed(title="Araclar & Sistemler", color=0x9B59B6, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Ticket - Yonetim", value="`.ticketkur [kategori] #log @rol` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Kurar\n`.ticketpanel` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Panel gonderir\n`.ticketkapat` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Ticketi kapatir\n`.ticketekle @uye` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Uye ekler\n`.ticketcikar @uye` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Uye cikarir", inline=False)
        e.add_field(name="Ticket - Ozellikler", value="`.ticketkonu [konu]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Konu ayarlar\n`.ticketlist` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Acik ticketlari listeler\n`.ticketsayi` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Toplam ticket sayisi\n`.ticketoncelik [dusuk/orta/yuksek]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Oncelik belirler\n`.ticketsahip @uye` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Sahibi degistirir\n`.ticketyeniden @uye` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Yeniden acar", inline=False)
        e.add_field(name="Anti-Link", value="`.antilink` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Durum gosterir\n`.antilink ac` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Acar\n`.antilink kapat` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Kapatir\n`.antilink muaf @rol/#kanal` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Muafiyet ekler/kaldirir", inline=False)
        e.add_field(name="Renk Sistemi", value="`.renkekle @rol` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Menuye rol ekler\n`.renkcikar @rol` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Menuden rol cikarir\n`.renklist` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Listedeki rolleri gosterir\n`.renkpanel` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Secim paneli gonderir", inline=False)
        e.add_field(name="Log Sistemi", value="`.logkur` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Otomatik kanal tarar\n`.logkurkanal` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Eksik log kanallarini olusturur\n`/log-kur` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `/log-kaldir` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `/log-durum` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `/log-sifirla`", inline=False)
        e.add_field(name="Level Sistemi", value="`.levelkur` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Modal ile kurulum\n`.levelrol <seviye> @rol` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Rol odulu ekler\n`.levelrolsil <seviye>` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Rol odulunu siler\n`.levelrolleri` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Odulleri listeler\n`.levelmesajtest [@uye]`\n`.leveldurum` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.seviye [@uye]`", inline=False)
        e.add_field(name="Hosgeldin Sistemi", value="`.hosgeldinkur` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Modal ile kurulum\n`.hosgeldindurum` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Ayarlari gosterir\n`.hosgeldinmesajtest [@uye]`", inline=False)
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
        e.add_field(name="Hizli Baslangic", value="`.profil` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.ticketpanel` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.levelkur` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.hosgeldinkur`", inline=False)
        e.set_footer(text=f"{ctx.guild.name} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Yardim Menusu")
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
        e.add_field(name="Ticket", value="`.ticketkur [kategori] #log @rol`\n`.ticketpanel`\n`.ticketkapat` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.ticketekle` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.ticketcikar`\n`.ticketkonu` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.ticketlist` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.ticketsayi`\n`.ticketoncelik` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.ticketsahip` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.ticketyeniden`", inline=False)
        e.add_field(name="Log", value="`.logkur`\n`.logkurkanal`\n`/log-kur` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `/log-kaldir`\n`/log-durum` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `/log-sifirla`", inline=False)
        e.add_field(name="Level", value="`.levelkur`\n`.levelrol <seviye> @rol`\n`.levelrolsil <seviye>`\n`.levelrolleri`\n`.levelmesajtest [@uye]`\n`.leveldurum` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.seviye [@uye]`", inline=False)
        e.add_field(name="Hosgeldin", value="`.hosgeldinkur`\n`.hosgeldindurum`\n`.hosgeldinmesajtest [@uye]`\n`.karsilamakur`\n`.karsilamadurum`\n`.karsilamatest [@uye]`", inline=False)
        e.add_field(name="Diger", value="`.antilink`\n`.antilink ac`\n`.antilink kapat`\n`.antilink muaf @rol/#kanal`\n`.renkekle @rol` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.renkcikar @rol`\n`.renklist` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.renkpanel`", inline=False)
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
        e.set_footer(text=f"{ctx.guild.name} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")
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
        e.add_field(name="Ticket", value="`.ticketkur [kategori] #log @rol [@rol2 ...]`\n`.ticketpanel`\n`.ticketkapat` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.ticketekle` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.ticketcikar`\n`.ticketkonu` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.ticketlist` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.ticketsayi`\n`.ticketoncelik` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.ticketsahip` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.ticketyeniden`", inline=False)
        e.add_field(name="Log", value="`.logkur`\n`.logkurkanal`\n`/log-kur` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `/log-kaldir`\n`/log-durum` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `/log-sifirla`", inline=False)
        e.add_field(name="Level", value="`.levelkur`\n`.levelrol <seviye> @rol`\n`.levelrolsil <seviye>`\n`.levelrolleri`\n`.levelmesajtest [@uye]`\n`.leveldurum` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.seviye [@uye]`", inline=False)
        e.add_field(name="Hosgeldin", value="`.hosgeldinkur`\n`.hosgeldindurum`\n`.hosgeldinmesajtest [@uye]`", inline=False)
        e.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Guvenlik Sistemleri", value="`.spam-koruma-kur` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Modal ile spam koruma ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±\n`.link-koruma-kur` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Modal ile link koruma ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±\n`.link-koruma-muaf-rol @rol` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Link muaf rol ekle\n`.link-koruma-muaf-kanal #kanal` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Link muaf kanal ekle\n`.link-koruma-durum` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Link koruma durumu", inline=False)
        e.add_field(name="Diger Sistemler", value="`.antilink`\n`.antilink ac`\n`.antilink kapat`\n`.antilink muaf @rol/#kanal`\n`.renkekle @rol` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.renkcikar @rol`\n`.renklist` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.renkpanel`\n`.guvenlikkur` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.guvenlikdurum`\n`.guvenlikizin @uye/@rol` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ `.guvenlikizinsil @uye/@rol`", inline=False)
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

# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  BOTU BAÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚ÂLAT
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

    def mod_embed():
        e = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Moderasyon", color=0xE74C3C, timestamp=datetime.now(timezone.utc))
        e.add_field(name="ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye", value="`.ban @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Banlar\n`.unban <id> [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Ban kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r\n`.kick @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Atar\n`.mute @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re] [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Susturur ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· boÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸=kalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±\n`.unmute @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r", inline=False)
        e.add_field(name="Kanal & Mesaj", value="`.sil [adet]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Mesaj siler (max 100)\n`.slowmode [sn]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â YavaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ mod ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· 0=kapat\n`.duyuru #kanal mesaj` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Duyuru gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderir", inline=False)
        e.add_field(name="UyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value="`.warn @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Verir\n`.uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lar @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶sterir\n`.uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sil @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Temizler", inline=False)
        return e

    def partner_embed():
        e = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤Ãƒâ€šÃ‚Â Partner Sistemi", color=0x57F287, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Komutlar", value="`.partner-kur #text #log` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â KanallarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ayarlar\n`.partner-istatistik` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°statistikler\n`.partner-top` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¥ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¥Ãƒâ€¹Ã¢â‚¬Â Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¥ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ralama\n`.partner-liste` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Sunucu listesi\n`.partner-sifirla` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±fÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rlar", inline=False)
        e.add_field(name="NasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±l ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§alÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r?", value="Yetkili kanala partner textini atar\nBot davet linkini kontrol eder\nLink yoksa siler ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· Var ise kaydeder\nAynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± sunucu ile 1 saat bekleme var", inline=False)
        return e

    def eglence_embed():
        e = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° EÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸lence & Bilgi", color=0xF1C40F, timestamp=datetime.now(timezone.utc))
        e.add_field(name="ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸", value="`.cekilisbaslat [sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re] [kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i] [ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼l]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â BaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸latÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r\n`.cekilisbitir <mesaj_id>` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Erken bitirir", inline=False)
        e.add_field(name="AFK", value="`.afk [sebep]` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â AFK moduna girer\nÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Mesaj atÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nca otomatik ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±kar\nÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Etiketlenince AFK bildirilir", inline=False)
        e.add_field(name="Bilgi", value="`.sunucu` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Sunucu istatistikleri", inline=False)
        return e

    def araclar_embed():
        e = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â§ AraÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§lar & Sistemler", color=0x9B59B6, timestamp=datetime.now(timezone.utc))
        e.add_field(name="Ticket", value="`.ticketkur [kategori] #log @rol` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Kurar\n`.ticketpanel` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Panel gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderir", inline=False)
        e.add_field(name="Anti-Link", value="`.antilink` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Durum\n`.antilink ac` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â AÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ar\n`.antilink kapat` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â KapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r\n`.antilink muaf @rol/#kanal` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Muafiyet", inline=False)
        e.add_field(name="Log Sistemi", value="`.logkur` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.logkurkanal`\n`/log-kur` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `/log-kaldir` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `/log-durum` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `/log-sifirla`", inline=False)
        e.add_field(name="Level Sistemi", value="`.levelkur` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.levelrol` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.levelrolsil` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.levelrolleri`\n`.levelmesajtest` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.leveldurum` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.seviye`", inline=False)
        e.add_field(name="Hosgeldin Sistemi", value="`.hosgeldinkur` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.hosgeldindurum` ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· `.hosgeldinmesajtest`", inline=False)
        e.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Guvenlik Sistemleri", value="`.spam-koruma-kur` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Modal ile spam koruma ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±\n`.link-koruma-kur` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Modal ile link koruma ayarlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±\n`.link-koruma-muaf-rol @rol` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Link muaf rol ekle\n`.link-koruma-muaf-kanal #kanal` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Link muaf kanal ekle\n`.link-koruma-durum` ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Link koruma durumu", inline=False)
        return e

    class HelpView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=60)

        @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Moderasyon", style=discord.ButtonStyle.danger)
        async def btn_mod(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=mod_embed(), view=self)

        @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤Ãƒâ€šÃ‚Â Partner", style=discord.ButtonStyle.success)
        async def btn_partner(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=partner_embed(), view=self)

        @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° EÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸lence", style=discord.ButtonStyle.primary)
        async def btn_eglence(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=eglence_embed(), view=self)

        @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â§ AraÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§lar", style=discord.ButtonStyle.secondary)
        async def btn_araclar(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=araclar_embed(), view=self)

        @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â  Ana MenÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼", style=discord.ButtonStyle.secondary, row=1)
        async def btn_ana(self, i: discord.Interaction, b: discord.ui.Button):
            await i.response.edit_message(embed=ana_embed(), view=self)

    await ctx.send(embed=ana_embed(), view=HelpView())


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  BOTU BAÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚ÂLAT
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬




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
        "Moderasyon": {"ban", "unban", "kick", "mute", "unmute", "sil", "warn", "uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lar", "uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sil", "slowmode", "duyuru", "jail", "unjail"},
        "Roller": {"renkekle", "renkcikar", "renklist", "renkpanel", "animerollerikur", "animerollerikaldir", "animerolpanel", "asagitasi", "levelrol", "levelrolsil", "levelrolleri"},
        "Sistemler": {"ticketekle", "ticketcikar", "ticketkapat", "ticketkonu", "ticketlist", "ticketsayi", "ticketoncelik", "ticketsahip", "ticketyeniden", "hosgeldindurum", "hosgeldinmesajtest", "karsilamadurum", "karsilamatest", "leveldurum", "levelmesajtest"},
        "Kullanici": {"profil", "seviye", "sunucu", "afk", "partner-istatistik", "partner-top", "partner-liste", "partner-sifirla"},
        "Eglence": {"cekilisbaslat", "cekilisbitir", "ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸katÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", "ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸sil", "ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸yenile", "ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸bilgi"},
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
        "Eglence": {"cekilisbaslat", "cekilisbitir", "ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸katÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", "ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸sil", "ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸yenile", "ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸bilgi", "afk"},
        "Moderasyon": {"ban", "unban", "kick", "mute", "unmute", "sil", "warn", "uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lar", "uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sil", "slowmode", "duyuru"},
    }


def _yardim_komutlarini_topla():
    prefix_komutlar = {}
    for komut in bot.commands:
        if komut.hidden or komut.name in {"yardÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±m", "yardim", "help"}:
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


for _eski in ("yardim", "help", "yardÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±m"):
    try:
        bot.remove_command(_eski)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m", "help"])
async def yardim(ctx):
    await gelismis_yardim_v3(ctx)

# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ AFK yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± fonksiyonlar ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

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

# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Anti-link yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± fonksiyonlar ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

def antilink_durum_al(guild_id: int) -> dict:
    return ayarlari_yukle().get(str(guild_id), {}).get("antilink", {"aktif": False, "muaf_roller": [], "muaf_kanallar": []})

def antilink_kaydet(guild_id: int, veri: dict):
    def _guncelle(ayarlar):
        gk = str(guild_id)
        if gk not in ayarlar:
            ayarlar[gk] = {}
        ayarlar[gk]["antilink"] = veri

    ayarlari_guncelle(_guncelle)

# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  PARTNER KANALI ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â MESAJ KONTROLÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

import re
DAVET_REGEX = re.compile(r"(?:https?://)?(?:discord\.(?:gg|com)|discordapp\.com)/(?:invite/)?([a-zA-Z0-9_-]+)")
@bot.event
async def on_message(message: discord.Message):
    """
    Partner kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± mesaj kontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ + AFK + Anti-link + prefix komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±
    """
    if message.author.bot:
        await _prefix_komutlari_isle(message)
        return

    if message.guild:
        # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Partner kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
        partner_ch_id = partner_kanal_id_al(message.guild.id)
        if partner_ch_id and message.channel.id == partner_ch_id:
            eslesen = DAVET_REGEX.search(message.content)

            if not eslesen:
                try:
                    await message.delete()
                except discord.Forbidden:
                    pass
                uyari = await message.channel.send(embed=discord.Embed(
                    title="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ GeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ersiz Partner Metni",
                    description=f"{message.author.mention} MesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±zda Discord davet linki bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±. MesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z silindi.",
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

            # 1 saat bekleme kontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼
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
                            title="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â³ Bekleme SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼resi DolmadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                            description=(
                                f"{message.author.mention} Bu sunucuyla tekrar partner yapmak iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in\n"
                                f"**{kalan // 60} dakika {kalan % 60} saniye** beklemeniz gerekiyor.\n"
                                f"Son partner: <@{onceki_id}> tarafÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan yapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±."
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
                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤Ãƒâ€šÃ‚Â Yeni Partner YapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±!",
                description=f"{message.author.mention} yeni bir partnerlik yaptÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±!",
                color=0x57F287,
                timestamp=simdi
            )
            stats_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Sunucu SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",  value=f"**#{sira}**",                              inline=True)
            stats_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ Yetkili SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"**#{yetkili_sira}** ({yetkili_toplam} partnerlik)", inline=True)
            stats_embed.add_field(
                name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â Zamana DayalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±:",
                value=(
                    f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Âº GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nlÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼k: **{stats['gunluk']}**\n"
                    f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Âº HaftalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k: **{stats['haftalik']}**\n"
                    f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Âº AylÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k: **{stats['aylik']}**"
                ),
                inline=True
            )
            stats_embed.add_field(name="ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Toplam", value=f"**{stats['toplam']}**", inline=True)
            stats_embed.set_footer(text=f"{bot.user.name} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Partner Sistemi")
            if message.guild.icon:
                stats_embed.set_thumbnail(url=message.guild.icon.url)
            await message.channel.send(embed=stats_embed)

            log_kanal_id = partner_log_kanali_al(message.guild.id)
            if log_kanal_id:
                log_kanal = message.guild.get_channel(log_kanal_id)
                if log_kanal:
                    log_embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Partner Logu", color=0x57F287, timestamp=simdi)
                    log_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Davet",          value=f"`{davet_kodu}`",                       inline=True)
                    log_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ Yapan",          value=message.author.mention,                  inline=True)
                    log_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Zaman",          value=simdi.strftime("%d.%m.%Y %H:%M UTC"),    inline=True)
                    log_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Toplam",         value=str(stats["toplam"]),                    inline=True)
                    log_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ Yetkili ToplamÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=str(yetkili_toplam),                   inline=True)
                    log_embed.set_footer(text=zaman_damgasi())
                    await log_kanal.send(embed=log_embed)
            return

        # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ AFK kontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
        afk_veri = afk_al(message.guild.id, message.author.id)
        if afk_veri and not message.content.startswith(".afk"):
            afk_sil(message.guild.id, message.author.id)
            zaman_afk = utc_datetime_from_iso(afk_veri["zaman"])
            dk = int((datetime.now(timezone.utc) - zaman_afk).total_seconds() // 60)
            uyari = await message.channel.send(embed=discord.Embed(
                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ AFK Modundan ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±kÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                description=f"{message.author.mention} AFK modundan ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ktÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±! ({dk} dakika AFK'daydÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±)",
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

        # Etiketlenen kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i AFK mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±?
        for etiket in message.mentions:
            afk_bilgi = afk_al(message.guild.id, etiket.id)
            if afk_bilgi:
                await message.channel.send(embed=discord.Embed(
                    description=f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¤ {etiket.mention} ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸u an AFK ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â **{afk_bilgi['sebep']}**",
                    color=RENKLER["bilgi"]
                ), delete_after=8)

        # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Anti-link kontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
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
                        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Link Engellendi",
                        description=f"{message.author.mention} Bu kanalda link paylaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸mak yasak!",
                        color=RENKLER["hata"]
                    ))
                    await asyncio.sleep(5)
                    try:
                        await uyari.delete()
                    except discord.NotFound:
                        pass
                    return

        # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ KÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r KorumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kontolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
        yasakli_kelimeler = kufur_kelimelerini_al(message.guild.id)
        if yasakli_kelimeler and mesajda_yasakli_kelime_var_mi(message.content, yasakli_kelimeler):
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            uyari = await message.channel.send(embed=discord.Embed(
                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â KÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r AlgÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±landÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                description=f"{message.author.mention} MesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±zda yasak kelime bulunduÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸u iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in silinmiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tir.",
                color=RENKLER["hata"]
            ))
            await asyncio.sleep(5)
            try:
                await uyari.delete()
            except discord.NotFound:
                pass
            return

    await _prefix_komutlari_isle(message)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â
#  SLOWMODE
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â

@bot.command(name="slowmode", aliases=["sm", "yavasm"])
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, sure: int = 0):
    if sure < 0 or sure > 21600:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re 0-21600 saniye arasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nda olmalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±."); return
    await ctx.channel.edit(slowmode_delay=sure)
    if sure == 0:
        embed = discord.Embed(title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ YavaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ Mod KapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", color=RENKLER["basari"])
    else:
        embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¢ YavaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ Mod AÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", color=RENKLER["mute"])
        embed.add_field(name="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re", value=f"{sure} saniye", inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Kanal", value=ctx.channel.mention, inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Yetkili", value=ctx.author.mention, inline=True)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)

@slowmode.error
async def slowmode_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Kanal yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶netme yetkine sahip deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilsin.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.slowmode [saniye]`")


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â
#  DUYURU
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â

@bot.command(name="duyuru", aliases=["announce", "ann"])
@commands.has_permissions(manage_guild=True)
async def duyuru(ctx, kanal: discord.TextChannel = None, *, mesaj: str = None):
    if not mesaj:
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.duyuru #kanal mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z`"); return
    hedef = kanal or ctx.channel
    embed = discord.Embed(description=mesaj, color=0xE74C3C, timestamp=datetime.now(timezone.utc))
    embed.set_author(name=f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¢ {ctx.guild.name} Duyurusu", icon_url=ctx.guild.icon.url if ctx.guild.icon else None)
    embed.set_footer(text=f"Duyuran: {ctx.author}")
    await hedef.send("@everyone", embed=embed)
    try: await ctx.message.delete()
    except: pass

@duyuru.error
async def duyuru_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Sunucu yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶netme yetkine sahip deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilsin.")


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â
#  SUNUCU ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°STATÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°STÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°K
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â

@bot.command(name="sunucu", aliases=["server", "serverinfo", "si"])
async def sunucu_bilgi(ctx):
    g = ctx.guild
    insan  = sum(1 for m in g.members if not m.bot)
    botlar = sum(1 for m in g.members if m.bot)
    embed = discord.Embed(title=f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  {g.name}", color=0x5865F2, timestamp=datetime.now(timezone.utc))
    if g.icon: embed.set_thumbnail(url=g.icon.url)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ Sahip",       value=g.owner.mention,                                    inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ID",          value=f"`{g.id}`",                                        inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ KuruluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸",     value=g.created_at.strftime("%d.%m.%Y"),                  inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¥ Toplam ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye",  value=str(g.member_count),                                inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°nsan",       value=str(insan),                                         inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ Bot",         value=str(botlar),                                        inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¬ Metin Kanal", value=str(len(g.text_channels)),                          inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â  Ses Kanal",   value=str(len(g.voice_channels)),                         inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â­ Rol",         value=str(len(g.roles) - 1),                             inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Boost",       value=f"{g.premium_subscription_count} ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· Seviye {g.premium_tier}", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â
#  AFK SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°STEMÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â

@bot.command(name="afk")
async def afk_cmd(ctx, *, sebep: str = "AFK"):
    afk_kaydet(ctx.guild.id, ctx.author.id, sebep)
    embed = discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¹Ã…â€œÃƒâ€šÃ‚Â´ AFK Moduna GeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ildi",
        description=f"{ctx.author.mention} AFK moduna geÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ti.\n**Sebep:** {sebep}",
        color=RENKLER["bilgi"]
    )
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)
    try:
        await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}"[:32])
    except discord.Forbidden:
        pass


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â
#  ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡EKÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°LÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°STEMÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â

import random as _random

@bot.command(name="cekilisbaslat", aliases=["cekilish", "gstart", "giveaway"])
@commands.has_permissions(manage_guild=True)
async def cekilisbaslat(ctx, sure: str = None, kazanan: int = 1, *, odul: str = None):
    if not sure or not odul:
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.cekilisbaslat 1h 1 Nitro`"); return
    birimler = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    try:
        saniye = int(sure[:-1]) * birimler[sure[-1]]
    except (ValueError, KeyError, IndexError):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ GeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ersiz sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re. ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“rnek: `10s`, `5m`, `2h`, `1d`"); return
    bitis = datetime.now(timezone.utc) + timedelta(seconds=saniye)
    embed = discord.Embed(
        title=f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡EKÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°LÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â {odul}",
        description=f"KatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lmak iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° tepkisini ver!\n\n**ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â° BitiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸:** {bitis.strftime('%d.%m.%Y %H:%M UTC')}\n**Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â  Kazanan:** {kazanan} kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i\n**Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼l:** {odul}",
        color=0xFF73FA, timestamp=bitis
    )
    embed.set_footer(text="BitiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸")
    mesaj = await ctx.send(embed=embed)
    await mesaj.add_reaction("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°")
    try: await ctx.message.delete()
    except: pass
    await asyncio.sleep(saniye)
    try: mesaj = await ctx.channel.fetch_message(mesaj.id)
    except discord.NotFound: return
    tepki = discord.utils.get(mesaj.reactions, emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°")
    if not tepki:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Kimse katÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lmadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±, ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ iptal."); return
    katilimcilar = [u async for u in tepki.users() if not u.bot]
    if not katilimcilar:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ GeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§erli katÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± yok."); return
    kazananlar  = _random.sample(katilimcilar, min(kazanan, len(katilimcilar)))
    kazanan_str = " ".join(u.mention for u in kazananlar)
    bitis_embed = discord.Embed(
        title=f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€¦Ã‚Â  ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡EKÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°LÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â SONA ERDÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â {odul}",
        description=f"**Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â  Kazanan:** {kazanan_str}\n**Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼l:** {odul}\n**Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¥ KatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±:** {len(katilimcilar)}",
        color=0xFF73FA, timestamp=datetime.now(timezone.utc)
    )
    await mesaj.edit(embed=bitis_embed)
    await ctx.channel.send(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° Tebrikler {kazanan_str}! **{odul}** kazandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z!")

@cekilisbaslat.error
async def cekilisbaslat_hata(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Sunucu yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶netme yetkine sahip deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ilsin.")

@bot.command(name="cekilisbitir", aliases=["gend"])
@commands.has_permissions(manage_guild=True)
async def cekilisbitir(ctx, mesaj_id: int = None):
    if not mesaj_id:
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.cekilisbitir <mesaj_id>`"); return
    try: mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Mesaj bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°")
    if not tepki:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Bu mesajda Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° tepkisi yok."); return
    katilimcilar = [u async for u in tepki.users() if not u.bot]
    if not katilimcilar:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ KatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± yok."); return
    kazanan = _random.choice(katilimcilar)
    await ctx.send(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° Yeni kazanan: {kazanan.mention}!")


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Ek ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ KomutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

@bot.command(name="ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸katÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", aliases=["glist", "cekiliskatilimci", "katilimcilar"])
async def cekiliskatilimci(ctx, mesaj_id: int = None):
    """.ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸katÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± <mesaj_id> ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ katÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±larÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± listeler."""
    if not mesaj_id:
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸katÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± <mesaj_id>`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Mesaj bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°")
    katilimcilar = [u async for u in tepki.users() if not u.bot] if tepki else []
    if not katilimcilar:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ HenÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼z kimse katÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lmamÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸."); return
    embed = discord.Embed(
        title=f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ KatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±larÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â {len(katilimcilar)} kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i",
        description="\n".join(f"`{i+1}.` {u.mention}" for i, u in enumerate(katilimcilar[:30])),
        color=0xFF73FA,
        timestamp=datetime.now(timezone.utc)
    )
    if len(katilimcilar) > 30:
        embed.set_footer(text=f"ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°lk 30 gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶steriliyor ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â· Toplam: {len(katilimcilar)}")
    else:
        embed.set_footer(text=f"Toplam: {len(katilimcilar)} katÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±")
    await ctx.send(embed=embed)


@bot.command(name="ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸sil", aliases=["gdelete", "cekilissil", "gcancel"])
@commands.has_permissions(manage_guild=True)
async def cekilissil(ctx, mesaj_id: int = None):
    """.ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸sil <mesaj_id> ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i iptal eder ve siler."""
    if not mesaj_id:
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸sil <mesaj_id>`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
        await mesaj.delete()
        await ctx.send(embed=discord.Embed(
            title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ptal Edildi",
            description="ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± silindi.",
            color=RENKLER["hata"]
        ), delete_after=5)
    except discord.NotFound:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Mesaj bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.")


@bot.command(name="ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸yenile", aliases=["greroll", "cekilisyenile"])
@commands.has_permissions(manage_guild=True)
async def cekilisyenile(ctx, mesaj_id: int = None, kazanan: int = 1):
    """.ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸yenile <mesaj_id> [kazanan sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±] ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Yeni kazanan seÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§er."""
    if not mesaj_id:
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸yenile <mesaj_id> [kazanan sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±]`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Mesaj bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°")
    katilimcilar = [u async for u in tepki.users() if not u.bot] if tepki else []
    if not katilimcilar:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ KatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± yok."); return
    kazananlar = _random.sample(katilimcilar, min(kazanan, len(katilimcilar)))
    kazanan_str = " ".join(u.mention for u in kazananlar)
    embed = discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€¦Ã‚Â  ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ Yenilendi!",
        description=f"**Yeni kazanan(lar):** {kazanan_str}",
        color=0xFF73FA,
        timestamp=datetime.now(timezone.utc)
    )
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)
    await ctx.send(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° Tebrikler {kazanan_str}!")


@bot.command(name="ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸bilgi", aliases=["ginfo", "cekilisbilgi"])
async def cekilisbilgi(ctx, mesaj_id: int = None):
    """.ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸bilgi <mesaj_id> ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ bilgilerini gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶sterir."""
    if not mesaj_id:
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸bilgi <mesaj_id>`"); return
    try:
        mesaj = await ctx.channel.fetch_message(mesaj_id)
    except discord.NotFound:
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Mesaj bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±."); return
    tepki = discord.utils.get(mesaj.reactions, emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°")
    katilimcilar = [u async for u in tepki.users() if not u.bot] if tepki else []
    embed = discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ Bilgileri",
        color=0xFF73FA,
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¥ KatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=str(len(katilimcilar)), inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ OluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turma", value=mesaj.created_at.strftime("%d.%m.%Y %H:%M"), inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Mesaj", value=f"[TÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±kla]({mesaj.jump_url})", inline=True)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â
#  TÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°CKET SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°STEMÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â° (GELÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚ÂTÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°RÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°LMÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â)
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â

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
            ekler = f'<div class="attachments">Ekler: {" ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ ".join(baglantilar)}</div>'
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
      <p>{len(mesajlar)} mesaj ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {html.escape(channel.guild.name)}</p>
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
    .ticketkur [kategori] #log-kanal @destek-rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ [@destek-rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼-2 ...]
    Ticket sistemini kurar.
    """
    if not kategori or not log or not destek_rolleri:
        await ctx.send(embed=kullanim_embedi("`.ticketkur [kategori] #log-kanal @destek-rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ [@destek-rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼-2 ...]`")); return

    destek_rolleri = list(dict.fromkeys(rol.id for rol in destek_rolleri if rol))
    if not destek_rolleri:
        await ctx.send(embed=hata_embedi("Destek RolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ Gerekli", "Ticket sistemi iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in en az bir destek rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ belirtmelisin."))
        return

    mevcut = ticket_ayar_al(ctx.guild.id)
    mevcut.update({"kategori": kategori.id, "log": log.id, "rol_ids": destek_rolleri, "rol": destek_rolleri[0]})
    ticket_ayar_kaydet(ctx.guild.id, mevcut)

    embed = discord.Embed(title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Ticket Sistemi Kuruldu", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Kategori",    value=kategori.name,      inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Log",         value=log.mention,         inline=True)
    destek_rol_mentionlari = [ctx.guild.get_role(rid).mention for rid in destek_rolleri if ctx.guild.get_role(rid)]
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Destek Rolleri", value=", ".join(destek_rol_mentionlari) if destek_rol_mentionlari else "Yok", inline=False)
    embed.set_footer(text=zaman_damgasi())
    await ctx.send(embed=embed)


@bot.command(name="ticketpanel", aliases=["ticket-panel"])
@commands.has_permissions(administrator=True)
async def ticket_panel(ctx):
    """.ticketpanel ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Ticket aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ma paneli gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderir."""
    ayar = ticket_ayar_al(ctx.guild.id)
    if not ayar.get("kategori"):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“nce `.ticketkur` ile sistemi kur."); return

    class TicketView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â« Ticket AÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§", style=discord.ButtonStyle.primary, custom_id="global_ticket_ac")
        async def ticket_ac(self, interaction: discord.Interaction, button: discord.ui.Button):
            ayar        = ticket_ayar_al(interaction.guild_id)
            kategori    = interaction.guild.get_channel(ayar.get("kategori"))
            destek_rolleri = [interaction.guild.get_role(rid) for rid in ayar.get("rol_ids", [])]
            destek_rolleri = [rol for rol in destek_rolleri if rol]
            log_id      = ayar.get("log")

            if not kategori:
                await interaction.response.send_message("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Kategori bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±. `.ticketkur` ile yeniden kur.", ephemeral=True); return

            # AÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k ticket var mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kontrol et
            for kanal in kategori.text_channels:
                if kanal.topic and str(interaction.user.id) in kanal.topic:
                    await interaction.response.send_message(f"ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Zaten aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k bir ticketÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n var: {kanal.mention}", ephemeral=True); return

            # Ticket numarasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±
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

            # Ticket kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± view (kapat + talep al)
            class TicketKontrolView(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=None)

                @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Kapat", style=discord.ButtonStyle.danger, custom_id=f"ticket_kapat_{ticket_kanal.id}")
                async def kapat(self, i2: discord.Interaction, b: discord.ui.Button):
                    await _ticket_kapat_logu_ve_transkript(ticket_kanal, i2.user, log_id)
                    await i2.response.send_message("Ticket kapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±yor...", ephemeral=True)

                    if False and log_id:
                        log_k = i2.guild.get_channel(log_id)
                        if log_k:
                            await log_k.send(embed=discord.Embed(
                                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Ticket KapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                                description=(
                                    f"**Ticket:** `{ticket_kanal.name}`\n"
                                    f"**Sahip:** {interaction.user.mention}\n"
                                    f"**Kapatan:** {i2.user.mention}"
                                ),
                                color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)
                            ))
                    await ticket_kanal.delete(reason=f"{i2.user} tarafÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan kapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±")

                @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¥ ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“ye Ekle", style=discord.ButtonStyle.secondary, custom_id=f"ticket_uyeekle_{ticket_kanal.id}")
                async def uye_ekle(self, i2: discord.Interaction, b: discord.ui.Button):
                    if destek_rolleri and not any(rol in i2.user.roles for rol in destek_rolleri) and not i2.user.guild_permissions.administrator:
                        await i2.response.send_message("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Bu iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lem iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in destek rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ veya yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶netici yetkisi gerekli.", ephemeral=True)
                        return
                    await i2.response.send_message("Eklemek istediÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸in kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±yÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± etiketle: (ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶rn: @kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±)", ephemeral=True)

                    def check(m):
                        return m.author == i2.user and m.channel == ticket_kanal and m.mentions

                    try:
                        yanit = await bot.wait_for("message", check=check, timeout=30)
                        for uye in yanit.mentions:
                            await ticket_kanal.set_permissions(uye, read_messages=True, send_messages=True)
                        await ticket_kanal.send(f"ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ {' '.join(u.mention for u in yanit.mentions)} ticketa eklendi.")
                        await yanit.delete()
                    except asyncio.TimeoutError:
                        pass

                @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Talep Al", style=discord.ButtonStyle.success, custom_id=f"ticket_talep_{ticket_kanal.id}")
                async def talep_al(self, i2: discord.Interaction, b: discord.ui.Button):
                    if destek_rolleri and not any(rol in i2.user.roles for rol in destek_rolleri) and not i2.user.guild_permissions.administrator:
                        await i2.response.send_message("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Bu iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸lem iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in destek rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ gerekli.", ephemeral=True); return
                    await ticket_kanal.edit(topic=f"{ticket_kanal.topic} | Talep: {i2.user}")
                    await i2.response.send_message(f"ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Ticket {i2.user.mention} tarafÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan talep alÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.")

            ac_embed = discord.Embed(
                title=f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â« Ticket #{sayi:04d}",
                description=(
                    f"Merhaba {interaction.user.mention}!\n"
                    f"Destek ekibimiz en kÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sa sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rede yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± olacak.\n\n"
                    f"TicketÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kapatmak iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ butonunu kullan."
                ),
                color=0x57F287, timestamp=datetime.now(timezone.utc)
            )
            ac_embed.set_footer(text=f"Ticket #{sayi:04d} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")

            await ticket_kanal.send(
                content=" ".join([interaction.user.mention] + [rol.mention for rol in destek_rolleri]),
                embed=ac_embed,
                view=TicketKontrolView()
            )
            await interaction.response.send_message(f"ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ TicketÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±: {ticket_kanal.mention}", ephemeral=True)

            if log_id:
                log_k = interaction.guild.get_channel(log_id)
                if log_k:
                    await log_k.send(embed=discord.Embed(
                        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â« Yeni Ticket AÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                        description=f"**AÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§an:** {interaction.user.mention}\n**Kanal:** {ticket_kanal.mention}\n**Numara:** `#{sayi:04d}`",
                        color=RENKLER["giris"], timestamp=datetime.now(timezone.utc)
                    ))

    panel_embed = discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â« Destek Merkezi",
        description="YardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m almak iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in aÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸aÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±daki butona tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±kla.\nEkibimiz en kÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sa sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rede sana yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± olacak.",
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
    """.ticketekle @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Ticket kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye ekler."""
    if not uye:
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.ticketekle @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye`"); return
    await ctx.channel.set_permissions(uye, read_messages=True, send_messages=True)
    await ctx.send(embed=discord.Embed(
        description=f"ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ {uye.mention} ticketa eklendi.",
        color=RENKLER["basari"]
    ))


@bot.command(name="ticketcikar", aliases=["ticket-cikar"])
@commands.has_permissions(manage_channels=True)
async def ticket_cikar(ctx, uye: discord.Member = None):
    """.ticketcikar @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Ticket kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±karÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r."""
    if not uye:
        await ctx.send("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬â„¢ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.ticketcikar @ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye`"); return
    await ctx.channel.set_permissions(uye, read_messages=False)
    await ctx.send(embed=discord.Embed(
        description=f"ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ {uye.mention} tickettan ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±karÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
        color=RENKLER["hata"]
    ))


@bot.command(name="ticketkapat", aliases=["ticket-kapat"])
@commands.has_permissions(manage_channels=True)
async def ticket_kapat(ctx):
    """.ticketkapat ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Mevcut ticket kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r."""
    if not ctx.channel.name.startswith("ticket-"):
        await ctx.send("ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Bu komut sadece ticket kanallarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nda kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±labilir."); return

    ayar   = ticket_ayar_al(ctx.guild.id)
    log_id = ayar.get("log")
    await _ticket_kapat_logu_ve_transkript(ctx.channel, ctx.author, log_id)

    if False and log_id:
        log_k = ctx.guild.get_channel(log_id)
        if log_k:
            await log_k.send(embed=discord.Embed(
                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Ticket KapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                description=f"**Ticket:** `{ctx.channel.name}`\n**Kapatan:** {ctx.author.mention}",
                color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)
            ))
    await ctx.send("Ticket kapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±yor...")
    await asyncio.sleep(2)
    await ctx.channel.delete(reason=f"{ctx.author} tarafÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan kapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±")

# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  FLASK (RENDER CANLI TUTMAK ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°N)
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

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
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¥ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Naruto ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Sasuke ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¸ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Sakura ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¡ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Kakashi ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Itachi ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¦Ãƒâ€¦Ã‚Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Kurama ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Luffy ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Zoro ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€¦Ã‚Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Nami ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Ace ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Shanks ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Law ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€¦Ã‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Robin ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Franky ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â» ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Brook ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¹Ã…â€œÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Sanji ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Ichigo ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Rukia ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¦Ã¢â‚¬â„¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Aizen ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Ulquiorra ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Goku ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¥ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Vegeta ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¦Ã‚Â¸ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Gohan ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¹Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Broly ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€¹Ã¢â‚¬Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Beerus ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â³ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Whis ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â©Ãƒâ€šÃ‚Â¸ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Eren ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂªÃƒâ€šÃ‚Â½ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Mikasa ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Armin ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â§ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Levi ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Âº ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Hange ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Reiner ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Tanjiro ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¸ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Nezuko ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Inosuke ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¡ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Zenitsu ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Rengoku ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â«ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Muichiro ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Shinobu ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Tengen ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â©Ãƒâ€šÃ‚Âµ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Gojo ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Âº ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Megumi ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Âº ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Nobara ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Sukuna ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¼ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Panda ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Maki ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Yuta ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Geto ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â­ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Lelouch ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â C.C. ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¹ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Kallen ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Light ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â L ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Ryuk ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â» ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Kira ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Hikari ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â« ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Emilia ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Rem ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Ram ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬â„¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Âº ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Subaru ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¼ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Zero Two ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Âº ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Hiro ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¦Ã‚Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Marin ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Gojo Wakana ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Âµ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Bocchi ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¸ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Kita ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¥Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Nijika ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¼ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Ryo ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Âª ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Senku ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Gen ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂªÃƒâ€šÃ‚Â¨ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Taiju ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¿ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Yuzuriha ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¹Ã¢â‚¬Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Natsu ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Gray ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¤ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Erza ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Happy ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â£ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Kaneki ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¹Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Touka ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â·ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Hisoka ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â£ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Gon ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¡ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Killua ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Kurapika ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€ Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Chrollo ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â» ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Power ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Âª ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Denji ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¶ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Pochita ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â©Ãƒâ€šÃ‚Â¸ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Makima ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¦Ãƒâ€¹Ã¢â‚¬Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Beam ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Âº ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Frieren ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Fern ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Stark ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â­ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Himmel ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Anya ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â¶ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Loid ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¹ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Yor ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Bond ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¦Ã¢â‚¬â„¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Madoka ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Homura ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¡ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Kagome ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Âº ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Inuyasha ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
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
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¥ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Naruto ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¹Ã…â€œÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â One Piece ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Bleach ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Dragon Ball ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂªÃƒâ€šÃ‚Â½ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Attack on Titan ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Demon Slayer ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â©Ãƒâ€šÃ‚Âµ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Jujutsu Kaisen ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â­ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Code Geass ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Death Note ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â« ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Re:Zero ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¼ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Darling in the Franxx ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¦Ã‚Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â My Dress-Up Darling ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Âµ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Bocchi the Rock ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Âª ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Dr. Stone ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¹Ã¢â‚¬Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Fairy Tail ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â£ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Tokyo Ghoul ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â£ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Hunter x Hunter ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Âª ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Chainsaw Man ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Âº ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Frieren ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¤ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Spy x Family ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¦Ã¢â‚¬â„¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Madoka Magica ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¡ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Inuyasha ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â» ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Your Lie in April ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¤ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Oshi no Ko ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Haikyuu ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â¡ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Orange ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€¦Ã¢â‚¬â„¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Horimiya ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¸ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Kimi ni Todoke ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂªÃƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Steins;Gate ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Violet Evergarden ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¥ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Black Butler ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Fire Force ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Shield Hero ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â² ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â No Game No Life ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Sword Art Online ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Âº ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Wolf's Rain ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â© ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Classroom of the Elite ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Land of the Lustrous ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¿ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â The Ancient Magus' Bride ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Sailor Moon ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â¸ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Kuma Kuma Bear ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â° ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Food Wars ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¹ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Forest of Piano ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€¹Ã¢â‚¬Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Natsume's Book of Friends ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â The Eminence in Shadow ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â» ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Summer Time Rendering ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Monster ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¹ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Fate Stay Night ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¡ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â A Certain Scientific Railgun ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Blue Period ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â¡ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Bungou Stray Dogs ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¹ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Rose of Versailles ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Âµ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Kill la Kill ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€¦Ã‚Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Free ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€¦Ã‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Angel Beats ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â§ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Weathering With You ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¹Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Garden of Words ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¹Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Blend S ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Black Clover ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Little Witch Academia ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¼ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Yona of the Dawn ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Cardcaptor Sakura ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¬ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Cowboy Bebop ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â White Album 2 ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Mashle ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â«Ãƒâ€šÃ‚Â§ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Bubble ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â°ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Astra Lost in Space ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¥ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Mob Psycho 100 ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â¯ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Hell Girl ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¾ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Beastars ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¯ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Assassination Classroom ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â To Your Eternity ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â­ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Noragami ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¸ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Gintama ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Erased ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂªÃƒâ€šÃ‚Â¶ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Princess Tutu ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â¶ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Komi Can't Communicate ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Âº ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â A Sign of Affection ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Is the Order a Rabbit ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â® ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Log Horizon ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬Å“ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Toriko ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¨ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Magi ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â­ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Vinland Saga ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â® ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â The Apothecary Diaries ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â´ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Black Lagoon ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¥Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Given ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¤ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Barakamon ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¦Ãƒâ€¦Ã‚Â  ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Spice and Wolf ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¦Ã‚Â¸ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Love Live ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â§ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Mawaru Penguindrum ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¥ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Blue Exorcist ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Fruits Basket ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂªÃƒâ€šÃ‚Â¼ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Jellyfish Can't Swim in the Night ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¬ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Millennium Actress ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¦ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Charlotte ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â¹ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â The World God Only Knows ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
    "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â¹ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Revolutionary Girl Utena ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€šÃ‚Â± ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Mushishi ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Dororo ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±", "ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â°ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â° Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â©Ãƒâ€šÃ‚Â¶ ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€¦Ã‚Â ÃƒÆ’Ã¢â‚¬Â¹Ãƒâ€šÃ‚Â Parasyte ÃƒÆ’Ã‚ÂªÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â±",
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
    embed.set_footer(text=f"Sayfa {sayfa + 1}/{max(1, (len(roller) + 23) // 24)} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Toplam {len(roller)} anime rolu")
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
            placeholder=f"Anime rol(ler)i sec ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Sayfa {sayfa + 1}",
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
            secenekler.append(discord.SelectOption(label="Renk KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r", value="clear", description="ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“zerindeki renk rollerini temizler"))
            super().__init__(placeholder="Kendine bir renk rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ seÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            mevcut_renkler = [rol for rol in roller if rol in interaction.user.roles]
            if mevcut_renkler:
                await interaction.user.remove_roles(*mevcut_renkler, reason="Renk secimi guncellendi")
            if self.values[0] == "clear":
                await interaction.response.send_message("ÃƒÆ’Ã†â€™Ãƒâ€¦Ã¢â‚¬Å“zerindeki renk rolleri temizlendi.", ephemeral=True)
                return
            yeni_rol = interaction.guild.get_role(int(self.values[0]))
            if yeni_rol:
                await interaction.user.add_roles(yeni_rol, reason="Renk paneli secimi")
                await interaction.response.send_message(f"Yeni rengin baÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸arÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±yla {yeni_rol.mention} olarak ayarlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.", ephemeral=True)

    class RenkView(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)
            self.add_item(RenkSec())

    rol_listesi = "\n".join(f"`{i+1}.` {rol.mention}" for i, rol in enumerate(roller[:12]))
    embed = discord.Embed(
        title="Renk RolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ SeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§im MenÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼",
        description=(
            "AÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸aÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±daki menÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼den sunucuda kullanmak istediÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸in renk rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ seÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ebilirsin.\n"
            "Yeni bir renk seÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§tiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸inde eski renk rollerin otomatik kaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r."
        ),
        color=RENKLER["rol"],
        timestamp=datetime.now(timezone.utc)
    )
    embed.add_field(name="NasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±l ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡alÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r?", value="MenÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼den bir renk seÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§.\nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°stersen `Renk KaldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r` ile tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m renk rollerini temizle.", inline=False)
    embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±labilir Roller", value=rol_listesi if rol_listesi else "Rol bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.", inline=False)
    embed.set_footer(text=f"Toplam {len(roller)} renk rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {ctx.guild.name}")
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    mesaj = await ctx.send(embed=embed, view=globals()["RenkView"](ctx.guild.id, [rol.id for rol in roller]))
    renk_panel_mesaji_ekle(ctx.guild.id, ctx.channel.id, mesaj.id)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â
#  LEVEL + HOSGELDIN SISTEMI (EK BLOK)
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â

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
        embed.set_footer(text=f"Sayfa {sayfa + 1}/{max(1, (len(roller) + 23) // 24)} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Toplam {len(roller)} anime rolu")
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
            super().__init__(placeholder=f"Anime rolu sec ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Sayfa {sayfa + 1}", min_values=1, max_values=1, options=secenekler)

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
        embed.set_footer(text=f"Sayfa {sayfa + 1}/{max(1, (len(roller) + 23) // 24)} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Toplam {len(roller)} anime rolu")
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
            super().__init__(placeholder=f"Anime rol(ler)i sec ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Sayfa {sayfa + 1}", min_values=1, max_values=max(1, len(secenekler)), options=secenekler)

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
        "mesaj": veri.get("mesaj", "AramÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±za hoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ geldin {username}. Seninle birlikte {member_count} kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iyiz."),
    }


def _karsilama_ayar_kaydet(guild_id: int, veri: dict):
    _guild_ayar_kismi_kaydet(guild_id, "karsilama_sistemi", veri)


TURKCE_KUFUR_LISTESI = [
    "amk", "aq", "amÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na", "amina", "amÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na koyim", "amina koyim", "amÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na koyayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m", "amina koyayim",
    "orospu", "orospu ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ocuÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸u", "orospu cocugu", "oc", "piÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§", "pic", "sikik", "sikerim", "sikiyim",
    "siktir", "siktir git", "yarrak", "yarak", "gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶t", "got", "gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶tveren", "gotveren", "ibne", "amcÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k",
    "amcik", "pezevenk", "kahpe", "puÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸t", "pust", "ananÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", "ananÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± sikeyim", "anani", "bok", "boktan",
    "salak orospu", "gerizekalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", "gerizekali", "piÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ kurusu", "ebenin", "ebesinin", "gavat", "mallÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k",
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
            title="GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlik UyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
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
        title="GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlik Sistemi Tetiklendi",
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
        ac_embed.set_footer(text=f"Ticket #{sayi:04d} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")

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
    return now.strftime("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ %d.%m.%Y ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â° %H:%M:%S UTC")


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
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Spam Koruma Durumu",
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
        title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Tum Sistemleri Kaldir",
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
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â° Sunucu Paneli", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
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
            satirlar.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ {uye.mention} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Uyari: {warn_sayi} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Partner: {partner_sayi}")
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â® Yetkili Paneli", description="\n".join(satirlar[:20]) or "Yetkili bulunamadi.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
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
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¹Ã…â€œ Ceza Gecmisi", description=f"{hedef.mention} icin kayitlar", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Uyari Sayisi", value=str(len(warnlar)), inline=True)
    embed.add_field(name="Aktif Timeout", value=timeout_var, inline=True)
    embed.add_field(name="Aktif Jail", value="Evet" if jail_kayit else "Hayir", inline=True)
    if warnlar:
        son_warn = "\n".join(f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {k.get('sebep', 'Sebep yok')}" for k in warnlar[-5:])
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
    await ctx.send(embed=discord.Embed(title="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â³ Sureli Rol Verildi", description=f"{uye.mention} kullanicisina {rol.mention} rolu verildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


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
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¬ Oto Cevap Kaydedildi", description=f"Anahtar: **{anahtar}**", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="sayac")
@commands.has_permissions(manage_guild=True)
async def sayac(ctx, hedef: int = 0, kanal: discord.TextChannel = None, *, mesaj: str = None):
    if hedef <= 0 or kanal is None:
        await ctx.send(embed=kullanim_embedi(".sayac 500 #kanal Hedefe ulastik! {member_count}/{target}"))
        return
    veri = {"aktif": True, "hedef": hedef, "kanal_id": kanal.id, "mesaj": mesaj or "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° Seninle birlikte {member_count} kisiyiz! Hedefimiz {target} idi.", "tetiklendi": False}
    _sayac_ayar_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¯ Sayac Ayarlandi", description=f"Hedef: **{hedef}** ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Kanal: {kanal.mention}", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


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
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨ Rol Menusu", description="Asagidan istedigin rolleri secebilirsin.", color=RENKLER["rol"], timestamp=datetime.now(timezone.utc))
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
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Uye Notu Eklendi", description=f"{uye.mention} icin not kaydedildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="isimgecmisi")
@commands.has_permissions(manage_guild=True)
async def isim_gecmisi(ctx, uye: discord.Member = None):
    if not uye:
        await ctx.send(embed=kullanim_embedi(".isimgecmisi @uye"))
        return
    veri = _isim_gecmisi_al(ctx.guild.id).get(str(uye.id), [])
    satirlar = [f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {k.get('eski')} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ {k.get('yeni')}" for k in veri[-10:]]
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â·ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Isim Gecmisi", description="\n".join(satirlar) or "Kayit yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="sesistatistik")
async def ses_istatistik(ctx):
    ayarlar = ayarlari_yukle().get(str(ctx.guild.id), {}).get("profil_istat", {})
    satirlar = []
    for uye_id, veri in sorted(ayarlar.items(), key=lambda x: int(x[1].get("voice_seconds", 0)), reverse=True)[:10]:
        uye = ctx.guild.get_member(int(uye_id))
        if uye:
            satirlar.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¤ {uye.mention} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {_sureyi_formatla(int(veri.get('voice_seconds', 0)))}")
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Ses Istatistik", description="\n".join(satirlar) or "Kayit yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="mesajistatistik")
async def mesaj_istatistik(ctx):
    ayarlar = ayarlari_yukle().get(str(ctx.guild.id), {}).get("profil_istat", {})
    satirlar = []
    for uye_id, veri in sorted(ayarlar.items(), key=lambda x: int(x[1].get("message_count", 0)), reverse=True)[:10]:
        uye = ctx.guild.get_member(int(uye_id))
        if uye:
            satirlar.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¬ {uye.mention} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {int(veri.get('message_count', 0))} mesaj")
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¨ Mesaj Istatistik", description="\n".join(satirlar) or "Kayit yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="kurulumdurum")
@commands.has_permissions(manage_guild=True)
async def kurulum_durum(ctx):
    ticket = ticket_ayar_al(ctx.guild.id)
    level = _level_ayar_al(ctx.guild.id)
    hosgeldin = _welcome_ayar_al(ctx.guild.id)
    karsilama = _karsilama_ayar_al(ctx.guild.id)
    guvenlik = _guvenlik_ayar_al(ctx.guild.id)
    jail = _jail_ayar_al(ctx.guild.id)
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â© Kurulum Durumu", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Ticket", value="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦" if ticket.get("kategori") else "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢", inline=True)
    embed.add_field(name="Level", value="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦" if level.get("kanal_id") else "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢", inline=True)
    embed.add_field(name="Hosgeldin", value="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦" if hosgeldin.get("kanal_id") else "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢", inline=True)
    embed.add_field(name="Karsilama", value="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦" if karsilama.get("kanal_id") else "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢", inline=True)
    embed.add_field(name="Guvenlik", value="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦" if guvenlik.get("aktif") else "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢", inline=True)
    embed.add_field(name="Jail", value="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦" if jail.get("aktif") else "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢", inline=True)
    embed.add_field(name="Partner", value="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦" if partner_kanal_id_al(ctx.guild.id) else "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢", inline=True)
    embed.add_field(name="Oto Cevap", value="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦" if _auto_cevap_ayar_al(ctx.guild.id).get("kayitlar") else "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢", inline=True)
    embed.add_field(name="Spam", value="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦" if _guild_ayar_al(ctx.guild.id).get("guvenlik_spam_koruma", {}).get("aktif") else "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢", inline=True)
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
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« Yasakli Komutlar Guncellendi", description=f"{kanal.mention} icin: {', '.join(sorted(mevcut)) or 'Yok'}", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


try:
    bot.remove_command("yardim")
    bot.remove_command("help")
    bot.remove_command("yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m")
except Exception:
    pass


@bot.command(name="yardim", aliases=["help", "yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m"])
async def yardim_canli(ctx):
    sahibi_id = ctx.author.id
    kategoriler = {
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Ayarlar": ["ticketpanel", "ticketkur", "levelkur", "hosgeldinkur", "karsilamakur", "guvenlikkur", "jailkur", "sayac", "kurulumdurum"],
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨ Moderasyon": ["ban", "blupbum", "kick", "mute", "unmute", "warn", "uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lar", "uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sil", "jail", "unjail", "temprol"],
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨ Roller": ["renkpanel", "rolmenu", "animerolpanel", "animerollerikur", "animerollerikaldir", "asagitasi"],
        "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Sistemler": ["gifcevap", "otocevap", "spam-koruma-kur", "spam-koruma-durum", "spam-koruma-muaf-rol", "spam-koruma-muaf-kanal", "kufur-kur", "yetkilikufurkur", "yasakli-komut"],
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ Kullanici": ["profil", "sunucu", "sunucupanel", "sesistatistik", "mesajistatistik", "isimgecmisi", "notekle", "cezagecmisi", "yetkilipanel"],
    }

    def ana_embed():
        embed = discord.Embed(
            title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¹Ã¢â‚¬Â  Blup Komut Menusu",
            description="Canli, renkli ve sade bir yardim menusu.\nAsagidaki menuden kategori secip komutlari inceleyebilirsin.",
            color=0xFF66C4,
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(
            name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€¦Ã‚Â  Kategoriler",
            value="\n".join(f"{k} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {len(v)} komut" for k, v in kategoriler.items()),
            inline=False
        )
        embed.add_field(
            name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Populer Komutlar",
            value="profil ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ ticketpanel ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ levelkur ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ gifcevap ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ jailkur ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ kurulumdurum",
            inline=False
        )
        embed.set_footer(text=f"{sum(len(v) for v in kategoriler.values())} komut ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")
        return embed

    def kategori_embed(baslik: str):
        renkler = [0xFF66C4, 0x5865F2, 0x57F287, 0xFEE75C, 0xED4245]
        komut_listesi = [f"ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¨ .{k}" for k in kategoriler.get(baslik, [])]
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
            secenekler = [discord.SelectOption(label=k.replace("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ", "").replace("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨ ", "").replace("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨ ", "").replace("ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â ", "").replace("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ ", ""), value=k, description=f"{len(v)} komut", emoji=k.split()[0]) for k, v in kategoriler.items()]
            super().__init__(placeholder="Bir kategori sec", options=secenekler, min_values=1, max_values=1)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            await interaction.response.edit_message(embed=kategori_embed(self.values[0]), view=view)

    class KisaYolSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label="Ana Menu", value="ana", emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â "),
                discord.SelectOption(label="Moderasyon", value="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨ Moderasyon", emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨"),
                discord.SelectOption(label="Sistemler", value="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Sistemler", emoji="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â"),
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


for _yardim_eski in ("yardim", "help", "yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m"):
    try:
        bot.remove_command(_yardim_eski)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["help", "yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m"])
async def yardim_renkli(ctx):
    sahibi_id = ctx.author.id

    komutlar = {}
    for komut in bot.commands:
        if komut.hidden:
            continue
        ad = komut.name
        if ad in {"yardim", "help", "yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m"}:
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
        "Ayarlar": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â",
        "Moderasyon": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨",
        "Roller": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨",
        "Sistemler": "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â",
        "Kullanici": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤",
        "Diger": "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¨",
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
        return "\n".join(f"{kategori_simgeleri.get(kategori, 'ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢')} .{k.name}" for k in liste[:25]) or "Komut bulunamadi."

    def ana_embed():
        embed = discord.Embed(
            title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¹Ã¢â‚¬Â  Blup Help Menusu",
            description="Kategorileri asagidan secerek komutlari goruntuleyebilirsin.",
            color=0x5865F2,
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(
            name="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¨ Kisa Ozet",
            value="\n".join(
                f"{kategori_simgeleri.get(k, 'ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢')} **{k}** ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {len(komutlar.get(k, []))} komut"
                for k in kategori_sirasi if komutlar.get(k)
            ),
            inline=False
        )
        embed.add_field(
            name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Hizli Baslangic",
            value=".profil ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ .ticketpanel ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ .levelkur ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ .gifcevap ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ .jailkur ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ .spam-koruma-durum",
            inline=False
        )
        embed.set_footer(text=f"Toplam {sum(len(v) for v in komutlar.values())} komut ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")
        return embed

    def kategori_embed(kategori: str):
        embed = discord.Embed(
            title=f"{kategori_simgeleri.get(kategori, 'ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¨')} {kategori} Komutlari",
            description=komut_satirlari(kategori),
            color=kategori_renkleri.get(kategori, 0x5865F2),
            timestamp=datetime.now(timezone.utc)
        )
        embed.set_footer(text=zaman_damgasi())
        return embed

    class KategoriSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label=k, value=k, description=f"{len(komutlar.get(k, []))} komut", emoji=kategori_simgeleri.get(k, "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¨"))
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
                discord.SelectOption(label="Ana Menu", value="ana", description="Baslangic ekranina don", emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â "),
                discord.SelectOption(label="Sistemler", value="Sistemler", description="Tum sistem komutlari", emoji="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â"),
                discord.SelectOption(label="Moderasyon", value="Moderasyon", description="Ceza ve yonetim komutlari", emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨"),
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
    eslesmeler = list(re.finditer(r"(\d+)\s*(g[uÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼]n|saat|dakika|saniye|sn|dk|g|h|m|s)\b", metin.lower()))
    if not eslesmeler:
        return 0, metin.strip()

    birimler = {
        "g": 86400, "gun": 86400, "gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼n": 86400,
        "h": 3600, "saat": 3600,
        "m": 60, "dk": 60, "dakika": 60,
        "s": 1, "sn": 1, "saniye": 1,
    }
    toplam = 0
    for eslesme in eslesmeler:
        adet = int(eslesme.group(1))
        birim = eslesme.group(2)
        toplam += adet * birimler.get(birim, 0)

    kalan = re.sub(r"(\d+)\s*(g[uÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼]n|saat|dakika|saniye|sn|dk|g|h|m|s)\b", "", metin, flags=re.IGNORECASE).strip()
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
        title="HoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ Geldin!",
        description=_sablon_doldur(ayar.get("mesaj", "HoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ geldin {member_mention}!"), uye),
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
        ayar.get("mesaj", "AramÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±za hoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ geldin {username}. Seninle birlikte {member_count} kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iyiz."),
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
        title=f"{hedef.display_name} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Profil",
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
    e.set_footer(text=f"{ctx.guild.name} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")
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


@bot.command(name="karsilamadurum", aliases=["karÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama-durum", "karsilama-durum"])
async def karsilama_durum(ctx):
    ayar = _karsilama_ayar_al(ctx.guild.id)
    kanal = ctx.guild.get_channel(ayar.get("kanal_id")) if ayar.get("kanal_id") else None
    e = discord.Embed(title="KarÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama MesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Sistemi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    e.add_field(name="Kanal", value=kanal.mention if kanal else "AyarlanmamÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸", inline=False)
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


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
#  MODAL TABANLI LEVEL / HOSGELDIN KURULUMU
# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

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
        default="AramÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±za hoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ geldin {username}. Seninle birlikte {member_count} kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸iyiz."
    )

    async def on_submit(self, interaction: discord.Interaction):
        kanal_id = _kanal_id_coz(self.kanal_id.value)
        if kanal_id is None:
            await interaction.response.send_message("GeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ersiz kanal ID girdin.", ephemeral=True)
            return

        kanal = interaction.guild.get_channel(kanal_id) if interaction.guild else None
        if not isinstance(kanal, discord.TextChannel):
            await interaction.response.send_message("Bu ID ile metin kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.", ephemeral=True)
            return

        ayar = _karsilama_ayar_al(interaction.guild.id)
        ayar["kanal_id"] = kanal.id
        ayar["mesaj"] = (self.mesaj.value or "").strip()
        _karsilama_ayar_kaydet(interaction.guild.id, ayar)

        await interaction.response.send_message(
            f"KarÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± sistemi kaydedildi.\nKanal: {kanal.mention}",
            ephemeral=True
        )

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        try:
            if interaction.response.is_done():
                await interaction.followup.send(f"KarÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama modal hatasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±: {error}", ephemeral=True)
            else:
                await interaction.response.send_message(f"KarÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama modal hatasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±: {error}", ephemeral=True)
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
            title="GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlik Sistemi Kaydedildi",
            description="Sunucu koruma limitleri modal ile baÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸arÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±yla kaydedildi.",
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


@bot.command(name="karsilamakur", aliases=["karÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama-kur", "karsilama-kur"])
@commands.has_permissions(manage_guild=True)
async def karsilama_kur_modal(ctx):
    e = discord.Embed(
        title="KarÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama MesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Kurulumu",
        description="AÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸aÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±daki butona tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±kla; etiket atmayan karÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± modal ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼zerinden kur.",
        color=RENKLER["bilgi"]
    )
    await ctx.send(embed=e, view=_KurulumView("karsilama"))


@bot.command(name="guvenlikkur", aliases=["gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlikkur"])
@commands.has_permissions(administrator=True)
async def guvenlik_kur_modal(ctx):
    e = discord.Embed(
        title="GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlik Sistemi Kurulumu",
        description=(
            "Asagidaki butona tikla ve limitleri modal uzerinden ayarla.\n"
            "Yazdigin limit sayisina ulasilinca kullanici direkt jaile atilir."
        ),
        color=RENKLER["bilgi"]
    )
    await ctx.send(embed=e, view=_KurulumView("guvenlik"))


@bot.command(name="guvenlikdurum", aliases=["gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlikdurum"])
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
        title="GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlik Sistemi",
        color=RENKLER["bilgi"],
        timestamp=datetime.now(timezone.utc)
    )
    e.add_field(name="Durum", value="Aktif" if ayar.get("aktif") else "KapalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", inline=True)
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


@bot.command(name="guvenlikkapat", aliases=["gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlikkapat"])
@commands.has_permissions(administrator=True)
async def guvenlik_kapat(ctx):
    ayar = _guvenlik_ayar_al(ctx.guild.id)
    ayar["aktif"] = False
    _guvenlik_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(embed=discord.Embed(
        title="GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlik Sistemi KapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        description="Sunucu guvenlik limitleri devre disi birakildi.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    ))


@bot.command(name="guvenlikizin", aliases=["gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlikizin", "guvenlik-whitelist"])
@commands.has_permissions(administrator=True)
async def guvenlik_izin_ekle(ctx, hedef = None):
    if hedef is None:
        await ctx.send("KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.guvenlikizin @uye` veya `.guvenlikizin @rol`")
        return
    hedef_obj = None
    if ctx.message.role_mentions:
        hedef_obj = ctx.message.role_mentions[0]
    elif ctx.message.mentions:
        hedef_obj = ctx.message.mentions[0]
    if hedef_obj is None:
        await ctx.send("LÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼tfen bir ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye veya rol etiketle.")
        return
    ayar = _guvenlik_ayar_al(ctx.guild.id)
    whitelist = list(dict.fromkeys((ayar.get("whitelist_ids", []) or []) + [hedef_obj.id]))
    ayar["whitelist_ids"] = whitelist
    _guvenlik_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(embed=discord.Embed(
        title="Whitelist GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ncellendi",
        description=f"{hedef_obj.mention} gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlik whitelist listesine eklendi.",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    ))


@bot.command(name="guvenlikizinsil", aliases=["gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlikizinsil", "guvenlik-whitelist-sil"])
@commands.has_permissions(administrator=True)
async def guvenlik_izin_sil(ctx, hedef = None):
    if hedef is None:
        await ctx.send("KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m: `.guvenlikizinsil @uye` veya `.guvenlikizinsil @rol`")
        return
    hedef_obj = None
    if ctx.message.role_mentions:
        hedef_obj = ctx.message.role_mentions[0]
    elif ctx.message.mentions:
        hedef_obj = ctx.message.mentions[0]
    if hedef_obj is None:
        await ctx.send("LÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼tfen bir ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ye veya rol etiketle.")
        return
    ayar = _guvenlik_ayar_al(ctx.guild.id)
    ayar["whitelist_ids"] = [x for x in (ayar.get("whitelist_ids", []) or []) if x != hedef_obj.id]
    _guvenlik_ayar_kaydet(ctx.guild.id, ayar)
    await ctx.send(embed=discord.Embed(
        title="Whitelist GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ncellendi",
        description=f"{hedef_obj.mention} whitelist listesinden ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±karÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
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
        await ctx.send("HoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸geldin sistemi iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in kanal ayarlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸il. `.hosgeldinkur` ile ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nce kurulum yap.")
        return
    if not isinstance(kanal, discord.TextChannel):
        await ctx.send("AyarlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± hoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸geldin kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±. `.hosgeldinkur` ile sistemi tekrar kur.")
        return
    try:
        ust_metin, e = _hosgeldin_icerigi_hazirla(hedef, ayar)
        e.title = "HoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ Geldin! (Test)"
        await kanal.send(ust_metin, embed=e)
    except discord.Forbidden:
        await ctx.send("Test mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderilemedi; botun hoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸geldin kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nda yazma yetkisi yok.")
        return
    except Exception as e:
        await ctx.send(f"HoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸geldin test mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± oluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turulurken hata oldu: {e}")
        return

    await ctx.send(f"HoÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸geldin test mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± {kanal.mention} kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderildi.", delete_after=8)


@bot.command(name="karsilamatest", aliases=["karÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama-test", "karsilama-test"])
@commands.has_permissions(manage_guild=True)
async def karsilama_test(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    ayar = _karsilama_ayar_al(ctx.guild.id)
    kanal_id = ayar.get("kanal_id")
    kanal = ctx.guild.get_channel(kanal_id) if kanal_id else None

    if not kanal_id:
        await ctx.send("KarÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama sistemi iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in kanal ayarlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± deÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸il. `.karsilamakur` ile ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nce kurulum yap.")
        return
    if not isinstance(kanal, discord.TextChannel):
        await ctx.send("AyarlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± karÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±. `.karsilamakur` ile sistemi tekrar kur.")
        return

    try:
        mesaj = _karsilama_mesaji_hazirla(hedef, ayar)
        baslikli_mesaj = f"**KarÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama MesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± (Test)**\n{mesaj}"
        dosya = await hedef.display_avatar.to_file(filename="karsilama-avatar.png") if hedef.display_avatar else None
        if dosya:
            await kanal.send(baslikli_mesaj, file=dosya)
        else:
            await kanal.send(baslikli_mesaj)
    except discord.Forbidden:
        await ctx.send("Test mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderilemedi; botun karÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nda yazma yetkisi yok.")
        return
    except Exception as e:
        await ctx.send(f"KarÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama test mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± oluÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸turulurken hata oldu: {e}")
        return

    await ctx.send(f"KarÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama test mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± {kanal.mention} kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nderildi.", delete_after=8)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Partner Koruma Sistemleri ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

# Everyone/Here korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in veri deposu
_everyone_here_log = {}
# Spam korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in veri deposu (mesaj iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§erikli)
_spam_log = {}

@bot.event
async def on_message(message):
    # Bot mesajlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ignore et
    if message.author.bot:
        return
    
    # Mevcut event handler'larÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§alÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r
    try:
        await bot.process_commands(message)
    except:
        pass
    
    # Genel gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlik sistemleri
    ayarlar = ayarlari_yukle()
    gk = str(message.guild.id)
    sunucu_ayari = ayarlar.get(gk, {})

    # Partner kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼
    partner_ch_id = partner_kanal_id_al(message.guild.id)
    if partner_ch_id and message.channel.id == partner_ch_id:
        eslesen = DAVET_REGEX.search(message.content)

        if not eslesen:
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            uyari = await message.channel.send(embed=discord.Embed(
                title="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ GeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ersiz Partner Metni",
                description=f"{message.author.mention} MesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±zda Discord davet linki bulunamadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±. MesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±z silindi.",
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

        # 1 saat bekleme kontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼
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
                        title="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â³ Bekleme SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼resi DolmadÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                        description=(
                            f"{message.author.mention} Bu sunucuyla tekrar partner yapmak iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in\n"
                            f"**{kalan // 60} dakika {kalan % 60} saniye** beklemeniz gerekiyor.\n"
                            f"Son partner: <@{onceki_id}> tarafÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan yapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±."
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
            title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤Ãƒâ€šÃ‚Â Yeni Partner YapÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±!",
            description=f"{message.author.mention} yeni bir partnerlik yaptÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±!",
            color=0x57F287,
            timestamp=simdi
        )
        stats_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Sunucu SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"**#{sira}**", inline=True)
        stats_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ Yetkili SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"**#{yetkili_sira}** ({yetkili_toplam} partnerlik)", inline=True)
        stats_embed.add_field(
            name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¢Ãƒâ€šÃ‚Â Zamana DayalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±:",
            value=(
                f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Âº GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nlÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼k: **{stats['gunluk']}**\n"
                f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Âº HaftalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k: **{stats['haftalik']}**\n"
                f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Âº AylÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k: **{stats['aylik']}**"
            ),
            inline=True
        )
        stats_embed.add_field(name="ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Toplam", value=f"**{stats['toplam']}**", inline=True)
        stats_embed.set_footer(text=f"{bot.user.name} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Partner Sistemi")
        if message.guild.icon:
            stats_embed.set_thumbnail(url=message.guild.icon.url)
        await message.channel.send(embed=stats_embed)

        log_kanal_id = partner_log_kanali_al(message.guild.id)
        if log_kanal_id:
            log_kanal = message.guild.get_channel(log_kanal_id)
            if log_kanal:
                log_embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Partner Logu", color=0x57F287, timestamp=simdi)
                log_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Davet", value=f"`{davet_kodu}`", inline=True)
                log_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ Yapan", value=message.author.mention, inline=True)
                log_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Zaman", value=simdi.strftime("%d.%m.%Y %H:%M UTC"), inline=True)
                log_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Toplam", value=str(stats["toplam"]), inline=True)
                log_embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ Yetkili ToplamÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=str(yetkili_toplam), inline=True)
                log_embed.set_footer(text=zaman_damgasi())
                await log_kanal.send(embed=log_embed)
        return

    # KÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±
    if kufur_kontrol(message.guild.id, message.content):
        try:
            await message.delete()
            
            # Embed uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nder
            embed = discord.Embed(
                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« KÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r Yasak",
                description=f"{message.author.mention} KÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± yasaktÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r!",
                color=0xFF6B6B,
                timestamp=datetime.now(timezone.utc)
            )
            await message.channel.send(embed=embed, delete_after=5)
            
            # Log gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nder (varsa)
            log_kanal_id = sunucu_ayari.get("guvenlik_log")
            if log_kanal_id:
                log_kanal = message.guild.get_channel(log_kanal_id)
                if log_kanal:
                    embed = discord.Embed(
                        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« KÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                        description=f"{message.author.mention} kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼rlÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ mesaj attÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
                        color=0xFF6B6B,
                        timestamp=datetime.now(timezone.utc)
                    )
                    embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"{message.author} ({message.author.id})", inline=True)
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

    # Genel spam korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±
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
        
            # KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n mesaj geÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§miÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ini kontrol et
            if user_id not in _spam_log:
                _spam_log[user_id] = []
        
            _spam_log[user_id].append((now, mesaj_icerik))
        
            # Eski mesajlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± temizle (1 saatten eski olanlar)
            _spam_log[user_id] = [(t, m) for t, m in _spam_log[user_id] if now - t < 3600]
        
            # AynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± mesaj spam kontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼
            max_ayni_mesaj = spam_ayar.get("max_ayni_mesaj", 3)
            zaman_araligi = spam_ayar.get("zaman_araligi", 10)
        
            # Son zaman aralÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndaki aynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± mesajlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± say
            son_mesajlar = [(t, m) for t, m in _spam_log[user_id] if now - t < zaman_araligi]
            ayni_mesaj_sayisi = sum(1 for t, m in son_mesajlar if m == mesaj_icerik)
        
            if ayni_mesaj_sayisi > max_ayni_mesaj:
                try:
                    # Timeout uygula
                    mute_suresi = spam_ayar.get("mute_suresi", 300)  # 5 dakika
                
                    await message.author.timeout(timedelta(seconds=mute_suresi), reason="AynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± mesaj spam korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± - Genel gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlik")
                
                    # Embed bildirim gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nder
                    embed = discord.Embed(
                        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ Spam CezasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                        description=f"{message.author.mention} aynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± tekrarladÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in susturuldu!",
                        color=0xFF9500,
                        timestamp=datetime.now(timezone.utc)
                    )
                    embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"{message.author} ({message.author.id})", inline=True)
                    embed.add_field(name="SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re", value=f"{mute_suresi//60} dakika", inline=True)
                    embed.add_field(name="Sebep", value=f"{zaman_araligi} saniyede aynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± mesaj {ayni_mesaj_sayisi} kez", inline=False)
                    await message.channel.send(embed=embed, delete_after=10)
                
                    # Log gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nder
                    log_kanal_id = sunucu_ayari.get("guvenlik_log")
                    if log_kanal_id:
                        log_kanal = message.guild.get_channel(log_kanal_id)
                        if log_kanal:
                            embed = discord.Embed(
                                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¡ Spam CezasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                                description=f"{message.author.mention} aynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± tekrarladÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in susturuldu.",
                                color=0xFF9500,
                                timestamp=datetime.now(timezone.utc)
                            )
                            embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"{message.author} ({message.author.id})", inline=True)
                            embed.add_field(name="SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼re", value=f"{mute_suresi//60} dakika", inline=True)
                            embed.add_field(name="Sebep", value=f"{zaman_araligi} saniyede aynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± mesaj {ayni_mesaj_sayisi} kez", inline=False)
                            embed.add_field(name="Mesaj", value=f"```{message.content[:100]}...```" if len(message.content) > 100 else f"```{message.content}```", inline=False)
                            await log_kanal.send(embed=embed)
                except discord.Forbidden:
                    pass
    
    # Genel link korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±
    link_ayar = sunucu_ayari.get("guvenlik_link_koruma", {})
    if link_ayar.get("aktif", False):
        # Muaf kontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼
        muaf_roller = link_ayar.get("muaf_roller", [])
        muaf_kanallar = link_ayar.get("muaf_kanallar", [])
        
        # KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± muaf mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±?
        kullanici_muaf = any(role.id in muaf_roller for role in message.author.roles)
        
        # Kanal muaf mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±?
        kanal_muaf = message.channel.id in muaf_kanallar
        
        if not kullanici_muaf and not kanal_muaf:
            # Link kontrolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ (basit regex)
            import re
            link_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
            if re.search(link_pattern, message.content):
                try:
                    await message.delete()
                    
                    # Embed hata mesajÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±
                    embed = discord.Embed(
                        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« Link PaylaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Yasak",
                        description=f"{message.author.mention} Link paylaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± yasaktÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r!",
                        color=0xFF6B6B,
                        timestamp=datetime.now(timezone.utc)
                    )
                    await message.channel.send(embed=embed, delete_after=5)
                    
                    # Log gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶nder
                    log_kanal_id = sunucu_ayari.get("guvenlik_log")
                    if log_kanal_id:
                        log_kanal = message.guild.get_channel(log_kanal_id)
                        if log_kanal:
                            embed = discord.Embed(
                                title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« Link PaylaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                                description=f"{message.author.mention} kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± link paylaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
                                color=0xFF6B6B,
                                timestamp=datetime.now(timezone.utc)
                            )
                            embed.add_field(name="KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"{message.author} ({message.author.id})", inline=True)
                            embed.add_field(name="Kanal", value=message.channel.mention, inline=True)
                            embed.add_field(name="Mesaj", value=f"```{message.content[:100]}...```" if len(message.content) > 100 else f"```{message.content}```", inline=False)
                            await log_kanal.send(embed=embed)
                except discord.Forbidden:
                    pass
    
    # ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Genel GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlik KomutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Modal SÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±flarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬
class SpamModal(discord.ui.Modal, title="Spam Koruma Ayarlari"):
    max_ayni_mesaj = discord.ui.TextInput(
        label="Maksimum AynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Mesaj",
        placeholder="ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“rn: 3 (10 saniyede aynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± mesajdan en fazla 3 kez)",
        style=discord.TextStyle.short,
        required=True,
        default="3"
    )
    zaman_araligi = discord.ui.TextInput(
        label="Zaman AralÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± (saniye)",
        placeholder="ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“rn: 10",
        style=discord.TextStyle.short,
        required=True,
        default="10"
    )
    mute_suresi = discord.ui.TextInput(
        label="Mute SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼resi (saniye)",
        placeholder="ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“rn: 300 (5 dakika)",
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
                title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Spam Koruma AyarlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
                description="Spam yapan kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lara otomatik timeout uygulanacak.",
                color=RENKLER["basari"],
                timestamp=datetime.now(timezone.utc)
            )
            embed.add_field(name="Max AynÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Mesaj", value=f"**{max_msg}** mesaj", inline=True)
            embed.add_field(name="Zaman AralÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", value=f"**{zaman}** saniye", inline=True)
            embed.add_field(name="Mute SÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼resi", value=f"**{sure//60}** dakika", inline=True)
            
            await interaction.response.send_message(embed=embed, ephemeral=True)
            
        except ValueError:
            await interaction.response.send_message("LÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼tfen tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m alanlara geÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§erli sayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lar girin!", ephemeral=True)

class SpamModalView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Modal AÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§", style=discord.ButtonStyle.primary)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = SpamModal()
        await interaction.response.send_modal(modal)

class LinkModal(discord.ui.Modal, title="Link Koruma Ayarlari"):
    aktif_mi = discord.ui.TextInput(
        label="Link Koruma Aktif? (evet/hayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r)",
        placeholder="ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“rn: evet",
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
        
        aktif = self.aktif_mi.value.lower() in ["evet", "aktif", "true", "1", "aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§"]
        sunucu_ayari["guvenlik_link_koruma"]["aktif"] = aktif
        
        if "muaf_roller" not in sunucu_ayari["guvenlik_link_koruma"]:
            sunucu_ayari["guvenlik_link_koruma"]["muaf_roller"] = []
        if "muaf_kanallar" not in sunucu_ayari["guvenlik_link_koruma"]:
            sunucu_ayari["guvenlik_link_koruma"]["muaf_kanallar"] = []
        
        ayarlari_kaydet(ayarlar)
        
        embed = discord.Embed(
            title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Link Koruma AyarlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
            description=f"Link korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± {'aktif' if aktif else 'pasif'} durumuna ayarlandÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.\n\nMuaf roller eklemek iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in: `.link-koruma-muaf-rol @rol`\nMuaf kanallar eklemek iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in: `.link-koruma-muaf-kanal #kanal`",
            color=RENKLER["basari"] if aktif else RENKLER["hata"],
            timestamp=datetime.now(timezone.utc)
        )
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

class LinkModalView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    
    @discord.ui.button(label="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Modal AÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§", style=discord.ButtonStyle.primary)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = LinkModal()
        await interaction.response.send_modal(modal)


# ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Genel GÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼venlik KomutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬

@bot.command(name="spam-koruma-kur")
@commands.has_permissions(manage_guild=True)
async def spam_koruma_kur(ctx):
    """Genel spam korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± modal ile kurar."""
    await ctx.send("Modal aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§mak iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in butona tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±klayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n:", view=SpamModalView())


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
    """Genel link korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± modal ile kurar."""
    await ctx.send("Modal aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§mak iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in butona tÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±klayÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n:", view=LinkModalView())

@bot.command(name="link-koruma-aktif")
@commands.has_permissions(manage_guild=True)
async def link_koruma_aktif(ctx):
    """Genel link korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± aktif eder."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.setdefault(gk, {})
    
    if "guvenlik_link_koruma" not in sunucu_ayari:
        sunucu_ayari["guvenlik_link_koruma"] = {}
    
    sunucu_ayari["guvenlik_link_koruma"]["aktif"] = True
    ayarlari_kaydet(ayarlar)
    
    embed = discord.Embed(
        title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Genel Link Koruma Aktif",
        description="TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m kanallarda link paylaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± engellendi (muaf olanlar hariÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§).",
        color=RENKLER["basari"],
        timestamp=datetime.now(timezone.utc)
    )
    await ctx.send(embed=embed)

@bot.command(name="link-koruma-kapat")
@commands.has_permissions(manage_guild=True)
async def link_koruma_kapat(ctx):
    """Genel link korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±nÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± kapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±r."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.setdefault(gk, {})
    
    if "guvenlik_link_koruma" in sunucu_ayari:
        sunucu_ayari["guvenlik_link_koruma"]["aktif"] = False
        ayarlari_kaydet(ayarlar)
    
    embed = discord.Embed(
        title="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Genel Link Koruma KapatÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±",
        description="Link paylaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±mÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± serbest bÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±rakÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ldÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    )
    await ctx.send(embed=embed)

@bot.command(name="link-koruma-muaf-rol")
@commands.has_permissions(manage_guild=True)
async def link_koruma_muaf_rol(ctx, rol: discord.Role):
    """Link korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan muaf rol ekler."""
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
            title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Muaf Rol Eklendi",
            description=f"{rol.mention} rolÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ link korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan muaf tutuldu.",
            color=RENKLER["basari"],
            timestamp=datetime.now(timezone.utc)
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu rol zaten muaf listesinde!")

@bot.command(name="link-koruma-muaf-kanal")
@commands.has_permissions(manage_guild=True)
async def link_koruma_muaf_kanal(ctx, kanal: discord.TextChannel):
    """Link korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan muaf kanal ekler."""
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
            title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Muaf Kanal Eklendi",
            description=f"{kanal.mention} kanalÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± link korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ndan muaf tutuldu.",
            color=RENKLER["basari"],
            timestamp=datetime.now(timezone.utc)
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send("Bu kanal zaten muaf listesinde!")

@bot.command(name="link-koruma-durum")
@commands.has_permissions(manage_guild=True)
async def link_koruma_durum(ctx):
    """Genel link koruma durumunu gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶sterir."""
    ayarlar = ayarlari_yukle()
    gk = str(ctx.guild.id)
    sunucu_ayari = ayarlar.get(gk, {})
    link_ayar = sunucu_ayari.get("guvenlik_link_koruma", {})
    
    embed = discord.Embed(
        title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Genel Link Koruma Durumu",
        color=0x5865F2,
        timestamp=datetime.now(timezone.utc)
    )
    
    durum = "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Aktif" if link_ayar.get("aktif", False) else "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Pasif"
    embed.add_field(name="Durum", value=durum, inline=True)
    
    muaf_roller = link_ayar.get("muaf_roller", [])
    muaf_kanallar = link_ayar.get("muaf_kanallar", [])
    
    if muaf_roller:
        roller_text = "\n".join([f"<@&{rid}>" for rid in muaf_roller[:5]])
        if len(muaf_roller) > 5:
            roller_text += f"\n...ve {len(muaf_roller)-5} rol daha"
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â­ Muaf Roller", value=roller_text or "Yok", inline=False)
    
    if muaf_kanallar:
        kanallar_text = "\n".join([f"<#{kid}>" for kid in muaf_kanallar[:5]])
        if len(muaf_kanallar) > 5:
            kanallar_text += f"\n...ve {len(muaf_kanallar)-5} kanal daha"
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¢ Muaf Kanallar", value=kanallar_text or "Yok", inline=False)
    
    await ctx.send(embed=embed)


bot.remove_command("kufur-temizle")


@bot.command(name="kufur-temizle")
@commands.has_permissions(administrator=True)
async def kufur_temizle_v2(ctx):
    guild_key = str(ctx.guild.id)
    ayarlar = ayarlari_yukle()
    if guild_key not in ayarlar or not ayarlar[guild_key].get("yasakli_kelimeler"):
        await ctx.send("Bu sunucuda zaten kÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼fÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼r korumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± ayarlanmamÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸.")
        return
    ayarlar[guild_key]["yasakli_kelimeler"] = []
    ayarlari_kaydet(ayarlar)
    await ctx.send(embed=discord.Embed(
        title="Kufur KorumasÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Temizlendi",
        description="Tum yasak kelimeler silindi ve kufur korumasi kapatildi.",
        color=RENKLER["hata"],
        timestamp=datetime.now(timezone.utc)
    ))


class GifCevapModal(discord.ui.Modal, title="GIF Cevap Kurulumu"):
    anahtar = discord.ui.TextInput(label="Anahtar Kelime", placeholder="ornek: gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼naydÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±n", required=True, max_length=100)
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
        await interaction.followup.send(f"Jail sistemi kaydedildi. Kanal: {kanal.mention} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Jail Rol: {jail_rol.mention}", ephemeral=True)


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


for _eski in ("yardim", "help", "yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m", "ban"):
    try:
        bot.remove_command(_eski)
    except Exception:
        pass


def _komut_sahibi_degisebilir_mi(interaction: discord.Interaction, sahibi_id: int) -> bool:
    return interaction.user.id == sahibi_id


@bot.command(name="yardim", aliases=["yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m", "help"])
async def yardim_final(ctx):
    komutlar = _yardim_komutlarini_topla()
    sistem_haritasi = _yardim_sistem_haritasi()
    sahibi_id = ctx.author.id

    def temel_embed(baslik: str, aciklama: str) -> discord.Embed:
        embed = discord.Embed(
            title=f"Komut Paneli ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {baslik}",
            description=aciklama,
            color=0x20253A,
            timestamp=datetime.now(timezone.utc)
        )
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
            embed.set_author(name=f"{ctx.guild.name} Komutlar", icon_url=ctx.guild.icon.url)
        else:
            embed.set_author(name=f"{ctx.guild.name} Komutlar")
        embed.set_footer(text=f"Toplam {sum(len(v) for v in komutlar.values())} komut ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Secici menu aktif")
        return embed

    def ana_embed():
        embed = temel_embed("Ana Menu", "Asagidaki secicilerle kategorileri ve sistemleri gezebilirsin.")
        kategori_ozet = [f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ **{kategori}** `({len(kayitlar)})`" for kategori, kayitlar in komutlar.items() if kayitlar]
        embed.add_field(name="Kategoriler", value="\n".join(kategori_ozet[:8]) or "-", inline=True)
        sistem_ozet = []
        for sistem, adlar in sistem_haritasi.items():
            sayi = sum(1 for liste in komutlar.values() for kayit in liste if kayit["ad"] in adlar)
            sistem_ozet.append(f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ **{sistem}** `({sayi})`")
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
    embed = mod_embed("Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨ Uye Banlandi", RENKLER["ban"], **{
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ Hedef": hedef_yazi,
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Sebep": sebep,
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Yetkili": ctx.author.mention
    })
    await ctx.send(embed=embed)
    await log_gonder(ctx.guild, "ban_log", embed)


for _eski_help in ("yardim", "help", "yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m"):
    try:
        bot.remove_command(_eski_help)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m", "help"])
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
        embed.add_field(name="Kategoriler", value=" ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ ".join(kategori_ozet[:8]) or "-", inline=False)
        embed.add_field(name="Sistemler", value=" ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ ".join(sistem_ozet[:7]) or "-", inline=False)
        embed.add_field(name="Hizli Baslangic", value=".profil ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ .ticketpanel ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ .levelkur ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ .gifcevap ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ .jailkur", inline=False)
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
    return "Bot ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§alÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±yor"

def run_flask():
    port = int(os.environ.get("PORT", 10000))  # Render iÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§in 10000
    app.run(host="0.0.0.0", port=port)

Thread(target=run_flask).start()


if __name__ == "__main__":
    pass


for _eski_help2 in ("yardim", "help", "yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m"):
    try:
        bot.remove_command(_eski_help2)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m", "help"])
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
        "Eglence": "m:eÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸lence",
        "Slash": "m:slash",
        "Diger": "m:komutlar",
    }
    kategori_renkleri = {
        "Ayarlar": "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Âº",
        "Moderasyon": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â©",
        "Roller": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¥",
        "Sistemler": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¦",
        "Kullanici": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Âª",
        "Eglence": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¨",
        "Slash": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§",
        "Diger": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¹Ã¢â‚¬Â ",
    }
    sistem_gosterimleri = {
        "Log": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â¾ log",
        "Ticket": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€¦Ã‚Â¸ destek",
        "Partner": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤Ãƒâ€šÃ‚Â partner",
        "Level": "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ /rank",
        "Hosgeldin": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° karÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lama",
        "Guvenlik": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ koruma",
        "Rol Panelleri": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨ roller",
        "Eglence": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€¦Ã‚Â  ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸",
        "Moderasyon": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨ mod",
    }
    kullanici_sistemleri = [
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ profil",
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  seviye",
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ afk",
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â  sunucu",
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ekiliÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸",
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¼ gifcevap",
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ jail",
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â¹ rolidler",
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
        embed.set_footer(text=f"Toplam {sum(len(v) for v in komutlar.values())} komut ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")
        return embed

    def ana_embed():
        embed = temel_embed("Marpel Komutlar")
        kategori_satirlari = []
        toplam = sum(len(v) for v in komutlar.values())
        kategori_satirlari.append(f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¹Ã¢â‚¬Â  **m:komutlar** ({toplam})")
        for kategori in kategori_sirasi:
            if komutlar.get(kategori):
                kategori_satirlari.append(f"{kategori_renkleri.get(kategori, 'ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Ãƒâ€šÃ‚Â«ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â')} **{kategori_etiketleri.get(kategori, kategori.lower())}** ({len(komutlar[kategori])})")
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¹ Kategoriler", value="\n".join(kategori_satirlari[:6]), inline=True)
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“", value="ÃƒÆ’Ã‚Â£ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦Ãƒâ€šÃ‚Â¤", inline=True)

        sol = []
        for sistem in ["Eglence", "Guvenlik", "Log", "Ticket", "Rol Panelleri"]:
            if sistem in sistem_gosterimleri:
                sol.append(sistem_gosterimleri[sistem])
        sag = kullanici_sistemleri
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â  Sistemler", value="\n".join(sol[:8]), inline=True)
        embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¥ KullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±cÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± Sistemleri", value="\n".join(sag[:8]), inline=True)
        return embed

    def detay_embed(baslik: str, kayitlar: list[dict], aciklama: str):
        embed = temel_embed(f"Marpel Komutlar", aciklama)
        embed.add_field(name=baslik, value="\n\n".join(_yardim_parcalari(_yardim_komut_metni(kayitlar), limit=850)[:3]) or "Komut bulunamadi.", inline=False)
        return embed

    class KategoriSec(discord.ui.Select):
        def __init__(self):
            secenekler = []
            tum = sum(len(v) for v in komutlar.values())
            secenekler.append(discord.SelectOption(label="TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m Komutlar", value="__tum__", description=f"{tum} komut"))
            for kategori in kategori_sirasi:
                if komutlar.get(kategori):
                    secenekler.append(discord.SelectOption(
                        label=kategori,
                        value=kategori,
                        description=f"{len(komutlar[kategori])} komut",
                        emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â"
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
                await interaction.response.edit_message(embed=detay_embed("TÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m Komutlar", tum, "Sunucudaki tÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼m aktif komutlar."), view=view)
                return
            await interaction.response.edit_message(embed=detay_embed(self.values[0], komutlar.get(self.values[0], []), "SeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§tiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸in kategorideki komutlar."), view=view)

    class SistemSec(discord.ui.Select):
        def __init__(self):
            secenekler = [discord.SelectOption(label=sistem, value=sistem, description="Sistem komutlarini gosterir", emoji="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â") for sistem in sistem_haritasi]
            super().__init__(placeholder="Sistemler", min_values=1, max_values=1, options=secenekler, row=2)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menuyu sadece komutu yazan kisi kullanabilir.", ephemeral=True)
                return
            kayitlar = []
            for liste in komutlar.values():
                kayitlar.extend([kayit for kayit in liste if kayit["ad"] in sistem_haritasi.get(self.values[0], set())])
            kayitlar.sort(key=lambda x: x["gosterim"])
            await interaction.response.edit_message(embed=detay_embed(f"{self.values[0]} Sistemi", kayitlar, "SeÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§tiÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸in sistemle ilgili komutlar."), view=view)

    class YardimMenuSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label="Ana MenÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼", value="ana", description="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°lk gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ aÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§"),
                discord.SelectOption(label="HÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±zlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± BaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸langÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§", value="hizli", description="En sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lan komutlar"),
            ]
            super().__init__(placeholder="YardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m MenÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼", min_values=1, max_values=1, options=secenekler, row=3)

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
            await interaction.response.edit_message(embed=detay_embed("HÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±zlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± BaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸langÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§", hizli, "En sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±k kullanÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lan kurulum komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±."), view=view)

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


for _yardim_sil in ("yardim", "yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m", "help"):
    try:
        bot.remove_command(_yardim_sil)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m", "help"])
async def yardim_final_renkli(ctx):
    sahibi_id = ctx.author.id

    kategoriler = {
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Ayarlar": [
            "ticketkur", "ticketpanel", "levelkur", "hosgeldinkur", "karsilamakur",
            "guvenlikkur", "jailkur", "sayac", "kurulumdurum", "butunsistemlerikaldir"
        ],
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨ Moderasyon": [
            "ban", "blupbum", "kick", "mute", "unmute", "warn", "uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±lar",
            "uyarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sil", "jail", "unjail", "temprol", "kanalkilit", "kanalac"
        ],
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨ Roller": [
            "renkpanel", "rolmenu", "animerolpanel", "animerollerikur",
            "animerollerikaldir", "asagitasi", "rolidler"
        ],
        "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Sistemler": [
            "gifcevap", "otocevap", "spam-koruma-kur", "spam-koruma-durum",
            "spam-koruma-muaf-rol", "spam-koruma-muaf-kanal", "kufur-kur",
            "yetkilikufurkur", "yasakli-komut", "link-koruma-kur"
        ],
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ Bilgi": [
            "profil", "sunucu", "sunucupanel", "sesistatistik", "mesajistatistik",
            "isimgecmisi", "notekle", "notlar", "notsil", "cezagecmisi",
            "yetkilipanel", "komutbilgi", "avatar", "banner", "say"
        ],
        "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° Extra": [
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
            title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¹Ã¢â‚¬Â  Blup Komut MenÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼",
            description="Daha canlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±, daha sade ve daha rahat okunur bir yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m ekranÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±.\nAÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸aÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±dan kategori seÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§erek komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ntÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼leyebilirsin.",
            color=0xFF66C4,
            timestamp=datetime.now(timezone.utc)
        )
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.add_field(
            name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€¦Ã‚Â  Kategoriler",
            value="\n".join(f"{kategori} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ **{len(komutlar)}** komut" for kategori, komutlar in kategoriler.items() if komutlar),
            inline=False
        )
        embed.add_field(
            name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ HÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±zlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± BaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸langÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§",
            value="profil ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ ticketpanel ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ levelkur ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ gifcevap ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ jailkur ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ kurulumdurum",
            inline=False
        )
        embed.add_field(
            name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢Ãƒâ€šÃ‚Â¡ Not",
            value="Bu menÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼de kod yazÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±sÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶rÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ yok; komutlar normal yazÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼zeninde gÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶sterilir.",
            inline=False
        )
        embed.set_footer(text=f"Toplam {sum(len(v) for v in kategoriler.values())} komut ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ {zaman_damgasi()}")
        return embed

    def kategori_embed(kategori):
        komutlar = kategoriler.get(kategori, [])
        embed = discord.Embed(
            title=f"{kategori}",
            description="\n".join(f"ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¨ .{komut}" for komut in komutlar) or "Komut bulunamadi.",
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
            super().__init__(placeholder="Bir kategori seÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ sadece komutu yazan kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i kullanabilir.", ephemeral=True)
                return
            await interaction.response.edit_message(embed=kategori_embed(self.values[0]), view=view)

    class HizliSec(discord.ui.Select):
        def __init__(self):
            secenekler = [
                discord.SelectOption(label="Ana MenÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼", value="ana", description="BaÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸langÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ ekranÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±na dÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¶n", emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â "),
                discord.SelectOption(label="Moderasyon", value="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨ Moderasyon", description="Ceza komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¨"),
                discord.SelectOption(label="Sistemler", value="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Sistemler", description="Kurulum komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", emoji="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â"),
                discord.SelectOption(label="Bilgi", value="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ Bilgi", description="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â°statistik ve bilgi komutlarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤"),
            ]
            super().__init__(placeholder="HÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±zlÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â± geÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§iÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸", min_values=1, max_values=1, options=secenekler)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != sahibi_id:
                await interaction.response.send_message("Bu menÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ sadece komutu yazan kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i kullanabilir.", ephemeral=True)
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
                await interaction.response.send_message("Bu menÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼yÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¼ sadece komutu yazan kiÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€¦Ã‚Â¸i kullanabilir.", ephemeral=True)
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
        satirlar.append(f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ **{yazan.display_name if yazan else 'Bilinmiyor'}:** {kayit.get('metin', '')}")
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Uye Notlari", description="\n".join(satirlar) or "Kayitli not yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
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
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â¹ Uye Notlari Silindi", description=f"{uye.mention} icin notlar temizlendi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


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
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â½ Ceza Gecmisi Temizlendi", description=f"{uye.mention} icin warn kayitlari temizlendi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="otorol")
@commands.has_permissions(manage_roles=True)
async def otorol(ctx, rol: discord.Role = None):
    if not rol:
        ayar = _otorol_ayar_al(ctx.guild.id)
        aktif_rol = ctx.guild.get_role(int(ayar.get("rol_id", 0))) if ayar.get("rol_id") else None
        await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â­ Otorol Durumu", description=f"Aktif: {'Evet' if ayar.get('aktif') else 'Hayir'}\nRol: {aktif_rol.mention if aktif_rol else 'Yok'}", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))
        return
    _otorol_ayar_kaydet(ctx.guild.id, {"rol_id": rol.id, "aktif": True})
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â­ Otorol Ayarlandi", description=f"Yeni gelenlere {rol.mention} verilecek.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="yetkiver")
@commands.has_permissions(manage_roles=True)
async def yetki_ver(ctx, uye: discord.Member = None, rol: discord.Role = None):
    if not uye or not rol:
        await ctx.send(embed=kullanim_embedi(".yetkiver @uye @rol"))
        return
    await uye.add_roles(rol, reason=f"{ctx.author} tarafindan yetki verildi")
    await ctx.send(embed=discord.Embed(title="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Yetki Verildi", description=f"{uye.mention} kullanicisina {rol.mention} verildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="yetkial")
@commands.has_permissions(manage_roles=True)
async def yetki_al(ctx, uye: discord.Member = None, rol: discord.Role = None):
    if not uye or not rol:
        await ctx.send(embed=kullanim_embedi(".yetkial @uye @rol"))
        return
    await uye.remove_roles(rol, reason=f"{ctx.author} tarafindan yetki alindi")
    await ctx.send(embed=discord.Embed(title="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“ Yetki Alindi", description=f"{uye.mention} kullanicisindan {rol.mention} alindi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="komutbilgi")
async def komut_bilgi(ctx, komut_adi: str = None):
    if not komut_adi:
        await ctx.send(embed=kullanim_embedi(".komutbilgi mute"))
        return
    komut = bot.get_command(komut_adi.lower())
    if not komut:
        await ctx.send(embed=hata_embedi("Komut Bulunamadi", "Bu isimle kayitli bir komut yok."))
        return
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â¡ Komut Bilgisi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Komut", value=f".{komut.name}", inline=True)
    embed.add_field(name="Kisa Aciklama", value=komut.help or "Aciklama yok.", inline=False)
    embed.add_field(name="Aliaslar", value=", ".join(komut.aliases) if komut.aliases else "Yok", inline=False)
    await ctx.send(embed=embed)


@bot.command(name="avatar")
async def avatar(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¼ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Avatar", description=f"{hedef.mention} kullanicisinin avatarÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.set_image(url=hedef.display_avatar.url)
    await ctx.send(embed=embed)


@bot.command(name="banner")
async def banner(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    kullanici = await bot.fetch_user(hedef.id)
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â´ Banner", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
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
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬Å“ Sunucu Kurallari", description=metin, color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    await ctx.send(embed=embed)


@bot.command(name="duyurupanel")
@commands.has_permissions(manage_guild=True)
async def duyuru_panel(ctx, *, metin: str = None):
    if not metin:
        await ctx.send(embed=kullanim_embedi(".duyurupanel Bugun etkinlik var!"))
        return
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¢ Duyuru", description=metin, color=RENKLER["basari"], timestamp=datetime.now(timezone.utc))
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)
    await ctx.send(embed=embed)


@bot.command(name="destekistek")
async def destek_istek(ctx, *, metin: str = None):
    if not metin:
        await ctx.send(embed=kullanim_embedi(".destekistek Yardim lazim"))
        return
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Ãƒâ€¹Ã…â€œ Destek Istegi", description=f"{ctx.author.mention}: {metin}", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="partnerpuan")
@commands.has_permissions(manage_guild=True)
async def partner_puan(ctx, uye: discord.Member = None, puan: int = None):
    if not uye or puan is None:
        await ctx.send(embed=kullanim_embedi(".partnerpuan @uye 10"))
        return
    veri = _partner_puan_al(ctx.guild.id)
    veri[str(uye.id)] = int(veri.get(str(uye.id), 0)) + int(puan)
    _partner_puan_kaydet(ctx.guild.id, veri)
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤Ãƒâ€šÃ‚Â Partner Puani Guncellendi", description=f"{uye.mention} kullanicisinin puani `{veri[str(uye.id)]}` oldu.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


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
            satirlar.append((toplam, f"Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â  {uye.mention} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Puan: {toplam} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Mesaj: {mesaj} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Ses: {_sureyi_formatla(ses)} ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Partner: {puan}"))
    satirlar.sort(key=lambda x: x[0], reverse=True)
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Leaderboard", description="\n".join(s[1] for s in satirlar[:10]) or "Veri yok.", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
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
        await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¹Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Emoji Eklendi", description=f"{emoji} basariyla eklendi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))
    except Exception as e:
        await ctx.send(embed=hata_embedi("Emoji Eklenemedi", str(e)))


@bot.command(name="kanalkilit")
@commands.has_permissions(manage_channels=True)
async def kanal_kilit(ctx, kanal: discord.TextChannel = None):
    hedef = kanal or ctx.channel
    await hedef.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ Kanal Kilitlendi", description=f"{hedef.mention} kilitlendi.", color=RENKLER["mute"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="kanalac")
@commands.has_permissions(manage_channels=True)
async def kanal_ac(ctx, kanal: discord.TextChannel = None):
    hedef = kanal or ctx.channel
    await hedef.set_permissions(ctx.guild.default_role, send_messages=None)
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Kanal Acildi", description=f"{hedef.mention} tekrar acildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


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
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¥ Herkese Rol Verildi", description=f"{sayi} uyeye {rol.mention} verildi.", color=RENKLER["basari"], timestamp=datetime.now(timezone.utc)))


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
    await ctx.send(embed=discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â§Ãƒâ€šÃ‚Â¹ Herkesten Rol Alindi", description=f"{sayi} uyeden {rol.mention} alindi.", color=RENKLER["hata"], timestamp=datetime.now(timezone.utc)))


@bot.command(name="say")
async def say_cmd(ctx):
    g = ctx.guild
    ses = sum(1 for u in g.members if u.voice and u.voice.channel)
    aktif = sum(1 for u in g.members if u.status != discord.Status.offline)
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Say", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
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
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨ Rol Bilgisi", color=rol.color if rol.color.value else RENKLER["rol"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Rol", value=rol.mention, inline=True)
    embed.add_field(name="ID", value=str(rol.id), inline=True)
    embed.add_field(name="Uye Sayisi", value=str(len(rol.members)), inline=True)
    embed.add_field(name="Renk", value=str(rol.color), inline=True)
    embed.add_field(name="Pozisyon", value=str(rol.position), inline=True)
    await ctx.send(embed=embed)


@bot.command(name="kanalbilgi")
async def kanal_bilgi(ctx, kanal: discord.abc.GuildChannel = None):
    hedef = kanal or ctx.channel
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Kanal Bilgisi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Ad", value=hedef.name, inline=True)
    embed.add_field(name="ID", value=str(hedef.id), inline=True)
    embed.add_field(name="Tur", value=type(hedef).__name__, inline=True)
    if getattr(hedef, "category", None):
        embed.add_field(name="Kategori", value=hedef.category.name, inline=True)
    await ctx.send(embed=embed)


@bot.command(name="kullanicibilgi")
async def kullanici_bilgi(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤ Kullanici Bilgisi", color=RENKLER["bilgi"], timestamp=datetime.now(timezone.utc))
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
    await ctx.send(embed=discord.Embed(title="ÃƒÆ’Ã¢â‚¬ÂÃƒâ€¦Ã‚Â¸ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã¢â‚¬Å“ Pong", description=f"Gecikme: **{ms}ms**", color=renk, timestamp=datetime.now(timezone.utc)))


def _yardim_final_haritasi():
    return {
        "Ayarlar": {"emoji": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¹Ã¢â‚¬Â ", "komutlar": ["kurulumdurum", "butunsistemlerikaldir", "uygulamakomutkapat", "otorol", "sunucukural", "duyurupanel", "sayac", "yasakli-komut"]},
        "Moderasyon": {"emoji": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â", "komutlar": ["ban", "blupbum", "kick", "mute", "unmute", "jail", "unjail", "cezagecmisi", "cezasil", "kanalkilit", "kanalac"]},
        "Roller": {"emoji": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨", "komutlar": ["renkpanel", "animerolpanel", "animerollerikur", "animerollerikaldir", "rolmenu", "levelrol", "levelrolsil", "levelrolleri", "yetkiver", "yetkial", "temprol", "herkese-rol", "herkesten-rol", "rolbilgi", "asagitasi", "rolidler"]},
        "Sistemler": {"emoji": "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬ÂÃ‚Â¢ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â", "komutlar": ["ticketpanel", "ticketkur", "partner-kur", "partner-kapat", "partnerpuan", "gifcevap", "gifcevapkapat", "gifcevapdurum", "otocevap", "jailkur", "jailkapat", "guvenlikkur", "guvenlikkapat", "guvenlikdurum", "kufur-kur", "kufur-kapat", "kufur-listele", "yetkilikufurkur", "yetkilikufurkapat", "yetkilikufurdurum", "spam-koruma-durum", "hosgeldinkur", "hosgeldinkapat", "karsilamakur", "karsilamakapat", "levelkur", "levelkapat"]},
        "Kullanici": {"emoji": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‹Å“Ãƒâ€šÃ‚Â¤", "komutlar": ["profil", "avatar", "banner", "kullanicibilgi", "isimgecmisi", "notekle", "notlar", "notsil", "destekistek"]},
        "Bilgi": {"emoji": "Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â¡", "komutlar": ["sunucupanel", "yetkilipanel", "sesistatistik", "mesajistatistik", "leaderboard", "say", "kanalbilgi", "komutbilgi", "ping"]},
        "Diger": {"emoji": "ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¨", "komutlar": []},
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
    satirlar = [f"ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ **.{komut.name}** - {_yardim_aciklama(komut)}" for komut in komutlar] or ["Bu bolumde gorunur komut yok."]
    return ["\n".join(satirlar[i:i + parca]) for i in range(0, len(satirlar), parca)] or ["Bu bolumde gorunur komut yok."]


def _yardim_ana_embed(istek_sahibi):
    kategoriler = _yardim_final_topla()
    toplam = sum(len(v["komutlar"]) for v in kategoriler.values())
    embed = discord.Embed(title="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã¢â‚¬â„¢Ãƒâ€¦Ã‚Â¸ Komut Menusu", description="Canli, duzgun ve daha renkli bir yardim menusu. Asagidan kategori secip direkt istedigin komutlara gec.", color=0xF7C948, timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¯ Kategoriler", value="\n".join(f"{veri['emoji']} **{kategori}**: {len(veri['komutlar'])}" for kategori, veri in kategoriler.items() if veri["komutlar"]) or "Komut bulunamadi.", inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬ Hizli Baslangic", value="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¨ `.renkpanel`\nÃƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â« `.ticketpanel`\nÃƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¹Ã¢â‚¬Â  `.levelkur`\nÃƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚ÂÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â `.gifcevap`\nÃƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€Â¢ `.jailkur`\nÃƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â¡ `.komutbilgi mute`", inline=True)
    embed.add_field(name="ÃƒÆ’Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å“Ãƒâ€šÃ‚Â¨ Ipuclari", value="Menuler sadece komutu yazan kisi tarafindan kullanilir.\n`.komutbilgi komutadi` ile detay gorebilirsin.\nToplam komut sayisi dinamik hesaplanir.", inline=False)
    embed.set_footer(text=f"{istek_sahibi} tarafindan acildi ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€šÃ‚Â¢ Toplam {toplam} komut")
    return embed


def _yardim_kategori_embed(kategori, veri, sayfa):
    renkler = {"Ayarlar": 0x7ED957, "Moderasyon": 0xFF6B6B, "Roller": 0x6BCBFF, "Sistemler": 0xC77DFF, "Kullanici": 0xF9C74F, "Bilgi": 0x4D96FF, "Diger": 0xB8B8D1}
    sayfalar = _yardim_sayfalari(veri["komutlar"])
    embed = discord.Embed(title=f"{veri['emoji']} {kategori} Komutlari", description=sayfalar[sayfa], color=renkler.get(kategori, 0xF7C948), timestamp=datetime.now(timezone.utc))
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ Komut", value=str(len(veri["komutlar"])), inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Sayfa", value=f"{sayfa + 1}/{len(sayfalar)}", inline=True)
    embed.add_field(name="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Ekstra", value="`.komutbilgi komutadi`", inline=True)
    return embed


class YardimKategoriSec(discord.ui.Select):
    def __init__(self, sahip_id):
        self.sahip_id = sahip_id
        kategoriler = _yardim_final_topla()
        options = [discord.SelectOption(label=kategori, description=f"{len(veri['komutlar'])} komut", emoji=veri["emoji"], value=kategori) for kategori, veri in kategoriler.items() if veri["komutlar"]]
        super().__init__(placeholder="Bir kategori sec", min_values=1, max_values=1, options=options, custom_id="yardim_final_kategori")

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
        super().__init__(style=discord.ButtonStyle.secondary, label="Sonraki" if ileri else "Onceki", emoji="ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¡ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â" if ileri else "ÃƒÆ’Ã‚Â¢Ãƒâ€šÃ‚Â¬ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ÃƒÆ’Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â", custom_id=f"yardim_final_{'ileri' if ileri else 'geri'}")

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
        super().__init__(style=discord.ButtonStyle.primary, label="Ana Menu", emoji="Ãƒâ€Ã…Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â ", custom_id="yardim_final_ana")

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


for _yardim_sil in ("yardim", "yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m", "yardÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±m", "help"):
    try:
        bot.remove_command(_yardim_sil)
    except Exception:
        pass


@bot.command(name="yardim", aliases=["yardÃƒÆ’Ã¢â‚¬ÂÃƒâ€šÃ‚Â±m", "help"], help="Renkli komut menusunu gosterir.")
async def yardim_final_gercek(ctx):
    view = YardimFinalView(ctx.author.id, str(ctx.author))
    await ctx.send(embed=view.mevcut_embed(), view=view)


if __name__ == "__main__":
    bot.run(BOT_TOKEN)
