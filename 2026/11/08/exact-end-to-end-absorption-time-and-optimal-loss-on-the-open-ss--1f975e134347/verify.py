"""Independent finite-dimensional checks of an exact end-trapping identity."""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov, eigh
from math import isclose

def check(n,v,w,k):
 N=2*n
 bonds=np.array([v if i%2==0 else w for i in range(N-1)])
 H=np.diag(bonds,1)+np.diag(bonds,-1)
 B=-1j*H
 B[0,0]-=k/2
 X=solve_continuous_lyapunov(B.conj().T,-np.eye(N))
 estimate=float(X[-1,-1].real)
 formula=2*n/k+k*((n-1)/(2*w*w)+w**(2*n-2)/(4*v**(2*n)))
 return estimate,formula

k=0
for n in range(1,11):
 for v,w in [(1,1),(1,1.7),(1.4,1),(2,.9),(.7,.9)]:
  for rate in [.3,1,2.5]:
   a,b=check(n,v,w,rate)
   assert isclose(a,b,rel_tol=3e-6,abs_tol=2e-6),(n,v,w,rate,a,b)
   k+=1
print('LYAPUNOV CASES',k)
# Verify the trimmed-chain spectral endpoint formula independently.
k=0
for n in range(2,16):
 for v,w in [(.7,1.1),(2.,.6),(1.,1.),(.8,.9)]:
  N=2*n-1
  bonds=np.array([w if i%2==0 else v for i in range(N-1)])
  H=np.diag(bonds,1)+np.diag(bonds,-1)
  _,Q=eigh(H)
  ratios=np.sum((Q[-1,:]/Q[0,:])**2)
  expected=(2*n-2)*v*v/(w*w)+(w/v)**(2*n-2)
  assert isclose(ratios,expected,rel_tol=1e-7,abs_tol=1e-7),(n,v,w,ratios,expected)
  k+=1
print('SPECTRAL CASES',k)
