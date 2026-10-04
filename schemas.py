from pydantic import BaseModel


class StudentCreate(BaseModel):
    student_name: str
    email: str
    department_id: int


class StudentUpdate(BaseModel):
    student_name: str
    email: str
    department_id: int


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str