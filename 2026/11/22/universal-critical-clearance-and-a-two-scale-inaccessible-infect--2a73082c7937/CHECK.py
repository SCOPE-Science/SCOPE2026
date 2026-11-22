#!/usr/bin/env python3
"""Standalone numerical and rational corroboration of a six-state critical SIRA theorem.

Requires only Python's standard library. This checker is not a proof of the
universal limits; see the companion analytical derivation.
"""
from fractions import Fraction as F
from math import isfinite

G=M=K1=K2=D1=D2=RHO=OMEGA=F(1)
K=G+M
Q=K*(K/M+(RHO/OMEGA)*((M+K1)/(M+K2)+D1/(D2+K)))
assert Q==F(20,3)
assert 1/Q==F(3,20)
assert D1*RHO/(OMEGA*(D2+K)*Q*Q)==F(3,400)

def deriv(y):
    su,ia,iu,rec,a=y
    sa=1-su-ia-iu-rec
    return (
        a+ a*sa-(1-a)*su-su,
        2*sa*ia-a*ia+(1-a)*iu-2*ia,
        a*ia-(1-a)*iu-2*iu,
        ia+iu-rec,
        (ia+iu)*(1-a)-a,
    )

y=(0.,0.05,0.,0.,0.)
for i in range(50000):
    h=0.2
    k1=deriv(y)
    k2=deriv(tuple(x+h*z/2 for x,z in zip(y,k1)))
    k3=deriv(tuple(x+h*z/2 for x,z in zip(y,k2)))
    k4=deriv(tuple(x+h*z for x,z in zip(y,k3)))
    y=tuple(x+h*(u+2*v+2*w+z)/6 for x,u,v,w,z in zip(y,k1,k2,k3,k4))
    if i%1000==0:
        su,ia,iu,rec,a=y
        sa=1-su-ia-iu-rec
        assert min(y)>-1e-9 and sa>0 and a<1
        assert abs((deriv(y)[1]+deriv(y)[2]) + 2*((1-sa)*ia+iu))<2e-12
su,ia,iu,rec,a=y
t=10000.
assert abs(t*(ia+iu)-0.15)<.002
assert abs(t*su-0.15)<.002
assert abs(t*rec-0.15)<.002
assert abs(t*a-0.15)<.002
assert abs(t*t*iu-0.0075)<.0002
print('PASS: exact rational coefficients, pointwise identities and numerical tail')
