from fastapi import FastAPI, Depends, HTTPException
from pydantic.types import UUID4
from sqlalchemy.orm.session import Session

from cal import crud, models, schemas
from cal.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/user/{user_uuid}', response_model=schemas.User)
async def root(user_uuid: UUID4, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_uuid=user_uuid)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return
