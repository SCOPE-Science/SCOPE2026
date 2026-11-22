"""Supplementary exact arithmetic and numerical diagnostics for the three-pole Gabor window.

The analytic proof of the all-parameter phase diagram appears in RESULT.md.
This script checks algebraic identities and samples the Zak multiplier; finite
sampling is not a proof of zero-freeness.
"""
from fractions import Fraction as F
from math import pi, log, sqrt, isclose
from cmath import exp

A, B, C, q = F(4, 5), F(1, 5), F(1, 20), F(1, 4)
p, v, u, w = F(1)-A, F(1)-B, F(1)-C, F(1)+B
assert v/p == 4 and v/u == F(16, 19)
assert w/(1+A) == F(2, 3) and w/(1+C) == F(8, 7)
assert ((1+C)/(1+A))**2 == F(49,144)
assert (B-C)/(A-B) == F(1,4)
assert F(49,144)>F(1,4)
assert 4+F(16,19) == F(92,19)
assert 4/q+F(16,19)*q == F(308,19)
assert F(2,3)/q+F(8,7)*q == F(62,21)
assert F(62,21)<F(92,19)
assert F(7,12)>q*q
lmin = 8/sqrt(21)
assert isclose(lmin,2*sqrt((2/3)*(8/7)),rel_tol=1e-14)

def z_multiplier(lam, x, omega):
    s=float(q)**omega
    z=exp(2j*pi*x)
    return 1/(1-float(A)*z)-lam*s/(1-float(B)*z)+s*s/(1-float(C)*z)

def lambda_curve(x, omega):
    s=float(q)**omega
    z=exp(2j*pi*x)
    return ((1-float(B)*z)/(1-float(A)*z)/s
           +s*(1-float(B)*z)/(1-float(C)*z))

checks=0
for j in range(1,39):
    omega=j/39
    s=float(q)**omega
    for x in (0, .5):
        val=lambda_curve(x,omega)
        assert abs(val.imag)<1e-12
        expected=(4/s+16*s/19) if x==0 else (2/(3*s)+8*s/7)
        assert abs(val.real-expected)<1e-11
        assert abs(z_multiplier(val.real,x,omega))<1e-11
        checks+=3
    # No interior angular zero for a real coefficient.
    for k in range(1,39):
        x=k/78
        val=lambda_curve(x,omega)
        assert abs(val.imag)>1e-5
        checks+=1

# The critical inner-band minimum occurs at s=sqrt(7/12).
sstar=sqrt(7/12)
omegastar=log(sstar)/log(float(q))
assert 0<omegastar<1
assert abs(z_multiplier(lmin,.5,omegastar))<1e-12
checks+=2

# Verify directly that each sample in each stable phase has a separated Zak multiplier.
for lam in (-2,0,1,3.5,4.0,18):
    m=min(abs(z_multiplier(lam,j/80,k/80)) for j in range(80) for k in range(1,80))
    assert m>1e-3, (lam,m)
    checks+=1

print('PASS:',checks,'supplementary algebraic and finite-sample checks')
print('forbidden:',(lmin,float(F(62,21))),(float(F(92,19)),float(F(308,19))))
