#!/usr/bin/env python3
"""Exact and numerical checks for the moving-seed two-state stochastic map.
No external dependencies; theorem itself relies on the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log, sqrt

def recurrence(z, n):
    for _ in range(n):
        z=z/(1+z)
    return z

def exact_path(N, beta0, beta1, rho):
    A=F(N,1)
    a0=A/beta0
    a1=A/beta1
    law={(): (1-rho, rho)}
    for k in range(1,N+1):
        new={}
        for path, pair in law.items():
            p0=F(1,1)/(a0+k); p1=F(1,1)/(a1+k)
            prob1=pair[0]*p0+pair[1]*p1
            prob0=pair[0]*(1-p0)+pair[1]*(1-p1)
            new[path+(0,)]=(prob0,F(0))
            new[path+(1,)]=(F(0),prob1)
        law=new
    return {path:sum(pair) for path,pair in law.items()}

def indep_path(N, beta0):
    a=F(N,1)/beta0
    out={}
    for path in product((0,1),repeat=N):
        v=F(1)
        for k,b in enumerate(path,1):
            p=F(1)/(a+k)
            v*=p if b else 1-p
        out[path]=v
    return out

def tv(P,Q):
    return sum(abs(P.get(k,F(0))-Q.get(k,F(0))) for k in set(P)|set(Q))/2

def test():
    for z in (F(1,2),F(2,3),F(1,7)):
        for n in range(1,12):
            assert recurrence(z,n)==1/(F(1,1)/z+n)
    for N in (4,6,8):
        b0,b1,rho=F(2,5),F(4,5),F(1,3)
        P=exact_path(N,b0,b1,rho)
        Q=indep_path(N,b0)
        assert sum(P.values())==sum(Q.values())==1
        a=F(N,1)/b0
        # Telescoping survival conditional on starting at 0.
        surv=F(1)
        for m in range(1,N+1):
            surv*=1-1/(a+m)
            assert surv==a/(a+m)
        d=tv(P,Q)
        delta1=rho*abs(1/(F(N,1)/b1+1)-1/(F(N,1)/b0+1))
        assert d>=delta1
        # Direct valid bound from union coupling.
        a1=F(N,1)/b1
        bound=abs(F(1)/(a+1)-F(1)/(a1+1))
        for k in range(2,N+1):
            bound+=max(F(1)/(a+k-1),F(1)/(a1+k-1))*abs(F(1)/(a+k)-F(1)/(a1+k))
        assert d<=bound
    # Exact PGF / rising factorial and exact zero-count probability.
    N=7; a=F(11,3)
    Q={(): F(1)}
    for k in range(1,N+1):
        p=1/(a+k)
        Q={path+(b,):v*(p if b else 1-p) for path,v in Q.items() for b in (0,1)}
    counts={j:sum(v for path,v in Q.items() if sum(path)==j) for j in range(N+1)}
    for z in (F(0),F(1,2),F(2),F(3)):
        lhs=sum(v*z**j for j,v in counts.items())
        rhs=F(1)
        for k in range(1,N+1): rhs*=(a+z+k-1)/(a+k)
        assert lhs==rhs
    assert counts[0]==a/(a+N)
    # Critical Poisson parameter convergence and quantitative upper bounds.
    beta=1.7
    for N in (100,1000,10000):
        a=N/beta
        m=sum(1/(a+k) for k in range(1,N+1))
        assert abs(m-log(1+beta))<=beta/N
        assert sum(1/(a+k)**2 for k in range(1,N+1))<=beta*beta/N
    print('MOVING_SEED_PARABOLIC_POISSON_OK exact_paths=3 pgf=4 survival=multiple critical_rates=3')

if __name__=='__main__':test()
