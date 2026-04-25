import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary="Root", tags=["Get welcome message"])
def home():
    return "Hello World!"

if __name__ == "__main__":
    # ============================================================
    # THREE WAYS TO RUN FASTAPI
    # ============================================================
    #
    # 1. fastapi dev main.py
    #    - Simplest way (modern approach)
    #    - Auto-reload on code changes
    #    - Clear error messages
    #    - NEW METHOD (FastAPI CLI)
    #
    # 2. uvicorn main:app --reload
    #    - Classic way
    #    - main:app = "filename:FastAPI_variable_name"
    #    - --reload = auto-restart when code changes
    #    - More control over server parameters
    #
    # 3. python main.py (via uvicorn.run())
    #    - Convenient for scripts
    #    - Can be embedded in other code
    #    - Parameters are set directly in code
    #    - Requires if __name__ == "__main__" block
    #
    # ============================================================
    uvicorn.run("main:app", reload=True)