from typing import Dict, List
from pydantic import BaseModel


class Role(BaseModel):
    _id: str
    name: str
    created_at: str
    updated_at: str
    deleted_at: str


class RoleByMenuAccess(BaseModel):
    _id: str
    role_id: str
    menu_show: Dict
    created_at: str
    updated_at: str
    deleted_at: str


class User(BaseModel):
    _id: str
    role_id: str
    username: str
    email: str
    phone_number: str
    password: str
    is_active: bool
    is_agree: bool
    last_login: str
    is_reset_mail_send: bool
    reset_link: str
    otp: int
    pin: int
    created_at: str
    updated_at: str
    deleted_at: str


class UserProfile(BaseModel):
    _id: str
    user: str
    dob: str
    age: int
    gender: str
    phone_no: str
    pan_number: str
    upload_image: str
    marital_status: str
    address: Dict
    dashboard_users_count: Dict
    dashboard_stock_execution_count: Dict
    certification_details: Dict
    experience_details: Dict
    education_details: Dict


class UserOnboarding(BaseModel):
    _id: str
    user: str
    pancard_details: Dict
    aadhar_details: Dict
    photo_upload: str
    salary_slip: str
    bank_details: Dict
    bank_statement: str
    Declaration: str


class Option(BaseModel):
    id: str
    meta_key: str
    title: str
    meta_value: str
    created_at: str
    updated_at: str
    deleted_at: str


class BankDetails(BaseModel):
    _id: str
    name: str
    logo: str
    created_at: str
    updated_at: str
    deleted_at: str
