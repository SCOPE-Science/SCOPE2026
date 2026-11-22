#!/usr/bin/env python3
"""Reproduce numerical checks for sharp entrywise matrix-log stability theorem.

This is supplementary floating-point evidence; the proof is analytic.
"""
import numpy as np
from scipy.special import roots_legendre

rng = np.random.default_rng(918273)

def c(n):
    return (1 + np.sqrt(n))/2

def bound(n,a,b):
    q=c(n)
    if a==b: return 1/a
    return q*q/a+(1-q)*(1-q)/b + 2*q*(1-q)*np.log(b/a)/(b-a)

def extremizer(n):
    u=np.zeros(n)
    u[0]=np.sqrt((1+1/np.sqrt(n))/2)
    if n>1:
        u[1:]=np.sqrt((1-u[0]*u[0])/(n-1))
    return np.outer(u,u)

def logm_sym(A):
    w,U=np.linalg.eigh(A)
    return (U * np.log(w)) @ U.T

def deriv_log(A,H):
    w,U=np.linalg.eigh(A)
    C=U.T@H@U
    D=np.empty((len(w),len(w)))
    for i,x in enumerate(w):
        for j,y in enumerate(w):
            D[i,j] = (np.log(x)-np.log(y))/(x-y) if abs(x-y)>1e-9*max(x,y) else 1/x
    return U@(D*C)@U.T

# quadrature for Dlog integral, mapped [0,infty) to [0,1]
xs,ws=roots_legendre(96)
ss=(xs+1)/2
wts=ws/2

def deriv_log_resolvent(A,H):
    n=A.shape[0]
    I=np.eye(n)
    S=np.zeros_like(A)
    for s,w in zip(ss,wts):
        # R(s/(1-s)) /(1-s) = ((1-s) A+sI)^{-1}
        Z=np.linalg.inv((1-s)*A+s*I)
        S+=w*Z@H@Z
    return S

count=0
for n in range(1,10):
    P=extremizer(n)
    if abs(np.sum(abs(P[0,:]))-c(n))>2e-14:
        raise AssertionError((n,'projection row'))
    for a,b in [(1,1.1),(0.4,4),(2,5),(1,12)]:
        E=np.ones((n,n))
        A=a*P+b*(np.eye(n)-P)
        got=deriv_log_resolvent(A,E)[0,0]
        exact=bound(n,a,b)
        if abs(got-exact)>3e-9*max(1,exact):
            raise AssertionError(('sharp derivative',n,a,b,got,exact))
        count+=1

for n in range(2,10):
    for rep in range(35):
        G=rng.standard_normal((n,n))
        U,_=np.linalg.qr(G)
        a,b=0.5,3.0
        spec=a+(b-a)*rng.random(n)
        A=(U*spec)@U.T
        H=rng.uniform(-1,1,(n,n));H=(H+H.T)/2
        deriv=deriv_log_resolvent(A,H)
        if np.max(abs(deriv))>bound(n,a,b)+4e-10:
            raise AssertionError(('upper bound',n,rep))
        if np.max(abs(deriv-deriv_log(A,H)))>6e-9:
            raise AssertionError(('Frechet comparison',n,rep))
        count+=2

for n in (2,3,5,9):
    a,b=0.7,4
    P=extremizer(n)
    eps=1e-4
    A=(a+eps)*P+(b-eps)*(np.eye(n)-P)
    E=np.ones((n,n))
    h=1e-7
    w=np.linalg.eigvalsh(A+h*E)
    if w[0]<a-1e-8 or w[-1]>b+1e-8: raise AssertionError('invalid finite pair')
    ratio=np.max(abs(logm_sym(A+h*E)-logm_sym(A)))/h
    if ratio>bound(n,a,b)+1e-5 or ratio<bound(n,a,b)-0.008:
        raise AssertionError(('finite-pair sharpness',n,ratio,bound(n,a,b)))
    count+=1

# Positive diameter effect: finite band is strictly smaller than half-line bound.
for n in (2,3,4,8,32):
    for a,b in ((1,1.01),(1,2),(1,100)):
        L=bound(n,a,b)
        if L<1/a-1e-9 or L>c(n)**2/a+1e-8:
            raise AssertionError(('spectral limits',n,a,b,L))
        count+=1
print('PASS',count,'independent numerical comparisons')
# Critical-width crossover: b/a=1+x/sqrt(n).
for x in (0.1, 0.5, 1, 3):
    limit=1+x/2+x*x/12
    errs=[]
    for n in (1000,10000,1000000):
        got=bound(n,1,1+x/np.sqrt(n))
        errs.append(abs(got-limit))
    if not (errs[-1]<errs[0] and errs[-1]<0.025):
        raise AssertionError(('critical crossover',x,errs))
    count+=1

# Fixed-width asymptotics.
for r in (1.1, 2, 20):
    leading=(1+1/r-2*np.log(r)/(r-1))/4
    for n in (1000,100000):
        got=bound(n,1,r)/n
        if abs(got-leading)>0.03: raise AssertionError('large-dimensional coefficient')
        count+=1
print('PASS asymptotic checks',count,'total numerical comparisons')
