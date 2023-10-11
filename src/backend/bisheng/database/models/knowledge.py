from datetime import datetime
from typing import Optional

from bisheng.database.models.base import SQLModelSerializable
from sqlalchemy import Column, DateTime, text
from sqlmodel import Field


class KnowledgeBase(SQLModelSerializable):
    user_id: Optional[int] = Field(index=True)
    name: str = Field(index=True)
    description: Optional[str] = Field(index=True)
    model: Optional[str] = Field(index=False)
    collection_name: Optional[str] = Field(index=False)
    create_time: Optional[str] = Field(default=(datetime.now()).strftime('%Y-%m-%d %H:%M:%S'), index=True)
    update_time: Optional[str] = Field(default=(datetime.now()).strftime('%Y-%m-%d %H:%M:%S'), index=True)


class Knowledge(KnowledgeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class KnowledgeRead(KnowledgeBase):
    id: int
    user_name: Optional[str]


class KnowledgeCreate(KnowledgeBase):
    pass
