# database.py - Настройка базы данных
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "postgresql://myuser:mypassword@localhost/myapp_db"postgres
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/myapp_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
