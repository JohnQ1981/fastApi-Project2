from fastapi import FastAPI

app = FastAPI()

BOOKS =[
    {'title': 'Hello1', 'author': 'John', 'category': 'science'},
    {'title': 'Hello2', 'author': 'Johny Writer7', 'category': 'biology'},
    {'title': 'Hello3', 'author': 'Johny Writer8', 'category': 'math'},
    {'title': 'Hello4', 'author': 'Johny Writer9', 'category': 'technology1'},
    {'title': 'Hello5', 'author': 'John', 'category': 'science'}
]


@app.get("/api-endpoint")
async def first_api():
    return {'message': 'Hello Johny1!'}

@app.get("/books")
async def read_all_books():
    return {'message': 'Hello Books1!'}

@app.get("/books1")
async def read_all_books1():
    return BOOKS

@app.get("/books/myfavbook")
async def read_all_books():
    return {'book_title': 'My Fav Book!'}

@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
                books_to_return.append(book)
    return books_to_return

# Get all books from a specific author using path or query parameters
@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return
