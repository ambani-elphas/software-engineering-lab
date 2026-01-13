from sqlalchemy.future import select
from domain.entities import Item

class SQLAlchemyItemRepository:
    def __init__(self, session):
        self.session = session

    async def get_all(self):
        result = await self.session.execute(select(Item))
        return result.scalars().all()

    async def create(self, item):
        self.session.add(item)
        await self.session.commit()
        await self.session.refresh(item)
        return item
