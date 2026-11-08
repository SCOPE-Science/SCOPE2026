#!/usr/bin/env python3
"""Reproduce numerical checks for signed rank-one cone-angle formulas.
Only finite numerical corroboration; the general theorem is analytic.
"""
from math import acos, pi, sqrt, exp
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr

def alpha(u, eps):
    u=np.asarray(u,dtype=float)
    delta=sqrt(eps/(1-eps))
    fn=lambda t: exp(-0.5*(delta*t)**2)*float(np.prod(ndtr(u*t)))
    val=quad(fn,-np.inf,np.inf,epsabs=3e-11,epsrel=3e-11,limit=450)[0]
    return delta/sqrt(2*pi)*val

def mixed_lead(u):
    u=np.asarray(u,dtype=float)
    assert np.any(u>0) and np.any(u<0)
    fn=lambda t:float(np.prod(ndtr(u*t)))
    return quad(fn,-np.inf,np.inf,epsabs=3e-11,epsrel=3e-11,limit=450)[0]/sqrt(2*pi)

def uniform(n,p,eps):
    return alpha(np.array([1]*p+[-1]*(n-p))/sqrt(n),eps)

def main():
    checks=0
    # Exact planar cone angles in both sign configurations.
    for eps in [0.001,0.01,0.1,0.3,0.8]:
        s=acos((1-eps)/(1+eps))/(2*pi)
        assert abs(uniform(2,1,eps)-s)<3e-10
        assert abs(uniform(2,0,eps)-(0.5-s))<3e-10
        checks+=2
    # Strict sign-partition ordering, symmetry and exact covariance eigenvalues.
    for n in range(2,10):
        for eps in [0.001,0.03,0.2,0.7]:
            aa=[uniform(n,p,eps) for p in range(n+1)]
            for p in range(n+1):
                assert abs(aa[p]-aa[n-p])<3e-10
                checks+=1
            for p in range(n//2):
                assert aa[p]>aa[p+1]+1e-10
                checks+=1
            for p in range(n+1):
                u=np.array([1]*p+[-1]*(n-p))/sqrt(n)
                gram=np.eye(n)-(1-eps)*np.outer(u,u)
                ev=np.linalg.eigvalsh(gram)
                assert abs(ev[0]-eps)<3e-14
                assert np.max(abs(ev[1:]-1))<3e-14
                checks+=2
    # Leading square-root coefficient: test two successive small eps values.
    for u in [(1,-1),(1,-2),(2,-1,-1),(1,1,-1,-1),(1,2,-2,-3)]:
        u=np.asarray(u,dtype=float);u=u/np.linalg.norm(u)
        k=mixed_lead(u)
        for eps in [2e-3,5e-4]:
            a=alpha(u,eps)
            assert abs(a/sqrt(eps)-k) < 0.018 * k
            checks+=1
    print(f"PASS {checks} independent numerical normalization, ordering, spectral, and edge-limit checks")
    print("n=2 mixed coefficient",mixed_lead([1/sqrt(2),-1/sqrt(2)]),"expected",1/pi)
    print("n=3 split coefficient",mixed_lead([1/sqrt(3),-1/sqrt(3),-1/sqrt(3)]))

if __name__=='__main__': main()
