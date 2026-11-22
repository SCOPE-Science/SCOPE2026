#!/usr/bin/env python3
"""Finite exact checks and high-precision sanity checks for conditioned triangle-free exponential sticks.

The infinite limit and tail asymptotic are analytical and are not certified by these tests.
No third-party modules are required.
"""
from fractions import Fraction
from itertools import product
from math import factorial, sqrt, isclose
from decimal import Decimal, localcontext

CHECKS = 0

def verify(condition):
    global CHECKS
    if not condition:
        raise AssertionError('a check failed')
    CHECKS += 1

F = [0, 1, 1]
for i in range(3, 101):
    F.append(F[-1] + F[-2])

def G(r):
    return F[r+2] - 1

def reconstruct(z):
    y = []
    for i, x in enumerate(z):
        if i == 0:
            y.append(x)
        elif i == 1:
            y.append(y[0] + x)
        else:
            y.append(y[i-1] + y[i-2] + x)
    return y

for n in range(3, 14):
    for zz in product((Fraction(1, 2), Fraction(2, 3)), repeat=n if n <= 8 else 3):
        if len(zz) != n:
            z = list(zz) + [Fraction((i % 5)+1, 7) for i in range(n-len(zz))]
        else:
            z = list(zz)
        y = reconstruct(z)
        verify(all(y[i] >= y[i-1] for i in range(1,n)))
        verify(all(y[i] >= y[i-1]+y[i-2] for i in range(2,n)))
        for i in range(n):
            verify(y[i] == sum(F[i-j+1]*z[j] for j in range(i+1)))
        verify(sum(y) == sum(G(n-i)*z[i] for i in range(n)))
        verify(all(y[i] > 0 for i in range(n)))

for r in range(1, 96):
    verify(G(r) == sum(F[k] for k in range(1,r+1)))
    verify(F[r] <= G(r))
for r in range(1, 95):
    # Cassini-derived finite-n exact monotonicity.
    verify(F[r]*G(r+1)-F[r+1]*G(r) == (-1)**(r+1)+F[r-1])
    verify(F[r]*G(r+1) >= F[r+1]*G(r))
for n in range(3, 25):
    p = Fraction(factorial(n), 1)
    for r in range(1,n+1):
        p /= G(r)
    verify(0 < p < 1)
    if n == 3: verify(p == Fraction(3, 4))
    if n == 4: verify(p == Fraction(3, 7))
    if n == 5: verify(p == Fraction(5, 28))
    if n == 6: verify(p == Fraction(3, 56))
    coeff = [Fraction(F[r],G(r)) for r in range(1,n+1)]
    verify(min(coeff) == Fraction(F[n],G(n)))
    # Dirichlet(1,...,1) moments of conditional largest-share.
    av = sum(coeff) / n
    second = (sum(c*c for c in coeff) + sum(coeff)**2)/ (n*(n+1))
    variance = second - av*av
    verify(Fraction(0) < av < Fraction(1))
    verify(variance > 0)

# Validate the limiting constants, logarithmic rates, and the exact telescope.
with localcontext() as ctx:
    ctx.prec = 65
    phi = (Decimal(1)+Decimal(5).sqrt())/Decimal(2)
    c = phi**-2
    q = -phi**-1
    series_mean=Decimal(0)
    series_var=Decimal(0)
    for r in range(1, 78):
        b = Decimal(F[r])/Decimal(G(r)) - c
        b2 = (Decimal(1)-q**r)/(phi**2*Decimal(G(r)))
        verify(abs(b-b2) < Decimal('1e-55'))
        verify(b > 0)
        if r>=2: verify(b<phi**-1)
        series_mean+=b
        series_var+=b*b
    tailprod=Decimal(1)
    for r in range(2, 72):
        b=Decimal(F[r])/Decimal(G(r))-c
        tailprod /= (1-phi*b)
        verify(abs(tailprod - Decimal(G(r))/(phi**(r-1))) < Decimal('1e-52'))
    C=phi**3/Decimal(5).sqrt()
    verify(abs(C-(Decimal(1)+Decimal(2)/Decimal(5).sqrt())) < Decimal('1e-60'))
    verify(abs(tailprod-C) < Decimal('1e-13'))
    verify(abs(series_mean-Decimal('0.98369455639074'))<Decimal('1e-12'))
    verify(abs(series_var-Decimal('0.41375352870235'))<Decimal('1e-12'))
    print('mean_limit',series_mean)
    print('variance_limit',series_var)
    print('sharp_tail_prefactor',C)
print('PASS',CHECKS,'finite algebraic/high-precision assertions')
