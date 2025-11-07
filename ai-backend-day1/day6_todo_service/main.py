from fastapi import FastAPI,HTTPException
from models import Todo
from database import todos


app= FastAPI(title="day6 CRUD MicroService")