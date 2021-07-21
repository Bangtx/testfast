from fastapi import FastAPI, Depends
from typing import Optional, re
from pydantic import BaseModel
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


@app.post("/users/", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    # db_user = crud.get_user_by_email(db, email=user.email)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    print('xxx')
    print(user, db)
    db_user = models.UserModel(id=user.id, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return 'ok'


@app.get('/')
def getuser(user: User, db: Session = Depends(get_db)):
    return db.query(models.UserModel).all()

