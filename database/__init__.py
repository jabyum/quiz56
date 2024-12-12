from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# подключение к файлу/серверу базы данных
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
# создаю движок для своей базы данных
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# создаю функцию для создания сессий
SessionLocal = sessionmaker(bind=engine)
# создаю суперкласс для моделей (потом буду его наследовать)
Base = declarative_base() # как Model в джанго

# создание функции-генератора сессий
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


