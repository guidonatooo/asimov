import random
import seaborn as sns

class Academia:
   def __init__(self):
        self.halteres = [i for i in range(10, 50) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()
        
   def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}
              
   def listar_halteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]
        
   def listar_espacos(self):
        return [key for key, value in self.porta_halteres.items() if value == 0]
  
    
   def pegar_halter(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = 0
        return peso
    
   def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso
    
   def calcular_caos(self):
        num_caos = [i for i , j in self.porta_halteres.items() if i != j]
        return len(num_caos) / len(self.porta_halteres)
    
class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo
        self.academia = academia
        self.peso = 0
        
    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_halter(self.peso)
        
    def finalizar_treino(self):
        espaco = self.academia.listar_espacos()
        
        if self.tipo == 1:
            if self.peso in espaco:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = random.choice(espaco)
                self.academia.devolver_halter(pos, self.peso)
        if self.tipo==2:
                pos = random.choice(espaco)
                self.academia.devolver_halter(pos, self.peso)
        self.peso = 0
        
Academia = Academia()

usuarios = [Usuario(1, Academia) for i in range(10)]
usuarios += [Usuario(2, Academia) for i in range(1)]
random.shuffle(usuarios)

lista_caos = []

for k in range (50):
    Academia.reiniciar_o_dia()
    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()  
    lista_caos += [Academia.calcular_caos()]
    
sns.displot(lista_caos, kde=True)
lista_caos

