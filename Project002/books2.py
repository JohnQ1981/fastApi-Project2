from fastapi import FastAPI

app = FastAPI()

BOOKS =[]

@app.get("/books")