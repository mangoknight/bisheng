from datetime import datetime
from typing import Optional

from bisheng.database.models.base import SQLModelSerializable
from sqlalchemy import Column, DateTime, text
from sqlmodel import Field


class UserBase(SQLModelSerializable):
    user_name: str = Field(index=True, unique=True)

    email: Optional[str] = Field(index=True)
    phone_number: Optional[str] = Field(index=True)
    remark: Optional[str] = Field(index=False)
    role: str = Field(index=False, default='user')
    delete: int = Field(index=False, default=0)
    create_time: Optional[datetime] = Field(
        sa_column=Column(
            DateTime,
            nullable=False,
            index=True,
            server_default=text('CURRENT_TIMESTAMP')
        )
    )
    update_time: Optional[datetime] = Field(
        sa_column=Column(
            DateTime,
            nullable=False,
            server_default=text('CURRENT_TIMESTAMP'),
            onupdate=text('CURRENT_TIMESTAMP')
        )
    )


class Users(UserBase, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    passwords: str = Field(index=False)


class UserRead(UserBase):
    user_id: Optional[int]


class UserQuery(UserBase):
    user_id: Optional[int]
    user_name: Optional[str]


class UserLogin(UserBase):
    password: str
    user_name: str


class UserCreate(UserBase):
    password: str


class UserUpdate(SQLModelSerializable):
    user_id: int
    delete: Optional[int] = 0
