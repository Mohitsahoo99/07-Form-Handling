## Multiple Files Uploads

from fastapi import FastAPI, Form, File, UploadFile
from typing import Annotated
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
import os
import uuid
import shutil
app = FastAPI()

### application/x-www-form-urlencoded --> media type 
## multipart/form-data

# # Simple HTML form for testing
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body>
            <h2>Multiple File Upload(bytes)</h2>
            <form action="/uploadfiles/" enctype= "multipart/form-data"
              method="post">
                <input name="files" type="file" multiple>
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

@app.post("/uploadfiles/")
async def create_upload_file(files:Annotated[list[UploadFile], File()]):
    save_files = []
    os.makedirs("uploads", exist_ok=True)
    for file in files:
        save_path = f"uploads/{file.filename}"
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        save_files.append({"filename" : file.filename})
    return save_files
   
