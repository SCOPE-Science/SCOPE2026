#!/usr/bin/env python3
"""Supplementary numeric tests of idealized hybrid-sampler inversion.
Only the analytic argument in RESULT.md proves the universal statements.
"""
import math, random


def exprel(z):
    if abs(z)<1e-5:
        return 1+z*(.5+z*(1/6+z*(1/24+z*(1/120+z/720))))
    return math.expm1(z)/z


def record(lam,delta,k,c0,d):
    a=math.exp(-lam*d); b=math.exp(-delta*d)
    y1=k*c0*d*a*exprel((lam-delta)*d)
    y2=y1*(a+b)
    y3=y1*(a*a+a*b+b*b)
    x1=c0*a; x2=x1*a
    return x1,x2,y1,y2,y3


def inv_known(k,d,x1,y1,y2):
    target=y1/(k*d*x1)
    lo,hi=-60.,60.
    for _ in range(140):
        mid=(lo+hi)/2
        if exprel(mid)<target: lo=mid
        else:hi=mid
    w=(lo+hi)/2
    u=math.exp(w)
    a=(y2/y1)/(1+u)
    b=a*u
    return -math.log(a)/d, -math.log(b)/d, x1/a


def inv_unknown(d,x1,x2,y1,y2):
    a=x2/x1
    b=y2/y1-a
    lam=-math.log(a)/d
    delta=-math.log(b)/d
    c0=x1/a
    k=y1/(d*x1*exprel((lam-delta)*d))
    return lam,delta,k,c0


def verify():
    rng=random.Random(202611170823)
    checks=0
    for j in range(10000):
        d=rng.uniform(0.12,1.2)
        lam=rng.uniform(.1,3)
        delta=rng.uniform(.1,3)
        if j%4==0: delta=lam
        elif j%4==1:delta=lam+(rng.random()-.5)*1e-5
        k=math.exp(rng.uniform(-2,2))
        c0=math.exp(rng.uniform(-2,2))
        x1,x2,y1,y2,y3=record(lam,delta,k,c0,d)
        lk,dk,ck=inv_known(k,d,x1,y1,y2)
        lu,du,ku,cu=inv_unknown(d,x1,x2,y1,y2)
        # Floating point inversion near coincident rates can magnify cancellation.
        for value,expect in ((lk,lam),(dk,delta),(ck,c0),
                             (lu,lam),(du,delta),(ku,k),(cu,c0)):
            assert abs(value-expect)<3e-8*max(1,expect),(j,value,expect)
            checks+=1
        # Three passive values recover the unordered two poles;
        # compare symmetric combinations, which are well-conditioned.
        s=y2/y1; p=s*s-y3/y1
        a=math.exp(-lam*d); b=math.exp(-delta*d)
        assert abs(s-(a+b))<2e-12
        assert abs(p-a*b)<2e-12
        checks+=2
        # Swapped rates with same product k*C0 have exactly the same passive curve.
        yy=record(delta,lam,k,c0,d)
        assert abs(yy[2]-y1)<2e-12
        assert abs(yy[3]-y2)<2e-12
        assert abs(yy[4]-y3)<2e-12
        checks+=3
    # For any positive rates and a single active sample, adjustable gain
    # cannot break the rate permutation for passive observations.
    for _ in range(4000):
        d=rng.uniform(.1,1.8); lam=rng.uniform(.2,3);delta=rng.uniform(.2,3)
        k=rng.uniform(.1,3); c0=rng.uniform(.1,5)
        x1,_,y1,y2,y3=record(lam,delta,k,c0,d)
        new_c0=x1/math.exp(-delta*d)
        new_k=k*c0/new_c0
        xx1,_,z1,z2,z3=record(delta,lam,new_k,new_c0,d)
        assert abs(x1-xx1)<2e-12
        assert max(abs(y1-z1),abs(y2-z2),abs(y3-z3))<2e-12
        checks+=2
    # Quadratic near-collision indistinguishability of passive signals.
    for eps in [1e-1,1e-2,1e-3,1e-4]:
        d=1.; r=1.; k=2.; c0=3.
        vals=record(r+eps,r-eps,k,c0,d)
        base=record(r,r,k,c0,d)
        error=max(abs(vals[i]-base[i]) for i in (2,3,4))
        assert error<40*eps*eps
        assert abs(vals[0]-base[0])>.1*eps
        checks+=2
    return checks

if __name__=='__main__':
    print('SUPPLEMENTARY_ASSERTIONS_PASSED',verify())
