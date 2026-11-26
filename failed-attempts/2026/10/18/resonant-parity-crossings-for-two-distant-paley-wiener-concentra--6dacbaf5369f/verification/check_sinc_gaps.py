"""Numerical quadrature cross-check for two-interval sinc concentration splitting.
Standalone science-only calculation; does not certify infinite-dimensional statements.
"""
import numpy as np
from scipy.special import roots_legendre
from scipy.linalg import eigh
from scipy.optimize import brentq

def trial(a=0.25, W=0.5, nquad=160):
    omega=2*np.pi*W
    raw,w=roots_legendre(nquad); x=a*raw; w=a*w
    ww=np.sqrt(w); X=x[:,None]; Y=x[None,:]
    def sinc_kernel(t):
        return 2*W*np.sinc(2*W*t)
    T=ww[:,None]*ww[None,:]*sinc_kernel(X-Y)
    spectrum,V=eigh(T)
    lam=spectrum[-1]; v=V[:,-1]
    if v.sum()<0:v=-v
    phi=v/ww
    A=np.dot(w*phi,np.cos(omega*x))
    B=np.dot(w*x*phi,np.sin(omega*x))
    tau_star=2*B/(omega*A)
    q=ww*np.sin(omega*x)
    z=V.T@q; R=np.sum(z[:-1]**2/(lam-spectrum[:-1]))
    L=A*A*R/np.pi**2
    print('a,W,nquad,lambda,A,B,tau*,L=',a,W,nquad,lam,A,B,tau_star,L)
    def parities(D):
        C=ww[:,None]*ww[None,:]*sinc_kernel(D-X-Y)
        return eigh(T+C,eigvals_only=True,subset_by_index=[nquad-1,nquad-1])[0],eigh(T-C,eigvals_only=True,subset_by_index=[nquad-1,nquad-1])[0]
    for n in (20,40,80,120):
        dn=n*np.pi/omega
        root=brentq(lambda tau: parities(dn+tau/dn)[0]-parities(dn+tau/dn)[1],tau_star-.25,tau_star+.25,xtol=5e-11)
        p,m=parities(dn+root/dn)
        assert abs(root-tau_star)<2e-4, 'parity crossing must approach predicted shift'
        assert abs(p-m)<5e-10, 'parity crossing root accuracy'
        eps=(-1)**n
        for tau in (0.,tau_star-.12,tau_star,tau_star+.12):
            lplus,lminus=parities(dn+tau/dn)
            diff=dn**2*(lplus-lminus)
            pred=2*eps*(omega*tau*A*A-2*A*B)/np.pi
            ctr=dn**2*((lplus+lminus)/2-lam)
            assert abs(diff-pred)<3e-4, 'uniform second-order splitting'
            assert abs(ctr-L)<3e-3, 'reduced-resolvent centroid correction'
            print(f'n={n} tau={tau:.8f} diff={diff:.9f} pred={pred:.9f} centroid={ctr:.9f} L={L:.9f}')
        print('n=',n,'root tau=',root,'drift=',root-tau_star)
    D=40.5
    lplus,lminus=parities(D)
    assert abs(D*(max(lplus,lminus)-lam)-A*A/np.pi)<2e-3, 'off-resonant leading coefficient'
    print('ALL NUMERICAL ASYMPTOTIC CHECKS PASSED')
    return tau_star,L
if __name__=='__main__':
    trial()
