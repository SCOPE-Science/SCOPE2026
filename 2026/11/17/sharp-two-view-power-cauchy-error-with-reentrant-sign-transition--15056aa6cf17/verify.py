"""Numerical cross-checks for the two-view power-cosine theorem.

Proof is analytic; this program is a reproducible finite check only.
Python 3 standard library; run `python verify.py`.
"""
from math import pi, sin, cos, sqrt, exp, lgamma, isclose
from random import Random


def c(p):
    return exp(lgamma((p+1.0)/2.0)-lgamma((p+2.0)/2.0))/sqrt(pi)


def potential(p,theta,phi,w):
    return w*abs(cos(theta))**p+(1-w)*abs(cos(theta-phi))**p


def target(p):
    return max(.5-c(p),c(p)-2.0**(-p/2.0))

checks=0
for p in (2.,2.2,3.,3.9,4.,4.2,4.9,5.8,6.,6.2,7.,8.,11.,16.):
    # Independent midpoint quadrature for the normalized circular average.
    samples=8192
    integral=sum(abs(cos(pi*(j+.5)/samples))**p for j in range(samples))/samples
    assert abs(integral-c(p))<2e-7,(p,integral,c(p))
    checks+=1
    # For the proposed equal orthogonal rule, compute the entire angular range.
    vals=[potential(p,(pi/2)*j/2048,pi/2,.5) for j in range(2049)]
    assert abs(max(vals)-.5)<1e-12
    assert abs(min(vals)-2**(-p/2))<1e-12
    assert abs(max(abs(v-c(p)) for v in vals)-target(p))<1e-12
    checks+=3

for p,expected_sign in ((3.,-1),(4.5,1),(5.,1),(7.,-1),(10.,-1)):
    h=2*c(p)-.5-2**(-p/2)
    assert h*expected_sign>1e-6
    checks+=1
for p in (2.,4.,6.):
    assert abs(2*c(p)-.5-2**(-p/2))<1e-12
    checks+=1

rng=Random(190226)
for p in (2.1,3.4,4.6,5.5,7.2,12.0):
    for _ in range(400):
        phi=rng.random()*pi
        w=1e-7+(1-2e-7)*rng.random()
        a=max(potential(p,0.,phi,w),potential(p,phi,phi,w))
        # Midpoint of the larger *projective-circle* empty gap.
        mid=phi/2 if phi>=pi/2 else (phi+pi)/2
        b=potential(p,mid,phi,w)
        assert a>=.5-1e-12
        assert b<=2**(-p/2)+1e-12
        err=max(abs(a-c(p)),abs(b-c(p)))
        assert err>=target(p)-1e-12,(p,phi,w,err,target(p))
        checks+=3
print('PASS:',checks,'deterministic numerical comparisons')
print('Exact proof covers all real p>=2, positive weights, and all projective two-node rules.')
