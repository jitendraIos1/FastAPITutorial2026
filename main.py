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

@app.get("/users")
def users():
    return {
        "users": ["Ravi", "Suresh", "Kumar"]
        }
