from fastapi import FastAPI
from api.user_api.users import user_router
from database import Base, engine
app = FastAPI(docs_url="/")
# создаем бд и делаем миграцию
Base.metadata.create_all(bind=engine)
# регистрации компонентов (роутеров) проекта
app.include_router(user_router)
# запуск проект uvicorn main:app --reload


