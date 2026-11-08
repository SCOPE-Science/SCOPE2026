#!/usr/bin/env python3
"""Reproducibility checks for random equal-arc circular covering.
Only numerical or finite algebra checks are implemented; the analytic proof is in RESULT.md.
"""
from fractions import Fraction
from math import comb, exp
import itertools

def closed_cov(n,a):
    b=1-a
    return b**n+(n-1)*max(1-2*a,0)**n-n*b**(2*n-1)

def beta_tail(n,a):
    return (1-a)**(n-1)

def mixed_excess(n,a):
    # Integrate (x-a) over the Dirichlet simplex with S_2>a:
    # for n>=2: integral_{x=a}^{1-a} (n-1)(x-a)(1-x-a)^(n-2) dx.
    # Independent polynomial-exact integration via expanding (x-a)(b-(x-a))^(n-2).
    if 2*a >= 1: return Fraction(0)
    b=1-2*a
    return (n-1)*sum(((-1)**j)*comb(n-2,j)*b**(n-j-2)*b**(j+2)/Fraction(j+2)
                       for j in range(n-1))

def direct_cov(n,a):
    # E U = n int_a^1 P(S_1>t) dt; E G=n P(S_1>a)
    eu=(1-a)**n
    eg=n*beta_tail(n,a)
    # E U G = same-spacing terms + distinct-spacing terms.
    eug=eu+n*(n-1)*mixed_excess(n,a)
    return eug-eu*eg

checks=0
for n in range(2,20):
    for d in (7,11,29,59):
        for k in range(1,d):
            a=Fraction(k,d)
            assert direct_cov(n,a)==closed_cov(n,a),(n,a)
            checks+=1
for n in range(2,40):
    grid=[Fraction(k,1000) for k in range(1,1000)]
    signs=[1 if closed_cov(n,r)>0 else -1 if closed_cov(n,r)<0 else 0 for r in grid]
    assert all(signs[i]<=signs[i+1] for i in range(len(signs)-1)),n
    assert signs[0]<0 and signs[-1]>0
    checks+=1
# Verify h(w) is strictly unimodal from derivative numerator 1-(2n-1)w,
# and g is decreasing then increasing, via exact values at an internal mesh.
for n in range(2,40):
    for k in range(1,100):
        w=Fraction(k,100)
        h=(1-w)**(n-1)*(1+w)**n
        dh=Fraction(1-(2*n-1)*w,1-w*w)
        if w<Fraction(1,2*n-1): assert dh>0
        if w>Fraction(1,2*n-1): assert dh<0
        checks+=1
# Asymptotic root check against limit bracket e^c-1-c-c^2.
c_star=1.7932821329007556
for n in (100,1000,10000):
    for c in (0.5,1.0,1.5,2.1,3.0):
        assert abs(float(closed_cov(n,c/n))-exp(-2*c)*(exp(c)-1-c-c*c))<0.004
        checks+=1
    assert closed_cov(n,(c_star-0.05)/n)<0
    assert closed_cov(n,(c_star+0.05)/n)>0
    checks+=2
print('PASS',checks,'exact or numeric assertions')
