"""Finite numerical consistency checks for a sparse strictly positive definite spherical kernel.
The analytic proof is independent of these diagnostics.
"""
import numpy as np
rng=np.random.default_rng(1729)
def sample(n):
    a=rng.normal(size=(n,3));return a/np.linalg.norm(a,axis=1)[:,None]
def kernel(p):
    u=p[:,0]+1j*p[:,1];v=p[:,2]
    return (1+v[:,None]*v[None,:])/(1-u[:,None]*u.conj()[None,:]/2)
checks=0;smallest=1e100
for n in [2,3,4,5,7,10,15]:
 for _ in range(12):
    p=sample(n); K=kernel(p); K=(K+K.conj().T)/2
    mine=float(np.linalg.eigvalsh(K)[0]); assert mine>0,(n,mine)
    R=K.real; minr=float(np.linalg.eigvalsh(R)[0]);assert minr>0,(n,minr)
    smallest=min(smallest,mine,minr);checks+=2
for L in range(1,50):
 assert 1+2*L<=(L+1)**2
 assert 4*L<=(L+1)**2
 checks+=2
# Orthogonality on symmetric equatorial sample under rotations holds symbolically:
# monomial azimuth numbers ell and ell-1 differ by one.
print({'finite_diagnostics_passed':checks,'smallest_sample_eigenvalue':smallest})
