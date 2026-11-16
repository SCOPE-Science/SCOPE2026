#!/usr/bin/env python3
"""Finite consistency tests for the atomic weighted-composition identities.

These finite checks do not certify global convergence, sharp infinite-dimensional
Riesz bounds, or asymptotic claims; those require the analytical proof.
"""
import math

COUNT=0

def chk(cond, message):
    global COUNT
    if not cond: raise AssertionError(message)
    COUNT += 1


def coeffs(p,q,N):
    # exp(p * sum_{n>=1} q**n/(n(1-q**n)) * z**n)
    a=[1.]+[0.]*N
    b=[1.]+[0.]*N
    for n in range(1,N+1):
        a[n]=p*sum(q**j/(1-q**j)*a[n-j] for j in range(1,n+1))/n
        b[n]=-p*sum(q**j/(1-q**j)*b[n-j] for j in range(1,n+1))/n
    return a,b


def poly_mul(a,b,N):
    return [sum(a[j]*b[n-j] for j in range(n+1)) for n in range(N+1)]


def powcoeffs(p,q,N):
    # (1-qz)^(-p)
    c=[1.]
    for n in range(1,N+1): c.append(c[-1]*q*(p+n-1)/n)
    return c

for p in [1.1,2.,2.5,4.]:
    for q in [.125,.27,.48,.67]:
        N=30
        a,b=coeffs(p,q,N)
        c=poly_mul(a,b,N)
        chk(abs(c[0]-1)<1.e-13,'inverse constant')
        for n in range(1,N+1): chk(abs(c[n])<2.e-8,'reciprocal product')
        # Weighted-composition eigenidentity for each finite degree.
        w=powcoeffs(p,q,N)
        for m in range(6):
            for n in range(N-m+1):
                lhs=sum(w[k]*a[n-k] * q**(n-k+m) for k in range(n+1))
                rhs=q**m*a[n]
                chk(abs(lhs-rhs)<3.e-7*max(1.,abs(rhs)),'eigen coefficient')
        # Directly evaluate the exact rank-one coefficient-functional norm.
        for n in range(1,10):
            functional=sum(b[j]*b[j] for j in range(n+1))
            reverse=sum(b[n-j]*b[n-j] for j in range(n+1))
            chk(abs(functional-reverse)<1.e-9,'projection functional')
        # Product formulas and inequalities for the unnormalized basis.
        K=250
        plus=math.exp(sum(math.log1p(q**k) for k in range(1,K+1)))
        minus=math.exp(sum(math.log1p(-q**k) for k in range(1,K+1)))
        lower=plus**(-2*p)
        upper=minus**(-2*p)
        ratio=(plus/minus)**(2*p)
        chk(0<lower<=1<=upper,'positive bounds')
        chk(abs(upper/lower-ratio)<1.e-10*ratio,'product condition')
print('PASS:',COUNT,'finite assertions')
