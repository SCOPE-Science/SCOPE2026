"""Supplementary finite diagnostics for sharp two-mode superquadratic circle sampling.

The infinite-dimensional parameter theorem is proved analytically in RESULT.md;
finite computations here are consistency checks only.
"""
import math
import random


def predicted(s, m, terms=3000):
    assert 1 < s < 2 and m >= 2
    c = -2 * math.gamma(s + 1)**2 * math.sin(math.pi * s) / math.pi
    total = sum(math.exp(math.lgamma(l*m - s) - math.lgamma(l*m + s + 1))
                for l in range(1, terms + 1))
    # For this diagnostic only, the 3,000-term truncation is compared at 1e-6 scale.
    return c * total


def normalized_integral(s, r, n=8192):
    return sum((1 + r * math.cos(2*math.pi*j/n))**s
               for j in range(n)) / n


def relative_error(s, m, r, phase, n=8192):
    d = normalized_integral(s, r, n)
    q = sum((1 + r * math.cos(phase + 2*math.pi*j/m))**s
            for j in range(m)) / m
    return q/d - 1


def p3_cot(m):
    a = math.pi / (2*m)
    return 3*math.pi/(16*m) * (3/math.tan(a) - 1/math.tan(3*a)) - 1


def run():
    checks = 0
    rng = random.Random(614082)
    for s in (1.05, 1.20, 1.35, 1.5, 1.75, 1.95):
        for m in (2, 3, 4, 5, 6, 9, 12):
            e = predicted(s, m)
            assert e > 0
            checks += 1
            zero_phase = math.pi if m % 2 else 0.0
            actual = relative_error(s, m, 1.0, zero_phase)
            assert abs(actual - e) <= 3e-7, (s, m, actual, e)
            checks += 1
            for _ in range(75):
                r = rng.random()
                phase = rng.random()*2*math.pi
                actual = relative_error(s, m, r, phase, n=4096)
                assert abs(actual) <= e + 3e-7, (s, m, r, phase, actual, e)
                checks += 1
    for m in range(2, 41):
        a = predicted(1.5, m)
        b = p3_cot(m)
        assert abs(a - b) < 2e-7, (m, a, b)
        checks += 1
    assert abs(p3_cot(2) - (3*math.pi/8-1)) < 1e-13
    checks += 1
    # Polynomial endpoint p=4: grid 2 has a nonzero second harmonic;
    # m>=3 removes it by root-of-unity averaging.
    for m in range(2, 35):
        phase = math.pi if m % 2 else 0.0
        observed = relative_error(2, m, 1.0, phase)
        limit = 1/3 if m == 2 else 0.0
        assert abs(observed - limit) < 1e-12, (m, observed, limit)
        checks += 1
    print('SUPERQUADRATIC_CIRCLE_SAMPLING_DIAGNOSTIC_OK', checks)

if __name__ == '__main__':
    run()
