#!/usr/bin/env python3
"""Reproducible mathematical tests for the anisotropic rook-walk Kemeny law.

Python standard library only.  Exact tests invert rational matrices rather than
using the claimed eigenvalue decomposition; asymptotic tests use scalar bisection.
"""
from fractions import Fraction as F
from math import isclose

def formula(p,q,x,y):
    a=p*x; b=q*y
    return F(p-1,1)/a+F(q-1,1)/b+F((p-1)*(q-1),1)/(a+b)

def exact_trace_inverse(A):
    n=len(A)
    U=[[F(A[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        i=next((i for i in range(c,n) if U[i][c]),None)
        assert i is not None
        U[c],U[i]=U[i],U[c]
        d=U[c][c]
        U[c]=[z/d for z in U[c]]
        for r in range(n):
            if r==c:continue
            z=U[r][c]
            if z:U[r]=[u-z*v for u,v in zip(U[r],U[c])]
    return sum(U[i][n+i] for i in range(n))

def direct_kemeny(p,q,x,y):
    n=p*q
    M=[[F(1,n) for j in range(n)] for i in range(n)]
    for i in range(p):
      for j in range(q):
       u=i*q+j
       M[u][u]+=(p-1)*x+(q-1)*y
       for k in range(p):
          if i!=k:M[u][k*q+j]-=x
       for l in range(q):
          if j!=l:M[u][i*q+l]-=y
    return exact_trace_inverse(M)-1

def optimum(p,q):
    # Unique positive zero of q*t^3*(t+2)=p*(2*t+1).
    def f(t):return q*t**3*(t+2)-p*(2*t+1)
    lo=0.0;hi=1.0
    while f(hi)<0:hi*=2
    for _ in range(180):
        mid=(lo+hi)/2
        if f(mid)<0:lo=mid
        else:hi=mid
    t=(lo+hi)/2
    beta=1/((p-1)*t/p+(q-1)/q)
    return t,t*beta/p,beta/q

count=0
# Exact matrix-inverse comparisons in unreduced graph coordinates.
for p,q in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,3)]:
    for k in range(1,7):
        x=F(k,12*(p-1));y=F(7-k,12*(q-1))
        A=direct_kemeny(p,q,x,y)
        B=formula(p,q,x,y)
        assert A==B,(p,q,k,A,B)
        count+=1
# Full-support and no-holding optimality, plus direct objective comparisons.
for p in range(2,16):
    for q in range(2,17):
        t,x,y=optimum(p,q)
        assert x>0 and y>0 and abs((p-1)*x+(q-1)*y-1)<1e-12
        assert abs(q*t**3*(t+2)-p*(2*t+1))<1e-9*max(p,q)
        best=float(formula(p,q,x,y))
        for delta in [-0.02,-0.001,0.001,0.02]:
            newt=t*(1+delta)
            newbeta=1/((p-1)*newt/p+(q-1)/q)
            newalpha=newt*newbeta
            assert float(formula(p,q,newalpha/p,newbeta/q))>best-1e-7
            count+=1
# Asymptotic scale and benchmark relative gap (without large matrices).
for p in [2,3,4,8]:
    for q in [10000,100000,1000000,10000000]:
        t,x,y=optimum(p,q)
        k=float(formula(p,q,x,y))
        tpred=(p/(2*q))**(1/3)
        corr=3*(p-1)/((4*p)**(1/3))*q**(1/3)
        assert abs(t/tpred-1)<0.07
        assert abs((k-p*q)/corr-1)<0.15
        beta=1/((p-1)/p+(q-1)/q)
        equal=float(formula(p,q,beta/p,beta/q))
        assert abs(equal/k-(p+1)*(2*p-1)/(2*p*p))<0.005
        count+=1
# A globally fastest-mixing example on K_2 square K_q.
for q in range(2,100):
    alpha=F(2,3);beta=F(2,3)
    x=alpha/2;y=beta/q
    assert (2-1)*x+(q-1)*y<=1
    assert formula(2,q,x,y)==F(9*q-3,4)
    assert max(abs(1-float(alpha)),abs(1-float(beta)),
               abs(1-float(alpha+beta)))==1/3 or isclose(max(abs(1-float(alpha)),abs(1-float(beta)),abs(1-float(alpha+beta))),1/3)
    count+=1
print('PASS: %d finite exact-algebra, optimizer and asymptotic assertions'%count)
for p,q in [(2,2),(2,3),(2,20),(2,100000)]:
    t,x,y=optimum(p,q)
    print('p=%d q=%d ratio=%.12g x=%.12g y=%.12g K=%.12g'%
          (p,q,t,x,y,float(formula(p,q,x,y))))
