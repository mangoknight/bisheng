from datetime import datetime
from typing import Optional

from bisheng.database.models.base import SQLModelSerializable
from sqlalchemy import Column, DateTime, text
from sqlmodel import Field


class KnowledgeFileBase(SQLModelSerializable):
    user_id: Optional[int] = Field(index=True)
    knowledge_id: int = Field(index=True)
    file_name: str = Field(index=True)
    md5: Optional[str] = Field(index=False)
    status: Optional[int] = Field(index=False)
    object_name: Optional[str] = Field(index=False)
    create_time: Optional[str] = Field(default=(datetime.now()).strftime('%Y-%m-%d %H:%M:%S'), index=True)
    update_time: Optional[str] = Field(default=(datetime.now()).strftime('%Y-%m-%d %H:%M:%S'), index=True)


class KnowledgeFile(KnowledgeFileBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class KnowledgeFileRead(KnowledgeFileBase):
    id: int


class KnowledgeFileCreate(KnowledgeFileBase):
    pass
