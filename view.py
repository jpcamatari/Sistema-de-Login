
print("-----------------Sistema de Login-----------------")
print("|| 0 - Cadastrar || 1 - Logar ||")

while True:

    try:
        escolha = int(input('Escolha uma opção: '))
        if escolha == 0:
            print('Cadastrando')
            break
        elif escolha == 1:
            print('Logando')
            break
        else:
            print('Opção inválida!')

    except ValueError:
        print('Valor informado não é numérico!')
