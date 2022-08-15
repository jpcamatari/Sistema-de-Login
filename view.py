from controller import ControllerCadastro, ControllerLogin

while True:
    print("-----------------Sistema de Login-----------------")
    print("|| 0 - Cadastrar || 1 - Logar ||")

    escolha = int(input('Escolha uma opção: '))
    
    if escolha == 0:
        print('Insira seus dados para cadastro:')
        resultado = ControllerCadastro.cadastrar(input('Nome:'), input('Email:'), input('Senha:'))
        
        if resultado == 2:
            print("Tamanho do nome digitado inválido")
        elif resultado == 3:
            print("Email maior que 200 caracteres")
        elif resultado == 4:
            print("Tamanho da senha inválido")
        elif resultado == 5:
            print("Email já cadastrado")
        elif resultado == 6:
            print("Erro interno do sistema")
        elif resultado == 1:
            print("Cadastro realizado com sucesso")

    elif escolha == 1:
        print('Insira seus dados de login.')
        resultado = ControllerLogin.login(input('Email:'), input('Senha:'))
        if not resultado:
            print("Email ou senha Invalidos")
        else:
            print (resultado)

    
    else:
        print('Opção inválida!')
        

