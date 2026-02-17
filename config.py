# +++ Modified By [telegram username: @Codeflix_Bots
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", ""))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "Links-Share")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @Codeflix_Bots</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC = "https://graph.org/file/7228e9fe7ebf6145cca11-38b598b785ee91950b.jpg"
START_IMG = "https://graph.org/file/7228e9fe7ebf6145cca11-38b598b785ee91950b.jpg"
# Messages
START_MSG = os.environ.get("START_MSG", "<b>👋 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ!</b>\n\n<blockquote><b>ᴛʜɪs ʙᴏᴛ ɪs ᴀɴ ᴇxᴄʟᴜsɪᴠᴇ ɢᴀᴛᴇᴡᴀʏ ғᴏʀ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴛᴏ ᴀᴄᴄᴇss ᴄᴏɴᴛᴇɴᴛ sᴇᴄᴜʀᴇʟʏ. ᴘʟᴇᴀsᴇ ᴜsᴇ ᴛʜᴇ ʟɪɴᴋs ᴘʀᴏᴠɪᴅᴇᴅ ɪɴ ᴛʜᴇ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs.</b></blockquote>\n\n<b>• 💠 ᴛʜɪs ɪs ᴀ ᴘʀɪᴠᴀᴛᴇʟʏ ᴍᴀɴᴀɢᴇᴅ sʏsᴛᴇᴍ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ᴏᴜʀ ᴄᴏɴᴛᴇɴᴛ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.</b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Creator: <a href=https://t.me/proyato>Yato</a>\n» Our Community: <a href=https://t.me/otakuflix_network>Flix Network</a>\n» Anime Channel: <a href=https://t.me/animes_cruise>Anime Cruise</a>\n» Ongoing Anime: <a href=https://t.me/Ongoing_cruise>Ongoing cruise</a>\n» Developer: <a href=https://t.me/onlyyuji>Yuji</a></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/Unrated_Coder'>Uɴʀᴀᴛᴇᴅ Cᴏᴅᴇʀ ™</a></b>\n<blockquote><b>╭━━━━━━━━━━━━━━━━━━━━━\n├›› ᴏᴡɴᴇʀ: <a href='https://t.me/ProKillua'>Kɪʟʟᴜᴀ</a> Zᴏʟᴅʏᴄᴋ\n├›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3'>Pʏᴛʜᴏɴ 3.10</a>\n├›› ʟɪʙʀᴀʀʏ: <a href='https://www.mongodb.com/docs/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>\n├›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>\n├›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ProKillua\n╰━━━━━━━━━━━━━━━━━━━━━</b></blockquote>")

ABOUT_TXT = """<b>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/Unrated_Coder'>Uɴʀᴀᴛᴇᴅ Cᴏᴅᴇʀ ™</a></b>
<blockquote><b>╭━━━━━━━━━━━━━━━━━━━━━
├›› ᴏᴡɴᴇʀ: <a href='https://t.me/ProKillua'>Kɪʟʟᴜᴀ Zᴏʟᴅʏᴄk</a>
├›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3'>Pʏᴛʜᴏɴ 3.10</a>
├›› ʟɪʙʀᴀʀʏ: <a href='https://www.mongodb.com/docs/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a>
├›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a>
├›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ProKillua
╰━━━━━━━━━━━━━━━━━━━━━</b></blockquote>""" 

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/animes_cruise'>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>
<blockquote expandable>›› ᴍᴏᴠɪᴇs: <a href='https://t.me/movieflixspot'>ᴍᴏᴠɪᴇғʟɪx sᴘᴏᴛ</a>
›› ᴡᴇʙsᴇʀɪᴇs: <a href='https://t.me/webseries_flix'>ᴡᴇʙsᴇʀɪᴇs ғʟɪx</a>
›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/hanime_arena'>ᴄᴏʀɴʜᴜʙ</a>
›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/pornhwa_flix'>ᴘᴏʀɴʜᴡᴀ</a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/otakuflix_network'>ᴏᴛᴀᴋᴜғʟɪx</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ProYato</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "6497757690").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
