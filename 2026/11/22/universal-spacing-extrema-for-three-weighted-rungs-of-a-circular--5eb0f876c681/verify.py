"""Exact finite diagnostics for weighted rung arrangements on circular ladders.

Usage: python3 verify.py. No third-party packages are required.
"""
from fractions import Fraction as F
from itertools import combinations


def inverse_rational(M):
    n=len(M)
    a=[[F(x) for x in M[i]]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        l=next((i for i in range(k,n) if a[i][k]),None)
        assert l is not None
        a[k],a[l]=a[l],a[k]
        v=a[k][k];a[k]=[x/v for x in a[k]]
        for i in range(n):
            if i!=k and a[i][k]:
                v=a[i][k];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
    return [row[n:] for row in a]


def rung_kernel(n):
    M=[[4*(i==j)-(j==(i+1)%n)-(j==(i-1)%n) for j in range(n)] for i in range(n)]
    B=inverse_rational(M)
    return [[2*x for x in row] for row in B]


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
          - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
          + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def ratio(K,ind,t):
    u=F(t)-1
    return det3([[F(i==j)+u*K[ind[i]][ind[j]] for j in range(3)] for i in range(3)])


def bareiss(A):
    A=[[F(x) for x in row] for row in A]
    N=len(A); sign=1; prev=F(1)
    for k in range(N-1):
        if not A[k][k]:
            h=next((j for j in range(k+1,N) if A[j][k]),None)
            assert h is not None
            A[k],A[h]=A[h],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,N):
            for j in range(k+1,N):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])/prev
            A[i][k]=F(0)
        prev=pivot
    return sign*A[-1][-1]


def full_tree_count(n,inds,t):
    N=2*n; L=[[F(0) for _ in range(N)] for __ in range(N)]
    def add(i,j,w):
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    for s in range(2):
        for j in range(n):add(s*n+j,s*n+(j+1)%n,F(1))
    for j in range(n): add(j,n+j,F(t) if j in inds else F(1))
    return bareiss([row[:-1] for row in L[:-1]])


def cheb_tau(n):
    a,b=1,2
    for i in range(n):a,b=b,4*b-a
    return n*(a-1)


def gaps(n,ind):
    a,b,c=ind
    return tuple(sorted((b-a,c-b,n-c+a)))


def tests():
    checks=0
    for n in range(5,18):
        K=rung_kernel(n)
        assert all(K[i][j]==K[0][(j-i)%n] for i in range(n) for j in range(n));checks+=n*n
        for t in (F(1,5),F(1,2),F(2),F(5)):
            vals=[]
            for inds in combinations(range(n),3):
                val=ratio(K,inds,t)
                gp=gaps(n,inds)
                vals.append((val,gp))
                # Each gap-redistribution with the third gap unchanged must increase the tree polynomial.
                x,y,z=(inds[1]-inds[0],inds[2]-inds[1],n-inds[2]+inds[0])
                if y>=x+2:
                    j=(0,x+1,x+y)
                    assert ratio(K,j,t)>val
                checks+=1
            minv=min(v for v,g in vals)
            maxv=max(v for v,g in vals)
            assert {g for v,g in vals if v==minv}=={(1,1,n-2)}
            q,rem=divmod(n,3)
            expected=tuple(sorted([q,q,q+rem] if rem<2 else [q,q+1,q+1]))
            assert {g for v,g in vals if v==maxv}=={expected}
            checks+=2
    for n in range(5,10):
        K=rung_kernel(n)
        base=full_tree_count(n,(),1)
        assert base==cheb_tau(n)
        for t in (F(1,3),F(2),F(7,2)):
            for inds in combinations(range(n),3):
                assert full_tree_count(n,inds,t)==base*ratio(K,inds,t)
                checks+=1
    print('VERIFY_OK',checks,'exact rational tests')

if __name__=='__main__':tests()
