from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Books API", description="Simple CRUD for books management")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:63342"]
)

class BookCreate(BaseModel):
    title: str
    author: str
    year: int


class Book(BookCreate):
    id: int


books_db = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthews", "year": 2019},
    {"id": 2, "title": "FastAPI Guide", "author": "John Doe", "year": 2023},
]


def get_next_id():
    return max([book["id"] for book in books_db], default=0) + 1


# ==================== GET /books ====================
@app.get("/books", response_model=List[Book], summary="Get Books")
async def get_books():
    return books_db


# ==================== POST /books ====================
@app.post("/books", response_model=Book, status_code=201, summary="Add Book")
async def add_book(book: BookCreate):
    new_book = {
        "id": get_next_id(),
        "title": book.title,
        "author": book.author,
        "year": book.year
    }
    books_db.append(new_book)
    return new_book


# ==================== PUT /books/{book_id} ====================
@app.put("/books/{book_id}", response_model=Book, summary="Change Book")
async def update_book(book_id: int, book: BookCreate):
    for index, existing_book in enumerate(books_db):
        if existing_book["id"] == book_id:
            updated_book = {
                "id": book_id,
                "title": book.title,
                "author": book.author,
                "year": book.year
            }
            books_db[index] = updated_book
            return updated_book

    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")


# ==================== DELETE /books/{book_id} ====================
@app.delete("/books/{book_id}", summary="Delete Book")
async def delete_book(book_id: int):
    for index, existing_book in enumerate(books_db):
        if existing_book["id"] == book_id:
            books_db.pop(index)
            return {"message": f"Book with id {book_id} deleted successfully"}

    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")


# ==================== GET /books/{book_id} ====================
@app.get("/books/{book_id}", response_model=Book, summary="Get book by ID")
async def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")