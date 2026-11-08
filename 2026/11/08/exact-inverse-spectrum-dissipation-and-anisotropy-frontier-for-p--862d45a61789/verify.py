#!/usr/bin/env python3
"""Deterministic finite matrix identities for a planar Gaussian diffusion frontier.

The continuum statement and uniqueness are established analytically in RESULT.md.
"""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov

count = 0

def close(x, y, tol=1e-9):
    global count
    assert np.allclose(x, y, atol=tol, rtol=tol), (x, y)
    count += 1

for a, b in ((2.0,1.0), (1.5,0.5), (5.0,1.3), (1.001,0.8)):
    cvals = [b, 0.3*b+0.7*a, 0.8*b+0.2*a, 0.05*b+0.95*a]
    for c in cvals:
        v = np.sqrt(c*c-b*b)
        S = np.array([[c,0.0],[0.0,-c]])
        for sign in (-1,1):
            W = np.array([[0.,sign*v],[-sign*v,0.]])
            A = -a*np.eye(2) + S + W
            B = -(A + A.T)
            D = B/2
            close(np.linalg.eigvalsh(B), [2*(a-c), 2*(a+c)])
            close(np.linalg.eigvals(A).real, sorted([-a-b,-a+b])) if False else None
            close(sorted(np.linalg.eigvals(A).real), [-a-b,-a+b])
            close(solve_continuous_lyapunov(A, -B), np.eye(2))
            close(A + D, W)
            phi = np.trace(W.T @ np.linalg.inv(D) @ W)
            theory = 2*a*(c*c-b*b)/(a*a-c*c)
            close(phi, theory, 2e-8)
            K = np.linalg.cond(B)
            close(K, (a+c)/(a-c))
            frontier = (a*a*(K-1)**2-b*b*(K+1)**2)/(2*a*K)
            close(phi, frontier, 2e-8)
            close(np.trace(B), 4*a)
            tau = 0.71
            from scipy.linalg import expm
            C = expm(A.T*tau)
            val = np.linalg.norm(C-C.T,ord='fro')
            close(val, 2*np.sqrt(2)*v*np.exp(-a*tau)*np.sinh(b*tau)/b)
            close(val <= 2*np.sqrt(2)*np.sqrt(a*a-b*b)*np.exp(-a*tau)*np.sinh(b*tau)/b + 1e-10, True)
for a,b in ((2.,1.), (4.,2.3)):
    K0=(a+b)/(a-b)
    close((a*a*(K0-1)**2-b*b*(K0+1)**2)/(2*a*K0),0.0)
    for K in (1.01*K0,2*K0,10*K0):
        c=a*(K-1)/(K+1)
        phi=2*a*(c*c-b*b)/(a*a-c*c)
        bound=(a*a*(K-1)**2-b*b*(K+1)**2)/(2*a*K)
        close(phi,bound)
print('PASS:', count, 'deterministic independent matrix assertions')
