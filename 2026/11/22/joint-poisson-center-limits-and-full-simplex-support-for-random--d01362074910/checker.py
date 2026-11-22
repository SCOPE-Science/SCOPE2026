#!/usr/bin/env python3
"""Deterministic finite diagnostics for Poisson linear-envelope optimizers.
Requires numpy and scipy. The theorem is proved analytically; finite tests do not prove convergence.
"""
import math
import numpy as np
from scipy.optimize import linprog

rng=np.random.default_rng(27182818)
checks=0
results={}
for d in (2,3,4):
  for alpha in (0.5,1.0,2.0):
    successes=0
    for rep in range(90):
      # Poisson atoms with radial coordinate s<=T; mean T**alpha.
      T=25 if alpha<=1 else 6
      m=int(rng.poisson(T**alpha))
      m=max(10*d,m)
      # Conditional simulation with fixed m checks only LP structure, not Poisson count distribution.
      depths=T*rng.random(m)**(1/alpha)
      directions=rng.normal(size=(m,d))
      directions/=np.linalg.norm(directions,axis=1)[:,None]
      # Maximize h subject to h-u_i.dot(z) <= s_i.
      A=np.column_stack([-directions,np.ones(m)])
      c=np.r_[np.zeros(d),-1.]
      sol=linprog(c,A_ub=A,b_ub=depths,bounds=[(None,None)]*(d+1),method='highs')
      assert sol.success, ('unbounded LP for sampled directions',d,alpha,rep,sol.message)
      z=sol.x[:d]; h=sol.x[d]
      slacks=depths+directions@z-h
      assert min(slacks)>-1e-7;checks+=1
      active=np.flatnonzero(abs(slacks)<1e-6)
      assert len(active)==d+1, ('non-generic finite solver instance',d,alpha,rep,active,slacks[active]);checks+=1
      U=directions[active]
      bary=np.linalg.solve(np.vstack([U.T,np.ones(d+1)]),np.r_[np.zeros(d),1])
      assert np.min(bary)>1e-10;checks+=1
      assert np.linalg.norm(U.T@bary)<1e-8;checks+=1
      assert abs(bary.sum()-1)<1e-9;checks+=1
      # Perturbing the optimizer in several directions must reduce the envelope.
      for j in range(4*d):
        v=rng.normal(size=d);v/=np.linalg.norm(v)
        step=0.12 + 0.05*j
        newh=np.min(depths+directions@(z+step*v))
        assert newh<h-1e-9;checks+=1
      successes+=1
    results[f'{d}d_alpha_{alpha}']=successes
print('Passed',checks,'finite checks; successful LP instances:',results)
