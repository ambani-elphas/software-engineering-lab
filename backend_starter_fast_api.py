# backend/src/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/engineering_lab"
)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------------------------
# backend/src/models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

# ---------------------------------------------
# backend/src/schemas.py
from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True

# ---------------------------------------------
# backend/src/crud.py
from sqlalchemy.orm import Session
from models import Item
from schemas import ItemCreate


def get_items(db: Session):
    return db.query(Item).all()


def create_item(db: Session, item: ItemCreate):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# ---------------------------------------------
# backend/src/app.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Software Engineering Lab API")

@app.get("/items", response_model=list[schemas.ItemResponse])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@app.post("/items", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

# ---------------------------------------------
# requirements.txt
fastapi
uvicorn
sqlalchemy
psycopg2-binary

# ---------------------------------------------
# README (Database Layer)
"""
Database Layer
--------------
PostgreSQL-backed persistence using SQLAlchemy ORM.

Run PostgreSQL:
  docker run --name lab-postgres -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=engineering_lab -p 5432:5432 -d postgres

Run API:
  uvicorn app:app --reload
"""
