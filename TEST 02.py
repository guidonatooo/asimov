print ("---sorte na jogada---")
sorte = 7
tentativas= 3
parabens = False
for tentativa in range(1, tentativas + 1):
    chute = int(input("Você tem {tentativa} de {tentativas}. Escolha um numero de 1 a 9:\n"))
    
    if chute > sorte:
        print("chutou alto, pense mais um pouco")
    elif chute < sorte:
        print("quase lá, um pouco mais alto")
    elif chute == sorte:
        print("Parabéns, você está com sorte!")
        break
    else:
        print("Parece que hoje não foi seu dia. Tente novamente amanhã.")
    
if tentativa == tentativas:
    print(f"Suas tentativas acabaram. O numero certo era {sorte}")