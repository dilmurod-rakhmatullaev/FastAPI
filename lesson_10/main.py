from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("table cleared")
    await create_tables()
    print("table created")
    yield
    print("Switching off")


app = FastAPI(lifespan=lifespan)
app.include_router(router)

