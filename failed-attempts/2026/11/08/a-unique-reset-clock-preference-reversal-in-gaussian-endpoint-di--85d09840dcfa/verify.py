#!/usr/bin/env python3
"""Deterministic numerical cross-checks of the Gaussian reset-clock comparison.
Run: python3 verify.py ; only Python standard library required.
These tests supplement, but do not replace, the continuous proof.
"""
from math import exp, expm1, isfinite

def g(a, x):
    f = -expm1(-x)
    return 0.5 * a*a * f*f / (1 + a*f)

def gpp(a, x):
    f = -expm1(-x)
    return .5*a*a*(1-f)*(2-4*f-3*a*f*f-a*a*f*f*f)/(1+a*f)**3

def simpson(f, lo, hi, n=24000):
    assert n % 2 == 0
    step = (hi-lo)/n
    sm = f(lo)+f(hi)
    for j in range(1, n):
        sm += (4 if j%2 else 2)*f(lo+j*step)
    return sm*step/3

def exp_g(a,x):
    return simpson(lambda z: exp(-z)*g(a,x*z),0.,40.,10000)

def delta(a,x):
    return exp_g(a,x)-g(a,x)

def bisection(a,lo,hi):
    assert delta(a,lo)>0 and delta(a,hi)<0
    for k in range(50):
        mid = .5*(lo+hi)
        if delta(a,mid)>0:lo=mid
        else:hi=mid
    return .5*(lo+hi)

def K(z):
    return exp(-z)-(1-z if z<1 else 0)

def H(x,t):
    return x*K(t/x)

def tests():
    tests=0
    for a in [0.1, 1., 10.]:
        for x in [.03,.1,.3,.5,1.,2.,3.,8.]:
            h=1.e-4
            err=abs((g(a,x+h)-2*g(a,x)+g(a,x-h))/h**2-gpp(a,x))
            assert err<5.e-5,(a,x,err)
            tests+=1
    # Negative and positive curvature are separated by one crossing.
    for a in [.01,.1,1,10,100]:
        cc=0
        last=None
        for j in range(1,201):
            t=j/70
            s=1 if gpp(a,t)>0 else -1
            if last is not None and s!=last:cc+=1
            last=s
            tests+=1
        assert cc==1,(a,cc)
    # Kernel is strictly TP2 across scales: larger x lifts larger t relatively.
    for x1,x2 in [(.1,.15),(.3,1.),(1.,3.),(2.,8.)]:
        ts=[k/50 for k in range(1,500)]
        ratios=[H(x2,t)/H(x1,t) for t in ts if H(x1,t)>1e-15]
        assert all(v>u*(1-1e-8) for u,v in zip(ratios,ratios[1:])),(x1,x2)
        tests+=len(ratios)-1
    for a in [.01,.1,1.,10.,100.]:
        root=bisection(a,1e-3,10.)
        assert delta(a,root*.9)>0
        assert delta(a,root*1.1)<0
        assert abs(delta(a,root))<3e-11,(a,root,delta(a,root))
        tests+=3
        print(f'a={a:8g} x_cross={root:.13f} reduced_reset_rate={1/root:.13f}')
    # Prove no accidental collapse to the teleportation approximation by a=1 example.
    a=1.
    assert delta(a,.1)>0 and delta(a,1.)<0
    print('a=1, s=10: periodic=',10*g(a,.1),'Poisson=',10*exp_g(a,.1))
    print('a=1, s=1: periodic=',g(a,1),'Poisson=',exp_g(a,1))
    print('All',tests+2,'deterministic checks passed')

if __name__=='__main__':tests()
