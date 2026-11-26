#!/usr/bin/env python3
"""Exact certificate for the cubic-surface Steiner support lattice.

Uses only Python's standard library.  All enumerations are finite and
lexicographically ordered.  Matrices have integer entries throughout.
"""
from itertools import combinations
from collections import Counter, defaultdict

# Picard coordinates (d,m_1,...,m_6) for dH - sum m_i E_i.
A = (3,) + (1,)*6
lines = ([(0,) + tuple(-int(j == i) for j in range(6)) for i in range(6)]
         + [(1,) + tuple(int(j in pair) for j in range(6))
            for pair in combinations(range(6), 2)]
         + [(2,) + tuple(int(j != i) for j in range(6)) for i in range(6)])
assert len(lines) == 27

def class_sum(indices):
    return tuple(sum(lines[i][j] for i in indices) for j in range(7))

# Three-line anticanonical plane sections are exactly the tritangents.
tritangents = [tuple(t) for t in combinations(range(27), 3)
              if class_sum(t) == A]
assert len(tritangents) == 45

# Disjoint tritangent triples define nine-line unions.  The unions with
# exactly two such partitions are the Steiner trihedral PAIRS.
partitions = defaultdict(list)
for triple in combinations(range(45), 3):
    union = set().union(*(tritangents[j] for j in triple))
    if len(union) == 9:
        partitions[tuple(sorted(union))].append(triple)
steiner = sorted(s for s, p in partitions.items() if len(p) == 2)
assert len(steiner) == 120
assert Counter(map(len, partitions.values())) == {1: 5040, 2: 120}
assert all(class_sum(u) == tuple(3*x for x in A) for u in steiner)
assert all(sum(i in u for u in steiner) == 40 for i in range(27))

# Indices refer to the exact lexicographic collections above, zero based.
T_COL = (2,37,39,41,42,38,34,43,24,18,27,12,11,10,30,32,22,16,25,6,0)
S_COL = (86,6,16,97,87,107,79,105,52,10,43,109,89,103,5,50,15,37,27,59,21)
ROWS  = (11,6,8,2,10,23,15,18,22,16,13,4,17,9,24,12,5,14,25,7,26)
assert len(set(T_COL)) == len(set(S_COL)) == len(set(ROWS)) == 21

def minor(collection, cols):
    return [[int(row in collection[j]) for j in cols] for row in ROWS]

def bareiss(M):
    """Fraction-free integer determinant with row swaps."""
    a = [row[:] for row in M]
    n = len(a)
    assert n and all(len(row) == n for row in a)
    sign = 1
    prev = 1
    for k in range(n-1):
        if not a[k][k]:
            pivot = next((j for j in range(k+1,n) if a[j][k]), None)
            if pivot is None:
                return 0
            a[k],a[pivot] = a[pivot],a[k]
            sign = -sign
        x = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                y = a[i][j]*x-a[i][k]*a[k][j]
                assert y % prev == 0
                a[i][j] = y//prev
        for i in range(k+1,n):
            a[i][k] = 0
        prev = x
    return sign*a[n-1][n-1]

dT = bareiss(minor(tritangents, T_COL))
dS = bareiss(minor(steiner, S_COL))
assert (dT,dS) == (-1,3), (dT,dS)

# Structural constraints used with the determinant certificate:
# (i) 27 line classes span Picard of rank 7 (E_i and H=E_1+E_2+L_12).
# (ii) All tritangents have class A and hence lie in the rank-21 inverse
#      image of Z*A in Z^27.
# (iii) A 21x21 unit minor makes T_COL a primitive rank-21 sublattice.
# (iv) S_COL is a sublattice of index |dS/dT|=3.  All Steiner supports
#      have class 3A, so they belong to the index-3 sublattice of T
#      selected by coefficient of A modulo 3. Thus equality holds.
assert lines[0] == (0,-1,0,0,0,0,0)
assert lines[6] == (1,1,1,0,0,0,0)
assert tuple(lines[0][j]+lines[1][j]+lines[6][j]
             for j in range(7)) == (1,0,0,0,0,0,0)
print('45 tritangents; 120 Steiner pairs; valency 40')
print('tritangent primitive basis minor:', dT)
print('Steiner index-three basis minor:', dS)
print('cokernel: Z^6 direct-sum Z/3Z')
print('VERIFY_OK')
