import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        connection = psycopg2.connect(
            dbname="myapp_db",
            user="myuser",
            password="mypassword",
            host="localhost"
        )
        print("Соединение с базой данных успешно!")
        return connection
    except OperationalError as e:
        print(f"Ошибка подключения: {e}")
        return None

# Проверка соединения
conn = create_connection()
if conn:
    conn.close()