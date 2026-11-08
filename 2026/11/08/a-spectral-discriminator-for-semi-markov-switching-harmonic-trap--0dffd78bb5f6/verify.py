"""Exact and independent tests for the alternating-renewal harmonic-trap theorem.
Uses standard-library fractions and random-number generators and numpy linear solves.
"""
from fractions import Fraction as Q
from math import log, isclose
from random import Random
import numpy as np


def formula(k, D, means, g, ell):
    q = [D / k[i] for i in range(2)]
    b = [q[0] + (q[1] - q[0]) * (1 - ell[1]) / (1 - ell[0]*ell[1]),
         q[1] + (q[0] - q[1]) * (1 - ell[0]) / (1 - ell[0]*ell[1])]
    h = [(1-g[i])/k[i] for i in range(2)]
    H = [(h[0]+g[0]*h[1])/(1-g[0]*g[1]),
         (h[1]+g[1]*h[0])/(1-g[0]*g[1])]
    M = [q[i]*means[i]+(b[i]-q[i])*(1-ell[i])/(2*k[i]) for i in range(2)]
    J = [q[i]*h[i]+(b[i]-q[i])*(g[i]-ell[i])/k[i] for i in range(2)]
    I = sum(M[i]/k[i]+(H[1-i]-1/k[i])*J[i] for i in range(2))/(means[0]+means[1])
    V = sum(M)/(means[0]+means[1])
    work = (k[0]-k[1])*(b[0]-b[1])/(2*(means[0]+means[1]))
    return I,V,work,b,M,J,H

# Witness: both protocols have exactly the same dwell means and ell_i,
# and hence exactly the same stationary state-conditioned second moments,
# mean squared displacement and switching work, but distinct spectral weight.
p = [[Q(1,4)]*4, [Q(9,40),Q(16,40),Q(1,40),Q(14,40)]]
k = [Q(2),Q(1)]

def witness(prob):
    g = [Q(1,4),sum(prob[n-1]/(2**n) for n in range(1,5))]
    ell = [Q(1,16),sum(prob[n-1]/(4**n) for n in range(1,5))]
    # scaled dwell length c=ln(2); stationary density involves one c denominator
    # and a constant term. Symbolically model c via direct recomposition below.
    # H, J, b all rational; M = q*m_i*c + constant correction.
    q = [Q(1,2),Q(1)]
    b=[q[0]+(q[1]-q[0])*(1-ell[1])/(1-ell[0]*ell[1]),
       q[1]+(q[0]-q[1])*(1-ell[0])/(1-ell[0]*ell[1])]
    h = [(1-g[i])/k[i] for i in range(2)]
    H = [(h[0]+g[0]*h[1])/(1-g[0]*g[1]),
         (h[1]+g[1]*h[0])/(1-g[0]*g[1])]
    J=[q[i]*h[i]+(b[i]-q[i])*(g[i]-ell[i])/k[i] for i in range(2)]
    tm=[Q(1),Q(5,2)]
    ttotal=sum(tm)
    static_var=sum(q[i]*tm[i] for i in range(2))/ttotal
    static_variance_correction=sum((b[i]-q[i])*(1-ell[i])/(2*k[i]) for i in range(2))/ttotal
    integrated_base=sum(q[i]*tm[i]/k[i] for i in range(2))/ttotal
    integrated_correction=sum((b[i]-q[i])*(1-ell[i])/(2*k[i]*k[i])+(H[1-i]-1/k[i])*J[i] for i in range(2))/ttotal
    workcoefficient=(k[0]-k[1])*(b[0]-b[1])/(2*ttotal)
    return dict(g=g,ell=ell,b=b,V0=static_var,V1=static_variance_correction,G0=integrated_base,G1=integrated_correction,W1=workcoefficient)

A,B=map(witness,p)
assert A['g']==[Q(1,4),Q(15,64)] and B['g']==[Q(1,4),Q(19,80)]
assert A['ell']==B['ell']==[Q(1,16),Q(85,1024)]
assert A['b']==B['b']==[Q(10441,10866),Q(2873,5433)]
assert A['V0']==B['V0']==Q(6,7)
assert A['V1']==B['V1']==-Q(1565,50708)
assert A['W1']==B['W1']==Q(1565,25354)
assert A['G0']==B['G0']==Q(11,14)
assert A['G1']==-Q(2407701,24441256)
assert B['G1']==-Q(2995809,30526216)
assert B['G1']-A['G1']==Q(341004,919602257)>0
v=Q(6,7)-Q(1565,50708)/log(2)
gA=Q(11,14)-Q(2407701,24441256)/log(2)
gB=Q(11,14)-Q(2995809,30526216)/log(2)
assert isclose(float(v),.8126169886607393,rel_tol=1e-13)
assert isclose(float(gA),.6435948180141233,rel_tol=1e-13)
assert isclose(float(gB),.6441297936255668,rel_tol=1e-13)
assert gB>gA

# Independent exact birth-recursion and renewal-reward identities.
for x in [A,B]:
  b=x['b'];ell=x['ell'];q=[Q(1,2),Q(1)]
  assert b[1]==q[0]+(b[0]-q[0])*ell[0]
  assert b[0]==q[1]+(b[1]-q[1])*ell[1]
  assert (x['V0']+x['V1']/log(2))>0

# Independent Markov-chain (exponential sojourn) computation of covariance,
# via integrated forward matrix covariance, not the renewal derivation.
rng=Random(9042)
for idx in range(240):
  kk=np.array([10**rng.uniform(-0.8,0.8),10**rng.uniform(-0.8,0.8)])
  tau=np.array([10**rng.uniform(-0.8,0.8),10**rng.uniform(-0.8,0.8)])
  DD=10**rng.uniform(-0.8,0.8)
  gg=1/(1+kk*tau)
  ll=1/(1+2*kk*tau)
  rr=1/tau
  I,V,W,*_=formula(kk,DD,tau,gg,ll)
  pi=tau/tau.sum()
  birthmatrix=np.array([[2*kk[0]+rr[0],-rr[1]],[-rr[0],2*kk[1]+rr[1]]])
  state_m=np.linalg.solve(birthmatrix,2*DD*pi)
  dynamics=np.array([[kk[0]+rr[0],-rr[1]],[-rr[0],kk[1]+rr[1]]])
  direct_I=np.linalg.solve(dynamics,state_m).sum()
  direct_V=state_m.sum()
  assert np.isclose(I,direct_I,rtol=2e-12,atol=2e-12),(idx,I,direct_I)
  assert np.isclose(V,direct_V,rtol=2e-12,atol=2e-12),(idx,V,direct_V)

# Equal-stiffness invariance for completely different semi-Markov dwell transforms.
for idx in range(80):
  kk=10**rng.uniform(-0.8,0.8)
  DD=10**rng.uniform(-0.8,0.8)
  t1=10**rng.uniform(-0.8,0.8)
  t2=10**rng.uniform(-0.8,0.8)
  e1=np.exp(-kk*t1)
  e2=np.exp(-kk*t2)
  I,V,W,*_=formula([kk,kk],DD,[t1,t2],[e1,e2],[e1**2,e2**2])
  assert np.isclose(I,DD/(kk**2),rtol=1e-12)
  assert np.isclose(V,DD/kk,rtol=1e-12)
  assert np.isclose(W,0,atol=1e-12)

print('PASS: exact two-protocol witness; 240 independent two-state Markov matrix tests; 80 equal-stiffness invariance checks.')
print('Stationary variance (both):',v)
print('Work injection rate (both):',float(Q(1565,25354)/log(2)))
print('Integrated covariance protocols P and Q:',gA,gB,'difference:',gB-gA)
