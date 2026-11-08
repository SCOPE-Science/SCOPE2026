#!/usr/bin/env python3
"""Finite checks for sharp asymmetric-degree Crank--Nicolson positivity theorem.
Requires Python 3 standard library only. These tests supplement, not replace, the proof.
"""
from fractions import Fraction
from math import sqrt
from itertools import product
import random


def sigma(p,q):
    assert p>q>=2
    b=2*p*p-2*p*q-2*p+q
    c=p*(2*p*q-p-q)
    t=(b+sqrt(b*b+4*(2*p-1)*c))/(2*(2*p-1))
    return 1/t


def messages(p,q,s):
    a=b=0.0
    for _ in range(20000):
        aa=1/(1/s+p-(p-1)*b)
        bb=1/(1/s+q-(q-1)*a)
        if abs(aa-a)+abs(bb-b)<1e-14:
            return aa,bb
        a,b=aa,bb
    raise AssertionError('convergence failed')


def ball_return(p,q,s,r):
    assert r>=1
    msg=1/(1+s) # last layer is degree one when radius>=1
    for depth in range(r-1,0,-1):
        d=q if depth%2 else p
        msg=1/(1+s*d-s*s*(d-1)*msg)
    return 1/(1+s*p-s*s*p*msg)


def inv_frac(matrix):
    n=len(matrix)
    a=[[Fraction(v) for v in row]+[Fraction(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
    for c in range(n):
        k=next(k for k in range(c,n) if a[k][c])
        a[c],a[k]=a[k],a[c]
        k0=a[c][c]
        a[c]=[x/k0 for x in a[c]]
        for i in range(n):
            if i!=c:
                mul=a[i][c]
                if mul:
                    a[i]=[a[i][j]-mul*a[c][j] for j in range(2*n)]
    return [row[n:] for row in a]


def graph_test(p,q,n,m,edges,s):
    # connectedness irrelevant to lower bound but check the chosen tests
    L=[[0]* (n+m) for _ in range(n+m)]
    for i,j in edges:
        j+=n
        L[i][i]+=1;L[j][j]+=1
        L[i][j]-=1;L[j][i]-=1
    D=[[Fraction(int(i==j))+s*L[i][j] for j in range(n+m)] for i in range(n+m)]
    R=inv_frac(D)
    if min(R[i][i] for i in range(n+m)) < Fraction(1,2):
        raise AssertionError(('negative diagonal',p,q,n,m,edges,s))
    if min(R[i][j] for i in range(n+m) for j in range(n+m))<0:
        raise AssertionError(('negative resolvent',p,q,n,m,edges,s))


def main():
    count=0
    for p in range(3,12):
        for q in range(2,p):
            s=sigma(p,q)
            a,b=messages(p,q,s)
            ru=1/(1+s*p*(1-b))
            rv=1/(1+s*q*(1-a))
            assert abs(ru-.5)<1e-11 and rv >=ru-1e-12,(p,q,ru,rv)
            assert sigma(p,q)> (2*p-1)/(2*p*(p-1))+1e-10
            assert ball_return(p,q,s,50) > .5-1e-11
            assert ball_return(p,q,s*1.02,50) < .5
            count+=5
    random.seed(271828)
    graph_cases=0
    for p,q in [(3,2),(4,2),(4,3),(5,2),(5,3)]:
        for n,m in [(2,3),(3,3),(3,4),(4,3)]:
            for _ in range(25):
                ed=[]
                for i in range(n):
                    for j in range(m):
                        if random.random()<.65: ed.append((i,j))
                du=[sum(e[0]==i for e in ed) for i in range(n)]
                dv=[sum(e[1]==j for e in ed) for j in range(m)]
                if not ed or min(du+dv)==0 or max(du)>p or max(dv)>q:continue
                # fix a conservative rational step strictly smaller than sigma(p,q)
                s=Fraction(int(sigma(p,q)*10000)-2,10000)
                graph_test(p,q,n,m,ed,s)
                graph_cases+=1
    # The polynomial elimination identity is exact over Q for arbitrary rational t.
    elimination_cases=0
    for p in range(3,12):
        for q in range(2,p):
            t=Fraction(p,3)
            av=Fraction(p,1) - t
            av/=p
            au=Fraction(p,1)/(p+(2*p-1)*t)
            P=p*(2*p*q-p-q)+(2*p*p-2*p*q-2*p+q)*t-(2*p-1)*t*t
            residual=1/av-(q+t-(q-1)*au)
            assert residual == -t*P/((p-t)*(p+(2*p-1)*t)),(p,q,residual,P)
            elimination_cases+=1
    print('VERIFY_OK', 'tree-root-threshold-tests',count//5,
          'rational-inverse-graphs',graph_cases,'exact-elimination-identities',elimination_cases)

if __name__=='__main__':main()
