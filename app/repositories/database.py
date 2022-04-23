from bson.objectid import ObjectId
from app.repositories.db_config import collection
from fastapi import Response


async def insert_post(post_data):
    post = await collection.insert_one(post_data)
    new_post = await collection.find_one({'_id': 0})
    return new_post

async def get_all_posts():
    posts = []
    async for post in collection.find():
        post['id'] = str(post['_id'])
        del[post['_id']]
        posts.append((post))
    return posts

async def delete_post(id:str):
    post = await collection.find_one({"_id": ObjectId(id)})
    if post:
        collection.delete_one({"_id": ObjectId(id)})
        return True
    

async def get_post_by_id(id: str):
    post = await collection.find_one({"_id": ObjectId(id)}, {'_id': 0})
    if not post:
        raise PostNotFoundError(id)

    
class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class PostNotFoundError(NotFoundError):

    entity_name: str = "Post"

