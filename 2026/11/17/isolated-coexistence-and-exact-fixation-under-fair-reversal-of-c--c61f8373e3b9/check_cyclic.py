"""Exact finite-word checks for symmetric sign-switching cyclic Volterra dynamics.

This checks one rational parameter instance. Infinite-time claims depend on
analytic martingale and Lyapunov arguments, not finite enumeration.
"""
from fractions import Fraction as F
from itertools import product

a, b, c = F(1, 2), F(1, 3), F(1, 4)
A = ((F(0), a, -c), (-a, F(0), b), (c, -b, F(0)))
r = (b / (a+b+c), c / (a+b+c), a / (a+b+c))
start = (F(1, 2), F(1, 3), F(1, 6))

assert r == (F(4, 13), F(3, 13), F(6, 13))
assert all(sum(A[i][j] * r[j] for j in range(3)) == 0 for i in range(3))
assert all(sum(r[i] * A[i][j] for i in range(3)) == 0 for j in range(3))

def step(p, sign):
    drift = tuple(sum(A[i][j] * p[j] for j in range(3)) for i in range(3))
    next_p = tuple(p[i] * (1 + sign * drift[i]) for i in range(3))
    assert sum(next_p) == 1 and all(0 <= t <= 1 for t in next_p)
    return next_p

def potential(p):
    return p[0]**4 * p[1]**3 * p[2]**6

assert step(r, 1) == r == step(r, -1)
checks = 0
for n in range(1, 6):
    means = [F(0), F(0), F(0)]
    for signs in product((-1, 1), repeat=n):
        p = start
        for sign in signs:
            next_p = step(p, sign)
            assert potential(next_p) <= potential(p)
            if p != r and all(t > 0 for t in p):
                assert potential(next_p) < potential(p)
            p = next_p
        for i in range(3):
            means[i] += p[i] / (2**n)
        checks += 1
    assert tuple(means) == start

for p in (start, (F(2, 5), F(1, 5), F(2, 5)), r):
    plus, minus = step(p, 1), step(p, -1)
    for i in range(3):
        drift = sum(A[i][j] * p[j] for j in range(3))
        assert (plus[i] + minus[i]) / 2 == p[i]
        assert (plus[i]**2 + minus[i]**2) / 2 - p[i]**2 == p[i]**2 * drift**2

print('CYCLIC_VOLTERRA_EXACT_OK words=62 kernel=PASS Lyapunov=PASS martingale=PASS')
