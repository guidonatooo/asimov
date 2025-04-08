#db com usuario e senha
usuario = 'Gui'
senha = '123'
#inicio
print("---Meu primeiro desafio---")
#Pedir usuario e senha
Login = input("Qual o seu usuario?")
Password = input("Qual a sua senha?")
#Identificar
if Login == usuario and Password == senha:
    print(f'Acesso autorizado, bem vindo {Login}!')
elif Login != usuario:
    print(f'usuario {Login} não cadastrado')
elif Password != senha:
    print(f'senha incorreta para usuário {Login}')
elif usuario != 'Pedro' and senha != 'senha':
        print(f'usuario e senha errados')
