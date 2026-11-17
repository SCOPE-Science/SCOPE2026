from itertools import combinations
import numpy as np
from scipy.optimize import minimize

def test(sizes):
 n=sum(sizes); vs=[];labels=[];off=0
 for j,a in enumerate(sizes):
  labels.extend([j]*a)
 E=[(i,k) for i,k in combinations(range(n),2) if labels[i]!=labels[k]]
 V=np.array([np.eye(n)[i]+np.eye(n)[k] for i,k in E]);
 a=max(sizes);b=n-a
 c0=np.full(n,2/n) if 2*a<=n else np.array([1/a if sizes[labels[i]]==a and a>n/2 else 1/b for i in range(n)])
 # all directions from feasible centered candidate
 rad=max(np.sum((V-c0)**2,axis=1))
 res=minimize(lambda z:z[-1], np.r_[c0,rad],method='SLSQP',constraints=[{'type':'ineq','fun':lambda z: z[-1]-np.sum((V-z[:-1])**2,axis=1) }], options={'ftol':1e-10,'maxiter':1500})
 if not res.success and abs(res.fun-rad)>1e-5:raise Exception('slsqp fail',sizes,res.message)
 if np.max(np.abs(res.x[:-1]-c0))>1e-4 or abs(res.fun-rad)>1e-5:raise Exception('sphere difference',sizes,res.x,c0,rad)
 # projections via constrained barycentric
 A=V.T
 mm=0
 for i,k in combinations(range(n),2):
  if labels[i]!=labels[k]:continue
  x=np.eye(n)[i]+np.eye(n)[k]
  a=sizes[labels[i]]; b=n-a; exact=.5+1/b
  p=np.zeros(n);p[i]=p[k]=.5; p[ [v for v in range(n) if labels[v]!=labels[i]]]=1/b
  assert abs(np.dot(x-p,x-p)-exact)<1e-9
  # stationarity nearest point p·(v-p)≥0
  gap=np.min((V-p)@(p-x))
  assert gap>=-1e-9,(sizes,i,k,gap)
  mm+=1
 return len(E),mm
if __name__=='__main__':
 tests=[(1,1,1),(2,2),(1,2,3),(1,1,5),(2,3,4),(1,2,2,4),(3,3,3),(2,2,5),(1,1,1,7),(1,4,5)]
 for x in tests:
  print(x,test(x))
