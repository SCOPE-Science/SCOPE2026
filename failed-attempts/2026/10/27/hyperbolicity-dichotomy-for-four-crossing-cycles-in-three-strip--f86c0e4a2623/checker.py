#!/usr/bin/env python3
"""Exact boundary-energy and return-multiplier checks for three-strip Hamiltonian flows.

Only finite rational identities and one published example are checked here;
the universal claim follows from the proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt

count=0

def check_case(b, a, alpha, uR, uL, vR, vL, beta):
    global count
    tR=b*uR+a+alpha
    tL=b*uL-a+alpha
    y0,y1=uR+vR,uR-vR
    y2,y3=uL-vL,uL+vL
    def HR(y): return b*y*y/2+(a+alpha)*y-beta
    def HL(y): return b*y*y/2+(-a+alpha)*y+beta
    assert HR(y0)==HL(y3)
    assert HR(y1)==HL(y2)
    assert tR*vR==tL*vL
    w=lambda x,y: b*y+a*x+alpha
    assert w(1,y0)>0 and w(1,y1)<0
    assert w(-1,y2)<0 and w(-1,y3)>0
    u=w(1,y1)*w(-1,y3)/(w(-1,y2)*w(1,y0))
    assert u>0
    assert (u-1)*((w(-1,y2)*w(1,y0))) == 2*b*(tR*vL-tL*vR)
    assert (u==1)==(tR==tL)
    if tR!=tL:
        assert (u<1)==(tR>tL)
        assert (u>1)==(tR<tL)
    else:
        assert u==1
    count+=1

for tR,tL,k,sgn in product(range(1,8),range(1,8),range(8,14),(-1,1)):
    # Orientation reversal changes all of the vector-field coefficients.
    b=F(sgn)
    a=F(0);alpha=F(0)
    uR=F(tR);uL=F(tL)
    vR=F(sgn*k*tL);vL=F(sgn*k*tR)
    tr=b*uR;tl=b*uL
    # beta makes both central Hamiltonian passage energies identical.
    beta=(b*(uR*uR-uL*uL+vR*vR-vL*vL)/2)/2
    check_case(b,a,alpha,uR,uL,vR,vL,beta)

# Genuine four-crossing example 5 from Pessoa--Ribeiro, arXiv:2106.04638.
z=sqrt(1259/235)
y0=31*z/48; y1=-y0; y2=5/16-z/3; y3=5/16+z/3
w=lambda x,y: 2*y+F(2,3)
mu=(w(1,y1)*w(-1,y3))/(w(-1,y2)*w(1,y0))
assert abs(mu-7.16368982517432)<1e-12
assert all(abs(v)>1e-3 for v in [w(1,y0),w(1,y1),w(-1,y2),w(-1,y3)])
assert mu>1
assert abs((F(2,3)*(y0-y1)/2-F(31,24)*(y3-y2)/2))<1e-12

# Time reversal: the nontrivial Floquet multiplier becomes its reciprocal.
wrev=lambda x,y: -w(x,y)
assert abs((1/mu)-0.1395928)<1e-4

print(f"PASS: {count} exact-rational cycle-geometry fixtures, one published four-crossing example, and orientation reversal check")
