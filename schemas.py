from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str
    id: int