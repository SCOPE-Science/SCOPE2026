"""Finite-state and Brownian-path diagnostics for the interval-last-visit theorem.

Run: python3 verify.py All assertions are finite checks, not proofs of asymptotics.
"""
from fractions import Fraction
from math import gamma, sqrt, pi, floor, isclose
import numpy as np

COUNT = 0

def check(condition, label):
    global COUNT
    if not condition:
        raise AssertionError(label)
    COUNT += 1


def transition(m, x, a):
    # ERW future transition at absolute time m.
    up = (1 + a * Fraction(x, m)) / 2
    return {x+1: up, x-1: 1-up}


def product_r(n, m, a):
    r = Fraction(1)
    for k in range(n,m):
        r /= 1 + a/Fraction(k)
    return r

# Exact martingale, conditional variance and recurrence checks.
for a in [Fraction(3,5), Fraction(3,4), Fraction(9,10)]:
    for n in range(2,19):
        for x in range(-n,n+1,2):
            r = product_r(n,n+1,a)
            trans = transition(n,x,a)
            check(sum(prob*r*y for y,prob in trans.items()) == x, 'martingale')
            var = sum(prob*(r*y-x)**2 for y,prob in trans.items())
            check(var == r*r*(1-(a*Fraction(x,n))**2), 'variance')
            check(sum(trans.values())==1 and min(trans.values())>0, 'probabilities')


def dp_hitting(n,x, rad, horizon, a):
    if abs(x)<=rad: return Fraction(1)
    alive={x: Fraction(1)}
    hit=Fraction(0)
    for m in range(n,horizon):
        new={}
        for state,weight in alive.items():
            for y,p in transition(m,state,a).items():
                if abs(y)<=rad: hit+=weight*p
                else: new[y]=new.get(y,Fraction(0))+weight*p
        alive=new
    return hit


def brute_hitting(n,x,rad,horizon,a):
    stack=[(n,x,Fraction(1),False)]
    mass=Fraction(0)
    while stack:
        m,y,w,hit=stack.pop()
        hit=hit or abs(y)<=rad
        if m==horizon:
            if hit: mass+=w
            continue
        for z,p in transition(m,y,a).items(): stack.append((m+1,z,w*p,hit))
    return mass

for a in [Fraction(3,4),Fraction(2,3)]:
    for n in (3,4,5,6):
        for rad in (0,1,2):
            for x in range(-n,n+1,2):
                for length in (1,3,6):
                    actual=dp_hitting(n,x,rad,n+length,a)
                    brute=brute_hitting(n,x,rad,n+length,a)
                    check(actual==brute,'exact hitting DP vs complete path enumeration')

# Deterministic formula for the constant's origin and perturbation derivative.
for a in [0.55,0.65,0.75,0.85,0.95]:
    delta=2*a-1
    beta=a/delta
    v=1/delta
    kappa=sqrt(8/(pi*delta))
    slope=2*gamma(beta+0.5)/(sqrt(pi)*gamma(beta+1))
    check(kappa>0 and 0<slope<2 and beta>1,'analytic domain')
    if a==0.75:
        # Monte Carlo Brownian polygon with fixed pseudo-random seed.
        rng=np.random.default_rng(20261107)
        samples=12000
        steps=768
        maxima={c:np.zeros(samples) for c in [0.,.05,.25,.5,2.,10.]}
        times=np.linspace(0.,v,steps+1)
        lengths={c:np.zeros(samples) for c in maxima}
        argmax=np.zeros(samples,dtype=float)
        # modest block batching for memory
        for start in range(0,samples,400):
            count=min(400,samples-start)
            increments=rng.normal(0.,sqrt(v/steps),size=(count,steps))
            paths=np.concatenate([np.zeros((count,1)),np.cumsum(increments,axis=1)],axis=1)
            maximum_pos=paths.argmax(axis=1)
            argmax[start:start+count]=times[maximum_pos]
            for c in maxima:
                barrier=c*(1-delta*times)**beta
                m=(paths+barrier).max(axis=1)
                maxima[c][start:start+count]=m
                # Check that continuous union of moving intervals has predicted range
                min_bound=(-paths-barrier).min(axis=1)
                max_bound=(-paths+barrier).max(axis=1)
                union_length=max_bound-min_bound
                lengths[c][start:start+count]=union_length
        means={c:2*maxima[c].mean() for c in maxima}
        for c in means:
            check(abs(lengths[c].mean()-means[c])<0.05,'Brownian width identity in expectation')
        check(abs(means[0.]-kappa)<0.08,'zero-radius Brownian reflection constant')
        slope_mc=2*np.mean((1-delta*argmax)**beta)
        check(abs(slope_mc-slope)<0.05,'arcsine first derivative')
        check(all(means[c] >= 2*c-0.001 for c in means),'moving interval width lower bound')
        check(means[10.]/20 < 1.07,'large radius ratio')
        print('Brownian constants for a=0.75:',{str(c):round(val,5) for c,val in means.items()})
        print('C(0):', kappa, 'C\u2032(0+):', slope, 'simulated derivative:',slope_mc)
print('CHECKS_PASSED:',COUNT)
