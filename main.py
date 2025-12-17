from fastapi import FastAPI
from database import users_collection
from models.user_model import user_model
from utils.security import hash_password
from config import (
    SUPER_ADMIN_USERNAME,
    SUPER_ADMIN_EMAIL,
    SUPER_ADMIN_PASSWORD
)
from fastapi.middleware.cors import CORSMiddleware
from api import api_router  

app = FastAPI(title="Retail Stock Management Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js URL
    allow_credentials=True,
    allow_methods=["*"],   # GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],   # Authorization, Content-Type
)
# -------- SUPER ADMIN AUTO CREATE --------
# ✅ Moved to startup event to prevent import crash
@app.on_event("startup")
async def startup_event():
    try:
        print("🔄 Checking database connection...")
        # Simple check to trigger connection
        users_collection.database.command("ping")
        print("✅ Database Connected")
        
        create_default_super_admin()
    except Exception as e:
        print(f"⚠️ Database Connection Warning: {e}")

def create_default_super_admin():
    try:
        admin = users_collection.find_one({"role": "SUPER_ADMIN"})
        if not admin:
            users_collection.insert_one(
                user_model(
                    username=SUPER_ADMIN_USERNAME,
                    email=SUPER_ADMIN_EMAIL,
                    password=hash_password(SUPER_ADMIN_PASSWORD),
                    role="SUPER_ADMIN"
                )
            )
            print("✅ Default Super Admin Created")
    except Exception as e:
        print(f"❌ Failed to create super admin: {e}")


# -------- INCLUDE ALL ROUTES --------
app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Backend running successfully"}
