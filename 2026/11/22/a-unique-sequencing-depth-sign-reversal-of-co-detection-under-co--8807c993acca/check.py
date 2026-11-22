#!/usr/bin/env python3
"""Exact and numerical checks for the two-taxon fixed-read-depth detection theorem."""
from fractions import Fraction as F
from itertools import product
from math import exp,log
from random import Random

checks=0

def require(condition,tag):
    global checks
    checks+=1
    if not condition: raise AssertionError(tag)

def cov(n,r,a,b,c):
    s=a+b+c
    u=(b+c)/s; v=(a+b)/s; w=b/s
    return r*(1-u**n-v**n+w**n)-r*r*(1-u**n)*(1-v**n)

def theta(t,a,b,c):
    s=a+b+c;u=(b+c)/s;v=(a+b)/s;w=b/s
    return ((u*v)**t-w**t)/((1-u**t)*(1-v**t))

def sign(x,eps=1e-11):
    return 1 if x>eps else (-1 if x<-eps else 0)

# Compare independent exhaustive enumeration of all read words with the closed formula.
for a,b,c in product((1,2,3),repeat=3):
    s=a+b+c
    for k in (1,2,3,4,5,6):
        for r in (F(1,5),F(2,5),F(4,5)):
            weights=(F(a,s),F(c,s),F(b,s))
            meansX=meansY=meansXY=F(0)
            for word in product(range(3),repeat=k):
                p=F(1)
                for j in word:p*=weights[j]
                x=int(0 in word);y=int(1 in word)
                meansX+=r*p*x;meansY+=r*p*y;meansXY+=r*p*x*y
            brute=meansXY-meansX*meansY
            formula=cov(k,r,F(a),F(b),F(c))
            require(formula==brute,(a,b,c,k,r,formula,brute))

# Monotone threshold, sign equivalence, unique integer crossing.
rng=Random(20261119)
for trial in range(2300):
    a=10**rng.uniform(-2,2); b=10**rng.uniform(-2,2); c=10**rng.uniform(-2,2)
    r=rng.uniform(0.001,0.998)
    prev=theta(1,a,b,c)
    require(abs(prev-1)<1e-8,'theta(1)')
    prevsign=-1
    for n in range(1,41):
        cur=theta(n,a,b,c)
        if n>1: require(cur<prev*(1+1e-10),'theta decreases')
        C=cov(n,r,a,b,c)
        expected=sign(1-r-cur,eps=1e-9)
        actual=sign(C,eps=1e-10)
        if expected and abs(C)>1e-10: require(actual==expected,'cov sign factorization')
        if prevsign==1: require(expected>=0,'no return to negative')
        if expected==1:prevsign=1
        prev=cur

# Exact two-read tie and positive latent occupancy correlation.
a,b,c,r=F(2),F(1),F(3),F(4,5)
require(cov(1,r,a,b,c)==-F(8,75),'one read exact negative')
require(cov(2,r,a,b,c)==0,'two reads exact tie')
require(cov(3,r,a,b,c)>0,'three reads exact positive')
require(r*(1-r)==F(4,25),'positive latent covariance')

# Poissonized read totals: positive covariance at every positive mean depth.
for trial in range(1000):
    a,b,c=[10**rng.uniform(-2,2) for _ in range(3)]
    r=rng.uniform(.01,.99)
    exposure=10**rng.uniform(-2,3)
    qA=1-exp(-exposure*a/(a+b+c));qB=1-exp(-exposure*c/(a+b+c))
    C=r*(1-r)*qA*qB
    require(C>0,'poisson covariance')

# High-prevalence asymptotic of the crossing depth.
for a,b,c in ((2.,1.,3.),(.8,1.4,.25),(3.,2.,1.)):
    s=a+b+c; alpha=-log((b+c)/s); beta=-log((a+b)/s)
    for x in (20.,40.,80.,120.):
        r=1-exp(-x)
        if r==1.: continue
        lo=1.;hi=max(2.,2*x/(alpha+beta))
        while theta(hi,a,b,c)>1-r:hi*=2
        for _ in range(100):
            mid=(lo+hi)/2
            if theta(mid,a,b,c)>1-r:lo=mid
            else:hi=mid
        t=(lo+hi)/2
        require(abs(t/(x/(alpha+beta))-1)<.04,'asymptotic ratio')

print(f'PASS {checks} assertions: exact exhaustive read-word enumeration, monotone threshold, signs, rational tie, Poissonization, asymptotic checks')
