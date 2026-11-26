import itertools
import numpy as np
from numpy.linalg import norm, eigvals
from scipy.linalg import expm

def run(n,edges,p=.39,dt=.7):
 mat=np.zeros((n*n,n*n),dtype=complex)
 for bits in itertools.product((0,1),repeat=len(edges)):
  L=np.zeros((n,n),dtype=float)
  for included,(u,v) in zip(bits,edges):
   if included:
    L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
  U=expm(-1j*dt*L)
  w=np.prod([p if x else 1-p for x in bits]);mat+=w*np.kron(U.conj(),U)
 u=np.ones((n,1))/np.sqrt(n)
 P=u@u.T
 psi=np.arange(1,n+1,dtype=float)+1j*np.arange(n,0,-1,dtype=float);psi/=norm(psi);rho=np.outer(psi,psi.conj())
 predicted=np.trace(P@rho)*P + np.trace((np.eye(n)-P)@rho)*(np.eye(n)-P)/(n-1)
 v=rho.reshape(-1,order='F')
 for _ in range(650):v=mat@v
 gap=1-np.sort(np.abs(eigvals(mat)))[-3]
 err=norm(v-predicted.reshape(-1,order='F'))
 print(n,len(edges),'third_gap',gap,'error',err,'initial_uniform_mass',np.trace(P@rho).real,'pred_offdiag',predicted[0,1])
 assert err < 2e-7
for n,edges in [(2,[(0,1)]),(3,[(0,1),(1,2)]),(4,[(0,1),(1,2),(2,3)]),(4,[(0,1),(1,2),(2,3),(3,0)]),(4,[(0,1),(1,2),(2,3),(3,0),(0,2),(1,3)])]: run(n,edges)
# resonance counterexample two vertices at pi => all unitaries are identity
n=2; L=np.array([[1,-1],[-1,1]])
assert norm(expm(-1j*np.pi*L)-np.eye(n))<1e-12
print('resonance at pi verified')
