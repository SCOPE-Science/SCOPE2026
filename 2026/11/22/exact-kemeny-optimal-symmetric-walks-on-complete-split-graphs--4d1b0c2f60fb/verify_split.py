#!/usr/bin/env python3
"""Exact-arithmetic checks for Kemeny-optimal symmetric walks on complete split graphs.

Python 3 standard library only. The finite checks supplement, rather than replace,
the general proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product


def inv(A):
    n=len(A)
    T=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if T[i][k])
        T[k],T[pivot]=T[pivot],T[k]
        d=T[k][k]
        T[k]=[x/d for x in T[k]]
        for i in range(n):
            if i!=k:
                d=T[i][k]
                T[i]=[a-d*b for a,b in zip(T[i],T[k])]
    return [r[n:] for r in T]


def kemeny_by_inverse(p,q,b,c):
    n=p+q
    P=[[F(0)]*n for _ in range(n)]
    for i in range(p):
        for j in range(i+1,p):
            P[i][j]=P[j][i]=c
        for j in range(p,n):
            P[i][j]=P[j][i]=b
    for i in range(n):
        P[i][i]=1-sum(P[i])
        assert P[i][i]>=0
    S=[[F(i==j)-P[i][j]+F(1,n) for j in range(n)] for i in range(n)]
    Z=inv(S)
    return sum(Z[i][i] for i in range(n))-1


def kemeny_spectrum(p,q,b,c):
    return F(q-1,p)/b + F(p-1)/(q*b+p*c) + 1/(F(p+q)*b)


def optimum(p,q):
    b=F(1,max(p,q))
    c=F(max(p-q,0),p*(p-1))
    K=(F(q-1)*q/p+F(p-1)+F(q,p+q)) if q>=p else (F(q-1)+F(p*(p-1)**2,p*p-q)+F(p,p+q))
    return b,c,K


def reduced_derivative_num(p,q,b):
    A=F(q-1,p)+F(1,p+q)
    return -A/b**2 + F(q*(p-1)**2)/(p-q*b)**2


def run():
    count=0
    # Global symbolic derivative certificate: endpoint derivative is negative
    # throughout the two integer-size regimes.
    for p,q in product(range(2,181),repeat=2):
        b,c,K=optimum(p,q)
        assert b>0 and c>=0 and p*b<=1 and q*b+(p-1)*c<=1
        assert reduced_derivative_num(p,q,b)<0
        assert kemeny_spectrum(p,q,b,c)==K
        b0=F(1,max(p,q))
        K_no_clique=kemeny_spectrum(p,q,b0,F(0))
        exact_gap=F(p*p*(p-1)*(p-q),q*(p*p-q)) if p>q else F(0)
        assert K_no_clique-K==exact_gap
        if p>q:
            assert c>0 and p*b==1 and q*b+(p-1)*c==1
        else:
            assert c==0 and q*b==1 and p*b<=1
        count+=5
    # Matrix verification at nonoptimal feasible rational weights, as well as
    # the published closed-form optimum, using entirely independent inversion.
    for p,q in product(range(2,7),repeat=2):
        b,c,K=optimum(p,q)
        assert kemeny_by_inverse(p,q,b,c)==K
        count+=1
        for frac in (F(1,4),F(1,2),F(3,4)):
            B=b*frac
            C=(F(1)-q*B)/(p-1)
            assert kemeny_by_inverse(p,q,B,C)==kemeny_spectrum(p,q,B,C)
            assert kemeny_spectrum(p,q,B,C)>K
            count+=2
    # Exact finite line-segment tests inside the two-dimensional feasible cone.
    for p,q in product(range(2,20),repeat=2):
        b,c,K=optimum(p,q)
        for t in (F(1,5),F(2,5),F(3,5),F(4,5)):
            B=t*b
            for u in (F(0),F(1,2),F(1)):
                C=u*(1-q*B)/(p-1)
                assert B>0 and C>=0
                assert kemeny_spectrum(p,q,B,C)>K
                count+=2
    print('PASS:',count,'exact checks; 2<=p,q<=180 endpoint proof samples, exact matrix inverses, feasible-grid comparisons')

if __name__=='__main__':
    run()
