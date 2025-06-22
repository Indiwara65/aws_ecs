from enum import Enum
from pydantic import BaseModel, Field

#Data Models
class Role(str, Enum):
    admin       = "admin"
    jobManager  = "job manager"
    storeKeeper = "store keeper"  
    worker      = "worker"

class User(BaseModel):
    firstname : str = Field(min_length=3, max_length=24)
    lastname  : str = Field(min_length=3, max_length=24)
    password  : str = Field(min_length=10)
    role      : Role

class Login(BaseModel):
    username  : str
    password  : str
    long_live : str = Field(default="off")

class Session(BaseModel):
    sessionID : int