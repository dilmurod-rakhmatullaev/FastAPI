import asyncio
import time
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def send_mail():
    time.sleep(3)
    print("Email sent!")

async def call_external_api():
    await asyncio.sleep(3)
    print("API call completed!")


@app.post("/send-email")
async def email_route(bg_tasks: BackgroundTasks):
    bg_tasks.add_task(send_mail)
    return {"ok": True, "message": "Email will be sent in background"}

@app.post("/call-api")
async def api_route():
    asyncio.create_task(call_external_api())
    return {"ok": True, "message": "API call started in background"}