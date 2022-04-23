import motor.motor_asyncio
import os

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DATABASE_URL"])
database = client['DATABASE_NAME']
collection = database.get_collection("COLLECTION_NAME")