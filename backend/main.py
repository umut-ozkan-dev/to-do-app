from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

todos: dict[int, str] = {}


 
@app.get("/")
def welcome():
    return {"message": "welcome"}


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos")
def add_todos(id: int, todo_text: str):
    todos[id] = todo_text


@app.delete("/todos")
def delete_todos(id: int):
    del todos[id]


@app.put("/todos")
def update_todos(id: int, new_text: str):
    todos[id] = new_text
