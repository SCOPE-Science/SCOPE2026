#!/usr/bin/env python3
"""Numerical diagnostics for Gaussian antithetic matching; no external packages."""
import math
import itertools

PI = math.pi
SQRT2 = math.sqrt(2.0)

def phi(x):
    return math.exp(-0.5 * x*x) / math.sqrt(2 * PI)

def Phi(x):
    return 0.5 * math.erfc(-x / SQRT2)

def g(t, d):
    return 2*t*phi(d/t) + d*(2*Phi(d/t)-1)

def h(s, d):
    return g(2*s, d) - g(SQRT2*s, d)

def hsecond(s, d):
    return (phi(d/(2*s))-SQRT2*phi(d/(SQRT2*s)))/s

def gain(n, L, permutation, s=1, mass=1):
    return (mass*mass/4.0)*sum(h(s, (permutation[j]-j-1)*L) for j in range(n))

def simpson(fn, aa, bb, intervals=12000):
    step = (bb-aa)/intervals
    acc = fn(aa)+fn(bb)
    for i in range(1, intervals):
        acc += (4 if i%2 else 2)*fn(aa+i*step)
    return step*acc/3

def var_integral_pair(s,d):
    # Compute integrated covariance directly, NOT via the absolute-moment formula.
    def cov(x):
        p,q=Phi(x/s), Phi((x-d)/s)
        return max(p+q-1,0)-p*q
    return -0.5*simpson(cov, -14*s, d+14*s)

def main():
    count=0
    for s in (0.25,1.0,2.0):
        for d in (0.0,0.2*s,0.8*s,1.7*s,3*s):
            assert abs(var_integral_pair(s,d)-h(s,d)/4)<1e-7*s
            count+=1
        z=2*s*math.sqrt(math.log(2))
        assert hsecond(s,z*.99)<0 and hsecond(s,z*1.01)>0
        count+=1
        assert abs(h(s,0)-s*(2-SQRT2)*math.sqrt(2/PI))<1e-12*s
        count+=1
        for d in (.01*s,.1*s,1*s,3*s):
            assert h(s,d)>0 and h(s,d)<h(s,0)
            count+=1
    for n in range(2,8):
        cyc=tuple(list(range(1,n))+[0])
        rank=tuple(range(n))
        for L in (.5,1.,1.5,2.,3.,5.):
            values=[gain(n,L,p) for p in itertools.permutations(range(n))]
            assert len(values)==math.factorial(n)
            count+=1
            assert abs(gain(n,L,rank)-n*h(1,L)/4)<1e-12
            count+=1
            assert abs(gain(n,L,cyc)-((n-1)*h(1,0)+h(1,n*L))/4)<1e-12
            count+=1
            indep=n/(2*math.sqrt(PI))
            assert max(values)/indep<=SQRT2-1+1e-12
            count+=1
            if h(1,L)<h(1,0)/2:
                other=max(gain(n,L,p) for p in itertools.permutations(range(n)) if p!=cyc)
                assert gain(n,L,cyc)>other+1e-10
                count+=1
    print('PASS:',count,'kernel, covariance, exhaustive assignment, and sharp-bound diagnostics')

if __name__=='__main__':
    main()
