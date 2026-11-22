#!/usr/bin/env python3
"""Exact-rational verifier for weighted-star inverse-square grounded trace.

Usage: python3 verify.py  (stdlib only)
The general theorem is established analytically in RESULT.md; finite tests are diagnostics.
"""
from fractions import Fraction as F
from itertools import combinations
import random
import sys


def inv(A):
    n=len(A)
    if n==0:return []
    T=[[F(A[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next((i for i in range(c,n) if T[i][c]!=0),None)
        assert p is not None
        T[c],T[p]=T[p],T[c]
        v=T[c][c]
        T[c]=[x/v for x in T[c]]
        for i in range(n):
            if i==c:continue
            v=T[i][c]
            if v:T[i]=[a-v*b for a,b in zip(T[i],T[c])]
    return [row[n:] for row in T]


def direct(w,S):
    m=len(w); verts=[j for j in range(m+1) if j not in S]
    if not verts:return F(0)
    L=[[F(0)]*(m+1) for _ in range(m+1)]
    for j,x in enumerate(w,1):
        L[0][0]+=x;L[j][j]+=x;L[0][j]-=x;L[j][0]-=x
    G=inv([[L[i][j] for j in verts] for i in verts])
    return sum((G[i][j]*G[j][i] for i in range(len(verts)) for j in range(len(verts))), F(0))


def closed(w,S):
    m=len(w);r=m-len(S)
    if 0 in S:return sum((1/w[i-1]**2 for i in range(1,m+1) if i not in S),F(0))
    W=sum((w[i-1] for i in S),F(0))
    R=[w[i-1] for i in range(1,m+1) if i not in S]
    return sum((1/x**2 for x in R),F(0))+2*sum((1/x for x in R),F(0))/W+(len(R)+1)**2/W**2


def candidates(w,k):
    m=len(w); z=sorted(w)
    C=sum((1/x**2 for x in z[k-1:]),F(0))
    P=sum(z[:k],F(0)); A=sum((1/x for x in z[k:]),F(0))
    B=sum((1/x**2 for x in z[k:]),F(0))+2*A/P+(m-k+1)**2/P**2
    return C,B


def run():
    rng=random.Random(20261117)
    counts={'matrices':0,'minima':0,'threshold':0}
    weights=[(F(1),)*m for m in range(2,9)]
    weights += [tuple(F(j+1) for j in range(m)) for m in range(2,9)]
    weights += [tuple(F([1,2,3,5,8,13,21,34][j]) for j in range(m)) for m in range(2,9)]
    weights += [tuple(F(rng.randint(1,19),rng.randint(1,9)) for _ in range(m)) for m in range(2,9) for _ in range(6)]
    for w in weights:
        m=len(w)
        for k in range(1,m+1):
            vals=[]
            for S in combinations(range(m+1),k):
                a=closed(w,S); b=direct(w,S)
                assert a==b,('inverse mismatch',w,k,S,a,b)
                counts['matrices']+=1
                vals.append(a)
            C,B=candidates(w,k)
            assert min(vals)==min(C,B),('global minimum',w,k,min(vals),C,B)
            counts['minima']+=1
    for m in range(2,100):
        for k in range(1,m+1):
            C,B=candidates((F(1),)*m,k)
            pred=2*k*k+2*k-m*m-2*m-1
            assert (B<C)-(B>C)==(pred>0)-(pred<0) # False/True signs
            counts['threshold']+=1
    # The second-order objective switches later than first-order on the unit-weight six-leaf star.
    assert candidates((F(1),)*6,4)==(F(3),F(2)+F(4,4)+F(9,16)) # center=3; leaf cost=3.5625
    print('VERIFY_OK',counts)

if __name__=='__main__':run()
