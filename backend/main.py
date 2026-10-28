from fastapi import FastAPI, HTTPException, status

app = FastAPI()

my_fruit_list = ["watermelon", "banana", "pineapple", "strawberry"]


@app.get("/")
def return_message():
    return {"message": "hello world"}


fruit_list: list[str] = []


@app.get("/fruits")
def return_fruit_list():
    return fruit_list


@app.get("/fruits/{id}")
def return_fruit(id: int):
    if id > len(fruit_list) or id < 0:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail="You entered a wrong index"
        )
    return fruit_list[id]


@app.post("/fruits")
def add_fruit():
    for frut in my_fruit_list:
        fruit_list.append(frut)
