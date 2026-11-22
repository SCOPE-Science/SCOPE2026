#!/usr/bin/env python3
"""Exact-rational checks for the branch-imbalance moment theorem.

Only Python's standard library is needed. These finite checks verify the
polynomial generator and sample high-moment coefficients; the general theorem
is proved analytically in RESULT.md.
"""
from fractions import Fraction
from math import comb, factorial

checks = 0

def verify(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)


def generator(a, b):
    """Generator on S**a * D**b; b must be even."""
    verify(a >= 0 and b >= 0 and b % 2 == 0, 'nonnegative/even powers')
    out = {}
    def add(exps, value):
        out[exps] = out.get(exps, 0) + value
    for k in range(a + 1):
        for j in range(0, b + 1, 2):
            add((k + 1, b - j), comb(a, k) * comb(b, j))
        for j in range(1, b + 1, 2):
            add((k, b - j + 1), comb(a, k) * comb(b, j))
    add((a + 1, b), -1)
    if b == 0:
        for k in range(a + 1):
            add((k, 0), 2**a * comb(a, k))
    add((a, b), -1)
    return {key: val for key, val in out.items() if val != 0}


def expect_coeff(r):
    """Coefficient of exp((r+2**r-1)t) in E[D**(2r)],
    normalized by that in E[S**r], using the triangular generator."""
    lam = r + 2**r - 1
    coeff = {}
    for degree in range(2*r+1):
        for a in range(degree + 1):
            b = degree-a
            if b % 2 or a + b//2 > r:
                continue
            if (a, b) == (r, 0):
                coeff[(a, b)] = Fraction(1)
                continue
            g = generator(a, b)
            diag = g.get((a, b), 0)
            verify(diag == (a + 2**a - 1 if b == 0 and a else a+b-1 if b else 0),
                   'diagonal generator')
            verify(all(i + j <= degree and j % 2 == 0 and i+j//2 <= r
                       for i,j in g), 'generator closure')
            if degree <= r:
                coeff[(a, b)] = Fraction(0)
            else:
                verify(lam != diag, 'nonresonance')
                total = sum((Fraction(c) * coeff.get((i,j), Fraction(0))
                             for (i,j),c in g.items() if (i,j)!=(a,b)), Fraction(0))
                coeff[(a,b)] = total / (lam-diag)
    return coeff[(0, 2*r)]


def beta_ratio(r):
    q = 2**r-r
    return Fraction(2**r * factorial(2*r), 2**r * factorial(r)) * Fraction(
        factorial(q-1)*factorial(r), factorial(2**r))

verify(generator(1,0) == {(1,0):2,(0,0):2}, 'G S')
verify(generator(2,0) == {(2,0):5,(1,0):9,(0,0):4}, 'G S^2')
verify(generator(0,2) == {(0,2):1,(1,0):1}, 'G D^2')
verify(generator(0,4) == {(0,4):3,(1,2):6,(0,2):4,(1,0):1}, 'G D^4')
known = [Fraction(1),Fraction(1),Fraction(3,7),Fraction(1,13),Fraction(5,899)]
for r in range(1,7):
    actual = expect_coeff(r)
    verify(actual == beta_ratio(r), 'beta coefficient identity')
    if r <= 5:
        verify(actual == known[r-1], 'small exact ratio')
    print('r=',r,'exponent=',r+2**r-1,'ratio=',actual)
print('PASS',checks,'exact assertions')
