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
