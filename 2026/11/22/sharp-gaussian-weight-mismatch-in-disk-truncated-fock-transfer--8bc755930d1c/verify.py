#!/usr/bin/env python3
"""Finite reproducibility checks for disk-truncated cross-Gaussian Fock transfer.

Only standard-library Python 3 is required. Assertions are finite checks,
not substitutes for the analytic proof of the all-parameter theorem.
"""
import math

checks=0

def demand(ok, message):
    global checks
    assert ok, message
    checks += 1

def q(n,x):
    # Poisson survival P(N_x >= n+1), summed forward with positive terms.
    k=n+1
    term=math.exp(-x+k*math.log(x)-math.lgamma(k+1))
    total=term
    for j in range(1, int(max(100,8*x+400))):
        term *= x/(k+j)
        total += term
        if k+j>x and term<total*2.e-16:
            break
    return total

def a(n,x,u):
    return u**n*q(n,x)

# Radial monomial integrals agree with the Poisson survival formula.
for x in (0.4,1.0,3.0,7.0,15.0):
    for n in range(9):
        independent=1.-math.exp(-x)*sum(x**k/math.factorial(k) for k in range(n+1))
        if independent>1.e-9:
            demand(abs(independent-q(n,x))<2.e-11,'monomial moment')

# Exact strict log-concavity: q_{n+1}/q_n decreases.
for x in (0.5,2,5,10,30,80):
    for n in range(int(x/2),int(x/2)+65):
        v1=q(n+1,x)/q(n,x)
        v2=q(n+2,x)/q(n+1,x)
        demand(v1>v2*(1+1.e-10),'strict survival ratio decline')

# Exact staircase thresholds, including all mode ties and the vacuum transition.
for x in (1.1,3.0,8.0,20.0):
    for n in range(16):
        r=q(n,x)/q(n+1,x)
        r_next=q(n+1,x)/q(n+2,x)
        demand(r_next>r,'strict threshold order')
        weights=[a(j,x,r) for j in range(max(20,n+25))]
        peak=max(weights)
        demand(abs(weights[n]-peak)<5.e-9*max(1,peak),'tied mode n')
        demand(abs(weights[n+1]-peak)<5.e-9*max(1,peak),'tied mode n+1')

# Fixed u<1: the constant function is always the maximizing mode.
for x in (.5,1,3,10,100):
    for u in (.2,.75,1.):
        seq=[a(n,x,u) for n in range(125)]
        demand(all(seq[0]>=v-1.e-12 for v in seq),'vacuum norm')
        demand(abs(seq[0]-(1-math.exp(-x)))<5.e-12,'vacuum formula')

# Sharp asymptotic norm, with numerical ratios approaching 1.
for u in (1.5,2.,3.):
    previous_error=1.e6
    for x in (30.,100.,300.):
        nmax=int(3*x*u+30)
        logs=[n*math.log(u)+math.log(q(n,x)) for n in range(nmax) if q(n,x)>0]
        top=max(logs)
        target=x*(u-1)-math.log(u-1)-.5*math.log(2*math.pi*u*x)
        ratio=math.exp(top-target)
        err=abs(ratio-1.)
        demand(err<(.12 if x==30 else .035 if x==100 else .012),'sharp constant')
        demand(err<previous_error,'rate convergence in samples')
        previous_error=err

print('PASS:',checks,'finite assertions')
