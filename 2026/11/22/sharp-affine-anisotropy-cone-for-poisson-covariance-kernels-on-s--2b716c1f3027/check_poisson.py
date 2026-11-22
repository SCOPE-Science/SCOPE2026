#!/usr/bin/env python3
"""Reproducibility checks for affine Poisson-kernel covariance classification."""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

def poisson(s, x, y):
    # Probability-measure normalization on S^2.
    return (1.0-s*s)/(1.0+s*s-2.0*s*np.dot(x,y))**1.5

def check_sphere(s, x, y, u, order=128, nphi=256):
    t,w=leggauss(order)
    phi=2*np.pi*np.arange(nphi)/nphi
    sx=np.sqrt(np.maximum(0,1-t*t))
    z=np.stack((np.broadcast_to(sx[:,None]*np.cos(phi)[None,:], (order,nphi)),
                np.broadcast_to(sx[:,None]*np.sin(phi)[None,:], (order,nphi)),
                np.broadcast_to(t[:,None], (order,nphi))), axis=-1)
    px=(1-s*s)/(1+s*s-2*s*np.einsum('...i,i->...',z,x))**1.5
    py=(1-s*s)/(1+s*s-2*s*np.einsum('...i,i->...',z,y))**1.5
    lhs=np.sum((px*py*np.einsum('...i,i->...',z,u))*w[:,None])/(2*nphi)
    rhs=s/(1+s*s)*(np.dot(u,x)+np.dot(u,y))*poisson(s*s,x,y)
    assert abs(lhs-rhs)<2.e-9, (lhs,rhs)
    return abs(lhs-rhs)

def check_circle(s, theta, eta, center, n=8192):
    z=2*np.pi*np.arange(n)/n
    def p(delta):
        return (1-s*s)/(1+s*s-2*s*np.cos(delta))
    lhs=np.mean(p(theta-z)*p(eta-z)*np.cos(z-center))
    rhs=s/(1+s*s)*(np.cos(theta-center)+np.cos(eta-center))*((1-s**4)/(1+s**4-2*s*s*np.cos(theta-eta)))
    assert abs(lhs-rhs)<3e-12, (lhs,rhs)
    return abs(lhs-rhs)

def check_fourier_blocks():
    # Exact rational matrix-level identity:  r=1/4, s=1/2.
    from fractions import Fraction
    s=Fraction(1,2); r=s*s
    max_n=20; nlist=list(range(-max_n,max_n+1))
    checks=0
    for m in nlist:
        for n in nlist:
            M=Fraction(1,2) if abs(n-m)==1 else Fraction(0)
            lhs=(r**abs(n)+r**abs(m))*M
            rhs=(s+1/s)*s**(abs(n)+abs(m))*M
            assert lhs==rhs
            checks+=1
    return checks

def check_boundary_certificate():
    # Exact negative quadratic form for r=1/4, epsilon=9/20.
    from fractions import Fraction
    s=Fraction(1,2); eps=Fraction(9,20)
    n=6
    q=1-eps*(s+1/s)*Fraction(2*n,2*n+1)
    assert q==Fraction(-1,26), q
    # For alpha=1 and epsilon=2/5, the weighted midpoint integral has
    # nonnegative multiplier, vanishing at just one boundary pole.
    assert Fraction(2,5)*(s+1/s)==1
    return str(q)

def main():
    checks=check_fourier_blocks()
    w=check_boundary_certificate()
    rng=np.random.default_rng(81423)
    errs=[]
    for s in (0.2,0.45,0.63):
        for _ in range(8):
            x=rng.normal(size=3); x/=np.linalg.norm(x)
            y=rng.normal(size=3); y/=np.linalg.norm(y)
            u=rng.normal(size=3); u/=np.linalg.norm(u)
            errs.append(check_sphere(s,x,y,u))
    ce=[]
    for s in (0.2,0.5,0.8):
        for _ in range(12):
            theta,eta,center=rng.uniform(-np.pi,np.pi,3)
            ce.append(check_circle(s,theta,eta,center))
    print('exact rational Fourier matrix entries:',checks)
    print('exact outside-cone negative certificate:',w)
    print('S2 normalized bridge-moment comparisons:',len(errs),'max absolute discrepancy:',max(errs))
    print('S1 normalized bridge-moment comparisons:',len(ce),'max absolute discrepancy:',max(ce))
    print('All checks passed.')
if __name__=='__main__': main()
