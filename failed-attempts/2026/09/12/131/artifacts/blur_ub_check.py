"""Validate proof-skeleton Step 2a: blurred-diagonal upper bound on self-term C(mu,mu)
vs exact 1D Gaussian formula. UB(sigma): cost + eps*KL with pi=Law(X,X+sigma Z).
N(0,a): cost=sigma^2/2; KL = H(mu)-(1/2)log(2pi e sigma^2)+(sigma^2/2)(1/a),
H(mu)=(1/2)log(2pi e a). Check UB(sigma=sqrt(eps)) >= exact, and gap = O(eps^2)."""
import numpy as np

def C1(a,b,eps):
    s=np.sqrt(a*b); D=np.sqrt(eps*eps+4*a*b)
    t=min((D-eps)/(2*s),1-1e-15)
    return (a+b-(D-eps))/2-(eps/2)*np.log1p(-t*t)

def blurUB_self(a,eps,sig2=None):
    s2=eps if sig2 is None else sig2
    H=0.5*np.log(2*np.pi*np.e*a)
    KL=H-0.5*np.log(2*np.pi*np.e*s2)+(s2/2)/a
    return s2/2+eps*KL

print("self-term: exact vs blur UB (sigma^2=eps), gap/eps^2:")
for a in [0.1,0.5,1.0,2.0]:
    for eps in [0.2,0.1,0.05,0.02,0.01]:
        ex=C1(a,a,eps); ub=blurUB_self(a,eps)
        assert ub>=ex-1e-12,(a,eps,ex,ub)
        print(f"a={a} eps={eps}: exact={ex:.6f} UB={ub:.6f} (UB-ex)/eps^2={(ub-ex)/eps**2:.4f}")
    print()
