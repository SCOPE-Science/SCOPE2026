#!/usr/bin/env python3
"""Exact finite consistency checks for harmonic Bergman monomial commutators.

This auxiliary program checks rational basis coefficients and finite identities.
It is not a proof of the infinite-dimensional spectral theorem.
"""
from fractions import Fraction

checks = 0

def ok(statement):
    global checks
    assert statement
    checks += 1


def projected_coefficient(p, q):
    """The harmonic projection of z**p * conjugate(z)**q, monomial output."""
    if p >= q:
        return Fraction(p-q+1, p+1)
    return Fraction(q-p+1, q+1)


def direct_weight_square(m, j):
    p, q = (m+j, 0) if j >= 0 else (m, -j)
    return Fraction(abs(j)+1, abs(j+m)+1)*projected_coefficient(p,q)**2


def weight_square(m, j):
    if j >= 0:
        return Fraction(j+1, j+m+1)
    n = -j
    if n <= m:
        return Fraction((n+1)*(m-n+1), (m+1)**2)
    return Fraction(n-m+1, n+1)


def a(m, j):
    assert j >= 1
    if j < m:
        return Fraction(j*j*(j+1), (j+m+1)*(m+1)**2)
    return Fraction(m*m, (j+1)*(j+m+1))


def d(m, j):
    return weight_square(m,j)-weight_square(m,j-m)


def analytic_norm(m):
    return Fraction(m*m,(m+1)*(2*m+1))


def finite_positive_sum(m):
    return sum((a(m,j) for j in range(1,m)),Fraction(0))


def tail_positive_sum(m):
    # sum_{j=m}^infinity m**2/((j+1)(j+m+1))
    return m*sum((Fraction(1,j+1) for j in range(m,2*m)),Fraction(0))


def trace_norm(m):
    return Fraction(m*(5*m+1),3*(m+1))

for m in range(1,31):
    for j in range(-5*m-10, 5*m+11):
        ok(weight_square(m,j) == direct_weight_square(m,j))
        ok(Fraction(0) < weight_square(m,j) <= 1)
        ok(d(m,-j) == -d(m,j))
        if j > 0:
            ok(d(m,j) == a(m,j))
            ok(d(m,j) > 0)
        if j == 0:
            ok(d(m,j) == 0)
    ok(a(m,m) == analytic_norm(m))
    for j in range(1,m):
        ok(a(m,j) < a(m,j+1))
    for j in range(m,m+30):
        ok(a(m,j)>a(m,j+1))
    ok(2*(finite_positive_sum(m)+tail_positive_sum(m))==trace_norm(m))
    sum_min = sum((Fraction((m-r+1)*(r+1),(m+1)**2) for r in range(m)),Fraction(0))
    ok(2*(m-sum_min)==trace_norm(m))
    for j in range(50*m,50*m+11):
        ok(a(m,j)*j*j < m*m)
        ok(a(m,j)*(j+m+1)*(j+1)==m*m)

print('HARMONIC_BERGMAN_MONOMIAL_FINITE_OK', checks)
