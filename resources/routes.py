from fastapi import APIRouter
from resources import auth
from resources import drone_add

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(drone_add.router)
