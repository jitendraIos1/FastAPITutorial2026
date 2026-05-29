from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return {"message": "Welcome to fastAPI VENV"}

#about Route

@app.get("/about")
def about():
    return {"message": "This is about us page"}

#Users Route

@app.get("/users/{user_id}")
def get_users(user_id:str):
    return {"user_id": user_id}