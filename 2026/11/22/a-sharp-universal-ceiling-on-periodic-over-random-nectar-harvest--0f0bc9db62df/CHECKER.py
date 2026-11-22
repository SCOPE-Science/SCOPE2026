#!/usr/bin/env python3
"""Numerical diagnostics for a renewal-resource harvesting theorem.

The analytic proof, not these finite diagnostics, establishes the infinite
parameter-range assertions.
"""
import math
import random

checks=0

def check(ok, context=''):
    global checks
    if not ok:
        raise AssertionError(context)
    checks += 1

def expected_rate(r, c, lam, q, m, phi):
    alpha=r+lam
    return q*r*c/(alpha*m) * (1-phi)/(1-(1-q)*phi)

def periodic_rate(r,c,lam,q,m):
    return expected_rate(r,c,lam,q,m,math.exp(-(r+lam)*m))

def poisson_rate(r,c,lam,q,m):
    return q*r*c/((r+lam)*m+q)

def ratio(q,x):
    e=math.expm1(x)
    return (x+q)*e/(x*(e+q))

def root():
    lo,hi=1.,3.
    for _ in range(110):
        mid=(lo+hi)/2
        if math.exp(mid)-1-mid-mid*mid>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

star=root()
ceiling=(1+star)*(-math.expm1(-star))/star
check(1.79<star<1.80)
check(abs(math.exp(star)-1-star-star*star)<1e-12)
check(abs(ceiling-1.298425607525639)<1e-12)

rng=random.Random(741201)
for _ in range(18000):
    x=math.exp(rng.uniform(math.log(.002),math.log(55.)))
    q=rng.uniform(.005,1.)
    # Periodic versus a same-mean Poisson clock; and the sharp ceiling.
    h=ratio(q,x)
    check(h>1-5e-14)
    check(h<=ceiling+5e-13)
    # Partial harvesting cannot improve on complete harvest's relative edge.
    check(h<=ratio(1,x)+1e-13)
    r=math.exp(rng.uniform(-2,2))
    lam=rng.uniform(0,8)
    m=x/(r+lam)
    c=rng.uniform(.1,15)
    H1=periodic_rate(r,c,lam,q,m)
    H2=poisson_rate(r,c,lam,q,m)
    check(abs(H1/H2-h)<3e-12)
    # Two-point renewal distribution with fixed mean cannot exceed periodic.
    eps=rng.uniform(.0001,.9)
    phi=.5*math.exp(-(r+lam)*m*(1-eps))+.5*math.exp(-(r+lam)*m*(1+eps))
    Hmix=expected_rate(r,c,lam,q,m,phi)
    check(Hmix<=H1+2e-12)

# Resource trajectory simulation with exactly sampled Poisson competitors.
def experiment(m,lam,q,exp_clock=False,n=120000):
    r=1.3; c=4.0
    stock=0.0; vol=0.0; total=0.0
    for _ in range(n):
        T=(rng.expovariate(1/m) if exp_clock else m)
        remain=T
        while True:
            w=rng.expovariate(lam) if lam>0 else float('inf')
            dt=min(w,remain)
            stock=c+(stock-c)*math.exp(-r*dt)
            remain-=dt
            if w>=remain+dt-1e-14: break
            stock=0.0
        vol+=q*stock
        stock*=(1-q)
        total+=T
    return vol/total

for lam,q,m in [(.0,1.,1.4),(.9,1.,.7),(2.4,.45,.9),(.2,.1,.4)]:
    for exp_clock in [False,True]:
        estimate=experiment(m,lam,q,exp_clock)
        theo=poisson_rate(1.3,4,lam,q,m) if exp_clock else periodic_rate(1.3,4,lam,q,m)
        check(abs(estimate/theo-1)<.025, (lam,q,m,exp_clock,estimate,theo))

# Sign of derivative characterizes a unique interior maximizer.
for i in range(1,800):
    x=i*0.01
    numerator=math.exp(-x)*(x*x+x+1)-1
    check(numerator>0 if x<star else numerator<0)
print('CHECKS_PASSED',checks)
print('X_STAR',f'{star:.15f}')
print('GLOBAL_RATIO_CEILING',f'{ceiling:.15f}')
print('MAXIMUM_RELATIVE_GAIN_PERCENT',f'{(ceiling-1)*100:.12f}')
