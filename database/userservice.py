from database import get_db
from database.models import *

# функция добавления юзера
def add_user_db(name, phone):
    # создаем сессию
    db = next(get_db())
    # создаем объект нового пользователя по шаблону класса
    new_user = User(username=name, phone_number=phone)
    # добавляем объект (нового юзера) в базу данных
    db.add(new_user)
    # сохраняем изменения произведенные в бд
    db.commit()
    return True
def get_all_users_db():
    db = next(get_db())
    # создаем запрос в базу данных
    all_users = db.query(User).all()
    return all_users
def get_exact_user_db(user_id):
    db = next(get_db())
    # создаем запроc, но с фильтрацией
    exact_user = db.query(User).filter_by(id=user_id).first()
    return exact_user
# функция сохранения ответов юзера
def user_answer_db(user_answer, user_id, q_id, level):
    db = next(get_db())
    exact_question = db.query(Question).filter_by(id=q_id).first()
    answers = ["", exact_question.v1, exact_question.v2,
               exact_question.v3, exact_question.v4]
    if answers.index(user_answer) == exact_question.correct_answer:
        correctness = True
    else:
        correctness = False
    exact_rating = db.query(Rating).filter_by(user_id=user_id).first()
    if exact_rating:
        if correctness == True:
            exact_rating.correct_answers += 1
            db.commit()
            return True
        return False
    elif not exact_rating:
        if correctness == True:
            new_rating = Rating(user_id=user_id, level=level, correct_answers=1)
            db.add(new_rating)
            db.commit()
            return True
        else:
            new_rating = Rating(user_id=user_id, level=level)
            db.add(new_rating)
            db.commit()
            return False









