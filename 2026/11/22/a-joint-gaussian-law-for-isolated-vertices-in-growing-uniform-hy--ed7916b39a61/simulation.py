"""Seeded Monte Carlo sanity check of exact no-repeat growing-hypergraph transition law."""
import numpy as np
from math import comb
from fractions import Fraction as F
from checker import coefficients

def simulate(k=3,p=0.5,steps=1200,replications=16000,seed=261114824):
 rng=np.random.default_rng(seed)
 N=np.full(replications,k,dtype=np.int64)
 I=N.copy(); E=np.zeros(replications,dtype=np.int64)
 for t in range(steps):
  birth=rng.random(replications)<p
  N[birth]+=1; I[birth]+=1
  edge=~birth
  active=np.nonzero(edge)[0]
  if len(active)==0:continue
  # choose uniformly among as-yet-unused k-sets; old sets contain no isolated vertices
  total=np.array([comb(int(n),k) for n in N[active]],dtype=np.int64)
  active=active[E[active]<total]
  waiting=active
  while len(waiting):
   yy=rng.hypergeometric(I[waiting],N[waiting]-I[waiting],k)
   old_space=np.array([comb(int(n-i),k) if n-i>=k else 0 for n,i in zip(N[waiting],I[waiting])],dtype=np.int64)
   reject=(yy==0)&(old_space>0)&(rng.random(len(waiting))<np.divide(E[waiting],old_space,where=old_space>0,out=np.zeros(len(waiting))))
   accept=~reject
   I[waiting[accept]]-=yy[accept]
   E[waiting[accept]]+=1
   waiting=waiting[reject]
 u=N/1.;v=I/1.
 return np.cov(u,v,ddof=1)/steps

if __name__=='__main__':
 for k,p in [(3,0.5),(4,0.5),(3,0.7)]:
  s=simulate(k,p)
  nn,ni,ii=map(float,coefficients(k,F(p).limit_denominator(1000))[2:5])
  expected=np.array([[nn,ni],[ni,ii]])
  print(k,p,'observed covariance / t:',s.flatten(),'theory:',expected.flatten(),'max relative error:',np.max(abs((s-expected)/expected)))
  assert np.max(abs((s-expected)/expected))<0.14
 print('PASS seeded finite-size covariance sanity checks')
