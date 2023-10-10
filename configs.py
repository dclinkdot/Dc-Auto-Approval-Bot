# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23679347"))
    API_HASH = getenv("API_HASH", "7de55f9c943538839c4bdb877724a773")
    BOT_TOKEN = getenv("BOT_TOKEN", "6124544274:AAG2Reu-UDZPHpjno90WwJNf8gIQ5Le7YQY")
    FSUB = getenv("FSUB", "DC_Botz")
    CHID = int(getenv("CHID", "-1001924495958"))
    SUDO = list(map(int, getenv("SUDO", "5421323272").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://bhoomikbm9:XBxt4X2aH1msCHiU@cluster0.czv5bwi.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
