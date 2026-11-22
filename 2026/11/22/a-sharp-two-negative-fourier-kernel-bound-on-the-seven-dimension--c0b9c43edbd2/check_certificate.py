"""Exact rational checks for a two-negative eight-point Fourier-kernel bound.

Run: python3 check_certificate.py
No third-party packages. These checks verify finite rational identities used
in the analytic proof, rather than replacing the compact-group Fourier theorem.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb

checks = 0


def check(actual, expected):
    global checks
    assert actual == expected, (actual, expected)
    checks += 1


def elementary(values, order):
    return sum((product_of(values[i] for i in subset)
                for subset in combinations(range(len(values)), order)), 0)


def product_of(values):
    z = 1
    for value in values:
        z *= value
    return z


def f_at_signs(values):
    first, rest = values[0], values[1:]
    return Q(3, 28) + Q(1, 28) * elementary(rest, 2) + Q(1, 56) * first * elementary(rest, 3)


def krawtchouk(k, t):
    return sum((-1)**j * comb(t, j) * comb(6-t, k-j)
               for j in range(k+1) if j <= t and k-j <= 6-t)


vertex_tables = [
    [Q(v, 7) for v in (7, 2, 0, 0, 1, 2, 2)],
    [Q(v, 7) for v in (2, 2, 1, 0, 0, 2, 7)],
]
slack_tables = [
    (0, 36, 0, 4, 96, 260, 416),
    (260, 80, 20, 0, 4, 80, 340),
]
for h in range(2):
    for t in range(7):
        value = f_at_signs([(-1)**h] + [-1]*t + [1]*(6-t))
        check(value, vertex_tables[h][t])
        check(value >= 0, True)
    for k in range(7):
        a = Q(krawtchouk(k, 3), comb(6, k))
        b = (-1)**h * Q(krawtchouk(k, 4), comb(6, k))
        w = 5 - 2*k - (-1)**h
        slack = 7*(w*w-Q(12, 7)-Q(40, 7)*a-Q(60, 7)*b)
        check(slack, slack_tables[h][k])
        check(slack >= 0, True)

for signs in product((-1, 1), repeat=7):
    check(f_at_signs(signs) >= 0, True)
    h = int(signs[0] == -1)
    t = sum(a == -1 for a in signs[1:])
    check(f_at_signs(signs), vertex_tables[h][t])

# The explicit function is a positive combination of 36 cosine-character
# products. Each product has nonnegative Fourier coefficients.
weights = {(0,)*7: Q(3, 28)}
for subset in combinations(range(1, 7), 2):
    weights[tuple(int(i in subset) for i in range(7))] = Q(1, 28)
for subset in combinations(range(1, 7), 3):
    weights[tuple(int(i == 0 or i in subset) for i in range(7))] = Q(1, 56)
check(len(weights), 36)
check(sum(weights.values()), Q(1))
for bitvector in product((0, 1), repeat=7):
    spectral_reconstruction = sum(
        coefficient * (-1)**sum(u*v for u, v in zip(bitvector, parity))
        for parity, coefficient in weights.items())
    check(spectral_reconstruction, f_at_signs([(-1)**u for u in bitvector]))

# Exact eight-node kernel, quadratic form, and comparison threshold.
points = [(1,)*7]
points += [tuple(-1 if k == j else 1 for k in range(7)) for j in range(7)]
contrast = (-1, -1, 1, 1, 1, 1, 1, 1)
matrix = [[f_at_signs([a*b for a, b in zip(x, y)]) for y in points] for x in points]
for i in range(8):
    for j in range(8):
        target = Q(1) if i == j else (Q(0) if i >= 2 and j >= 2 else Q(2, 7))
        check(matrix[i][j], target)
value = sum(contrast[i]*matrix[i][j]*contrast[j] for i in range(8) for j in range(8))
check(value, Q(12, 7))
check(Q(sum(contrast)**2, 8), Q(2))
check(value-Q(sum(contrast)**2, 8), Q(-2, 7))
check(sum(coefficient*(5-2*sum(parity[1:])-(-1)**parity[0])**2
          for parity, coefficient in weights.items()), Q(12, 7))
print(f"PASS: {checks} exact rational assertions")
