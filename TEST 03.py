#Exercicio 01
#VALORES
valores = [0, 5, 10, 15, -20, -10]
soma = 0
#SOMA
for valor in valores:
    soma += valor
#MEDIA
media = soma / len(valores)
#RESULTADO SOMA 
print('\n' f'Resultado {soma}\n')
#RESULTADO MEDIA
print (f'Media {media}')
print('\n')
#Exercicio 02
#VALORES
valores = [0, 5, 10, 15, -20, -10]
maximo = valores [0]
for valor in valores:
    if valor > maximo:
        maximo = valor
print(f'O valor maximo é: {maximo}\n')

palavras = ['Guilherme', 'Gui', 'Donato', 'Moraes', 'Vê']
for palavra in palavras:
    if len(palavra) >= 5:
        print(f'Palavra acima de 5 caracteres: {palavra}\n')

