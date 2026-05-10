import numpy as np

def inserare_mutatie(individ):
    n = len(individ)-1
    poz = np.random.randint(0, n, 2)
    while (poz[0]==poz[1]):
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    individ_m = individ.copy()
    individ_m[p1+1] = individ[p2]
    j = p1+2
    for i in range(p1+1, n):
        if(individ[i]!=individ[p2]):
            individ_m[j] =  individ[i]
            j = j+1
    individ_m[-1]=fitness(individ_m[:-1])
    return individ_m

def mutatie_pop(pop, pm):
    popm = pop.copy()
    dim = len(popm)
    for i in range(dim):
        p = np.random.rand()
        if(p <= pm):
            popm[i] = inserare_mutatie(popm[i])
    return popm

def fitness(individ):
    scor = 0
    for i in range(len(individ)):
        j = individ[i]
        if(i < j and individ[j]==i):
            scor = scor+1
    return scor

def generare_pop(dim, n):
     pop = []
     for i in range(dim):
         pop.append(np.random.permutation(n).tolist())
         pop[i].append(fitness(pop[i]))
     return pop

if __name__== "__main__":
    pop = generare_pop(5, 5)
    print("Populatie initiala:")
    print(pop)
    pm = 0.6
    print("Populatie dupa mutatie (pm=0.6):")
    popm = mutatie_pop(pop, pm)
    print(popm)