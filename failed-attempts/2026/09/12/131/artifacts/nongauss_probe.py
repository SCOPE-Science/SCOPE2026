"""Non-Gaussian 1D probe: mixtures / scaled-kink potentials.
Family: rho_k(x) propto exp(-x^2/2 - A|x|^p), 1<=p<2 (still 1-log-concave),
pair against N(0,1). Track diff/eps (R1) at small eps: does it stay bounded
(O(eps) rate) or blow up like log(1/eps) as p->1 (Laplace-like cusp)?
Also check Fisher/moment values for class membership (kappa=1 proxy).
Grid: L=10, N=1201."""
import numpy as np
from sinkhorn1d import sinkhorn_C, W2sq_half_1d

L=10.0; N=1201
xs=np.linspace(-L,L,N); dx=xs[1]-xs[0]
X,Y=np.meshgrid(xs,xs,indexing='ij'); cmat=(X-Y)**2/2

def dens(pot):
    p=np.exp(-pot); p/=p.sum(); return p

def stats(p):
    m2=np.sum(p*xs**2)
    # Fisher: E[(p'/p)^2] via centered differences on log p
    lp=np.log(np.maximum(p,1e-300))
    g=np.gradient(lp,dx)
    F=np.sum(p*g**2)
    return m2,F

results={}
for pwr,A in [(2.0,0.0),(1.5,1.0),(1.25,1.0),(1.0,1.0),(1.0,2.0),(1.0,3.0)]:
    pot=xs**2/2 + A*np.abs(xs)**pwr
    if pwr==2.0 and A==0.0: pot=xs**2/2
    mu=dens(pot)
    # reference nu = N(0,1)
    nu=dens(xs**2/2)
    m2,F=stats(mu)
    w=W2sq_half_1d(mu,nu,xs,xs)
    row=[]
    for eps in [0.2,0.1,0.05,0.03]:
        C,_=sinkhorn_C(mu,nu,xs,xs,cmat,eps,niter=6000,tol=1e-10)
        Cmm,_=sinkhorn_C(mu,mu,xs,xs,cmat,eps,niter=6000,tol=1e-10)
        Cnn,_=sinkhorn_C(nu,nu,xs,xs,cmat,eps,niter=6000,tol=1e-10)
        S=C-0.5*(Cmm+Cnn)
        row.append((eps,(S-w)/eps))
    results[(pwr,A)]=(m2,F,w,row)
    print(f"p={pwr} A={A}: m2={m2:.4f} F={F:.4f} W2^2/2={w:.6f} " +
          " ".join(f"R1(eps={e})={r:+.4f}" for e,r in row))
