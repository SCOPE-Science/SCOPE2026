#!/usr/bin/env python3
"""Standalone finite diagnostics for circular heat/Fejer bandwidth formulas.

Requires Python 3 standard library only. The analytic theorem is proved in RESULT.md;
finite tests below are consistency checks, not infinite certification.
"""
import math, random


def b(n,t):
    return sum(k * math.exp(-t*k*k) for k in range(1,n+1))


def threshold(n):
    target=(2*n*(n+1)-1)/12
    lo, hi = 0., 4.
    while b(n,hi)>target:
        hi *= 2
    for _ in range(80):
        mid=(lo+hi)/2
        if b(n,mid)>target: lo=mid
        else: hi=mid
    return (lo+hi)/2


def delta(n,t):
    return 2/3-1/(3*n*(n+1))-4*b(n,t)/(n*(n+1))


def objective(n,t):
    cutoff=math.ceil(math.sqrt(40/t))
    s=2*sum(math.exp(-2*t*k*k) for k in range(1,cutoff+1))
    return s+2*sum((1-k/n)**2-2*math.exp(-t*k*k)*(1-k/n) for k in range(1,n))


def kernel_error_quadrature(n,t,m=16384):
    cutoff=math.ceil(math.sqrt(40/t))
    sq=0.
    for i in range(m):
        theta=2*math.pi*i/m
        heat=1+2*sum(math.exp(-t*k*k)*math.cos(k*theta) for k in range(1,cutoff+1))
        fejer=1+2*sum((1-k/n)*math.cos(k*theta) for k in range(1,n))
        sq+=(heat-fejer)**2
    return sq/m


def universal():
    lo,hi=2.,3.
    for _ in range(75):
        u=(lo+hi)/2
        if 1-math.exp(-u)-u/3>0: lo=u
        else: hi=u
    u=(lo+hi)/2
    c=math.sqrt(u)
    j=math.sqrt(math.pi/2)-2*math.sqrt(math.pi)*math.erf(c)+4*c/3
    return u,c,j


def run():
    checks=0
    u,c,j=universal()
    assert abs(1-math.exp(-u)-u/3)<2e-14;checks+=1
    assert abs(threshold(1)-math.log(4))<2e-14;checks+=1
    for n in range(1,51):
        tn=threshold(n)
        assert abs(delta(n,tn))<4e-14;checks+=1
        if n>=2:
            assert tn<threshold(n-1); checks+=1
    for n in [5,10,20,40,80,160,320]:
        tn=threshold(n)
        z=n*(n+1)*tn
        # second-order asymptotics: bounded residual in the natural n^-2 scale
        assert abs(z-u) < 2.3/n**2 + .006;checks+=1
    rng=random.Random(71803)
    for _ in range(500):
        t=10**rng.uniform(-3.0,1.5)
        n=rng.randint(1,80)
        e0=objective(n,t)
        e1=objective(n+1,t)
        assert abs((e1-e0)-delta(n,t)) < 2e-12;checks+=1
        assert delta(n+1,t)>delta(n,t);checks+=1
    for t in [0.005,0.015,0.1,1.5]:
        n=1
        while delta(n,t)<0:
            n+=1
        assert all(objective(n,t)<=objective(k,t)+1e-12 for k in range(1,130)); checks+=1
        assert abs(objective(n,t)-kernel_error_quadrature(n,t,m=8192))<5e-11;checks+=1
    for t in [1.e-3,1.e-4,1.e-5]:
        n=1
        while delta(n,t)<0: n+=1
        assert abs(n*math.sqrt(t)-c)<2*math.sqrt(t);checks+=1
        scaled=math.sqrt(t)*objective(n,t)
        assert abs(scaled-j)<.001;checks+=1
    for t in [.001,.0001]:
        n=max(1,round(1/(1-math.exp(-t))))
        ratio=t*objective(n,t)
        assert abs(ratio-2/3)<.08;checks+=1
    print('PASS',checks,'finite diagnostics')
    print('u*=%.15f, c*=%.15f, J*=%.15f'%(u,c,j))
    print('first five threshold times:',*[f'{threshold(n):.12f}' for n in range(1,6)])
    for n in [10,50,100,300]:
        print(f'n={n}, t_n={threshold(n):.15g}, n(n+1)t_n={n*(n+1)*threshold(n):.12g}')

if __name__=='__main__': run()
