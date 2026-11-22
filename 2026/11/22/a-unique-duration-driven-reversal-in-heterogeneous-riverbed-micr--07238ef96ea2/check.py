#!/usr/bin/env python3
"""Numerical consistency checks for an idealized two-class reversible exchange model.

Not an infinite-domain proof; analytic statements are established in RESULT.md.
Requires Python 3 standard library only.
"""
import math
import random
from fractions import Fraction


def phase(x, p, lam, h):
    return p + (x-p)*math.exp(-lam*h)


def F(a, b, h):
    return -math.expm1(-a*h)*(-math.expm1(-b*h))


def ratio(a1, b1, a2, b2, h):
    return F(a1,b1,h)/F(a2,b2,h)


def calc_diff(w, pA, pB, a, b, h, x0):
    direct = 0.0
    formula = 0.0
    for j in range(2):
        ab = phase(phase(x0[j],pA[j],a[j],h),pB[j],b[j],h)
        ba = phase(phase(x0[j],pB[j],b[j],h),pA[j],a[j],h)
        direct += w[j]*(ab-ba)
        formula += w[j]*(pB[j]-pA[j])*F(a[j],b[j],h)
    return direct, formula


def root(q, a1,b1,a2,b2):
    lo,hi=1e-10,1.0
    for _ in range(300):
        if ratio(a1,b1,a2,b2,hi) > q:
            break
        hi *= 2
    assert ratio(a1,b1,a2,b2,lo) < q < ratio(a1,b1,a2,b2,hi)
    for _ in range(140):
        mid=(lo+hi)*.5
        if ratio(a1,b1,a2,b2,mid) < q:
            lo=mid
        else:
            hi=mid
    return (lo+hi)*.5



def exp_neg_interval(x, n=68):
    """Exact rational enclosure for exp(-x), x>=0 rational, n even, n+2>x."""
    assert x>=0 and n % 2 == 0 and Fraction(n+2,1) > x
    term=Fraction(1)
    series=term
    for k in range(1,n+2):
        term *= -x/k
        series += term
        if k==n:
            upper=series  # even partial sum (N even)
    lower=series         # odd partial sum (N+1 odd)
    assert 0 < lower < upper < 1
    return lower,upper


def exact_delta_interval(h):
    """Outward exact-Fraction interval for the illustrated two-class swap difference."""
    def bounds_F(aa,bb):
        eaL,eaU=exp_neg_interval(Fraction(aa)*h)
        ebL,ebU=exp_neg_interval(Fraction(bb)*h)
        return (1-eaU)*(1-ebU),(1-eaL)*(1-ebL)
    f1L,f1U=bounds_F(1,2)
    f2L,f2U=bounds_F(3,5)
    C,D=Fraction(21,50),Fraction(9,50)
    return C*f1L-D*f2U,C*f1U-D*f2L


def run():
    rnd=random.Random(190723)
    tests=0
    for _ in range(12000):
        a1=rnd.uniform(0.02,5.0); b1=rnd.uniform(0.02,5.0)
        a2=a1+rnd.uniform(.01,7.0); b2=b1+rnd.uniform(.01,7.0)
        w1=rnd.uniform(.01,.99)
        pA=[rnd.uniform(.02,.49),rnd.uniform(.51,.98)]
        pB=[rnd.uniform(.51,.98),rnd.uniform(.02,.49)]
        h=10.0**rnd.uniform(-2,0.3)
        direct,formula=calc_diff([w1,1-w1],pA,pB,[a1,a2],[b1,b2],h,
                                  [rnd.random(),rnd.random()])
        assert abs(direct-formula) <= 5e-15
        r=ratio(a1,b1,a2,b2,h)
        hplus=h*(1+1e-5)
        assert ratio(a1,b1,a2,b2,hplus) > r
        q0=(a1*b1)/(a2*b2)
        assert q0 < r < 1
        tests+=3
    # An exact rational admissible example, with initial fractions irrelevant.
    w=[0.7,0.3]
    pA=[.2,.8]; pB=[.8,.2]
    a=[1.,3.];b=[2.,5.]
    C=w[0]*(pB[0]-pA[0]); D=w[1]*(pA[1]-pB[1]);q=D/C
    q0=a[0]*b[0]/(a[1]*b[1]); assert q0 < q < 1
    hstar=root(q,*[a[0],b[0],a[1],b[1]])
    assert 0.66424243 < hstar < 0.66424246
    # Certified rational-enclosure signs: no floating point used in this step.
    assert exact_delta_interval(Fraction(66424243,100000000))[1] < 0
    assert exact_delta_interval(Fraction(66424246,100000000))[0] > 0
    tests += 2
    for h in (0.05,0.1,0.3,0.5,0.7,1.,2.,5.,10.):
        d,f=calc_diff(w,pA,pB,a,b,h,[.13,.89])
        assert abs(d-f)<1e-14
        assert (d<0) == (h<hstar)
        tests+=2
    assert abs(calc_diff(w,pA,pB,a,b,hstar,[.01,.99])[1])<1e-13
    print('PASS:', tests, 'supplementary comparisons; unique illustrative root:',repr(hstar))
    for h in (.1,1.,2.):
        print('h=',h,'AB minus BA=',calc_diff(w,pA,pB,a,b,h,[0.,1.])[1])

if __name__=='__main__':
    run()
