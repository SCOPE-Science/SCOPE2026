"""Reproduce an exact hemisphere geodesic-cycle variance constant.

Requires NumPy; no internet or data files. Run with Python 3.10+.
"""
from math import pi, sqrt, comb
import numpy as np


def variance_rate(nterms=32):
    cs = [comb(2*k,k)/4**k for k in range(nterms)]
    series = sum((4*k+3)*c**6/(k+1)**6 for k,c in enumerate(cs))
    cov = pi*pi*series/256 - (pi/2-4/pi)**2
    rate = 2-16/pi**2+2*cov
    # From C_k <= 1/sqrt(k+1), the series remainder after k=nterms-1
    # is bounded by 4/(7*nterms**7).
    rate_error = pi*pi/(224*nterms**7)
    return cov, rate, rate_error


def random_hemisphere(rng,n):
    z = rng.random(n)
    theta = rng.uniform(0,2*pi,n)
    r = np.sqrt(1-z*z)
    return np.column_stack((r*np.cos(theta),r*np.sin(theta),z))


def verify(n=420000):
    rng=np.random.default_rng(1601989)
    X=random_hemisphere(rng,n)
    Y=random_hemisphere(rng,n)
    Z=random_hemisphere(rng,n)
    A=np.arccos(np.clip(np.sum(X*Y,axis=1),-1,1))
    B=np.arccos(np.clip(np.sum(Y*Z,axis=1),-1,1))
    C=np.arccos(np.clip(np.sum(Z*X,axis=1),-1,1))
    P=A+B+C
    mu=4/pi
    cov,rate,error=variance_rate()
    assert 0<cov<0.04 and error<1e-10
    assert abs(np.mean(A)-mu)<0.006
    assert abs(np.mean(A*A)-2)<0.012
    assert abs(np.mean(A*B)-mu*mu-cov)<0.012
    assert abs(np.var(P)-3*rate)<0.040
    assert abs(np.mean(P)-3*mu)<0.014
    # Independent spherical-coordinate cross-check for a 5-cycle.
    W=random_hemisphere(rng,n)
    V=random_hemisphere(rng,n)
    verts=(X,Y,Z,W,V)
    L=np.zeros(n)
    for i in range(5):
        L+=np.arccos(np.clip(np.sum(verts[i]*verts[(i+1)%5],axis=1),-1,1))
    assert abs(np.var(L)-5*rate)<0.08
    print('HEMISPHERE_GEODESIC_CYCLE_VARIANCE_OK',n, 'covariance',format(cov,'.13f'), 'rate',format(rate,'.13f'), 'tail',error)

if __name__=='__main__':
    verify()
