

from os import environ

API_ID = int(environ.get("API_ID", "30744675"))
API_HASH = environ.get("API_HASH", "2b2ab5de1550aaf6e8c4bb91daf8d1cf")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "5230086079").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "5230086079"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")







