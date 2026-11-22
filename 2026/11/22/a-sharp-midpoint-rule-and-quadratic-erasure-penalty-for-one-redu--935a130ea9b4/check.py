#!/usr/bin/env python3
"""Reproduce the exact one-erasure Fourier sampling theorem numerically.

Requires only Python 3 and numpy. Checks matrix spectra against closed forms
at many parameters and verifies strict midpoint optimality on sampled grids.
"""
import math
import numpy as np

def coeff(N, t, j):
    d=t-j
    s=math.sin(math.pi*d/N)
    if abs(s)<1e-12: return 1.0
    return abs(math.sin(math.pi*d)/(N*s))

def worst_c(N,t):
    return min(coeff(N,t,j) for j in range(N))

def midpoint_c(N):
    return 1/(N*(math.cos(math.pi/(2*N)) if N%2==0 else 1))

def matrix(N,t,remove):
    nodes=[float(j) for j in range(N)]+[float(t)]
    nodes.pop(remove)
    return np.exp(2j*np.pi*np.outer(nodes,np.arange(N))/N)/math.sqrt(N)

def eig_analytic(N,t,remove):
    if remove==N: return np.ones(N)
    c=coeff(N,t,remove)
    s=math.sqrt(max(0,1-c*c))
    return np.array(sorted([1-s, 1+s]+[1]*(N-2)))

checks=0
for N in range(2,35):
    for t in [0.019,0.13,0.337,0.499,0.5,0.677,0.811,0.987]:
        for j in range(N+1):
            A=matrix(N,t,j)
            ev=np.linalg.eigvalsh(A.conj().T@A)
            target=eig_analytic(N,t,j)
            assert np.allclose(ev,target,rtol=1e-8,atol=8e-13), (N,t,j,ev,target)
            checks+=1
        pred=min(eig_analytic(N,t,j)[0] for j in range(N+1))
        wc=worst_c(N,t)
        assert abs(pred-(1-math.sqrt(1-wc*wc))) < 2e-14
        checks+=1
    cbest=midpoint_c(N)
    assert abs(worst_c(N,0.5)-cbest)<5e-14
    checks+=1
    for t in np.linspace(0.01,0.49,49):
        assert worst_c(N,t) < cbest + 1e-14
        checks+=1
print('PASS',checks,'independent spectral/minimax numerical checks, N=2..34')
