from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Day 4 - User Manager API")

class User(BaseModel):
    id: int
    name: str
    email: str

users_db = {}

@app.post("/users")
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists.")
    users_db[user.id] = user
    return {"message": "User created successfully", "user": user}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = updated_user
    return {"message": "User updated", "user": updated_user}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted"}
        