#!/usr/bin/env python3
"""Exact finite consistency checks for cubic Walsh projection norm plateaus.

All decisive statements for unbounded dimension are proved algebraically in RESULT.md.
This script uses only Python's standard library.
"""
from fractions import Fraction
from math import comb
from itertools import product


def e2(n, s):
    assert (s*s-n)%2 == 0
    return (s*s-n)//2


def e3(n, s):
    assert (s**3 - (3*n-2)*s)%6 == 0
    return (s**3-(3*n-2)*s)//6


def norm(n):
    return Fraction(sum(comb(n,j)*abs(e3(n,n-2*j)) for j in range(n+1)),2**n)


def prediction(n):
    return any(r*(r+2)==3*n for r in range(3,n+1,2))


if __name__ == '__main__':
    for n in range(3,11):
        brute = Fraction(sum(abs(sum(x[i]*x[j]*x[k]
                     for i in range(n) for j in range(i+1,n) for k in range(j+1,n)))
                     for x in product((-1,1),repeat=n)),2**n)
        assert brute == norm(n), (n, brute, norm(n))
    plateaus = []
    for n in range(3,181):
        old, new = norm(n), norm(n+1)
        delta = new-old
        assert delta >= 0
        prediction_here = prediction(n)
        assert (delta == 0) == prediction_here, n
        # Independent pointwise comparison for the martingale step.
        rhs = Fraction(sum(comb(n,j)*max(0,abs(e2(n,n-2*j))-abs(e3(n,n-2*j)))
                           for j in range(n+1)),2**n)
        assert delta == rhs, n
        if prediction_here:
            plateaus.append(n)
    assert plateaus == [5,21,33,65,85,133,161], plateaus
    for r in range(3,80,2):
        if r%3 in (0,1):
            n = r*(r+2)//3
            if n >= 3:
                assert prediction(n)
    print('CUBIC_WALSH_PLATEAU_PASS brute_dimensions=3..10 exact_n=3..181 plateaus=' + ','.join(map(str,plateaus)))
