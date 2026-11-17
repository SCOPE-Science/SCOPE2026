#!/usr/bin/env python3
"""Exact independent modular rank tests for second-order graph waves on punctured rook graphs."""

def matmul(A,B):
    return [[sum(x*y for x,y in zip(row,col))%3 for col in zip(*B)] for row in A]

def rank(A):
    B=[r[:] for r in A]; m=len(B); n=len(B[0]); i=0
    for j in range(n):
        p=next((k for k in range(i,m) if B[k][j]),None)
        if p is None: continue
        B[i],B[p]=B[p],B[i]
        if B[i][j]==2:B[i]=[(2*x)%3 for x in B[i]]
        for k in range(i+1,m):
            if B[k][j]:
                s=B[k][j]; B[k]=[(x-s*y)%3 for x,y in zip(B[k],B[i])]
        i+=1
        if i==m:break
    return i

def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def matpow(A,t):
    B=ident(len(A))
    while t:
        if t&1:B=matmul(B,A)
        A=matmul(A,A);t//=2
    return B

def expected_dim(m,n,t):
    h=m+n-4; j=(m-2)*(n-2)+1
    if t%2: return 0
    v=1; x=t
    while x%3==0:x//=3;v*=3
    return h*min(4,v)+j*min(2,v)+(4 if t%8==0 else 0)

checkcount=0
for m,n in [(3,3),(3,6),(6,3),(3,9),(6,6)]:
    vertices=[(i,j) for i in range(m) for j in range(n) if (i,j)!=(0,0)]
    k=len(vertices);A=[[int(i!=j and (a==c or b==d)) for j,(c,d) in enumerate(vertices)] for i,(a,b) in enumerate(vertices)]
    T=[[0]*(2*k) for _ in range(2*k)]
    for i in range(k):
        for j in range(k):T[i][j]=A[i][j]
        T[i][k+i]=2; T[k+i][i]=1
    eye=ident(2*k)
    for t in [1,2,3,4,6,8,9,12,18,24,36,72]:
        P=matpow(T,t)
        dim=2*k-rank([[(x-y)%3 for x,y in zip(row,er)] for row,er in zip(P,eye)])
        exp=expected_dim(m,n,t)
        assert dim==exp, (m,n,t,dim,exp)
        checkcount+=1
    assert matpow(T,72)==eye
    assert matpow(T,36)!=eye and matpow(T,24)!=eye
    print(f'PASS {m}x{n} minus corner: {2*k} time-coordinates, all 12 kernel dimensions and sharp order72')
print(f'PASS {checkcount} exact matrix kernel comparisons')
