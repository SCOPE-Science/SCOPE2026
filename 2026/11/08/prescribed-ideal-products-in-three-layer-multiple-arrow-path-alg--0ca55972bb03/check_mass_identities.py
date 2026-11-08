#!/usr/bin/env python3
"""Independent arithmetic consistency checks; prime powers used only as integer q."""
from functools import lru_cache

@lru_cache(None)
def gb(n,k,q):
    if k<0 or k>n:return 0
    if k==0 or k==n:return 1
    return gb(n-1,k,q)+q**(n-k)*gb(n-1,k-1,q)

@lru_cache(None)
def sub(n,q):return sum(gb(n,k,q) for k in range(n+1))

def rec(a,b,q):
    A=[sum(gb(b,z,q)*sub((a-u)*(b-z),q) for z in range(b+1)) for u in range(a+1)]
    B=[sum(gb(a,u,q)*sub((a-u)*(b-z),q) for u in range(a+1)) for z in range(b+1)]
    N=sum(gb(a,u,q)*A[u] for u in range(a+1))
    assert N==sum(gb(b,z,q)*B[z] for z in range(b+1))
    F0=N*(A[0]+B[0])-A[0]*B[0]
    pos=sum(gb(a,u,q)*gb(b,z,q)*A[u]*B[z] for u in range(1,a+1) for z in range(1,b+1))
    assert F0+pos==N*N
    N11=N-A[0]-B[0]+sub(a*b,q)
    bothzero=N*N-2*(N-A[0])*(N-B[0])+N11**2
    bothpossame=sum(gb(a,u,q)*gb(b,z,q)*sub((a-u)*(b-z),q)**2 for u in range(1,a+1) for z in range(1,b+1))
    C=bothzero+bothpossame
    assert 0<=C<=N*N
    return (N,F0,C)

if __name__=='__main__':
    checks=0
    for q in (2,3,4,5,7,8,9):
      for a in range(1,6):
       for b in range(1,6):
        assert rec(a,b,q)==rec(b,a,q)
        checks+=1
    assert rec(1,1,2)==(5,21,19)
    assert rec(2,1,2)==(17,234,199)
    assert rec(2,2,2)==(124,13695,12682)
    assert rec(2,2,3)==(303,87453,84851)
    print(f'PASS {checks} ordered (a,b,q) configurations; product mass, swapped-dimension symmetry, and commuting bounds.')
    print('ALL_THREE_LAYER_IDEAL_MASS_IDENTITIES_PASS')
