from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    surname = Column(String(200))
    email = Column(String, unique=True, index=True)





