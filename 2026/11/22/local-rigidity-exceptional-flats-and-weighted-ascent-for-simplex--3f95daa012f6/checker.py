"""Finite diagnostics for exact Grassmannian projection-sign stability.

This program checks small integers and sampled perturbations; the general theorem
is established analytically in RESULT.md, not by finite computation.
"""
import itertools
import numpy as np


def setup(m):
    q = m+1
    edges = list(itertools.combinations(range(q), 2))
    n = len(edges)
    B = np.zeros((n,q))
    for r, e in enumerate(edges):
        B[r, list(e)] = 1
    H0 = np.eye(q)-np.ones((q,q))/q
    P0 = B @ H0 @ B.T/(q-2)
    K = np.zeros((n,n))
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            K[i,j] = int(not (set(e)&set(f)))
    S = np.ones((n,n)) - 2*K
    return B,P0,S

rng=np.random.default_rng(73913)
checks=0
for m in range(4,13):
    B,P0,S=setup(m)
    n=len(S);q=m+1
    a=(-m*m+7*m-4)/2
    b=2*(m-2)
    assert np.allclose(P0@P0,P0,atol=1e-12)
    assert np.linalg.matrix_rank(P0,tol=1e-8)==m
    assert np.all(np.sign(P0)==S)
    vals=np.linalg.eigvalsh(S)
    expected=np.sort(np.array([a]+[b]*m+[-2]*(n-m-1)))
    assert np.allclose(vals,expected,atol=1e-9)
    assert abs(np.abs(P0).sum()/n - b*m/n)<1e-10
    checks += 5
    gamma=min(b-a,b+2)
    if m==4: assert abs(a-b)<1e-14
    else: assert gamma>0
    checks+=1
    W,e=np.linalg.eigh(P0)
    E=e[:,-m:]
    C=np.ones((n,1))/np.sqrt(n)
    Fproj=np.eye(n)-P0-C@C.T
    for k in range(60):
        Y=rng.normal(size=(n,m))*0.005+E
        U,_=np.linalg.qr(Y)
        P=U@U.T
        assert np.all(np.sign(P)==S)
        val=np.abs(P).sum()/n
        val0=np.abs(P0).sum()/n
        d=np.trace((np.eye(n)-P0)@P)
        c=float((C.T@P@C)[0,0])
        f=float(np.trace(Fproj@P))
        exact=((b-a)*c+(b+2)*f)/n
        assert abs((val0-val)-exact)<2e-10
        assert val0-val+1e-11>=gamma*d/n
        if m==7: assert abs((val0-val)-gamma*d/n)<2e-10
        checks+=4
    for which,v in enumerate([C[:,0],None]):
        if v is None:
            QF,_=np.linalg.qr(Fproj@rng.normal(size=(n,1)))
            v=QF[:,0]
        for theta in (0.001,0.01):
            Z=E.copy()
            Z[:,0]=np.cos(theta)*E[:,0]+np.sin(theta)*v
            P=Z@Z.T
            if np.min(np.abs(P0))>np.max(np.abs(P-P0)):
                actual=(np.abs(P0).sum()-np.abs(P).sum())/n
                predicted=((b-a) if which==0 else (b+2))*np.sin(theta)**2/n
                assert abs(actual-predicted)<2e-10
                checks+=1
# Flat four-dimensional manifold: optimizing the positive weight vector
# strictly improves the objective away from the symmetric midpoint frame.
B,P0,S=setup(4)
n=len(S)
C=np.ones(n)/np.sqrt(n)
E=np.linalg.eigh(P0)[1][:,-4:]
PH=P0+np.outer(C,C)
lam0=np.linalg.eigvalsh(np.abs(P0))[-1]
assert abs(lam0-8/5)<1e-12
for j in range(4):
    u=E[:,j]
    for theta in [0.0005,0.001,0.005,0.01]:
        w=np.cos(theta)*C+np.sin(theta)*u
        P=PH-np.outer(w,w)
        assert np.array_equal(np.sign(P),S)
        assert np.allclose(P@P,P,atol=1e-12)
        assert abs(np.abs(P).sum()/n-8/5)<1e-10
        lam=np.linalg.eigvalsh(np.abs(P))[-1]
        assert lam>lam0+1e-10
        assert abs((lam-lam0)/theta**2-48/125)<0.004
        checks+=5
print('SIMPLEX_LOCAL_SIGN_SPECTRAL_CHECK_OK',checks)
