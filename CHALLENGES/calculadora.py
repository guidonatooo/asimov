import os

print ("====================")
operations = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão"
}


while True:
    os.system("clear")
    i = 0
    for op, name in operations.items():
        print(i, ":", name)
        i += 1
    print("Escolha a operação que deseja realizar:")
    op = int(input())
    op_string = list(operations.keys())
    if op not in operations:
        print("Operação inválida")
    print("===========")    
    print("Digite o primeiro número:")
    num1 = float(input())
    print("===========")
    print("Digite o segundo número:")
    num2 = float(input())
    
    if op == 0:
        print("Resultado:", num1 + num2)
    elif op == 1:
        print("Resultado:", num1 - num2)
    elif op == 2:
        print("Resultado:", num1 * num2)
    else:
        print("Resultado:", num1 / num2)
    print("===========")
    print("Deseja realizar outra operação? (s/n)")
    if input() != "s":
        break
print("Fim do programa")
print("===========")
  