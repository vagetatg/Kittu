import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 23255238))
API_HASH = getenv("API_HASH", "009e3d8c1bdc89d5387cdd8fd182ec15")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8329333238:AAEAwyudQ6eaU5CS-ynJfuudejo8pO0AD4A")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Kittu:Kittu@kittu.nvijrco.mongodb.net/?retryWrites=true&w=majority&appName=Kittu")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Tvk_musicbot")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "Tvk_musicbot")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1003135308769"))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7943359877"))

OWNER_USERNAME = getenv("OWNER_USERNAME","Kittu_the_meoww")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/vagetatg/Kittu",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/privatelog_tvk")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/teakadai_update")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4"
)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION", "BQG5kuUAPi54o9nkUK4z8qWeCp87RE9XlHloQ-gdk1L7y5X9IObCyv9vC8ZA3cPfiD16eIKwhHNC000yc-Ytoj4hA-EdJdtpmAMPZ9OAOv7W3kVaoYXXqfGv-J4tftkN5bZVDsqNFQ7JO6iZ-2fvH0Ke7yKpBwtw1Lp5YHw5syzK6IF3jJG0TIQQMqEIMPHWEAOtuQPLwqbRR_6vD_V5BUnyNM-D_zT4bAgbzWGvKbIEo-ZxGFa64mFh8XbQPlHNXsUc5SdJyHdnsVCAt7B8TpND4MhX0fJW7WSh9EGv2Jz9O9_E8zoS0nfKuS75sMBbY3LqXOf5-uCgO6hxlRQce25plSlfUAAAAAHv8Np5AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/sv1a44.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/7mhdku.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/4wn6s3.jpg"
STATS_IMG_URL = "https://files.catbox.moe/o4m8ep.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/khtmmz.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/x6leoc.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/rzo9jm.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/x6leoc.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/khtmmz.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/o4m8ep.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/4wn6s3.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/x6leoc.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


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
