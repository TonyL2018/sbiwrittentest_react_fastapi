"""import uvicorn
from models import User as ModelUser
from schema import User as SchemaUser
from app import app
from db import db


@app.post("/user/")
async def create_user(user: SchemaUser):
    user_id = await ModelUser.create(**user.dict())
    return {"user_id": user_id}


@app.get("/user/{id}", response_model=SchemaUser)
async def get_user(id: int):
    user = await ModelUser.get(id)
    return SchemaUser(**user).dict()
"""

import uvicorn

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from schemas import EmployeeCreate, Employee
# from crud import crud
from models import Base
# from schemas import schemas
from database import SessionLocal, engine

from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees/", response_model=Employee)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)


@app.post("/employees/update", response_model=Employee)
def create_employee(employee: Employee, db: Session = Depends(get_db)):
    return crud.update_employee(db=db, employee=employee)

@app.get("/employees/delete/{code}", response_model=Employee)
def delete_employee(code: str, db: Session = Depends(get_db)):
    return crud.delete_employee(db=db, code=code)

@app.get("/employees/", response_model=List[Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees


@app.get("/employees/{code}", response_model=Employee)
def read_employee(code: str, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, code=code)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
