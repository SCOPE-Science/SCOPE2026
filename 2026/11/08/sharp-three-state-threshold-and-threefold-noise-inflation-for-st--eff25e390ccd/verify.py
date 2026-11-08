#!/usr/bin/env python3
"""Exact-rational checks for the integer stochastic-rounding invariant law."""
from fractions import Fraction as F
from math import floor

checks = 0

def check(c, label):
    global checks
    checks += 1
    assert c, label

def round_dist(x):
    lo = x.numerator // x.denominator
    p = x-F(lo)
    return ({lo: F(1)} if p == 0 else {lo: 1-p, lo+1: p})

def step_dist(x,r,u):
    return round_dist(u-r*(F(x)-u))

def predicted(r,u):
    t=min(u,1-u)
    b=(1+r)*t
    if t >= r/(1+r):
        return {0:1-u,1:u}
    h=t/(1-r+b)
    ell=(r-b)*h
    left={-1:ell,0:1-h-ell,1:h}
    return left if u<=F(1,2) else {1-k:p for k,p in left.items()}

def var_formula(r,u):
    t=min(u,1-u)
    b=(1+r)*t
    return u*(1-u) + (2*t*(r-b)/(1-r+b) if b<r else 0)

r_values=[F(1,100),F(1,7),F(1,4),F(2,5),F(1,2)]
u_values=[F(1,1000),F(1,100),F(1,10),F(1,7),F(1,5),F(1,4),F(1,3),F(2,5),F(1,2),F(3,5),F(2,3),F(3,4),F(9,10),F(99,100),F(999,1000)]
for r in r_values:
  for u in u_values:
    pi=predicted(r,u)
    check(all(p>=0 for p in pi.values()),('positivity',r,u))
    check(sum(pi.values(),F(0))==1,('total',r,u))
    check(sum(F(x)*p for x,p in pi.items())==u,('mean',r,u))
    evolved={}
    for x,p in pi.items():
      for y,q in step_dist(x,r,u).items():
        evolved[y]=evolved.get(y,F(0))+p*q
    check(all(evolved.get(x,0)==p for x,p in pi.items()),('stationarity',r,u,pi,evolved))
    check(all(pi.get(x,0)==p for x,p in evolved.items()),('support',r,u))
    variance=sum((F(x)-u)**2*p for x,p in pi.items())
    check(variance==var_formula(r,u),('variance',r,u,variance,var_formula(r,u)))
    base=u*(1-u)
    check(base<=variance<3*base,('threefold',r,u))
    # The bounded four-state trapping set is invariant.
    S={-1,0,1,2}
    check(all(set(step_dist(x,r,u))<=S for x in S),('invariant',r,u))
    # Every state of the four-state set reaches the recurrent class by a path of positive probability.
    target={x for x,p in pi.items() if p>0}
    for x in S:
      frontier={x}
      reached=False
      for _ in range(5):
        if frontier & target:
          reached=True; break
        frontier={y for z in frontier for y in step_dist(z,r,u)}
      check(reached,('reach',r,u,x))

r=F(2,5);u=F(1,10)
pi=predicted(r,u)
check(pi=={-1:F(13,370),0:F(307,370),1:F(5,37)},'exact example probabilities')
check(var_formula(r,u)==F(593,3700),'exact example variance')
check(var_formula(r,u)/(u*(1-u))==F(593,333),'exact example ratio')

# A rational approach to the sharp factor 3 as r=1/2 and u -> 0.
prev=F(0)
for n in (2,3,4,5,6,7,8):
    t=F(1,10**n)
    ratio=var_formula(F(1,2),t)/(t*(1-t))
    check(ratio>prev and ratio<3,('sharpness',n,ratio))
    prev=ratio
check(3-prev<F(1,10**5),'near-sharpness')
print('PASS:',checks,'exact-rational assertions')
print('example:',pi,'variance',var_formula(r,u),'inflation',F(593,333))
print('sharp-ratio example:',prev)
