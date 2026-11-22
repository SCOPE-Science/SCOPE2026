"""Standalone algebraic and numerical spot checks for the spectral locking theorem.

Only Python 3 standard library is required. Numerical checks corroborate,
but do not replace, the universal analytic proof.
"""
from fractions import Fraction
from math import sqrt, exp, log, isclose

checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1

def F(n, lam):
    z = lam + n*n
    return z*z / ((lam + (n-1)**2)*(lam + (n+1)**2))

def R(n, lam, s):
    z = lam + n*n
    if n == 0:
        return (lam/(lam+1))**s
    return Fraction(1,2) * ((z/(lam+(n-1)**2))**s +
                  (z/(lam+(n+1)**2))**s)

def a(n, lam, s):
    return (lam+n*n)**(-s)

def coeff(n, lam, s, b):
    return a(n,lam,s) + b/2*(a(abs(n-1),lam,s)+a(n+1,lam,s))

# Formulae for all rational parameters here are checked EXACTLY.
for lam in [Fraction(1,2),Fraction(3,4),Fraction(1),
            Fraction(5,4),Fraction(3,2)]:
    check(F(1,lam) <= 1)
    check(F(2,lam) > 1)
    check(F(2,lam) > F(3,lam))
    for n in range(2,70):
        check(F(n,lam) > 1)
    for n in range(3,69):
        check(F(n,lam) > F(n+1,lam))
    for s in [1,2,3,4,5,6]:
        r2 = R(2,lam,s)
        check(r2 > 1)
        for n in range(70):
            if n != 2:
                check(r2 > R(n,lam,s))
        bcrit = -1/r2
        check(coeff(2,lam,s,bcrit) == 0)
        for n in range(70):
            if n != 2:
                check(coeff(n,lam,s,bcrit) > 0)
        check(coeff(2,lam,s,bcrit-Fraction(1,10000)) < 0)

# Floating-point stress tests also include fractional orders and the exact
# upper interval endpoint (where the n=2 and n=3 log-product conditions tie).
star=(5*sqrt(22)-14)/6
for lam in [0.5,0.51,0.75,1.0,1.3,1.5,star]:
    for s in [0.0005,0.02,0.1,0.51,0.7,1.1,2.3,5,15]:
        r2=R(2,lam,s)
        for n in range(70):
            if n != 2:
                check(r2 >= R(n,lam,s) - 2e-13)
        check(r2 > 1)
# Two necessity mechanisms outside the locking interval.
check(R(1,0.4,80) > R(2,0.4,80))
check(R(3,2,0.001) > R(2,2,0.001))
# A direct continuous-kernel example: lambda=s=1, sharp b=-2/3.
check(R(2,1,1) == 1.5)
check(coeff(2,1,1,-2/3) == 0 or abs(coeff(2,1,1,-2/3)) < 1e-15)
print('PASS',checks,'assertions')
