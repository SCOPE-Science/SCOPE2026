#!/usr/bin/env python3
"""Exact enumeration of all smooth projective F2-filling cubic-surface pencils.
All operations are finite bit arithmetic; no external packages are needed.
"""
from itertools import combinations

PAIR = tuple(combinations(range(4), 2))

def pf(a):
    return (((a >> 0) & 1) & ((a >> 5) & 1)) ^ (((a >> 1) & 1) & ((a >> 4) & 1)) ^ (((a >> 2) & 1) & ((a >> 3) & 1))

def M(a):
    x = [[0] * 4 for _ in range(4)]
    for k, (i, j) in enumerate(PAIR):
        x[i][j] = x[j][i] = (a >> k) & 1
    return x

def code(x):
    return sum((x[i][j] & 1) << k for k, (i, j) in enumerate(PAIR))

def transvection(a, i, j):
    # Change variable x_i -> x_i + x_j, i != j.
    x = M(a)
    for k in range(4):
        x[k][j] ^= x[k][i]
    for k in range(4):
        x[j][k] ^= x[i][k]
    return code(x)

def pair_value(a, x, y):
    z = 0
    for k, (i, j) in enumerate(PAIR):
        if (a >> k) & 1:
            z ^= (((x >> i) & 1) & ((y >> j) & 1)) ^ (((x >> j) & 1) & ((y >> i) & 1))
    return z

nondeg = {a for a in range(1, 64) if pf(a) == 1}
assert len(nondeg) == 28
pencils = {tuple(sorted((a, b, a ^ b))) for a, b in combinations(nondeg, 2) if pf(a ^ b)}
assert len(pencils) == 56
assert all(len(set(P)) == 3 for P in pencils)
# Transvections generate GL_4(F2) (which has order 20160).
first = tuple(sorted((33, 13, 44)))
seen = {first}
queue = [first]
while queue:
    P = queue.pop()
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            Q = tuple(sorted(transvection(a, i, j) for a in P))
            assert Q in pencils
            if Q not in seen:
                seen.add(Q)
                queue.append(Q)
assert seen == pencils
assert 20160 // len(seen) == 360
# Projective F2-lines are triples {x,y,x+y} of nonzero binary 4-vectors.
lines = {tuple(sorted((x, y, x ^ y))) for x, y in combinations(range(1, 16), 2)}
assert len(lines) == 35
spreads = set()
for P in pencils:
    a, b, _ = P
    common = tuple(sorted(L for L in lines if pair_value(a, L[0], L[1]) == 0 and pair_value(b, L[0], L[1]) == 0))
    assert len(common) == 5
    assert sorted(x for L in common for x in L) == list(range(1, 16))
    spreads.add(common)
assert len(spreads) == 56
rep_spread = sorted(L for L in lines if pair_value(33, L[0], L[1]) == 0 and pair_value(13, L[0], L[1]) == 0)
assert rep_spread == [(1, 4, 5), (2, 8, 10), (3, 12, 15), (6, 11, 13), (7, 9, 14)]
# A dimension >=3 smooth filling subspace is impossible: a quadratic form
# on F2^3 must have a nonzero isotropic vector. Verify this latter finite fact.
for coeffs in range(64):
    zeros = []
    for x in range(1, 8):
        y = [(x >> i) & 1 for i in range(3)]
        terms = [y[0], y[1], y[2], y[0]*y[1], y[0]*y[2], y[1]*y[2]]
        if sum(((coeffs >> i) & 1) * terms[i] for i in range(6)) % 2 == 0:
            zeros.append(x)
    assert zeros
print('FROBENIUS_CUBIC_PENCILS_PASS', len(nondeg), len(pencils), len(seen), len(spreads), 20160 // len(seen), len(lines))
