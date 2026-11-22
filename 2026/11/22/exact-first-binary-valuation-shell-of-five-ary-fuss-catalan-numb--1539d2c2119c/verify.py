#!/usr/bin/env python3
"""Exact first dyadic shell for the quintic Fuss--Catalan coefficients.

This program uses only Python's standard library. It checks polynomial
identities that hold in every degree, then compares a finite range of
independent carry counts. It is not an independent mathematical audit.
"""
from collections import defaultdict

STATES = [(u, v, c) for u in (0, 1) for v in (0, 1) for c in (0, 1)]
INDEX = {s: i for i, s in enumerate(STATES)}
M0 = [[0] * 8 for _ in STATES]
M1 = [[0] * 8 for _ in STATES]
for i, (u, v, c) in enumerate(STATES):
    for a in (0, 1):
        d = (a + u + c) // 2
        target = INDEX[(v, a, d)]
        (M0 if d == 0 else M1)[i][target] += 1

# Each polynomial is a mapping degree -> integer coefficient.
def poly(seq):
    return {i: a for i, a in enumerate(seq) if a}


def add(a, b, scale=1):
    c = defaultdict(int, a)
    for k, val in b.items():
        c[k] += scale * val
    return {k: v for k, v in c.items() if v}


def mult(a, b):
    c = defaultdict(int)
    for i, x in a.items():
        for j, y in b.items():
            c[i + j] += x * y
    return {k: v for k, v in c.items() if v}


def mulmat(A, v):
    result = []
    for row in A:
        pol = {}
        for c, expr in zip(row, v):
            if c:
                pol = add(pol, expr if c == 1 else {k: c * a for k, a in expr.items()})
        result.append(pol)
    return result


D = poly([1, -1, 0, -1, -1])
D2 = mult(D, D)
t = poly([0, 1])
# These 16 explicit polynomial vectors are certificates for the resolvent.
U = [poly(x) for x in ([1, 1, 2, 1], [1, 0, 1, 1], [1, 1], [1],
                     [1, 0, 1, 1], [], [1], [])]
V = [poly(x) for x in ([0, 0, 0, 1, 1], [0, 1, -1], [0, 0, 1, 0, -1],
                     [0, 0, 1, -1], [0, 1, -1], [1, 0, -1, -1, -2, -1],
                     [0, 0, 1, -1], [])]
h0 = [1, 1, 1, 1, 1, 0, 1, 0]
h1 = [0, 0, 0, 0, 0, 1, 0, 0]

for i in range(8):
    lhs = add(U[i], mult(t, mulmat(M0, U)[i]), -1)
    assert lhs == ({k: h0[i] * a for k, a in D.items()} if h0[i] else {}), ('zero', i)
    lhs = add(V[i], mult(t, mulmat(M0, V)[i]), -1)
    rhs = add(({k: h1[i] * a for k, a in D2.items()} if h1[i] else {}),
              mult(mult(t, D), mulmat(M1, U)[i]))
    assert lhs == rhs, ('one', i, lhs, rhs)
assert U[0] == poly([1, 1, 2, 1])
assert V[0] == poly([0, 0, 0, 1, 1])


def coeffs(numerator, denominator, max_index):
    out = []
    for k in range(max_index + 1):
        cur = numerator.get(k, 0)
        for j, a in denominator.items():
            if j != 0 and j <= k:
                cur -= a * out[k - j]
        out.append(cur)
    return out

b0 = coeffs(U[0], D, 16)
b1 = coeffs(V[0], D2, 16)
assert b0[:12] == [1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, 273]
assert b1[:12] == [0, 0, 0, 1, 3, 5, 9, 19, 37, 66, 118, 214]
comparisons = 0
for L in range(17):
    c0 = c1 = 0
    for n in range(1 << L):
        # Legendre's factorial valuation formula, independent of the transfer.
        v = n.bit_count() + (4 * n).bit_count() - (5 * n).bit_count()
        c0 += v == 0
        c1 += v == 1
        comparisons += 1
    assert (c0, c1) == (b0[L], b1[L]), (L, (c0, c1), (b0[L], b1[L]))
print('VERIFY_OK exact_resolvent_vector_identities=16 all_dyadic_blocks=17 index_comparisons=' + str(comparisons))
