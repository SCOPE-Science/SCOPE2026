#!/usr/bin/env python3
"""Finite arithmetic and quadrature diagnostics for normalized chainability envelopes.

Uses only the Python standard library.  Numerical checks are not a proof of
statements quantified over arbitrary probability measures or all chain depths.
"""
from math import comb, exp, factorial

assertions = 0


def check(condition, message):
    global assertions
    assert condition, message
    assertions += 1


def inverse_moments(terminal_value, depth, order):
    """Raw moments under repeated inverse positive-chain transformations."""
    layers = [[terminal_value ** k for k in range(order + 1)]]
    for _ in range(depth):
        nxt = layers[-1]
        cur = [1]
        for k in range(order):
            cur.append(sum(comb(k, j) * cur[j] * nxt[k-j]
                           for j in range(k + 1)))
        layers.append(cur)
    return layers[-1]


# The first N moments are factorial, whereas the (N+1)st depends on the
# terminal mean; the terminal point masses 0, 1, 2 test both directions.
for depth in range(1, 13):
    for terminal in (0, 1, 2):
        moments = inverse_moments(terminal, depth, depth + 1)
        for k in range(depth + 1):
            check(moments[k] == factorial(k),
                  ('moment', depth, terminal, k, moments[k]))
        check(moments[depth+1] == factorial(depth+1) + terminal - 1,
              ('frontier', depth, terminal))

GRID = 1500
LIMIT = 3.0
STEP = LIMIT / GRID
xs = [j * STEP for j in range(GRID + 1)]


def T(f):
    out = [1.0]
    cumulative = 0.0
    for i in range(1, len(f)):
        cumulative += (f[i-1] + f[i]) * STEP / 2
        out.append(exp(-cumulative))
    return out


def T_power(f, count):
    for _ in range(count):
        f = T(f)
    return f


h = [[0.0 for _ in xs]]
for _ in range(10):
    h.append(T(h[-1]))
ref = [1/(1+x) for x in xs]

for depth in range(1, 9):
    lo = [min(h[depth][j], h[depth+1][j]) for j in range(len(xs))]
    hi = [max(h[depth][j], h[depth+1][j]) for j in range(len(xs))]
    for param in (0, 0.25, 1, 3, 20):
        actual = T_power([exp(-param*x) for x in xs], depth)
        for j in range(0, len(xs), 25):
            check(lo[j] - 1e-9 <= actual[j] <= hi[j] + 1e-9,
                  ('envelope', depth, param, j))
            check(abs(actual[j] - ref[j]) < xs[j]**depth / factorial(depth) + 6e-6,
                  ('factorial contraction', depth, param, j))
    for j in range(20, len(xs), 60):
        check(lo[j] - 4e-6 <= ref[j] <= hi[j] + 4e-6,
              ('reference is bracketed', depth, j))

# The first few endpoint curves admit closed forms.
for j in range(0, GRID+1, 30):
    x = xs[j]
    check(abs(h[1][j]-1.0) < 1e-12, 'h1')
    check(abs(h[2][j]-exp(-x)) < 1e-6, 'h2')
    check(abs(h[3][j]-exp(-(1-exp(-x)))) < 3e-6, 'h3')

print(f'PASS: {assertions} finite exact and quadrature diagnostics')
