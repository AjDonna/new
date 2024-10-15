#(©)CodeXBotz




import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7116038251:AAEK0Fx9gxAp41Yv0ZLqj_vJUbBWIcaep70")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7603458"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "910e420f1f74f40305a684a331dade35")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002027498504"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1735152469"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Sistaanimebash:Sistaanimebash@cluster0.w6ucx5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DB_URI)
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001715616229"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001974461884"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\nI am a file store bot Powered by @Animes_bash in⚡</b>.")
try:
    ADMINS=[6446763201]
    for x in (os.environ.get("ADMINS", "1889175355 6427494689 1119579816 1735152469 1632095203 6610700592").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Sorry Dude ned MChann</b>\n\n<b>So Please Joinhaning Your Favourite Animes ⚡</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Please Avoid Direct Messages. I'm Here merely for file sharing!"

ADMINS.append(OWNER_ID)
ADMINS.append(6446763201)

LOG_FILE_NAME = "filesharingbot.txt"

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
   
