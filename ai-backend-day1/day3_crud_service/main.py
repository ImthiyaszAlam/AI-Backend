# main.py
from fastapi import FastAPI, HTTPException
from models import User

app = FastAPI(title="User Service")

# fake DB (list)
users_db = []

@app.post("/users")
def create_user(user: User):
    users_db.append(user)
    return {"message": "User created", "user": user}

@app.get("/users")
def list_users():
    return {"users": users_db}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for u in users_db:
        if u.id == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users_db
    users_db = [u for u in users_db if u.id != user_id]
    return {"message": f"User {user_id} deleted"}
