#!/usr/bin/env python3
"""Reproduce exact generalized-Watson / Anderson-Darling null cross moments.
Python 3 standard library only. Run: python3 check.py
"""
from fractions import Fraction as Q
from math import comb, factorial, pi, log, cos, sqrt
import random

checks = 0

def eq(a,b):
    global checks
    assert a == b, (a,b)
    checks += 1

def near(a,b,tol):
    global checks
    assert abs(a-b)<=tol, (a,b,tol)
    checks += 1

def bernoulli(n):
    # Use generating identity B_0=1, sum_{k=0}^r binom(r+1,k) B_k=0.
    ans=[Q(1)]
    for r in range(1,n+1):
        ans.append(-sum(Q(comb(r+1,k))*ans[k] for k in range(r))/Q(r+1))
    return ans

def bern_poly(n):
    b=bernoulli(n)
    return [Q(comb(n,k))*b[n-k] for k in range(n+1)]

def kappa_direct(m):
    # B_{2m}(t) times J(t)=2(1-t)+4t log t.
    out=Q(0)
    for k,c in enumerate(bern_poly(2*m)):
        out+=c*(Q(2,k+1)-Q(2,k+2)-Q(4,(k+2)**2))
    return Q(2)*((-1)**(m-1))*out/Q(factorial(2*m))

def kappa_alternate(m):
    # Integral of (B_{2m+2}(0)-B_{2m+2}(t))/[t(1-t)] .
    b=bern_poly(2*m+2)
    # Numerator has zero at t=0 and t=1. Let numerator = t(1-t)q(t).
    a=[-v for v in b]; a[0]+=b[0]
    # recurrence a_{j+1} = q_j - q_{j-1}, q_{-1}=0
    q=[]; last=Q(0)
    for degree in range(1,len(a)-1):
        cur=a[degree]+last
        q.append(cur); last=cur
    eq(-last,a[-1])
    integral=sum(c/Q(k+1) for k,c in enumerate(q))
    return Q(4)*((-1)**m)*integral/Q(factorial(2*m+2))

known={1:Q(1,36),2:Q(7,10800),3:Q(41,2540160),4:Q(19,46656000),5:Q(181,17563392000)}
for m in range(1,10):
    a=kappa_direct(m); b=kappa_alternate(m)
    eq(a,b)
    eq(a>0,True)
    if m in known: eq(a,known[m])

# Independent Fourier integration approximation: 8 sum_k I_k/(2pi k)^{2m+2},
# I_k=2 int_0^1 (1-cos(2 pi k t))/t dt computed by midpoint rule.
# First use Ci-independent quadrature for m=1,2 with 59 frequencies; the remaining tail is small.
for m in (1,2):
    Nquad=18000
    z=0.
    for k in range(1,60):
        h=1/Nquad
        Ik=2*h*sum((1-cos(2*pi*k*(j+.5)*h))/((j+.5)*h) for j in range(Nquad))
        z+=8*Ik/(2*pi*k)**(2*m+2)
    near(z,float(kappa_direct(m)), 1.2e-6 if m==1 else 2e-9)

# Exact finite-sample variance terms and strict opposite monotonicities of correlation.
VA=2*pi*pi/3-6
Vdiag=4-pi*pi/3

def rho(n,m):
    # zeta(4m) approximated by absolute convergent positive series.
    zet=sum(k**(-4*m) for k in range(1,2200))
    varA=VA+(10-pi*pi)/n
    varW=4*(n-1)/n*zet/(2*pi)**(4*m)
    return (n-1)/n*float(kappa_direct(m))/sqrt(varA*varW)
for n in (2,3,5,10,100):
    arr=[rho(n,m) for m in range(1,8)]
    for x,y in zip(arr,arr[1:]): eq(x>y,True)
    for x in arr: eq(0<x<1,True)
for m in range(1,8):
    arr=[rho(n,m) for n in (2,3,5,10,100)]
    for x,y in zip(arr,arr[1:]): eq(x<y,True)

# Direct independent finite-N Monte Carlo of pair kernels and order-statistic AD.
rng=random.Random(20240409)
for n in (2,5):
    B=44000
    sumA=sumW=sumAW=0.
    for _ in range(B):
        v=sorted(rng.random() for _ in range(n))
        A=-n-sum((2*i-1)*(log(v[i-1])+log(1-v[n-i])) for i in range(1,n+1))/n
        d=[abs(x-y) for x in v for y in v]
        # m=2, H_2(t)=-B_4(t)/24
        W=-sum(t**4-2*t**3+t**2-1/30 for t in d)/(24*n)
        sumA+=A; sumW+=W; sumAW+=A*W
    cov=sumAW/B-(sumA/B)*(sumW/B)
    near(cov,(n-1)/n*float(known[2]),.000030)
print('PASS:',checks,'checks; exact rational Bernoulli identities, Fourier quadrature, monotonic profiles and independent Monte Carlo')
