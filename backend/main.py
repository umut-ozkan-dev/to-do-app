from fastapi import FastAPI, HTTPException, status

app = FastAPI()

my_fruit_list = ["watermelon", "banana", "pineapple", "strawberry"]


@app.get("/")
def return_message():
    return {"message": "Welcome to fruit shop"}


fruit_list: list[str] = []


@app.get("/fruits")
def return_fruit_list():
    return fruit_list


@app.get("/fruits/{id}")
def return_fruit(id: int):
    if id > (len(fruit_list) - 1) or id < 0:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail="You entered a wrong index"
        )
    return fruit_list[id]


@app.delete("/fruits/{id}")
def delete_fruit(id: int):
    del fruit_list[id]
    return {"message": "fruit deleted succesfully"}


@app.post("/fruits")
def add_fruit(fruit: str):
    fruit_list.append(fruit)


@app.delete("/fruits")
def empty_the_list():
    for i in range(len(fruit_list)):
        del fruit_list[i]
