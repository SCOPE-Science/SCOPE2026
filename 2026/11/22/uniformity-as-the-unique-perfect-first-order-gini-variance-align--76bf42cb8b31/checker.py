#!/usr/bin/env python3
"""Exact rational checks for the stated U-statistic/Watson identities.

No external dependencies. Run: python3 checker.py
These finite checks supplement, but do not establish, the general proofs.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import pi, cos

checks = 0

def check(cond, label):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(label)


def abs_moment(power):
    return F(2, (power + 1) * (power + 2))

# Exact shared-index and repeated-index U-statistic kernel moments.
mu_a, mu_b = abs_moment(1), abs_moment(2)
check(mu_a == F(1, 3), 'Gini mean')
check(mu_b == F(1, 6), 'squared-difference mean')
var_a = abs_moment(2) - mu_a**2
var_b = abs_moment(4) - mu_b**2
cov_ab = abs_moment(3) - mu_a * mu_b
check((var_a, var_b, cov_ab) == (F(1, 18), F(7, 180), F(2, 45)), 'same pair')

# E[|x-Y|]=x^2-x+1/2; E[(x-Y)^2]=x^2-x+1/3.
# Their centered projections coincide: x^2-x+1/6.
projection_square = (F(1, 5) - F(2, 4) + F(4, 9)
                     - F(2, 2) / 6 + F(1, 36))
# Direct integration of (x^2-x+1/6)^2.
check(projection_square == F(1, 180), 'first projection variance')

for n in range(2, 121):
    denom = n * (n - 1)
    expected_va = F(n + 3, 45 * denom)
    expected_vb = F(2 * n + 3, 90 * denom)
    expected_c = F(n + 2, 45 * denom)
    va = (2 * var_a + 4 * (n - 2) * projection_square) / denom
    vb = (2 * var_b + 4 * (n - 2) * projection_square) / denom
    cab = (2 * cov_ab + 4 * (n - 2) * projection_square) / denom
    check((va, vb, cab) == (expected_va, expected_vb, expected_c), f'U-moments n={n}')
    check(va + vb - 2 * cab == F(1, 90 * denom), f'contrast n={n}')
    check(2*(n+2)**2 == (n+3)*(2*n+3) - (n+1), f'rho^2 n={n}')


def sample_quantities(samples):
    n = len(samples)
    pairs = list(combinations(samples, 2))
    g = sum(abs(x - y) for x, y in pairs) / len(pairs)
    b = sum((x - y) ** 2 for x, y in pairs) / len(pairs)
    return g, b


def watson(samples):
    n = len(samples)
    q = sorted(samples)
    avg = sum(q) / n
    return (sum((x - F(2*i-1, 2*n))**2 for i, x in enumerate(q, 1))
            + F(1, 12*n) - n*(avg-F(1,2))**2)


def bernoulli2(z):
    return z*z-z+F(1, 6)

for n in range(2, 8):
    for values in product((F(0),F(1,5),F(1,2),F(4,5),F(1)), repeat=n):
        if n >= 6 and (sum(i for i, a in enumerate(values) if a == F(1,5)) % 3):
            continue
        if n == 7 and values[0] not in (F(0),F(1)):
            continue
        g, b = sample_quantities(values)
        w = watson(values)
        check((n-1)*(g-b-F(1,6)) == F(1,6)-2*w, f'Watson n={n} values={values}')
        check(w == sum(bernoulli2(abs(x-y)) for x in values for y in values)/F(2*n), 'kernel form')

for m in (40, 100, 1000, 4000):
    for t in (0.01, 0.05, 0.23, 0.5, 0.73):
        partial = sum(cos(2*pi*k*t)/(pi*pi*k*k) for k in range(1,m+1))
        target = t*t-t+1/6
        check(abs(partial-target) <= 2/(pi*pi*m)+1e-12, 'Fourier remainder')

print(f'PASS: {checks} deterministic exact and Fourier checks')
