from pymongo import mongo_client
import pymongo
from app.config import settings

client = mongo_client.MongoClient(settings.DATABASE_URL)
print('Connected to MongoDB...')

db = client[settings.MONGO_INITDB_DATABASE]
User = db.users
Jobs = db.jobs
User.create_index([("email", pymongo.ASCENDING)], unique=True)
Jobs.create_index([("job_name", pymongo.ASCENDING)], unique=True)
