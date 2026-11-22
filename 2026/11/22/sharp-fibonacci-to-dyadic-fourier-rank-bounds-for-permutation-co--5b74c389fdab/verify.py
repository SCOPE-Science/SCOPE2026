#!/usr/bin/env python3
"""Exact small-order verification of permutation-edge Fourier rank extremizers.

Standard library only. Exhaustive labeled trees through six vertices.
The all-order proof is mathematical; this is a finite independent check.
"""
from itertools import product, permutations
from math import factorial


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def prufer_edges(seq, n):
    deg = [1]*n
    for x in seq: deg[x] += 1
    edges=[]
    for x in seq:
        u=next(i for i in range(n) if deg[i] == 1)
        edges.append((u,x)); deg[u]-=1; deg[x]-=1
    u,v=[i for i in range(n) if deg[i]==1]
    edges.append((u,v))
    return sorted((min(u,v),max(u,v)) for u,v in edges)


def root_states(n, edges, root=0):
    adj=[[] for _ in range(n)]
    for u,v in edges: adj[u].append(v); adj[v].append(u)
    def visit(v,p):
        A,B=1,0
        for u in adj[v]:
            if u==p: continue
            a,b=visit(u,v)
            A,B=A*(a+b)+B*a, B*(a+b)+A*a
        return A,B
    return visit(root,-1)


def brute_rank(n, edges):
    r=0
    for bits in product((0,1), repeat=n-1):
        adj=[[] for _ in range(n)]
        for take,(u,v) in zip(bits,edges):
            if take: adj[u].append(v);adj[v].append(u)
        seen=set(); valid=True
        for u in range(n):
            if u in seen: continue
            stack=[u];seen.add(u);vcount=0
            while stack:
                v=stack.pop();vcount+=1
                for w in adj[v]:
                    if w not in seen: seen.add(w);stack.append(w)
            if vcount % 2 == 0: valid=False;break
        r+=valid
    return r


def is_path(n,edges):
    deg=[0]*n
    for u,v in edges:deg[u]+=1;deg[v]+=1
    return max(deg) <= 2


def is_star(n,edges):
    deg=[0]*n
    for u,v in edges:deg[u]+=1;deg[v]+=1
    return max(deg) == n-1


def signed_multiplier(n,edges,mask):
    total=0
    for perm in permutations(range(n)):
        neg=sum(perm[u]>perm[v] for j,(u,v) in enumerate(edges) if mask>>j & 1)
        total += -1 if neg%2 else 1
    return total


def verify():
    tree_count=0; frequencies=0
    for n in range(2,7):
        low,high=fib(n),2**(n-2)
        for seq in product(range(n),repeat=n-2):
            edges=prufer_edges(seq,n)
            a,b=root_states(n,edges)
            rank=brute_rank(n,edges)
            assert a==rank, (n,seq,a,rank)
            assert low<=rank<=high,(n,seq,rank,low,high)
            if n>=4:
                assert (rank==low)==is_path(n,edges)
                assert (rank==high)==is_star(n,edges)
            for root in range(n):
                ar,br=root_states(n,edges,root)
                assert ar==a and ar>=fib(n) and br>=fib(n-1)
            tree_count+=1
    # All multipliers for each small labelled tree, testing zero-pattern directly.
    for n in range(2,6):
        for seq in product(range(n),repeat=n-2):
            edges=prufer_edges(seq,n)
            for mask in range(1<<(n-1)):
                # Number of connected components of selected forest with even vertex size.
                sub=[edges[i] for i in range(n-1) if mask>>i & 1]
                adj=[[] for _ in range(n)]
                for u,v in sub: adj[u].append(v);adj[v].append(u)
                seen=set();allowed=True
                for i in range(n):
                    if i in seen:continue
                    stack=[i];seen.add(i);size=0
                    while stack:
                        v=stack.pop();size+=1
                        for w in adj[v]:
                            if w not in seen:seen.add(w);stack.append(w)
                    if size%2==0:allowed=False;break
                val=signed_multiplier(n,edges,mask)
                assert (val!=0)==allowed,(n,seq,mask,val,allowed)
                frequencies+=1
    print('PASS',tree_count,'labeled-tree DP/exhaustive rank instances;',frequencies,'exact signed Fourier multipliers')


if __name__=='__main__': verify()
