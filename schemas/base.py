from pydantic import BaseModel


class BaseDroneAdd(BaseModel):
    manufacturer: str
    description: str
    model: str
    drone_type: str
    photo_url: str
