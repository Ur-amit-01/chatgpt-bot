# ©️biisal jai shree krishna 😎
from os import environ

load_dotenv()

API_ID = environ.get("API_ID" , "22012880")
API_HASH = environ.get("API_HASH" , "5b0e07f5a96d48b704eb9850d274fe1d")
BOT_TOKEN = environ.get("BOT_TOKEN" , "")
ADMIN = int(environ.get("ADMIN" , "7728066109"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1004758607891"))
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002355632078")
MONGO_URL = environ.get("MONGO_URL" , "mongodb://localhost:27017")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1002355632078")
)
FSUB = environ.get("FSUB", True)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", False
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
