from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime,\
                       create_engine
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
connection_string = 'sqlite:///' + os.path.join(BASE_DIR, 'site.db')

Base = declarative_base()
engine = create_engine(connection_string, echo=True)
Session = sessionmaker(bind=engine)

"""
class User
    id int
    username varchar(255)
    email  varchar(255)
    date_created datetime
"""


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    date_created = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<User(id='{self.id}', username='{self.username}', email='{self.email}',date_created='{self.date_created}')>"


new_user = User(id=1, username='joe', email='joe@gmail.com')
print(new_user)
