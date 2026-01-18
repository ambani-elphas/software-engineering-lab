from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from infrastructure.sqlalchemy_repository import SQLAlchemyItemRepository
from domain.entities import Item
from auth.dependencies import get_current_user

app = FastAPI()

@app.get("/items")
async def list_items(
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
):
    repo = SQLAlchemyItemRepository(db)
    return await repo.get_all()
