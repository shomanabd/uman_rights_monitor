import os
from dotenv import load_dotenv

load_dotenv()

# Validate critical environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

if not SECRET_KEY:
    raise ValueError("❌ SECRET_KEY is required in .env file. Run generate_keys.py first!")

if not ENCRYPTION_KEY:
    raise ValueError("❌ ENCRYPTION_KEY is required in .env file. Run generate_keys.py first!")

# Database settings
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "human_rights_monitor")

# Auth settings
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

print("✅ Configuration loaded successfully")