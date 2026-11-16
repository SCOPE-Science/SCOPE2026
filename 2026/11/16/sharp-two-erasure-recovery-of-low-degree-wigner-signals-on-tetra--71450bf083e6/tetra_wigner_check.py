#!/usr/bin/env python3
"""Exact rational verification of the tetrahedral degree-one sampling spectrum.

Run with: python3 tetra_wigner_check.py
No dependencies outside the Python standard library.
"""
from fractions import Fraction as Q
from itertools import permutations, combinations


def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i+1,4))

G = tuple(p for p in permutations(range(4)) if sign(p) == 1)
assert len(G) == 12
identity = (0,1,2,3)

def compose(a,b):
    return tuple(a[b[i]] for i in range(4))

def inverse(a):
    b = [0]*4
    for i, j in enumerate(a): b[j] = i
    return tuple(b)

def character_3(p):
    return sum(p[i] == i for i in range(4)) - 1

# A4's standard three-dimensional rotation representation is the
# four-vertex permutation representation minus its fixed line.
assert sorted(character_3(g) for g in G) == [-1]*3 + [0]*8 + [3]
assert sum(character_3(g)**2 for g in G) == 12

# Isotypic projector for the constant coefficient and all nine
# coefficients of the degree-one rotation representation.
K = [[Q(1 + 3*character_3(compose(inverse(g), h)),12)
      for h in G] for g in G]
assert all(sum(K[i][k]*K[k][j] for k in range(12)) == K[i][j]
           for i in range(12) for j in range(12))
assert sum(K[i][i] for i in range(12)) == 10
assert all(K[i][i] == Q(5,6) for i in range(12))

# Nonzero eigenvalues of the deleted-data map on the 10-dimensional
# signal space are the nonzero eigenvalues of K restricted to E.
# The retained-data squared singular spectrum is 1 - these numbers,
# together with 1 of multiplicity 8.
counts = {'half_turn': 0, 'three_cycle': 0}
for i,j in combinations(range(12),2):
    r = compose(inverse(G[i]),G[j])
    v = K[i][j]
    assert v in (Q(-1,6),Q(1,12))
    deletion_eigenvalues = sorted((Q(5,6)-v,Q(5,6)+v))
    retained_spectrum = sorted((Q(1)-x for x in deletion_eigenvalues))
    if character_3(r) == -1:
        assert retained_spectrum == [Q(0),Q(1,3)]
        counts['half_turn'] += 1
    else:
        assert character_3(r) == 0
        assert retained_spectrum == [Q(1,12),Q(1,4)]
        counts['three_cycle'] += 1
assert counts == {'half_turn': 18, 'three_cycle': 48}, counts

# Exactly one deletion: one affected eigenvalue, 1-5/6 = 1/6.
assert all(1-K[i][i] == Q(1,6) for i in range(12))

# A half-turn-separated pair is supported by a nonzero signal in
# the coefficient space: the difference of the two coordinate deltas.
for i,j in combinations(range(12),2):
    if K[i][j] == Q(-1,6):
        v = [int(k==i)-int(k==j) for k in range(12)]
        assert [sum(K[a][b]*v[b] for b in range(12)) for a in range(12)] == v

# Independent analytic character formula for every invisible mode:
# [tr(R g^{-1}) - tr(R h^{-1})] / 4 is exactly delta_g - delta_h
# on the tetrahedral group whenever g^{-1}h is a half-turn.
for g in G:
    for h in G:
        if g == h or character_3(compose(inverse(g), h)) != -1:
            continue
        for u in G:
            numerator = character_3(compose(u, inverse(g))) - character_3(compose(u, inverse(h)))
            target = 4*(int(u == g)-int(u == h))
            assert numerator == target

print('PASS: all 36 ordered half-turn witness pairs by explicit trace formula')
print('PASS: 12 tetrahedral rotations, exact rank 10 projector')
print('PASS: all 66 double-erasure patterns: 18 singular, 48 invertible')
print('PASS: singular spectra [0, 1/3, 1 x8] or [1/12, 1/4, 1 x8]')
print('PASS: one-deletion spectrum [1/6, 1 x9]')
