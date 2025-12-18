from pymongo import MongoClient
import certifi
import sys

# Hardcoded Cloud URL for testing
MONGO_URL = "mongodb+srv://learnhive2025_db_user:8Ogy0uxjD5JW60xs@cluster0.td8nbsq.mongodb.net/?appName=Cluster0"

print(f"Python Version: {sys.version}")
print("Attempting to connect to Cloud MongoDB...")

try:
    client = MongoClient(
        MONGO_URL,
        tls=True,
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=5000
    )
    # The command execution triggers the connection
    info = client.server_info()
    print(f"SUCCESS! Connected to Cloud MongoDB.")
    print(f"Server Version: {info.get('version')}")
except Exception as e:
    print(f"Connection Failed: {e}")
