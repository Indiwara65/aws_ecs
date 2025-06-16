#External Dependencies
from fastapi import FastAPI, Cookie, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from typing import Annotated
import uvicorn

#Internal Dependencies
import data_classes as dc
from routers import users

#Variables
app = FastAPI()
app.mount("/static",StaticFiles(directory=Path("static")),name="static")
templates = Jinja2Templates(directory=Path("templates"))

#Routes
app.include_router(users.router)

@app.get("/health", response_class=JSONResponse)
async def health():
    #check s3 connection
    #check dynamo db connection
    status = "Ok"
    return {"status":status}

@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    session = None
    #not logged in
    if session is None:
        return templates.TemplateResponse(request=request, name="login.html")
    #check sessionId in DB
    #home page


if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8090, reload=True)