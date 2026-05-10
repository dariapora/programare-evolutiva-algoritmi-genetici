import copy

import numpy as np
import copy

def fitness(individ, valori_jucatori):
    n = len(individ)
    val1 = 0
    val2 = 0
    for i in range(n//2):
        val1 = val1 + valori_jucatori[individ[i]]
    for i in range(n//2, n):
        val2 = val2+ valori_jucatori[individ[i]]
    return 1/(1+int(np.absolute(val1-val2)))

def mutatie_inserare(individ, valori_jucatori):
    poz = np.random.randint(0, len(individ), 2)
    while(poz[0]==poz[1]):
       poz = np.random.randint(0, len(individ), 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    if(p1==len(individ)-2):
        return individ
    nou = individ[:p1+1]
    nou.append(individ[p2])
    for i in range(p1+1, len(individ)):
        if(i!=p2):
            nou.append(individ[i])
    return nou

def mutatie_pop(pop, pm, valori_jucatori):
    popm = copy.deepcopy(pop)
    for i in range(len(popm)):
        r = np.random.uniform(0, 1)
        if(r<=pm):
            popm[i] = mutatie_inserare(popm[i][:-1], valori_jucatori)
            popm[i].append(fitness(popm[i], valori_jucatori))
    return popm

def generare_pop(n, dim):
    pop=[]
    valori_jucatori = np.random.randint(1, 11, n).tolist()
    for _ in range(dim):
        individ = np.random.permutation(n).tolist()
        individ.append(fitness(individ, valori_jucatori))
        pop.append(individ)
    return pop, valori_jucatori

if __name__=="__main__":
    pop, valori_jucatori = generare_pop(10, 40)
    print("Populatie inainte de mutatie:")
    print(pop)
    print("Populatie dupa mutatie:")
    popm = mutatie_pop(pop, 0.9, valori_jucatori)
    print(popm)
