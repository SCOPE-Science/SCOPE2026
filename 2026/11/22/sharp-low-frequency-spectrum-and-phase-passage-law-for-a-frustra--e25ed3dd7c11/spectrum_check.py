import numpy as np
from scipy.linalg import eigh
from math import comb
for n in [3,4,5,6,8,10,12,16,20,28]:
 N=6*n; C=np.zeros((N,N)); mass=np.ones(N)
 # corner j index j, cube j internal level k index 6 + j*(n-1)+(k-1), endpoints junction j and j+1
 for j in range(6):
  z=[j]+[6+j*(n-1)+k-1 for k in range(1,n)]+[(j+1)%6]
  for k in range(1,n):mass[z[k]]=comb(n,k)
  for k in range(n):
   conductance=comb(n,k)*(n-k)/2
   a,b=z[k:k+2];C[a,a]+=conductance;C[b,b]+=conductance;C[a,b]-=conductance;C[b,a]-=conductance
 eig=eigh(C,np.diag(mass),subset_by_index=[0,6],eigvals_only=True)
 print(n, np.round(eig[1:6]*(2**n)/n,7),flush=True)
