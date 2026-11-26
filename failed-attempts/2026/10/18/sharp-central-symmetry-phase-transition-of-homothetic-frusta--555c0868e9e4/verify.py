#!/usr/bin/env python3
"""Deterministic regression tests for central-overlap profiles of symmetric-base homothetic frusta."""
from math import isclose

def threshold(d):
    q=2**(-1/(d-1))
    a=1/(2-q)
    return 2*a-1,a

def core(d,r,s):
    # Volume divided by horizontal base volume.
    n=d-1
    if isclose(r,1,abs_tol=1e-14):return 2*min(s,1-s)
    a=r+(1-r)*s
    if s<=.5:return 2*(a**d-r**d)/(d*(1-r))
    b=2*a-1
    return 2*(a**d-b**d)/(d*(1-r))

def optimal(d,r):
    t,a=threshold(d)
    s=(a-r)/(1-r) if r<t else .5
    if r==1:return s,1.
    if r<=t:ratio=a**(d-1)/(1-r**d)
    else:ratio=2*((1+r)/2)**d/(1-r**d)-2*r**d/(1-r**d)
    return s,ratio

def base_volume(d,r):
    return (1-r**d)/(d*(1-r)) if r<1 else 1.

def integrate2(r,s,u,N=1600):
    # Planar trapezoid with symmetric interval base [-1,1] and center (u,s).
    lo=max(0,2*s-1);hi=min(1,2*s)
    def f(z):
        w=r+(1-r)*z;v=r+(1-r)*(2*s-z)
        return max(0,min(w,2*u+v)-max(-w,2*u-v))
    h=(hi-lo)/N
    return h/3*(f(lo)+f(hi)+4*sum(f(lo+i*h) for i in range(1,N,2))+2*sum(f(lo+i*h) for i in range(2,N,2)))

def run():
    tests=0; worst=0
    for d in range(2,31):
        t,_=threshold(d)
        for r in [0,.05,.25,max(0,t-.0001),t,min(1,t+.0001),.8,.95,.999,1]:
            s,v=optimal(d,r)
            assert 0<s<=1 and 0<v<=1+1e-12
            assert abs(v-core(d,r,s)/base_volume(d,r))<5e-10,(d,r,s,v)
            for k in range(0,101):
                z=k/100
                assert core(d,r,z)<=core(d,r,s)+1e-12,(d,r,z,s)
                tests+=1
    for r in [0,.1,1/3,.35,.5,.9,1]:
        s,_=optimal(2,r)
        for z in [0.25,0.5,s,0.7,0.85]:
            if 0<z<1:
                exact=2*core(2,r,z)
                calculated=integrate2(r,z,0)
                worst=max(worst,abs(exact-calculated))
                assert abs(exact-calculated)<1e-11
                for u in [.0001,.05,.25,.5]:
                    assert integrate2(r,z,u)<integrate2(r,z,0)-1e-14
                    tests+=1
    print('VERIFY_OK',tests,'max_2D_integration_error',worst)
if __name__=='__main__':run()
