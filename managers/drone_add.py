from db import database
from models import RoleType, State, drone


class DroneAddManager:
    @staticmethod
    async def get_drones(user):
        q = drone.select()
        if user["role"] == RoleType.user:
            q = q.where(drone.c.drone_pilot_id == user["id"])

        elif user["role"] == RoleType.verify_person:
            q = q.where(drone.c.state == State.verified)
        return await database.fetch_all(q)

    @staticmethod
    async def create_drone(drone_data, user):
        drone_data["drone_pilot_id"] = user["id"]
        id_ = await database.execute(drone.insert().values(drone_data))
        return await database.fetch_one(drone.select().where(drone.c.id == id_))
7