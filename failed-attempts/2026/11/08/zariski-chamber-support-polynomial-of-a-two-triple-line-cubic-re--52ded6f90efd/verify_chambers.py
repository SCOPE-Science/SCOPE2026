"""Exact support enumeration for a two-triple-line blow-up of the plane."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

A = range(3)
B = range(3, 6)
CURVES = ([('E', i) for i in range(6)]
          + [('L', i, j) for i in A for j in B]
          + [('R', 'A'), ('R', 'B')])
assert len(CURVES) == 17

def picard_class(c):
    v = [0] * 7                         # coefficients of H, E_1,...,E_6
    if c[0] == 'E':
        v[c[1] + 1] = 1
    elif c[0] == 'L':
        v[0] = 1
        v[c[1] + 1] = v[c[2] + 1] = -1
    else:
        v[0] = 1
        for i in (A if c[1] == 'A' else B):
            v[i + 1] = -1
    return v

def intersection(u, v):
    return u[0] * v[0] - sum(x * y for x, y in zip(u[1:], v[1:]))

V = [picard_class(c) for c in CURVES]
M = [[intersection(a, b) for b in V] for a in V]
assert [M[i][i] for i in range(17)] == [-1] * 15 + [-2, -2]
assert M[15][16] == 1
assert all(M[15][i] == 0 and M[16][i] == 0 for i in range(6,15))

def negative_definite(indices):
    """Independent exact-rational Cholesky/Schur test of -M positive definite."""
    n = len(indices)
    q = [[-Fraction(M[i][j]) for j in indices] for i in indices]
    for k in range(n):
        p = q[k][k]
        if p <= 0:
            return False
        for i in range(k + 1, n):
            for j in range(i, n):
                q[j][i] -= q[j][k] * q[i][k] / p
                q[i][j] = q[j][i]
        for i in range(k + 1, n):
            q[k][i] = q[i][k] = Fraction(0)
    return True

def pairwise_disjoint_minus_one(selected):
    ids = [i for i in selected if i < 15]
    return all(M[i][j] == 0 for i, j in combinations(ids, 2))

# Full enumeration of 2^17 possible negative-curve supports, independent
# of the closed-form binomial argument. Exact-rational matrix elimination.
DIRECT = Counter()
for mask in range(1 << len(CURVES)):
    subset = [i for i in range(len(CURVES)) if (mask >> i) & 1]
    if not pairwise_disjoint_minus_one(subset):
        continue  # a pair of intersecting (-1)-curves has determinant zero
    if negative_definite(subset):
        DIRECT[len(subset)] += 1

def poly_add(p, q):
    out = Counter(p)
    for d, c in q.items():
        out[d] += c
    return out

def poly_shift_scale(p, degree, scale):
    return Counter({d + degree: c * scale for d, c in p.items()})

def exceptional_and_roots(a, b):
    """Allowed exceptional choices and optional A2 roots, for free E counts a,b."""
    p = Counter()
    for ra in range(a + 1):
        for rb in range(b + 1):
            c = comb(a, ra) * comb(b, rb)
            p[ra + rb] += c
            p[ra + rb + 1] += c * (int(ra <= 1) + int(rb <= 1))
            p[ra + rb + 2] += c * int(ra + rb <= 1)
    return p

# Nonempty disjoint cross-line subsets are single edges, pairs from one
# row or column, or full triples from a row or column.
FORMULA = exceptional_and_roots(3, 3)
for shift, scale, ab in [(1, 9, (2, 2)), (2, 9, (2, 1)),
                         (2, 9, (1, 2)), (3, 3, (2, 0)),
                         (3, 3, (0, 2))]:
    FORMULA = poly_add(FORMULA, poly_shift_scale(
        exceptional_and_roots(*ab), shift, scale))
EXPECTED = [1, 17, 100, 281, 401, 255, 37]
assert [DIRECT[i] for i in range(7)] == EXPECTED, DIRECT
assert [FORMULA[i] for i in range(7)] == EXPECTED, FORMULA
assert sum(DIRECT.values()) == 1092
assert max(DIRECT) == 6
print('NEGATIVE_CURVES=17')
print('TOTAL_SUBSETS_EXAMINED=131072')
print('CHAMBER_SUPPORT_COEFFICIENTS=' + ','.join(map(str, EXPECTED)))
print('CHAMBER_TOTAL=1092')
print('INDEPENDENT_FORMULA_MATCH=YES')
print('ALL_CHECKS_PASSED')
