#!/usr/bin/env python3
"""Standalone exact-rational and floating-point checks for local PCHIP sensitivity.
All results are supplementary checks, not a substitute for the proof.
"""
from fractions import Fraction as F
from random import Random
from math import sqrt


def q(a,b):
    return 3*b*(a+b)/(a*(a+2*b))

def H(A,B,al,be):
    if A<=0 or B<=0: return F(0)
    return A*B/(al*B+be*A)

def hermite(a,b,c,y,t):
    alpha=(a+2*b)/(3*(a+b)); beta=1-alpha
    alpha2=(b+2*c)/(3*(b+c)); beta2=1-alpha2
    A=(y[1]-y[0])/a; B=(y[2]-y[1])/b; C=(y[3]-y[2])/c
    d0=H(A,B,alpha,beta); d1=H(B,C,alpha2,beta2)
    s=t*t*(3-2*t)
    u=t*(1-t)*(1-t)
    v=t*t*(1-t)
    return y[1]+(y[2]-y[1])*s+b*u*d0-b*v*d1

def point_bound(a,b,c,t):
    return 1+2*t*(1-t)*(q(a,b)*(1-t)+q(c,b)*t)

def global_bound(a,b,c):
    u=float(q(a,b)); v=float(q(c,b))
    if abs(v-u)<1e-12: t=.5
    else:t=(v-2*u+sqrt(u*u-u*v+v*v))/(3*(v-u))
    return 1+2*t*(1-t)*(u*(1-t)+v*t),t

def test():
    rng=Random(20261120)
    n=1200
    for i in range(n):
        a,b,c=(F(rng.randint(1,12),rng.randint(1,8)) for _ in range(3))
        t=F(rng.randint(0,100),100)
        yy=[F(rng.randint(-10,10))]
        for _ in range(3): yy.append(yy[-1]+F(rng.randint(0,20),rng.randint(1,10)))
        zz=[F(rng.randint(-10,10))]
        for _ in range(3): zz.append(zz[-1]+F(rng.randint(0,20),rng.randint(1,10)))
        delta=max(abs(u-v) for u,v in zip(yy,zz))
        assert abs(hermite(a,b,c,yy,t)-hermite(a,b,c,zz,t))<=point_bound(a,b,c,t)*delta
        # interpolation has its own range preservation for monotone data
        assert yy[1]<=hermite(a,b,c,yy,t)<=yy[2]
    # exact midpoint uniform and graded values
    assert global_bound(1.,1.,1.)[0]==2
    assert global_bound(1.,2.,1.)[0]==2.8
    assert point_bound(F(1),F(2),F(1),F(1,2))==F(14,5)
    # all gradients have the specified signed pattern, checked exactly
    for i in range(1000):
        a,b,c=(F(rng.randint(1,14),rng.randint(1,10)) for _ in range(3))
        A,B,C=(F(rng.randint(1,17),rng.randint(1,9)) for _ in range(3))
        t=F(rng.randint(1,99),100)
        al=(a+2*b)/(3*(a+b));be=1-al
        al2=(b+2*c)/(3*(b+c));be2=1-al2
        HA=al*B*B/(al*B+be*A)**2
        HB=be*A*A/(al*B+be*A)**2
        HB2=al2*C*C/(al2*C+be2*B)**2
        HC2=be2*B*B/(al2*C+be2*B)**2
        s=t*t*(3-2*t);u=t*(1-t)**2;v=t*t*(1-t)
        partials=[-b*u/a*HA,1-s+b*u/a*HA-u*HB+v*HB2,s+u*HB-v*HB2+b*v/c*HC2,-b*v/c*HC2]
        assert partials[0]<=0 and partials[1]>=0 and partials[2]>=0 and partials[3]<=0
        assert sum(partials)==1
        assert sum(abs(x) for x in partials)<=point_bound(a,b,c,t)
    # a concrete strict-monotonicity witness approaching the sharp norm
    for a,b,c in [(F(1),F(1),F(1)),(F(1),F(2),F(1)),(F(1,10),F(1),F(1))]:
        K,t0=global_bound(float(a),float(b),float(c))
        t=F(round(t0*100000),100000)
        gap=F(1,10000)
        y=[F(0),gap,gap+b,gap+b+gap]
        eps=F(1,10**8)
        z=[y[0]-eps,y[1]+eps,y[2]+eps,y[3]-eps]
        assert all(z[k]<=z[k+1] for k in range(3))
        gain=abs(hermite(a,b,c,z,t)-hermite(a,b,c,y,t))/eps
        assert float(gain)>K-0.01,(a,b,c,gain,K)
    # balancing a+c at fixed b reduces K uniquely; random tested
    for _ in range(300):
        b=float(F(rng.randint(1,25),rng.randint(1,12)))
        total=float(F(rng.randint(1,30),rng.randint(1,9)))
        a=float(F(rng.randint(1,99),100))*total;c=total-a
        K,_=global_bound(a,b,c)
        symmetric,_=global_bound(total/2,b,total/2)
        assert K>=symmetric-1e-12
    print('PASS: 1200 exact-rational two-input range and Lipschitz checks, 1000 exact Jacobian checks, 3 sharpness witnesses, 300 balancing comparisons; exact graded values 2 and 14/5')
if __name__=='__main__':test()
