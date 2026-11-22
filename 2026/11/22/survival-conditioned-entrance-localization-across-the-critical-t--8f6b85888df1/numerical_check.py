import numpy as np
from scipy.special import ive
from math import sqrt,erf,log,pi
rho=.5;d=2.;a=2.;b=.5
# Optional finite-time illustration; SciPy and NumPy are required.
# These calculations are not used as proofs of the infinite limits.
for beta in [1,2,3]:
 for t in [100,1000,10000]:
  i=np.arange(1,int(20*sqrt(d*t))+1,dtype=float)
  j=np.arange(1,60)
  B=ive(np.abs(i[:,None]-j),d*t)-ive(i[:,None]+j,d*t)
  p=(i[:,None]**(-beta)*B)@(rho**j)
  p=p/p.sum()
  if beta==1:
   v=float(p[i<=sqrt(t)].sum());tar=erf(1/sqrt(2*d));desc='start<=sqrt(t)'
  elif beta==2:
   v=float(p[i<=t**.25].sum());tar=.5;desc='start<=t^1/4'
  else:
   v=float(p[0]);tar=6/pi**2;desc='start=1'
  print(beta,t,desc,round(v,6),'limit',round(tar,6))
