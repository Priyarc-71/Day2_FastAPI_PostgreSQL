from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

DB_PASSWORD = "YOUR_PASSWORD""

DATABASE_URL = (
    f"postgresql+psycopg://postgres:{quote_plus(DB_PASSWORD)}"
    "@localhost:5432/day2_fastapi"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()