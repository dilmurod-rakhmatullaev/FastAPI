import uvicorn
from fastapi import FastAPI

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


@app.get("/books")
def read_books():
    return books



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
