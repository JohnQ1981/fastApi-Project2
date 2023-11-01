from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    {'title': 'Title One', 'author': 'John', 'category': 'science'},
    }

@app.get("/api-endpoint")
async def first_api():
    return {'message': 'Hello John!'}

@app.get("/books")
async def read_all_books():
    return {'message': 'Hello Books!'}
