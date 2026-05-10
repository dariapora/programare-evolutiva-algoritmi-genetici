import copy

import numpy as np

# consideram o lista de n elemente lista, fiecare lista avand 2 elemente (coordonatele unui punct)
# individul va fi un vector compus din valorile indecsilor

lista_puncte = [[10, 47], [17, 79], [0, 91], [86, 28], [94, 70], [94, 66], [4, 92], [21, 27], [90, 58], [38, 28], [19, 71], [86, 20]]

def calculeaza_distanta(p1, p2):
    return np.sqrt((p2[0]-p1[0])*(p2[0]-p1[0]) + (p2[1]-p1[1])*(p2[1]-p1[1]))

def calculeaza_perimetru(l1, l2, l3, l4):
    return float(l1+l2+l3+l4)

def fitness(individ):
    perimetru = calculeaza_perimetru(calculeaza_distanta(lista_puncte[individ[0]], lista_puncte[individ[1]]), calculeaza_distanta(lista_puncte[individ[1]], lista_puncte[individ[2]]), calculeaza_distanta(lista_puncte[individ[2]], lista_puncte[individ[3]]), calculeaza_distanta(lista_puncte[individ[3]], lista_puncte[individ[0]]))
    return perimetru

def recombinare_unipunct(p1, p2):
    k = np.random.randint(1, 4)
    c1 = p1[:k]+p2[k:]
    c2 = p2[:k]+p1[k:]
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
            c1, c2 = recombinare_unipunct(p1, p2)
            if(len(c1)!=len(set(c1))):
                c1 = p1
            if(len(c2)!=len(set(c2))):
                c2 = p2
            popc[i] = c1
            popc[i+1] = c2
    return popc


def generare_pop(puncte, dim):
    pop = []
    n = len(puncte)
    for _ in range(dim):
        individ = np.random.choice(n, 4, replace=False).tolist()
        individ.append(fitness(individ))
        pop.append(individ)
    return pop



if __name__ == "__main__":
    pop = generare_pop(lista_puncte, 5)
    print(pop)
    print(recombinare(pop, 1))