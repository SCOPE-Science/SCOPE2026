#!/usr/bin/env python3
"""Exact arithmetic checks for equal-edge star pairwise averaging.

The proof for arbitrary star order is in RESULT.md. This program tests
independent finite-dimensional covariance recursions and exact formulas.
"""
from fractions import Fraction as F
from math import isqrt


def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return list(map(list, zip(*a)))


def build(m):
    n=m+1
    H=[]
    for leaf in range(1,n):
        w=[[F(int(i==j)) for j in range(n)] for i in range(n)]
        for a in [0,leaf]:
            for b in [0,leaf]:
                w[a][b]=F(1,2)
        H.append(w)
    return H


def operator(M, Ws):
    n=len(M)
    s=[[F(0) for _ in range(n)] for _ in range(n)]
    for W in Ws:
        tmp=matmul(matmul(W,M),W)
        for i in range(n):
            for j in range(n):
                s[i][j]+=tmp[i][j]/len(Ws)
    return s


def matrix_power(a,k):
    n=len(a)
    R=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for _ in range(k):R=matmul(R,a)
    return R


def trace(a):return sum(a[i][i] for i in range(len(a)))


def dot(a,b):return sum(x*y for x,y in zip(a,b))


def assertion():
    count=0
    for m in range(2,12):
        n=m+1
        ws=build(m)
        # h is unnormalized. Its squared norm is m(m+1).
        h=[F(m)]+[F(-1)]*m
        hnorm=F(m*n)
        H=[[h[i]*h[j]/hnorm for j in range(n)] for i in range(n)]
        J=[[F(1,n) for j in range(n)] for i in range(n)]
        S=[[F(int(i==j))-J[i][j]-H[i][j] for j in range(n)] for i in range(n)]
        alpha=F(m-1,2*m)
        c2=F(m*m-1,4*m*m)
        d=1-F(3,4*m)-F(1,4*m*m)
        M=[[alpha*alpha,c2],[c2/F(m-1),d]]
        # Check invariant covariance decomposition independently from pairwise matrices.
        OH=operator(H,ws)
        OS=operator(S,ws)
        predH=[[M[0][0]*H[i][j]+M[1][0]*S[i][j] for j in range(n)] for i in range(n)]
        predS=[[M[0][1]*H[i][j]+M[1][1]*S[i][j] for j in range(n)] for i in range(n)]
        for A,B in [(OH,predH),(OS,predS)]:
            for i in range(n):
                for j in range(n):
                    assert A[i][j]==B[i][j], (m,i,j,A[i][j],B[i][j]);count+=1
        # Independently iterate complete covariance matrix for two contrasting inputs.
        e=[F(0),F(1),F(-1)]+[F(0)]*(m-2)
        e=[x/F(2) for x in e]  # need not have unit norm; norm^2=1/2
        basis=[h,e]
        for x in basis:
            norm=dot(x,x)
            X=[[x[i]*x[j]/norm for j in range(n)] for i in range(n)]
            for k in range(7):
                Nk=matrix_power(M,k)
                q=Nk[0][0]+Nk[0][1]
                r=Nk[1][0]+Nk[1][1]
                expected=q if x==h else r
                assert trace(X)==expected,(m,k,trace(X),expected);count+=1
                X=operator(X,ws)
        # Verify quadratic recurrence and strict finite-horizon gap using exact fractions.
        nu=F(2*m-1,2*m)
        assert nu>alpha;count+=1
        U=F(1);V=F(1)
        for k in range(1,30):
            U,V=M[0][0]*U+M[0][1]*V,M[1][0]*U+M[1][1]*V
            assert U<V;count+=1
            assert V<nu**k if k>=2 else V==nu;count+=1
        # Characteristic polynomial at conventional one-step factor.
        tr=M[0][0]+M[1][1]
        det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
        assert tr==F(5*(m-1),4*m);count+=1
        assert det==F((m-2)*(m-1),4*m*m);count+=1
        assert nu*nu-tr*nu+det==F(m+1,8*m*m);count+=1
        assert nu>tr/2;count+=1
    return count

if __name__=='__main__':
    count=assertion()
    print('PASS exact rational finite assertions:',count)
