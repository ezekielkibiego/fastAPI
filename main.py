from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import UUID, uuid4

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name='Ezekiel',
        last_name='Kibiego',
        gender=Gender.male,
        roles=[Role.staff]
        
    ),
    User(
        id=uuid4(),
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
    return db;

@app.post("/api/users")
async def register_users(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{user.id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
