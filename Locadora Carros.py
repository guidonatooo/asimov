import os

carros = [
    ("Hyundai HB20", 120),
    ("Fiat Palio", 80),
    ("Fiat Uno", 60),
    ("Chevrolet Celta", 60),
    ("Ford Ka", 100),
]

alugados = []


def mostrar_carros(lista):
    print("Carros Disponíveis:")
    for i, car in enumerate(lista):
        print(f"[{i}] {car[0]} - R$ {car[1]} /dia.")
        

while True:
    print ("======")
    print ("Bem Vindo a Loja de Carros")
    print ("======")
    print ("Escolha uma opção")
    print ("0 - Portifólio | 1 - Alugar um carro | 2 - Devolver um carro | 3 - Sair")
    print ("======")
    try:
        op = int(input("Digite a opção desejada: "))
    except ValueError:
        print ("Opção inválida")
        continue
         
    if op == 0:
        mostrar_carros(carros)
        
    elif op == 1:
        if not carros:
            print ("Nenhum carro disponível para aluguel")
        else:
            mostrar_carros(carros)
            print("============")
            print("Escolha um carro para alugar")
            cod_car= int(input("Digite o código do carro: "))
            print("============")   
            print("Por quantos dias deseja alugar?")
            dias = int(input("Digite a quantidade de dias: "))
                        
            print("============")
            print("Resumo do Aluguel") 
            print("============")
            print("Você escolheu o carro {} por {} dias.".format(carros[cod_car][0], dias))
            print("Total a pagar: R$ {}".format(carros[cod_car][1] * dias))
            print("============")
            print("Confirma o aluguel?")
            print("1 - Sim | 2 - Não")
            confirm = int(input("Digite a opção desejada: "))
            if confirm == 1:
                print("Parabéns! Você alugou o carro {} por {} dias.".format(carros[cod_car][0], dias))
                alugados.append(carros.pop(cod_car))
            else:
                print("Aluguel cancelado.")
                
    elif op == 2:
        if not alugados:
            print ("Nenhum carro para devolver.")
        else:
            print("Carros alugados:")
            mostrar_carros(alugados)
            try: 
                carro = int(input("Escolha um carro pelo número: "))
                if 0 <= carro < len(alugados):
                    carros.append(alugados.pop(carro))
                    print ("Carro devolvido com sucesso!")
                else:
                    print ("Número inválido. Tente novamente.")        
            except ValueError:
                ("Por favor, digite um número válido.")
    else:
        print ("Obrigado por usar nosso sistema!")
        break

