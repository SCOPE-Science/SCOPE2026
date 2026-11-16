#!/usr/bin/env python3
"""Finite numerical consistency checks for positive circular kernel extremals.
These tests do not certify infinite-dimensional convergence or global novelty.
"""
import math
import numpy as np
from scipy.linalg import eigh, toeplitz
from scipy.integrate import quad
from scipy.special import sici

CHECKS = 0

def verify(test, message):
    global CHECKS
    if not test:
        raise AssertionError(message)
    CHECKS += 1


def matrix(n):
    t = np.zeros(n+1, dtype=float)
    t[0] = np.pi/2
    for m in range(1, n+1):
        t[m] = ((-1)**m-1)/(np.pi*m*m)
    return toeplitz(t)


def exact_kernel(n):
    M = matrix(n)
    evals, evecs = eigh(M)
    u = np.real(evecs[:,0])
    if np.sum(u)<0: u=-u
    return float(evals[0]),u


def angular_integral(u):
    q = np.arange(len(u))
    def fun(t):
        P = np.sum(u*np.exp(1j*q*t))
        return t*(P.real**2+P.imag**2)/np.pi
    return quad(fun,0,np.pi,epsabs=1e-10,epsrel=1e-10,limit=300)[0]

for n in range(1,33):
    M=matrix(n)
    lam,u=exact_kernel(n)
    verify(np.linalg.norm(M@u-lam*u)<1e-11, f'eigenpair n={n}')
    verify(np.min(u)>0, f'Perron positivity n={n}')
    verify(np.linalg.norm(u-u[::-1])<1e-10,f'reflection n={n}')
    verify(abs(angular_integral(u)-lam)<1e-10,f'angular integral n={n}')
    verify(abs(np.dot(u,u)-1)<1e-12, f'normalization n={n}')
    verify(np.all(np.linalg.eigvalsh(M)>0),f'positive definite n={n}')
    v=np.ones(n+1)/np.sqrt(n+1)
    verify(float(v@M@v)+1e-12>=lam,f'variational n={n}')
    if n<16:
        z=np.sin(np.pi*np.arange(1,n+2)/(n+2))
        z=z/np.linalg.norm(z)
        verify(float(z@M@z)+1e-12>=lam, f'sine test n={n}')

rv=2*sici(np.pi)[0]-4/np.pi
verify(abs(rv-2.430634559229769)<1e-12,'Rivlin constant')
for n in [64,128,256,512]:
    lam,u=exact_kernel(n)
    verify((n+1)*lam<rv,'large-degree improvement')
    verify(2.30<(n+1)*lam<2.33, f'Cauchy convergence n={n}')
print(f'PASS: {CHECKS} finite consistency checks; Rivlin trial energy {rv:.13f}')
for n in [2,4,8,16,32,64,128,256,512]:
    lam,u=exact_kernel(n)
    print(f'n={n} C_n={lam:.12f} (n+1)C_n={(n+1)*lam:.12f}')
