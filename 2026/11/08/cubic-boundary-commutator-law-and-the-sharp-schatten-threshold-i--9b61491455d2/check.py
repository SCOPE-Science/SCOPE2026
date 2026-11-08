"""Finite Jacobi block consistency checks for radial polyanalytic Toeplitz commutators."""
import numpy as np
from scipy.special import roots_jacobi, eval_jacobi, gammaln

counter=0

def b(j, alpha, xi):
    return np.sqrt(j*(j+alpha)*(j+xi)*(j+alpha+xi))/((2*j+alpha+xi)*np.sqrt((2*j+alpha+xi)**2-1))

def recurrence(n,alpha,xi):
    J=np.zeros((n,n))
    for j in range(n):
        J[j,j]=(1+(xi*xi-alpha*alpha)/((2*j+alpha+xi)*(2*j+alpha+xi+2)))/2
        if j:
            J[j,j-1]=J[j-1,j]=b(j,alpha,xi)
    return J

def quadrature(n,alpha,xi):
    nodes,weights=roots_jacobi(2*n+7,alpha,xi)
    t=(nodes+1)/2
    v=np.array([eval_jacobi(j,alpha,xi,nodes)*np.exp(-0.5*(gammaln(j+alpha+1)+gammaln(j+xi+1)-np.log(2*j+alpha+xi+1)-gammaln(j+alpha+xi+1)-gammaln(j+1))) for j in range(n)]).T
    v*=np.sqrt(weights/2**(alpha+xi+1))[:,None]
    gram=v.T@v
    # normalized polynomial on [-1,1] with jacobi quadrature weights: factor 2^(alpha+xi+1), cancelling in normalization from shifted [0,1]
    return t, v/np.sqrt(2**(alpha+xi+1)) if False else v, gram

# Use orthonormality from Gram numerically rather than reference scaling.
for alpha in [-0.4,0.,0.5,2.]:
 for n in [2,3,4]:
  for xi in [3,7,13,31]:
   t, v, gram=quadrature(n,alpha,xi)
   # orthonormalize from Gram, which also verifies no erroneous assumed normalization;
   assert np.max(np.abs(gram-np.eye(n)))<2e-10, (alpha,n,xi,gram)
   J=v.T @ (t[:,None]*v)
   J2=v.T @ (t[:,None]**2*v)
   J_exact=recurrence(n,alpha,xi)
   assert np.max(np.abs(J-J_exact))<3e-10,(alpha,n,xi, J,J_exact)
   C=J@J2-J2@J
   E=np.zeros((n,n)); E[n-2,n-1]=1; E[n-1,n-2]=-1
   pred=b(n,alpha,xi)**2*b(n-1,alpha,xi)*E
   assert np.max(np.abs(C-pred))<1e-10, (alpha,n,xi,C,pred)
   assert abs(np.linalg.svd(C,compute_uv=False)[0]-b(n,alpha,xi)**2*b(n-1,alpha,xi))<1e-10
   counter+=4
# Large-frequency sharp coefficient for polynomial pair.
for alpha in [-0.4,0.,0.75,2.]:
 for n in [2,3,5]:
  c=n*(n+alpha)*np.sqrt((n-1)*(n-1+alpha))
  for xi in [300,1000,10000]:
   ratio=(xi**3)*b(n,alpha,xi)**2*b(n-1,alpha,xi)/c
   assert abs(ratio-1)<(35*n+25*abs(alpha))/xi
   counter+=1
print('POLY_BERGMAN_COMMUTATOR_CHECKS_PASS',counter)
# For polynomial symbols h(t)=t+t^3, k(t)=t^2,
# the boundary jet mismatch is h''k'-h'k''=6*2-4*2=4.
for alpha in [-0.4,0,1.25]:
 for n in [2,3,4]:
  c=n*(n+alpha)*np.sqrt((n-1)*(n-1+alpha))
  for xi in [200,500,1000,3000]:
   T=recurrence(n+5,alpha,xi)
   H=(T+np.linalg.matrix_power(T,3))[:n,:n]
   K=np.linalg.matrix_power(T,2)[:n,:n]
   C=H@K-K@H
   ratio=np.linalg.svd(C,compute_uv=False)[0]*xi**3/(2*c)
   assert abs(ratio-1)<300*(n+abs(alpha))/xi, (alpha,n,xi,ratio)
   counter+=1
print('POLY_BERGMAN_GENERAL_JETS_PASS',counter)
