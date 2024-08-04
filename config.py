#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

load_dotenv()

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

API_ID = getenv("API_ID", "25488022")
API_HASH = getenv("API_HASH", "0c999a454fddd79251213be7944811e8")

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

BOT_TOKEN = getenv("BOT_TOKEN", "6548314357:AAEFhj5_pAfTY9_lCsPkHvD_Zck4Xq8ibpU")

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

LOG_GROUP_ID = getenv("LOG_GROUP_ID", "-1002136795173")

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

OWNER_ID = int(getenv("OWNER_ID", 1356469075))

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 999999))

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TEAM_DC_BOTS")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TEAM_DC_BOTS")

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "821d1bf8430346b98aa98e62ceb31416")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "5fad47a0e1a340ca9cf88d9aa60b494b")

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---
#PROVIDE IMAGES
START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/83da25751161cc4b9d408.jpg")

PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/59d3d5fbaca41ec09f33d.jpg")

PLAYLIST_IMG_URL = "https://graph.org/file/954b70e8c68314875cb78.jpg"

STATS_IMG_URL = "https://graph.org/file/dc565712c080a72b0320e.jpg"

TELEGRAM_AUDIO_URL = "https://graph.org/file/92349afcdfb9da6f7c693.jpg"

TELEGRAM_VIDEO_URL = "https://graph.org/file/92349afcdfb9da6f7c693.jpg"

YOUTUBE_IMG_URL = "https://graph.org/file/4cf64c2a1902b56a52d13.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/cb50d35a419853de6cd48.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/cb50d35a419853de6cd48.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/cb50d35a419853de6cd48.jpg"

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

#---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---x---


