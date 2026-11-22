#!/usr/bin/env python3
"""Independent finite checks for zero-start Ornstein–Uhlenbeck one-site design.
The continuum theorem is proved separately; these computations cannot certify it.
Requires only Python 3 standard library.
"""
import math


def simpson(fn, hi, pieces=4000):
    assert pieces % 2 == 0
    h = hi / pieces
    acc = fn(0.0) + fn(hi)
    for i in range(1, pieces):
        acc += (4 if i % 2 else 2) * fn(i * h)
    return acc * h / 3


def v(lam, t):
    return -math.expm1(-2 * lam * t) / (2 * lam)


def c(lam, t):
    # Rearranged to avoid the most severe cancellation for small parameters.
    return (-math.expm1(-lam * t) - 0.5 * math.exp(-lam * (1-t)) * (-math.expm1(-2*lam*t))) / (lam*lam)


def root(lam, eta):
    L = math.exp(lam)
    a = 0.5 / L
    b = 1-a
    T = 2*lam*eta
    y0 = (math.sqrt(1 + 8*L)-1)/2
    yi = math.sqrt(2*L-1)
    if eta == 0:
        return math.log(y0)/lam
    def f(y): return a*(1+T)*y**3-(2*a+b*(1+T))*y+1
    lo,hi=y0,yi
    for _ in range(85):
        mid=(lo+hi)*0.5
        if f(mid)<=0: lo=mid
        else: hi=mid
    return math.log((lo+hi)/2)/lam


def reduction(lam, eta, t):
    if t == 0.0:
        return 0.0
    return c(lam,t)**2/(v(lam,t)+eta)


def main():
    total=0
    for lam in (0.04,0.1,0.5,1,2,5,10):
        prev=-1
        for eta in (0,0.01,0.1,1,10,100):
            t=root(lam,eta)
            assert 0.5<t<1
            assert t>=prev-1e-10
            prev=t
            L=math.exp(lam)
            t0=math.log((math.sqrt(1+8*L)-1)/2)/lam
            ti=math.log(2*L-1)/(2*lam)
            assert t0-1e-10 <=t<=ti+1e-10
            # Compare the independently integrated Itô covariance with closed form.
            cc=simpson(lambda u: math.exp(-lam*(t-u))*(-math.expm1(-lam*(1-u)))/lam, t)
            assert abs(c(lam,t)-cc)<3e-9, (lam,eta,t,c(lam,t),cc)
            vr=simpson(lambda u: math.exp(-2*lam*(t-u)), t)
            assert abs(v(lam,t)-vr)<3e-9
            # Every member of this dense grid must have no better posterior reduction.
            best=reduction(lam,eta,t)
            for i in range(1001):
                check=reduction(lam,eta,i/1000)
                assert check<=best+1e-9,(lam,eta,t,i,check,best)
                total+=1
            # The cubic's normalized stationary equation is independently checked.
            y=math.exp(lam*t); a=1/(2*L); b=1-a; T=2*lam*eta
            F=a*(1+T)*y**3-(2*a+b*(1+T))*y+1
            assert abs(F)<2e-8,(lam,eta,F)
            total+=5
    print('PASS:',total,'finite analytic, quadrature, and grid assertions')

if __name__=='__main__': main()
