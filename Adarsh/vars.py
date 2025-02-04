# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = True
    API_ID = int(getenv('API_ID','1031795'))
    API_HASH = str(getenv('API_HASH','18dd863b73c1a440852bf5dcdce63ea1'))
    BOT_TOKEN = str(getenv('BOT_TOKEN','6411618566:AAHR_F0tU1tPw85G_SDUvtCWtlvz4W8SHSQ'))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL','-1001989804673'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "857115270").split())
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME','Imstark3000'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME', 'mhstream1-a545c81b7f7f'))

    else:
        ON_HEROKU = True
    FQDN = str(getenv('FQDN', "mhstream1-a545c81b7f7f.herokuapp.com")) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL','mongodb+srv://movieshubxd:movieshubxd@cluster0.rxtlmfw.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'moviesub_premium_membership'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
