from pydantic import BaseModel

from models import State
from schemas.base import BaseDroneAdd


class DroneAddIn(BaseDroneAdd):
    status: State

