#!/usr/bin/env python3
"""Supplementary numerical checks of the stated cyclic finite-memory spectral law."""
from math import isclose
import numpy as np
from scipy.optimize import brentq

def exact_root(s, laws):
    n=len(laws)
    def f(r):
        return n*np.log(s)+sum(np.log(np.dot(q,r**(-np.arange(len(q))-1))) for q in laws)
    return brentq(f,1e-5,1.0,xtol=1e-14)

def lifted(s,laws):
    n=len(laws); L=max(len(q) for q in laws)-1
    T=np.zeros((n*(L+1),n*(L+1)))
    for i,q in enumerate(laws):
        for k,w in enumerate(q):
            T[i,k*n+(i-1)%n]+=s*w
    for k in range(1,L+1):
        for i in range(n): T[k*n+i,(k-1)*n+i]=1.
    return T

def check():
    checks=0
    rng=np.random.default_rng(521719)
    for n in range(2,7):
        for L in range(0,5):
            for trial in range(18):
                s=float(rng.uniform(.08,.92))
                laws=[rng.dirichlet(np.ones(L+1)) for _ in range(n)]
                r=exact_root(s,laws)
                rho=max(abs(np.linalg.eigvals(lifted(s,laws))))
                assert abs(r-rho)<4e-9,(n,L,r,rho)
                B=sum(sum(k*float(v) for k,v in enumerate(q)) for q in laws)
                assert r+1e-10>=s**(n/(n+B))
                checks+=2
    s=.5
    A=[np.eye(5)[k] for k in (1,1,1,1)]
    B=[np.eye(5)[k] for k in (4,0,0,0)]
    C=[np.array([.75,0,0,0,.25]) for _ in range(4)]
    assert abs(exact_root(s,A)-2**(-.5))<1e-12
    assert abs(exact_root(s,B)-2**(-.5))<1e-12
    assert abs(exact_root(s,C)-0.7565523330592138)<1e-12
    checks+=3
    for L in range(1,7):
      for n in range(2,5):
       for trial in range(30):
        s=float(rng.uniform(.15,.9))
        q=[rng.dirichlet(np.ones(L+1)) for _ in range(n)]
        qlo=[]; qhi=[]
        for qi in q:
            mu=float(np.dot(np.arange(L+1),qi)); lo=int(np.floor(mu))
            qi_lo=np.zeros(L+1); qi_lo[lo]+=lo+1-mu
            if lo<L: qi_lo[lo+1]+=mu-lo
            else: qi_lo[lo]=1.
            qi_hi=np.zeros(L+1); qi_hi[0]=1-mu/L; qi_hi[-1]+=mu/L
            qlo.append(qi_lo); qhi.append(qi_hi)
        a=exact_root(s,qlo); b=exact_root(s,q); c=exact_root(s,qhi)
        assert a-1e-10<=b<=c+1e-10,(n,L,a,b,c)
        checks+=1
    print('PASS: '+str(checks)+' spectral/convexity checks; exact cycle examples verified')

if __name__=='__main__':check()
