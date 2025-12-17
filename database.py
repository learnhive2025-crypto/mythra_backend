from pymongo import MongoClient
from config import MONGO_URL, DB_NAME

client = MongoClient(MONGO_URL)
db = client[DB_NAME]   # 👈 retail_shop_db create aagum

users_collection = db["users"]
