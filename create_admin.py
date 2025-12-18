from database import users_collection
from models.user_model import user_model
from utils.security import hash_password
from config import SUPER_ADMIN_USERNAME, SUPER_ADMIN_EMAIL, SUPER_ADMIN_PASSWORD
import sys

print(f"Creating super admin: {SUPER_ADMIN_USERNAME}")

try:
    # Check if exists
    if users_collection.find_one({"username": SUPER_ADMIN_USERNAME}):
        print("User already exists!")
    else:
        new_admin = user_model(
            username=SUPER_ADMIN_USERNAME,
            email=SUPER_ADMIN_EMAIL,
            password=hash_password(SUPER_ADMIN_PASSWORD),
            role="SUPER_ADMIN"
        )
        users_collection.insert_one(new_admin)
        print("SUCCESS! Super Admin Created.")
except Exception as e:
    print(f"FAILED to create admin: {e}")
