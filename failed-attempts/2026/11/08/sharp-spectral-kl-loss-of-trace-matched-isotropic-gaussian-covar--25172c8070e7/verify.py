"""Reproduce finite checks for a sharp trace-matched Gaussian KL bound.

Uses only the Python standard library. Finite checks support, but do not replace,
the mathematical proof of the universal inequality.
"""
import itertools
import math
import random


def kl_from_eigenvalues(lambdas):
    n = len(lambdas)
    avg = sum(lambdas) / n
    return 0.5 * (avg * sum(1.0 / v for v in lambdas) - n
                  - n * math.log(avg) + sum(math.log(v) for v in lambdas))


def branch(n, ratio, j):
    p = j / n
    delta = ratio - 1.0
    return 0.5 * n * (delta**2 / ratio * p * (1 - p)
                      - math.log1p(delta * p) + p * math.log(ratio))


def cap(n, ratio):
    if ratio == 1:
        return 0.0
    return max(branch(n, ratio, j) for j in range(1, n))


def derivative(lambdas, i):
    x = lambdas[i]
    others = lambdas[:i] + lambdas[i + 1:]
    c = sum(others)
    h = sum(1.0 / v for v in others)
    n = len(lambdas)
    return h / n - c / (n * x * x) - n / (x + c) + 1 / x


def run():
    rng = random.Random(260910080)
    checks = 0
    for n in range(2, 11):
        for ratio in (1.001, 1.03, 1.25, 2.0, 10.0, 50.0, 200.0):
            bound = cap(n, ratio)
            for j in range(n + 1):
                vals = [ratio] * j + [1.0] * (n - j)
                assert abs(kl_from_eigenvalues(vals) - (branch(n, ratio, j) if 0 < j < n else 0.0)) < 2e-11 * max(1.0, bound)
                checks += 1
            for _ in range(120):
                vals = [math.exp(rng.uniform(0.0, math.log(ratio))) for _ in range(n)]
                got = kl_from_eigenvalues(vals)
                assert -3e-12 <= got <= bound + 3e-10 * max(1.0, bound), (n, ratio, got, bound)
                checks += 1
            for _ in range(12):
                vals = [rng.uniform(1.0, ratio) for _ in range(n)]
                i = rng.randrange(n)
                eps = 1e-5 * vals[i]
                hi = vals.copy(); lo = vals.copy()
                hi[i] += eps; lo[i] -= eps
                numeric = (kl_from_eigenvalues(hi) - kl_from_eigenvalues(lo)) / (2 * eps)
                analytic = 0.5 * derivative(vals, i)
                assert abs(numeric - analytic) < 1e-6
                checks += 1
    # Fixed numerical example and asymptotic coefficients.
    assert abs(cap(4, 10.0) - 2.943088908517195) < 1e-12
    checks += 1
    for n in (2, 3, 4, 5, 7, 10):
        small_coefficient = (n*n // 4) / (4*n)
        h = 1e-4
        assert abs(cap(n, 1+h)/h**2 - small_coefficient) < 3e-4
        large_coefficient = (n*n // 4) / (2*n)
        assert abs(cap(n, 1e7)/1e7 - large_coefficient) < 3e-5
        checks += 2
    print(f"PASS: {checks} deterministic boundary, random interior, differential, and asymptotic checks")


if __name__ == '__main__':
    run()
