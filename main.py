from fastapi import FastAPI
import bcrypt

from database import SessionLocal
import models
from schemas import StudentCreate, StudentUpdate, UserCreate, UserLogin

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI + PostgreSQL is working!"}


@app.get("/students")
def get_students():
    db = SessionLocal()
    students = db.query(models.Student).all()
    db.close()
    return students


@app.post("/students")
def add_student(student: StudentCreate):
    db = SessionLocal()

    new_student = models.Student(
        student_name=student.student_name,
        email=student.email,
        department_id=student.department_id
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()

    return new_student


@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    db = SessionLocal()

    data = db.query(models.Student).filter(
        models.Student.student_id == student_id
    ).first()

    if not data:
        db.close()
        return {"message": "Student not found"}

    data.student_name = student.student_name
    data.email = student.email
    data.department_id = student.department_id

    db.commit()
    db.refresh(data)
    db.close()

    return data


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    db = SessionLocal()

    data = db.query(models.Student).filter(
        models.Student.student_id == student_id
    ).first()

    if not data:
        db.close()
        return {"message": "Student not found"}

    db.delete(data)
    db.commit()
    db.close()

    return {"message": "Student deleted"}


@app.post("/register")
def register(user: UserCreate):
    db = SessionLocal()

    password = user.password.encode()
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    new_user = models.User(
        username=user.username,
        password=hashed_password.decode()
    )

    db.add(new_user)
    db.commit()
    db.close()

    return {"message": "User registered"}


@app.post("/login")
def login(user: UserLogin):
    db = SessionLocal()

    data = db.query(models.User).filter(
        models.User.username == user.username
    ).first()

    if not data:
        db.close()
        return {"message": "User not found"}

    password = user.password.encode()
    stored_password = data.password.encode()

    if bcrypt.checkpw(password, stored_password):
        db.close()
        return {"message": "Login successful"}

    db.close()
    return {"message": "Wrong password"}