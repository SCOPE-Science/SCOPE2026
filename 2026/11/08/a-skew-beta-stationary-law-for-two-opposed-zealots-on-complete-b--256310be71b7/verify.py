#!/usr/bin/env python3
"""Reproducible finite checks for two-zealot bipartite voter dynamics.

Requires Python >=3.9, sympy, numpy and scipy. Finite checks do not certify
asymptotic convergence; that relies on the analytic proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
import math
import numpy as np
import sympy as sp
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

CHECKS = 0

def check(a, b, msg):
    global CHECKS
    CHECKS += 1
    if a != b:
        raise AssertionError(f'{msg}: {a} != {b}')

def rates(m,n,i,j):
    return {(i+1,j): F((m-1-i)*j,n),
            (i-1,j): F(i*(n-j),n),
            (i,j+1): F((n-1-j)*(i+1),m),
            (i,j-1): F(j*(m-1-i),m)}

def labeled_rates(m,n,i,j):
    """Direct site and neighbor enumeration, independent of count formulas."""
    A=(1,)+tuple([1]*i+[0]*(m-1-i))
    B=(0,)+tuple([1]*j+[0]*(n-1-j))
    out={}
    for idx in range(1,m):
        for val in B:
            if val != A[idx]:
                dest=(i+(1 if val else -1),j)
                out[dest]=out.get(dest,F(0))+F(1,n)
    for idx in range(1,n):
        for val in A:
            if val != B[idx]:
                dest=(i,j+(1 if val else -1))
                out[dest]=out.get(dest,F(0))+F(1,m)
    return out

def quad(m,n,i,j):
    p=F(i+1,m); q=F(j,n)
    d=p-q; x=(p+q)/2; T=F(2*m*n,m+n)
    ls=rates(m,n,i,j)
    Lp=F(0); Lq=F(0); aD=F(0); aX=F(0)
    for (ii,jj),rate in ls.items():
        if not rate: continue
        dp=F(ii-i,m); dq=F(jj-j,n)
        Lp+=rate*dp; Lq+=rate*dq
        aD+=rate*(dp-dq)**2
        aX+=rate*((dp+dq)/2)**2
    check(Lp, q-p+(1-q)/m, 'Lp')
    check(Lq, p-q-p/n, 'Lq')
    check(Lp-Lq, -2*d+(1-q)/m+p/n, 'LD')
    check(m*Lp+n*Lq, -(m-n)*d+1-p-q, 'L total positives')
    theta=F(n,m+n)
    check(T*(Lp+Lq)/2,theta-x+(theta-F(1,2))*d,'scaled drift')
    target=x*(1-x)+d*d/4-F(n,2*m*(m+n))*(1-q)-F(m,2*n*(m+n))*p
    check(T*aX,target,'scaled covariance')
    bound=F(m-1,m*m)+F(n-1,n*n)
    if not aD<=bound: raise AssertionError('quadratic bound')
    global CHECKS
    CHECKS+=1

def exact_stationary(m,n):
    size=m*n
    A=sp.zeros(size,size)
    for i,j in product(range(m),range(n)):
        k=i*n+j
        for (ii,jj),rate in rates(m,n,i,j).items():
            if not rate: continue
            v=sp.Rational(rate.numerator, rate.denominator)
            A[ii*n+jj,k]+=v
            A[k,k]-=v
    b=sp.zeros(size,1); b[size-1]=1
    A[size-1,:]=sp.ones(1,size)
    probs=A.inv()*b
    check(sum(probs),1,'stationary normalization')
    if any(z<0 for z in probs): raise AssertionError('negative stationary mass')
    check(probs[(m-1)*n+0],0,'unreachable extreme stationary mass')
    global CHECKS
    CHECKS+=1
    avgp=sum(probs[i*n+j]*sp.Rational(i+1,m) for i,j in product(range(m),range(n)))
    avgq=sum(probs[i*n+j]*sp.Rational(j,n) for i,j in product(range(m),range(n)))
    check(avgp,sp.Rational(n,m+n-1),'stationary mean A')
    check(avgq,sp.Rational(n-1,m+n-1),'stationary mean B')
    check((m*avgp+n*avgq)/(m+n),sp.Rational(n,m+n),'overall mean')

def large_stationary(m,n):
    size=m*n; A=lil_matrix((size,size));
    for i,j in product(range(m),range(n)):
        k=i*n+j
        for (ii,jj),rate in rates(m,n,i,j).items():
            if not rate: continue
            v=float(rate)
            A[ii*n+jj,k]+=v;A[k,k]-=v
    A[-1,:]=np.ones(size); b=np.zeros(size); b[-1]=1
    sol=spsolve(A.tocsc(),b)
    assert abs(float(sum(sol))-1)<1e-9
    p=np.array([(i+1)/m for i in range(m) for _ in range(n)])
    q=np.array([j/n for _ in range(m) for j in range(n)])
    x=(p+q)/2
    theta=n/(m+n)
    for k in range(1,5):
        got=float(np.dot(sol,x**k))
        goal=math.prod(2*theta+t for t in range(k))/math.prod(2+t for t in range(k))
        if abs(got-goal)>0.023: raise AssertionError(f'moment {k}: {got} vs {goal}')
        global CHECKS
        CHECKS+=1
    mean_d=float(np.dot(sol,p-q)); assert abs(mean_d-1/(m+n-1))<1e-10
    CHECKS+=1

if __name__=='__main__':
    for m,n in [(2,2),(2,3),(3,4),(4,3),(5,5),(6,4)]:
        for i,j in product(range(m),range(n)):
            predicted={k:v for k,v in rates(m,n,i,j).items() if v}
            check(predicted,labeled_rates(m,n,i,j),'full labeled transitions')
            quad(m,n,i,j)
    for m,n in [(2,2),(2,3),(3,3),(3,4),(4,4)]:
        exact_stationary(m,n)
    for m,n in [(20,20),(20,30),(40,40)]:
        large_stationary(m,n)
    print(f'PASS: {CHECKS} exact-rational and numerical comparisons')
