from typing import Dict, List, Optional
from pydantic import BaseModel, model_validator,Field
from datetime import datetime, date
from uuid import UUID, uuid4


class Role(BaseModel):
    name: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime


class RoleByMenuAccess(BaseModel):
    role_id: str
    menu_show: Dict
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime


class User(BaseModel):
    role_id: Optional[str] = None
    username: str
    email: str
    phone_number: Optional[str] = None
    password: str
    is_active: bool = True
    is_agree: bool = False
    last_login: Optional[datetime]=None
    is_reset_mail_send: bool = False
    reset_link: Optional[str] = None
    otp: Optional[int] = None
    pin: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    @model_validator(pre=True, allow_reuse=True)
    def set_default_values(cls, values):
        values['created_at'] = values.get('created_at') or datetime.utcnow()
        values['otp'] = values.get('otp') or None
        return values


class UserProfile(BaseModel):
    user: str
    dob: date
    age: int
    gender: str
    phone_no: str
    pan_number: str
    upload_image: str  # filefield
    marital_status: str
    address: Dict
    dashboard_users_count: Dict
    dashboard_stock_execution_count: Dict
    certification_details: Dict
    experience_details: Dict
    education_details: Dict


class UserOnboarding(BaseModel):
    user: str
    pancard_details: Dict
    aadhar_details: Dict
    photo_upload: str  # filefield
    salary_slip: str  # filefield
    bank_details: Dict
    bank_statement: str  # filefield
    Declaration: str


class Option(BaseModel):
    meta_key: str
    title: str
    meta_value: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime


class BankDetails(BaseModel):
    name: str
    logo: str  # filefield
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
