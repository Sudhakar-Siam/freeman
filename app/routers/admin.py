from datetime import datetime
from fastapi import APIRouter
from settings import db
from utils.password_hash import hash_password
from models.models import User
from bson import ObjectId

router = APIRouter()
users_collection = db["users"]
roles_collection = db["role"]


@router.post("/admin-register")
async def register_admin_user(user: User):
    admin_role = roles_collection.find_one({"name": "admin"})
    hashed_password = hash_password(user.password)
    admin_user = dict(role_id="string", username="string", email="string", phone_number="string",
                         password="string", is_active=true, is_agree=false, last_login="2023-09-26T12:52:09.617Z",
                         is_reset_mail_send=false, reset_link="string", otp=0, pin=0,
                         created_at="2023-09-26T12:52:09.617Z", updated_at="2023-09-26T12:52:09.617Z",
                         deleted_at="2023-09-26T12:52:09.617Z"
                         )
    users_collection.insert_one(admin_user)

    return {"message": "Admin user registered successfully"}
