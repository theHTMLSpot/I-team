# main.py
from fastapi import FastAPI, HTTPException
from __init__ import initialize_db
import services
from uuid import UUID

app = FastAPI()

# Initialize the database when the application starts
initialize_db()

@app.post("/insert_user")
async def insert_user(name: str, email: str, cv: str = None, id: UUID = None):
    try:
        services.insert_user(name, email, cv)
        return {"message": "User inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_users")
async def get_users():
    try:
        users = services.get_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_user/")
async def get_user(email: str, name: str):
    try:
        user = services.get_user(name, email)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.put("/verify_user/")
async def verify_user(email: str, name: str):
    try:
        user = services.verify_user(name, email)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User successfully verified"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    