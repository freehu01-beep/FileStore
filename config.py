import os
import logging
from logging.handlers import RotatingFileHandler

# ---------------- BOT CONFIG ----------------
LOG_FILE_NAME = "bot.log"
PORT = os.getenv("PORT", "5010")

OWNER_ID = int(os.getenv("OWNER_ID", "7372953562"))

MSG_EFFECT = int(os.getenv("MSG_EFFECT", "5046509860389126442"))

SHORT_URL = os.getenv("SHORT_URL", "linkshortify.com")
SHORT_API = os.getenv("SHORT_API", "")
SHORT_TUT = os.getenv("SHORT_TUT", "https://t.me/CrazyXAbhi_official")

# ---------------- TELEGRAM ----------------
SESSION = os.getenv("SESSION", "crazyxabhi_bot")
TOKEN = os.getenv("BOT_TOKEN")              # BotFather token
API_ID = int(os.getenv("API_ID"))           # my.telegram.org
API_HASH = os.getenv("API_HASH")
WORKERS = int(os.getenv("WORKERS", "5"))

# ---------------- DATABASE ----------------
DB_URI = os.getenv("DB_URI")                # MongoDB URI
DB_NAME = os.getenv("DB_NAME", "yato")

# ---------------- FORCE SUB ----------------
FSUBS = [[-1003016571084, True, 10]]  # keep same structure

# Database Channel (Primary)
DB_CHANNEL = int(os.getenv("DB_CHANNEL"))

# Auto Delete Timer (seconds)
AUTO_DEL = int(os.getenv("AUTO_DEL", "300"))

# Admin IDs (space separated in ENV)
ADMINS = list(map(int, os.getenv("ADMINS", "6734851240").split()))

# Bot Settings
DISABLE_BTN = os.getenv("DISABLE_BTN", "True") == "True"
PROTECT = os.getenv("PROTECT", "True") == "True"

# ---------------- MESSAGES ----------------
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!!, {first} ~ <blockquote>I am File Store Bot by CrazyXAbhi 😎🔥</blockquote></b>",

    "FSUB": "<b><blockquote>›› ʜᴇʏ ×</blockquote>\nʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️\nᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴛᴏ ɢᴇᴛ ғɪʟᴇs</b>",

    "ABOUT": "<b>›› Powered by CrazyXAbhi\n<blockquote expandable>"
             "›› Channel: <a href='https://t.me/CrazyXAbhi_official'>Click Here</a>\n"
             "›› Owner: CrazyXAbhi\n"
             "›› Library: Pyrogram v2\n"
             "›› Database: MongoDB\n"
             "›› Developer: CrazyXAbhi</blockquote></b>",

    "REPLY": "<b>For more updates join 👉 https://t.me/CrazyXAbhi_official</b>",

    "SHORT_MSG": "<b>📊 Hey {first},\n\nYour access link is ready.\nClick OPEN LINK to continue.</b>",

    "START_PHOTO": "https://graph.org/file/510affa3d4b6c911c12e3.jpg",
    "FSUB_PHOTO": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT_PIC": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}

# ---------------- LOGGER ----------------
def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
