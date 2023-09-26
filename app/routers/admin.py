# from datetime import datetime
# from fastapi import APIRouter
# from settings import db
# from utils.password_hash import hash_password
# from models.models import User
#
# router = APIRouter()
# users_collection = db["users"]
# roles_collection = db["roles"]
#
# @router.post("/admin-register")
# async def register_admin_user(user: User):
#     admin_role = roles_collection.find_one({"name": "admin"})
#     hashed_password = hash_password(user.password)
#     admin_user = {
#         "role_id": str(admin_role["_id"]),
#         "username": user.username,
#         "email": user.email,
#         "password": hashed_password,
#         "created_at": datetime.utcnow(),
#         "updated_at": datetime.utcnow(),
#         "deleted_at": None,
#     }
#
#     users_collection.insert_one(admin_user)
#
#     return {"message": "Admin user registered successfully"}
#
#
#
