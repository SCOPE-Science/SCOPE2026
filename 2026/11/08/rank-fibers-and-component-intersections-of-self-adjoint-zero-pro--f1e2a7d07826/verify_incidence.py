#!/usr/bin/env python3
"""Independent exhaustive set-theoretic checks of rank-component incidence over F_2."""
from itertools import product
from math import prod

def rank2(A):
    B=[list(x) for x in A]
    n=len(B); pivot=0
    for c in range(n):
        row=next((j for j in range(pivot,n) if B[j][c]),None)
        if row is None: continue
        B[pivot],B[row]=B[row],B[pivot]
        for j in range(n):
            if j!=pivot and B[j][c]:
                B[j]=[a^b for a,b in zip(B[j],B[pivot])]
        pivot+=1
    return pivot

def sym(n):
    ij=[(i,j) for i in range(n) for j in range(i,n)]
    for values in product((0,1),repeat=len(ij)):
        M=[[0]*n for _ in range(n)]
        for (i,j),a in zip(ij,values):M[i][j]=M[j][i]=a
        yield M

def mulzero(A,B):
    n=len(A)
    return all((sum(A[i][k]*B[k][j] for k in range(n))%2)==0
               for i in range(n) for j in range(n))

def g(n,k,q):
    return (prod(q**(n-i)-1 for i in range(k)) //
            prod(q**(k-i)-1 for i in range(k)))

def s(m,q):
    u=(m+1)//2
    return q**(m*(m+1)//2)*prod(q**(2*i-1)-1 for i in range(1,u+1))//prod(q**(2*i-1) for i in range(1,u+1))

def pred_intersection(n,i,j,q):
    return sum(g(n,a,q)*s(a,q)*g(n-a,b,q)*s(b,q)
               for a in range(i+1) for b in range(n-j+1))

for n in range(1,4):
    mats=list(sym(n)); ranks=list(map(rank2,mats)); P=[]
    for idx,A in enumerate(mats):
        for jdx,B in enumerate(mats):
            if mulzero(A,B):P.append((ranks[idx],ranks[jdx]))
    assert len(P)==sum(g(n,a,2)*s(a,2)*2**((n-a)*(n-a+1)//2) for a in range(n+1))
    for i in range(n+1):
        Ci=[(a,b) for a,b in P if a<=i and b<=n-i]
        assert len(Ci)==pred_intersection(n,i,i,2)
        for j in range(i,n+1):
            overlap=[(a,b) for a,b in P if a<=i and b<=n-j]
            assert len(overlap)==pred_intersection(n,i,j,2)
            assert all((a<=i and b<=n-j) for a,b in overlap)
    assert all(any(a<=i and b<=n-i for i in range(n+1)) for a,b in P)
    print('COMPONENT_INCIDENCE',n,'TOTAL',len(P),'COMPONENT_COUNTS', [pred_intersection(n,i,i,2) for i in range(n+1)])
print('ALL_SELFADJOINT_INCIDENCE_TESTS_PASS')
