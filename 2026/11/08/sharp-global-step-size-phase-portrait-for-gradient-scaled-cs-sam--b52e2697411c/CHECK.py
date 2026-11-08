"""Standalone finite checks supporting the exact scalar CS-SAM phase-portrait proof.

Run with: python3 CHECK.py
All exact arithmetic uses Python's Fraction; sampled tests are not the proof.
"""
from fractions import Fraction as Q
from math import sqrt


def filter_gain(rho, t):
    return (1 + t + rho) / ((1 + t) ** 2 + rho * t)


def direct_step(x, rho, gamma):
    y = x + rho * x / (1 + abs(x))
    return x - gamma * y / (1 + abs(y))


def gain_derivative_numerator(rho, t):
    return -(t * t + (2 + 2 * rho) * t + 1 + 3 * rho + rho * rho)


def radial_derivative_numerator(rho, t):
    return (1 + t) ** 2 + rho

checks = 0
rhos = [Q(0), Q(1, 10), Q(1), Q(3), Q(10)]
gammas = [Q(1, 7), Q(1, 2), Q(1), Q(4, 3), Q(2), Q(10, 3), Q(7)]
samples = [Q(k, 7) for k in range(-35, 36)]
for rho in rhos:
    for gamma in gammas:
        for x in samples:
            t = abs(x)
            reduced = x * (1 - gamma * filter_gain(rho, t))
            assert direct_step(x, rho, gamma) == reduced
            checks += 1
        for t in [Q(k, 7) for k in range(0, 100)]:
            assert gain_derivative_numerator(rho, t) < 0
            assert radial_derivative_numerator(rho, t) > 0
            checks += 2

# Explicit exact rational nonzero two-cycle (rho=1, gamma=10/3, scale L1=1).
rho = Q(1)
gamma = Q(10, 3)
assert filter_gain(rho, Q(1)) == Q(3, 5)
assert direct_step(Q(1), rho, gamma) == -1
assert direct_step(Q(-1), rho, gamma) == 1
checks += 3

# Unique positive phase root and strict target-distance contraction on a grid;
# tests are illustrative only; the proof uses monotonic gain and radial gain.
for rho_f in (0.2, 1.0, 3.5):
    for multiple in (1.1, 1.7, 4, 100):
        gamma_f = multiple * 2 / (1 + rho_f)
        b = 4 + 2 * rho_f - gamma_f
        p = (-b + sqrt(b*b + 8 * (gamma_f * (1 + rho_f) - 2))) / 4
        assert p > 0 and abs(gamma_f * filter_gain(rho_f, p) - 2) < 1e-10
        for j in range(1, 200):
            t = (2 * p) * j / 200
            if abs(t-p) < 1e-13:
                continue
            tnext = t * abs(1 - gamma_f * filter_gain(rho_f, t))
            assert abs(tnext-p) < abs(t-p) + 1e-12
            checks += 1

# Borderline rate for a nonterminating trajectory from a rational value.
t = 0.08
rho_f, gamma_f = 1.0, 1.0
for _ in range(50000):
    t = t * abs(1 - gamma_f * filter_gain(rho_f, t))
assert abs(50000*t - 0.2) < 0.006, (50000*t)
checks += 1
print(f'PASS: {checks} supplementary checks; rational two-cycle and critical-rate test verified')
