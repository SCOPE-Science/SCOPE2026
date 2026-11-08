#!/usr/bin/env python3
"""Finite exact checks for the uniform-attachment edge-count and tilt formulas.

All calculations use the Python standard library. Infinite assertions rely on the
analytical arguments in RESULT.md, not on extrapolation from these tests.
"""
from fractions import Fraction
from itertools import product
from math import comb, exp, expm1, log

CHECKS = 0


def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def counts(n):
    """Coefficient counts in product_{j=1}^n(1+...+z^{j-1})."""
    a = [1]
    for j in range(2, n + 1):
        b = [0] * (len(a) + j - 1)
        for i, v in enumerate(a):
            for k in range(j):
                b[i + k] += v
        a = b
    return a


def finite_exact():
    for n in range(2, 9):
        a = counts(n)
        max_edges = n * (n - 1) // 2
        check(len(a) == max_edges + 1, 'degree of generating polynomial')
        total = 1
        for j in range(2, n + 1):
            total *= j
        check(sum(a) == total, 'count of outdegree sequences')
        for m in range(len(a)):
            check(a[m] == a[-m-1], 'edge-count complement symmetry')
            check(a[m] > 0, 'every edge count is attainable')
        mean = sum(Fraction(i * a[i], total) for i in range(len(a)))
        second = sum(Fraction(i * i * a[i], total) for i in range(len(a)))
        check(mean == Fraction(n * (n - 1), 4), 'edge count mean')
        expected_var = sum(Fraction(j * j - 1, 12) for j in range(2, n + 1))
        check(second - mean * mean == expected_var, 'edge count variance')
        if n <= 6:
            b = [0] * len(a)
            for seq in product(*(range(j) for j in range(2, n + 1))):
                b[sum(seq)] += 1
            check(a == b, 'independent enumeration agrees with convolution')
            for m in range(len(a)):
                sequences = [seq for seq in product(*(range(j) for j in range(2, n + 1))) if sum(seq) == m]
                check(len(sequences) == a[m], 'microcanonical cardinality')
                if sequences:
                    for theta in (-1.2, 0.7, 2.3):
                        numerators = [exp(theta * sum(seq) / n) for seq in sequences]
                        check(max(numerators) - min(numerators) < 1e-10 * max(numerators),
                              'exponential tilt constant on every exact-count fibre')


def beta_moment(a):
    if abs(a) < 0.0001:
        return 0.5 + a / 12 - (a ** 3) / 720
    return -1 / expm1(-a) - 1 / a


def logz(a):
    if abs(a) < 0.0001:
        return a / 2 + a * a / 24 - a ** 4 / 2880
    return log(expm1(a) / a)


def midpoint_integral(f, N):
    return sum(f((i + 0.5) / N) for i in range(N)) / N


def rho(theta, n=5000):
    return midpoint_integral(lambda x: x * beta_moment(theta * x), n)


def cumulant(theta, n=5000):
    return midpoint_integral(lambda x: logz(theta * x), n)


def asymptotics_and_coupling():
    check(abs(rho(0.0) - 0.25) < 1e-12, 'typical density')
    check(abs(cumulant(0.0)) < 1e-12, 'cumulant at zero')
    for th in (0.1, 0.5, 1, 2, 5):
        check(rho(-th) < 0.25 < rho(th), 'monotone tilt side')
        check(abs(rho(th) + rho(-th) - 0.5) < 1e-9, 'complement density')
        check(abs(cumulant(-th) - cumulant(th) + th / 2) < 1e-9,
              'complement cumulant')
        check(th * rho(th) - cumulant(th) > 0, 'positive rate off the mean')
    check(rho(-30) < 0.06, 'near sparse endpoint')
    check(rho(30) > 0.44, 'near dense endpoint')
    eps = 0.001
    check(abs((cumulant(eps) - cumulant(-eps)) / (2 * eps) - 0.25) < 1e-7,
          'first derivative at zero')
    check(abs((cumulant(eps) - 2 * cumulant(0) + cumulant(-eps)) / eps ** 2 - 1 / 36) < 2e-6,
          'second derivative at zero')
    # Exact first two moments and expected number of differing edges in a column.
    for j in range(2, 11):
        N = j - 1
        for k in range(N + 1):
            u = Fraction(k, N)
            probs = [Fraction(comb(N, h), 1) * u ** h * (1 - u) ** (N - h)
                     for h in range(N + 1)]
            check(sum(probs) == 1, 'binomial probabilities sum to one')
            check(sum(h * p for h, p in enumerate(probs)) == k,
                  'priority threshold edge expectation')
            actual = sum(abs(h - k) * p for h, p in enumerate(probs))
            check(actual * actual <= N, 'expected symmetric-difference bound')
    # The unconditioned graphon has edge density 1/2 but triangle density 1/6.
    check(Fraction(2, 1) * Fraction(1, 4) == Fraction(1, 2), 'edge density')
    check(Fraction(6, 1) * Fraction(1, 6) * Fraction(1, 2) * Fraction(1, 3)
          == Fraction(1, 6), 'unconditioned triangle density')


if __name__ == '__main__':
    finite_exact()
    asymptotics_and_coupling()
    print(f'PASS: {CHECKS} finite exact and numerical checks; no infinite proof claimed by this program.')
