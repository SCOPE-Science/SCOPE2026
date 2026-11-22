#!/usr/bin/env python3
"""Finite, exact-arithmetic checks supporting the two-tail stick theorem.

This script verifies finite geometric certificates and algebraic identities.
It does not establish the asymptotic theorem, which is proved analytically.
"""
from fractions import Fraction
from math import log, factorial

Q = Fraction(13, 8)
H = Fraction(1, 1000)
assert (1 + H) * (1 + Q) < Q * Q
assert 1 + H < Q


def fib(n):
    assert n >= 1
    a, b = 1, 1
    if n <= 2:
        return 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


def rectangle(n, m):
    # The first m intervals are below 1, the rest are above 1.
    return [(Q ** (i - m - 1), (1 + H) * Q ** (i - m - 1))
            for i in range(1, n + 1)]


def validate(n, m):
    intervals = rectangle(n, m)
    assert sum(hi < 1 for lo, hi in intervals) == m
    assert sum(lo >= 1 for lo, hi in intervals) == n - m
    for i, (lo, hi) in enumerate(intervals):
        assert lo < hi
        if i:
            assert intervals[i - 1][1] < lo
        if i >= 2:
            assert intervals[i - 2][1] + intervals[i - 1][1] < lo
    # Pairwise Fibonacci domination of every admissible ordered choice.
    for i in range(n):
        for j in range(i + 1, n):
            assert intervals[j][0] >= fib(j - i + 1) * intervals[i][1] \
                if j - i >= 2 else intervals[j][0] >= intervals[i][1]
    return 1 + sum(i >= 2 for i in range(n))


def quadratic_identity(alpha, beta, n, m):
    # Difference from the optimizing fraction of n is a perfect square.
    lhs = beta * m*m + alpha * (n-m)*(n-m)
    rhs = (alpha*beta*Fraction(n*n, 1) / (alpha + beta)
           + (alpha + beta)*(Fraction(m, 1) - alpha*n/(alpha+beta))**2)
    assert lhs == rhs


checks = 0
for n in range(3, 38):
    for m in range(n + 1):
        checks += validate(n, m)
        for a, b in [(Fraction(1), Fraction(1)), (Fraction(3, 2), Fraction(5, 3)),
                     (Fraction(2), Fraction(1))]:
            quadratic_identity(a, b, n, m)
            checks += 1

# Explicit double-Pareto (asymmetric Laplace log-density) rectangle mass.
def log_interval_mass(lo, hi, alpha, beta):
    k = alpha*beta/(alpha+beta)
    if hi <= 1:
        v = k * (hi**beta - lo**beta)/beta
    elif lo >= 1:
        v = k * (lo**(-alpha) - hi**(-alpha))/alpha
    else:
        raise ValueError('An interval straddled the pivot')
    assert 0 < v < 1
    return log(float(v))

alpha, beta = Fraction(2), Fraction(1)
theta = float(alpha/(alpha+beta))
for n in (24, 40, 75, 120):
    m = round(n*theta)
    lower_log = log(factorial(n)) + sum(log_interval_mass(a, b, alpha, beta)
                                           for a, b in rectangle(n, m))
    theoretical = -float(alpha*beta/(alpha+beta))*log((1+5**0.5)/2)/2
    geometric_q = -float(alpha*beta/(alpha+beta))*log(float(Q))/2
    print(f'n={n} m={m}  log(rectangle)/n^2={lower_log/(n*n):.8f}  '
          f'geometric-q target={geometric_q:.8f} true exponent={theoretical:.8f}')
    assert lower_log/(n*n) < 0
    checks += 1
print(f'PASS: {checks} exact finite assertions and {4} double-Pareto lower-event calculations')
