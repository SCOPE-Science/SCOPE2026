#!/usr/bin/env python3
"""Exact integer-cyclotomic census of all Fourier 3-by-3 minors at N=30.

Python 3 standard library only.  Every translation class is represented
by triples containing zero.  This checker reduces the six-term determinant
in Z[x]/(Phi_30(x)) and computes rank-one minors separately.
"""
from collections import Counter
from itertools import combinations

N = 30
# Phi_30(x) = x^8 + x^7 - x^5 - x^4 - x^3 + x + 1.
POLY = (1, 1, 0, -1, -1, -1, 0, 1)


def multiply_by_x(v):
    carry = v[-1]
    return tuple((v[i - 1] if i > 0 else 0) - carry * POLY[i]
                 for i in range(8))


powers = [(1,) + (0,)*7]
for _ in range(N-1):
    powers.append(multiply_by_x(powers[-1]))
assert multiply_by_x(powers[-1]) == powers[0]
assert max(abs(v) for poly in powers for v in poly) == 1

triples = list(combinations(range(1,N),2))
hist = Counter()
for a,b in triples:
    for c,d in triples:
        exponents = [a*c+b*d, a*d+b*c, a*c, b*d, a*d, b*c]
        signs = (1,-1,-1,-1,1,1)
        vector = tuple(sum(sign*powers[ex%N][i]
                           for sign,ex in zip(signs,exponents))
                       for i in range(8))
        assert max(abs(q) for q in vector) <= 6
        if any(vector):
            rank = 3
        elif all(z % N == 0 for z in (a*c,a*d,b*c,b*d)):
            rank = 1
        else:
            rank = 2
        hist[rank] += 1
assert hist == {1:180, 2:15192, 3:149464},hist
print('EXACT_CYCLOTOMIC_N30_PASS',dict(sorted(hist.items())))
print('ALL_PAIR_COUNTS', {j:100*hist[j] for j in (1,2,3)})
