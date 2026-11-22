#!/usr/bin/env python3
"""Exact independent spanning-tree, Walsh and signed-matrix-tree check for a six-rim wheel."""
from itertools import combinations
from collections import Counter
from fractions import Fraction

N = 7
EDGES = [(0, v) for v in range(1, 7)] + [(v, 1 + v % 6) for v in range(1, 7)]

def is_tree(combo):
    p = list(range(N))
    def root(x):
        while p[x] != x:
            x = p[x]
        return x
    for j in combo:
        a, b = EDGES[j]
        a, b = root(a), root(b)
        if a == b:
            return False
        p[a] = b
    return len({root(i) for i in range(N)}) == 1

def walsh(a):
    a = a[:]
    for j in range(N):
        bit = 1 << j
        for m in range(1 << N):
            if not m & bit:
                v, w = a[m], a[m | bit]
                a[m], a[m | bit] = v + w, v - w
    return a

def det_exact(a):
    n = len(a)
    out = 0
    # Leibniz determinant from permutation parity; independent of the tree enumerator.
    def rec(row, used, prod, odd):
        nonlocal out
        if row == n:
            out += (-1 if odd else 1) * prod
            return
        for col in range(n):
            if not used & (1 << col) and a[row][col]:
                rec(row + 1, used | (1 << col), prod * a[row][col], odd ^ ((used >> (col + 1)).bit_count() & 1))
    rec(0, 0, 1, 0)
    return out

def signed_laplacian(mask):
    signs = [1 if not (mask >> j & 1) else -1 for j in range(N)]
    mat = [[0] * 6 for _ in range(6)]
    for a,b in EDGES:
        w = signs[a] * signs[b]
        if a:
            mat[a-1][a-1] += w
        if b:
            mat[b-1][b-1] += w
        if a and b:
            mat[a-1][b-1] -= w
            mat[b-1][a-1] -= w
    return mat

counts = [0] * 128
for sub in combinations(range(12), 6):
    if not is_tree(sub):
        continue
    bit = 0
    for i in sub:
        a, b = EDGES[i]
        bit ^= (1 << a) | (1 << b)
    counts[bit] += 1
assert sum(counts) == 320
assert all(v == 0 for i,v in enumerate(counts) if i.bit_count() % 2)
lam = walsh(counts)
assert Counter(lam) == {-52:12,-16:12,-4:40,0:38,12:12,16:12,320:2}
# Independently compute all 128 Walsh eigenvalues using signed matrix-tree determinants.
for m in range(128):
    assert lam[m] == det_exact(signed_laplacian(m)), (m,lam[m])
    assert lam[m] == lam[m ^ 127]
# Verify that twelve rotation/reflection classes plus final class exhaust 64 rim assignments.
seen = set()
profile = []
for b in range(64):
    if b in seen:
        continue
    orbit = set()
    for shift in range(6):
        for reverse in (0,1):
            x = 0
            for i in range(6):
                if (b >> i) & 1:
                    x |= 1 << ((-i if reverse else i) + shift) % 6
            orbit.add(x)
    seen |= orbit
    profile.append((b, len(orbit), lam[b << 1]))
assert len(profile) == 13 and len(seen) == 64
assert profile == [
 (0,1,320),(1,6,-52),(3,6,16),(5,6,-16),(7,6,12),
 (9,3,0),(11,12,-4),(15,6,0),(21,2,-4),(23,6,0),
 (27,3,0),(31,6,-4),(63,1,0)]
visibility = [int(v != 0) for v in lam]
projection_numerators = walsh(visibility)
assert Counter(projection_numerators) == {0:64,2:32,-6:18,10:12,90:1,-38:1}
assert sum(map(abs,projection_numerators)) == 420
assert Fraction(420,128) == Fraction(105,32)
assert min(abs(v) for v in lam if v) == 4
print('PASS: 320 spanning trees, 128 independent determinants, 13 dihedral classes, spectral multiplicities, 38 zeros, and sharp endpoint norm 105/32')
