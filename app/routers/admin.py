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
    admin_user = dict(role_id=str(admin_role["_id"]), username=user.username, email=user.email,
                      phone_number=user.phone_number,
                      password=hashed_password, is_active=True, is_agree=False, last_login=None,
                      is_reset_mail_send=False, reset_link=None, pin=None,
                      updated_at=None, deleted_at=None
                      )
    users_collection.insert_one(admin_user)

    return {"message": "Admin user registered successfully"}
