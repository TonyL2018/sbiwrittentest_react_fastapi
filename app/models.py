from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Employee(Base):
    __tablename__ = "employees"

    code = Column(String, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    address = Column(String)
    department = Column(String)
