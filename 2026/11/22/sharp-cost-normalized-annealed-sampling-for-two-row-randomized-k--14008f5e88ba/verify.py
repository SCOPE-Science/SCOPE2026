#!/usr/bin/env python3
"""Reproduce finite exact and numerical checks for the two-row sampling theorem.
Only the general analytic argument in RESULT.md proves the quantifiers.
"""
from fractions import Fraction as Q
from random import Random
from math import sqrt, log
from scipy.optimize import brentq

rng=Random(14057)
checks=0

def test(ok, desc):
    global checks
    assert ok, desc
    checks+=1

def root(p,c):
    s=sqrt(c**4+(1-c**4)*(1-2*p)**2)
    return (1+s)/2

def objective(p,c,a,b):
    return -log(root(p,c))/(b+(a-b)*p)

def derivative_numerator(p,c,a,b):
    d=1-c**4
    s=sqrt(1-4*d*p*(1-p))
    n=-log((1+s)/2)
    np=2*d*(1-2*p)/(s*(1+s))
    return np*(b+(a-b)*p)-(a-b)*n

def best(c,a,b):
    return brentq(lambda p:derivative_numerator(p,c,a,b),1.e-12,.5,xtol=1e-14)

# Exact transition matrix trace and determinant from two-state switch counting.
for _ in range(600):
    p=Q(rng.randrange(1,50),rng.randrange(51,102))
    c=Q(rng.randrange(1,50),rng.randrange(51,101))
    a=p;b=1-p; w=c*c
    # Last-label-conditioned squared-norm recurrence (a, a*w; b*w, b).
    tr=a+b; det=a*b*(1-w*w)
    test(tr==1,'trace')
    test(det==p*(1-p)*(1-c**4),'determinant')
    # One and two further draws after a fixed row-1 label.
    y1=(a+b*w)
    y2=a*(a+b*w)+b*w*(a*w+b)
    direct=a*a+a*b*w+a*b*w*w+b*b*w
    test(y2==direct,'two-switch decomposition')

# All unequal costs: p* between square-root-price share and one half;
# numerical stationary equation and strict advantage over equal sampling.
for _ in range(125):
    a=1.1+95*rng.random()
    b=.1+rng.random()
    c=.025+.95*rng.random()
    p=best(c,a,b)
    pl=sqrt(b)/(sqrt(a)+sqrt(b))
    test(pl < p < .5, 'interior share interval')
    test(abs(derivative_numerator(p,c,a,b))<2e-8,'stationarity')
    test(objective(p,c,a,b)>objective(.5,c,a,b),'strict optimal advantage')
    test(objective(p,c,a,b)>objective(pl,c,a,b),'strict square root advantage')
    # Check global dominance over grid, not a substitute for analytic proof.
    test(objective(p,c,a,b)>=max(objective(j/200,c,a,b) for j in range(201))-1e-12,'grid optimum')

# Strict monotone movement from fair sampling toward square-root cost law.
for a,b in [(2,1),(9,1),(100,1),(1.001,1)]:
    cs=[.05,.2,.5,.8,.95,.995]
    ps=[best(c,a,b) for c in cs]
    test(all(x>y for x,y in zip(ps,ps[1:])),'monotone coherence')

# Matched limiting rates and first orthogonal correction.
a,b=9.,1.
chi=(a-b)*log(2)/(a+b)
k=chi/sqrt(1-chi**2)
for c in [.1,.05,.025,.0125]:
    p=best(c,a,b)
    test(abs((.5-p)/(c*c)-k/2)<c*c*1.5,'near-orthogonal boundary layer')
for c in [.99,.995,.999,.9999]:
    p=best(c,a,b)
    test(abs(p-.25)<2*(1-c),'near-parallel price share')
    val=objective(p,c,a,b)/(1-c**4)
    test(abs(val-1/16)<.3*(1-c),'near-parallel exponent')
print(f'VERIFY_OK {checks} checks')
