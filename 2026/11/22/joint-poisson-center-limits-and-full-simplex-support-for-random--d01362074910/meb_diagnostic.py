#!/usr/bin/env python3
"""Finite-sample numerical sanity checks for planar uniform-disk enclosing circles.
The simulation is not proof of any limiting assertion.
"""
import math
import numpy as np
from scipy.optimize import linprog
rng=np.random.default_rng(3141592653)

def circle3(a,b,c):
    ab=b-a;ac=c-a
    den=2*(ab[0]*ac[1]-ab[1]*ac[0])
    if abs(den)<1e-13:
        pts=[(a,b),(a,c),(b,c)]
        x,y=max(pts,key=lambda ab:np.sum((ab[0]-ab[1])**2))
        cent=(x+y)/2
        return cent, np.linalg.norm(x-cent)
    x=np.array([(np.dot(ab,ab)*ac[1]-np.dot(ac,ac)*ab[1])/den,
                (np.dot(ac,ac)*ab[0]-np.dot(ab,ab)*ac[0])/den])+a
    return x, np.linalg.norm(a-x)

def meb(points):
    c=np.zeros(2);r=-1
    for i,p in enumerate(points):
      if np.linalg.norm(p-c)<=r+1e-10:continue
      c=p.copy();r=0
      for j in range(i):
        q=points[j]
        if np.linalg.norm(q-c)<=r+1e-10:continue
        c=(p+q)/2;r=np.linalg.norm(p-c)
        for k in range(j):
          s=points[k]
          if np.linalg.norm(s-c)<=r+1e-10:continue
          c,r=circle3(p,q,s)
    return c,r

checks=0
for n in (50,150,400):
    k_counts={2:0,3:0};diffs=[]
    for rep in range(24):
      ang=rng.uniform(0,2*np.pi,n)
      radial=np.sqrt(rng.uniform(0,1,n))
      x=np.stack([radial*np.cos(ang),radial*np.sin(ang)],axis=1)
      # fixed random order inherited from iid sample
      c,r=meb(x)
      distances=np.linalg.norm(x-c,axis=1)
      assert max(distances)<=r+1e-7; checks+=1
      k=int(np.sum(np.abs(distances-r)<1e-7))
      assert k in (2,3), (n,rep,k);checks+=1
      k_counts[k]+=1
      bn=1/(2*n)
      depths=(1-radial)/bn
      U=x/radial[:,None]
      sol=linprog(np.array([0,0,-1]),A_ub=np.c_[-U,np.ones(n)],b_ub=depths,bounds=[(None,None)]*3,method='highs')
      assert sol.success;checks+=1
      diffs.append((np.linalg.norm(c/bn-sol.x[:2]),abs((1-r)/bn-sol.x[2])))
    print('n',n,'support_counts',k_counts,'mean_scaled_center_gap',round(np.mean([v[0] for v in diffs]),4),'mean_scaled_radius_gap',round(np.mean([v[1] for v in diffs]),4))
print('checks_passed',checks)
