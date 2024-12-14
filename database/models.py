from database import Base
from sqlalchemy import (Column, Integer, String,
                        DateTime, Boolean, ForeignKey)
from datetime import datetime
from sqlalchemy.orm import relationship

# создание моделей
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    reg_date = Column(DateTime, default=datetime.now())
# вопросы
class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    main_question = Column(String, nullable=False) # на самом деле nullable по умолчанию False
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String, nullable=True)
    v4 = Column(String, nullable=True)
    correct_answer = Column(Integer)
    level = Column(String, default="easy")
    # timer = Column(Integer, default=45)
# регистрация ответов на каждый вопрос
class UserAnswer(Base):
    __tablename__ = "useranswers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    user_answer = Column(String, nullable=True)
    # user_answer = Column(Integer, nullable=True)
    correctness = Column(Boolean, default=False)
    level = Column(String)
    # создаем связь с другими таблицами в виде подзапроса
    user_fk = relationship(User, lazy="subquery")
    question_fk = relationship(Question, lazy="subquery")

class Rating(Base):
    __tablename__ = "rating"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    correct_answers = Column(Integer, default=0)
    level = Column(String, ForeignKey("questions.level"))
    user_fk = relationship(User, lazy="subquery")
    question_fk = relationship(Question, lazy="subquery")









