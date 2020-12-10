from typing import List, Optional

from pydantic import BaseModel




class StudentIn(BaseModel):
    name: str
    surname: str
    email: str


class Student(BaseModel):
    id: int
    name: str
    surname: str
    email: str

    class Config:
        orm_mode = True