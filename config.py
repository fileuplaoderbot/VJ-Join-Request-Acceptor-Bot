import re
from os import environ

API_ID = int(environ.get("API_ID", "26683574"))
API_HASH = environ.get("API_HASH", "69ba051f43cff367bf569bd54eb277a7")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002321487882"))
ADMINS = int(environ.get("ADMINS", "6069621485"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://AniReal123:AniReal123@anireal123.wqnsp.mongodb.net/?retryWrites=true&w=majority&appName=AniReal123") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "AniReal123")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
id_pattern = re.compile(r'^.\d+$')
AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '-1002442800721').split()] # give channel id with seperate space. Ex : ('-10073828 -102782829 -1007282828')
