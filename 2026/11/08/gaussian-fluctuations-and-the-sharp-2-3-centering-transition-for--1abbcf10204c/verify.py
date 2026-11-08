"""Finite numerical checks for the aligned critical-Zipf quorum theorem.

Runs using Python 3 standard library.  No finite check proves weak convergence.
"""
import math
from fractions import Fraction
from itertools import product
from statistics import NormalDist

EULER = 0.57721566490153286060651209008240243104215933593992


def harmonic(n):
    return math.fsum(1.0 / i for i in range(1, n + 1))


def mean(n, a):
    return math.fsum(-math.expm1(-a / i) / i for i in range(1, n + 1))


def derivative(n, a):
    return math.fsum(math.exp(-a / i) / (i * i) for i in range(1, n + 1))


def variance(n, a):
    return math.fsum(math.exp(-a / i) * -math.expm1(-a / i) / (i * i)
                     for i in range(1, n + 1))


def bisection_root(n, theta):
    target = theta * harmonic(n)
    lo, hi = 0.0, 1.0
    while mean(n, hi) < target:
        hi *= 2.0
    for _ in range(70):
        mid = (lo + hi) / 2.0
        if mean(n, mid) >= target:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def finite_subset_test(n, theta, a):
    """Brute force all subsets, checking first-contact event mass > threshold."""
    h_exact = sum((Fraction(1, i) for i in range(1, n + 1)), Fraction(0))
    q = [1.0 - math.exp(-a / i) for i in range(1, n + 1)]
    probability = 0.0
    moments = [0.0, 0.0]
    for indicators in product((0, 1), repeat=n):
        prob = math.prod(q[i] if j else 1 - q[i] for i, j in enumerate(indicators))
        mass = sum((Fraction(j, i + 1) for i, j in enumerate(indicators)), Fraction(0))
        probability += prob if mass > Fraction(str(theta)) * h_exact else 0.0
        x = float(mass)
        moments[0] += x * prob
        moments[1] += x*x*prob
    expected = mean(n, a)
    v_expected = variance(n, a)
    assert abs(moments[0] - expected) < 1e-11
    assert abs(moments[1] - moments[0]**2 - v_expected) < 1e-11
    assert -1e-10 <= probability <= 1.0000000001
    return probability


def main():
    count = 0
    for n in range(2, 9):
        for theta in (0.2, 0.5, 0.7):
            for a in (0.4, 1.3, 4.0):
                p = finite_subset_test(n, theta, a)
                assert 0 <= p <= 1
                count += 1
    for n in (1000, 10000, 100000):
        for theta in (0.50, 2/3, 0.80):
            h = harmonic(n)
            b = math.exp(theta*h - 2*EULER)
            root = bisection_root(n, theta)
            assert abs(mean(n, root) - theta*h) < 1e-11
            assert 0.75 < (root-b) / (b*b/n) < 1.3
            assert root > b
            assert 0 < root*derivative(n, root) < 1.20
            count += 4
    for a, n in ((20.0, 100000), (60.0, 200000), (200.0, 500000)):
        varcoef = a*variance(n, a)
        expected = 0.5
        # O(a/n) upper tail and O(a^-1) discretization are allowed.
        assert abs(varcoef-expected) < (a/n)*1.5 + 0.01
        count += 1
    for a in (20.0, 60.0, 200.0):
        # Infinite harmonic correction measured by finite sum and analytic tail.
        n = 300000
        f = mean(n, a)
        corrected = f + a/n - a*a/(4*n*n)
        assert abs(corrected - math.log(a) - 2*EULER) < 0.002
        count += 1
    print(f"PASS: {count} case groups; exact subset enumeration, mean/variance, root bias, and kernel limits")

if __name__ == '__main__':
    main()
