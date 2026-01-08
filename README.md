# software-engineering-lab
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
