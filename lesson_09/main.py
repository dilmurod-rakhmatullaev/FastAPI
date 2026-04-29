from typing import Callable
import time
from fastapi import FastAPI, Request, Response
import uvicorn

app = FastAPI()


@app.middleware("http")
async def middleware(request: Request, call_next: Callable):
    ip_address = request.client.host
    print(f"Making request to {ip_address}")
    # if ip_address in ["127.0.0.1", "localhost"]:
    #    return Response(status_code=429, content="You are sending too many requests")

    start = time.perf_counter()
    response = await call_next(request)
    end = time.perf_counter() - start
    print(f"Request time: {end} seconds")
    response.headers["X-Special"] = "Special one"
    return response


@app.get("/users")
def get_users():
    time.sleep(0.5)
    return [
        {
            "id": 1,
            "name": "Arsenal"
        }
    ]

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)