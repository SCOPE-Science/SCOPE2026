#!/usr/bin/env python3
"""Reproduce the finite-size antipodal trapping-time identity on K_(2n)-matching.
Requires sympy, numpy, scipy; run `python check_exact.py`.
This checks the analytic Lyapunov certificate and independently constructs
full graph adjacency matrices. No external assets are required.
"""
import sympy as sp
import numpy as np
from scipy.linalg import solve_continuous_lyapunov

def exact_certificate():
    J, k, m=sp.symbols('J k m', positive=True, real=True)
    s=sp.sqrt(m)
    H=sp.Matrix([[0,0,J*s],[0,0,J*s],[J*s,J*s,J*(m-2)]])
    G=-sp.I*H-sp.diag(k/2,0,0)
    Xaa=1/k
    Xbb=1/k+k*(m*m-3*m+4)/(4*J**2*m*m)
    Xcc=1/k+k/(4*J**2*m)
    p=(m-2)/(2*J*m)
    q=-1/(2*J*s)
    r=1/(2*J*s)
    z=-k*(m-2)/(4*J**2*m*s)
    X=sp.Matrix([[Xaa,sp.I*p,sp.I*q],[-sp.I*p,Xbb,z+sp.I*r],[-sp.I*q,z-sp.I*r,Xcc]])
    residual=G*X+X*G.conjugate().T+sp.diag(0,1,0)
    assert all(sp.simplify(y)==0 for y in residual)
    T=sp.factor(sp.trace(X))
    target=3/k+k/(4*J**2)*(1-2/m+4/m**2)
    assert sp.simplify(T-target)==0
    # The absorption rate is k*Xaa=1, so loss occurs with probability one.
    assert sp.simplify(k*Xaa-1)==0
    print('PASS exact symbolic 3x3 integrated-state certificate')

def finite_matrices():
    for n in range(2,13):
        m=2*n-2
        N=2*n
        Adj=np.ones((N,N))-np.eye(N)
        for j in range(0,N,2): Adj[j,j+1]=Adj[j+1,j]=0
        Q=np.zeros((N,3))
        Q[0,0]=1;Q[1,1]=1;Q[2:,2]=1/np.sqrt(m)
        assert np.max(np.abs(Q.T@Q-np.eye(3))) < 1e-12
        assert np.max(np.abs(Adj@Q-Q@(Q.T@Adj@Q))) < 1e-11
        for J,k in [(1.,1.),(1.7,.7),(.5,5.)]:
            H=J*Adj
            R=Q.T@H@Q
            G=-1j*R-np.diag([k/2,0,0])
            init=np.diag([0,1,0])
            X=solve_continuous_lyapunov(G,-init)
            time=np.trace(X).real
            expected=3/k+k/(4*J*J)*(1-2/m+4/m**2)
            assert abs(time-expected)<1e-9,(n,J,k,time,expected)
            assert abs(k*X[0,0].real-1)<1e-9
        # All initial vectors orthogonal to span{a,b,uniform-others} are dark.
        e=np.eye(N)[2]
        assert abs(np.linalg.norm(Q.T@e)**2-1/m)<1e-12
        assert abs(np.linalg.norm(Q.T@np.eye(N)[1])**2-1)<1e-12
    print('PASS 33 independent full-graph matrix checks; exact capture fractions for n=2,...,12')

if __name__=='__main__':
    exact_certificate()
    finite_matrices()
