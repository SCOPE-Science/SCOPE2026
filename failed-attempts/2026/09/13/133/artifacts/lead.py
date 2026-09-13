import numpy as np
# Second-order Taylor structure: |Delta| = (1/2)|D2| |a||b| + O(|a||b|(|a|^theta+|b|^theta))
# leading coefficient K(x) = |d^2/(du ds) [series]|; compute via high-order mixed difference.
import sys
sys.path.insert(0, 'output/artifacts')
from delta import Delta, r
n=120
xs=np.linspace(0,1,n,endpoint=False)
h=0.004
K=np.zeros((n,n))
X=np.zeros((n,n,2))
for i in range(n):
  for j in range(n):
    x=np.array([xs[i],xs[j]])
    dpp=Delta(x,h,h,N=14); dpm=Delta(x,h,-h,N=14); dmp=Delta(x,-h,h,N=14); dmm=Delta(x,-h,-h,N=14)
    K[i,j]=(dpp-dpm-dmp+dmm)/(4*h*h)
print("K stats: min|K|",np.abs(K).min(),"mean|K|",np.abs(K).mean(),"max",np.abs(K).max())
idx=np.unravel_index(np.argmin(np.abs(K)),(n,n))
print("argmin K",xs[idx[0]],xs[idx[1]],"K=",K[idx])
print("pct|K|",np.percentile(np.abs(K),[0,1,5,25,50]))
np.save('output/artifacts/K.npy',K)
