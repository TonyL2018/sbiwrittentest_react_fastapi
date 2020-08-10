from typing import List, Optional

from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    age: int
    address: str
    department: str

class Employee(EmployeeCreate):
    code: str

    class Config:
        orm_mode = True
