#!/usr/bin/env python3
"""Exact independent finite checks for a Catalan cherry--path-length identity."""
from math import comb
from fractions import Fraction
from functools import lru_cache


def catalan(n):
    return comb(2*n,n)//(n+1)

def moments(nmax):
    # Enumerate tree shapes by bilinear moment recurrences from root decomposition.
    T=[0]*(nmax+1); A=[0]*(nmax+1); B=[0]*(nmax+1); Q=[0]*(nmax+1)
    T[0]=1
    for n in range(1,nmax+1):
        for a in range(n):
            b=n-1-a
            c=T[a]*T[b]
            T[n]+=c
            A[n]+=A[a]*T[b]+T[a]*A[b]+int(a==0 and b==0)
            B[n]+=B[a]*T[b]+T[a]*B[b]+(n-1)*c
            Q[n]+=Q[a]*T[b]+T[a]*Q[b]+A[a]*B[b]+B[a]*A[b]
            Q[n]+=(n-1)*(A[a]*T[b]+T[a]*A[b])
    return T,A,B,Q

@lru_cache(None)
def all_trees(n):
    if n==0: return (None,)
    return tuple((l,r) for a in range(n) for l in all_trees(a) for r in all_trees(n-1-a))

def stats(t):
    if t is None: return (0,0,0)
    a,b=t
    na,ca,pa=stats(a); nb,cb,pb=stats(b)
    return (1+na+nb,ca+cb+int(a is None and b is None),pa+pb+na+nb)

def closed(n):
    c=catalan(n); b=comb(2*n,n)
    A=comb(2*n-2,n-1) if n>=1 else 0
    B=4**n-3*b+2*c
    Q=Fraction((n+1)*4**n,4)-Fraction((6*n+1)*b,8)-Fraction(catalan(n-1),4)
    cov=-Fraction(n+1,4*(2*n-1))*(Fraction((n+1)*4**n,b)-4*n)
    return c,A,B,Q,cov

def run():
    maxn=55
    T,A,B,Q=moments(maxn)
    checks=0
    for n in range(1,maxn+1):
        ct,at,bt,qt,cov=closed(n)
        for got,want in [(T[n],ct),(A[n],at),(B[n],bt),(Q[n],qt)]:
            assert got==want,(n,got,want)
            checks+=1
        actual=Fraction(Q[n],T[n])-Fraction(A[n]*B[n],T[n]**2)
        assert actual==cov,(n,actual,cov)
        checks+=1
        assert (actual==0 if n<=2 else actual<0)
        checks+=1
    for n in range(0,12):
        ts=all_trees(n)
        assert len(ts)==T[n]
        checks+=1
        suma=sumb=sumq=0
        for t in ts:
            nn,cc,pp=stats(t)
            assert nn==n
            suma+=cc;sumb+=pp;sumq+=cc*pp
            checks+=1
        assert (suma,sumb,sumq)==(A[n],B[n],Q[n]),(n,suma,sumb,sumq,A[n],B[n],Q[n]);checks+=3
    print('EXACT_CHECKS_PASSED',checks)
    for n in (3,4,5,8,15,30,55):
        print('n',n,'covariance',str(closed(n)[4]))

if __name__=='__main__': run()
