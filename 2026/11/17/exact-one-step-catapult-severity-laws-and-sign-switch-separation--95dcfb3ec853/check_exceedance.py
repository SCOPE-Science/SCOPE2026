#!/usr/bin/env python3
"""Check exact algebra and sampled interval lengths for one-step severity tails."""
from math import sqrt
from fractions import Fraction

def q(a,r): return 1-2*a+(a*a-2*a)*r+a*a*r*r

def p_weight(a,t):
    d=a*a+4*a-4*sqrt(t)
    return sqrt(max(0,1-2*sqrt(1+sqrt(t))/(a+2))) if d>0 else 0.

def p_residual(a,t): return sqrt(max(0,a*a+4*a-4*sqrt(t)))/(a+2)

for a in map(Fraction,['1/3','7/8','19/20']):
    for r in map(Fraction,['-1','-1/3','0','1/4','1/2','1','2']):
        assert (1+r)*(1-a*r)**2-1==r*q(a,r)
for a in (.84,.87,.9,.95,.99):
    high=(a+a*a/4)**2
    for z in (.07,.25,.55,.9):
        t=1+z*(high-1)
        d=a*a+4*a-4*sqrt(t)
        lo=(2-a-sqrt(d))/(2*a);hi=(2-a+sqrt(d))/(2*a)
        ex=(sqrt(1+hi)-sqrt(1+lo))/sqrt(1+2/a)
        ez=a*(hi-lo)/(a+2)
        assert abs(p_weight(a,t)-ex)<2e-12
        assert abs(p_residual(a,t)-ez)<2e-12
        n=15000;R=sqrt(1+2/a)
        nx=sum(q(a,(R*(j+.5)/n)**2-1)**2>t for j in range(n))
        nz=sum(q(a,(-a+(a+2)*(j+.5)/n)/a)**2>t for j in range(n))
        assert abs(nx/n-ex)<1.1/n
        assert abs(nz/n-ez)<1.1/n
    assert (2-a+sqrt(a*a+4*a-4))/(2*a)<1/a
print('VERIFY_OK exact_rational_cases=21 severity_cases=20 midpoint_tests=600000')
