"""Independent spin-by-spin enumeration of the three-state Potts model on K_{2,2,...,2}."""
from itertools import product
from math import factorial


def prediction(m):
    t, s = divmod(m, 3)
    en = 2 * (3*t*t+2*s*t+s)-2*m
    if s == 0:
        return en, factorial(m)//factorial(t)**3, 0
    mono = 3*factorial(m)//(factorial(t+1)**s * factorial(t)**(3-s))
    split = 2*(t+1)*mono
    return en, mono+split, split


def check(m):
    edges=[(i,j) for i in range(2*m) for j in range(i+1,2*m) if i//2 != j//2]
    e_best=10**10
    n_best=0
    split_best=0
    for colors in product(range(3),repeat=2*m):
        energy=sum(colors[i]==colors[j] for i,j in edges)
        if energy < e_best:
            e_best=energy
            n_best=0
            split_best=0
        if energy == e_best:
            n_best += 1
            split_best += sum(colors[2*i]!=colors[2*i+1] for i in range(m)) == 1
    assert (e_best,n_best,split_best) == prediction(m), (m,e_best,n_best,split_best,prediction(m))
    return e_best,n_best,split_best

if __name__ == '__main__':
    for m in range(2,7):
        print('m',m,'E/J,ground_count,split_count',*check(m))
    print('BRUTE_FORCE_PASS')
