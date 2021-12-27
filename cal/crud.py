from pydantic.types import UUID4
from sqlalchemy.orm import Session

from cal import models, schemas


def get_user(db: Session, user_uuid: UUID4):
    return db.query(models.User).filter(models.User.uuid == user_uuid).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
