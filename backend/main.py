from fastapi import FastAPI, HTTPException

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
def add_fruit(id: int, name: str, price: float):
    fruits.append(Fruit(id=id, name=name, price=price))


@app.delete("/fruits")
def delete_fruit(id: int):
    for fruit in fruits:
        if fruit.id == id:
            del fruits[fruits.index(fruit)]
    raise HTTPException(status_code=404)
