#!/usr/bin/env python3
"""Independent finite cellular checks for power-cycle independence complexes."""
from itertools import combinations

def rank(A,p):
    A=[list(map(lambda x:x%p,row)) for row in A]
    if not A: return 0
    n=len(A); k=len(A[0]); i=0
    for j in range(k):
        piv=next((z for z in range(i,n) if A[z][j]),None)
        if piv is None: continue
        A[i],A[piv]=A[piv],A[i]
        inv=pow(A[i][j],-1,p); A[i]=[(x*inv)%p for x in A[i]]
        for z in range(n):
            if z!=i and A[z][j]:
                a=A[z][j];A[z]=[(u-a*v)%p for u,v in zip(A[z],A[i])]
        i+=1
        if i==n:break
    return i

def calc(m):
    n=3*m; verts=range(n)
    edges=[(i,j) for i in verts for j in range(i+1,n) if min(j-i,n-j+i)>=m]
    triples=[(i,i+m,i+2*m) for i in range(m)]
    E=len(edges); lookup={e:i for i,e in enumerate(edges)}
    d1=[[0]*E for _ in verts]
    d2=[[0]*m for _ in edges]
    for j,(a,b) in enumerate(edges): d1[a][j]=-1;d1[b][j]=1
    for i,(a,b,c) in enumerate(triples):
        for e,v in [((b,c),1),((a,c),-1),((a,b),1)]:d2[lookup[e]][i]=v
    g=[[0]*E for _ in edges]
    for j,(a,b) in enumerate(edges):
        aa=(a+m)%n; bb=(b+m)%n
        ee=tuple(sorted((aa,bb)));sgn=1 if aa<bb else -1
        g[lookup[ee]][j]=sgn
    for p in (2,3,5):
        assert rank(d1,p)==n-1
        assert rank(list(map(list,zip(*d2))),p)==m
        assert E-(n-1)-m==(m-1)*(3*m-2)//2
        for i in range(n):
            for j in range(m):
                assert sum(d1[i][k]*d2[k][j] for k in range(E))==0
        for i in range(E):
            for j in range(m):
                assert sum(g[i][k]*d2[k][j] for k in range(E))==d2[i][j]
    # Signed Lefschetz calculation: vertex fixed = 0, edge fixed orbit =0,
    # triangular 2-simplices fixed setwise and cyclically permuted (+).
    # Reduced trace of g on H1 = -m + 1 (Lefschetz correction).
    fixed0=sum((i+m)%n==i for i in verts)
    fixed1=sum(g[i][i] for i in range(E))
    fixed2=m
    trace=1-(fixed0-fixed1+fixed2)
    assert trace==1-m
    print(f'm={m}: vertices={n}, edges={E}, triangles={m}, H1_rank={(m-1)*(3*m-2)//2}, order3_trace={trace}, free_R={((m-1)*(m-2))//2}, Eisenstein={m-1}; mod-p ranks verified')

if __name__=='__main__':
    for m in range(2,9): calc(m)
    print('POWER_CYCLE_C3_INTEGRAL_CELLULAR_CHECK_PASS')

def nullspace(A,p):
    B=[[v%p for v in row] for row in A]
    rows=len(B); cols=len(B[0]); pivots=[]; r=0
    for c in range(cols):
        piv=next((i for i in range(r,rows) if B[i][c]),None)
        if piv is None: continue
        B[r],B[piv]=B[piv],B[r]
        mul=pow(B[r][c],-1,p);B[r]=[(v*mul)%p for v in B[r]]
        for i in range(rows):
            if i!=r and B[i][c]:
                fac=B[i][c];B[i]=[(a-fac*b)%p for a,b in zip(B[i],B[r])]
        pivots.append(c);r+=1
        if r==rows:break
    frees=[c for c in range(cols) if c not in pivots]
    out=[]
    for c in frees:
        v=[0]*cols;v[c]=1
        for i,k in enumerate(pivots):v[k]=(-B[i][c])%p
        out.append(v)
    return out

def jordan(m):
    n=3*m
    ed=[(a,b) for a in range(n) for b in range(a+1,n) if min(b-a,n-b+a)>=m]
    E=len(ed); edge_ix={e:i for i,e in enumerate(ed)}
    d1=[[0]*E for _ in range(n)]
    d2=[[0]*m for _ in range(E)]
    T=[[0]*E for _ in range(E)]
    for j,(a,b) in enumerate(ed):
        d1[a][j]=-1;d1[b][j]=1
        a2=(a+m)%n;b2=(b+m)%n
        idx=edge_ix[tuple(sorted((a2,b2)))];T[idx][j]+=1 if a2<b2 else -1
        T[j][j]-=1
    for i in range(m):
        a,b,c=i,i+m,i+2*m
        for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:d2[edge_ix[e]][i]=s
    K=nullspace(d1,3)
    U=[[sum(T[i][j]*v[j] for j in range(E))%3 for i in range(E)] for v in K]
    V=[[sum(T[i][j]*v[j] for j in range(E))%3 for i in range(E)] for v in U]
    def combined_rank(vecs):
        mat=[[d2[i][k] for k in range(m)]+[v[i] for v in vecs] for i in range(E)]
        return rank(mat,3)-m
    r1=combined_rank(U);r2=combined_rank(V)
    q=(m-1)*(m-2)//2
    assert r1==2*q+(m-1),(m,r1)
    assert r2==q,(m,r2)
    print(f'  F3 action: rank(g-I)={r1}, rank((g-I)^2)={r2}, predicted blocks J3={q}, J2={m-1}')

if __name__=='__main__':
    for m in range(2,9):jordan(m)
    print('POWER_CYCLE_C3_MOD3_JORDAN_CHECK_PASS')
