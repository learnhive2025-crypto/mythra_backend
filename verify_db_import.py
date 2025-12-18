import sys
import os

# Add current directory to path so we can import database.py
sys.path.append(os.getcwd())

try:
    print("Importing database module...")
    from database import client
    print("Attempting to connect...")
    info = client.server_info()
    print(f"SUCCESS! Connected to: {client.address}")
    print(f"Server Version: {info.get('version')}")
except Exception as e:
    print(f"Connection Failed: {e}")
