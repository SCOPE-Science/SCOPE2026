#!/usr/bin/env python3
"""Standalone numerical tests for a one-purge indoor/outdoor exposure theorem.
No third-party dependencies. Finite checks supplement, not replace, the analytic proof.
"""
import math
import random

def bisect(f,lo,hi,steps=90):
    flo=f(lo)
    fhi=f(hi)
    assert flo*fhi<=0,(lo,hi,flo,fhi)
    for _ in range(steps):
        mid=(lo+hi)/2
        if f(mid)*flo<=0: hi=mid
        else: lo=mid; flo=f(mid)
    return (lo+hi)/2

def onset(a,b,x):
    def d(t):return -math.expm1(-a*t)-x*math.exp(-b*t)
    right=1
    while d(right)<=0:right*=2
    return bisect(d,0,right)

def savings(a,b,x,u,eta,T,t):
    d=-math.expm1(-a*t)-x*math.exp(-b*t)
    return eta*u/a*(-math.expm1(-a*(T-t)))*d

def optimizer(a,b,x,T):
    t0=onset(a,b,x)
    if T<=t0:return t0,T
    def g(t):
        d=-math.expm1(-a*t)-x*math.exp(-b*t)
        dp=a*math.exp(-a*t)+x*b*math.exp(-b*t)
        return dp/d-a/math.expm1(a*(T-t))
    return t0,bisect(g,t0+max(1e-12,1e-12/a),T-max(1e-12,1e-12/a))

def exact_exposure(a,b,x,u,eta,T,t):
    # Directly integrate the exact piecewise ODE solutions, independently
    # of the closed-form savings formula.
    # c_off(v)=u*(1-exp(-a*v)); c_out(v)=u*x*exp(-b*v)
    def integral_off(z):return u*(z+math.expm1(-a*z)/a)
    pre=integral_off(t)
    c_before=u*(-math.expm1(-a*t))
    c_after=(1-eta)*c_before+eta*u*x*math.exp(-b*t)
    rem=T-t
    after=u*rem+(c_after-u)*(-math.expm1(-a*rem))/a
    return pre+after

def check(seed=2048):
    rng=random.Random(seed)
    n=0
    for _ in range(1500):
        a=10**rng.uniform(-0.6,0.6)
        b=10**rng.uniform(-0.7,0.7)
        x=10**rng.uniform(-1.2,1.2)
        u=10**rng.uniform(-1,1.5)
        eta=rng.uniform(0.03,0.95)
        t0=onset(a,b,x)
        T=t0+rng.uniform(0.01,12)/a
        _,t=optimizer(a,b,x,T)
        assert t0<t<T and t>=T/2-1e-9*max(1,T),(a,b,x,T,t0,t)
        v=savings(a,b,x,u,eta,T,t)
        assert v>0
        # Interior unique optimum: all sampled alternatives lose or tie only due to FP.
        for j in range(0,61):
            w=savings(a,b,x,u,eta,T,j*T/60)
            assert v>=w-1e-9*max(1,abs(v)),(a,b,x,T,t,w,v)
            n+=1
        off=u*(T+math.expm1(-a*T)/a)
        direct=exact_exposure(a,b,x,u,eta,T,t)
        assert abs((off-direct)-v)<1e-9*max(1,abs(v),abs(off)),(off,direct,v)
        n+=1
        # At/under threshold, no positive benefit.
        H=t0*rng.uniform(.02,.99)
        for j in range(0,8):
            assert savings(a,b,x,u,eta,H,H*j/7)<=1e-9
            n+=1
        # Optimal time increases with horizon, but less than 1-to-1.
        _,tnew=optimizer(a,b,x,T+.01/a)
        assert t<tnew<t+.01/a+1e-8
        n+=1
    # At equal relaxation rates the optimum and benefit are exactly explicit.
    for _ in range(1000):
        a=10**rng.uniform(-1,1); x=10**rng.uniform(-1,1)
        T=math.log1p(x)/a+rng.uniform(.1,20)/a
        eta=.4;u=2.0
        _,t=optimizer(a,a,x,T)
        known=(T+math.log1p(x)/a)/2
        assert abs(t-known)<1e-9*max(1,T), (t,known)
        known_v=eta*u/a*(1-math.sqrt((1+x)*math.exp(-a*T)))**2
        assert abs(savings(a,a,x,u,eta,T,t)-known_v)<1e-8
        n+=2
    # Local quadratic onset law from an independent small-horizon test.
    for b in [.3, 1., 3.]:
        a=1.;x=.7;u=2.;eta=.4
        t0=onset(a,b,x)
        dprime=a*math.exp(-a*t0)+x*b*math.exp(-b*t0)
        for eps in [1e-2, 5e-3, 1e-3]:
            H=t0+eps
            _,tau=optimizer(a,b,x,H)
            assert abs((tau-t0)/eps-.5)<.01,(b,eps,tau)
            actual=savings(a,b,x,u,eta,H,tau)
            lead=eta*u*dprime*eps*eps/4
            assert abs(actual/lead-1)<.01,(actual,lead)
            n+=2
    # Long-horizon three-regime asymptotic, direct root versus claimed offset.
    for b in [0.25,0.6,1.,1.5,2.,4.]:
        a=1.;x=.7;T=100.
        _,t=optimizer(a,b,x,T)
        if b<a:m=b;C=x
        elif b==a:m=a;C=1+x
        else:m=a;C=1.
        approx=a/(a+m)*T+math.log(m*C/a)/(a+m)
        assert abs(t-approx)<1e-6,(b,t,approx)
        n+=1
    print(f'PASS {n} numerical assertions; 1500 varied parameter cases, 1000 equal-rate cases, 6 asymptotic cases')

if __name__=='__main__':check()
