#!/usr/bin/env python3
"""Supplementary checks for the exact positive-spectrum DGT step-size theorem.
Dependencies: numpy and sympy. The proof is analytic; these finite checks are not its substitute.
"""
from fractions import Fraction as F
import numpy as np
import sympy as sp

def assemble(W, H, alpha):
    n = len(W)
    I = np.eye(n)
    return np.block([[W, -alpha*W], [H@(W-I), W-alpha*H@W]])

def threshold(W,H):
    n=len(W)
    t=1/np.sqrt(np.diag(H))
    C=np.linalg.inv(W)+2*np.eye(n)+W
    return np.linalg.eigvalsh(t[:,None]*C*t[None,:])[0]/2

def reduced_radius(W,H,alpha):
    eigenvalues=np.linalg.eigvals(assemble(W,H,alpha))
    assert sum(abs(eigenvalues-1)<2e-7)==1
    return max(abs(x) for x in eigenvalues if abs(x-1)>2e-7)

# Exact two-node example; this is a certificate for a noncommuting H and W.
W=sp.Matrix([[sp.Rational(3,4),sp.Rational(1,4)],
             [sp.Rational(1,4),sp.Rational(3,4)]])
H=sp.diag(sp.Rational(7,6),sp.Rational(5,6))
critical=sp.Rational(9,5)
C=W.inv()+2*sp.eye(2)+W
assert C==sp.Matrix([[sp.Rational(17,4),-sp.Rational(1,4)],
                    [-sp.Rational(1,4),sp.Rational(17,4)]])
assert (C-2*critical*H).det()==0
assert (C-2*critical*H)[0,0]>0
T=sp.BlockMatrix([[W,-critical*W],[H*(W-sp.eye(2)), W-critical*H*W]]).as_explicit()
z=sp.Symbol('z')
p=sp.factor((z*sp.eye(4)-T).det())
assert sp.expand(p-(z-1)*(z+1)*(40*z*z-12*z-19)/40)==0
assert all(abs(float(v))<1 for v in [(3+sp.sqrt(199))/20,(3-sp.sqrt(199))/20])
print('EXACT_TWO_NODE: PASS; alpha_c=9/5; p(z)=(z-1)(z+1)(40z^2-12z-19)/40')

rng=np.random.default_rng(20261107)
checks=0
for n in range(2,9):
    for case in range(24):
        G=rng.uniform(.15,1.0,(n,n));G=np.triu(G,1);G=G+G.T
        L=np.diag(G.sum(axis=1))-G
        maxeig=np.linalg.eigvalsh(L)[-1]
        W=np.eye(n)-.65/maxeig*L
        H=np.diag(rng.uniform(.35,4.,size=n))
        assert min(np.linalg.eigvalsh(W))>.349999
        assert np.allclose(W.sum(axis=1),1)
        a=threshold(W,H)
        Q=np.linalg.inv(W)+2*np.eye(n)+W-2*a*H
        assert abs(np.linalg.eigvalsh(Q)[0])<2e-9
        assert reduced_radius(W,H,a*.93)<1-1e-8
        assert abs(reduced_radius(W,H,a)-1)<2e-7
        assert reduced_radius(W,H,a*1.07)>1+1e-8
        # Check positive/negative definiteness of the boundary pencil.
        assert np.linalg.eigvalsh(np.linalg.inv(W)+2*np.eye(n)+W-2*a*.93*H)[0]>0
        assert np.linalg.eigvalsh(np.linalg.inv(W)+2*np.eye(n)+W-2*a*1.07*H)[0]<0
        checks+=6
print('RANDOM_N2_TO_N8: PASS; %d assertions across 168 connected SPD networks'%checks)
