#!/usr/bin/env python3
"""Independent finite Zak-series checks for exact Laplace-window frame bounds.

Only built-in Python libraries are required. Finite sampling cannot prove global extrema.
"""
import cmath
import math

def formulas(a,q):
    r=math.exp(-a)
    t=r**q
    H=sum(r**(2*j) for j in range(q))
    A=2*q*(r*H-q*t)/(1+t)**2
    B=q*((1+r*r)*H+2*q*t)/(1-t)**2
    return A,B

def direct_zak_multiplier(a,q,x,w,cut=100):
    vals=[math.exp(-a*abs(x+n)) for n in range(-cut,cut+1)]
    out=0.0
    for j in range(q):
        freq=w+j/q
        z=sum(v*cmath.exp(-2j*math.pi*n*freq) for n,v in zip(range(-cut,cut+1),vals))
        out+=abs(z)**2
    return out

counter=0
for a in (0.5,1.0,2.0):
    for q in (2,3,5):
        A,B=formulas(a,q)
        assert 0 < A <= B
        exa=direct_zak_multiplier(a,q,0.5,1/(2*q))
        exb=direct_zak_multiplier(a,q,0.,0.)
        assert math.isclose(exa,A,rel_tol=3e-11,abs_tol=3e-11),(a,q,exa,A)
        assert math.isclose(exb,B,rel_tol=3e-11,abs_tol=3e-11),(a,q,exb,B)
        counter+=2
        for x in (0.,0.17,0.5,0.73,1.):
            for w in (0.,0.09/q,0.3/q,0.5/q,0.7/q,1./q):
                phi=direct_zak_multiplier(a,q,x,w)
                assert A-3e-10<=phi<=B+3e-10,(a,q,x,w,phi,A,B)
                counter+=1
# Use a separate high-redundancy exact-rational expression to check the limit.
a=0.8
assert abs(formulas(a,80)[1]/formulas(a,80)[0]-math.cosh(a))<1e-11
counter+=1
print('TWO_SIDED_EXPONENTIAL_SHARP_GABOR_CHECKS_PASSED',counter)
