from fastapi import APIRouter , Response, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
import tempfile
router = APIRouter()


#todo should move to db name should be unique
images = [
     {"name":"deadsea","path":r"C:\Users\Idan\Documents\images\deadsea.jpg","categories":['work'],"description":"עבודה במפעלי ים המלח", "header":"כותרת"},
     {"name":"img1","path":r"C:\Users\Idan\Documents\images\img1.jpg","categories":[],"description":"", "header":"כותרת"},
     {"name":"img2","path":r"C:\Users\Idan\Documents\images\img2.jpg","categories":[],"description":"", "header":"כותרת"},
    {"name":"img3","path":r"C:\Users\Idan\Documents\images\img3.jpeg","categories":[],"description":"", "header":"כותרת"},
    {"name":"img4","path":r"C:\Users\Idan\Documents\images\img4.jpeg","categories":[],"description":"", "header":"כותרת"}
    ,
     ]

categories = [
    {"name":"wedding", "color":"primary"},
    {"name":"family", "color":"red"},
    {"name":"work", "color": "secondary"},
    {"name":"vacations", "color":"green"}
]


# basemodels for post

class Image(BaseModel):
    name: str
    description: str
    categories: list
    header: str

class Category(BaseModel):
    name: str
    color: str

@router.get("/images/{name}", tags=["images"])
async def get_image(name):
    for image in images:
        if image['name'] == name:
            with open(image['path'], 'r') as f:
                return FileResponse(f.name, media_type="image/png")

@router.post("/images", tags=["images"])
async def update_image(image: Image):
    print(image)
    for im in images:
        if image.name == im['name']:
            im['description'] = image.description
            im['categories'] = image.categories
            im['header'] = image.header
    return {"IsSuccess":True}

@router.get("/images", tags=["images"])
async def get_all_images():
    return images


@router.get("/categories", tags=["images"])
async def get_categoris():
    return categories


