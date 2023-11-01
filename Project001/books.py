from fastapi import FastAPI

app = FastAPI()


@app.get("/api-endpoint")
async def first_api():
    return {'message': 'Hello Johny!'}

@app.get("/books")
def read_all_books():
    return {'message': 'Hello Books!'}
