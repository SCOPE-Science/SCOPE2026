"""Verify log-cancellation mechanism: C(mu,nu) alone carries (1/2)|log eps|
per-dim growth, while debiased S cancels it (1D kink pair)."""
import numpy as np, sys
sys.path.insert(0,'output/artifacts')
from sinkhorn1d import sinkhorn_C, W2sq_half_1d
L=8.0; N=801
xs=np.linspace(-L,L,N)
X,Y=np.meshgrid(xs,xs,indexing='ij'); cmat=(X-Y)**2/2
def dens(pot):
    p=np.exp(-pot); p/=p.sum(); return p
mu=dens(xs**2/2+2.0*np.abs(xs)); nu=dens(xs**2/2+np.abs(xs))
w=W2sq_half_1d(mu,nu,xs,xs)
print("OT=",w)
for eps in [0.2,0.1,0.05,0.03,0.02]:
    C,_=sinkhorn_C(mu,nu,xs,xs,cmat,eps,niter=6000,tol=1e-10)
    Cmm,_=sinkhorn_C(mu,mu,xs,xs,cmat,eps,niter=6000,tol=1e-10)
    Cnn,_=sinkhorn_C(nu,nu,xs,xs,cmat,eps,niter=6000,tol=1e-10)
    S=C-0.5*(Cmm+Cnn)
    print(f"eps={eps}: (C-OT)/eps={(C-w)/eps:+.4f}  (S-OT)/eps={(S-w)/eps:+.4f}  ratio={abs((C-w)/eps)/max(abs((S-w)/eps),1e-9):.1f}x")
