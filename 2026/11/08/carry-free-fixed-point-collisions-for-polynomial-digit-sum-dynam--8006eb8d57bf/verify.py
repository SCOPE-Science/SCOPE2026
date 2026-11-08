#!/usr/bin/env python3
"""Exact finite diagnostics for digit-sum polynomial fixed-point identities.

This is not a replacement for the unlimited-degree/binomial proof.
Requires only the Python standard library.
"""
from itertools import product
from math import comb


def digitsum(n, base):
    assert n > 0 and base >= 2
    total = 0
    while n:
        n, d = divmod(n, base)
        total += d
    return total


def eval_poly(coeff, x):
    val = 0
    for c in reversed(coeff):
        val = val * x + c
    return val


def translated_coefficients(coeff, a):
    # g(Y+a-1) = sum_j c_j Y^j
    d = len(coeff) - 1
    return [sum(coeff[i] * comb(i,j) * (a-1)**(i-j)
                for i in range(j,d+1)) for j in range(d+1)]


def check_polynomial_family():
    cases = 0
    for d in range(2, 6):
        for lower in product(range(3), repeat=d):
            for lc in (1,2,3):
                p = tuple(lower) + (lc,)
                for a in range(2, 13):
                    v = eval_poly(p,a)
                    b = v-a+1
                    assert b >= 3 and v > a
                    cx = translated_coefficients(p,a)
                    assert sum(cx) == v
                    assert all(0<=t<b for t in cx)
                    assert digitsum(v,b) == a
                    assert digitsum(eval_poly(p,v),b) == v
                    cases += 1
    print('POLYNOMIAL_FAMILY_OK', cases)


def check_square_progressions():
    cases = 0
    for j in range(0, 2000):
        b = 9*j+7
        a=3*j+3
        z=12*j+9
        assert a+ b-1 == z
        assert a*a == (j+1)*b+(2*j+2)
        assert z*z == b*b+(7*j+4)*b+(5*j+4)
        assert digitsum(a*a,b)==a and digitsum(z*z,b)==z
        cases+=1
    for j in range(1, 2000):
        b=9*j+4
        a=6*j+3
        z=15*j+6
        assert a+b-1==z
        assert a*a == (4*j+2)*b+(2*j+1)
        assert z*z == 2*b*b+(7*j)*b+(8*j+4)
        assert digitsum(a*a,b)==a and digitsum(z*z,b)==z
        cases+=1
    print('SQUARE_ARITHMETIC_PROGRESSIONS_OK',cases)


def check_first_two_residue_lifts():
    # Independent brute-force check of the optional exact two-lift criterion.
    tests = 0
    for b in range(3, 501):
        m=b-1
        for a in range(2,b):
            t=a-1
            h,r=divmod(t*(t+1),m)
            criterion=(r == 0 and
                       (2*t+h <= b or
                        (t+h>b and 2*t+h <=2*b+1)))
            direct=(digitsum(a*a,b)==a and
                    digitsum((a+m)**2,b)==a+m)
            assert criterion==direct,(a,b,h)
            tests+=1
    print('TWO_LIFT_CRITERION_CHECK_OK',tests)


if __name__ == '__main__':
    check_polynomial_family()
    check_square_progressions()
    check_first_two_residue_lifts()
    print('VERIFY_OK exact_integer=yes independent_formula_crosschecks=yes finite_tests_not_infinite_proof=yes')
