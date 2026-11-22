#!/usr/bin/env python3
"""Reproducibility checks for an idealized event-interception scheduling theorem.

Uses only the Python standard library; numerical checks supplement, but do not
replace, the analytic proof stated in RESULT.md.
"""
import math
import random

def survival_exp(t, rate=1.0):
    return math.exp(-rate*t)

def truncated_mean_exp(g, rate=1.0):
    return -math.expm1(-rate*g)/rate

def density_exp(t, rate=1.0):
    return rate*math.exp(-rate*t)

def Q(n, P, B, h, H):
    assert n >= 1 and n*h < B < P
    return (B-n*h+n*H(h+(P-B)/n))/P

def F(x, c, B, h, H):
    return B-h*x+x*H(h+c/x)

def Fprime(x, c, h, H, S):
    g=h+c/x
    return -h + H(g)-(g-h)*S(g)

def Fdoubleprime(x, c, h, f):
    return -c*c*f(h+c/x)/x**3

def delta(n, c, h, H):
    return -h+(n+1)*H(h+c/(n+1))-n*H(h+c/n)

def bisect_inc(fun, a, b, iterations=130):
    assert fun(a) < 0 < fun(b)
    for _ in range(iterations):
        mid=(a+b)/2
        if fun(mid)>0: b=mid
        else:a=mid
    return (a+b)/2

def verify():
    checks=0
    rng=random.Random(239188)
    S=lambda t:survival_exp(t)
    H=lambda t:truncated_mean_exp(t)
    f=lambda t:density_exp(t)
    # Probe full count phase structure for multiple costs and resource totals.
    for h in [0.04,0.13,0.35,0.5,0.75,0.92]:
        d=bisect_inc(lambda v:H(h+v)-v*S(h+v)-h,1e-10,60.0)
        thresholds=[]
        for n in range(1,22):
            c=bisect_inc(lambda z:delta(n,z,h,H),1e-12,100.0)
            assert n*d<c<(n+1)*d
            thresholds.append(c)
            checks+=1
        assert all(a<b for a,b in zip(thresholds,thresholds[1:]))
        checks+=1
        for _ in range(250):
            c=rng.uniform(0.005,70.0)
            B=rng.uniform(3*h+0.5,15*h+9)
            P=B+c
            N=math.ceil(B/h)-1
            g=h+c/4.0
            assert abs(Fprime(4,c,h,H,S)-(-h+H(g)-(g-h)*S(g)))<1e-12
            checks+=1
            x=rng.uniform(0.2,25)
            g=h+c/x
            assert abs((Fdoubleprime(x,c,h,f)) -
                       (-c*c*f(g)/x**3))<1e-12
            checks+=1
            vals=[Q(n,P,B,h,H) for n in range(1,N+1)]
            best=max(vals)
            xstar=c/d
            cand=set([1,N])
            for nn in [math.floor(xstar),math.ceil(xstar)]:
                if 1<=nn<=N: cand.add(nn)
            assert abs(best-max(vals[nn-1] for nn in cand))<2e-14
            checks+=1
            if N>=2:
                for n in range(1,N-1):
                    assert (vals[n]-vals[n-1])>(vals[n+1]-vals[n])-1e-12
                    checks+=1
    # Mean-duration boundary: h>=E[L] implies strict preference n=1.
    for h in [1.0,1.01,1.2,2,4]:
        for _ in range(250):
            B=rng.uniform(1.03*h,8*h+20)
            P=B+rng.uniform(0.001,30)
            vals=[Q(n,P,B,h,H) for n in range(1,math.ceil(B/h))]
            assert all(vals[0]>val for val in vals[1:])
            checks+=1
    # Gamma(2,1) distribution has mean 2, positive density on (0,infinity).
    Hg=lambda g: 2-(g+2)*math.exp(-g)
    Sg=lambda g:(g+1)*math.exp(-g)
    for h in [0.5,1,1.8,2.0,2.7]:
        for n in range(1,20):
            for c in [0.2,1.5,5.0,20.0]:
                B=100.0
                P=B+c
                assert abs(Q(n,P,B,h,Hg) -
                           (B-n*h+n*(2-(h+c/n+2)*math.exp(-h-c/n)))/P)<1e-12
                checks+=1
                if h>=2 and n<10:
                    assert Q(1,P,B,h,Hg)>Q(n+1,P,B,h,Hg)
                    checks+=1
    # Example: 5 on-windows (uniform is one optimal arrangement)
    B,P,h=8.0,12.0,0.5
    vals=[Q(n,P,B,h,H) for n in range(1,math.ceil(B/h))]
    assert max(range(1,len(vals)+1),key=lambda n:vals[n-1])==5
    assert abs(vals[4]-0.7614450862358281)<1e-13
    assert abs(vals[0]-0.7074075836218131)<1e-13
    checks+=3
    # Equal gaps beat arbitrary unequal gaps for fixed N (Jensen).
    for _ in range(5000):
        n=rng.randint(2,15)
        h=rng.uniform(0.01,0.9)
        B=n*h+rng.uniform(0.1,15)
        P=B+rng.uniform(0.5,50)
        gap_total=P-B+n*h
        w=[rng.random()+.01 for _ in range(n)]
        gaps=[gap_total*a/sum(w) for a in w]
        raw=(B-n*h+sum(H(g) for g in gaps))/P
        optimum=Q(n,P,B,h,H)
        assert raw<=optimum+1e-13
        checks+=1
    return checks

if __name__=="__main__":
    print("CHECKS_PASSED",verify())
