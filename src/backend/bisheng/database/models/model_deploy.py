from datetime import datetime
from typing import Optional

from bisheng.database.models.base import SQLModelSerializable
from sqlalchemy import Column, DateTime, String, text
from sqlmodel import Field


class ModelDeployBase(SQLModelSerializable):
    endpoint: str = Field(index=False, unique=False)
    server: str = Field(index=True)
    model: str = Field(index=False)
    config: Optional[str] = Field(index=False, sa_column=Column(String(length=1024)))
    status: Optional[str] = Field(index=False)
    remark: Optional[str] = Field(index=False, sa_column=Column(String(length=4096)))

    create_time: Optional[str] = Field(default=(datetime.now()).strftime('%Y-%m-%d %H:%M:%S'), index=True)
    update_time: Optional[str] = Field(default=(datetime.now()).strftime('%Y-%m-%d %H:%M:%S'), index=True)


class ModelDeploy(ModelDeployBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ModelDeployRead(ModelDeployBase):
    id: Optional[int]


class ModelDeployQuery(SQLModelSerializable):
    id: Optional[int]
    server: Optional[str]


class ModelDeployCreate(ModelDeployBase):
    pass


class ModelDeployUpdate(SQLModelSerializable):
    id: int
    config: Optional[str] = None
