#!/usr/bin/env python3
"""Reproduce exact four-adic digit-energy arithmetic; no external dependencies."""
from collections import Counter
from math import sqrt, log
D = (0, 1, 3)
states = (-1, 0, 1)
T = tuple(tuple(sum(a+b-c-d+i == 4*j
                    for a in D for b in D for c in D for d in D)
                for j in states) for i in states)
assert T == ((8,10,2),(3,15,3),(2,10,8))
def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))
P = ((1,0,0),(0,1,0),(0,0,1))
energies = []
for n in range(7):
    energies.append(P[1][1])
    P=matmul(P,T)
assert energies[:6] == [1,15,285,5775,118725,2448375]
assert all(energies[n+2] == 25*energies[n+1]-90*energies[n] for n in range(5))
A=(0,)
for n in range(1,5):
    A=tuple(4*a+d for a in A for d in D)
    counts=Counter(a+b for a in A for b in A)
    assert sum(v*v for v in counts.values()) == energies[n]
lam=(25+sqrt(265))/2
assert 4*lam > 81
dimension = (4*log(3)-log(lam))/log(4)
assert abs(dimension-0.9862600784105084)<1e-12
print("FOUR_ADIC_CONVOLUTION_CHECKS_PASSED", "four_brute_levels", dimension)
