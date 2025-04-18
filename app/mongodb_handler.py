# app/mongodb_handler.py

import os
from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

# Define DB and collections
db = client["content_ai_db"]
uploads_col = db["uploads"]
agents_col = db["agents"]
projects_col = db["projects"]

def save_upload(file_name, project_name, role, purpose, source_type="file", source_path=None):
    entry = {
        "file_name": file_name,
        "project_name": project_name,
        "role": role,
        "purpose": purpose,
        "source_type": source_type,  # 'file' or 'url'
        "source_path": source_path,  # local path or url
        "timestamp": datetime.utcnow()
    }
    result = uploads_col.insert_one(entry)
    return str(result.inserted_id)

def get_all_uploads(project_name=None):
    query = {}
    if project_name:
        query["project_name"] = project_name
    return list(uploads_col.find(query))