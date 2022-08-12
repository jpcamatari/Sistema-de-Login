from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "login-system"
PORT = "3306"

CON = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CON, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(50))
    senha = Column(String(10))

Base.metadata.create_all(engine)