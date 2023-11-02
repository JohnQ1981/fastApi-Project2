"""
Assignment

Here is your opportunity to keep learning!

1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.
"""
from fastapi import Body, FastAPI

app = FastAPI()

BOOKS =[
    {'title': 'Hello1', 'author': 'John', 'category': 'science'},
    {'title': 'Hello2', 'author': 'Johny Writer7', 'category': 'biology'},
    {'title': 'Hello3', 'author': 'Johny Writer8', 'category': 'math'},
    {'title': 'Hello4', 'author': 'Johny Writer9', 'category': 'technology1'},
    {'title': 'Hello5', 'author': 'John', 'category': 'science'}
]

@app.get("/mybooks")
async def get_all_books():
    return BOOKS

@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return

@app.get("/books/byauthor/{author}")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return