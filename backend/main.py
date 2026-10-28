from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def return_hello():
    return {"message": "hello"}
