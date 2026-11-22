#!/usr/bin/env python3
"""Numerical diagnostics for the norm jump of rotating Fock composition semigroups.

All infinite-dimensional statements rely on the proof, not on these finite tests.
"""
import math
import cmath
from itertools import product

N = 0

def ensure(cond, message):
    global N
    N += 1
    if not cond:
        raise AssertionError(message)

def profile(u, rho):
    return abs(1.0-cmath.exp(complex(-u, rho*u)))

def optimum(rho):
    assert rho > 0
    lo, hi = math.pi/(2*rho), math.pi/rho
    def h(u):
        return math.cos(rho*u)+rho*math.sin(rho*u)-math.exp(-u)
    for _ in range(110):
        mid = (lo+hi)/2
        if h(mid)>0:
            lo = mid
        else:
            hi = mid
    u = (lo+hi)/2
    j = profile(u, rho)
    curvature = (1+rho*rho)*math.exp(-u)*(-math.cos(rho*u))/j
    return u,j,curvature

for rho in [.12, .2, .5, 1, 1.7, 4, 12, 40]:
    u,j,d = optimum(rho)
    ensure(j>1 and d>0, 'positive jump and curvature')
    ensure(math.pi/(2*rho)<u<math.pi/rho, 'maximizer in first half-turn')
    for k in range(1,1201):
        x = 1.4*math.pi/rho*k/1200
        ensure(profile(x,rho)<=j+1e-12, 'global upper envelope')
    eps = 1e-4*min(u,1)
    fd = (profile(u+eps,rho)-2*profile(u,rho)+profile(u-eps,rho))/eps**2
    ensure(abs(fd+d) < max(.005*d,2e-6), 'curvature differentiation')

for rho in [.15,.2,.25,.35,.5]:
    u,j,d=optimum(rho)
    sharp=rho/math.e*math.exp(-math.pi/(2*rho))
    ensure(.90<(j-1)/sharp<1.02,'nonperturbative small-angle profile')

for rho in [12,20,50,100]:
    u,j,d=optimum(rho)
    approx=2-math.pi/rho+(1+math.pi**2/2)/rho**2
    ensure(abs(j-approx) < 12/rho**3,'large-rotation expansion')

# Finite grids approximate the infinite monomial spectrum; the tail contributes 1.
for rho in [.4,1,3,8]:
    u,j,d=optimum(rho)
    for a in [.7,2.5]:
        for phase in [0,.12,.28,.5,.72,.94]:
            n=1500
            t=u/(a*(n+phase))
            step=a*t
            best=max(1., *(profile(k*step,rho) for k in range(max(0,n-6),n+8)))
            predicted=a*a*d/2*min(phase,1-phase)**2
            observed=(j-best)/t**2
            ensure(abs(observed-predicted) < max(.012, .025*predicted), 'lattice phase law')

# Every multivariate sampling point must obey the largest angle/decay ratio law.
for a,omega in [([1.,2.], [2.,-1.]),([.5,2.,1.5],[-.6,0.,4.5]),([1.,3.],[0.,0.])]:
    rho=max(abs(w)/v for v,w in zip(a,omega))
    J=optimum(rho)[1] if rho else 1.
    for t in [.003,.02,.1,.5]:
        for ns in product(range(8),repeat=len(a)):
            lam=cmath.exp(t*sum(complex(-v,w)*n for v,w,n in zip(a,omega,ns)))
            ensure(abs(1-lam)<=J+1e-12, 'max-ratio envelope')

print('PASS',N,'finite diagnostics')
