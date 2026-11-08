#!/usr/bin/env python3
"""Reproduce algebraic and finite-iteration checks for a congestion-game map.
This verifies sampled identities and iteration values, not infinite quantifiers.
"""
import math


def sigma(a):
    assert a > 8
    lo, hi = 0.0, 1.0
    for _ in range(90):
        t = (lo + hi)/2
        if t >= 1:
            hi=t
            continue
        eq = 8*math.atanh(t)/t if t else 8.0
        if eq < a: lo=t
        else: hi=t
    return (1-(lo+hi)/2)/2


def f(x, a):
    return x/(x+(1-x)*math.exp(a*(x-0.5)))


def F(x, y, a):
    return (x/(x+(1-x)*math.exp(a*(y-0.5))),
            y/(y+(1-y)*math.exp(a*(x-0.5))))


def transverse(u,a):
    e=math.exp(a*(u-.5));D=u+(1-u)*e
    return (1+a*u*(1-u))*e/D**2


def exit_time(a,z,eps,delta):
    x,y=z+eps,z-eps
    assert 0<y<x<1
    for n in range(200000):
        if x-y>=2*delta:
            return n
        x,y=F(x,y,a)
    raise AssertionError('no exit in finite experiment')


def checks():
    pairs=[]
    for a in (8.1,9,12,16,24,40):
        s=sigma(a);p=s*(1-s);lam=1+a*p
        assert 0<s<.5 and 1<lam<3
        assert abs(f(s,a)-(1-s))<1e-11
        assert abs(f(1-s,a)-s)<1e-11
        assert abs(transverse(s,a)-lam)<1e-10
        assert abs(transverse(1-s,a)-lam)<1e-10
        # Analytic tangential derivative from the source's exact quotient formula.
        e=math.exp(a*(s-.5));D=s+(1-s)*e
        tangent=(1-a*s*(1-s))*e/D**2
        assert abs(tangent-(1-a*p))<1e-10
        pairs.append((a,s,lam))
    assert all(pairs[i][2]>pairs[i+1][2] for i in range(len(pairs)-1))
    rows=[]
    for a in (9,12,16,24):
        s=sigma(a);lam=1+a*s*(1-s)
        delta=min(0.0003,s/50)
        for z in (s, .32):
            for eps in (1e-6,1e-8,1e-10,1e-12):
                if eps>=delta/100:continue
                n=exit_time(a,z,eps,delta)
                predicted=math.log(delta/eps)/math.log(lam)
                err=n-predicted
                assert abs(err)<80, (a,z,eps,n,predicted)
                rows.append((a,z,eps,delta,n,round(predicted,4),round(err,4)))
    # Large-a asymptotic ratios (a=80 still resolve sigma via bisection).
    asym=[]
    for a in (24,40,60,80):
        s=sigma(a)
        v=(1+a*s*(1-s)-1)/(a*math.exp(-a/4))
        asym.append((a,v))
    assert abs(asym[-1][1]-1)<1e-5
    print('PASS: 6 sampled two-cycle points, Jacobian factors and monotonicity checks')
    print('PASS: %d near-diagonal first-exit numerical comparisons'%len(rows))
    print('asymptotic multipliers:',asym)
    for row in rows: print('N',*row)

if __name__=='__main__':checks()
