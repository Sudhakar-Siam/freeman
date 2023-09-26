from fastapi import APIRouter
from ..utils.auth import create_access_token
from ..utils.password import hash_password, verify_password
from app.settings import db

router = APIRouter()
users_collection = db["users"]


@router.post("/register")
async def register_user(user: User):
    hashed_password = hash_password(user.password)
    users_collection.insert_one({"username": user.username, "password": hashed_password})
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: User):
    stored_user = db.users.find_one({"username": user.username})
    if stored_user and verify_password(user.password, stored_user["password"]):
        token = create_access_token(user.username)
        return {"message": "Login successful", "token": token}
    return {"message": "Login failed"}

@router.post("/forgot-password")
async def forgot_password(username: str):
    # Implement the forgot password logic here
    # Generate a reset token and send it to the user's email
    return {"message": "Password reset instructions sent to your email"}

@router.post("/reset-password")
async def reset_password(username: str, token: str, new_password: str):
    # Implement the password reset logic here
    # Verify the token and update the user's password
    return {"message": "Password reset successful"}
