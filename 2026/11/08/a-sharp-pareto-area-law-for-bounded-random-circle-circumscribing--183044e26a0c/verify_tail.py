#!/usr/bin/env python3
"""Standalone arithmetic and seeded simulation for the circle-tangent area-tail theorem.

Only uses the Python standard library. Finite tests support, not replace, the proof.
"""
import math
import random
from fractions import Fraction


def p_bounded(n):
    return Fraction(1, 1) - Fraction(n, 2 ** (n - 1))


def unconditioned_coefficient(n):
    return n * (n - 1) / (2 ** (n - 2) * math.pi)


def gap_strip(n, d):
    return (Fraction(1, 2) + d) ** (n - 1) - Fraction(1, 2) ** (n - 1)


def shifted_simplex_two(n, s1, s2):
    if s1 + s2 >= 1:
        return Fraction(0, 1)
    return (1 - s1 - s2) ** (n - 1)


def exact_checks():
    for n in range(3, 13):
        pb = p_bounded(n)
        assert pb > 0
        d = Fraction(1, 1000)
        # The two-gap cap event has exact translated-simplex measure.
        assert shifted_simplex_two(n, Fraction(1, 2) - d, Fraction(1, 2) - d) == (2 * d) ** (n - 1)
        assert shifted_simplex_two(n, Fraction(1, 2) - d, Fraction(1, 2)) == d ** (n - 1)
        s = gap_strip(n, d)
        lower = s - (n - 1) * d ** (n - 1)
        assert lower > 0
        # The strip's leading derivative agrees with the exact claimed coefficient.
        target = Fraction(n - 1, 2 ** (n - 2))
        assert abs(float(s / d - target)) < 0.2
        assert abs(unconditioned_coefficient(n) / float(pb) -
                   2 * n * (n - 1) / (math.pi * (2 ** (n - 1) - n))) < 1e-12
    print('EXACT_OK n=3..12 Dirichlet simplex translated cap identity, strip coefficient, boundedness')


def simulation_checks():
    rng = random.Random(202611030231)
    tests = [(3, 720000), (4, 720000), (6, 720000)]
    threshold = 160.0
    report = []
    for n, total in tests:
        valid = 0
        high = 0
        for _ in range(total):
            exps = [-math.log(max(rng.random(), 1e-300)) for _ in range(n)]
            den = sum(exps)
            gaps = [v / den for v in exps]
            if max(gaps) < 0.5:
                valid += 1
                area = sum(math.tan(math.pi * v) for v in gaps)
                if area > threshold:
                    high += 1
        pb_hat = valid / total
        joint_constant_hat = threshold * high / total
        exact_constant = unconditioned_coefficient(n)
        assert abs(pb_hat - float(p_bounded(n))) < 0.006
        # Finite-threshold and Monte Carlo errors are allowed; not an asymptotic proof.
        assert abs(joint_constant_hat - exact_constant) < 0.16, (n, joint_constant_hat, exact_constant)
        report.append((n, round(pb_hat, 6), round(joint_constant_hat, 6), round(exact_constant, 6), high))
    print('SIMULATION_OK threshold=160 samples_per_n=720000 (n, bounded_fraction, t_joint_tail, exact_limit, exceedances)')
    print(report)


if __name__ == '__main__':
    exact_checks()
    simulation_checks()
