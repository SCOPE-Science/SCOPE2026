#!/usr/bin/env python3
"""Finite checks for Euclidean support on the spanning-tree polytope of K_(2,q)."""
import itertools
import math
import numpy as np
from scipy.special import ndtr, ndtri
from scipy.integrate import quad

rng=np.random.default_rng(134271)
count=0
for q in range(2,8):
    trees=[]
    for bridge in range(q):
        rest=[i for i in range(q) if i!=bridge]
        for bits in itertools.product((0,1), repeat=q-1):
            x=np.zeros((2,q),dtype=np.int8)
            x[:,bridge]=1
            for i,k in enumerate(rest): x[bits[i],k]=1
            assert x.sum()==q+1
            trees.append(x)
    assert len(trees)==q*2**(q-1)
    mats=np.array(trees,dtype=np.float64).reshape((-1,2*q))
    for _ in range(91):
        g=rng.normal(size=(2,q))
        target=np.maximum(g[0],g[1]).sum()+np.minimum(g[0],g[1]).max()
        direct=np.max(mats@g.reshape(-1))
        assert math.isclose(direct,target,rel_tol=1e-12,abs_tol=1e-12)
        count+=1
print('ENUMERATED_GAUSSIAN_SUPPORT_OK',count)

# Exact distribution at selected values q and x, and normalization of its density.
for q in (2,3,7,100,10000):
    def f(t):
        Q=ndtr(-t)
        return q*(1-Q*Q)**(q-1)*2*Q*math.exp(-t*t/2)/math.sqrt(2*math.pi)
    total=quad(f,-10,10,epsabs=2e-10)[0]
    assert abs(total-1)<2e-8,(q,total)
print('EXACT_CDF_DENSITY_OK')

# Extreme-value CDF and Gaussian-support expectation asymptotics, diagnostic only.
for q in (100,10000,1000000):
    b=ndtri(1-q**(-0.5)); a=q**(-0.5)/(2*math.exp(-b*b/2)/math.sqrt(2*math.pi))
    if q>=10000:
        for x in (-1.,0.,1.):
            F=(1-ndtr(-(b+a*x))**2)**q
            Fg=math.exp(-math.exp(-x))
            assert abs(F-Fg) < (0.20 if q==10000 else 0.09),(q,x,F,Fg)
print('GUMBEL_CDF_DIAGNOSTIC_OK')

# Min-maximum overshoot conditional on high minimum: direct Mills-ratio verification.
for b in (2.0,3.0,5.0):
    for u in (0.5,1.0,2.0):
        survival=ndtr(-b-u/b)/ndtr(-b)
        assert abs(survival-math.exp(-u))<0.18,(b,u,survival)
print('EXP_OVERSHOOT_DIAGNOSTIC_OK')
print('GAUSSIAN_BRIDGE_POLYTOPE_PASS')
