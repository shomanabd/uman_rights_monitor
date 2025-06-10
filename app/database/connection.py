from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB connection
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "human_rights_monitor")

client = MongoClient(MONGODB_URL)
database = client[DATABASE_NAME]

# Collections
victims_collection = database["victims"]
users_collection = database["users"]
victim_risk_assessments = database["victim_risk_assessments"]

# Create indexes for better performance and security
def create_indexes():
    # Index for faster queries
    victims_collection.create_index("type")
    victims_collection.create_index("risk_assessment.level")
    victims_collection.create_index("created_at")

    # Unique index for users
    users_collection.create_index("username", unique=True)
    users_collection.create_index("email", unique=True)

create_indexes()