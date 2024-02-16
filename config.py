import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "1779071"))
    API_HASH = os.environ.get("API_HASH", "3448177952613312689f44b9d909b5d3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6092537699:AAFdfZ5oo-P5peFlWJTN2iqzr_govF0jD-M") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "6092537699:AAFdfZ5oo-P5peFlWJTN2iqzr_govF0jD-M") 
    OWNER_ID = os.environ.get("OWNER_ID", "1169076058")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://filestream:filestream@cluster0.d1dlfzv.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "Forward_Session")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001751333376"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "NazriyaFilterBot")

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
