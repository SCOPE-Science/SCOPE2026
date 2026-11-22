#!/usr/bin/env python3
"""Checks the stationary run-occupancy / positional-energy lag-asymmetry theorem.
Requires sympy, numpy, scipy; uses an independent event-driven trajectory check.
"""
import math
import random
import sympy as sp
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad

a,c,z=sp.symbols('a c z',positive=True)
k=a+c; ell=a+1
p=c/k
crr=sp.factor(p*(1-p))
cry=sp.factor(crr/ell)
crz=sp.factor(2*crr/(ell*(k+2)))
forward=(crz + 2*cry/(z+ell) + 2*crr/((z+ell)*(z+k)))/(z+2)
backward=crz/(z+k)
arrow=sp.factor(forward-backward)
want=2*a*c*(2*z+3*a+c+4)/((a+1)*k*(k+2)*(z+2)*(z+k)*(z+ell))
assert sp.simplify(arrow-want)==0
conv=2*a*c/((a+1)*k*(k+2))*(2/((z+2)*(z+k))+(k+2)/((z+2)*(z+k)*(z+ell)))
assert sp.simplify(want-conv)==0
assert sp.simplify(arrow.subs(z,0)-a*c*(3*a+c+4)/((a+1)**2*k**2*(k+2)))==0
assert sp.simplify(sp.limit(z*z*arrow,z,sp.oo)-4*a*c/((a+1)*k*(k+2)))==0
assert sp.factor(arrow.subs({a:1,c:1})-(z+4)/(4*(z+2)**3))==0
print('Exact identities: PASSED')

def fconv(t,k):
    if abs(k-2)<1e-10:
        return t*math.exp(-2*t)
    return (math.exp(-2*t)-math.exp(-k*t))/(k-2)

for aa,cc in [(1,1),(0.2,3),(4,0.2),(1,2),(0.8,0.6),(5,1)]:
    kk=aa+cc; el=aa+1
    r=aa*cc/kk**2
    vec=np.array([r,r/el,2*r/(el*(kk+2))])
    generator=np.array([[-kk,0,0],[1,-el,0],[0,2,-2]],dtype=float)
    pref=2*aa*cc/(el*kk*(kk+2))
    for t in (0.01,0.15,0.7,1.5,3.0):
        f=expm(generator*t)@vec
        numeric=f[2]-vec[2]*math.exp(-kk*t)
        triple=quad(lambda u:fconv(u,kk)*math.exp(-el*(t-u)),0,t,epsabs=1e-12)[0]
        analytic=pref*(2*fconv(t,kk)+(kk+2)*triple)
        assert analytic>0 and abs(numeric-analytic)<5e-12, (aa,cc,t,numeric,analytic)
print('Independent matrix-semigroup / positive-kernel checks: PASSED (30 tests)')

def evolve(x,sgn,dt):
    q=math.exp(-dt)
    return q*x+sgn*(1-q)

def trajectory(aa,cc,t,rng,T=18):
    state=0 if rng.random()<aa/(aa+cc) else (1 if rng.random()<0.5 else -1)
    x=0.0
    now=-T
    record=[]
    for stop in (0.0,t):
        while now<stop:
            rate=cc if state==0 else aa
            jump=rng.expovariate(rate)
            h=min(jump,stop-now)
            x=evolve(x,state,h)
            now+=h
            if jump<=h and now<stop:
                state=(1 if rng.random()<.5 else -1) if state==0 else 0
        record.append((x,state))
    return record

rng=random.Random(12177)
n=30000
observed=0.0
for _ in range(n):
    first,last=trajectory(1,1,1.0,rng)
    observed += (first[1]!=0)*last[0]**2-(last[1]!=0)*first[0]**2
observed/=n
expected=0.5*math.exp(-2)
assert abs(observed-expected)<0.02,(observed,expected)
print('Independent event-driven trajectories: PASSED',n,'samples, observed',round(observed,8),'exact',round(expected,8))
