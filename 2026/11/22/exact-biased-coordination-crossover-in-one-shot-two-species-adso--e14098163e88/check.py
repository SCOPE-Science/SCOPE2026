#!/usr/bin/env python3
"""Numerical consistency tests for a two-color single-attempt adsorption law on regular trees.

Requires Python 3.10+ and scipy. Run: python check.py
Proof of the all-degree result is in RESULT.md; these finite tests are not its proof.
"""
import math
import random
from functools import lru_cache
from scipy.integrate import solve_ivp

assertions = 0

def verify(ok, message):
    global assertions
    assert ok, message
    assertions += 1

def ode(z, p, t=1.0):
    q = 1 - p
    def rhs(time, s):
        a, b, A, B = s
        return (p*(1-b)**(z-1), q*(1-a)**(z-1),
                p*(1-b)**z, q*(1-a)**z)
    solution = solve_ivp(rhs, (0., t), (0.,0.,0.,0.),
                         method='DOP853',rtol=2e-12,atol=2e-13)
    verify(solution.success, f'ODE solution failed z={z},p={p}')
    return solution.y[:,-1]

# Exact symmetric solution and full-time color imbalance invariant.
for z in range(2,13):
    for t in (.15,.5,1.):
        a,b,A,B=ode(z,.5,t)
        total = 1-math.exp(-t) if z==2 else -math.expm1(-2*math.log1p((z-2)*t/2)/(z-2))
        verify(abs((A+B)-total)<8e-10, f'symmetric z={z},t={t}')
        verify(abs(A-B)<3e-11, f'symmetry z={z},t={t}')
for z in (2,3,4,6,10,30,100,500):
    for p in (.1,.3,.7,.9):
        t=.8
        a,b,A,B=ode(z,p,t)
        q=1-p
        verify(abs((A-B)-(p-q)*t)<3e-10,f'color imbalance z={z},p={p}')
        verify(abs(q*(1-(1-a)**z)-p*(1-(1-b)**z))<2e-10,f'first integral z={z},p={p}')
        verify(0<=A<=p*t+1e-9 and 0<=B<=q*t+1e-9,f'physical density z={z},p={p}')

# Independent exact 1D benchmark: do Amaral & dos Santos (2023), equation (1).
for p in (.1,.3,.5,.7,.9):
    for t in (.1,.6,1.):
        gamma=math.sqrt(p*(1-p));theta=math.sqrt(p/(1-p))
        formula=(2*theta+(theta*theta-1)*2*gamma*t+(theta*theta+1)*math.sinh(2*gamma*t)-2*theta*math.cosh(2*gamma*t))/(4*theta)
        a,b,A,B=ode(2,p,t)
        verify(abs(A-formula)<2e-9,f'published exact 1D benchmark p={p} t={t}')

# Independent finite-depth causal simulation: only ancestors with earlier attempts can matter.
# Depth 18 makes an unobserved earlier-clock path extraordinarily unlikely for z <= 4.
def tree_sample(z,p, rng, max_depth=18):
    def assess(time, heading, depth):
        if depth>=max_depth: return 0
        n = (z if depth==0 else z-1)
        for j in range(n):
            tchild=rng.random()
            if tchild >=time: continue
            species=1 if rng.random()<p else -1
            if species==-heading and assess(tchild,species,depth+1)==species:
                return 0
        return heading
    heading=1 if rng.random()<p else -1
    return assess(rng.random(),heading,0)

# This simulator generates random clocks only for probed child nodes, which is
# distributionally identical to assigning all the independent clocks in advance.
for z,p in ((2,.5),(3,.5),(4,.5),(3,.7),(4,.7)):
    rng=random.Random(811*z+round(p*100))
    n=12000
    samples=[tree_sample(z,p,rng) for _ in range(n)]
    empirical_A=sum(s==1 for s in samples)/n
    empirical_B=sum(s==-1 for s in samples)/n
    a,b,A,B=ode(z,p)
    verify(abs(empirical_A-A)<0.025,f'causal Monte Carlo A z={z},p={p}')
    verify(abs(empirical_B-B)<0.025,f'causal Monte Carlo B z={z},p={p}')

# The coefficient limit follows from dominated convergence, not this finite test.
for p in (.6,.7,.8,.9):
    for z in (100,500,2000):
        a,b,A,B=ode(z,p)
        limit=math.log(p/(2*p-1))
        verify(0<z*B<limit+1e-7, f'finite z minority approach p={p} z={z}')

print(f'PASS: {assertions} deterministic assertions')
