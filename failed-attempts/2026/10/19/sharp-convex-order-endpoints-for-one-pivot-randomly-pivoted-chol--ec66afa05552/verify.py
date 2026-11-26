#!/usr/bin/env python3
"""Numerical reproducibility checks for the one-pivot Cholesky convex-order theorem."""
import numpy as np


def zero_diagonal_frame(B):
    # Construct an orthogonal frame whose B-quadratic diagonals vanish.
    n = B.shape[0]
    frame = np.eye(n)
    C = B.copy()
    for k in range(n - 1):
        eigenvalues, eigvecs = np.linalg.eigh(C)
        pos, neg = np.argmax(eigenvalues), np.argmin(eigenvalues)
        if np.max(np.abs(eigenvalues)) < 1e-12:
            chosen = np.eye(C.shape[0])[:, 0]
        else:
            a, b = eigenvalues[pos], -eigenvalues[neg]
            assert a > 0 and b > 0, (k, eigenvalues)
            chosen = np.sqrt(b/(a+b))*eigvecs[:, pos] + np.sqrt(a/(a+b))*eigvecs[:, neg]
        # Nullspace to the chosen unit vector via SVD.
        _, _, vh = np.linalg.svd(chosen.reshape(1,-1), full_matrices=True)
        N = vh[1:].T
        Q = np.column_stack([chosen,N]); assert np.allclose(Q.T@Q, np.eye(len(C)), atol=2e-13)
        frame[:, k:] = frame[:, k:]@Q
        C = Q.T@C@Q
        C = C[1:,1:]
    return frame


def check(lam,U):
    lam=np.asarray(lam,dtype=float)
    n=len(lam)
    A=U@np.diag(lam)@U.T
    S=np.sum(lam); q=np.sum(lam**2)/S
    diag=np.diag(A)
    b=np.diag(A@A)
    p=diag/S
    d=np.divide(b, diag, out=np.zeros(n), where=diag>1e-12)
    assert np.isclose(p.sum(),1,atol=1e-12)
    assert np.isclose(p@d,q,atol=1e-10)
    assert np.isclose(np.sum(p*(S-d)),S-q,atol=1e-10)
    v=np.sum(p*(d-q)**2)
    upper=np.sum(lam**3)/S-q*q
    assert -1e-9<=v<=upper+1e-9,(lam,v,upper)
    for f in [lambda x:x*x, lambda x:np.exp(x/max(lam)), lambda x:(x/max(lam))**4, lambda x:np.maximum(x-q,0)**2,lambda x:np.maximum(q-x,0)**2]:
        z=np.dot(p,f(d))
        top=np.dot(lam/S,f(lam))
        assert f(q)-1e-9<=z<=top+1e-9,(lam,z,top)
    # Direct Schur-complement trace calculation.
    for i in range(n):
        if diag[i]<1e-12: continue
        resid=A - A[:,i:i+1]@A[i:i+1,:]/diag[i]
        assert np.isclose(np.trace(resid),S-d[i],atol=1e-10)
    return v,upper


def main():
    rng=np.random.default_rng(314159)
    count=0
    for n in range(2,9):
        for j in range(60):
            lam=np.exp(rng.uniform(-2,2,n))
            if j%7==0: lam[0]=0
            if j%13==0: lam[:]=1
            if j%17==0: lam[-1]=0
            assert lam.sum()>0
            Z=rng.normal(size=(n,n));U,R=np.linalg.qr(Z);U=U@np.diag(np.sign(np.diag(R)))
            check(lam,U);count+=1
            v,top=check(lam,np.eye(n));assert np.isclose(v,top,atol=1e-9)
            S=lam.sum();q=(lam@lam)/S
            B=np.diag(lam*lam-q*lam)
            Q=zero_diagonal_frame(B)
            assert np.allclose(np.diag(Q.T@B@Q),0,atol=1e-10)
            v,top=check(lam,Q.T)
            assert abs(v)<1e-9,(lam,v)
            count+=3
    a=np.diag([1,4]);U=np.array([[1,1],[-1,1]],float)/np.sqrt(2)
    v,top=check([1,4],np.eye(2));assert np.isclose(v,36/25)
    v,top=check([1,4],U);assert np.isclose(v,0,atol=1e-12)
    print('PASS:',count,'random spectral and orthogonal-basis configurations/check groups, plus 2 numerically tested planar endpoints.')
    print('Exact planar example: independent eigenbasis gains {1,4} probabilities {1/5,4/5}; constant balanced gain 17/5.')
    print('Expected residual 8/5 in either basis; maximum variance 36/25, minimum 0.')

if __name__=='__main__':main()
