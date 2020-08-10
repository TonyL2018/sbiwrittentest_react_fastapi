from sqlalchemy.orm import Session

from models import Employee
from schemas import EmployeeCreate # , Employee

from sqlalchemy import func

USER_CODE = 0


def get_employee(db: Session, code: str):
    return db.query(Employee).filter(Employee.code == code).first()

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Employee).offset(skip).limit(limit).all()

def update_employee(db: Session, employee: Employee):
    db.query(Employee).filter(Employee.code == employee.code).update({'name': employee.name, 'age': employee.age, 'address': employee.address, 'department': employee.department})
    db.commit()
    return employee

def delete_employee(db: Session, code: str):
    employee = db.query(Employee).filter(Employee.code == code).first()
    db.delete(employee)
    db.commit()
    return employee

def create_employee(db: Session, employee: EmployeeCreate):
    global USER_CODE
    increment_code = db.query(func.max(Employee.code)).scalar()
    if increment_code is None:
        increment_code = "0"
    USER_CODE = int(increment_code)+1
    if USER_CODE < 9:
        increment_code = "0000" + str(USER_CODE)
    elif USER_CODE < 99:
        increment_code = "000" + str(USER_CODE)
    elif USER_CODE < 999:
        increment_code = "00" + str(USER_CODE)
    elif USER_CODE < 9999:
        increment_code = "0" + str(USER_CODE)
    else:
        increment_code = "" + str(USER_CODE)
    db_employee = Employee(code=increment_code, name=employee.name, age=employee.age, address=employee.address, department=employee.department)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
