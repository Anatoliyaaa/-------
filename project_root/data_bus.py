# data_bus.py
from sqlalchemy.orm import Session
from models import User
import crud

class DataBus:
    """Шина данных для обмена информацией между компонентами"""

    def __init__(self, db: Session):
        self.db = db

    def get_users(self, skip: int = 0, limit: int = 100):
        # Используем шину данных для получения пользователей
        return crud.get_users(self.db, skip, limit)
