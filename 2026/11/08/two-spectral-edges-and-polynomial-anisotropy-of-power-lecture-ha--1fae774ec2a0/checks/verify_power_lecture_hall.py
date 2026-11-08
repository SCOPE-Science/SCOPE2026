#!/usr/bin/env python3
"""Independent finite checks of power lecture-hall vertex-covariance identities.
Requires numpy and scipy. Numerical samples are not proofs of asymptotic claims.
"""
from fractions import Fraction
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq
from scipy.special import jv


def covariance(n, p):
    q=np.arange(1,n+1,dtype=np.float64)
    N=n+1.0
    return (q[:,None]*q[None,:])**p*(np.minimum.outer(q,q)/N-
                                     q[:,None]*q[None,:]/N**2)


def jacobi(n,p):
    i=np.arange(1,n+1,dtype=np.float64)
    return 2/i**(2*p),-1/(i[:-1]*i[1:])**p


def rho(n,p,r=1):
    d,off=jacobi(n,p)
    return eigh_tridiagonal(d,off,select='i',select_range=(n-r,n-1))[0][::-1]


# Exact enumeration of every vertex for small dimensions, and exact inverse.
for p in [0,1,2,3]:
    for n in range(1,7):
        N=n+1
        V=[[Fraction(i**p if k<=i else 0) for i in range(1,n+1)]
            for k in range(1,N+1)]
        mean=[sum(v[i] for v in V)/N for i in range(n)]
        C=[[sum(v[i]*v[j] for v in V)/N-mean[i]*mean[j]
            for j in range(n)] for i in range(n)]
        expected=[[Fraction((i+1)**p*(j+1)**p,1)*(
            Fraction(min(i+1,j+1),N)-Fraction((i+1)*(j+1),N*N))
            for j in range(n)] for i in range(n)]
        assert C==expected
        inv=[[Fraction(N*(2 if i==j else (-1 if abs(i-j)==1 else 0)),
            ((i+1)*(j+1))**p) for j in range(n)] for i in range(n)]
        assert all(sum(C[i][k]*inv[k][j] for k in range(n))==int(i==j)
            for i in range(n) for j in range(n))

# The unweighted benchmark has an exact sine spectrum.
for n in [3,10,32]:
    eig=np.linalg.eigvalsh(covariance(n,0))[::-1]
    N=n+1
    sine=np.array([1/(4*N*np.sin(k*np.pi/(2*N))**2) for k in range(1,N)])
    assert np.allclose(eig,sine,rtol=2e-12,atol=1e-12)

# Both edges of the spectrum and the trace, for positive integer powers.
for p in [1,2,3]:
    nu=1/(2*(p+1))
    z1=brentq(lambda z:jv(nu,z),2,4)
    z2=brentq(lambda z:jv(nu,z),4,7)
    k1=1/((p+1)**2*z1**2)
    k2=1/((p+1)**2*z2**2)
    r1,r2=rho(80,p,2)
    assert r1>r2>0
    for n in [80,160]:
        C=covariance(n,p)
        e=np.linalg.eigvalsh(C)[::-1]
        got1=e[0]/n**(2*p+1)
        got2=e[1]/n**(2*p+1)
        assert abs(got1/k1-1)<0.10
        assert abs(got2/k2-1)<0.16
        expected_trace=sum(i**(2*p+1)*(n+1-i) for i in range(1,n+1))/(n+1)**2
        assert abs(np.trace(C)-expected_trace)<1e-7*expected_trace
        assert abs(e[-1]*n - 1/r1)<0.10/r1
    print('p',p,'Bessel leading',k1,'Jacobi edge',1/r1,
          'quartic/power anisotropy constant',k1*r1)

print('POWER_LECTURE_HALL_TWO_EDGE_SPECTRUM_CHECKS_PASSED')
