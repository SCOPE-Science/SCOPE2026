#!/usr/bin/env python3
"""Standalone tests for a two-dimensional sketched Ritz collision law.
The infinite-dimensional/asymptotic conclusions require the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad

rng=np.random.default_rng(14523)

def profile(t):
    assert t >= 0
    g=lambda z: math.sqrt(1-z*z)/(1+z*z)*math.exp(-t*t*z*z/8)
    return math.sqrt(2)/math.pi * math.exp(-t*t/8)*quad(g,0,1,epsabs=1e-13)[0]

def complex_mask_2x2(M):
    return (M[...,0,0]-M[...,1,1])**2+4*M[...,0,1]*M[...,1,0]<0

# Exact Schur similarity and SPD of the 4 by 4 block; QR handles whitening.
for s in (5,9,20,50):
    for t in (0,1,3):
        H=np.diag([2-t/(2*math.sqrt(s)),2+t/(2*math.sqrt(s))])
        A=np.block([[H,np.eye(2)],[np.eye(2),2*np.eye(2)]])
        if np.linalg.eigvalsh(A)[0] <= 0: continue
        S=rng.normal(size=(s,4))/math.sqrt(s)
        X=np.eye(4,2)
        P=S@X
        Q=S[:,2:4]
        U,R=np.linalg.qr(P,mode='reduced')
        Rinv=np.linalg.inv(R)
        B=X@Rinv
        Ms=U.T@S@A@B
        M=np.linalg.solve(P.T@P,P.T@S@A@X)
        assert np.allclose(Ms,R@M@np.linalg.inv(R),atol=1e-12)
        assert np.allclose(M,H+np.linalg.solve(P.T@P,P.T@Q),atol=1e-12)
        assert np.allclose(B.T@S.T@S@B,np.eye(2),atol=1e-12)
        assert complex_mask_2x2(Ms)==complex_mask_2x2(M)


# Exact four-dimensional construction: subspace embedding can be arbitrarily
# close to an isometry even as the sketched pair stays nonreal.
for eps in (0.01,0.1,0.35):
    J=np.array([[0.,-1.],[1.,0.]])
    W=np.block([[np.eye(2),eps*J],[eps*J.T,np.eye(2)]])
    lam,V=np.linalg.eigh(W)
    assert np.allclose(lam,np.array([1-eps,1-eps,1+eps,1+eps]))
    S=(V* np.sqrt(lam))@V.T
    rho=0.4; gap=rho*eps
    H=np.diag([2-gap/2,2+gap/2])
    A=np.block([[H,rho*np.eye(2)],[rho*np.eye(2),2*np.eye(2)]])
    X=np.eye(4,2)
    M=np.linalg.solve(X.T@W@X, X.T@W@A@X)
    assert np.allclose(M,H+rho*eps*J)
    assert complex_mask_2x2(M)
    assert np.linalg.eigvalsh(A).min()>0

# In ambient dimension three an exactly repeated two-dimensional Ritz
# block has a rank-one residual perturbation; the nontrivial eigenvalues
# of the projected matrix must remain real.
for _ in range(200):
    a=rng.standard_normal(2)
    c=rng.uniform(1,3)
    H=np.eye(2)*c
    A=np.block([[H,a[:,None]],[a[None,:],np.ones((1,1))*2]])
    S=rng.standard_normal((5,3))
    X=np.eye(3,2)
    M=np.linalg.lstsq(S@X,S@A@X,rcond=None)[0]
    assert np.linalg.matrix_rank(M-c*np.eye(2),tol=1e-9)<=1
    assert (np.linalg.eigvals(M).imag==0).all()

# Probabilistic identity: shifted 2x2 Ginibre, compare both exact integral and
# independent spherical-cone simulation without diagonalization.
for t in (0,0.5,1,2,4):
    n=350000
    G=rng.standard_normal((n,2,2))
    G[:,0,0]-=t/2
    G[:,1,1]+=t/2
    observed=complex_mask_2x2(G).mean()
    expected=profile(t)
    err=6*math.sqrt(expected*(1-expected)/n)+0.001
    print('shifted_Ginibre',t,'formula',round(expected,8),'MC',round(observed,8),'tol',round(err,8))
    assert abs(observed-expected)<err
assert abs(profile(0)-(1-1/math.sqrt(2)))<1e-13
assert all(profile(t)>profile(t+0.1)>0 for t in (0,0.5,2,5))
for t in (8,12,16):
    approximate=2/(math.sqrt(math.pi)*t)*math.exp(-t*t/8)
    ratio=profile(t)/approximate
    print('large_t',t,round(ratio,8))
assert abs(profile(16)/(2/(math.sqrt(math.pi)*16)*math.exp(-16*16/8))-1)<0.025

# Finite sketch: column-entry independent Gaussian and independent Rademacher,
# zero- and nonzero-critical gaps.  Centered binomial uncertainty respected.
for kind in ('gaussian','rademacher'):
    for s in (48,128,384):
        n=12000
        # U,V have shape (batch,s,2); using chunks keeps memory small.
        for t in (0,2):
            acc=0
            for j in range(0,n,400):
                m=min(400,n-j)
                if kind=='gaussian':
                    U=rng.standard_normal((m,s,2)); V=rng.standard_normal((m,s,2))
                else:
                    U=rng.choice((-1.,1.),size=(m,s,2)); V=rng.choice((-1.,1.),size=(m,s,2))
                gram=np.einsum('bni,bnj->bij',U,U)
                cross=np.einsum('bni,bnj->bij',U,V)
                invprod=np.linalg.solve(gram,cross)
                invprod[:,0,0]-=t/(2*math.sqrt(s))
                invprod[:,1,1]+=t/(2*math.sqrt(s))
                acc+=int(complex_mask_2x2(invprod).sum())
            p=acc/n
            q=profile(t)
            # bias at finite s is small but may exceed sampling error:
            assert abs(p-q)<0.085,(kind,s,t,p,q)
            print('sketch',kind,s,t,round(p,6),'limit',round(q,6))
print('VERIFY_OK')
