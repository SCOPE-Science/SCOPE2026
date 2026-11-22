#!/usr/bin/env python3
"""Exact finite-capacity stationary-mode checks for the birth-death-immigration model.

Requires only Python 3 standard library. Numerical floating-point checks below
are diagnostics for the limiting expression, not a substitute for its proof.
"""
from fractions import Fraction as F
from math import sqrt, floor, ceil


def ratio(N, a, b, n):
    """Exact stationary ratio p[n]/p[n-1], normalized by mortality."""
    return F(N - n + 1, n) * (a + b * F(n - 1, N - 1))


def boundary_at(N, a, t):
    return F(N - 1, t * (N - t)) * ((1 + a) * t + 1 - N * a)


def boundary(N, a):
    return min((boundary_at(N, a, t), t) for t in range(1, N))


def test_exact():
    diagnostics = 0
    for N in range(2, 101):
        for eta in [F(1, 10), F(1, 5), F(1, 2), F(9, 10)]:
            a = eta / N
            B, idx = boundary(N, a)
            d = 1 - N * a
            assert d > 0
            tcrit = N * sqrt(float(d)) / (sqrt(N + 1) + sqrt(float(d)))
            choices = {min(N-1,max(1,floor(tcrit))), min(N-1,max(1,ceil(tcrit)))}
            assert idx in choices or any(boundary_at(N,a,j)==B for j in choices)
            for b in [B / 2, B, B + F(1, 10000), B + 1]:
                ratios = [ratio(N, a, b, n) for n in range(1, N+1)]
                assert ratios[0] < 1
                assert (any(x > 1 for x in ratios[1:])) == (b > B)
                if N > 2:
                    diffs = [ratios[i+1]-ratios[i] for i in range(N-1)]
                    assert all(diffs[i] > diffs[i+1] or not (diffs[i] < 0 and diffs[i+1] > 0)
                               for i in range(len(diffs)-1))
                diagnostics += 1
    # At or above the immigration threshold, no strictly declining first step.
    for N in range(2, 60):
        for a in [F(1, N), F(2, N)]:
            for b in [F(1, 2), F(1), F(3)]:
                assert ratio(N, a, b, 1) >= 1
                diagnostics += 1
    # The explicit ecological example.
    N, a, b = 10, F(1, 50), F(8, 5)
    B, index = boundary(N, a)
    assert B == F(639, 400) and index == 2
    ratios = [ratio(N, a, b, n) for n in range(1, N + 1)]
    assert ratios[0] < 1 and ratios[1] < 1 < ratios[2] and ratios[3] < 1
    weights = [F(1)]
    for r in ratios:
        weights.append(weights[-1] * r)
    # Zero and occupancy 3 are distinct strict local peaks.
    assert weights[0] > weights[1]
    assert weights[3] > weights[2] and weights[3] > weights[4]
    diagnostics += 7
    return diagnostics


def test_continuum():
    diagnostics = 0
    for N in [20, 50, 100, 300, 1000, 3000, 10000]:
        for eta in [0.0, 0.2, 0.6, 0.9]:
            a, delta = eta / N, 1-eta
            t = N * sqrt(delta) / (sqrt(N + 1) + sqrt(delta))
            Bc = (N-1)/(N*N)*(sqrt(N+1)+sqrt(delta))**2
            nearest = sorted({max(1,min(N-1,floor(t))), max(1,min(N-1,ceil(t)))})
            val = min(float(boundary_at(N,F(str(a)),j)) for j in nearest)
            v2 = Bc * (1+min((j-t)**2/(j*(N-j)) for j in nearest))
            assert abs(val-v2) < 1e-10
            approx = 1+2*sqrt(delta/N)+delta/N
            assert abs(val-approx) < 6.0 * N**(-1.5) + 1e-10
            diagnostics += 2
    return diagnostics


if __name__ == '__main__':
    print('exact_checks:', test_exact())
    print('continuum_diagnostics:', test_continuum())
    print('All checks passed (finite calculations do not prove the general theorem).')
