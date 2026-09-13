# Single-row Kramer-Mesner check + explicit SDS witness for lane-1708 target.
# Stdlib only. Run: python3 sds_single_row.py  (from any directory)
import sys
from itertools import combinations, product

N = 24  # orbit length; group C24

def diff_totals(family):
    """Sum of ordered-difference counts over all sets; index d=0..23."""
    tot = [0] * N
    for S in family:
        L = list(S)
        for a in L:
            for b in L:
                if a != b:
                    tot[(a - b) % N] += 1
    return tot

def mask(S):
    m = 0
    for x in S:
        m |= (1 << (x % N))
    return m

def popcount(x):
    return bin(x).count("1")

def rot(m, t):
    t %= N
    if t == 0:
        return m
    return ((m << t) | (m >> (N - t))) & ((1 << N) - 1)

# ---- Part 1: row-type lemma ----
# Row of 4x4 orbit matrix R: entries 0..20, sum 20, square-sum 112
# (from R R^T = 96 J + 16 I with all orbit sizes 24: diag 96+16=112).
vecs = [t for t in product(range(21), repeat=4)
        if sum(t) == 20 and sum(x * x for x in t) == 112]
types = sorted(set(tuple(sorted(t)) for t in vecs))
assert types == [(2, 6, 6, 6), (4, 4, 4, 8)], types
print("Part1 row types:", types, " nvecs=", len(vecs))

# ---- Part 2: full 4x4 orbit matrices (ordered rows), col sum 20, dots 96/112 ----
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))
quads = []
for q in product(vecs, repeat=4):
    ok = all(dot(q[a], q[b]) == 96 for a in range(4) for b in range(a + 1, 4))
    ok = ok and all(sum(q[i][j] for i in range(4)) == 20 for j in range(4))
    if ok:
        quads.append(q)
assert len(quads) == 48, len(quads)
print("Part2 orbit matrices (ordered-row count):", len(quads))
# every such matrix uses a single row-type and four distinct row perms
for q in quads:
    assert len(set(q)) == 4
assert all(set(tuple(sorted(r)) for r in q) in ({(2, 6, 6, 6)}, {(4, 4, 4, 8)})
           for q in quads)
print("Part2b: each matrix is single-type with 4 distinct row perms: OK")

# ---- Part 3: explicit single-row SDS witness, type A, 2-set {0,1} ----
S0 = {0, 1}
A = {0, 1, 2, 3, 7, 12}
B = {0, 2, 5, 9, 15, 18}
C = {0, 2, 7, 10, 14, 18}
assert len(S0) == 2 and len(A) == len(B) == len(C) == 6
t = diff_totals([S0, A, B, C])
assert all(t[d] == 4 for d in range(1, N)), t[1:]
print("Part3 single-row SDS diff totals:", t[1:])
F0m = [mask(S) for S in (S0, A, B, C)]
selfx = [sum(popcount(F0m[j] & rot(F0m[j], tt)) for j in range(4))
         for tt in range(N)]
assert selfx[0] == 20 and all(v == 4 for v in selfx[1:]), selfx
print("Part3b self cross-correlation:", selfx)

# ---- Part 4: row-compatibility sum identity ----
# Two distinct block-orbit rows need cross(t)=4 for all 24 t, i.e. total 96,
# but sum_t cross(t) = sum_j s_j f_j. Same type-A perm in same position: 112.
s = (2, 6, 6, 6)
assert sum(a * b for a, b in zip(s, s)) == 112  # -> same-position reuse impossible
s2 = (6, 2, 6, 6)
assert sum(a * b for a, b in zip(s, s2)) == 96  # distinct perm: compatible total
print("Part4 sum identity (112 vs 96): OK")
print("ALL CHECKS PASSED")
