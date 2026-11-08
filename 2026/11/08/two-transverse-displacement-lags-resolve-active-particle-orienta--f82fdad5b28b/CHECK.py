#!/usr/bin/env python3
"""Independent finite-arithmetic diagnostics for finite-lag active-particle inversion.

The universal mathematical claims are established in the accompanying proof;
these tests replay forward formulas and inverse numerics on selected inputs.
Requires only Python 3 standard library.
"""
import math
import random
from fractions import Fraction as F


def H(rate, t):
    z = rate*t
    if abs(z) < 0.0001:
        s = 0.0
        # H = t^2 * sum_{n=0}^inf (-z)^n/(n+2)!
        term = 0.5
        s = term
        for n in range(1, 14):
            term *= -z/(n+2)
            s += term
        return t*t*s
    return (math.expm1(-z)+z)/(rate*rate)


def ratio(rate, t1, t2):
    return H(rate,t2)/H(rate,t1)


def recover_rate(R,t1,t2):
    lo=0.0
    hi=1.0
    for k in range(200):
        if ratio(hi,t1,t2)<R: break
        hi*=2
    else: raise AssertionError('failed to bracket relaxation rate')
    for k in range(90):
        mid=(lo+hi)/2
        if ratio(mid,t1,t2)>R: lo=mid
        else: hi=mid
    return (lo+hi)/2


def g(z):
    return (1+z)**2/(z*z*(4+z))


def recover_z(target):
    lo=0.0
    hi=1.0
    while g(hi)>target:
        hi*=2
    for k in range(90):
        mid=(lo+hi)/2
        if g(mid)>target: lo=mid
        else: hi=mid
    return (lo+hi)/2


def h(z):
    return (2+5*z)/(2*(1+z)**2)


def forward(v,r,d,D,t):
    z=r/d
    lam=r+d
    u=v*z/(1+z)
    ay=4*v*v/(z+4)*H(lam,t)
    ax=ay*h(z)
    return u,2*D*t+ax,2*D*t+ay


def inverse(u,variance_y1,variance_y2,D,t1,t2):
    a1=variance_y1-2*D*t1
    a2=variance_y2-2*D*t2
    assert u>0 and a1>0 and a2>0
    rate=recover_rate(a2/a1,t1,t2)
    z=recover_z(a1/(4*u*u*H(rate,t1)))
    v=u*(1+z)/z
    d=rate/(1+z)
    r=rate*z/(1+z)
    return v,r,d


def close(a,b,rel=3e-9):
    assert abs(a-b)<=rel*max(1,abs(a),abs(b)),(a,b)


def main():
    count=0
    # Exact algebra in the published-forward anisotropy quotient.
    z1=F(2,13); z2=F(1,4)
    assert (2+5*z1)/(2*(1+z1)**2)==F(26,25);count+=1
    assert (2+5*z2)/(2*(1+z2)**2)==F(26,25);count+=1
    assert (1+z1)**2/(z1*z1*(z1+4))==F(325,24);count+=1
    assert (1+z2)**2/(z2*z2*(z2+4))==F(100,17);count+=1
    assert (2+5*F(1,5))/(2*(1+F(1,5))**2)==F(25,24);count+=1
    # Exact one-lag ambiguity: both physical parameter triples give
    # u=1, thermal-excess Ay=1 and Ax=26/25 at t=1, D=1.
    for z, target in [(float(z1),6/325),(float(z2),17/400)]:
        lo=1e-9; hi=1000
        for _ in range(100):
            mid=(lo+hi)/2
            if H(mid,1)>target: lo=mid
            else: hi=mid
        lam=(lo+hi)/2
        v=(1+z)/z
        r=lam*z/(1+z);d=lam/(1+z)
        u,ax,ay=forward(v,r,d,1,1)
        close(u,1);close(ay,3);close(ax,F(76,25));count+=3
    # The finite-lag ratio maps positive rates onto the predicted interval.
    for t1,t2 in [(0.1,0.3),(0.4,1.3),(1,2),(1,10)]:
        old=None
        for lam in [0.00001,0.001,0.1,1,10,100,1000]:
            value=ratio(lam,t1,t2)
            assert t2/t1<value<(t2/t1)**2,(lam,t1,t2,value)
            count+=1
            if old is not None:
                assert value<old
                count+=1
            old=value
    rng=random.Random(20261101)
    for _ in range(200):
        v=math.exp(rng.uniform(-1.5,2))
        r=math.exp(rng.uniform(-1.5,1.8))
        d=math.exp(rng.uniform(-1.5,1.8))
        D=math.exp(rng.uniform(-2,1))
        t1=math.exp(rng.uniform(-2,0))
        t2=t1*math.exp(rng.uniform(.1,1))
        u,ax1,ay1=forward(v,r,d,D,t1)
        _,ax2,ay2=forward(v,r,d,D,t2)
        v2,r2,d2=inverse(u,ay1,ay2,D,t1,t2)
        close(v,v2,rel=1e-7);close(r,r2,rel=1e-7);close(d,d2,rel=1e-7)
        close((ax1-2*D*t1)/(ay1-2*D*t1),h(r/d))
        close((ax2-2*D*t2)/(ay2-2*D*t2),h(r/d))
        count+=5
    print('PASS:',count,'exact/numerical assertions')


if __name__=='__main__':
    main()
