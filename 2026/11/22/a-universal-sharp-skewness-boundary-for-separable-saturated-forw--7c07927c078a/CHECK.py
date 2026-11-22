"""Exact-rational finite checks for the stated planar saturated forward iteration.

The analytic proof establishes all-parameter statements; this file checks examples,
sharpness witnesses and the identities that enter that proof. Python 3 standard library.
"""
from fractions import Fraction as Q
from itertools import product

checks = 0


def verify(ok, explanation):
    global checks
    assert ok, explanation
    checks += 1


def sat(t):
    return t / (1 + abs(t))


def F(s, x):
    a, b = x
    return (a - s * b, s * a + b)


def inverseF(s, y):
    a, b = y
    d = 1 + s * s
    return ((a + s * b) / d, (b - s * a) / d)


def norm2(x):
    return sum(t * t for t in x)


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def forward(s, gamma, x):
    y = F(s, x)
    g = tuple(map(sat, y))
    return tuple(t - gamma * z for t, z in zip(x, g))


# Exact inversion, and the one-step Fejer inequality within the claimed region.
values = [Q(k, 3) for k in range(-12, 13)]
for s in [Q(-1), Q(-1, 2), Q(0), Q(1, 5), Q(1, 2), Q(1)]:
    d = 1 + s * s
    for x in product(values, repeat=2):
        verify(inverseF(s, F(s, x)) == x, 'inverse')
        y = F(s, x)
        g = tuple(map(sat, y))
        verify(dot(x, g) * d >= norm2(g), 'core angular inequality')
        for t in [Q(1, 10), Q(1, 2), Q(1)]:
            gamma = (2 / d) * t
            verify(norm2(forward(s, gamma, x)) <= norm2(x), 'Fejer inside region')

# Every supercritical step increases distance from zero near that zero.
for s in [Q(-2), Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1), Q(2)]:
    d = 1 + s*s
    gamma = Q(201, 100) / d
    x = (Q(1, 100000), Q(1, 200000))
    verify(norm2(forward(s, gamma, x)) > norm2(x), 'sharp supercritical step')

# Every large skew permits a finite distance increase even for subcritical steps.
for s in [Q(5, 4), Q(3, 2), Q(2), Q(5)]:
    v = 2 / (s-1)
    y = (Q(100000), v)
    x = inverseF(s, y)
    g = tuple(map(sat, y))
    verify(dot(x, g) < 0, 'negative Euclidean drift')
    for gamma in [Q(1, 10000), 1 / (1+s*s), 2 / (1+s*s)]:
        verify(norm2(forward(s, gamma, x)) > norm2(x), 'large skew step increases norm')

# Pairwise nonexpansiveness fails by a derivative witness: for y=(0,v),
# DT(x)e2=(gamma*s, 1-gamma/(1+v)^2), whose norm exceeds one.
for s in [Q(-2), Q(-1), Q(-1, 10), Q(1, 10), Q(1), Q(2)]:
    for gamma in [Q(1, 10), Q(1), Q(2)]:
        v = Q(100000)
        column = (gamma*s, 1-gamma/(1+v)**2)
        verify(norm2(column) > 1, 'nonexpansive differential obstruction')

# A sharp positive-step counterexample for the published s=2 example.
s, gamma, y = Q(2), Q(1, 5), (Q(30), Q(2))
x = inverseF(s, y)
verify(norm2(forward(s, gamma, x)) > norm2(x), 'paper-family witness')

print(f'VERIFY_OK {checks} exact-rational assertions')
