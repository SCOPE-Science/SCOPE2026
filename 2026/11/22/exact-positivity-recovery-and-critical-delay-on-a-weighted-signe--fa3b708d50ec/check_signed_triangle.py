#!/usr/bin/env python3
"""Reproducible finite checks for the signed-triangle heat-kernel formulas.

No third-party packages are required.  Numerical tests are not a proof of
claims quantified over all positive edge weights and all real times.
"""
from fractions import Fraction as F
import math


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]


def lap(a, b, q):
    return [[a - q, q, -a], [q, b - q, -b], [-a, -b, a + b]]


def exact_identity(a, b, q):
    L = lap(a, b, q)
    L2 = mm(L, L)
    S, R = a + b - q, a * b - q * (a + b)
    for i in range(3):
        for j in range(3):
            correction = 3 * R * ((1 if i == j else 0) - F(1, 3))
            assert L2[i][j] - 2 * S * L[i][j] + correction == 0


def expm_minus(t, L):
    # Scaling / squaring with the Taylor series, independent of the
    # spectral-projector expression used for the claimed (1,2) entry.
    A = [[-t * L[i][j] for j in range(3)] for i in range(3)]
    size = max(sum(abs(v) for v in row) for row in A)
    s = max(0, math.ceil(math.log2(size / 0.25))) if size else 0
    A = [[v / (2 ** s) for v in row] for row in A]
    I = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]
    out = [row[:] for row in I]
    term = [row[:] for row in I]
    for k in range(1, 50):
        term = mm(term, A)
        term = [[v / k for v in row] for row in term]
        out = [[out[i][j] + term[i][j] for j in range(3)] for i in range(3)]
    for _ in range(s):
        out = mm(out, out)
    return out


def spectral(a, b, q):
    S = a + b - q
    R = a * b - q * (a + b)
    d = math.sqrt(S * S - 3 * R)
    lm, lp = S - d, S + d
    gap = lp - lm
    A = (q + lp / 3) / gap
    B = (q + lm / 3) / gap
    return lm, lp, gap, A, B


def k12(t, lm, lp, A, B):
    return 1.0 / 3 - A * math.exp(-lm * t) + B * math.exp(-lp * t)


def check_one(a, b, frac):
    q = a * b / (a + b) * frac
    lm, lp, gap, A, B = spectral(a, b, q)
    assert 0 < lm < lp and A > B > 0
    peak = math.log(lp * B / (lm * A)) / gap
    assert peak > 0
    lo, hi = peak, max(peak * 2, 2 / lm)
    while k12(hi, lm, lp, A, B) <= 0:
        hi *= 2
    for _ in range(90):
        mid = (lo + hi) / 2
        if k12(mid, lm, lp, A, B) < 0:
            lo = mid
        else:
            hi = mid
    T = (lo + hi) / 2
    L = lap(a, b, q)
    for t in [peak / 3, peak, (peak + T) / 2, T * 1.2, 2 * T]:
        E = expm_minus(t, L)
        assert abs(E[0][1] - k12(t, lm, lp, A, B)) < 3e-8
        assert E[0][2] > 0 and E[1][2] > 0
        assert all(E[i][i] > 0 for i in range(3))
        assert max(abs(sum(row) - 1) for row in E) < 2e-8
        induced = max(sum(abs(z) for z in row) for row in E)
        predicted = 1 - 2 * min(k12(t, lm, lp, A, B), 0)
        assert abs(induced - predicted) < 4e-8


for x in [(F(1), F(1), F(1, 4)), (F(2), F(3), F(1, 5)),
          (F(7), F(1, 2), F(1, 10)), (F(1), F(1), F(1, 2))]:
    exact_identity(*x)

for a, b in [(1.0, 1.0), (2.0, 3.0), (0.4, 4.0), (4.0, 0.4)]:
    for frac in (0.02, 0.2, 0.6, 0.95):
        check_one(a, b, frac)

# The boundary law is checked at decreasing distance to the critical edge.
a = b = 1.0
qc = 0.5
limit = math.log(1.5) / 2
for eps in (1e-2, 1e-3, 1e-4):
    lm, lp, gap, A, B = spectral(a, b, qc - eps)
    peak = math.log(lp * B / (lm * A)) / gap
    T = math.log(3 * A) / lm  # fast-mode correction is exponentially small here
    assert abs(eps * T - limit) < 1e-6
    assert abs(1 - 2 * k12(peak, lm, lp, A, B) - 4 / 3) < 0.04

print('PASS: four exact rational identities, 16 parameter configurations, '
      'five time samples each, and three boundary probes')
