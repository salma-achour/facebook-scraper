

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide
from ..models.models import ResponseModel, ErrorResponseModel
from app.repositories.database import NotFoundError

from ..Services.service import ScrapingService


router = APIRouter()

@router.post("/collect/{page_name}/{post_limit}")
@inject
async def add(
        page_name: str,
        post_limit: int,
        scraping_service: ScrapingService = Depends(ScrapingService)
):
    new_post=await scraping_service.add_posts(page_name,post_limit)
    return  ResponseModel(new_post, "All Posts Addes Successfully")

@router.get("/posts")
@inject
async def get_list(scraping_service: ScrapingService = Depends(ScrapingService)):
    posts  =  await scraping_service.get_posts()
    return ResponseModel(posts, "All Posts Returned Successfully")


@router.get("/posts/{id}")
@inject
async def get_by_id(
        id: str,
        scraping_service: ScrapingService = Depends(ScrapingService)):
    try:
        return await scraping_service.get_posts_by_id(id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    
    
@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def remove(
        id : str,
        scraping_service: ScrapingService = Depends(ScrapingService)
):
    try:
        await scraping_service.delete_post_by_id(id)
    except:
        return Response(status_code=status.HTTP_404_NOT_FOUND)



@router.get("/status")
def get_status():
    return {"status": "OK"}
