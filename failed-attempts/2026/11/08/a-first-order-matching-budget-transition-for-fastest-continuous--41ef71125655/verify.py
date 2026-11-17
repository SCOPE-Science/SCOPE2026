#!/usr/bin/env python3
"""Exact-rational checks for a costed complete-bipartite Laplacian theorem.

This finite checker supplements a dimension-independent analytic proof.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import product


def matvec(L, v):
    return [sum(L[i][j]*v[j] for j in range(len(v))) for i in range(len(v))]


def laplacian(W):
    n=len(W)
    L=[[F(0) for _ in range(2*n)] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            w=W[i][j]
            L[i][i]+=w
            L[n+j][n+j]+=w
            L[i][n+j]-=w
            L[n+j][i]-=w
    return L


def eigenspace_tests(n,x,y):
    W=[[x if i==j else y for j in range(n)] for i in range(n)]
    L=laplacian(W)
    zero=[F(0)]*(2*n)
    for i in range(n-1):
        a=[F(0)]*n
        a[i]=F(1)
        a[-1]=F(-1)
        for v,eigen in [ (a+a,n*y), (a+[-z for z in a],2*x+(n-2)*y) ]:
            assert matvec(L,v)==[eigen*z for z in v]
    s=[F(1)]*n+[-F(1)]*n
    assert matvec(L,s)==[2*(x+(n-1)*y)*z for z in s]
    assert matvec(L,[F(1)]*(2*n))==zero
    return min(n*y,2*x+(n-2)*y)


def calc(n,B,c,ratio):
    crit=F(2*(n-1),n-2)
    upper=B/(n*(c+n-1))
    if c<crit:
        x=y=upper
    elif c>crit:
        x=F(0);y=B/(n*(n-1))
    else:
        x=upper*ratio
        y=(B/n-c*x)/(n-1)
    val=B/(n-1+c) if c<crit else F(n-2,n*(n-1))*B
    assert c*n*x+n*(n-1)*y==B
    assert y>0 and x>=0 and x<=y
    assert eigenspace_tests(n,x,y)==val
    return x,y,val


def trace_bounds(W):
    n=len(W); L=laplacian(W)
    # Orthonormal E/O trace via sum of projected energy matrices.
    # P = I - J/n, and trace(P M) = trace(M) - sum(M)/n.
    def compression_trace(sign):
        M=[[F(0) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                M[i][j]=(L[i][j]+sign*L[i][n+j]
                     +sign*L[n+i][j]+L[n+i][n+j])/2
        return (sum(M[i][i] for i in range(n))-
                sum(sum(row) for row in M)/n)/(n-1)
    off=sum((W[i][j] for i in range(n) for j in range(n) if i!=j),F(0))
    diag=sum((W[i][i] for i in range(n)),F(0))
    assert compression_trace(1)==off/(n-1)
    assert compression_trace(-1)==F(2,n)*diag+F(n-2,n*(n-1))*off


def main():
    tests=0
    for n in range(3,17):
        crit=F(2*(n-1),n-2)
        costs=[F(1,7),F(1),crit*F(3,4),crit,crit*F(5,4),crit*3]
        for B,c in product([F(1),F(7,3),F(19,5)],costs):
            for r in [F(0),F(1,2),F(1)] if c==crit else [F(1)]:
                x,y,val=calc(n,B,c,r)
                assert val>0
                tests+=1
    for n in range(3,11):
        for k in range(1,16):
            W=[[F(((7*i+11*j+3*k+i*j)%29)+1,((i+2*j+k)%7)+2)
                for j in range(n)] for i in range(n)]
            trace_bounds(W)
            tests+=1
    # Verify strict increase in symmetric small-price branch and
    # strict decrease in the high-price branch for rational examples.
    for n in range(3,17):
        crit=F(2*(n-1),n-2); B=F(5)
        for c in [crit/2,crit,crit*2]:
            x,y,v=calc(n,B,c,F(1,2))
            assert v==(B/(n-1+c) if c<crit else B*F(n-2,n*(n-1)))
            tests+=1
    print('VERIFY_OK', tests)

if __name__=='__main__': main()
