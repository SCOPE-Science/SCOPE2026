#!/usr/bin/env python3
"""Independent finite sanity checks for the sharp Tsallis probability-map norm.
These tests do not replace the analytic argument in RESULT.md.
"""
import itertools
import math
import random

SEED = 20261115
rng = random.Random(SEED)
checks = 0


def predicted(n, alpha):
    if n == 1:
        return 0.0
    m, ell = n // 2, (n + 1) // 2
    gamma = (alpha - 1) / (3 - alpha)
    return 4 * (m * ell) ** (alpha - 1) / (
        m ** gamma + ell ** gamma) ** (3 - alpha)


def jacobian(p, alpha):
    s = [(v ** (2 - alpha) if v > 0 else 0.0)
         if alpha < 2 else (1.0 if v > 0 else 0.0) for v in p]
    total = sum(s)
    return [[(s[i] if i == j else 0.0) - s[i] * s[j] / total
             for j in range(len(p))] for i in range(len(p))]


def brute_norm(J):
    n = len(J)
    ans = 0.0
    for eps in itertools.product((-1.0, 1.0), repeat=n):
        out = [sum(row[j] * eps[j] for j in range(n)) for row in J]
        ans = max(ans, sum(abs(v) for v in out))
    return ans


def cut_norm(p, alpha):
    n = len(p)
    s = [(v ** (2 - alpha) if v > 0 else 0.0)
         if alpha < 2 else (1.0 if v > 0 else 0.0) for v in p]
    total = sum(s)
    out = 0.0
    for mask in range(1, 2 ** n - 1):
        a = sum(s[j] for j in range(n) if mask & (1 << j))
        out = max(out, 4 * a * (total - a) / total)
    return out


def entmax(z, alpha):
    # Original KKT positive-part formula; independent of Jacobian evaluation.
    power = 1.0 / (alpha - 1)
    lo = min((alpha - 1) * v for v in z) - 2.0
    hi = max((alpha - 1) * v for v in z)
    for _ in range(160):
        tau = (lo + hi) / 2
        mass = sum(max((alpha - 1) * v - tau, 0.0) ** power for v in z)
        if mass > 1:
            lo = tau
        else:
            hi = tau
    tau = (lo + hi) / 2
    p = [max((alpha - 1) * v - tau, 0.0) ** power for v in z]
    return [v / sum(p) for v in p]


for n in range(2, 10):
    for alpha in (1.05, 1.2, 1.5, 1.85, 2.0):
        m, ell = n // 2, (n + 1) // 2
        gamma = (alpha - 1) / (3 - alpha)
        q = ell ** gamma / (m ** gamma + ell ** gamma)
        witness = [q / m] * m + [(1 - q) / ell] * ell
        exact = predicted(n, alpha)
        assert math.isclose(brute_norm(jacobian(witness, alpha)), exact,
                            rel_tol=3e-12, abs_tol=3e-12)
        checks += 1
        for _ in range(110):
            vals = [rng.random() ** 3 + 1e-7 for j in range(n)]
            p = [v / sum(vals) for v in vals]
            a = brute_norm(jacobian(p, alpha))
            b = cut_norm(p, alpha)
            assert abs(a - b) < 3e-10, (n, alpha, a, b)
            assert a <= exact + 3e-10, (n, alpha, a, exact)
            checks += 2

for n in range(2, 7):
    for alpha in (1.2, 1.5, 1.9, 2.0):
        for _ in range(110):
            z = [rng.uniform(-1, 1) for _ in range(n)]
            dz = [rng.uniform(-1, 1) for _ in range(n)]
            h = 1e-5 / max(abs(v) for v in dz)
            p1, p2 = entmax(z, alpha), entmax([z[i] + h * dz[i] for i in range(n)], alpha)
            ratio = sum(abs(a-b) for a,b in zip(p1,p2)) / (h * max(abs(v) for v in dz))
            assert ratio <= predicted(n, alpha) + 5e-7, (n, alpha, ratio)
            checks += 1
print('PASS:', checks, 'deterministic supplementary assertions; no universal proof claimed')
