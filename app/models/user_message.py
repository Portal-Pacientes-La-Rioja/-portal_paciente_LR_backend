from sqlalchemy import Column, Integer, String, DateTime

from app.config.database import Base

class UserMessage(Base):

    __tablename__ = "user_message"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, nullable=False)
    id_message = Column(Integer, nullable=False)
    read_datetime = Column(DateTime, nullable=False)


