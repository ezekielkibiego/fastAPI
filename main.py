from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, UserUpdate
from uuid import UUID

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("b7f90076-d2f5-47bd-b59d-1debc7e86035"),
        first_name='Ezekiel',
        last_name='Kibiego',
        gender=Gender.male,
        roles=[Role.staff]
        
    ),
    User(
        id=UUID("b7f90076-d2f5-47bd-b59d-1debc7e86036"),
        first_name='Dinah',
        last_name='Datah',
        gender=Gender.female,
        roles=[Role.admin, Role.user]
        
    )
]

@app.get("/")
async def root():
    return {"Hello": "Kibiego"}

@app.get("/api/users")
async def fetch_users():
    return db

@app.post("/api/users")
async def register_users(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return

    raise HTTPException(
        status_code=404,
        detail=f"Could not find user with id: {user_id}"
        )
    
@app.put("/api/users/{user_id}")

async def update_user(user_update: UserUpdate, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    
    raise HTTPException(
        status_code=404,
        detail=f"Could not find user with id: {user_id}"
        )