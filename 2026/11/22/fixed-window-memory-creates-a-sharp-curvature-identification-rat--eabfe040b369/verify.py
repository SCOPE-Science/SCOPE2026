#!/usr/bin/env python3
"""Independent finite checks for fixed-window residual-feedback identities.

No experiment here claims to verify an all-window or all-iteration theorem.
"""
import math
from fractions import Fraction
import numpy as np


def recurrence(a, ell, count):
    q = [1.0 - a]  # alpha_1 = 1, q_1 = 1 - a
    for k in range(1, count):
        window = q[max(0, k - ell):k]
        g = math.exp(sum(math.log(t) for t in window) / len(window))
        q.append(1 - a - a * g)
    return q


def radius(a, ell):
    # Characteristic polynomial of the explicitly derived feedback companion.
    coeff = [1.0] + [a / ell] * ell
    return max(abs(z) for z in np.roots(coeff))


def main():
    for a in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        qstar = (1 - a) / (1 + a)
        assert qstar * (1 + a) == 1 - a
        assert a * a == Fraction(a.numerator**2, a.denominator**2)
        # For ell=2, modulus-squared equals a/2 exactly by Vieta.
        assert Fraction(a, 2) > 0 and a*a/Fraction(4) - 2*a < 0
        r1 = float(a)
        r2 = math.sqrt(float(a) / 2)
        if a < Fraction(1, 2):
            assert r2 > r1
        elif a > Fraction(1, 2):
            assert r2 < r1
        else:
            assert abs(r2-r1) < 1e-14

    for a in (0.1, 0.25, 0.5, 0.75, 0.95):
        for ell in (1, 2, 3, 5, 10, 20, 50):
            root_radius = radius(a, ell)
            lower = (a / ell) ** (1 / ell)
            upper = a ** (1 / ell)
            assert lower - 1e-9 <= root_radius <= upper + 1e-9, (a, ell)
            if ell == 1:
                assert abs(root_radius - a) < 1e-10
            if ell == 2:
                assert abs(root_radius - math.sqrt(a / 2)) < 1e-10
            q = recurrence(a, ell, 3000)
            assert min(q) >= (1-a)**2 - 1e-12, (a, ell)
            assert max(q) <= 1-a + 1e-12, (a, ell)
            assert abs(q[-1] - (1-a)/(1+a)) < 2e-8, (a, ell)
    print('PASS: exact rational identities; companion radii and bounds; finite recurrences')


if __name__ == '__main__':
    main()
