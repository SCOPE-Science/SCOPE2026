#!/usr/bin/env python3
"""Exact finite checks for the fractional-Volterra self-commutator theorem.

This program checks finite rational identities, not the infinite-rank theorem.
No third-party dependencies are required.
"""
from fractions import Fraction as F
from math import comb, factorial, gamma


def k_polynomial(m, x, y):
    """Oriented integral of the polynomial commutator kernel."""
    ans = F(0)
    for ell in range(m):
        p = m + ell
        ans += comb(m-1, ell) * (y-x)**(m-1-ell) * (x**p-(1-y)**p) / p
    return ans / factorial(m-1)**2


def k_direct(m, x, y):
    """Independently expand TT* and T*T in the integration variable."""
    a = F(0)
    b = F(0)
    u = min(x, y)
    v = max(x, y)
    for i in range(m):
        for j in range(m):
            c = comb(m-1, i) * comb(m-1, j)
            a += c * (-1)**(i+j) * x**(m-1-i) * y**(m-1-j) * u**(i+j+1) / (i+j+1)
            b += c * (-x)**(m-1-i) * (-y)**(m-1-j) * (1-v**(i+j+1)) / (i+j+1)
    return (a-b) / factorial(m-1)**2


def rank_rational(matrix):
    a = [list(row) for row in matrix]
    rows = len(a)
    cols = len(a[0])
    rank = 0
    for col in range(cols):
        q = next((q for q in range(rank, rows) if a[q][col]), None)
        if q is None:
            continue
        a[rank], a[q] = a[q], a[rank]
        piv = a[rank][col]
        a[rank] = [z/piv for z in a[rank]]
        for q in range(rows):
            if q != rank and a[q][col]:
                f = a[q][col]
                a[q] = [w-f*z for w,z in zip(a[q], a[rank])]
        rank += 1
    return rank


def run():
    tests = 0
    for m in range(1, 7):
        for a in range(1, 8):
            for b in range(1, 8):
                x = F(a, 9)
                y = F(b, 10)
                k = k_polynomial(m,x,y)
                assert k == k_direct(m,x,y), (m,x,y)
                assert k == k_polynomial(m,y,x)
                assert k == -k_polynomial(m,1-x,1-y)
                tests += 3
        grid = [F(i+1, 2*m+1) for i in range(2*m)]
        mat = [[k_polynomial(m,x,y) for y in grid] for x in grid]
        assert rank_rational(mat) == 2*m, m
        tests += 1
    for a in (0.75, 1.25, 1.5, 2.5, 3.1):
        p = 1.0
        for ell in range(12):
            if ell > 0:
                p *= (a-ell)/ell
            beta = gamma(ell+1)*gamma(a)/gamma(ell+1+a)
            coeff = ((-1)**ell)*p*beta/gamma(a)**2
            assert coeff != 0.0
            tests += 1
    print(f'PASS: {tests} exact rational identities and finite-rank witnesses / coefficient nonvanishing tests')
    print('Infinite-dimensional rank and inertia claims are established analytically, not by this program.')

if __name__ == '__main__':
    run()
