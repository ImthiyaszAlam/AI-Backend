from fastapi import FastAPI,HTTPException
from models import Todo
from database import todos


app= FastAPI(title="day6 CRUD MicroService")

@app.post("/todos")
async def create (todo:Todo):
    if todo.id in todos:
        raise HTTPException(status_code=400,detail="TODO Already exists")
    todos[todo.id]=todo
    return {"message": "todo created","todo": todo}


@app.get("/todos")
async def get_all():
    return list(todos.values())

@app.get("/todos/{todo_id}")
async def get_one(todo_id: int):
    todo = todos.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found.")
    return todo


@app.put("/todos/{todo_id}")
async def update(todo_id: int, updated: Todo):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found.")
    todos[todo_id] = updated
    return {"message": "Todo updated", "todo": updated}

@app.delete("/todos/{todo_id}")
async def delete(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found.")
    del todos[todo_id]
    return {"message": "Todo deleted successfully."}
