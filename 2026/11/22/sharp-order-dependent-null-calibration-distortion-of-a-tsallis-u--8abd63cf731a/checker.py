#!/usr/bin/env python3
"""Reproducibility checks for the CRTE uniform-null calibration theorem.

Requires Python 3 standard library only. No random-seed dependence of exact assertions.
"""
from fractions import Fraction as F
from math import sqrt, erfc
from random import Random

def weighted_stats(weights):
    # uniform n+1 spacings: n observations and n-1 interior weights
    n=len(weights)+1
    a=sum(weights,F(0)); b=sum((w*w for w in weights),F(0))
    den=(n+1)**2*(n+2)
    mean=a/F(n+1)
    var=((n+1)*b-a*a)/den
    reported=F(n)*b/den
    return mean,var,reported

def quadratic(n):
    return [F(i*(n-i),n*n) for i in range(1,n)]

def check_exact():
    checks=0
    for n in range(2,301):
        mean,var,published=weighted_stats(quadratic(n))
        assert mean==F(n-1,6*n); checks+=1
        assert var==F((n-1)*(n+3),180*n**3); checks+=1
        assert published==F((n-1)*(n*n+1),30*n*n*(n+1)*(n+2)); checks+=1
        assert published/var==F(6*n*(n*n+1),(n+1)*(n+2)*(n+3)); checks+=1
        if n>=3:
            assert published>var; checks+=1
        else:
            assert published==var; checks+=1
    return checks

def analytic(theta):
    # integrated squared profile, centered variance, published/true ratio
    b=2/(3*(theta+2)*(2*theta+1))
    v=(2*theta**2+theta+2)/(12*(theta+1)**2*(theta+2)*(2*theta+1))
    inflation=8*(theta+1)**2/(2*theta**2+theta+2)
    return b,v,inflation

def check_analytic():
    checks=0
    for theta in [0.05,0.1,0.2,0.5,0.9,1.1,2.,3.,5.,10.,50.]:
        b,v,r=analytic(theta)
        assert 4 <r<6.4; checks+=1
        assert abs(r-b/v)<1e-12;checks+=1
        for n in [100,1000,3000]:
            w=[((1-i/n)-(1-i/n)**theta)/(theta-1) for i in range(1,n)]
            sm=sum(w);sq=sum(x*x for x in w)
            expected=((n+1)*sq-sm**2)/((n+1)**2*(n+2))
            reported=n*sq/((n+1)**2*(n+2))
            assert expected>0;checks+=1
            assert reported>=expected;checks+=1
            if n==3000:
                assert abs(n*expected-v) < 0.005*v;checks+=1
                assert abs(reported/expected-r) < 0.035;checks+=1
    assert abs(analytic(1.)[2]-6.4)<1e-12;checks+=1
    assert abs(analytic(2.)[2]-6.0)<1e-12;checks+=1
    return checks

def check_simulation():
    # Independent reproducibility: generate raw uniform observations and sort.
    rng=Random(773052)
    n=100; trials=25000
    coef=[float(x) for x in quadratic(n)]
    sm=0.;s2=0.
    for _ in range(trials):
        u=sorted(rng.random() for _ in range(n))
        z=sum(coef[i]*(u[i+1]-u[i]) for i in range(n-1))
        sm+=z;s2+=z*z
    avg=sm/trials;vv=s2/trials-avg*avg
    ex_m=float(F(n-1,6*n));ex_v=float(F((n-1)*(n+3),180*n**3))
    assert abs(avg-ex_m)<0.0005, (avg,ex_m)
    assert abs(vv-ex_v)<2e-6, (vv,ex_v)
    return avg,vv,ex_m,ex_v

if __name__=='__main__':
    checks=check_exact()+check_analytic()
    sim=check_simulation()
    # z_0.975 from a well-known numerical normal quantile; this line is
    # a numerical illustration, not a component of the analytic proof.
    z975=1.959963984540054
    actual=erfc(z975*sqrt(6)/sqrt(2))
    print('exact+analytic assertions:',checks)
    print('simulation sample mean/variance:', sim[:2])
    print('exact n=100 mean/variance:', sim[2:])
    print('theta=2 sharp variance inflation:',6)
    print('limiting two-sided nominal-5% rejection probability:',format(actual,'.12g'))
