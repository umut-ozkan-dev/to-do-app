from fastapi import FastAPI, HTTPException
from psycopg2 

from models import Fruit

app = FastAPI()

fruits = [
    Fruit(id=1, name="mango", price=5.5),
    Fruit(id=2, name="apple", price=4),
    Fruit(id=3, name="watermelon", price=11),
    Fruit(id=4, name="banana", price=3),
]


@app.get("/")
def hello():
    return "Welcome to Fruit Shop"


@app.get("/fruits")
def return_fruits():
    return fruits


@app.get("/fruits/{id}")
def get_individual_fruit(id: int):
    for fruit in fruits:
        if fruit.id == id:
            return fruit
    raise HTTPException(status_code=404)


@app.post("/fruits")
def add_fruit(fruit: Fruit):
    fruits.append(fruit)
    return "Fruit added succesfully"


@app.delete("/fruits")
def delete_fruit(id: int):
    for i in range(len(fruits)):
        if fruits[i].id == id:
            del fruits[i]
            return "Fruit succesfully deleted"
    return HTTPException(status_code=404)


@app.put("/fruits")
def update_fruit(id: int, fruit: Fruit):
    for i in range(len(fruits)):
        if fruits[i].id == id:
            fruits[i] = fruit
            return "fruit updated succesfully"

    return HTTPException(status_code=404)
