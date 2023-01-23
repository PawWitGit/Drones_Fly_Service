from datetime import datetime

from sqlalchemy import null
from sqlmodel import Field
# from turtle import title

from pydantic import BaseModel

from models import State
from schemas.base import BaseDroneAdd

DATETIME = datetime.utcnow()


class DroneOut(BaseDroneAdd):
    id: int
    created_at: datetime
    status: State
