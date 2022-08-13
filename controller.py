from sqlalchemy import create_engine
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


class ValidarDados():

    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        return 1



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



