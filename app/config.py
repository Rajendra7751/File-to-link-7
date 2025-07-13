import os

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    MONGO_URI = os.getenv("MONGO_URI")
    BIN_CHANNEL = int(os.getenv("BIN_CHANNEL"))
    FQDN = os.getenv("FQDN", "localhost")
    PORT = int(os.getenv("PORT", "8080"))
    HAS_SSL = os.getenv("HAS_SSL", "False").lower() == "true"
