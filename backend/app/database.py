from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine( # по сути это наше соединение с базой данных
    settings.database_url, # settings имеет все параметры из класса settings в config
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # фабрика по штамповке сессий
Base = declarative_base()

def get_db():
    db = SessionLocal() # создаем сессию
    try:
        yield db # передать сессию
    finally:
        db.close() # закрыть сессию

def init_db():
    Base.metadata.create_all(bind=engine)