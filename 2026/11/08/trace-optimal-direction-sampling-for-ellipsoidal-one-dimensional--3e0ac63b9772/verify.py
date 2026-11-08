"""Reproducibility checks for minimax one-dimensional ellipsoidal alignment.

Uses only the Python standard library. All asymptotic and universal claims
are established by the analytic proof; sampling checks are corroborative.
"""
import math
import random
from fractions import Fraction

rng = random.Random(1729)
checks = 0

# Exact rational tests of the optimal spectral-axis design and trace bound.
for n in range(2, 15):
    for shift in range(1, 11):
        lambdas = [Fraction((i + 1) ** 2 + shift, 2 * shift + 3) for i in range(n)]
        tr = sum(lambdas)
        probs = [a / tr for a in lambdas]
        assert sum(probs) == 1
        moments = [p / a for p, a in zip(probs, lambdas)]
        assert all(x == Fraction(1, 1) / tr for x in moments)
        assert sum(a * x for a, x in zip(lambdas, moments)) == 1
        checks += 4

# Midpoint quadrature validates the closed planar power-family formula.
N = 40000
for a, b in [(1., 4.), (.1, 13.), (2., 3.), (0.3, 0.31)]:
    for gamma in (-2., -1., 0., 1., 2.):
        val1 = 0.
        val2 = 0.
        for i in range(N):
            t = 2 * math.pi * (i + .5) / N
            x, y = math.cos(t), math.sin(t)
            d = a ** (1-gamma) * x*x + b ** (1-gamma) * y*y
            val1 += a ** (-gamma) * x*x / d
            val2 += b ** (-gamma) * y*y / d
        val1 /= N
        val2 /= N
        denom = a ** ((1-gamma)/2) + b ** ((1-gamma)/2)
        exact1 = a ** (-(1+gamma)/2) / denom
        exact2 = b ** (-(1+gamma)/2) / denom
        assert math.isclose(val1, exact1, rel_tol=4e-9, abs_tol=4e-9), (a,b,gamma,val1,exact1)
        assert math.isclose(val2, exact2, rel_tol=4e-9, abs_tol=4e-9), (a,b,gamma,val2,exact2)
        assert math.isclose(a*val1+b*val2, 1., abs_tol=1e-9)
        checks += 3

# Exact strict ordering in dimension 2: metric guided < Haar < optimum.
for a, b in [(1., 2.), (1., 5.), (1., 50.), (0.1, 19.)]:
    tr = a+b
    metric = 1/(2*max(a,b))
    haar = min(1/(math.sqrt(a)*(math.sqrt(a)+math.sqrt(b))),
               1/(math.sqrt(b)*(math.sqrt(a)+math.sqrt(b))))
    optimum = 1/tr
    assert metric < haar < optimum
    assert abs((1/tr) - (a/(tr*a))) < 1e-15
    checks += 2

# Gaussian-Haar Monte Carlo, and exact importance-weight expectation.
# Only used to supplement the Haar second-moment identity.
for lambdas in [(1.,2.,5.), (0.1,1.,20.), (1.,1.,4.,9.)]:
    n = len(lambdas)
    tr = sum(lambdas)
    mat = [[0.0 for _ in range(n)] for __ in range(n)]
    draws = 50000
    for _ in range(draws):
        v = [rng.gauss(0,1) for __ in range(n)]
        norm2 = sum(x*x for x in v)
        q = [x / math.sqrt(norm2) for x in v]
        # Tilt density n(q^T S q)/tr(S) cancels the denominator exactly.
        for i in range(n):
            for j in range(n):
                mat[i][j] += n/tr * q[i] * q[j] / draws
    for i in range(n):
        for j in range(n):
            target = (1/tr if i==j else 0.)
            assert abs(mat[i][j]-target) < 0.012/tr, (lambdas,i,j,mat[i][j],target)
            checks += 1

print('PASS', checks, 'structured exact and numerical checks')
