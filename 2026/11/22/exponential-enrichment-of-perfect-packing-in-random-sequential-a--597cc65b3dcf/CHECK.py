#!/usr/bin/env python3
"""Finite exact and quadrature sanity checks for nearest-neighbour ladder adsorption."""
from fractions import Fraction
from itertools import permutations
from math import sqrt

def exact_dynamic(L):
    n = 2 * L
    adjacency = []
    for r in range(2):
        for j in range(L):
            neigh = {(1-r)*L+j}
            if j: neigh.add(r*L+j-1)
            if j+1<L: neigh.add(r*L+j+1)
            adjacency.append(neigh)
    successful = 0
    for perm in permutations(range(n)):
        occupied = set()
        for v in perm:
            if not adjacency[v].intersection(occupied): occupied.add(v)
        if len(occupied) == L: successful += 1
    return Fraction(successful, 1 if n == 0 else __import__('math').factorial(n))

def approximate_lambda(m, steps=160):
    # Positive midpoint Nyström discretization of the two-coordinate transfer operator.
    xs = [(i+0.5)/m for i in range(m)]
    f = [[1.0]*m for _ in range(m)]
    ratios=[]
    for t in range(steps):
        nf = [[sum((1-min(xs[i],xs[j],xs[k]))*f[j][k] for k in range(m))/m
                for j in range(m)] for i in range(m)]
        old = sum(sum(row) for row in f)
        new = sum(sum(row) for row in nf)
        ratio = new / old
        f = [[v/new*(m*m) for v in row] for row in nf]
        ratios.append(ratio)
    return ratios[-1]

def check():
    known={1:Fraction(1),2:Fraction(1),3:Fraction(7,9),4:Fraction(3,5)}
    for L,expected in known.items():
        got=exact_dynamic(L)
        assert got==expected,(L,got,expected)
        print('exact L',L,'maximum density probability',got)
    vals = [approximate_lambda(m) for m in (12,24,36)]
    print('midpoint transfer estimates',vals)
    for v in vals:
        assert 0.75<v<0.85
    assert abs(vals[-1]-vals[-2])<0.0025
    phi=(1+sqrt(5))/2
    assert (0.75*phi)>1
    print('passed: exact permutations, transfer estimates, rate comparison')

if __name__=='__main__':check()
