import copy

import numpy as np

def binar(num, lungime):
    numar = []
    for _ in range(lungime):
        numar.append(int(num % 2))
        num = int(num / 2)
    return numar

def decodificare(individ):
    x = 0
    y = 0
    for i in range (11):
        if(individ[i]==1):
            x = x + 2**i
    for i in range (11, 23):
        if (individ[i] == 1):
            y = y + 2**(i-11)
    y = y-1
    return [x, y]

def fitness(individ):
    [x, y] = decodificare(individ)
    return (float)(y * (np.sin(x-2))**2)

def generare_pop(dim):
    pop = []
    for i in range(dim):
        x = binar(np.random.randint(1, 1501), 11)
        y = binar(np.random.randint(0, 2502), 12)
        individ = x+y
        individ.append(fitness(individ))
        pop.append(individ)
    return pop

def recombinare_3p(p1, p2):
    puncte = np.sort(np.random.choice(np.arange(1, len(p1)), 3, replace=False))
    c1 = p1[0:puncte[0]]+p2[puncte[0]:puncte[1]]+p1[puncte[1]:puncte[2]]+p2[puncte[2]:len(p1)]
    c2 = p2[0:puncte[0]]+p1[puncte[0]:puncte[1]]+p2[puncte[1]:puncte[2]]+p1[puncte[2]:len(p2)]
    c1.append(fitness(c1))
    c2.append(fitness(c2))
    return c1, c2

def recombinare(pop, pc):
    popc = copy.deepcopy(pop)
    for i in range(0,len(pop)-1,2):
        r = np.random.uniform(0, 1)
        if r <= pc:
            p1 = pop[i][:-1].copy()
            p2 = pop[i+1][:-1].copy()
            c1, c2 = recombinare_3p(p1, p2)
            popc[i]=c1
            popc[i+1]=c2
    return popc

if __name__=="__main__":
    dim = 7
    pop = generare_pop(dim)
    print("Populatia initiala:")
    print(pop)
    print("Populatia recombinata:")
    print(recombinare(pop, 0.5))
    print(np.random.randint(1, 4))