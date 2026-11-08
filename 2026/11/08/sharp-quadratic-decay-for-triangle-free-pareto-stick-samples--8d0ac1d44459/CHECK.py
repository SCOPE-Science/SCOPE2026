#!/usr/bin/env python3
"""Independent finite checks for a Pareto random-stick large-deviation bound.
Only elementary arithmetic and Python's standard library are required.
The infinite asymptotic is established by the proof, not by these checks.
"""
from itertools import combinations, combinations_with_replacement
from math import exp, gamma, isclose, log, sqrt
from random import Random


def simpson(func, n=16000):
    assert n % 2 == 0
    h=1.0/n
    s=func(0.0)+func(1.0)
    for j in range(1,n):
        s+=(4 if j%2 else 2)*func(j*h)
    return s*h/3


def contains_triangle(a):
    return any(a[i]+a[j]>a[k] and a[i]+a[k]>a[j] and a[j]+a[k]>a[i]
               for i,j,k in combinations(range(len(a)),3))


def consecutive_avoids(a):
    a=sorted(a)
    return all(a[i]+a[i+1]<=a[i+2] for i in range(len(a)-2))


def bounds(n,alpha):
    z=log((1+sqrt(5))/2)
    lo=exp(-alpha*z*n*(n-1)/2)
    b=z*(n-1)*(n-2)/2
    v=alpha*b
    # Exact integer-shape Gamma survival probability, avoiding factorial overflows.
    term=1.0
    partial=1.0
    for k in range(1,n-1):
        term*=v/k
        partial+=term
    upper=exp(-v)*partial
    return lo, upper


def main():
    count=0
    phi=(1+sqrt(5))/2
    z=log(phi)
    c=1/(phi*phi)
    assert isclose(log(1+exp(-z)),z,abs_tol=1e-14);count+=1
    for j in range(201):
        y=j/20
        assert log(1+exp(-y))>=z-c*(y-z)-1e-13
        count+=1
    for n in range(3,8):
        for a in combinations_with_replacement(range(1,9),n):
            assert (not contains_triangle(a))==consecutive_avoids(a)
            count+=1

    rng=Random(20261104)
    for n in range(3,34):
        for rep in range(30):
            y=[rng.expovariate(1.0) for _ in range(n-1)]
            if rep%2:
                # Enforce feasibility using a recurrence, without assuming equal gaps.
                for i in range(1,n-1):
                    y[i]=max(y[i],log(1+exp(-y[i-1])))
            else:
                # Construct the geometrically spaced subevent used in the lower bound.
                y=[z+v for v in y]
            assert all(y[i+1]>=log(1+exp(-y[i]))-1e-13 for i in range(n-2))
            for m in range(1,n):
                assert sum(y[:m])>=(m-1)*z-1e-11
                count+=1
            weighted=sum((n-i)*v for i,v in enumerate(y,1))
            assert weighted>=z*(n-1)*(n-2)/2-1e-10
            count+=1

    p3=2*(1-log(2))
    p4=2+26*log(2)-18*log(3)
    num3=simpson(lambda r:2*r/(1+r))
    num4=simpson(lambda r:6*r*r*(1/(1+r)-log(1+1/(1+r))))
    assert abs(p3-num3)<1e-11 and abs(p4-num4)<1e-10
    count+=2

    # A second representation, sampling iid Pareto lengths directly rather than
    # generating the beta order-statistic ratios.
    for n,exact in [(3,p3),(4,p4)]:
        samples=180000
        success=0
        for _ in range(samples):
            lengths=[1.0/rng.random() for j in range(n)]
            success+=consecutive_avoids(lengths)
        empirical=success/samples
        assert abs(empirical-exact)<0.012, (n,empirical,exact)
        count+=1

    for n in range(3,85):
        for alpha in (0.25,0.5,1.0,2.0):
            lower, upper=bounds(n,alpha)
            assert lower<=upper*(1+1e-11)
            assert 0<=upper<=1+1e-10
            count+=1
    for n,exact in ((3,p3),(4,p4)):
        lower,upper=bounds(n,1)
        assert lower<=exact<=upper
        count+=1
    print('PASS',count,'independent finite checks; n=3 exact',format(p3,'.12g'),
          '; n=4 exact',format(p4,'.12g'))


if __name__=='__main__':
    main()
