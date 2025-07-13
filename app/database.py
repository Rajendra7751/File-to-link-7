from pymongo import MongoClient
from app.config import Config

client = MongoClient(Config.MONGO_URI)
db = client["filetolink"]
files = db["files"]

def insert_file(file_id, file_name):
    files.update_one(
        {"file_id": file_id},
        {"$set": {"file_name": file_name}},
        upsert=True
    )

def get_file_name(file_id):
    result = files.find_one({"file_id": file_id})
    return result["file_name"] if result else None
