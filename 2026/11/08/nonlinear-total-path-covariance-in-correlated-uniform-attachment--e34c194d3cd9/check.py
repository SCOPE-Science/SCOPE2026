#!/usr/bin/env python3
"""Exact finite checks and numerical diagnostics for correlated recursive-tree depth covariance.

Scientific identity tested: the covariance of centered total root-path lengths in
paired recursive trees with independently refreshed aligned-parent choices.
Tests do not replace the all-n analytic argument in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
import math

CHECKS=0

def check(actual, expected, label):
    global CHECKS
    if actual != expected:
        raise AssertionError(f"{label}: {actual!r} != {expected!r}")
    CHECKS+=1

def recur(n, alpha):
    """(q_n, c_n), where q_n=E cross-sectional depth covariance and
    c_n=Cov(S_n^(1)/n,S_n^(2)/n)."""
    q=F(0);c=F(0)
    for k in range(1,n):
        c+=alpha*q/F((k+1)**2)
        q=F(k*(k+1), (k+1)**2)*q+alpha*F(k,(k+1)**2)*q+F(k,(k+1)**2)
    return q,c

def product_r(n, alpha):
    if alpha==0:
        h=sum((F(1,j) for j in range(1,n+1)),F(0))
        return F(n)-h
    if alpha==1:
        h=sum((F(1,j) for j in range(1,n+2)),F(0))
        return F(n+1)*h-F(2*n+1)
    b=F(1)
    for j in range(1,n+1): b*=1+alpha/F(j)
    return (1+alpha*n-b)/(alpha*(1-alpha))

def brute(n, alpha):
    """Independent enumeration of coupled parent sequences: no recurrence used."""
    sums=F(0); sumsxy=F(0); qsum=F(0); weight_total=F(0)
    def visit(j, depth_a, depth_b, probability):
        nonlocal sums,sumsxy,qsum,weight_total
        if j>n:
            va=sum(depth_a); vb=sum(depth_b); k=n
            sums+=probability*va
            sumsxy+=probability*va*vb
            qsum+=probability*(sum(x*y for x,y in zip(depth_a,depth_b))/F(k)-F(va*vb,k*k))
            weight_total+=probability
            return
        m=j-1
        for u in range(m):
            for v in range(m):
                pr=(1-alpha)/F(m*m)+(alpha/F(m) if u==v else 0)
                if pr:
                    visit(j+1,depth_a+(depth_a[u]+1,),depth_b+(depth_b[v]+1,),probability*pr)
    visit(2,(0,),(0,),F(1))
    check(weight_total,F(1),f'probability normalization n={n} alpha={alpha}')
    h=sum((F(1,j) for j in range(1,n+1)),F(0))
    mean=F(n)*(h-1)
    check(sums,mean,f'mean n={n} alpha={alpha}')
    return qsum,(sumsxy-mean*mean)/F(n*n)

def series_constant(alpha,N=100000):
    return math.fsum(float(alpha)/(j*j*(j-float(alpha))) for j in range(2,N+1))

for a in (F(0), F(1,3),F(1,2),F(2,3),F(1)):
    for n in range(1,12):
        q,c=recur(n,a)
        check(q*n,product_r(n,a),f'product r n={n} alpha={a}')
        check(q>=0,True,f'positive q n={n} alpha={a}')
        check(c>=0,True,f'positive c n={n} alpha={a}')
    for n in range(2,7):
        q,c=brute(n,a)
        qr,cr=recur(n,a)
        check(q,qr,f'exhaustive q n={n} alpha={a}')
        check(c,cr,f'exhaustive c n={n} alpha={a}')

# Infinite-covariance identity: compare two distinct summation algorithms;
# the rigorous derivation uses a binomial generating integral in RESULT.md.
for a in (0.1,0.25,0.5,0.75,0.9,1.0):
    q=0.;c=0.
    N=100000
    for n in range(1,N):
        c+=a*q/((n+1)**2)
        q=(n*(n+1+a)/((n+1)**2))*q+n/((n+1)**2)
    s=series_constant(a)
    # Analytic tail bound: q_n(a) <= q_n(1) <= 2(log(n+1)+2),
    # hence tail < 3a(log N+3)/N for N>=2.
    err=3*a*(math.log(N)+3)/N
    if abs(c-s)>err: raise AssertionError(f'limit mismatch {a}: {c} {s} allowed {err}')
    CHECKS+=1

assert abs(series_constant(1,100000)-(2-math.pi**2/6))<1e-9
CHECKS+=1
assert 0 < series_constant(.5) < .5*series_constant(1)
CHECKS+=1
print(f'CHECKS_OK exact_exhaustive_and_numerical={CHECKS}; max_enumerated_vertices=6')
