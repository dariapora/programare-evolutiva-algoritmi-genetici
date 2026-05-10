import numpy as np
import copy

def inversiune(individ):
    n = len(individ)
    inversat = individ.copy()
    poz = np.random.randint(0, n, 2)
    while(poz[0]==poz[1]):
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    inversat[p1] = individ[p2]
    inversat[p2] = individ[p1]
    return inversat

def mutatie_pop(pop, pm, numere):
    popm = copy.deepcopy(pop)
    for i in range (len(popm)):
        r = np.random.uniform(0, 1)
        if (r<=pm):
            popm[i] = inversiune(popm[i][:-1])
            popm[i].append(fitness(popm[i], numere))
    return popm

def fitness(individ, numere):
    suma = 0
    for i in range (0, len(individ)-1):
        suma = suma + numere[individ[i]]*numere[individ[i+1]]
    suma = suma+numere[individ[0]]*numere[individ[-1]]
    return suma

def generare_pop(dim, n):
    pop = []
    numere = np.genfromtxt("numere.txt", dtype=int).tolist()
    for _ in range(dim):
        individ = np.random.permutation(n).tolist()
        individ.append(fitness(individ, numere))
        pop.append(individ)
    return pop, numere

if __name__=="__main__":
    pop, numere = generare_pop(100, 16)
    print(numere)
    print(pop)
    print(mutatie_pop(pop, 0.1, numere))