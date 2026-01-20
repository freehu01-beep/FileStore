# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ, getenv
import logging
from logging.handlers import RotatingFileHandler


# --------------------------------------------
# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
APP_ID = int(os.environ.get("APP_ID"))  # API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH")   # API HASH from my.telegram.org
# --------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))  # DB channel ID
OWNER = os.environ.get("OWNER", "CrazyXAbhi")   # Owner username
OWNER_ID = int(os.environ.get("OWNER_ID"))      # Owner Telegram ID
# --------------------------------------------
PORT = os.environ.get("PORT", "8080")
# --------------------------------------------
DB_URI = os.environ.get("DATABASE_URL")
DB_NAME = os.environ.get("DATABASE_NAME", "Store")
# --------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "0"))  # 0 = no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/CrazyXAbhi_official")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
# --------------------------------------------
START_PIC = os.environ.get(
    "START_PIC",
    "https://telegra.ph/file/ec17880d61180d3312d6a.jpg"
)
FORCE_PIC = os.environ.get(
    "FORCE_PIC",
    "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg"
)
# --------------------------------------------

# --------------------------------------------
HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ by <a href=https://t.me/CrazyXAbhi_official>CrazyXAbhi</a>\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ</blockquote></b>"

ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/CrazyXAbhi_official>CrazyXAbhi</a>\n◈ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/CrazyXAbhi_official>CrazyXAbhi Official</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/CrazyXAbhi_official>CrazyXAbhi</a></blockquote></b>"
# --------------------------------------------

START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>ʜᴇʟʟᴏ {first}\n\n<blockquote>ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ʙʏ CrazyXAbhi.\nɪ sᴛᴏʀᴇ ғɪʟᴇs ᴀɴᴅ ɢɪᴠᴇ ʏᴏᴜ sᴇᴄᴜʀᴇ ʟɪɴᴋs.</blockquote></b>"
)

FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇ.</b>"
)

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
"""

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>{previouscaption}</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "This bot belongs to CrazyXAbhi 😎🔥"

# --------------------------------------------

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
