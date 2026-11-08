#!/usr/bin/env python3
"""Independent exhaustive matrix check for Jordan strata of ad_x on square-zero quiver algebras."""
from itertools import product
from collections import Counter
from math import comb

def rank_mod(matrix,q):
    M=[list(map(lambda x:x%q,row)) for row in matrix]
    if not M:return 0
    h=len(M);w=len(M[0]); r=0
    for c in range(w):
        k=next((j for j in range(r,h) if M[j][c]),None)
        if k is None:continue
        M[r],M[k]=M[k],M[r]
        inv=pow(M[r][c],-1,q); M[r]=[(v*inv)%q for v in M[r]]
        for j in range(h):
            if j!=r and M[j][c]:
                v=M[j][c]
                M[j]=[(M[j][t]-v*M[r][t])%q for t in range(w)]
        r+=1
        if r==h:break
    return r

def matmul(A,B,q):
    N=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(N))%q for j in range(N)]for i in range(N)]

def count_components(n,edges):
    p=list(range(n))
    def root(a):
        while p[a]!=a:a=p[a]
        return a
    for u,v in edges:
        a=root(u);b=root(v)
        if a!=b:p[a]=b
    return len({root(i)for i in range(n)})

def build_adjoint(n,edges,colors,weights,q):
    N=n+len(edges)
    # Full multiplication table constructed independently from idempotent-arrow products.
    P=[[[0]*N for j in range(N)]for i in range(N)]
    for i in range(n):P[i][i][i]=1
    for j,(u,v) in enumerate(edges):
        P[u][n+j][n+j]=1
        P[n+j][v][n+j]=1
    x=tuple(colors)+tuple(weights)
    out=[[0]*N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if x[i]:
                for k in range(N):out[k][j]=(out[k][j]+x[i]*(P[i][j][k]-P[j][i][k]))%q
    return out

def inspect(n,edges,q):
    m=len(edges);N=n+m
    direct=Counter();formula=Counter();nil_counts=Counter();count=0
    for c in product(range(q),repeat=n):
        zero=[a for a,(u,v) in enumerate(edges) if c[u]==c[v]]
        cross=m-len(zero)
        for support in product((0,1),repeat=len(zero)):
            F=[edges[zero[j]]for j,on in enumerate(support)if on]
            rho=n-count_components(n,F)
            formula[(cross,rho)]+=q**cross*(q-1)**sum(support)
        for e in product(range(q),repeat=m):
            A=build_adjoint(n,edges,c,e,q)
            rank=rank_mod(A,q)
            # Product p(A) over distinct nonzero ground-field eigenvalues.
            p=[[int(i==j)for j in range(N)]for i in range(N)]
            for lam in range(1,q):
                B=[[ (A[i][j] - (lam if i==j else 0))%q for j in range(N)]for i in range(N)]
                p=matmul(p,B,q)
            nil_rank=rank_mod(matmul(A,p,q),q)
            F=[(u,v)for (u,v),w in zip(edges,e)if w!=0 and c[u]==c[v]]
            target=n-count_components(n,F)
            assert nil_rank==target and rank==cross+target,(n,edges,q,c,e,rank,cross,target,nil_rank)
            direct[(cross,nil_rank)]+=1; count+=1
    assert direct==formula,(direct,formula)
    if len(edges)==n-1 and count_components(n,edges)==1:
        expect=Counter()
        for a in range(len(edges)+1):
            for b in range(len(edges)-a+1):
                t=len(edges)-a-b
                mult=comb(len(edges),a)*comb(len(edges)-a,b)
                expect[(b,a)]+=q*mult*(q-1)**a*(q*(q-1))**b
        assert direct==expect,(direct,expect)
    rank_counts=Counter()
    for (cross,nil),v in direct.items():rank_counts[cross+nil]+=v
    print(f"{q=} {n=} {edges=} {count=} ranks={dict(sorted(rank_counts.items()))} Jordan_pair_counts={dict(sorted(direct.items()))}")
    return direct
if __name__=='__main__':
    inspect(2,[],2)
    inspect(3,[(0,1),(1,2)],2)
    inspect(4,[(0,1),(1,2),(2,3)],2)
    inspect(4,[(0,1),(0,2),(0,3)],2)
    inspect(3,[(0,1),(1,2),(2,0)],2)
    inspect(2,[(0,1),(0,1)],2)
    inspect(4,[(0,1),(1,2),(2,3),(3,0)],2)
    inspect(3,[(0,1),(1,2)],3)
    inspect(4,[(0,1),(0,2),(0,3)],3)
    inspect(3,[(0,1),(1,2),(2,0)],3)
    inspect(2,[(0,1),(0,1)],3)
    print('DIRECT_ADJOINT_AND_JORDAN_PASS')
