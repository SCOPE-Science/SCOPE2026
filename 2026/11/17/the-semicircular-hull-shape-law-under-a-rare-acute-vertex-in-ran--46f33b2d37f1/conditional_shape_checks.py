"""Numerical independent tests for the conditional rare-acute cyclic-polygon theorem."""
import math
import numpy as np
rng=np.random.default_rng(20261114)
for n in (4,5,6,8,10):
    N=500000
    gaps=rng.dirichlet(np.ones(n),size=N)
    count=(gaps+np.roll(gaps,1,axis=1)>0.5).sum(axis=1)
    assert np.max(count)<=2
    calc=np.array([(count==j).mean() for j in range(3)])
    truth=np.array([1-n*(n-2)/2**(n-1),n*(n-4)/2**(n-1),n/2**(n-2)])
    assert np.all(np.abs(calc-truth)<6*np.sqrt(truth*(1-truth)/N)+.001), (n,calc,truth)
    print('exact count',n,np.round(calc,6),np.round(truth,6))
# Importance sampling: force one designated acute vertex, whose two neighboring gaps sum beyond half.
for n in (30,80,200):
  N=3000
  # Conditional Beta(2,n-2) tail inverse numerically by bisection
  u=rng.random(N)
  lo=np.full(N,0.5);hi=np.ones(N)
  tail=lambda v:(1-v)**(n-2)*(1+(n-2)*v)
  target=u*tail(.5)
  for _ in range(65):
    mid=(lo+hi)*.5
    up=tail(mid)>target
    lo=np.where(up,mid,lo);hi=np.where(up,hi,mid)
  s=(lo+hi)*.5
  z=rng.random(N)
  gaps=np.empty((N,n));gaps[:,0]=s*z;gaps[:,1]=s*(1-z)
  rem=rng.dirichlet(np.ones(n-2),size=N)*(1-s)[:,None]
  gaps[:,2:]=rem
  ac=(gaps+np.roll(gaps,1,axis=1)>0.5).sum(axis=1)
  assert np.all((ac==1)|(ac==2))
  keep=ac==1
  # Rotate apex to angle zero: its adjacent gaps are g_0, g_1; gap order g_0 then g_1 then rest, apex is after g_0
  # points: vertex 0 at angle -2*pi*g0, vertex1 at 0, vertex2 at 2*pi*g1, etc
  edges=2*np.pi*gaps
  th=np.concatenate([np.zeros((N,1)),np.cumsum(edges,axis=1)[:,:-1]],axis=1)
  area=np.abs(np.sin(edges).sum(axis=1))*.5
  perimeter=2*np.sin(np.pi*gaps).sum(axis=1)
  targetarea=np.pi/2+np.sin(np.pi*z)
  targetperim=np.pi+2*(np.sin(np.pi*z/2)+np.cos(np.pi*z/2))
  ae=np.mean(np.abs(area[keep]-targetarea[keep]));pe=np.mean(np.abs(perimeter[keep]-targetperim[keep]))
  assert ae<3/n and pe<4/n, (n,ae,pe)
  print('shape',n,'unique fraction',round(keep.mean(),4),'mean abs area error',round(ae,5),'perimeter error',round(pe,5))
print('CONDITIONAL_CYCLIC_RARE_ACUTE_CHECKS_OK')
