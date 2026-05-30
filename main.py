from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

#Post request to create a new user
@app.post("/create-user")
def create_user(user: User):
    return {
        "Message": "User created successfully",
        "data": user
    }
