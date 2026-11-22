"""Finite exact Wick-contraction checks for normalized Gaussian Fourier fourth moments.

This script is supplementary to the all-degree proof and asymptotic cumulant argument.
Requires Python 3 standard library only.
"""
from collections import defaultdict
from fractions import Fraction
from math import factorial


def gaussian_expectation(poly):
    """Moment of a polynomial in independent standard circular complex Gaussians."""
    total = 0
    for (positive, negative), coefficient in poly.items():
        if positive == negative:
            term = coefficient
            for power in positive:
                term *= factorial(power)
            total += term
    return total


def fourth_norm_polynomial(n):
    """Formal polynomial for integral |sum g_j z^j|^4 dm(z)."""
    terms = defaultdict(int)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                d = a + b - c
                if not 0 <= d < n:
                    continue
                plus = [0]*n
                minus = [0]*n
                plus[a] += 1
                plus[b] += 1
                minus[c] += 1
                minus[d] += 1
                terms[(tuple(plus), tuple(minus))] += 1
    return dict(terms)


def product_poly(poly):
    n = len(next(iter(poly))[0])
    result = defaultdict(int)
    for (pos1, neg1), x in poly.items():
        for (pos2, neg2), y in poly.items():
            result[(tuple(pos1[i] + pos2[i] for i in range(n)),
                    tuple(neg1[i] + neg2[i] for i in range(n)))] += x*y
    return result


def exact_variance(n):
    return Fraction(4*(n-1)*(2*n*n-2*n-1), 3*(n+1)**2*(n+2)*(n+3))


def verify():
    checks=0
    for n in range(1, 10):
        auto = sum((n-abs(k))**2 for k in range(-n+1, n))
        assert auto == Fraction(2*n**3+n, 3)
        checks += 1
        mean_t = 2*n*n
        second_t = Fraction(4*n**4, 1) + Fraction(56*n**3 + 4*n, 3)
        ey = Fraction(mean_t, n*(n+1))
        ey2 = second_t / (n*(n+1)*(n+2)*(n+3))
        assert ey == Fraction(2*n, n+1)
        assert ey2 - ey*ey == exact_variance(n)
        checks += 2
    for n in range(1, 8):
        poly = fourth_norm_polynomial(n)
        t_mean = gaussian_expectation(poly)
        t_second = gaussian_expectation(product_poly(poly))
        assert t_mean == 2*n*n, (n, t_mean)
        assert t_second == Fraction(4*n**4,1) + Fraction(56*n**3+4*n,3), (n,t_second)
        checks += 2
    # n=2: Y=1+2U(1-U), U uniform on [0,1].
    assert Fraction(1, 1) + 2*(Fraction(1,2)-Fraction(1,3)) == Fraction(4,3)
    assert exact_variance(2) == Fraction(1,45)
    checks += 2
    # Limit of n*variance is the Wick quartic limit 8/3.
    for n in (100, 1_000, 10_000):
        approx = float(n*exact_variance(n))
        assert abs(approx - 8/3) < 30/n
        checks += 1
    print(f"PASS: {checks} exact and asymptotic arithmetic assertions; Gaussian expansion independent of closed-form variance")


if __name__ == '__main__':
    verify()
