#!/usr/bin/env python3
"""Exact audit of the Pascal-line Steiner/Kirkman concurrence graph.
Run: python3 verify_pascal.py. Standard library only.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import prod
from fractions import Fraction

N = 6

def canon(p):
    p = tuple(p)
    q = p[::-1]
    return min(
        [p[i:] + p[:i] for i in range(N)] +
        [q[i:] + q[:i] for i in range(N)])

HEX = sorted({canon(p) for p in permutations(range(N))})
assert len(HEX) == 60
IDX = {h: i for i, h in enumerate(HEX)}

def cycle_edges(h):
    return frozenset(tuple(sorted((h[i], h[(i+1) % N]))) for i in range(N))

EDGE = list(map(cycle_edges, HEX))

def cyc3(p):
    return min(tuple(p[i:] + p[:i]) for i in range(3))

def square_class(h):
    ab = (h[0::2], h[1::2])
    def key(triples):
        return tuple(sorted(cyc3(tuple(t)) for t in triples))
    return min(key(ab), key(tuple(t[::-1] for t in ab)))

S = defaultdict(set)
for i, h in enumerate(HEX):
    S[square_class(h)].add(i)
STEINER = {frozenset(v) for v in S.values()}
KIRKMAN = {frozenset(j for j, e in enumerate(EDGE) if e.isdisjoint(ee)) for ee in EDGE}
assert len(STEINER) == 20 and all(len(t) == 3 for t in STEINER)
assert len(KIRKMAN) == 60 and all(len(t) == 3 for t in KIRKMAN)

def from_published_triple(strings):
    base = [tuple(ord(c) - ord('A') for c in st) for st in strings]
    return {
        frozenset(IDX[canon(tuple(g[j] for j in h))] for h in base)
        for g in permutations(range(N))
    }

# Independent S_6-orbit construction from Baralic--Spasojevic (2012),
# Propositions 3.2 and 3.3, respectively.
S_ORBIT = from_published_triple(('ABEDCF', 'ADEFCB', 'AFEBCD'))
K_ORBIT = from_published_triple(('ABFDCE', 'AEFBDC', 'ABDFEC'))
assert STEINER == S_ORBIT and KIRKMAN == K_ORBIT

NEIGH = [set() for _ in range(60)]
for tri in STEINER | KIRKMAN:
    for a, b in combinations(sorted(tri), 2):
        assert b not in NEIGH[a], 'Distinct named concurrences share a pair'
        NEIGH[a].add(b); NEIGH[b].add(a)
assert all(len(v) == 8 for v in NEIGH)
assert sum(map(len, NEIGH)) // 2 == 240

seen = {0}; fringe = [0]
while fringe:
    a = fringe.pop()
    for b in NEIGH[a] - seen:
        seen.add(b); fringe.append(b)
assert len(seen) == 60

L = [[(8 if i == j else -int(j in NEIGH[i])) for j in range(60)]
     for i in range(60)]

def minor(root):
    return [[L[i][j] for j in range(60) if j != root]
            for i in range(60) if i != root]

def bareiss_det(A):
    A = [list(map(int, r)) for r in A]
    n = len(A); prev = 1; sign = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            pivot = next((i for i in range(k+1, n) if A[i][k]), None)
            if pivot is None: return 0
            A[k], A[pivot] = A[pivot], A[k]; sign = -sign
        pivot = A[k][k]
        for i in range(k+1, n):
            aik = A[i][k]
            for j in range(k+1, n):
                numerator = pivot * A[i][j] - aik * A[k][j]
                assert numerator % prev == 0
                A[i][j] = numerator // prev
            A[i][k] = 0
        prev = pivot
    return sign * A[-1][-1]

def elementary_valuations(A, p, precision=12):
    """Exact local Smith valuations via unit-pivot Schur complements over Z/p^k."""
    modulus = p**precision
    a = [[x % modulus for x in row] for row in A]
    n = len(a); valuation = 0; result = []
    while n:
        hit = next(((i, j) for i in range(n) for j in range(n)
                    if a[i][j] % p), None)
        if hit is None:
            assert valuation < precision, 'Increase modular precision'
            assert all(x % p == 0 for row in a for x in row)
            a = [[x // p for x in row] for row in a]
            modulus //= p; valuation += 1
            continue
        i, j = hit
        a[0], a[i] = a[i], a[0]
        if j:
            for row in a:
                row[0], row[j] = row[j], row[0]
        inv = pow(a[0][0], -1, modulus)
        first_row = a[0]
        a = [[(a[ii][jj] - a[ii][0] * inv * first_row[jj]) % modulus
              for jj in range(1, n)] for ii in range(1, n)]
        n -= 1
        result.append(valuation)
    return Counter(result)

# Verify the classical six Desargues sectors remain separate until Steiner
# concurrences are included.
k_adj = [set() for _ in range(60)]
for trio in KIRKMAN:
    for a in trio:
        k_adj[a].update(trio - {a})
remaining = set(range(60)); sectors = []
while remaining:
    a = min(remaining); remaining.remove(a); component = {a}; fringe = [a]
    while fringe:
        for b in k_adj[fringe.pop()] & remaining:
            remaining.remove(b); component.add(b); fringe.append(b)
    sectors.append(component)
assert len(sectors) == 6 and all(len(c) == 10 for c in sectors)
assert all(sum(len(k_adj[a]) for a in c) == 60 for c in sectors)
assert all(sum(bool(tr & c) for c in sectors) == 3 for tr in STEINER)

def rank_q(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    n = len(a); r = 0
    for j in range(n):
        pivot = next((i for i in range(r, n) if a[i][j]), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        den = a[r][j]
        for jj in range(j, n): a[r][jj] /= den
        for i in range(r + 1, n):
            factor = a[i][j]
            if factor:
                for jj in range(j, n): a[i][jj] -= factor * a[r][jj]
        r += 1
    return r

spectrum = ((0,1),(2,5),(6,14),(8,15),(10,9),(11,16))
assert sum(m for _,m in spectrum) == 60
for eigenvalue, multiplicity in spectrum:
    assert 60 - rank_q([[L[i][j]-(eigenvalue if i==j else 0)
                         for j in range(60)] for i in range(60)]) == multiplicity

expected = {
    2: {0: 36, 1: 8, 3: 1, 4: 10, 5: 4},
    3: {0: 46, 1: 13},
    5: {0: 51, 1: 8},
    11: {0: 43, 1: 16}
}
order = 2**71 * 3**13 * 5**8 * 11**16
for root in (0, 17, 59):
    M = minor(root)
    for p, pattern in expected.items():
        actual = elementary_valuations(M, p)
        assert dict(actual) == pattern, (root, p, actual)
    assert bareiss_det(M) == order, root

invariants = [2]*7 + [22, 88, 176] + [528]*5 + [2640]*4 + [5280]*4
assert len(invariants) == 23 and prod(invariants) == order
assert all(b % a == 0 for a, b in zip(invariants, invariants[1:]))
print('PASCAL_60_COMBINED_CONCURRENCE_CRITICAL_GROUP_VERIFIED_OK')
print('vertices=60 edges=240 regular_degree=8 source_orbits=20+60')
print('spectrum=', spectrum, 'kirkman_sectors=', [len(c) for c in sectors])
print('elementary_divisors=', {p:dict(v) for p,v in expected.items()})
print('invariant_factors=', invariants)
print('spanning_trees=', order)
