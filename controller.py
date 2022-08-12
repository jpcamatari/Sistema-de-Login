from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import Usuario

def RetornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "login-system"
    PORT = "3306"

    CON = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CON, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = RetornaSession()

def CadastrarUsuario():
    cad = Usuario(nome =input("Nome:") , email = input("Email:"), senha = input("Senha:"))
    print("Você foi Cadastrado com Sucesso! Efetue o login.")

    session.add(cad)
    session.commit()

CadastrarUsuario()

