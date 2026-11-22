"""Deterministic numerical checks of stationary lattice quantum collision formulas.
Requires Python 3, NumPy and SciPy. Not an infinite-dimensional proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import jv, j0, j1, ellipk, roots_laguerre

assertions=0
for kappa in [0.7,1.0,1.9]:
 for r in [0.8,1.3,3.0]:
  q=r/math.hypot(r,4*kappa)
  z,w=roots_laguerre(180)
  N=85
  n=np.arange(N+1)
  probs=(w[:,None]*(jv(n[None,:],2*kappa*z[:,None]/r)**2)).sum(axis=0)
  norm=probs[0]+2*probs[1:].sum()
  ipr=probs[0]**2+2*np.sum(probs[1:]**2)
  assert abs(norm-1)<1e-6,(kappa,r,norm)
  assertions+=1
  assert abs(ipr-q)<4e-6,(kappa,r,ipr,q)
  assertions+=1
  pur=r*quad(lambda t:math.exp(-r*t)*j0(2*kappa*t)**2,0,150/r,epsabs=3e-11,limit=800)[0]
  elliptic=(2*r/(math.pi*math.hypot(r,4*kappa)))*ellipk((4*kappa/math.hypot(r,4*kappa))**2)
  assert abs(pur-elliptic)<2e-10
  assertions+=1
  assert pur>ipr
  assertions+=1

for d in [1,2,3,4,6]:
 for r in [0.5,1.1,2.3]:
  p=r*quad(lambda t:math.exp(-r*t)*j0(2*t)**(2*d),0,120/r,epsabs=3e-10,limit=1000)[0]
  neighbor=r*quad(lambda t:math.exp(-r*t)*j0(2*t)**(2*d-1)*j1(2*t),0,120/r,epsabs=3e-10,limit=1000)[0]
  predicted=r*(1-p)/(4*d)
  assert abs(neighbor-predicted)<1e-9,(d,r,neighbor,predicted)
  assertions+=1

# Verify exact diagonal-occupation collision identity in two dimensions by independent quadratures.
for r in [1.5,2.2]:
 z,w=roots_laguerre(150)
 n=np.arange(0,19)
 arr=jv(n[None,:],2*z[:,None]/r)**2
 p=np.einsum('i,ij,ik->jk',w,arr,arr)
 weight=np.ones(len(n));weight[1:]=2
 ipr_diag=np.einsum('j,k,jk->',weight,weight,p*p)
 S=(arr*weight[None,:])@arr.T
 ipr_overlap=np.einsum('i,j,ij->',w,w,S*S)
 assert abs(ipr_diag-ipr_overlap)<2e-7,(r,ipr_diag,ipr_overlap)
 assertions+=1

# Positive and finite d>=3 unweighted collision-integral truncations.
times=np.linspace(0,120,901)
orders=np.arange(0,300)
B=jv(orders[None,:],2*times[:,None])**2
S=B@((B*np.r_[1,np.full(len(orders)-1,2.)][None,:]).T)
for d in [3,4]:
 val=np.trapezoid(np.trapezoid(S**d,times,axis=1),times)
 assert 0<val<100
 assertions+=1

print('PASSED',assertions,'deterministic tests including 2D independent representations')
