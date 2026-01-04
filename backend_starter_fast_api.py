# backend/src/app.py
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Software Engineering Lab API")

# ------------------
# Models
# ------------------
class HealthResponse(BaseModel):
    status: str

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

# ------------------
# In-memory store (for lab purposes)
# ------------------
ITEMS_DB: List[Item] = []

# ------------------
# Routes
# ------------------
@app.get("/health", response_model=HealthResponse)
def health_check():
    return {"status": "ok"}

@app.get("/items", response_model=List[Item])
def list_items():
    return ITEMS_DB

@app.post("/items", response_model=Item)
def create_item(item: Item):
    for existing in ITEMS_DB:
        if existing.id == item.id:
            raise HTTPException(status_code=400, detail="Item already exists")
    ITEMS_DB.append(item)
    return item

# ------------------
# Run with:
# uvicorn app:app --reload
# ------------------
