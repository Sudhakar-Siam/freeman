from typing import Dict, List,Optional
from pydantic import BaseModel,root_validator
from datetime import datetime, date
from uuid import UUID, uuid4


class Role(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime


class RoleByMenuAccess(BaseModel):
    id: UUID
    role_id: str
    menu_show: Dict
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime


class User(BaseModel):
    id: UUID = uuid4()
    role_id: Optional[str]
    username: str
    email: str
    phone_number: Optional[str]
    password: str
    is_active: bool=True
    is_agree: bool=False
    last_login: datetime
    is_reset_mail_send: bool=False
    reset_link: Optional[str]
    otp: Optional[int]
    pin: Optional[int]
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime

    @root_validator(pre=True, allow_reuse=True)
    def set_default_created_at(cls, values):
        values['created_at'] = values.get('created_at') or datetime.utcnow()
        return values


class UserProfile(BaseModel):
    id: UUID
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
    id: UUID
    user: str
    pancard_details: Dict
    aadhar_details: Dict
    photo_upload: str  # filefield
    salary_slip: str  # filefield
    bank_details: Dict
    bank_statement: str  # filefield
    Declaration: str


class Option(BaseModel):
    id: UUID
    meta_key: str
    title: str
    meta_value: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime


class BankDetails(BaseModel):
    id: UUID
    name: str
    logo: str  # filefield
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
