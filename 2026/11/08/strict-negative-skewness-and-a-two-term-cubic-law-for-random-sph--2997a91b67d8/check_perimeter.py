#!/usr/bin/env python3
"""Numerical cross-checks for the spherical perimeter third-moment identities."""
import math
import numpy as np
from scipy.special import eval_gegenbauer, roots_jacobi, gammaln

def lambda1(d):
    return math.exp(2*gammaln(d/2) -math.log(d-1) -gammaln((d-1)/2)-gammaln((d+1)/2))

def spectrum(d,max_l=25,nq=2048):
    p=(d-3)/2
    t,w=roots_jacobi(nq,p,p)
    w=w/w.sum()
    alpha=(d-2)/2
    out=[]
    for l in range(1,max_l+1,2):
        q=eval_gegenbauer(l,alpha,t)/eval_gegenbauer(l,alpha,1.0)
        lam=float(w@(np.arcsin(t)*q))
        dim=(2*l+d-2)* math.gamma(l+d-2) / (math.gamma(l+1)*math.gamma(d-1))
        out.append((l,lam,dim))
    return out

def check():
    for d in [3,4,8,16]:
        ls=spectrum(d,max_l=23)
        l1=ls[0][1]
        assert abs(l1-lambda1(d))<1e-9,(d,l1,lambda1(d))
        assert all(lam > -1e-12 for l,lam,h in ls), (d,ls)
        s=sum(h*lam**3 for l,lam,h in ls)
        assert s>=d*lambda1(d)**3-1e-9
        print('spectral',d,'lambda1',l1,'third central',-6*s,'strict bound',-6*d*lambda1(d)**3)
    # Low-dimensional exact Legendre-coefficient identity.
    ls=spectrum(3,max_l=23)
    for l, lam, h in ls:
        k=(l-1)//2
        a=math.comb(2*k,k)/4**k
        exact=math.pi*a*a/(8*(k+1)**2)
        assert abs(lam-exact)<1e-9,(l,lam,exact)
    print('legendre exact coefficients checked')
    rng=np.random.default_rng(261107)
    for d,n in [(3,220000),(8,260000),(24,250000),(64,160000)]:
        # Streaming batches to bound memory.
        acc=0.; ss=0.; cubic=0.; cprod=0.; count=0
        for j in range(0,n,20000):
            m=min(20000,n-j)
            x=rng.normal(size=(m,3,d))
            x/=np.linalg.norm(x,axis=2,keepdims=True)
            inner=np.sum(x*np.roll(x,-1,axis=1),axis=2).clip(-1,1)
            theta=np.arccos(inner)
            z=theta.sum(axis=1)-3*math.pi/2
            acc+=float(np.sum(z)); ss+=float(np.dot(z,z)); cubic+=float(np.sum(z**3))
            cprod+=float(np.sum(inner.prod(axis=1)))
            count+=m
        sd=(ss/n)**0.5
        # Simulation only cross-checks trend; no finite Monte Carlo proves a sign theorem.
        print('simulation',d,'n',count,'mean shift',acc/n,'variance',ss/n,'third central',cubic/n,'theory_leading',-6/d**2,'linear_product',cprod/n,'linear_exact',1/d**2)
    print('SPHERICAL_TRIANGLE_PERIMETER_CUBIC_CHECKS_OK')
if __name__=='__main__':
    check()
