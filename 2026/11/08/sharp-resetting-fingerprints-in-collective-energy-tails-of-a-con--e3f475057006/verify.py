#!/usr/bin/env python3
"""Independent numerical checks for stationary common-reset OU collective energy.
Uses only Python's standard library. These finite checks do not prove asymptotics.
Run: python3 verify.py
"""
from math import exp, log, lgamma, gamma, pi, sqrt, erfc


def regularized_gamma_upper(a, x):
    if a <= 0 or x < 0:
        raise ValueError('a must be positive and x nonnegative')
    if x == 0:
        return 1.0
    pref = exp(a * log(x) - x - lgamma(a))
    eps = 4e-14
    if x < a + 1:
        v = 1.0 / a
        term = v
        for k in range(1, 10000):
            term *= x / (a + k)
            v += term
            if abs(term) <= abs(v) * eps:
                break
        return max(0.0, min(1.0, 1 - pref * v))
    small = 1e-290
    z = x + 1 - a
    if abs(z) < small:
        z = small
    c = 1 / small
    d = 1 / z
    h = d
    for k in range(1, 10000):
        an = -k * (k - a)
        z += 2
        d = z + an * d
        if abs(d) < small:
            d = small
        c = z + an / c
        if abs(c) < small:
            c = small
        d = 1 / d
        delta = d * c
        h *= delta
        if abs(delta - 1) < eps:
            break
    return max(0.0, min(1.0, pref * h))


def chi_upper(n, z):
    return regularized_gamma_upper(n / 2, n * z / 2)


def composite_simpson(f, a, b, intervals=8000):
    assert intervals % 2 == 0
    h = (b - a) / intervals
    total = f(a) + f(b)
    for i in range(1, intervals):
        total += (4 if i % 2 else 2) * f(a + i * h)
    return total * h / 3


def probability(n, b, t):
    # Smooth boundary-aware quadrature of the exact Beta x chi-square mixture.
    # Upper-tail saddle uses w=O(1/n); the edge uses w=O(1/sqrt(n)).
    scale = sqrt(n) if abs(t - 1) <= 0.18 else n
    w_max = min(1.0, (30 if scale != n else 120) / scale)
    u_max = sqrt(scale * w_max)
    def integrand(u):
        w = (u * u) / scale
        if w >= 1:
            return 0.0
        jacobian = 2 * b * (u ** (2 * b - 1)) / (scale ** b)
        return jacobian * chi_upper(n, t / (1 - w))
    return composite_simpson(integrand, 0, u_max, intervals=12000)


def critical_constant(b):
    return 2 ** (b - 1) * gamma((b + 1) / 2) / sqrt(pi)


def upper_tail_asymptotic(n, b, t):
    assert t > 1
    rate = (t - 1 - log(t)) / 2
    return (2 ** b * gamma(b + 1) / (sqrt(pi) * (t - 1) ** (b + 1))
            * n ** (-b - 0.5) * exp(-n * rate))


def crossover_constant(b, x):
    normal_upper = lambda z: erfc(z / 2 ** 0.5) / 2
    # s=u^2 removes the b=1/2 integrable endpoint singularity.
    return composite_simpson(lambda u: 2 * b * u ** (2 * b - 1)
                             * normal_upper((x + u * u) / sqrt(2)),
                             0, sqrt(30), intervals=18000)


def test():
    checked = 0
    for n in [2, 4, 7, 25]:
        for b in [0.5, 1, 2, 3]:
            for p in [1, 2, 3, 4]:
                # Beta(1,b) moment times normalized chi-square moment.
                m_beta = exp(lgamma(1 + p) + lgamma(1 + b) - lgamma(1 + b + p))
                m_chi = exp(p * log(2 / n) + lgamma(n / 2 + p) - lgamma(n / 2))
                ref = m_beta * m_chi
                # Independent factorial/product expression.
                alt = 1.
                for k in range(1, p + 1):
                    alt *= k / (b + k) * (n + 2 * (k - 1)) / n
                assert abs(ref / alt - 1) < 1e-12
                checked += 1
    for b in [0.5, 1, 2]:
        for n in [100, 400, 1600]:
            p = probability(n, b, 1)
            asym = critical_constant(b) * n ** (-b / 2)
            assert 0.60 < p / asym < 1.08, (b, n, p / asym)
            checked += 1
        # Convergence improves as N grows.
        ratios = [probability(n, b, 1) / (critical_constant(b) * n ** (-b/2))
                  for n in [100, 400, 1600]]
        assert abs(ratios[2] - 1) < abs(ratios[0] - 1)
        checked += 1
    for b in [0.5, 1, 2]:
        for n in [100, 400, 1600]:
            p = probability(n, b, 1.4)
            asym = upper_tail_asymptotic(n, b, 1.4)
            assert 0.35 < p / asym < 1.06, (b, n, p / asym)
            checked += 1
        ratios = [probability(n, b, 1.4) / upper_tail_asymptotic(n, b, 1.4)
                  for n in [100, 400, 1600]]
        assert abs(ratios[2] - 1) < abs(ratios[0] - 1)
        checked += 1
    for b in [0.5, 1, 2]:
        c0 = crossover_constant(b, 0)
        assert abs(c0 / critical_constant(b) - 1) < 2e-5, (b, c0)
        checked += 1
        for x in [-2, 0, 2]:
            F = crossover_constant(b, x)
            assert F > 0
            n = 1600
            p = probability(n, b, 1 + x / sqrt(n))
            assert abs(p * n ** (b / 2) / F - 1) < .12, (b, x, p, F)
            checked += 1
    # Chi-square survival identity: for N=2, tail is exactly exp(-z).
    for z in [.4, 1, 2, 4, 8]:
        assert abs(chi_upper(2, z) - exp(-z)) < 1e-12
        checked += 1
    print(f'PASS: {checked} independent finite/numerical comparisons')

if __name__ == '__main__':
    test()
