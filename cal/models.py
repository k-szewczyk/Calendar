from sqlalchemy import DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String

from cal.database import Base


class User(Base):
    __tablename__ = 'users'
    uuid = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    events = relationship('Event', back_populates='owner')


class Event(Base):
    __tablename__ = 'events'
    uuid = Column(String, primary_key=True, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    name = Column(String)
    description = Column(String)
    owner_uuid = Column(String, ForeignKey("users.uuid"))

    owner = relationship('User', back_populates='events')
