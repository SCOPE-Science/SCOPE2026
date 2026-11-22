"""Reproducible finite checks for the even-normal cone-volume theorem.

The infinite-period theorem is proved analytically; these tests are not a proof.
Only NumPy and Python's standard library are required.
"""
from fractions import Fraction
import math
import numpy as np

TESTS = 0


def checked(condition, message):
    global TESTS
    assert condition, message
    TESTS += 1


# The four-normal exceptional family is verified in exact rational arithmetic.
for t in (Fraction(1, 7), Fraction(2, 5), Fraction(3, 2), Fraction(17, 3)):
    x = [t, 1 / t, t, 1 / t]
    for j in range(4):
        checked(x[(j - 1) % 4] + x[(j + 1) % 4] == 2 / x[j],
                'Four-period recurrence')
for s in (Fraction(1, 7), Fraction(2, 5), Fraction(4, 5)):
    for t in (Fraction(1, 6), Fraction(3, 7), Fraction(9, 10)):
        # Q half-widths (s,t), R half-widths (1-s,1-t).
        # Every Q cone-area atom is s*t, every R atom (1-s)*(1-t).
        checked(s * t > 0 and (1 - s) * (1 - t) > 0,
                'Positive proportional square cone-volume atoms')


# The Fourier cotangent identity used for the analytic proof is checked
# independently at high precision for a wide collection of even periods.
for n in range(6, 102, 2):
    angle = math.pi / n
    theta = 2 * angle
    a = 2 * math.cos(theta)
    kappa = 2 - a
    delta = lambda j: 1 / math.tan(j * angle) - 1 / math.tan((j + 1) * angle)
    for j in range(2, n - 1):
        mu = 2 * math.cos(j * theta) - a
        lhs = kappa / (-mu)
        rhs = math.tan(angle) * (delta(j - 1) + delta(j)) / 2
        checked(math.isclose(lhs, rhs, rel_tol=3e-10, abs_tol=3e-10),
                f'Cotangent identity at n={n}, j={j}: {lhs} != {rhs}')


# Positive reciprocal weights with vanishing first Fourier moment.
# Evaluate the weighted Bessel operator norm: it must be strictly < 1.
for n in (6, 8, 10, 12, 16, 24, 40):
    theta = 2 * math.pi / n
    j = np.arange(n)
    kappa = 2 - 2 * math.cos(theta)
    mu = np.array([2 * math.cos(k * theta) - 2 * math.cos(theta)
                   for k in range(2, n - 1)])
    for a2, b2, a3 in ((0., 0., 0.), (.3, -.21, .04),
                       (-.31, .17, -.08)):
        w = (1 + a2 * np.cos(2 * theta * j)
             + b2 * np.sin(2 * theta * j) + a3 * np.cos(3 * theta * j))
        checked(bool((w > 0).all()), 'Strict positivity of weights')
        checked(abs(np.dot(w, np.exp(1j * theta * j))) < 1e-10,
                'First reciprocal Fourier moment')
        e = np.exp(1j * theta * np.outer(j, np.arange(2, n - 1)))
        cols = np.sqrt(w / w.sum())[:, None] * e
        op = (cols * (kappa / (-mu))[None, :]) @ cols.conj().T
        eig = np.linalg.eigvalsh(op)[-1]
        checked(float(eig) < 1 - 1e-8,
                f'Expected strict Bessel norm at n={n}, got {eig}')

print(f'PASS: {TESTS} finite exact-rational/numerical assertions. The theorem uses an independent analytic proof.')
