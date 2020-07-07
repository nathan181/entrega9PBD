import random
from collections import Counter
import math 

class Usuario:
    def __init__ (self, idade, sexo, intencao_de_voto):
        self.idade = idade
        self.sexo = sexo
        self.intencao_de_voto = intencao_de_voto

    def __str__ (self):
        return f'idade: {self.idade}, sexo: {self.sexo}, intenção de voto: {self.intencao_de_voto}'

    def __eq__ (self, other):
        return self.intencao_de_voto == other.intencao_de_voto
    
    def __hash__(self):
        return 1 #ineficiente

def gera_base (n):
    l = []
    for i in range (n):
        #aleatorio no intervalo [a, b]
        idade = random.randint(18, 35)
        sexo = random.choice(['M', 'F'])
        intencao_de_voto = random.choice(['Haddad', "Bolsonaro"])
        user = Usuario(idade, sexo, intencao_de_voto)
        l.append(user)    
    return l

def rotulo_de_maior_frequencia_sem_empate (usuarios):
    frequencias = Counter (usuarios)
    rotulo, frequencia = frequencias.most_common(1)[0]
    qtde_de_mais_frequentes = len([count for count in frequencias.values() if count == frequencia])

    if qtde_de_mais_frequentes == 1:
        return rotulo
    return rotulo_de_maior_frequencia_sem_empate(usuarios[:-1])


def distance (p1, p2):
    i = math.pow((p1.idade - p2.idade), 2)
    s = math.pow((1 if p1.sexo == 'M' else 0) - (1 if p2.sexo == 'M' else 0), 2)
    
    return math.sqrt(i + s)

def knn (k, observacoes_rotuladas, nova_observacao):
    ordenados_por_distancia = sorted (observacoes_rotuladas, key= lambda obs: distance (obs, nova_observacao))
    k_mais_proximos = ordenados_por_distancia[:k]
    resultado = rotulo_de_maior_frequencia_sem_empate(k_mais_proximos)
    return resultado.intencao_de_voto

#------------------------------------------------- TESTES ---------------------------------------------------

def knn_teste():
    base = gera_base(10)
    print('-------------------------- BASE ------------------------------')
    for p in base:
        print(p)

    print('-------------------------- Rótulo de maior frequência ------------------------------')
    user = Usuario(19, 'M', None)
    user.intencao_de_voto = knn(5, base, user)    
    print (user)

#---------------------------------------- Atividade Semana 09 ---------------------------------------------------
def cross_validation_leave_one_out():
    
    base = gera_base(100)

    chance_erro = 0
    chance_acerto = 0

    for usuario in base:
        intencao_de_voto = knn(5, base[:-1], usuario)
        if(intencao_de_voto != usuario.intencao_de_voto):
            
            chance_erro = chance_erro + 1
        
    print('Falhas no knn: ', chance_erro)
    chance_acerto = ((len(base) - chance_erro)/len(base))*100
    chance_erro = chance_erro/len(base)*100

    print(f'A chance de acerto é de {chance_acerto}%')
    print(f'A chance de erro é de {chance_erro}%')
    
#----------------------------------------------------------------------------------------------------------------

def main():
    cross_validation_leave_one_out()

    # knn_teste()

    pass
main()