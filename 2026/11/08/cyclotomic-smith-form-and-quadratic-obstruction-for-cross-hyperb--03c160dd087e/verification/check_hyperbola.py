#!/usr/bin/env python3
"""Standalone modular-coefficient and complex-rank tests for cross-hyperbola sampling."""
from math import comb, pi
from cmath import exp


def primes(n):
    return [x for x in range(3,n+1,2) if all(x % d for d in range(2,int(x**0.5)+1))]


def coeff(p,c,r,j):
    # Reduction of the coefficient at (zeta_p-1)^j for the r-th Teichmuller twist.
    return sum(pow(u,r,p)*comb((u+c*pow(u,-1,p))%p,j)
               for u in range(1,p))%p


def numerical_rank(mat, tol=1.e-7):
    mat=[row[:] for row in mat]
    n=len(mat)
    i=0
    for j in range(n):
        pivot=max(range(i,n),key=lambda k:abs(mat[k][j]),default=None)
        if pivot is None or abs(mat[pivot][j])<tol:
            continue
        mat[i],mat[pivot]=mat[pivot],mat[i]
        v=mat[i][j]
        for k in range(i+1,n):
            alpha=mat[k][j]/v
            for h in range(j+1,n):
                mat[k][h]-=alpha*mat[i][h]
            mat[k][j]=0
        i+=1
    return i


def check(p):
    N=p-1
    half=N//2
    legendre=lambda c:pow(c,half,p)
    nonsquare=next(c for c in range(2,p) if legendre(c)==p-1)
    for c in (1,nonsquare):
        for r in range(N):
            d=min(r,N-r)
            values=[coeff(p,c,r,j) for j in range(d+1)]
            assert all(v==0 for v in values[:d]),(p,c,r,values)
            if r==half and legendre(c)==p-1:
                assert values[d]==0
                # Exact integer cyclotomic coefficient cancellation, not floating point.
                xcoeff=[sum(1 if legendre(u)==1 else -1
                            for u in range(1,p) if (u+c*pow(u,-1,p))%p==x)
                        for x in range(p)]
                assert xcoeff==[0]*p,(p,c,xcoeff)
            else:
                assert values[d]!=0,(p,c,r,values)
        mat=[[exp(2j*pi*((s*t+c*pow(s*t,-1,p))%p)/p)
              for t in range(1,p)] for s in range(1,p)]
        rank=numerical_rank(mat)
        assert rank==N-int(legendre(c)==p-1),(p,c,rank)
        if legendre(c)==p-1:
            null=[1 if legendre(t)==1 else -1 for t in range(1,p)]
            assert max(abs(sum(a*b for a,b in zip(row,null))) for row in mat)<1.e-7
    return p

if __name__=='__main__':
    tested=[check(p) for p in primes(31)]
    print('CROSS_HYPERBOLA_LOCAL_SMITH_PASS primes=',tested,'square_and_nonsquare_checked_each')
