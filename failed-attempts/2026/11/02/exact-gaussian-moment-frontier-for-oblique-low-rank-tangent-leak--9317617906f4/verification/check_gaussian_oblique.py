#!/usr/bin/env python3
"""Independent finite-sample checks of a Gaussian oblique tangent-projection identity.

Requires NumPy. Analytical moment finiteness is established by the proof, not by this script.
"""
import math
import numpy as np


def analytic_moment_of_column(rank, rows, order, scale=1.0):
    nu = rows-rank+1
    if order >= nu:
        return math.inf
    return scale**order * math.gamma((rank+order)/2)*math.gamma((nu-order)/2) / (math.gamma(rank/2)*math.gamma(nu/2))


def direct_projector(Z, U, V, Theta, Omega):
    left = U @ np.linalg.solve((Theta@U).T@(Theta@U), (Theta@U).T@Theta)
    right = V @ np.linalg.solve((Omega@V).T@(Omega@V), (Omega@V).T@Omega)
    return left@Z + Z@right.T - left@Z@right.T


def run():
    rng = np.random.default_rng(20261031)
    checks = 0
    # Algebraic identity for arbitrary orthonormal bases, normal matrices and Gaussian sketches.
    for r, m, n, l, k in [(1,4,5,3,4),(2,6,5,4,3),(3,8,7,6,5)]:
        for _ in range(70):
            X,_ = np.linalg.qr(rng.normal(size=(m,m)))
            Y,_ = np.linalg.qr(rng.normal(size=(n,n)))
            U,Up=X[:,:r],X[:,r:]
            V,Vp=Y[:,:r],Y[:,r:]
            C=rng.normal(size=(m-r,n-r))
            Z=Up@C@Vp.T
            T=rng.normal(size=(l,m))
            O=rng.normal(size=(k,n))
            left=np.linalg.lstsq(T@U,T@Up,rcond=None)[0]
            right=np.linalg.lstsq(O@V,O@Vp,rcond=None)[0]
            E=direct_projector(Z,U,V,T,O)
            blocks=U@(-left@C@right.T)@V.T+U@(left@C)@Vp.T+Up@(C@right.T)@V.T
            assert np.allclose(E,blocks,rtol=1e-9,atol=1e-9)
            e2=np.linalg.norm(E)**2
            block2=np.linalg.norm(left@C)**2+np.linalg.norm(C@right.T)**2+np.linalg.norm(left@C@right.T)**2
            assert np.isclose(e2,block2,rtol=1e-9,atol=1e-9)
            checks+=2
    # Vectorized independent rank-one sketches, away from high-variance moment boundaries.
    for left_rows,right_rows in [(5,6),(7,8),(10,10),(14,9)]:
        trials=120000
        Lg=rng.normal(size=(trials,left_rows)); Lh=rng.normal(size=(trials,left_rows))
        Rg=rng.normal(size=(trials,right_rows)); Rh=rng.normal(size=(trials,right_rows))
        a=np.sum(Lg*Lh,axis=1)/np.sum(Lg*Lg,axis=1)
        b=np.sum(Rg*Rh,axis=1)/np.sum(Rg*Rg,axis=1)
        empirical=np.mean(a*a+b*b+(a*b)**2)
        al=1/(left_rows-2); ar=1/(right_rows-2)
        predicted=al+ar+al*ar
        relative=abs(empirical/predicted-1)
        assert relative < .035,(left_rows,right_rows,empirical,predicted,relative)
        checks+=1
    for r in (1,2,3,4):
        for rows in range(r+2,r+10):
            actual=analytic_moment_of_column(r,rows,2)
            expected=r/(rows-r-1)
            assert abs(actual-expected)<1e-11
            checks+=1
        assert math.isinf(analytic_moment_of_column(r,r+1,2))
        checks+=1
    print(f"PASS: {checks} algebraic, simulation and gamma-moment checks")

if __name__=='__main__':
    run()
