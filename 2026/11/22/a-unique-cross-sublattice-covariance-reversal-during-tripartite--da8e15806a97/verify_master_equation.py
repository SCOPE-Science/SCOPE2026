#!/usr/bin/env python3
"""Independent full finite-state CTMC propagation for irreversible dimers on K_{n,n,n}."""
from math import log
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

def limiting_cov(t):
 y=1.+2.*t
 return (4*(1-y**(-3))-3*log(y))/(18*y)

def full(n,t):
 states=[(a,b,c) for a in range(n+1) for b in range(n+1) for c in range(n+1)]
 index={s:k for k,s in enumerate(states)}
 row=[];col=[];value=[]
 for k,(a,b,c) in enumerate(states):
  events=[((a-1,b-1,c),a*b/n),((a-1,b,c-1),a*c/n),((a,b-1,c-1),b*c/n)]
  total=0.
  for next_s,rate in events:
   if rate>0:
    row.append(index[next_s]);col.append(k);value.append(rate)
    total+=rate
  row.append(k);col.append(k);value.append(-total)
 size=len(states)
 Q=coo_matrix((value,(row,col)),shape=(size,size)).tocsr()
 q0=np.zeros(size);q0[index[(n,n,n)]]=1.
 qt=expm_multiply(Q*t,q0)
 A=np.fromiter((a for a,b,c in states),dtype=float)
 B=np.fromiter((b for a,b,c in states),dtype=float)
 meanA=float(qt@A);meanB=float(qt@B)
 cov=float(qt@(A*B)-meanA*meanB)/n
 assert abs(qt.sum()-1)<1e-9
 assert qt.min()>-1e-9
 return cov,meanA/n

for t in [0.2,1.,2.]:
 pred=limiting_cov(t)
 values=[]
 for n in [4,8,12,16]:
  z,m=full(n,t)
  assert abs(m-1/(1+2*t))<0.1
  values.append(z)
  print('t=%.2f n=%d cov/n=%+.9f limit=%+.9f error=%+.9f'%(t,n,z,pred,z-pred))
 assert abs(values[-1]-pred)<abs(values[0]-pred), 'finite-size covariance not converging'
 assert abs(values[-1]-pred)<0.0055
print('All finite-state generator conservation, positivity and convergence checks PASS')
