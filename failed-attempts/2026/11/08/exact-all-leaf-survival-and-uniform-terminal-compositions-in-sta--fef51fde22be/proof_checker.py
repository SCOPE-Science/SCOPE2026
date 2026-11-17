"""Exact-rational absorption checks for the star-opinion voter process.

Run: python checker.py. Requires sympy.
Not a proof for arbitrary population size; see the accompanying argument.
"""
from itertools import product
from math import comb
from sympy import Matrix, Rational, zeros

def vectors(r, total):
    if r == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for tail in vectors(r - 1, total - x):
            yield (x,) + tail

def verify(r, n):
    # The center holds n-sum(a) agents. States with 0<sum(a)<n are transient.
    states = [v for m in range(1, n) for v in vectors(r, m)]
    index = {v:i for i,v in enumerate(states)}
    Q = zeros(len(states)); targets = [v for v in vectors(r, n) if all(x>0 for x in v)]
    B = zeros(len(states), len(targets)); col = {v:i for i,v in enumerate(targets)}
    for i, v in enumerate(states):
        m = sum(v)
        Q[i,i] = 1
        for j, x in enumerate(v):
            if x == 0:
                continue
            for delta in (-1, 1):
                new = list(v);new[j] += delta; new = tuple(new)
                pr = Rational(x, 2*m)
                if sum(new) == n:
                    if new in col: B[i,col[new]] += pr
                elif sum(new) == 0:
                    pass
                else:
                    Q[i,index[new]] -= pr
    result = Q.inv() * B
    initial = (1,)*r
    prob = Rational(1, comb(n+r-1, 2*r-1))
    for v in targets:
        assert result[index[initial], col[v]] == prob, (r,n,v,result[index[initial],col[v]],prob)
    joint = sum(result[index[initial], col[v]] for v in targets)
    assert joint == Rational(comb(n-1,r-1),comb(n+r-1,2*r-1))
    print('PASS', 'r=',r,'n=',n,'all-positive-boundary-states=',len(targets),'per-state-probability=',prob,'joint=',joint)

if __name__=='__main__':
    for r,n in ((2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6),(4,5)):
        verify(r,n)
    print('All rational boundary-value tests passed.')
