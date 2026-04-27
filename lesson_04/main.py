from fastapi import FastAPI, File, UploadFile
from typing import Annotated, List
from fastapi.responses import StreamingResponse, FileResponse

app = FastAPI()

@app.post("/files")
async def upload_file(uploaded_file: UploadFile):
    content = await uploaded_file.read()
    with open(f"1_{uploaded_file.filename}", "wb") as f:
        f.write(content)
    return {"filename": uploaded_file.filename, "status": "uploaded"}

@app.post("/multiple_files")
async def upload_multiple_files(
    files: Annotated[List[UploadFile], File(description="Select one or more files to upload")]
):
    saved_files = []
    for uploaded_file in files:
        content = await uploaded_file.read()
        filename = f"1_{uploaded_file.filename}"
        with open(filename, "wb") as f:
            f.write(content)
        saved_files.append({"original": uploaded_file.filename, "saved_as": filename})
    return {"uploaded": saved_files}

@app.get("/files/{filename}")
async def get_file(filename: str):
    return FileResponse(f"1_{filename}")


def iterfile(filename: str):
    with open(filename, "rb") as file:
        while chunk := file.read(1024 * 1024):
            yield chunk


@app.get("/files/streaming/{filename}")
async def get_streaming_file(filename: str):
    return StreamingResponse(iterfile(filename), media_type="video/mp4")