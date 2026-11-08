"""Standalone numerical and exact-rational checks of the residual-polynomial identity.

Requires Python 3, numpy, and sympy. This script is supplementary to the proof.
"""
import numpy as np
import sympy as sp


def build(A, As, G, B, alpha):
    nd = A.shape[0]
    nv = As.shape[0]
    npres = B.shape[0]
    zdd = np.zeros((nd, nd))
    zdv = np.zeros((nd, nv))
    zdp = np.zeros((nd, npres))
    zvp = np.zeros((nv, npres))
    zpd = np.zeros((npres, nd))
    K = np.block([[A, G.T, zdp], [G, -As, B.T], [zpd, B, np.zeros((npres, npres))]])
    S1 = As + G @ np.linalg.solve(A, G.T)
    Q = np.block([[A, G.T, zdp], [G*0, S1, -B.T], [zpd, B, alpha*np.eye(npres)]])
    T = K @ np.linalg.inv(Q)
    S2 = B @ np.linalg.solve(S1, B.T)
    E = alpha * np.linalg.inv(S2 + alpha*np.eye(npres))
    X = G @ np.linalg.inv(A)
    Z = B @ np.linalg.inv(S1)
    predicted = np.block([[np.eye(nd), zdv, zdp], [X, -np.eye(nv), zvp], [zpd, E@Z, np.eye(npres)-E]])
    return T, predicted, E, X, Z


def polynomial(T, k):
    I = np.eye(T.shape[0]); return (I-T@T) @ np.linalg.matrix_power(I-T, k)


def test_float():
    rng=np.random.default_rng(20261107)
    checks=0
    for nd,nv,npres in [(1,1,1),(2,2,1),(2,3,2),(3,4,2),(3,4,3)]:
        for _ in range(35):
            V=rng.standard_normal((nd,nd)); A=V.T@V+np.eye(nd)
            U=rng.standard_normal((nv,nv)); As=U.T@U+np.eye(nv)
            G=rng.standard_normal((nv,nd))
            B=rng.standard_normal((npres,nv))
            while np.linalg.matrix_rank(B)<npres:B=rng.standard_normal((npres,nv))
            alpha=10**rng.uniform(-3,1)
            T,T0,E,X,Z=build(A,As,G,B,alpha)
            assert np.linalg.norm(T-T0)<1e-8; checks+=1
            n=nd+nv+npres
            for k in range(7):
                target=np.zeros((n,n)); target[nd+nv:, :nd]= -np.linalg.matrix_power(E,k+1)@Z@X
                target[nd+nv:,nd:nd+nv]=np.linalg.matrix_power(E,k+2)@Z
                target[nd+nv:,nd+nv:]=np.linalg.matrix_power(E,k+1)@(2*np.eye(npres)-E)
                err=np.linalg.norm(polynomial(T,k)-target)
                assert err<3e-7, (nd,nv,npres,alpha,k,err)
                checks+=1
                q=np.linalg.norm(E,ord=2)
                constant=np.linalg.norm(np.hstack([-Z@X,E@Z,2*np.eye(npres)-E]),ord=2)
                assert np.linalg.norm(target,ord=2) <= q**(k+1)*constant+1e-10
                checks+=1
    # Direct GMRES least-squares residual is bounded by the explicit polynomial.
    for nd,nv,npres in [(1,1,1),(2,3,2),(3,4,3)]:
        for _ in range(40):
            A=np.eye(nd); As=np.eye(nv)
            G=rng.normal(size=(nv,nd))*0.3
            B=rng.normal(size=(npres,nv))
            while np.linalg.matrix_rank(B)<npres:B=rng.normal(size=(npres,nv))
            alpha=10**rng.uniform(-3,0)
            T,_,E,X,Z=build(A,As,G,B,alpha)
            b=rng.normal(size=T.shape[0]); b/=np.linalg.norm(b)
            for m in range(2,min(T.shape[0],6)+1):
                V=np.column_stack([np.linalg.matrix_power(T,j)@b for j in range(1,m+1)])
                r=b-V@np.linalg.lstsq(V,b,rcond=None)[0]
                cert=polynomial(T,m-2)@b
                assert np.linalg.norm(r)<np.linalg.norm(cert)+3e-9
                checks+=1
    return checks


def exact_scalar():
    a=sp.symbols('a',positive=True)
    E=a/(1+a)
    T=sp.Matrix([[1,0,0],[0,-1,0],[0,E,1-E]])
    I=sp.eye(3)
    checks=0
    for k in range(12):
        M=sp.simplify((I-T*T)*(I-T)**k)
        target=sp.Matrix([[0,0,0],[0,0,0],[0,E**(k+2),E**(k+1)*(2-E)]])
        assert all(sp.simplify(v)==0 for v in M-target)
        checks+=1
    # Exact two-step GMRES residual for right-hand side (1,1,1).
    b=sp.ones(3,1); u=T*b;v=T*T*b
    cross=u.cross(v)
    residual_sq=sp.factor(sp.Matrix.hstack(b,u,v).det()**2 / cross.dot(cross))
    assert sp.factor(residual_sq-2*a**2/(1+a+a**2))==0, residual_sq
    assert sp.limit(residual_sq/a**2,a,0)==2
    checks+=2
    return checks

if __name__=='__main__':
    total=test_float()+exact_scalar()
    print('PASS: %d polynomial, norm, scalar and block-structure checks' % total)
