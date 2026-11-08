"""Exact finite checks for the axial pentablock Hardy-space identities.

The infinite-dimensional conclusions are proved analytically; these tests are
independent finite consistency checks, not a replacement for that proof.
"""
from fractions import Fraction
from math import comb, asin, sqrt, pi

checks = 0

def verify(statement):
    global checks
    assert statement
    checks += 1

def h(j):
    return Fraction(comb(2*j, j), 4**j)

def a(j):
    return 1 / h(j)

for m in range(3):
    for k in range(0, 201):
        moment = h(m+k) / h(m)
        verify(moment > 0)
        verify(moment == Fraction(comb(2*(m+k),m+k),4**(m+k)) / h(m))
        w2 = moment if k == 0 else moment / (h(m+k-1) / h(m))
        if k == 0:
            verify(h(m+1)/h(m) == Fraction(2*m+1, 2*m+2))
        else:
            squared_weight = (h(m+k+1)/h(m+k))
            previous_squared_weight = h(m+k)/h(m+k-1)
            verify(squared_weight == Fraction(2*(m+k)+1,2*(m+k)+2))
            verify(squared_weight-previous_squared_weight == Fraction(1,2*(m+k)*(m+k+1)))
        verify(Fraction(1, moment) == a(m+k)/a(m))

for j in range(0, 350):
    verify((2*j+1)*a(j+1) == 2*(j+1)*a(j))
    verify(a(j) == Fraction(4**j,comb(2*j,j)))

for m in range(3):
    verify(sum(Fraction(1,2*(m+k)*(m+k+1)) for k in range(1,1000))
           + Fraction(1,2*(m+1000)) == Fraction(1,2*(m+1)))
    verify(Fraction(2*m+1,2*m+2) + Fraction(1,2*(m+1)) == 1)

for z in (0.005,0.05,0.2,0.5,0.8):
    F = 1/(1-z) + sqrt(z)*asin(sqrt(z))/(1-z)**1.5
    trunc = sum(float(a(k))*z**k for k in range(130))
    verify(abs(F-trunc) <= 2e-9)

print(f'PENTABLOCK_AXIAL_EXACT_CHECKS_OK {checks}')
