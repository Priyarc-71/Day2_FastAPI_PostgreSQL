# Day 2 - FastAPI + PostgreSQL

## Project Overview

This project demonstrates the use of FastAPI with PostgreSQL for backend API development.

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQL
- SQLAlchemy
- Pydantic
- Bcrypt

## Task Areas

1. FastAPI integration
2. SQL queries and JOIN operations
3. PostgreSQL database
4. Basic authentication

## API Endpoints

- GET `/` - Check API status
- GET `/students` - Get students
- POST `/students` - Add a student
- PUT `/students/{student_id}` - Update a student
- DELETE `/students/{student_id}` - Delete a student
- POST `/register` - Register a user
- POST `/login` - Verify login credentials

## Authentication

Basic authentication was implemented using:

Register → Password Hashing → Login → Password Verification

## Database

PostgreSQL was used to store:

- Departments
- Students
- Users
