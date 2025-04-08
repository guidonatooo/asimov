#Exercicio 01
n1 = [0, 1, 2, 3]
n2 = [3, 4, 5, 1, 2, 0]
for lista1 in n1:
    for lista2 in n2:
        if lista1 == lista2:
            print(f'Os valores duplicados são: {lista2}\n')
            
#Exercicio 02
info1 = ['x', 0, 5, 'for',]
info2 = ['G', 0, 10, 'for']

comum=False

for elementos1 in info1:
    for elementos2 in info2:
        if elementos1 == elementos2:
            comum=True
if comum:
       print(f'Dentro de {info1} e {info2}, os elementos em comum são: {elementos1}\n')
else:
    print(f'Não existem elementos em comum')   
            
    