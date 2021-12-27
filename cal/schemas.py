from datetime import datetime
from typing import List

from pydantic import BaseModel
from pydantic.types import UUID4


class EventBase(BaseModel):
    name: str
    description: str
    date_start: datetime
    date_end: datetime


class EventCreate(EventBase):
    pass


class Event(EventBase):
    uuid: UUID4
    owner_uuid: UUID4

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    uuid: UUID4
    items: List[Event] = []

    class Config:
        orm_mode = True
