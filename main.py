from typing import Union
from jsonschema import validate, ValidationError
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from loguru import logger

from fastapi import FastAPI

app = FastAPI()

class UserLogin(BaseModel):
    email: str
    password: str

login_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string", "minLength": 8}
    },
    "required": ["email","password"]
}



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/signup")
def signup(user: UserLogin):
    try:
        validate(instance=user, schema=login_schema)
        return{
            "success": True,
            "error": False,
            "data":{
                "signed_up": True,
                "user": user.email
            }
        }
    except ValidationError as ve:
        logger.error(ve.message)
        return JSONResponse(status_code=400,content={
            "success": False,
            "error": True,
            "message": "Unable to create the user"
        })
