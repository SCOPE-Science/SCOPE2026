"""Numerical and exact checks for the Gaussian two-sketch Nyström rank-one law.

This is a reproducibility aid; the continuum and distributional claims use the
analytical argument in RESULT.md, not finite simulation.
"""
from fractions import Fraction
from math import sqrt, gamma
import numpy as np
from scipy.special import betainc, beta

count=0

def check(test, msg):
    global count
    assert bool(test), msg
    count+=1

# Exact codimension-one oblique projection constructed with rational data.
k=5; n=k+1; t=k+4
X=np.zeros((t,k)); X[:k,:]=np.eye(k)
y=np.zeros(t); y[0]=2
Psi_T=np.column_stack([X,y])
Omega=np.eye(n)[:,:k]
P=Omega@np.linalg.pinv(Psi_T@Omega)@Psi_T
Svals,U_or_V=None,None
U,S,Vh=np.linalg.svd(P,full_matrices=False)
P1=S[0]*np.outer(U[:,0],Vh[0])
lam=np.linalg.eigvalsh((P1+P1.T)/2)
check(np.allclose(P[:k,:k],np.eye(k)),"Projection block")
check(np.allclose(P[:k,-1], np.array([2.,0.,0.,0.,0.])),"Oblique block")
check(np.allclose(P@P,P),"Idempotence")
check(np.allclose(S[0],np.sqrt(5)),"Top singular value")
check(np.allclose(lam[0],(1-np.sqrt(5))/2),"Negative eigenvalue")
check(np.allclose(lam[-1],(1+np.sqrt(5))/2),"Positive eigenvalue")
check(np.allclose(np.linalg.eigvalsh((P+P.T)/2)[0],lam[0]),"Rank truncation retains defect")

# Independently form random two-sided Gaussian approximation and its geometric
# least-squares coefficient to check the reduction used by the proof.
rng=np.random.default_rng(20261020)
for k,l in [(1,1),(2,2),(5,4),(6,5),(8,7)]:
  n=k+1; t=k+l
  for it in range(32):
    Omega=rng.standard_normal((n,k)); Psi=rng.standard_normal((n,t))
    Q,_=np.linalg.qr(Omega,mode='reduced')
    v=np.linalg.svd(Q.T,full_matrices=True)[2][-1]
    X=Psi.T@Q; y=Psi.T@v
    b=np.linalg.lstsq(X,y,rcond=None)[0]
    normb=np.linalg.norm(b)
    P=Omega@np.linalg.pinv(Psi.T@Omega)@Psi.T
    Pf=Q@np.linalg.pinv(X)@Psi.T
    check(np.allclose(P,Pf,rtol=1e-8,atol=1e-8),"QR equivalence")
    check(np.allclose(P@P,P,rtol=1e-8,atol=1e-8),"Projector identity")
    U,S,Vh=np.linalg.svd(P,full_matrices=False)
    P1=S[0]*np.outer(U[:,0],Vh[0])
    eig=np.linalg.eigvalsh((P1+P1.T)/2)
    check(np.isclose(S[0],sqrt(1+normb**2),rtol=1e-8,atol=1e-8),"Oblique norm")
    check(np.isclose(eig[0],(1-sqrt(1+normb**2))/2,rtol=1e-8,atol=1e-8),"Negativity exact law")
    check(np.isclose(eig[-1],(1+sqrt(1+normb**2))/2,rtol=1e-8,atol=1e-8),"Positive exact law")

# Compare direct least-squares sampling with the F/Beta expression.
# This finite check is not a proof of a distributional identity.
for k,l in [(5,4),(7,8)]:
    t=k+l; nu=l+1; threshold=0.25
    trial_count=3000
    values=np.empty(trial_count)
    for i in range(trial_count):
        X=rng.standard_normal((t,k)); y=rng.standard_normal(t)
        b=np.linalg.lstsq(X,y,rcond=None)[0]
        values[i]=(sqrt(1+np.dot(b,b))-1)/2
    empirical=(values>threshold).mean()
    predicted=betainc(nu/2,k/2,(1+2*threshold)**-2)
    check(abs(empirical-predicted)<0.035,"Gaussian least squares / beta law")
    expected=(beta((nu-1)/2,k/2)/beta(nu/2,k/2)-1)/2
    check(abs(values.mean()-expected)<0.08,"Expected negativity / beta moments")
    assert np.min(values)>0

# Special identity from elementary beta values.
k,l=6,4
nu=l+1
expected=(beta((nu-1)/2,k/2)/beta(nu/2,k/2)-1)/2
check(abs(expected-41/128)<1e-13,"Exact gamma ratio 41/128 for k=6,ell=4")
print(f"PASS {count} checks; tested deterministic algebra, full Gaussian sketches and beta-law sampling")
