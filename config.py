# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "26184715"))
API_HASH = getenv("API_HASH", "7fc42fe25c89660b4e0b00dd7aa0beb1")
BOT_TOKEN = getenv("BOT_TOKEN", "8225077803:AAGqTGGMpLo4fywYcRDASFD4RhUDp2NrPl0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7744686564").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://dubeyji0995:Gqaqduzpm98kT6ZF@cluster0.ekxizvl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003777520171"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "7fc42fe25c89660b4e0b00dd7aa0beb1")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
