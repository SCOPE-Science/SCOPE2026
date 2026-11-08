"""Independent finite checks for domination roots of clique windmills.

Requires Python 3.10+ and SymPy. The unbounded theorem is proved separately.
"""
from itertools import product
from math import comb
from sympy import Poly, Symbol, oo, expand

z = Symbol('z')


def polynomial(k, m):
    return Poly(expand(z * (1 + z) ** (k * m) + ((1 + z) ** k - 1) ** m), z)


def enumerated_coefficients(k, m):
    n = 1 + k * m
    neighbors = [0] * n
    for u in range(1, n):
        neighbors[0] |= 1 << u
        neighbors[u] |= 1
    for blade in range(m):
        vv = range(1 + k * blade, 1 + k * (blade + 1))
        for u in vv:
            for v in vv:
                if u != v:
                    neighbors[u] |= 1 << v
    counts = [0] * (n + 1)
    for mask in range(1 << n):
        if all((mask >> v) & 1 or neighbors[v] & mask for v in range(n)):
            counts[mask.bit_count()] += 1
    return counts


for k, m in [(2, 2), (2, 3), (3, 2), (3, 3), (3, 4),
             (4, 2), (4, 3), (4, 4), (5, 2)]:
    P = polynomial(k, m)
    enumerated = enumerated_coefficients(k, m)
    coefficients = list(reversed([int(c) for c in P.all_coeffs()]))
    assert coefficients == enumerated, (k, m)
    assert coefficients[1] == 1
print('GRAPH_DEFINITION_EXHAUSTIVE_OK 9')

for k in range(2, 8):
    for m in range(2, 8):
        P = polynomial(k, m)
        Q, remainder = P.div(Poly(z, z))
        assert remainder.is_zero and Q.eval(0) == 1
        low = Q.count_roots(-oo, -2)
        mid = Q.count_roots(-2, -1)
        near = Q.count_roots(-1, 0)
        positive = Q.count_roots(0, oo)
        assert Q.eval(-2) != 0 and Q.eval(-1) != 0
        expected = ((1 if k % 2 else 0), (1 if k % 2 == 0 and m % 2 == 0 else 0),
                    (1 if m % 2 == 0 else 0), 0)
        if m % 2 == 1 and k % 2 == 0:
            expected = (0, 0, 0, 0)
        if m % 2 == 1 and k % 2 == 1:
            expected = (1, 0, 0, 0)
        assert (low, mid, near, positive) == expected, (k, m, (low, mid, near, positive), expected)
print('EXACT_STURM_INTERVAL_COUNTS_OK 36')
print('VERIFY_OK')
