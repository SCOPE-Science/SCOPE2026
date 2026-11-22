#!/usr/bin/env python3
"""Exact independent checks for the graded insertion-inversion type law.
Requires only the Python standard library.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb


def direct_mean_histogram(n):
    total = [0] * (n + 1)
    for p in permutations(range(1, n + 1)):
        for i in range(n + 1):
            # For a new point inserted after i old points and at value rank j,
            # the new inversion degree equals i+j-2 times their prefix overlap.
            for j in range(n + 1):
                overlap = sum(int(p[t] <= j) for t in range(i))
                total[i + j - 2 * overlap] += 1
    from math import factorial
    return [Fraction(x, factorial(n)) for x in total]


def hypergeometric_mean_histogram(n):
    res = [Fraction(0) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            for a in range(max(0, i + j - n), min(i, j) + 1):
                res[i + j - 2 * a] += Fraction(comb(j, a) * comb(n - j, i - a), comb(n, i))
    return res


def log_integral_mean_histogram(n):
    # Expand (1+x)^k(1-x)^(n-k), integrate even powers
    # against -log |x| on [-1,1]. Integral x^(2r)(-log x) = 1/(2r+1)^2.
    result = []
    for k in range(n + 1):
        summand = Fraction(0)
        for j in range(0, n + 1, 2):
            coeff = sum((-1) ** (j-a) * comb(k, a) * comb(n-k, j-a)
                        for a in range(max(0, j-(n-k)), min(k, j)+1))
            summand += Fraction(coeff, (j+1) ** 2)
        result.append(Fraction((n+1)**2 * comb(n, k), 2**n) * summand)
    return result


def run():
    for n in range(1, 7):
        d = direct_mean_histogram(n)
        h = hypergeometric_mean_histogram(n)
        b = log_integral_mean_histogram(n)
        assert d == h == b, (n, d, h, b)
        assert sum(b) == (n+1)**2
        assert b == list(reversed(b))
    for n in range(7, 13):
        h = hypergeometric_mean_histogram(n)
        b = log_integral_mean_histogram(n)
        assert h == b and sum(h) == (n+1)**2
    examples = {6: Fraction(176,15),8:Fraction(563,35),10:Fraction(6508,315),12:Fraction(88069,3465)}
    for n, target in examples.items():
        assert log_integral_mean_histogram(n)[n//2] == target
    print('VERIFY_OK: 6 complete enumeration checks; 12 hypergeometric/integral identities; central rational examples')

if __name__=='__main__':
    run()
