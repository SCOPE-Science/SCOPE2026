"""Reproduce exact algebra and finite independent covariance checks.

Run: python verify.py. The mathematical global-optimality proof is in RESULT.md;
finite numerical tests are supporting checks, not an exhaustive search.
"""
from fractions import Fraction
from math import sqrt
import random

import numpy as np
import sympy as sp


def optimal(n, P):
    if n < 1 or P <= 0:
        raise ValueError("n>=1 and P>0 required")
    A = 1 + 1/P
    d = 1/(n*A + sqrt(n*n*A*A-n*n+0.25))
    t = np.array([1-(n+0.5-i)*d for i in range(1, n+1)])
    w = np.full(n,d)
    p = np.full(n,P/n)
    risk = n*d**3/12+(1-n*d)**3/3+(n*d)**2/P
    return d,t,w,p,risk


def covariance_risk(t, p):
    t=np.asarray(t,dtype=float);p=np.asarray(p,dtype=float)
    k=t-t*t/2
    K=np.minimum.outer(t,t)+np.diag(1/p)
    return 1/3-float(k@np.linalg.solve(K,k))


def test_symbolic():
    n,i,P,d=sp.symbols("n i P d",positive=True)
    A=1+1/P
    f=(n*n-sp.Rational(1,4))*d*d-2*n*A*d+1
    r=n*d**3/sp.Integer(12)+(1-n*d)**3/sp.Integer(3)+(n*d)**2/P
    assert sp.factor(sp.diff(r,d)+n*((1-n*d)**2-d*d/4-2*n*d/P))==0
    t=1-(n+sp.Rational(1,2)-i)*d
    summing_t=n-n*(n+sp.Rational(1,2))*d + d*(i*n-i*(i-1)/2)
    # sum_j min(t_i,t_j) for increasing evenly spaced t_j
    assert sp.factor((t-t*t/2) - d*(summing_t+n/P)-f/2)==0
    d2=sp.Rational(2,15)
    t1,t2=sp.Rational(4,5),sp.Rational(14,15)
    p=sp.Rational(1,2)
    K=sp.Matrix([[t1+1/p,t1],[t1,t2+1/p]])
    k=sp.Matrix([t1-t1*t1/2,t2-t2*t2/2])
    assert K.inv()*k==sp.Matrix([d2,d2])
    assert sp.Rational(1,3)-(k.T*K.inv()*k)[0]==sp.Rational(137,675)
    for m in range(1,11):
        d0=sp.Rational(2,2*m+1)
        formula=m*d0**3/sp.Integer(12)+(1-m*d0)**3/sp.Integer(3)
        assert formula==sp.Rational(1,3*(2*m+1)**2)
    return True


def test_covariance():
    rng=random.Random(3051)
    comparisons=0
    for n in range(1,9):
        for P in (0.07,0.25,1,2,6,30,500):
            d,t,w,p,r=optimal(n,P)
            assert 0<t[0]<t[-1]<1 if n>1 else 0<t[0]<1
            assert abs(sum(p)-P)<1e-12
            assert abs(covariance_risk(t,p)-r)<2e-12
            K=np.minimum.outer(t,t)+np.diag(1/p)
            k=t-t*t/2
            assert max(abs(K@w-k)) < 2e-12
            if n<5:
                for _ in range(600):
                    tt=np.sort(np.array([rng.random() for _ in range(n)]))
                    pp=np.array([rng.random()+0.01 for _ in range(n)])
                    pp=P*pp/sum(pp)
                    rr=covariance_risk(tt,pp)
                    assert rr >= r-3e-11,(n,P,rr,r)
                    comparisons+=1
    return comparisons


def test_limits():
    for P in (0.03,0.2,1,2,10,200):
        A=1+1/P
        c=A-sqrt(A*A-1)
        rlim=(1-c)**3/3+c*c/P
        for n in (50,200,1000):
            d,t,w,p,r=optimal(n,P)
            assert abs(n*d-c) < 1/n
            assert abs(r-rlim) < 1/n
        risks=[optimal(n,P)[-1] for n in range(1,12)]
        assert all(a>b for a,b in zip(risks,risks[1:]))
    return True


if __name__=="__main__":
    assert test_symbolic()
    k=test_covariance()
    assert test_limits()
    print("PASS exact algebra (rational example, optimality equation, kernel normal equations)")
    print("PASS Gaussian covariance calculations for 56 (n,P) pairs")
    print(f"PASS {k} independent random feasible-design comparisons (supplementary only)")
    print("PASS continuum and small/large budget consistency checks")
