"""Exact rational witness and deterministic finite checks for ideal Planck-band inversion.

This is a supplement to, not a substitute for, the symbolic theorem.
"""
from fractions import Fraction as F
from math import sqrt
import random


def recover(s, y1, y2, y3):
    R = (y2-y1)/(y3-y2)
    assert 0 < R < 2*s*(s+1)/(s*s+1)
    t = ((s+1) + sqrt((s+1)**2 + 4*R*(s*(s+1)-R)))/(2*R)
    r2 = (s*s-1)/(t*t-1)
    r3 = (s-1)/(t-1)
    beta = (y3-y2)/(r3-r2)
    alpha = y2 - beta*r2
    return t, beta/(alpha+beta), 1/(alpha+beta), alpha, beta, R


def ratios(s, t):
    return [(s**k-1)/(t**k-1) for k in (4, 2, 1)]


# Exact rational witness: no rounding in this block.
s,t=F(2),F(3)
f,delta=F(1,4),F(1,100)
r=ratios(s,t)
y=[(1-f+f*ri)/delta for ri in r]
assert r==[F(3,16),F(3,8),F(1,2)]
assert y==[F(1275,16),F(675,8),F(175,2)]
R=(y[1]-y[0])/(y[2]-y[1]); assert R==F(3,2)
assert (s+1)*(s+t)/(t*t+1)==R
assert R*t*t-(s+1)*t+R-s*(s+1)==0
beta=(y[2]-y[1])/(r[2]-r[1]); alpha=y[1]-beta*r[1]
assert (alpha,beta)==(F(75),F(25))
assert (beta/(alpha+beta),1/(alpha+beta))==(f,delta)
assert alpha>1 and 0<f<1 and 0<delta<1-f

rng=random.Random(20261120)
num=12000
for k in range(num):
    s=1.1+4*rng.random()
    t=s+0.03+5*rng.random()
    f=0.02+0.96*rng.random()
    delta=(1-f)*(0.01+0.75*rng.random())
    r=ratios(s,t)
    y=[(1-f+f*ri)/delta for ri in r]
    t1,f1,d1,a,b,R=recover(s,*y)
    assert y[0]<y[1]<y[2] and a>1 and b>0
    assert abs(t1-t)/t<1e-9
    assert abs(f1-f)<1e-9
    assert abs(d1-delta)<1e-9
    assert 1-t*t-2*s*t<0  # numerator of F_s'(t)
    if k < 1500:
        # Two-band observation has another physical solution at nearby t.
        tt=t*(1+1e-5)
        rr=ratios(s,tt)
        bb=(y[2]-y[1])/(rr[2]-rr[1])
        aa=y[1]-bb*rr[1]
        ff=bb/(aa+bb); dd=1/(aa+bb)
        assert aa>1 and bb>0 and 0<ff<1 and 0<dd<1-ff
        assert abs(aa+bb*rr[1]-y[1])<1e-9
        assert abs(aa+bb*rr[2]-y[2])<1e-9
        assert abs(tt-t)>0
print('PASS rational witness,',num,'interior inversions, 1500 distinct two-band physical alternatives')
