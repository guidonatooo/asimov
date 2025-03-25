print (f'Cifra de Cesar')

texto = 'ABC'
chave = 2

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cifra = ''

def cifrar_caractere(caracter, seq, chave):
    indice_atual = seq.index(caracter)
    novo_indice = (indice_atual + chave) % len(seq)
    while novo_indice >= len(seq):
        novo_indice = novo_indice - len(seq)
    while novo_indice < 0:
        novo_indice = novo_indice + len(seq)
    return seq[novo_indice]

for caracter in texto:
    if caracter in minusculas:
        cifra += minusculas[(minusculas.index(caracter) + chave) % 26]
    elif caracter in maiusculas:
        cifra += maiusculas[(maiusculas.index(caracter) + chave) % 26]
    else:
        cifra += caracter
    
print(f'Texto cifrado: {cifra}')