#alembic init alembic
from database import Base
from domain.entities import Item

target_metadata = Base.metadata

#alembic revision --autogenerate -m "create items table"
#alembic upgrade head


