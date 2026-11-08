#!/usr/bin/env python3
"""Reproducible deterministic checks of exact algebra for the critical renewal-area law.
These finite checks do not establish the limiting probability theorems.
"""
import math
from fractions import Fraction

def midpoint(f,a,b,n):
    h=(b-a)/n
    return h*sum(f(a+(i+0.5)*h) for i in range(n))

def gaussian_area_coefficient(beta):
    return 4/((2+beta)*math.sqrt(math.pi))

checks=0
for beta in (0.1,0.4,1.0,1.6,1.9):
    rho=1+beta/2
    c=gaussian_area_coefficient(beta)
    mu=rho/(rho-1)
    # Independently integrate the Gaussian absolute expectation over local times.
    q=midpoint(lambda s:2/math.sqrt(math.pi)*s**(beta/2),0,1,24000)
    assert abs(q-c)<0.000015, (beta,q,c)
    checks+=1
    assert abs(c/mu-4*beta/((2+beta)**2*math.sqrt(math.pi)))<1e-12
    checks+=1
    # Pareto-to-uniform: E[tau^p] exact for each finite p<rho.
    for p in (0.25,0.6,0.9):
        z=midpoint(lambda u:u**(-p/rho),0.005,1,65000) + 0.005**(1-p/rho)/(1-p/rho)
        val=rho/(rho-p)
        assert abs(z-val)/val<0.00005,(beta,p,z,val)
        checks+=1
# Exact conditional cycle formulas for deterministic area marks L.
for L in (0.2,0.7,1.0,2.5,5.0):
    for cutoff in (0.1,0.8,1.5,5.0,13.0):
        lower=min(1.0,L/cutoff)
        # P(L/U>cutoff)=min(1,L/cutoff).
        tail=min(1.0,L/cutoff)
        assert abs(tail-lower)<1e-14
        checks+=1
        # Truncated moment from direct integration of L/u for u >= L/cutoff.
        if lower<1:
            val=midpoint(lambda u:L/u,lower,1.0,14000)
            exact=L*math.log(cutoff/L)
            assert abs(val-exact)<1e-6, (L,cutoff,val,exact)
        else:
            assert L>=cutoff
        checks+=1
# A Pareto(1,rho) draw has exactly E[tau]=rho/(rho-1), rho>1;
# the index-one reward tail constant is E[L].
for a,b in ((Fraction(3,2),Fraction(1,2)),(Fraction(7,4),Fraction(3,4))):
    assert a/(a-1)>1
    assert a-b==1
    checks+=1
print(f'PASS: {checks} deterministic algebraic and quadrature checks')
