#!/usr/bin/env python3
"""Deterministic algebraic and small-matrix checks for a Gaussian trace-sampling design theorem.
No stochastic experiment is used as a proof of an unbounded statement.
"""
import math
import numpy as np
from scipy.optimize import minimize


def clamp(t,lo,hi):return np.minimum(np.maximum(t,lo),hi)

def solve(lam,r,m):
    lam=np.asarray(lam,dtype=float);n=len(lam);assert 1<=r<n and m>=1
    hi=lam[:r];lo=lam[n-r:];T=sum(lam)
    assert np.all(lo<=hi)
    a=0.;b=max(1., m*T)
    for _ in range(90):
        t=(a+b)/2
        x=clamp(t,lo,hi)
        if sum(x)+2*t/m>T:b=t
        else:a=t
    t=(a+b)/2
    return clamp(t,lo,hi),t

def mse(mu,T,m):return (T-sum(mu))**2+2/m*sum(np.square(mu))

def check():
    count=0
    for n in range(2,10):
      for r in range(1,n):
       for m in (1,2,3,5,11,30,200):
        for seed in range(20):
         rng=np.random.default_rng(seed*541+n*37+r*19)
         lam=np.sort(rng.choice([0.,0.,0.1,0.3,1.,2.,10.],size=n))[::-1]
         mu,t=solve(lam,r,m);T=sum(lam);lo=lam[n-r:];hi=lam[:r]
         assert np.all(mu>=lo-1e-9) and np.all(mu<=hi+1e-9)
         assert np.all(np.diff(mu)<=1e-9)
         assert abs(sum(mu)+2*t/m-T)<1e-7
         def fun(x):return mse(x,T,m)
         result=minimize(fun, (lo+hi)/2,method='SLSQP',bounds=list(zip(lo,hi)), options={'ftol':1e-12,'maxiter':500})
         assert fun(mu)<=result.fun+1e-6,(lam,r,m,fun(mu),result.fun,result.message)
         for i in range(r):
          if lo[i]+1e-8<mu[i]<hi[i]-1e-8:assert abs(mu[i]-t)<1e-7
         count+=1
    lam=np.array([10.,2.,0.]);mu,t=solve(lam,2,3)
    assert np.allclose(mu,[6.,2.]) and abs(t-6.)<1e-10
    assert abs(mse(mu,12.,3)-128/3)<1e-10
    assert abs(mse([10.,2.],12.,3)-208/3)<1e-10
    c=math.sqrt(3/5);s=math.sqrt(2/5)
    U=np.array([[c,0.],[0.,1.],[s,0.]])
    A=np.diag(lam)
    B=U.T@A@U
    assert np.allclose(np.linalg.eigvalsh(B),[2.,6.])
    for m in range(1,21):
       x,t=solve([1.,0.],1,m)
       assert abs(x[0]-m/(m+2))<1e-10
       assert abs(mse(x,1.,m)-2/(m+2))<1e-10
       count+=1
    print('PASSED',count,'waterfill, numerical convex minimization, and explicit 2D/3D checks')

if __name__=='__main__':check()
