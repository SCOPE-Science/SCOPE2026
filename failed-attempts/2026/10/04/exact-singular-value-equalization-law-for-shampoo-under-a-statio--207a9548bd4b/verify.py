import math
import numpy as np

def inv_quarter(A):
    w,Q=np.linalg.eigh(A)
    return (Q*(w**(-0.25)))@Q.T

def make_G(s, seed=0, m=None, n=None):
    rng=np.random.default_rng(seed)
    r=len(s); m=m or r+2; n=n or r+3
    Qu,_=np.linalg.qr(rng.normal(size=(m,r)))
    Qv,_=np.linalg.qr(rng.normal(size=(n,r)))
    return Qu@np.diag(s)@Qv.T,Qu,Qv

for s in ([7.0,2.0,0.3],[4.0,4.0],[10.0,1.0]):
    G,U,V=make_G(s,seed=len(s)+3)
    eps=0.37
    sig=np.array(s,float)
    kG=sig.max()/sig.min()
    for t in (1,2,5,20,100):
        L=eps*np.eye(G.shape[0])+t*(G@G.T)
        R=eps*np.eye(G.shape[1])+t*(G.T@G)
        P=inv_quarter(L)@G@inv_quarter(R)
        expected=U@np.diag(1.0/np.sqrt(t+eps/sig**2))@V.T
        assert np.linalg.norm(P-expected) < 2e-11
        ps=np.linalg.svd(P,compute_uv=False)[:len(sig)]
        cond=ps[0]/ps[-1]
        closed=math.sqrt(1.0+eps*(kG*kG-1.0)/(eps+t*sig.max()**2))
        assert abs(cond-closed) < 2e-10
        polar=U@V.T
        err=np.linalg.norm(math.sqrt(t)*P-polar,2)
        closed_err=1.0-(1.0+eps/(t*sig.min()**2))**(-0.5)
        assert abs(err-closed_err) < 2e-10

# Exact target-condition threshold.
sig=np.array([9.0,3.0,0.75])
eps=0.8
k=sig[0]/sig[-1]
for K in (1.1,1.5,2.0,5.0):
    if K>=k: continue
    tau=eps*(k*k-K*K)/((K*K-1.0)*sig[0]**2)
    for t in (max(1,int(math.floor(tau))), max(1,int(math.ceil(tau)))):
        cond=math.sqrt(1.0+eps*(k*k-1.0)/(eps+t*sig[0]**2))
        if t+1e-12 >= tau:
            assert cond <= K+2e-12

# Cumulative polar drift.
G,U,V=make_G([6.0,1.7,0.4],seed=99)
eps=0.5
eta=0.03
polar=U@V.T
for T in (1000,5000,20000):
    acc=np.zeros_like(G)
    for t in range(1,T+1):
        L=eps*np.eye(G.shape[0])+t*(G@G.T)
        R=eps*np.eye(G.shape[1])+t*(G.T@G)
        acc += inv_quarter(L)@G@inv_quarter(R)
    scaled=eta*acc/math.sqrt(T)
    assert np.linalg.norm(scaled-2.0*eta*polar) < 0.02

print('verification passed')
