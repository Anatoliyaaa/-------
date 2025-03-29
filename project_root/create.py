from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Настройка подключения
DATABASE_URL = "postgresql://myuser:mypassword@localhost/myapp_db"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

# Определение модели для таблицы Users
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Создание таблиц
Base.metadata.create_all(bind=engine)
