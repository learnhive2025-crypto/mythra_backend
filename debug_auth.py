from database import users_collection
from config import SUPER_ADMIN_USERNAME, SUPER_ADMIN_PASSWORD
from utils.security import verify_password
import sys

print(f"Checking for user: {SUPER_ADMIN_USERNAME}")
try:
    user = users_collection.find_one({"username": SUPER_ADMIN_USERNAME})
    if user:
        print(f"User found: {user['username']}")
        print(f"Role: {user['role']}")
        print(f"Stored Hash: {user['password']}")
        
        is_valid = verify_password(SUPER_ADMIN_PASSWORD, user['password'])
        if is_valid:
            print(f"Password verification SUCCESS for '{SUPER_ADMIN_PASSWORD}'")
        else:
            print(f"Password verification FAILED for '{SUPER_ADMIN_PASSWORD}'")
    else:
        print("User NOT found in database.")
except Exception as e:
    print(f"Error during check: {e}")
