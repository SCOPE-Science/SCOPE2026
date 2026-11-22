#!/usr/bin/env python3
"""Independent numerical checks of exact two-opportunity restoration phase diagram.
The analytical proof rests on a quadratic identity, not this finite testing.
"""
import math
import random

def prob(k, rate, T, t):
    def p(u):
        x=math.exp(-rate*u)
        return k*x*(1-x)
    return 1-(1-p(t))*(1-p(T-t))

def thresholds(k,rate):
    assert 0<k<=4 and rate>0
    L=(2/rate)*math.log(2+math.sqrt(4-k))
    if k<=3:return (None,None,L)
    E=math.log(k-2)/rate
    U=(2/rate)*math.log(2-math.sqrt(4-k))
    return (E,U,L)

def candidates(k,rate,T):
    q=math.exp(-rate*T)
    lo=2*math.sqrt(q)
    hi=1+q
    s0=(1+k*q)/2
    s=min(hi,max(lo,s0))
    disc=max(0,s*s-4*q)
    x=(s+math.sqrt(disc))/2
    # The smaller gap corresponds to the larger x.
    t=-math.log(x)/rate
    return s,(t,T-t)

def checks():
    rng=random.Random(4403)
    n=0
    for k in [0.01,0.2,0.8,1,2,2.99,3,3.0001,3.1,3.5,3.99,4]:
        E,U,L=thresholds(k,1)
        if E is not None:
            assert 0<E<=U<=L
        for T in [0.01,0.1,.5,1,2,3,5,10,L*0.999,L,L*1.001]+ ([E*.999,E,E*1.001,U*.999,U,U*1.001] if E is not None else []):
            if T<=0:continue
            q=math.exp(-T)
            s,ts=candidates(k,1,T)
            assert all(-1e-12<=v<=T+1e-12 for v in ts)
            optimum=prob(k,1,T,ts[0])
            for i in range(151):
                t=T*i/150
                assert prob(k,1,T,t)<=optimum+1e-12,(k,T,t,optimum)
                n+=1
            x=math.exp(-ts[0]); y=math.exp(-ts[1]);
            assert abs(x*y-q)<3e-12
            assert abs(x+y-s)<3e-12
            n+=2
    for i in range(90000):
        k=rng.uniform(.001,4)
        T=rng.uniform(.015,20)
        t=rng.uniform(0,T)
        rate=rng.uniform(.1,6)
        q=math.exp(-rate*T)
        x=math.exp(-rate*t);y=math.exp(-rate*(T-t))
        s=x+y
        lhs=(1-k*x+k*x*x)*(1-k*y+k*y*y)
        rhs=k*s*s-k*(1+k*q)*s+1+(k*k-2*k)*q+k*k*q*q
        assert abs(lhs-rhs)<2e-12,(lhs,rhs,k,T)
        sstar,ts=candidates(k,rate,T)
        assert prob(k,rate,T,ts[0])>=prob(k,rate,T,t)-2e-12
        n+=2
    return n

if __name__=='__main__':
    print('ASSERTIONS_PASSED',checks())
