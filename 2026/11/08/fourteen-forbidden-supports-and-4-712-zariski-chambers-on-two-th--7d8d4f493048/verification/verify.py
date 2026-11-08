#!/usr/bin/env python3
"""Exact Zariski-support enumeration for the 3-torsion IV* elliptic configuration.

Only Python's standard library is required. All matrix calculations are over Q
or Z; the enumeration is complete over the 2**13 subsets of negative curves.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

N = 13
C = 0
A = (1, 2, 3)
B = (4, 5, 6)
T = (7, 8, 9)
S = (10, 11, 12)
LABELS = ("C", "A0", "A1", "A2", "B0", "B1", "B2",
          "T0", "T1", "T2", "S0", "S1", "S2")

M = [[0] * N for _ in range(N)]
for i in range(N):
    M[i][i] = -1 if i in S else -2
EDGES = set()
def edge(i, j):
    assert i != j
    i, j = sorted((i, j))
    assert (i, j) not in EDGES
    EDGES.add((i, j))
    M[i][j] = M[j][i] = 1
for i in range(3):
    edge(C, A[i])
    edge(A[i], B[i])
    edge(B[i], S[i])
    edge(S[i], T[i])
for i, j in combinations(range(3), 2):
    edge(T[i], T[j])
assert len(EDGES) == 15


def leading_negative_definite(mask):
    """Sylvester criterion, exact rational LDL without pivoting."""
    ix = [i for i in range(N) if mask & (1 << i)]
    if not ix:
        return True
    # Schur elimination on the symmetric principal submatrix.
    mat = [[Fraction(M[i][j]) for j in ix] for i in ix]
    for k in range(len(ix)):
        pivot = mat[k][k]
        if pivot >= 0:
            return False
        for i in range(k + 1, len(ix)):
            for j in range(i, len(ix)):
                mat[i][j] -= mat[i][k] * mat[j][k] / pivot
                mat[j][i] = mat[i][j]
    return True


def bareiss_det(A):
    """Division-exact fraction-free determinant, for an integer matrix."""
    n = len(A)
    if n == 0:
        return 1
    a = [row[:] for row in A]
    sign, previous = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numer = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numer % previous == 0
                a[i][j] = numer // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[n-1][n-1]


def minor_test(mask):
    """Independent integer Sylvester test via all leading determinants."""
    ix = [i for i in range(N) if mask & (1 << i)]
    for k in range(1, len(ix) + 1):
        b = [[M[i][j] for j in ix[:k]] for i in ix[:k]]
        if (-1)**k * bareiss_det(b) <= 0:
            return False
    return True


def bitset(indices):
    return sum(1 << j for j in indices)

FORBIDDEN = [bitset(list((C,)) + list(A) + list(B)), bitset(T)]
for i in range(3):
    FORBIDDEN += [
        bitset((B[i], T[i], S[i])),
        bitset((C,) + A + (B[i], S[i]))]
for i, j in combinations(range(3), 2):
    FORBIDDEN += [
        bitset((T[i], T[j], S[i], S[j])),
        bitset((C, A[i], A[j], B[i], B[j], S[i], S[j]))]
assert len(FORBIDDEN) == len(set(FORBIDDEN)) == 14


def allowed(mask):
    return all(mask & block != block for block in FORBIDDEN)


def main():
    counter = Counter()
    actual_bad = set()
    for mask in range(1 << N):
        via_q = leading_negative_definite(mask)
        via_z = minor_test(mask)
        via_forbidden = allowed(mask)
        assert via_q == via_z == via_forbidden, (mask, via_q, via_z, via_forbidden)
        if via_q:
            counter[mask.bit_count()] += 1
        else:
            actual_bad.add(mask)
    minimal_bad = {mask for mask in actual_bad if all(
        mask ^ (1 << i) not in actual_bad for i in range(N) if mask & (1 << i))}
    assert minimal_bad == set(FORBIDDEN)
    assert all(not leading_negative_definite(f) for f in FORBIDDEN)
    for f in FORBIDDEN:
        ix = [i for i in range(N) if f & (1 << i)]
        assert bareiss_det([[M[i][j] for j in ix] for i in ix]) == 0
    assert all(leading_negative_definite(f ^ (1 << j))
               for f in FORBIDDEN for j in range(N) if f & (1 << j))
    # Inclusion-exclusion as an independent polynomial count.
    ie = [0] * (N + 1)
    for choice in range(1 << len(FORBIDDEN)):
        union = 0
        for j, f in enumerate(FORBIDDEN):
            if choice & (1 << j):
                union |= f
        u = union.bit_count()
        sgn = (-1)**choice.bit_count()
        for k in range(u, N + 1):
            ie[k] += sgn * comb(N-u, k-u)
    assert [counter[i] for i in range(N+1)] == ie
    expected = [1,13,78,282,672,1092,1215,896,393,70,0,0,0,0]
    assert ie == expected
    print('NEGATIVE_CURVES',N)
    print('GRAPH_EDGES',len(EDGES))
    print('SUBSETS_EXAMINED',1 << N)
    print('MINIMAL_FORBIDDEN',len(FORBIDDEN))
    print('MINIMAL_FORBIDDEN_SIZE_DISTRIBUTION',dict(sorted(Counter(f.bit_count() for f in FORBIDDEN).items())))
    print('CHAMBER_COUNTS_BY_SUPPORT_SIZE',ie[:10])
    print('CHAMBERS_TOTAL',sum(ie))
    print('MAX_SUPPORT',max(i for i, v in enumerate(ie) if v))
    print('EXACT_RATIONAL_LDL_INTEGER_DETERMINANTS_INCLUSION_EXCLUSION_AGREE')
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    main()
