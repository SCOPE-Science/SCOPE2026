"""Finite-dimensional checks for two-atom lacunary Kaczmarz residuals.

Only finite algebra and representative phases are tested; the asymptotic
and Baire-category results require the mathematical proof.
"""
import math
import cmath
from fractions import Fraction

import numpy as np


def sample_indices(base, count):
    assert base >= 3 and base % 2 == 1
    return [(base ** j - 1) // (base - 1) for j in range(count)]


def residual_direct(base, alpha, phase, n):
    q = np.eye(2, dtype=complex)
    for k in sample_indices(base, n + 1):
        z = np.array([math.sqrt(alpha), math.sqrt(1.0-alpha)
                      * cmath.exp(2j * math.pi * ((k * phase) % 1.0))])
        proj_complement = np.eye(2) - np.outer(z, z.conjugate())
        q = proj_complement @ q
    return float(np.linalg.norm(q, 2))


def residual_product(base, alpha, phase, n):
    value = 1.0
    x = phase
    for _ in range(n):
        value *= abs(alpha + (1.0-alpha) * cmath.exp(2j * math.pi * x))
        x = (base * x) % 1.0
    return value


def algebraic_root_special(base, alpha, n):
    # All geometric gaps are odd, so a half-turn phase gives the minimum factor.
    return abs(2.0 * alpha - 1.0) ** n


def run():
    checks = 0
    for base in (3, 5, 7):
        for alpha in (0.2, 0.3, 0.5, 0.7, 0.8):
            for phase in (0.123456789, 0.317, 1.0/7, 1.0/13):
                for n in range(1, 8):
                    measured = residual_direct(base, alpha, phase, n)
                    expected = residual_product(base, alpha, phase, n)
                    assert abs(measured-expected) < 5e-11, (base, alpha, phase, n, measured, expected)
                    checks += 1
            for n in range(1, 8):
                observed = residual_product(base, alpha, 0.5, n)
                exact = algebraic_root_special(base, alpha, n)
                assert abs(observed-exact) < 2e-13
                checks += 1
        for k in (1, 2, 3):
            rational = Fraction(1, base ** k)
            # From step k onward the phase becomes zero in the circle.
            assert all((rational * base ** j).denominator == 1 for j in range(k, k + 10))
            checks += 1
    for alpha in (0.25, 0.5, 0.75):
        # Numerical asymptotic sanity check, not evidence of the universal theorem.
        phase = math.sqrt(2.0) - 1.0
        vals = []
        x = phase
        for j in range(20000):
            h = abs(alpha + (1-alpha) * cmath.exp(2j * math.pi * x))
            if h:
                vals.append(math.log(h))
            else:
                raise AssertionError('unexpected finite termination')
            x = (3*x) % 1.0
        rate = math.exp(sum(vals) / len(vals))
        target = max(alpha, 1-alpha)
        # Mixing diagnostics on this arithmetic phase are qualitative only.
        assert abs(rate-target) < 0.10, (rate, target)
        checks += 1
    print(f'LACUNARY_KACZMARZ_MATRIX_DIAGNOSTIC_OK {checks}')


if __name__ == '__main__':
    run()
