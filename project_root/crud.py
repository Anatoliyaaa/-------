# crud.py - Логика работы с БД
from sqlalchemy.orm import Session
from models import User  # <-- Убедитесь, что импорт без ошибок


def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    # Функция для получения всех пользователей из базы данных
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, name: str, email: str):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user