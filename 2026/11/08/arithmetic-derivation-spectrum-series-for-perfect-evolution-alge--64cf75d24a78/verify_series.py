#!/usr/bin/env python3
"""Exact formal-series arithmetic for the derivation-dimension enumerator."""
from math import factorial
from sympy import Symbol, Rational, expand

def gl(n,q):
    ans=1
    for i in range(n):ans*=q**n-q**i
    return ans

def ord2(p):
    if p==2:return None
    h=1;x=2%p
    while x!=1:x=(2*x)%p;h+=1
    return h

def counts(q,N):
    u=Symbol('u'); h=ord2(q)
    F=[Rational(gl(n,q),factorial(n)) for n in range(N+1)]
    if h is None:return [[gl(n,q)] for n in range(N+1)]
    Q=[Rational(0)]*(N+1); Q[0]=Rational(1)
    for m in range(1,N//h+1): Q[h*m]=Rational(gl(m,q)**h,factorial(m)**h)
    # log(Q) formal power series, defined recursively by Q'=Q(log Q)'.
    L=[Rational(0)]*(N+1)
    for n in range(1,N+1):
        L[n]=expand(Q[n]-sum(Rational(k,n)*L[k]*Q[n-k] for k in range(1,n)))
    # E=exp(a L); E'=a L' E.
    a=Rational(1,h)*(u-1)
    E=[Rational(1)]+[Rational(0)]*N
    for n in range(1,N+1):
        E[n]=expand(a*sum(Rational(k,n)*L[k]*E[n-k] for k in range(1,n+1)))
    out=[]
    for n in range(N+1):
        pol=expand(factorial(n)*sum(F[j]*E[n-j] for j in range(n+1)))
        row=[int(pol.coeff(u,k)) for k in range(n//h+1)]
        assert sum(row)==gl(n,q) and min(row)>=0,(q,n,row,gl(n,q))
        out.append(row)
    return out

for q,N in [(3,8),(5,9),(7,8),(2,5)]:
    rows=counts(q,N)
    for n,cs in enumerate(rows):
        if n in (2,3,4,6,7,8,9) and (n<=4 or n==N):
            print('q=',q,'n=',n,'by_derivation_dimension=',cs)
    if q==3:
        assert rows[2]==[44,4]
        assert rows[3]==[11208,24]
        assert rows[4][1:]==[7872,48],rows[4]
    if q==5:
        assert rows[4][1]==6*4**4
    if q==7:
        assert rows[3][1]==2*6**3
print('VERIFY_SERIES_OK')
