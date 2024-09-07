from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:AdDfgFRFVVfDEhdhyjjvjjftSEW")
    FSUB = getenv("FSUB", "justtestmmmu")
    CHID = int(getenv("CHID", "-1000112234"))
    SUDO = list(map(int, getenv("7040444713 2144812475").split())
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://hi:hi@auto.natzh.mongodb.net/?retryWrites=true&w=majority&appName=auto")
    
cfg = Config()
