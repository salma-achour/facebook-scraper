from facebook_scraper import get_posts
from ..repositories.database import *



class ScrapingService:

    def __init__(self) -> None:
        pass

    def get_posts(self):
        return get_all_posts()
    
    def get_posts_by_id(self, id:str):
        return get_post_by_id(id)

    def add_posts(self,page_name,post_limit):
        for post in get_posts(str(page_name), pages=int(post_limit)):
            return insert_post(post)

    def delete_post_by_id(self, id: str):
        return delete_post(id)

    
