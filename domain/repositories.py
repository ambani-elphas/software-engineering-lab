from abc import ABC, abstractmethod

class ItemRepository(ABC):
    @abstractmethod
    async def get_all(self): ...

    @abstractmethod
    async def create(self, item): ...
