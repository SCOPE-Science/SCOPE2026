#!/usr/bin/env python3
"""Independent finite-pair checks for noisy-voter correlations on wheel graphs.

Uses standard-library exact rational Gaussian elimination and Decimal spectral formula.
The finite calculations check illustrations and algebra, not the infinite monotonicity proof.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import gcd


def solve(A, b):
    n = len(b)
    A = [row[:] + [b[i]] for i,row in enumerate(A)]
    for j in range(n):
        i = next(i for i in range(j,n) if A[i][j])
        A[i],A[j] = A[j],A[i]
        piv = A[j][j]
        A[j] = [v/piv for v in A[j]]
        for k in range(j+1,n):
            factor=A[k][j]
            if factor:
                for m in range(j+1,n+1): A[k][m] -= factor*A[j][m]
                A[k][j]=F(0)
    x=[F(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=A[i][n]-sum(A[i][j]*x[j] for j in range(i+1,n))
    return x


def direct_pair(n, q):
    # rim vertices 0,...,n-1; hub n.
    vertices=list(range(n+1))
    N={i:((i-1)%n,(i+1)%n,n) for i in range(n)}
    N[n]=tuple(range(n))
    pairs=[(i,j) for i in vertices for j in vertices if i<j]
    ix={p:k for k,p in enumerate(pairs)}
    A=[[F(int(i==j)) for j in range(len(pairs))] for i in range(len(pairs))]
    rhs=[F(0) for _ in pairs]
    for row,(i,j) in enumerate(pairs):
        p=q/F(len(N[i])*len(N[j]))
        for u in N[i]:
            for v in N[j]:
                if u==v:rhs[row]+=p
                else:A[row][ix[tuple(sorted((u,v)))]]-=p
    x=solve(A,rhs)
    return x[ix[(0,n)]], {pair:x[k] for k,pair in enumerate(pairs)}


def closed(n,q):
    with localcontext() as ctx:
        ctx.prec=90
        Q=Decimal(q.numerator)/Decimal(q.denominator)
        delta=(1-4*Q/9).sqrt()
        t=(2*Q/9)/(1-2*Q/9+delta)
        l=n//gcd(n,2)
        H=(1-t**l)/(1+t**l)/(n*delta)
        k=2*Q/(3-Q)
        alpha=Q/(9-4*Q)
        return +(k*(alpha+(1-alpha)*H)/(1-4*k*alpha*(1-H)))


def run():
    nchecks=0
    for q in [F(1,4),F(4,9),F(9,16)]:
        prev=None
        for n in range(3,11):
            a, allpairs=direct_pair(n,q)
            with localcontext() as ctx:
                ctx.prec=80
                aD=Decimal(a.numerator)/Decimal(a.denominator)
                assert abs(aD-closed(n,q)) < Decimal('1e-70'), (q,n,a,aD-closed(n,q))
            nchecks+=1
            # Stationary pair equations checked separately on returned solution.
            assert all(F(0)<v<F(1) for v in allpairs.values())
            nchecks+=1
            if prev is not None:
                assert a<prev
                nchecks+=1
            prev=a
        # Closed-form theoretical sequence at larger sizes.
        prior=closed(10,q)
        for n in range(11,101):
            cur=closed(n,q)
            assert prior>cur
            prior=cur
            nchecks+=1
    # Exact small graphical examples with refresh probability 1/2.
    assert direct_pair(3,F(1,4))[0]==F(2,29)
    print('VERIFY_OK',nchecks,'exact pair/spectral and large-index assertions')

if __name__=='__main__':run()
