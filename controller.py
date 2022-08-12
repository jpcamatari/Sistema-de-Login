import email
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import Usuario
import re

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
    cad = Usuario(nome =str(input("Nome:")) , email = CheckEmail(input("Email:")), senha = input("Senha:"))
    

    session.add(cad)
    session.commit()


      
def CheckEmail(valid):  
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    
    while True:
        if (re.search(regex,valid)):  
            break 
            
        else:  
            email = input("Email Invalido, Digite um Email Valido:")
            break 



