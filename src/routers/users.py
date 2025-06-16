#External Dependancies
from datetime import datetime
from enum import Enum
from fastapi import APIRouter, Cookie, Response
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
import random
from typing import Annotated

#Internal Dependencies
import data_classes as dc

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.put("/login")
async def login(user:dc.Login, response:Response):
    #check database
    #set cookie
    response.set_cookie(
        key   = "sessionID",
        value = random.randint(1000,10000)
    )
    print(type(user))
    return user

@router.post("/add")
async def create_user(session:Annotated[dc.Session, Cookie()], user_data:dc.User):
    print(type(session))
    print(user_data)
    return session

@router.get("/redirect")
async def redirect():
    return RedirectResponse("/")