#!/usr/bin/env python3
"""Reproducibility checks for sharp half-density triangular Gabor frame bounds.

No non-standard dependencies. These finite checks corroborate but do not replace the analytical proof.
"""
from fractions import Fraction as Q
from math import sqrt, pi
from cmath import exp
import random


def g(t):
    return max(0.0, 1.0 - abs(t))


def predicted(b):
    b0 = 2-sqrt(10)/4
    b1 = (19-sqrt(10))/12
    if b <= b0:
        low = 1/(2*b**3)
    elif b <= b1:
        low = 4*(2-b)**2/(5*b**3)
    else:
        low = (7-4*b)**2/(8*b**3)
    return low, ((3*b-2)**2+(2*b-1)**2)/b**3


def fiber(b,y,phase):
    # Here y is in [0,a], the physical variable; the Zak step is 1/b=2a.
    a = 1/(2*b)
    z = exp(2j*pi*phase)
    s = sum(g(y-2*a*k)*z**k for k in range(-5,6))
    t = sum(g(y+a-2*a*k)*z**k for k in range(-5,6))
    return (abs(s)**2+abs(t)**2)/b


def exact_E(a,y):
    u = 1-2*a
    return 2*a-2*y-max(0,u-y)


def exact_low_y(a,y):
    return (exact_E(a,y)**2+exact_E(a,a-y)**2)/(1/(2*a))


def exact_hi_y(a,y):
    u,v=1-2*a,3*a-1
    return ((2-2*a+max(0,u-y))**2+(2-2*a+max(0,y-v))**2)/(1/(2*a))


def run():
    rng = random.Random(19370816)
    checks=0
    # All comparisons of the Zak fiber formula and the exact fixed-phase envelopes.
    for n in range(1,41):
        b = 1+n/80
        a = 1/(2*b)
        amin,bmax = predicted(b)
        assert bmax>=amin>0
        checks+=1
        ycenter = a/2
        yoff=(a+1)/5
        ystar= ycenter if b<=2-sqrt(10)/4 or b>=(19-sqrt(10))/12 else yoff
        assert abs(fiber(b,ystar,.5)-amin)<2e-12
        assert abs(fiber(b,0,0)-bmax)<2e-12
        checks+=2
        for k in range(101):
            y = a*k/100
            lo = exact_low_y(a,y)
            hi = exact_hi_y(a,y)
            assert abs(fiber(b,y,.5)-lo)<5e-12, (b,y,'lo',fiber(b,y,.5),lo)
            assert abs(fiber(b,y,0)-hi)<5e-12, (b,y,'hi',fiber(b,y,0),hi)
            assert lo >= amin-1e-10
            assert hi <= bmax+1e-10
            checks+=4
        for _ in range(15):
            y = rng.random()*a
            phase = rng.random()
            f = fiber(b,y,phase)
            lo = exact_low_y(a,y)
            hi = exact_hi_y(a,y)
            assert lo-1e-10 <= f <= hi+1e-10
            checks+=1
    # Exact rational arithmetic checks for boundary dominance and both polynomial expansions.
    for j in range(1,41):
        b=Q(1,1)+Q(j,80)
        a=1/(2*b)
        u,v=1-2*a,3*a-1
        for k in range(0,21):
            y=a*Q(k,20)
            ce=(u-y) if (u-y)>0 else Q(0)
            c0=1-y; c1=u+y
            d0=1-a-y; d1=1-a+y
            d2=y-v if y-v>0 else Q(0)
            assert c0>=ce+c1 and d1>=d0+d2
            assert c0-ce-c1 == 2*a-2*y-ce
            assert d1-d0-d2 == 2*y-d2
            checks+=4
    b0=2-sqrt(10)/4
    b1=(19-sqrt(10))/12
    def middle(b):return 4*(2-b)**2/(5*b**3)
    assert abs(1/(2*b0**3)-middle(b0))<1e-13
    assert abs(middle(b1)-(7-4*b1)**2/(8*b1**3))<1e-13
    checks+=2
    print('HAT_SPLINE_EXACT_BOUNDS_CHECKS_PASS',checks)

if __name__=='__main__':run()
