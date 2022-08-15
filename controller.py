import hashlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Pessoa


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

#session = RetornaSession()


class ControllerCadastro():
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
       
        return 1



    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = RetornaSession()
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()

        if len(usuario) > 0:
            return 5

        dados_verificados = cls.verifica_dados(nome, email, senha)

        if dados_verificados != 1:
            return dados_verificados


        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            p1 = Pessoa(nome=nome, email=email, senha=senha)
            session.add(p1)
            session.commit()
            return 1
        
        except Exception as e:
            print(e)


class ControllerLogin():
    @classmethod
    def login(cls, email, senha):
        session = RetornaSession()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        logado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).all()
        if len(logado) == 1:
            return {'logado': True, 'id': logado[0].id}
        else:
            return False

