import random
import os

class tictactoe:
    def __init__(self):
        self.tabuleiro = [' ' for i in range(9)]
        self.jogador = 'X'
        
    def print_tabuleiro(self):
        for i in range(3):
            print(' | '.join(self.tabuleiro[i*3:(i+1)*3]))
            if i != 2:
                print('-' * 9)
        print('\n')
        
    def jogada(self, pos):
        if self.tabuleiro[pos] == ' ':
            self.tabuleiro[pos] = self.jogador
            if self.verificar_vitoria(self.jogador):
                self.print_tabuleiro()
                print(f'O jogador {self.jogador} venceu!')
                return True
            if ' ' not in self.tabuleiro:
                self.print_tabuleiro()
                print('Empate!')
                return True
            self.jogador = 'O' if self.jogador == 'X' else 'X'
        return False
    
    def verificar_vitoria(self, jogador):
        for i in range(3):
            if self.tabuleiro[i] == self.tabuleiro[i+3] == self.tabuleiro[i+6] == jogador:
                return True
            if self.tabuleiro[i*3] == self.tabuleiro[i*3+1] == self.tabuleiro[i*3+2] == jogador:
                return True
        if self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] == jogador:
            return True
        if self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] == jogador:
            return True
        return False
    
    def jogar(self):
        while True:
            self.print_tabuleiro()
            pos = int(input(f'Jogador {self.jogador}, escolha uma posição (0-8): '))
            os.system('cls' if os.name == 'nt' else 'clear')
            if self.jogada(pos):
                break