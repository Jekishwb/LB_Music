import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = "28612368"
API_HASH = "3c23eaafcecfa70d11001dba6537b0fc"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7242981465:AAG5keMrdOrO6-0wGnKoeD60f5DIrwXsB38"


# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Yash_607:Yash_607@cluster0.r3s9sbo.mongodb.net/?retryWrites=true&w=majority"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = " -1002233702363"

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6935797014"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BAAZAR_X7")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/Friendly_Chatting_FC")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQG0lxAAN0h_yul7azjQEYZMjWIGVxFWunA20QkNpAigsYujZbRHbJsZH6CISm60pOE-pgXZA2KiwnV1-vdp2aADB_RbvcYmlqPJEzyh2CCoEI_Uoa3Y5Z9AkX0MvtvD0E4OAla0KFBPHWwPadoODqwFNKIxdElcgzGJMaGOm9wrzPajYpY6wbED3YiZyHLK4D4XzTxDqFri56cUL5an92iOfSlkBF_1DS1sBLHigvRqFmKIehYZmcfpCYr7mQfb14amK_WjNWWO2tLMwDHOvE-Nrrja9CrFXAfmY337pm3BWoYLsuL6Ma3lflqUFVm-3boG3OAjk6zoDpeBUhXDJO2qlQqJBAAAAAG95huZAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
STATS_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
STREAM_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/d6124ffb2b77deb60ae0b.jpg"


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
