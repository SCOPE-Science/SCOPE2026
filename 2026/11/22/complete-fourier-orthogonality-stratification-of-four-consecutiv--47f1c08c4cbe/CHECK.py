"""Reproduce exact and numerical checks of four-atom Fourier packing.
Only Python 3 standard-library modules are required. Finite tests are not proofs.
"""
import cmath
from fractions import Fraction as Q
from itertools import combinations, product
from math import acos, cos, pi, sin, sqrt


def predict(a, b, c, d):
    if a == b == c == d:
        return 4
    if b == c == a + d:
        return 3
    if a + c == b + d:
        return 2
    if d * (d - b) == a * (a - c) and abs(d - b) < 2 * a:
        return 2
    return 1


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def divide(f, g):
    f, g = trim(f), trim(g)
    if g == [Q(0)]:
        raise ZeroDivisionError()
    q = [Q(0)] * max(1, len(f) - len(g) + 1)
    while len(f) >= len(g) and f != [Q(0)]:
        k = len(f) - len(g)
        v = f[-1] / g[-1]
        q[k] = v
        for j, c in enumerate(g):
            f[j + k] -= v * c
        f = trim(f)
    return trim(q), trim(f)


def squarefree_part(p):
    p = [Q(v) for v in p]
    derivative = [Q(i) * p[i] for i in range(1, len(p))]
    f, g = p, trim(derivative)
    while g != [Q(0)]:
        _, r = divide(f, g)
        f, g = g, r
    quotient, remainder = divide(p, f)
    assert remainder == [Q(0)]
    return quotient


def cbrt(x):
    return (1 if x >= 0 else -1) * abs(x) ** (1 / 3)


def polynomial_roots(p):
    # Input coefficients in ascending order, after exact square-free reduction.
    n = len(p) - 1
    if n == 1:
        return [-float(p[0] / p[1])]
    if n == 2:
        a, b, c = map(float, p)
        disc = cmath.sqrt(b * b - 4 * a * c)
        return [(-b + disc) / (2 * c), (-b - disc) / (2 * c)]
    assert n == 3
    d, c, b, a = map(float, p)
    A, B, C = b / a, c / a, d / a
    pp = B - A * A / 3
    qq = 2 * A**3 / 27 - A * B / 3 + C
    discriminant = (qq / 2)**2 + (pp / 3)**3
    if discriminant < -1e-12:
        R = 2 * sqrt(-pp / 3)
        theta = acos(max(-1, min(1, -qq / (2 * sqrt(-(pp / 3)**3))))) / 3
        return [R * cos(theta - 2 * pi * k / 3) - A / 3 for k in range(3)]
    root = sqrt(max(0, discriminant))
    u, v = cbrt(-qq / 2 + root), cbrt(-qq / 2 - root)
    return [u + v - A / 3, -(u + v) / 2 - A / 3 + 1j * sqrt(3) * (u - v) / 2,
            -(u + v) / 2 - A / 3 - 1j * sqrt(3) * (u - v) / 2]


def circle_distance(x, y):
    diff = abs((x - y) % 1)
    return min(diff, 1 - diff)


def observe(a, b, c, d):
    p = squarefree_part([a, b, c, d])
    roots = polynomial_roots(p)
    phases = []
    for z in roots:
        if abs(abs(z) - 1) < 2e-7:
            phase = (cmath.phase(z) / (2 * pi)) % 1
            if not any(circle_distance(phase, r) < 2e-7 for r in phases):
                phases.append(phase)
    if not phases:
        return 1
    candidates = [0] + phases
    for k in range(len(candidates), 1, -1):
        for trial in combinations(candidates, k):
            if all(any(circle_distance((x-y) % 1, r) < 2e-7 for r in phases)
                   for x, y in combinations(trial, 2)):
                return k
    return 2


# Exact coefficient equalities at rational test parameters (no floating point).
for a, d, z, t in product((Q(1), Q(2), Q(3, 2)), repeat=4):
    left = (a + d * z) * (1 + z + z * z)
    right = a + (a + d) * z + (a + d) * z * z + d * z**3
    assert left == right
    left = (z * z - 2 * t * z + 1) * (a + d * z)
    right = a + (d - 2*t*a)*z + (a - 2*t*d)*z*z + d*z**3
    assert left == right

# Independent root construction and graph clique detection for every 1..6 tuple.
counts = {1: 0, 2: 0, 3: 0, 4: 0}
for weights in product(range(1, 7), repeat=4):
    got, expected = observe(*weights), predict(*weights)
    assert got == expected, (weights, got, expected)
    counts[got] += 1
assert counts == {1: 1102, 2: 173, 3: 15, 4: 6}
assert predict(1, 3, 3, 2) == 3
assert predict(1, 1, 1, 1) == 4
assert predict(1, 2, 4, 3) == 2
assert predict(1, 3, 2, 1) == 1
print('PASS: 81 exact factor checks; 1296 phase-graph cases; counts', counts)
