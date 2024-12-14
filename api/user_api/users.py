from fastapi import APIRouter
from database.userservice import *
user_router = APIRouter(prefix="/user",
                        tags=["Пользовательская часть"])
@user_router.post("/")
async def add_user(username: str, phone_number: str,
                   level: str = "easy"):
    result = add_user_db(name=username, phone=phone_number)
    if result:
        return {"status": 1, "message": "успешно зарегистрированы"}
    return {"status": 0, "message": "ошибка регистрации"}

