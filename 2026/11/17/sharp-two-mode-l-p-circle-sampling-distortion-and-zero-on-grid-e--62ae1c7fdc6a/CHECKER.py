"""Supplementary numerical checks for a two-mode circle-sampling identity.

Run with Python 3 and the standard library only. This finite test does not
certify infinite Fourier sums or global optimality; those use the proof.
"""
import cmath
import math
import random


def exact_balanced_mean(p):
    return 2.0 ** p * math.gamma((p + 1.0) / 2.0) / (math.sqrt(math.pi) * math.gamma((p + 2.0) / 2.0))


def sampled(a, b, p, m, tau=0.0):
    return sum(abs(a + b * cmath.exp(1j * (tau + 2 * math.pi * k / m))) ** p for k in range(m)) / m


def integrated(a, b, p, samples=8192):
    return sum(abs(a + b * cmath.exp(2j * math.pi * (k + .5) / samples)) ** p for k in range(samples)) / samples


def analytic_gamma_coefficient_ratio(p, k):
    s = p / 2
    # Reflection removes Gamma evaluated at a negative noninteger argument.
    return ((-1) ** (k - 1)) * math.gamma(1 + s) ** 2 * math.sin(math.pi * s) / math.pi * math.exp(math.lgamma(k - s) - math.lgamma(k + s + 1))


def run():
    count = 0
    random.seed(36078)
    for p in (1.1, 1.5, 1.9):
        balmean = exact_balanced_mean(p)
        for m in (1, 2, 3, 4, 6, 10, 16):
            grid_under = sampled(1.0, -1.0, p, m) / balmean
            E = 1.0 - grid_under
            assert 0 < E <= 1.00000001
            assert abs(integrated(1.0, -1.0, p) - balmean) < 0.00001
            count += 2
            for _ in range(45):
                a = cmath.rect(random.uniform(0.05, 2.0), random.uniform(-math.pi, math.pi))
                b = cmath.rect(random.uniform(0.05, 2.0), random.uniform(-math.pi, math.pi))
                tau = random.uniform(-math.pi, math.pi)
                ratio = sampled(a, b, p, m, tau) / integrated(a, b, p)
                assert abs(ratio - 1) <= E + 0.00003, (p, m, E, ratio)
                count += 1
        # Check the signed Fourier coefficient formula numerically at r=1.
        for k in (1, 2, 3, 4, 5, 6):
            approx = sum((1 + math.cos(2 * math.pi * (j + .5) / 32768)) ** (p / 2)
                         * math.cos(k * 2 * math.pi * (j + .5) / 32768) for j in range(32768)) / 32768
            mean = sum((1 + math.cos(2 * math.pi * (j + .5) / 32768)) ** (p / 2)
                       for j in range(32768)) / 32768
            assert abs(approx / mean - analytic_gamma_coefficient_ratio(p, k)) < 0.000002
            count += 1
    print('TWO_MODE_CIRCLE_CHECK_OK', count, 'finite assertions')


if __name__ == '__main__':
    run()
