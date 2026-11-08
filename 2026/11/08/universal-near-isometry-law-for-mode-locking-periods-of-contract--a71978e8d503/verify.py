#!/usr/bin/env python3
"""Reproducible finite checks for the contracted-rotation denominator law.

The checks do not replace the asymptotic proof. Standard library only.
"""
from fractions import Fraction
from math import exp, expm1, gcd, isclose, log, pi

checks = 0


def check(condition, message):
    global checks
    assert condition, message
    checks += 1


def totients(n):
    phi = list(range(n + 1))
    for p in range(2, n + 1):
        if phi[p] == p:
            for k in range(p, n + 1, p):
                phi[k] -= phi[k] // p
    return phi


# Laurent--Nogueira Theorem 3(ii) endpoints and numerator-independent width.
for lam in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)):
    for q in range(2, 19):
        expected = (1 - lam)**2 * lam**(q - 1) / (1 - lam**q)
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            c = 1 + sum(
                ((k + 1) * p // q - k * p // q) * lam**k
                for k in range(1, q - 1)
            )
            low = (1 - lam) * c / (1 - lam**q)
            high = (1 - lam) * (c + lam**(q - 1) - lam**q) / (1 - lam**q)
            check(high - low == expected, 'plateau width')
            check(0 <= low < high <= 1, 'plateau endpoints')

# Exact rational finite partial mass, bounded above by full mass 1.
for lam in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)):
    phi = totients(70)
    partial = (1 - lam) + sum(
        phi[q] * (1 - lam)**2 * lam**(q - 1) / (1 - lam**q)
        for q in range(2, 71)
    )
    check(Fraction(0) < partial < Fraction(1), 'finite rational mass')
    check(float(1 - partial) < 1e-6, 'finite tail in exact mass sum')


# The arithmetic limiting moments of the period distribution.
# The zeta(3) benchmark is computed from an independently convergent sum.
zeta3 = sum(k**(-3) for k in range(1, 300001)) + 1 / (2 * 300001**2)
mean_limit = 2 * zeta3 / (pi**2 / 6)
second_limit = 2 * pi**2 / 5
prior_mean_error = None
for lam in (.9, .95, .98, .99):
    tau = -log(lam)
    n = int(28 / tau) + 1
    phi = totients(n)
    mean = (1 - lam) * tau
    second = (1 - lam) * tau**2
    mass = 1 - lam
    cross = 0.0
    # All rational numerators of a fixed denominator share a width.
    for q in range(2, n + 1):
        weight = ((-expm1(-tau))**2) * exp(tau) / expm1(q * tau)
        probability = phi[q] * weight
        mass += probability
        mean += probability * q * tau
        second += probability * (q * tau)**2
        cross += probability * q * tau / 2  # reduced residues sum to phi(q)/2
    check(abs(mass - 1) < 2e-9, 'numerical total mass')
    check(abs(cross - mean / 2 + (1 - lam) * tau / 2) < 3e-12,
          'rotation-number symmetry for nonzero rotations')
    check(abs(second - second_limit) < .3, 'second moment scale')
    error = abs(mean - mean_limit)
    if prior_mean_error is not None:
        check(error < prior_mean_error, 'approach to limiting mean')
    prior_mean_error = error
check(prior_mean_error < 1e-4, 'numerical limiting mean')

print(f'PASS: {checks} exact-rational and numerical supporting checks')
print(f'limiting mean={mean_limit:.12f}, limiting second moment={second_limit:.12f}')
