#!/usr/bin/env python3
"""Exact arithmetic corroboration for centered coordinate-cross fourth moments.

Uses only the Python standard library. A finite checker cannot replace
analytical arguments about all dimensions or all phase alphabets.
"""
from itertools import product
from collections import defaultdict
from random import Random

U = (1, -1, 1j, -1j)

def energy(d, center, positive, negative):
    f = {(0,) * d: center}
    for j in range(d):
        e = [0] * d
        e[j] = 1
        f[tuple(e)] = positive[j]
        e[j] = -1
        f[tuple(e)] = negative[j]
    squared = defaultdict(complex)
    for u, a in f.items():
        for v, b in f.items():
            squared[tuple(k + l for k, l in zip(u, v))] += a * b
    result = sum(abs(z) ** 2 for z in squared.values())
    assert result == int(result)
    return int(result)

def predicted(d, center, positive, negative):
    x = [a*b/(center*center) for a,b in zip(positive, negative)]
    return int(8*d*d+2*d+4*abs(sum(x)+0.5)**2)

checked = 0
for d in (2,3,4):
    for negative in product(U, repeat=d):
        actual = energy(d, 1, [1]*d, negative)
        predicted_value = predicted(d, 1, [1]*d, negative)
        assert actual == predicted_value, (d, negative, actual, predicted_value)
        checked += 1

rng = Random(20261112)
for d in (2, 3, 4, 5):
    for _ in range(60):
        center = rng.choice(U)
        positive = [rng.choice(U) for _ in range(d)]
        negative = [rng.choice(U) for _ in range(d)]
        actual = energy(d, center, positive, negative)
        expected = predicted(d, center, positive, negative)
        assert actual == expected, (d, center, positive, negative, actual, expected)
        checked += 1

# Exact arithmetic in Q(sqrt(5)): a + b*sqrt(5) represented by (a,b).
def sign(a, b):
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if a > 0 and b > 0:
        return 1
    if a < 0 and b < 0:
        return -1
    if a > 0 and b < 0:
        return (a*a > 5*b*b) - (a*a < 5*b*b)
    return (5*b*b > a*a) - (5*b*b < a*a)

# 4*cos(2*pi*r/5) = A_r + B_r*sqrt(5).
cos4 = [(4,0), (-1,1), (-1,-1), (-1,-1), (-1,1)]
levels = {}
for i,j in product(range(5), repeat=2):
    a0,b0 = cos4[(i-j)%5]
    a1,b1 = cos4[i]
    a2,b2 = cos4[j]
    level = (45 + 2*a0 + a1 + a2, 2*b0 + b1 + b2)
    levels[(i,j)] = level
sharp5 = (41,-2)
optimizers = {(1,3), (2,4), (3,1), (4,2)}
assert {p for p,z in levels.items() if z == sharp5} == optimizers
for z in levels.values():
    assert sign(z[0]-sharp5[0], z[1]-sharp5[1]) >= 0

# Ternary count check is finite corroboration of the residue argument.
for d in range(2,31):
    achievable = []
    for a in range(d+1):
        for b in range(d-a+1):
            c = d-a-b
            achievable.append((3*a-d+1)**2 + 3*(b-c)**2)
    assert min(achievable) == (3 if d%3==1 else 1)

print('CENTERED_CROSS_FOURTH_PASS',
      'gaussian_convolutions=', checked,
      'quintic_alphabet_exact_cases=', len(levels),
      'ternary_dimensions=', 29)
