#!/usr/bin/env python3
"""Standalone supplementary checks for complementary heterogeneous capture hazards.
The analytic proofs, not these finite tests, establish the universal assertions.
"""
from math import exp, log, sqrt, isclose, gamma
from fractions import Fraction

checks=0

def check(assertion, description):
    global checks
    assert assertion, description
    checks+=1

def midpoint_integral(fn, n=4000):
    return sum(fn((i+.5)/n) for i in range(n))/n

def survival(distribution, B, x):
    return sum(w*exp(-p*x-(1-p)*(B-x)) for w,p in distribution)

def phi(distribution, delta):
    return sum(w*exp(-delta*(p-.5)) for w,p in distribution)

def dphi(distribution, delta):
    return -sum(w*(p-.5)*exp(-delta*(p-.5)) for w,p in distribution)

def delta_star(distribution):
    lo,hi=-200.,200.
    for _ in range(160):
        mid=(lo+hi)/2
        if dphi(distribution,mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

# Exact two-class tilted-mean certificate: solve exp(delta/2)=2.
dist=[(Fraction(1,3),Fraction(1,4)),(Fraction(2,3),Fraction(3,4))]
delta=2*log(2)
check(isclose(dphi(dist,delta),0,abs_tol=1e-14), 'two-class exact tilt')
check(isclose(phi(dist,delta),2*sqrt(2)/3,rel_tol=1e-14), 'two-class optimal constant')
check(isclose(delta_star(dist),delta,abs_tol=1e-12), 'two-class unique minimizer')
for B in [0.02,.1,.5,1,1.3,2,3,10,25,50]:
    projection=max(-B,min(B,delta))
    x=(B+projection)/2
    y=B-x
    check(x>=0 and y>=0 and isclose(x+y,B,abs_tol=1e-14),'feasible')
    check(isclose(survival(dist,B,x),exp(-B/2)*phi(dist,projection),rel_tol=1e-13),'factorization')
    for j in range(101):
        test_x=B*j/100
        check(survival(dist,B,x)<=survival(dist,B,test_x)+1e-13,'global grid inequality')
    if B>delta:
        check(isclose(x-y,delta,abs_tol=1e-12),'frozen difference')
    else:
        check(isclose(x,B,abs_tol=1e-12),'single lure before threshold')

# Every unit-mass discrete distribution on p=0,.25,.5,.75,1 with rational
# weights on a denominator-6 lattice (many interior and boundary cases).
from itertools import product
for a,b,c,d in product(range(7),repeat=4):
    e=6-a-b-c-d
    if e<0: continue
    distribution=[(w/6,p) for w,p in zip((a,b,c,d,e),(0,.25,.5,.75,1)) if w]
    if not any(p<.5 for w,p in distribution) or not any(p>.5 for w,p in distribution):
        continue
    ds=delta_star(distribution)
    check(abs(dphi(distribution,ds))<=1e-10,'tilted mean normal equation')
    for B in [.2,1,5,20]:
        deltaB=max(-B,min(B,ds));x=(B+deltaB)/2
        v=survival(distribution,B,x)
        for j in range(21):
            check(v<=survival(distribution,B,B*j/20)+1e-10,'global allocation check')

# Beta(2,1) tilted mean root by midpoint integration as an independent
# numerical method (bisection over exact integral, not shared with discrete checks).
def beta_phi(z):return midpoint_integral(lambda p:2*p*exp(-z*(p-.5)))
def beta_dphi(z):return -midpoint_integral(lambda p:2*p*(p-.5)*exp(-z*(p-.5)))
lo,hi=0.,8.
for _ in range(70):
    m=(lo+hi)/2
    if beta_dphi(m)>0:hi=m
    else:lo=m
betad=(lo+hi)/2
check(2.68<betad<2.7,'Beta(2,1) root bracket')
for B in [3.,5.,15.,20.]:
    x=(B+min(B,betad))/2
    v=exp(-B/2)*beta_phi(min(B,betad))
    for j in range(101):
        dx=2*B*j/100-B
        vj=exp(-B/2)*beta_phi(dx)
        check(v<=vj+1e-10,'beta numerical allocation')
# Minimax worst-case of any p in [0,1] is attained at p=0 or p=1.
for B in [.2,1,3,20]:
    for j in range(101):
        x=B*j/100
        worst=exp(-min(x,B-x))
        check(worst>=exp(-B/2)-1e-13,'minimax equal-exposure lower bound')
        for p in [0,.1,.25,.5,.75,.9,1]:
            check(exp(-p*x-(1-p)*(B-x))<=worst+1e-13,'worst endpoint law')
print('PASS:',checks,'supplementary checks; beta delta',round(betad,9))
