#!/usr/bin/env python3
"""Finite exhaustive certificate for maximal-matching shattering on the 3-cube.
Requires only Python 3 standard library; no external data.
"""
from collections import Counter
from itertools import permutations
from fractions import Fraction

V = range(8)
E = sorted((v, v ^ (1 << j)) for v in V for j in range(3) if v < (v ^ (1 << j)))
assert len(E) == 12
N = len(E)
INC = [sum(1 << i for i, f in enumerate(E) if set(e) & set(f)) for e in E]

def is_matching(s):
    return all(not ((s >> i) & 1) or (s & (INC[i] ^ (1 << i))) == 0 for i in range(N))

def is_maximal(s):
    return is_matching(s) and all((s & INC[i]) != 0 for i in range(N))

concepts = [s for s in range(1 << N) if is_maximal(s)]
faces = [s for s in range(1 << N) if len({x & s for x in concepts}) == (1 << s.bit_count())]
face_set = set(faces)
facets = [s for s in faces if all((s | (1 << j)) not in face_set for j in range(N) if not (s >> j) & 1)]
assert Counter(s.bit_count() for s in concepts) == {4: 9, 3: 8}
assert Counter(s.bit_count() for s in faces) == {0: 1, 1: 12, 2: 42, 3: 32}
assert Counter(s.bit_count() for s in facets) == {2: 6, 3: 32}

# A direction class consists of four mutually parallel cube edges.
D = [sum(1 << i for i, (u, v) in enumerate(E) if (u ^ v) == (1 << d)) for d in range(3)]
assert all(x.bit_count() == 4 for x in D)

def structural(s):
    if not is_matching(s) or s.bit_count() > 3:
        return False
    return all((s & x).bit_count() < 3 for x in D)

assert all((s in face_set) == structural(s) for s in range(1 << N))

# Full octahedral group of the cube = coordinate permutations and bit translations.
edge_index = {e: i for i, e in enumerate(E)}
actions = []
for perm in permutations(range(3)):
    for t in range(8):
        def moved(v):
            return t ^ sum(((v >> j) & 1) << perm[j] for j in range(3))
        actions.append(tuple(edge_index[tuple(sorted((moved(u), moved(v))))] for u, v in E))
assert len(set(actions)) == 48

def orbit(s):
    return {sum(1 << p[i] for i in range(N) if (s >> i) & 1) for p in actions}

def orbit_table(group):
    remaining = set(group)
    rows = []
    while remaining:
        s = min(remaining)
        o = orbit(s)
        assert o <= remaining
        remaining -= o
        rows.append((s, len(o), len({x & s for x in concepts})))
    return rows

expected = [(0, 1, 1), (1, 12, 2), (10, 12, 4), (12, 24, 4),
            (80, 6, 4), (52, 24, 8), (84, 12, 7), (328, 8, 8),
            (212, 3, 10), (449, 6, 12)]
actual = []
for k in range(5):
    actual.extend(orbit_table(s for s in range(1 << N) if is_matching(s) and s.bit_count() == k))
assert actual == expected, (actual, expected)

# Oriented boundary over Z: order edges by mask; on a triple remove the j-th ordered edge with sign (-1)^j.
pairs = sorted(s for s in faces if s.bit_count() == 2)
triples = sorted(s for s in faces if s.bit_count() == 3)
pi = {s: i for i, s in enumerate(pairs)}
B = [[0] * len(triples) for _ in pairs]
for col, s in enumerate(triples):
    selected = [i for i in range(N) if (s >> i) & 1]
    for j, i in enumerate(selected):
        B[pi[s ^ (1 << i)]][col] = 1 if j % 2 == 0 else -1

# Rational rank via exact Fraction elimination.
def rational_rank(M):
    A = [[Fraction(x) for x in row] for row in M]
    R, C = len(A), len(A[0])
    r = 0
    for c in range(C):
        pivot = next((i for i in range(r, R) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        b = A[r][c]
        for j in range(c, C):
            A[r][j] /= b
        for i in range(r + 1, R):
            b = A[i][c]
            if b:
                for j in range(c, C):
                    A[i][j] -= b * A[r][j]
        r += 1
    return r

assert rational_rank(B) == 25

ROWS = [0,1,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,20,21,22,23,25,26,30,31]
COLS = [0,1,2,3,4,5,6,7,8,10,11,12,13,14,16,17,18,19,20,22,24,25,26,28,30]
# Bareiss determinant algorithm, all integer operations exact.
def det_bareiss(A):
    A = [list(row) for row in A]
    n = len(A)
    denominator = 1
    sign = 1
    for k in range(n - 1):
        if not A[k][k]:
            h = next((i for i in range(k + 1, n) if A[i][k]), None)
            assert h is not None
            A[h], A[k] = A[k], A[h]
            sign = -sign
        p = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = A[i][j] * p - A[i][k] * A[k][j]
                assert numerator % denominator == 0
                A[i][j] = numerator // denominator
            A[i][k] = 0
        denominator = p
    return sign * A[-1][-1]
minor = [[B[i][j] for j in COLS] for i in ROWS]
assert det_bareiss(minor) == 1

# 1-skeleton is connected; reduced boundary from 12 vertices to the empty face has rank 1.
# The 42 x 32 boundary has rank 25 and a unimodular rank minor, so its image is primitive.
# Thus reduced H_1 = Z^(42-11-25) and H_2 = Z^(32-25).
print('cube_edges=12 maximal_matchings=17 sizes=(3:8,4:9)')
print('shattered_coefficients=1,12,42,32; facets=(2:6,3:32)')
print('support_orbit_table=' + str(expected))
print('boundary2_rational_rank=25 unimodular_25x25_minor_det=1')
print('reduced_integral_homology=H1:Z^6,H2:Z^7')
