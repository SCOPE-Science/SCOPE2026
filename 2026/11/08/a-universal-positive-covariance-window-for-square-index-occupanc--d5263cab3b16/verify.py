#!/usr/bin/env python3
"""Standalone checks for the square-index occupancy covariance crossover.

Run: python3 verify.py
Only Python's standard library is required.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial, exp
from decimal import Decimal, localcontext


def covariance_formula(m, n, r, s):
    """Exact covariance of distinct occupancy frequencies C_r,C_s."""
    if not (m >= 2 and n >= 0 and 0 <= r <= n and 0 <= s <= n and r != s):
        raise ValueError('invalid arguments')
    den = m ** n
    pr = Fraction(comb(n, r) * (m - 1) ** (n - r), den)
    ps = Fraction(comb(n, s) * (m - 1) ** (n - s), den)
    both = Fraction(0)
    if n >= r + s:
        mult = comb(n, r) * comb(n - r, s)
        both = Fraction(mult * (m - 2) ** (n - r - s), den)
    return m * (m - 1) * both - m * m * pr * ps


def test_exhaustive():
    checks = 0
    for m in range(2, 5):
        for n in range(0, 9):
            tally = [0] * (n + 1)
            joint = [[0] * (n + 1) for _ in range(n + 1)]
            for assignment in product(range(m), repeat=n):
                counts = [0] * m
                for box in assignment:
                    counts[box] += 1
                frequencies = [0] * (n + 1)
                for count in counts:
                    frequencies[count] += 1
                for r in range(n + 1):
                    tally[r] += frequencies[r]
                    for s in range(n + 1):
                        joint[r][s] += frequencies[r] * frequencies[s]
            den = m**n
            for r in range(n + 1):
                for s in range(n + 1):
                    if r == s:
                        continue
                    observed = Fraction(joint[r][s], den) - Fraction(tally[r] * tally[s], den * den)
                    assert observed == covariance_formula(m, n, r, s), (m, n, r, s)
                    checks += 1
    return checks


def coefficients(r, s, lam):
    lam = Fraction(lam)
    f = lam + 1 - r - s + Fraction(r * s, 1) / lam
    g = -2 * lam + Fraction(3 * (r + s) - 1, 2) - Fraction(r * s * (r + s - 1), 1) / (2 * lam * lam)
    return f, g


def test_square_pairs():
    checks = 0
    for j in range(1, 101):
        r, s, lam = j*j, (j+1)*(j+1), j*(j+1)
        f, g = coefficients(r, s, lam)
        assert f == 0 and g == 1
        assert (r+s-1)**2 == 4*r*s
        checks += 3
    return checks


def covariance_decimal(m, n, r, s):
    # Factorization avoids subtracting two large almost equal pair probabilities.
    with localcontext() as ctx:
        ctx.prec = 95
        d = Decimal
        p = d(1) - d(1)/d(m)
        pr = d(comb(n, r)) * d(m)**(-r) * p**(n-r)
        ps = d(comb(n, s)) * d(m)**(-s) * p**(n-s)
        ratio = d(m-1)/d(m)
        for k in range(s):
            ratio *= d(n-r-k)/d(n-k)
        ratio *= (d(1)-d(2)/d(m))**(n-r-s) / p**(2*n-r-s)
        return pr * ps * d(m)**2 * (ratio - 1)


def test_asymptotic():
    checks = 0
    for j in (1, 2):
        r, s, lam = j*j, (j+1)**2, j*(j+1)
        target = exp(-2*lam)*lam**(r+s)/(factorial(r)*factorial(s))
        data = [float(covariance_decimal(m,lam*m,r,s)) for m in (100, 200, 400)]
        assert max(abs(v-target) for v in data[-1:]) < 0.0015
        assert abs(data[2]-target) < abs(data[1]-target) < abs(data[0]-target)
        checks += 2
        m=1600
        for z in (-3.,-1.,0.,1.,3.):
            n = round(lam*m + z*m**0.5)
            observed = float(covariance_decimal(m,n,r,s))
            limit = target * (1-z*z/lam)
            # These are diagnostics for the finite-m convergence, not proof of it.
            assert abs(observed - limit) < max(0.008, abs(limit)*0.25)
            checks += 1
    return checks

if __name__ == '__main__':
    a,b,c = test_exhaustive(),test_square_pairs(),test_asymptotic()
    print(f'PASS: {a} exhaustive exact covariance assertions; {b} exact critical-polynomial assertions; {c} asymptotic diagnostic assertions; total {a+b+c}.')
