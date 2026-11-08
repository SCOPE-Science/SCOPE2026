#!/usr/bin/env python3
"""Reproducibility calculations for an explicit replicator-map repeller.

Analytic inequalities in RESULT.md prove the theorem for all parameters; this
script checks their rational certificate and representative endpoint values.
"""
from fractions import Fraction as Q
from math import exp,log,sqrt

# Pure rational estimates: 7 < exp(2) < 15/2, and exp(20)>100000.
e2_lower=sum((Q(2)**n)/__import__('math').factorial(n) for n in range(6))
e2_tail0=Q(2)**6/__import__('math').factorial(6)
e2_upper=e2_lower+e2_tail0/(1-Q(2,7))
assert Q(7)<e2_lower and e2_upper<Q(15,2)
assert Q(20)**8/__import__('math').factorial(8)>Q(100000)
# Endpoint and derivative bounds, at parameter extremes and several interiors.
checks=0
for a in (100,101,180,300,1000):
    for b in (0.25,0.27,1/3,0.37,0.4):
        g=lambda y: y + a/(1+exp(y)) - a*b
        gp=lambda y: 1-a*exp(-abs(y))/(1+exp(-abs(y)))**2
        L,R=a*b-5,a*b+5
        assert R>L>2
        assert g(-2)>R and g(2)<-2
        assert g(L)<-2 and g(R)>2 and g(R)<L
        assert gp(-2)<-9 and gp(2)<-9
        assert 0.999<gp(L)<=1 and 0.999<gp(R)<=1
        checks+=1
phi=(1+sqrt(5))/2
pi0=phi*phi/(phi*phi+1)
w00=phi/(phi*phi+1)
w01=1/(phi*phi+1)
assert abs(w00+w01-pi0)<1e-14
# For b=1/3, the two asymptotic branch factors agree exactly.
assert Q(1,3)*(1-Q(1,3)) == 2*Q(1,3)*(1-2*Q(1,3))
# Analytic leading branch factors checked against actual two-cycles (one 01 edge).
for a in (100,200,400):
    for b in (0.25,1/3,0.4):
        g=lambda y: y+a/(1+exp(y))-a*b
        gp=lambda y: 1-a*exp(-abs(y))/(1+exp(-abs(y)))**2
        z=log((1-2*b)/(2*b))
        lo,hi=z-0.2,z+0.2
        F=lambda y:g(g(y))-y
        assert F(lo)>0 and F(hi)<0
        for _ in range(90):
            mid=(lo+hi)/2
            if F(mid)>0:lo=mid
            else:hi=mid
        y0=(lo+hi)/2; y1=g(y0)
        assert -2<=y0<=2 and a*b-5<=y1<=a*b+5
        chi2=0.5*log(abs(gp(y0)*gp(y1)))
        pred2=0.5*(log(a)+log(2*b*(1-2*b)))
        assert abs(chi2-pred2)<0.15
print('VERIFY_OK rational_exp_bounds=2 endpoint_parameter_pairs=%d transition_matrix=golden_mean asymptotic_branch_balance=1 periodic_01_checks=9' % checks)
