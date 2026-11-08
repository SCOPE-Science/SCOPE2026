#!/usr/bin/env python3
"""Exact chamber-support and forbidden-configuration verification.

Dependencies: Python 3.9+ standard library only.
"""
from fractions import Fraction
from collections import Counter, defaultdict
from math import comb

names = [f'C{i}' for i in range(8)] + ['D0','D1'] + [f'S{i}' for i in range(4)]
n = len(names)
A = [[0]*n for _ in range(n)]
for i in range(10): A[i][i] = 2
for i in range(10,n): A[i][i] = 1
for i in range(8):
    j = (i+1)%8
    A[i][j] = A[j][i] = -1
A[8][9] = A[9][8] = -2
for k in range(4):
    s,c,d = 10+k,2*k,8+(k%2)
    A[s][c] = A[c][s] = -1
    A[s][d] = A[d][s] = -1

def positive_definite(mask):
    ids = [i for i in range(n) if (mask>>i)&1]
    B = [[Fraction(A[i][j]) for j in ids] for i in ids]
    while B:
        p = B[0][0]
        if p <= 0: return False
        B = [[B[i][j]-B[i][0]*B[0][j]/p for j in range(1,len(B))]
             for i in range(1,len(B))]
    return True

valid = [positive_definite(m) for m in range(1<<n)]
obstructions = [m for m in range(1,1<<n) if not valid[m]
                and all(valid[m ^ (1<<j)] for j in range(n) if m>>j&1)]
poly1 = [sum(valid[m] for m in range(1<<n) if m.bit_count()==k)
         for k in range(n+1)]
# Independent counting: complement of a union of forbidden-upset families,
# evaluated via inclusion-exclusion with a union-mask dynamic program.
coeff = {0:1}
for b in obstructions:
    nxt = defaultdict(int)
    for m,z in coeff.items():
        nxt[m] += z
        nxt[m|b] -= z
    coeff = {m:z for m,z in nxt.items() if z}
poly2 = [sum(z*comb(n-m.bit_count(),k-m.bit_count())
             for m,z in coeff.items() if m.bit_count()<=k)
         for k in range(n+1)]
assert poly1 == poly2, (poly1,poly2)
assert len(obstructions) == 24 and sum(poly1) == 6656
assert poly1 == [1,14,90,346,875,1508,1768,1352,600,102,0,0,0,0,0]
for m in range(1<<n):
    assert valid[m] == (not any((m&b)==b for b in obstructions))
print('ALL 16384 subsets checked by exact rational Schur complements')
print('24 inclusion-minimal forbidden supports:')
for m in obstructions:
    print(f'  size {m.bit_count()}: ' + ','.join(names[j] for j in range(n) if m>>j&1))
print('POLYNOMIAL',poly1)
print('INDEPENDENT_INCLUSION_EXCLUSION_POLYNOMIAL',poly2)
print('TOTAL_CHAMBERS',sum(poly1))
print('MAXIMAL_SUPPORT_SIZE',max(k for k,v in enumerate(poly1) if v))
print('MAXIMAL_SUPPORT_COUNT',poly1[9])
print('ALL_EXACT_TESTS_PASSED')
