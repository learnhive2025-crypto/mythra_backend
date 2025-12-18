from pymongo import MongoClient
import certifi
from config import MONGO_URL, DB_NAME

if "mongodb+srv" in MONGO_URL:
    client = MongoClient(MONGO_URL, tlsCAFile=certifi.where())
else:
    client = MongoClient(MONGO_URL)
db = client[DB_NAME]   # 👈 retail_shop_db create aagum

users_collection = db["users"]
