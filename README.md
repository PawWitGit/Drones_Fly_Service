# Drones_Fly_Service

## Technologies
- Python 3.10
- FASTApi
- Postgresql
- sqlalchemy
- JS/Bootsrap
### Run App:
- create .env file in the main location
```
$ touch .env
```
- fill in .env file:
- DB_USER = your db_user
- DB_PASSWORD = your db_password
- DB_URL = your db_url ()
- SECRET_KEY= your secret key

- make migrations with alembic (I'll add instruction for thi point later)
- run app:
```
$ uvicorn main:app --reload
```