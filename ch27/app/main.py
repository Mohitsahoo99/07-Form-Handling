## Handel Form Data

from fastapi import FastAPI, Form 
from typing import Annotated
from fastapi.responses import HTMLResponse
app = FastAPI()

### application/x-www-form-urlencoded --> media type 
## multipart/form-data

# # Simple HTML form for testing
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body>
            <h2>Login Form</h2>
            <form action="/login/" method="post">
                <label for="username">Username: </label><br>
                <input type="text" id="username"
                name="username"><br>
                <label for="password">Password :</label><br>
                <input type="password" id="password"
                name="password"><br><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </htm1>
    """    

# @app.post("/login/")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username, "password": len(password)}


## Validation in this
@app.post("/login/")
async def login(
    username: Annotated[str, Form(min_length=3, max_length=20)],
    password: Annotated[str, Form(min_length=3, max_length=8)]
    ):
    return {"username": username, "password": len(password)}