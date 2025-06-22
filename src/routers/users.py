#External Dependancies
from datetime import datetime
from enum import Enum
from fastapi import APIRouter, Response, Request, Cookie, Form
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import random
from typing import Annotated
from pathlib import Path

#Internal Dependencies
import data_classes as dc

router = APIRouter(
    prefix="/user",
    tags=["user"]
)
templates = Jinja2Templates(directory=Path("templates"))

@router.post("/login")
async def login(user:Annotated[dc.Login, Form()], response:Response, request:Request):
    #check database
    #set cookie
    response.set_cookie(
        key   = "sessionID",
        value = random.randint(1000,10000)
    )
    print(type(user), user)
    return templates.TemplateResponse(request=request, name='home.html')

@router.post("/add")
async def create_user(session:Annotated[dc.Session, Cookie()], user_data:dc.User):
    print(type(session))
    print(user_data)
    return session

@router.get("/redirect")
async def redirect():
    return RedirectResponse("/")