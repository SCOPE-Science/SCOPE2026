"""Exact rational Poisson-equation tests and independent diffusive-scale sums.

Run: python3 verify_green_limit.py
All dependencies are in the Python standard library.
"""
from fractions import Fraction as F
from math import cos, expm1, pi, sin


def exact_poisson(n):
    N = n - 1
    stationary_endpoint = F(2, N)
    # Mean-zero solution of -Qg=1_{endpoint}-2/N on reflecting path.
    g0 = F((N - 1) * (N - 2), 12 * N)
    g = [g0 - F(k, 2) + F(k * (k + 1), 2 * N) for k in range(N)]
    assert sum(g) == 0
    assert g[0] == g[-1]
    for k in range(N):
        terms = (2 * (g[k - 1] - g[k]) if k else 0) + (2 * (g[k + 1] - g[k]) if k < N - 1 else 0)
        desired = (F(1) if k in (0, N - 1) else F(0)) - stationary_endpoint
        assert -terms == desired, (n, k)
    # Exact Green-Kubo / marked-generator second cumulant.
    energy = (g[0] + g[-1]) / N
    mu = F(4 * (n - 2), N)
    fano = F(1) + 8 * energy / mu
    assert fano == F(1) + F(n - 3, 3 * (n - 1))
    # Independent published all-density long-time expression (Appert-Rolland et al. 2008).
    sigma = F(4 * (n - 2), n * n)
    second_rate = n * n * sigma * (n * n * sigma + 4 * n - 4) / (6 * (n - 1) ** 2)
    assert second_rate / mu == fano
    return fano


def finite_fano(n, x):
    N = n - 1
    t = x * N**2
    mu = 4 * (n - 2) / N
    extra = 0.0
    for ell in range(1, (N - 1) // 2 + 1):
        lam = 8 * sin(pi * ell / N) ** 2
        z = lam * t
        extra += 64 * cos(pi * ell / N) ** 2 / N**2 * (t / lam + expm1(-z) / lam**2)
    return 1 + extra / (mu * t)


def scaling(x, truncation=1000):
    return 4/3 - sum(-expm1(-8 * pi**2 * ell**2 * x) / ell**4 for ell in range(1, truncation + 1)) / (4 * pi**4 * x)


def main():
    for n in range(3, 251):
        exact_poisson(n)
    for x in (0.005, 0.02, 0.2, 2.0):
        a = scaling(x)
        assert 1 < a < 4 / 3
        vals = [finite_fano(n, x) for n in (101, 401, 1601)]
        assert abs(vals[-1] - a) < 0.002, (x, vals[-1], a)
        assert all(v < a for v in vals), (x, vals, a)
    print('PASS: 248 exact rational Poisson equations and 12 diffusive-scale comparisons')


if __name__ == '__main__':
    main()
