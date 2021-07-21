from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from schemas import *
from database import *


Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/")
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = models.UserModel(id=user.id, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return 'ok'


@app.get('/')
def getuser():
    return "ok"

