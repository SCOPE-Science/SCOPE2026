"""Independent finite-step checks for renewal-reset channel divisibility.

Run with Python 3 and NumPy. Finite computations supplement the proof;
they do not establish its infinite-time or dimension-uniform conclusions.
"""
from fractions import Fraction
import numpy as np


def renewal(h):
    n = len(h)
    S = [1.0]
    for x in h:
        S.append(S[-1] * (1.0 - x))
    p = [0.0] + [S[k-1] * h[k-1] for k in range(1,n+1)]
    nu = [1.0]
    for k in range(1,n+1):
        nu.append(sum(nu[k-j]*p[j] for j in range(1,k+1)))
    return S, p, nu


def unitary(d, rng):
    z = rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
    q,r = np.linalg.qr(z)
    return q @ np.diag(np.diag(r)/np.abs(np.diag(r)))


def choi(f,d):
    C = np.zeros((d*d,d*d),complex)
    for i in range(d):
        for j in range(d):
            e = np.zeros((d,d),complex); e[i,j]=1
            v = np.zeros((d,d),complex); v[i,j]=1
            C += np.kron(v,f(e))
    return C


def numerical_suite(h,d,rng):
    S,p,nu=renewal(h)
    unitaries=[unitary(d,rng) for _ in range(3)]
    weights=[0.20,0.30,0.50]
    E=lambda X: sum(w*U@X@U.conj().T for w,U in zip(weights,unitaries))
    v = rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
    sigma = v@v.conj().T; sigma /=np.trace(sigma)
    B=[np.zeros((d,d),complex)]
    for t in range(1,len(h)+1):
        nxt=np.zeros((d,d),complex)
        for s in range(1,t+1):
            y=sigma.copy()
            for _ in range(t-s): y=E(y)
            nxt += nu[s]*S[t-s]*y
        B.append(nxt)
    for t in range(len(h)):
        q=S[t+1]/S[t]
        Y=B[t+1]-q*E(B[t])
        form=nu[t+1]*sigma.copy()
        for s in range(1,t+1):
            y=sigma.copy()
            for _ in range(t+1-s): y=E(y)
            form += nu[s]*S[t-s]*(h[t]-h[t-s])*y
        assert np.max(np.abs(Y-form))<3e-12
        assert abs(np.trace(Y)-(1-q))<3e-12
        assert np.max(np.abs(Y-Y.conj().T))<3e-12
        phi=lambda k,X:S[k]*apply_k(E,X,k)+np.trace(X)*B[k]
        middle=lambda X:q*E(X)+np.trace(X)*Y
        for i in range(d):
            for j in range(d):
                X=np.zeros((d,d),complex); X[i,j]=1
                assert np.max(np.abs(phi(t+1,X)-middle(phi(t,X))))<3e-12
        if all(h[j]<=h[j+1] for j in range(len(h)-1)):
            assert np.linalg.eigvalsh(Y).min()>-4e-12
            assert np.linalg.eigvalsh(choi(middle,d)).min()>-4e-12
            assert np.max(np.abs(middle(np.eye(d)).conj().T-middle(np.eye(d))))<3e-12
    return len(h)


def apply_k(E,X,k):
    Y=X
    for _ in range(k): Y=E(Y)
    return Y


def negative_witness(h,m):
    """Exact cyclic-shift witness for a strict hazard drop at index m+1."""
    d=m+2
    S=[Fraction(1)]
    for j in range(m+1): S.append(S[-1]*(1-h[j]))
    p=[Fraction(0)]+[S[k-1]*h[k-1] for k in range(1,m+2)]
    nu=[Fraction(1)]
    for k in range(1,m+2):nu.append(sum((nu[k-j]*p[j] for j in range(1,k+1)),Fraction(0)))
    # Resetter state at |0>; all one-step correction terms are diagonal.
    Y=[Fraction(0) for _ in range(d)]; Y[0]+=nu[m+1]
    for s in range(1,m+1):
        Y[m+1-s]+=nu[s]*S[m-s]*(h[m]-h[m-s])
    q=S[m+1]/S[m]
    # Lambda(|m><m|) = q |m+1><m+1| + Y.
    spectrum=Y.copy(); spectrum[m+1]+=q
    assert Y[m] == h[0]*S[m-1]*(h[m]-h[m-1])
    assert spectrum[m] < 0
    assert sum(spectrum)==1
    assert all(0<=float(x)<=1 for x in h)
    return Y[m]


def main():
    rng=np.random.default_rng(20260119)
    checks=0
    for d in (2,3,4):
        for h in ([0.1,0.2,0.3,0.7,0.9],
                  [0.2]*5,[0.35,0.4,0.43,0.44,0.45],
                  [0.4,0.2,0.2,0.2,0.2]):
            checks+=numerical_suite(h,d,rng)
    F=Fraction
    assert negative_witness([F(2,5),F(1,5)],1)==-F(2,25)
    checks+=1
    for m in range(1,15):
        h=[F(2,5)+F(j,100) for j in range(m)] + [F(1,5)]
        v=negative_witness(h,m)
        assert v<0
        checks+=1
    print('PASS: {} numerical step checks and {} exact cyclic negative witnesses'.format(checks-15,15))
    print('Exact two-step witness: Y_1=diag(7/25,-2/25,0), q=4/5.')

if __name__=='__main__': main()
