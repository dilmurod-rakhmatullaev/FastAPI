import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Asyncio in Python",
        "author": "Andrew",
    },
    {
        "id": 2,
        "title": "Backend Python",
        "author": "Bob",
    },
]


@app.get("/books",
         tags=["📚 books"],
         summary="Get all books"
)
def read_books():
    return books


@app.get("/books/{book_id}",
         tags=["📚 books"],
         summary="Get book by id"
)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


class NewBook(BaseModel):
    title: str
    author: str

@app.post("/books",
          tags=["📚 books"],
          summary="Create a new book",)
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author
    })
    return {"success": True, "message": "Book created"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)