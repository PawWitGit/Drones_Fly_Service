from fastapi import APIRouter, Depends
from starlette.requests import Request
from typing import List
from managers.drone_add import DroneAddManager
from managers.auth import oauth2_scheme, is_drone_user
from schemas.request.drone_add import DroneAddIn
from schemas.response.drone_add import DroneOut

router = APIRouter(tags=["Drone Adding"])


@router.get(
    "/drones/", dependencies=[Depends(oauth2_scheme)], response_model=List[DroneOut]
)
async def get_drones(request: Request):
    user = request.state.user
    # DroneAddManager.get_drones(user)
    return await DroneAddManager.get_drones(user)


@router.post(
    "/drones/",
    dependencies=[Depends(oauth2_scheme), Depends(is_drone_user)],
    response_model=DroneOut,
)
async def create_drones(request: Request, drone_add: DroneAddIn):
    user = request.state.user
    return await DroneAddManager.create_drone(drone_add.dict(), user)
