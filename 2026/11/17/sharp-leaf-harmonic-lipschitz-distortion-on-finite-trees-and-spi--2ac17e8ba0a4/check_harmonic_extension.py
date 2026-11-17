#!/usr/bin/env python3
"""Exact arithmetic diagnostics for leaf-harmonic Lipschitz extension on finite trees.

Runs with Python 3 standard library only. Independent finite checks do not
replace the proofs for arbitrary trees or arbitrarily many arms.
"""
from fractions import Fraction as F
from itertools import product
from collections import deque


def gauss(A,b):
    n=len(b); a=[[F(x) for x in row]+[F(y)] for row,y in zip(A,b)]
    for k in range(n):
        t=next(j for j in range(k,n) if a[j][k])
        a[k],a[t]=a[t],a[k]
        c=a[k][k]; a[k]=[z/c for z in a[k]]
        for j in range(n):
            if j!=k:
                c=a[j][k]; a[j]=[u-c*v for u,v in zip(a[j],a[k])]
    return [row[-1] for row in a]


def spider(lengths):
    edges=[]; leaves=[]; count=1
    for L in lengths:
        v=0
        for _ in range(L):
            edges.append((v,count)); v=count; count+=1
        leaves.append(v)
    return count,edges,leaves


def harmonic_matrix(n,edges,leaves):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    B=set(leaves); I=[v for v in range(n) if v not in B]
    H=[[F(int(v==l)) for l in leaves] for v in range(n)]
    for k in range(len(leaves)):
        M=[[F(len(adj[v]) if v==w else -int(w in adj[v])) for w in I] for v in I]
        rhs=[F(int(leaves[k] in adj[v])) for v in I]
        z=gauss(M,rhs)
        for v,val in zip(I,z):H[v][k]=val
    return H


def signed_edge_extrema(n,edges,leaves,H):
    adj=[[] for _ in range(n)]
    for i,(a,b) in enumerate(edges):adj[a].append((b,i,1));adj[b].append((a,i,-1))
    parent=[(-1,-1,0)]*n; parent[0]=(0,-1,0)
    q=deque([0])
    while q:
        v=q.popleft()
        for w,i,sgn in adj[v]:
            if parent[w][0]<0: parent[w]=(v,i,sgn);q.append(w)
    M=F(0)
    for z in product((-1,1),repeat=len(edges)):
        values=[F(0)]*n
        for v in range(1,n):
            parentv,idx,sgn=parent[v]
            # The construction labels arms away from 0; parent index smaller.
            values[v]=values[parentv]+sgn*z[idx]
        b=[values[l] for l in leaves]
        h=[sum(H[v][k]*b[k] for k in range(len(leaves))) for v in range(n)]
        M=max(M,max(abs(h[u]-h[v]) for u,v in edges))
    return M


def exact_formula(lengths):
    m=len(lengths)
    if m<=2:return F(1)
    minimum=min(lengths)
    denom=F(minimum)*sum((F(1,x) for x in lengths),F(0))
    return F(1)+F(m-2)/denom


def compositions(S,m):
    if m==1:yield (S,);return
    for i in range(1,S-m+2):
        for tail in compositions(S-i,m-1): yield (i,)+tail


def balanced_formula(n,m):
    s=m-1;Q=n-2;q,r=divmod(Q,s)
    return F(1)+F(m-2)/(F(1)+F(s-r,q)+F(r,q+1))


def cut_formula(n,edges,leaves,H):
    adj=[[] for _ in range(n)]
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    rows=[]
    for u,v in edges:
        nu=[H[u][j]-H[v][j] for j in range(len(leaves))]
        val=F(0)
        for x,y in edges:
            todo=[y];seen={x,y};comp={y}
            while todo:
                z=todo.pop()
                for t in adj[z]:
                    if t not in seen:
                        seen.add(t);comp.add(t);todo.append(t)
            val+=abs(sum((nu[j] for j,b in enumerate(leaves) if b in comp),F(0)))
        rows.append(val)
    return max(rows)


def verify():
    count=0
    configs=((1,1,1),(1,1,2),(1,2,3),(2,2,2),(1,1,1,1),(1,2,2,2),
             (1,1,3,3),(1,3,4),(2,3,3),(1,2,4))
    for lengths in configs:
        n,edges,leaves=spider(lengths)
        H=harmonic_matrix(n,edges,leaves)
        res=signed_edge_extrema(n,edges,leaves,H)
        expect=exact_formula(lengths)
        assert res==expect,(lengths,res,expect)
        count+=1
    print('EXACT_HARMONIC_DIRICHLET_VS_INDEPENDENT_SIGN_ENUMERATION_PASSED',count)
    irregular_trees=[(6,[(0,1),(1,2),(1,3),(3,4),(3,5)]),
                     (7,[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]),
                     (8,[(0,1),(0,2),(1,3),(1,4),(3,5),(3,6),(6,7)]),
                     (8,[(i,i+1) for i in range(7)])]
    for n,edges in irregular_trees:
        degree=[0]*n
        for u,v in edges:degree[u]+=1;degree[v]+=1
        leaves=[i for i,d in enumerate(degree) if d==1]
        H=harmonic_matrix(n,edges,leaves)
        assert cut_formula(n,edges,leaves,H)==signed_edge_extrema(n,edges,leaves,H)
    print('GENERAL_TREE_HARMONIC_MEASURE_CUT_IDENTITY_CHECKS_PASSED',len(irregular_trees))
    count=0
    for n in range(4,13):
        for m in range(3,n):
            actual=max(exact_formula(c) for c in compositions(n-1,m))
            expect=balanced_formula(n,m)
            assert actual==expect,(n,m,actual,expect)
            count+=1
    print('EXHAUSTIVE_FIXED_ORDER_AND_LEAF_COUNT_SPIDER_EXTREMA_PASSED',count)
    for n in (25,100,400,1600):
        Q=n-2;s=int(Q**.5); q,r=divmod(Q,s)
        lengths=(1,)+(q,)*(s-r)+(q+1,)*r
        norm=exact_formula(lengths)
        assert 2*float(norm-1)/Q**0.5>1-5/Q**0.5
    print('SQRT_ORDER_ASYMPTOTIC_WITNESSES_PASSED',4)
    print('ALL_HARMONIC_EXTENSION_DIAGNOSTICS_PASSED')

if __name__=='__main__':verify()
