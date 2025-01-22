import random

config = {
    "quantidade_baralhos": 1,
    "embaralhar": True,
    "incluir_coringa": True,
    "exibir_baralho_antes": True,
    "distribuir": True,
    "mostrar_sobra_baralho": True,
    "quantidade_de_cartas": 6,
    "quantidade_de_jogadores": 4
}

cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
naipes = ['♠', '♣', '♥', '♦']
coringas = ['Joker1', 'Joker2']

baralho = [f"{carta}{naipe}" for naipe in naipes for carta in cartas]
if config["incluir_coringa"]:
    baralho += coringas

baralho_final = baralho * config["quantidade_baralhos"]

if config["quantidade_de_cartas"] * config["quantidade_de_jogadores"] > len(baralho_final):
    print('\nNão existem cartas suficientes no baralho para a quantidade de jogadores.\n')
    exit()

if config["embaralhar"]:
    random.shuffle(baralho_final)

if config["exibir_baralho_antes"]:
    print(f'\nCartas do baralho:\n\n{baralho_final}')

if config["distribuir"]:
    print('\nCartas distribuídas:')
    for jogador in range(1, config["quantidade_de_jogadores"] + 1):
        print(f"\n_____Jogador {jogador}_____")
        for _ in range(config["quantidade_de_cartas"]):
            print(baralho_final.pop())

if config["mostrar_sobra_baralho"]:
    print(f'\nCartas que sobraram no baralho:\n\n{baralho_final}')
