## Singal file Upload


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
            <h2>Single File Upload(bytes)</h2>
            <form action="/files/" enctype= "multipart/form-data"
              method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>
            <h2>Single File Upload(Uploadfiles)</h2>
            <form action="/uploadfile/" enctype= "multipart/form-data"
              method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

# @app.post("/files/")
# async def create_file(file:Annotated[bytes | None, File()]= None):
#     if not file:
#         return {"message": "no file sent"}
#     return{"file_size": len(file)}





# @app.post("/files/")
# async def create_file(file:Annotated[bytes | None, File()]= None):
#     if not file:
#         return {"message": "no file sent"}
    
#     filename = f"{uuid.uuid4()}.bin"
#     save_path = f"uploads/{filename}"

#     os.makedirs("uploads", exist_ok=True)

#     with open(save_path, "wb") as buffer:
#         buffer.write(file)
#     return{"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file:Annotated[UploadFile | None, File()]= None):
    if not file:
        return {"message": "no upload file sent"}
    
    save_path = f"uploads/{file.filename}"

    os.makedirs("uploads", exist_ok=True)

    with open(save_path, "wb") as buffer:
       shutil.copyfileobj(file.file,buffer)
    return{"filename": file.filename, "content_type":file.content_type}