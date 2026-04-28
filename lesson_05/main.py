from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users")
def get_users():
    ...
    return [{"id": 1, "name": "Alex"}, {"id": 2, "name": "Bob"}]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")