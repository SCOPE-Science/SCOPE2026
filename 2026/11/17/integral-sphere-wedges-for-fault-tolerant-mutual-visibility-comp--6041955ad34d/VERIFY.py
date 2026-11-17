#!/usr/bin/env python3
"""Direct-enumeration finite checks for redundant-geodesic visibility complexes.
Enumeration derives geodesics from graph adjacency, not from a face formula.
"""
from itertools import combinations
from math import comb
from collections import deque

def graph(m,n):
    vertices=list(range(m+n))
    adj=[set() for _ in vertices]
    for a in range(m):
        for b in range(m,m+n): adj[a].add(b); adj[b].add(a)
    return adj

def shortest_paths(adj,u,v):
    dist={u:0}; Q=deque([u]); paths=[]
    while Q:
        x=Q.popleft()
        for y in adj[x]:
            if y not in dist:dist[y]=dist[x]+1;Q.append(y)
    target=dist[v]
    def rec(x,path):
        if len(path)-1==target:
            if x==v:paths.append(tuple(path))
            return
        for y in sorted(adj[x]):
            if dist[y]==dist[x]+1: rec(y,path+[y])
    rec(u,[u]);return paths

def face_by_paths(adj,q,S):
    chosen=set(S)
    for u,v in combinations(S,2):
        if v in adj[u]: continue  # adjacent pairs need only one edge
        mids=[]
        for path in shortest_paths(adj,u,v):
            if not set(path[1:-1]) & chosen: mids.append(set(path[1:-1]))
        # generalized brute force: test whether q paths have pairwise disjoint interiors
        def can_pack(k,used,start):
            if k==0:return True
            for p in range(start,len(mids)):
                if mids[p].isdisjoint(used) and can_pack(k-1,used|mids[p],p+1): return True
            return False
        if not can_pack(q,set(),0): return False
    return True

def formula(m,n,q):
    a,b=m-q,n-q;out={}
    for i in range(m+1):
        for j in range(n+1):
            valid=(i<=a and j<=b) or (j<=1) or (i<=1)
            if valid:out[i+j]=out.get(i+j,0)+comb(m,i)*comb(n,j)
    return out

def rank_F2(cols):
    basis={};k=0
    for v in cols:
        while v:
            p=v.bit_length()-1
            if p in basis: v^=basis[p]
            else:basis[p]=v;k+=1;break
    return k

def compute(m,n,q):
    adj=graph(m,n);N=m+n
    faces_by_dim={}
    for mask in range(1,1<<N):
        S=tuple(i for i in range(N) if mask>>i&1)
        if face_by_paths(adj,q,S):faces_by_dim.setdefault(len(S)-1,[]).append(mask)
    pred=formula(m,n,q)
    actual={d+1:len(fs) for d,fs in faces_by_dim.items()};actual[0]=1
    assert pred==actual,(m,n,q,pred,actual)
    ranks={-1:0}
    for d,fs in faces_by_dim.items():
        if d==0:ranks[0]=1;continue # augmented degree zero boundary all 1
        prev={f:i for i,f in enumerate(faces_by_dim[d-1])}
        cols=[]
        for f in fs:
            v=0
            for i in range(N):
                if f>>i&1:v^=1<<prev[f^(1<<i)]
            cols.append(v)
        ranks[d]=rank_F2(cols)
    # rank[d] is rank of boundary d to d-1, rank0 augmented
    betti={d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0) for d,fs in faces_by_dim.items()}
    betti={d:v for d,v in betti.items() if v}
    a,b=m-q,n-q
    predicted={}
    for d,v in [(a+b-1,comb(m-1,q-1)*comb(n-1,q-1)),(a+1,(n-1)*comb(m-1,q-1)),(b+1,(m-1)*comb(n-1,q-1))]:predicted[d]=predicted.get(d,0)+v
    assert betti==predicted,(m,n,q,betti,predicted)
    print(f'PASS m={m} n={n} q={q} f={tuple(actual.get(i,0) for i in range(max(actual)+1))} reduced_mod2_betti={betti} total_nonempty_faces={sum(len(x) for x in faces_by_dim.values())}')
    return sum(len(x) for x in faces_by_dim.values())

if __name__=='__main__':
    checks=[(4,4,1),(4,4,2),(5,5,2),(5,5,3),(5,6,3),(6,5,2),(6,6,3)]
    total=0
    for args in checks:total+=compute(*args)
    print('ALL_FAULT_TOLERANT_VISIBILITY_CHECKS_PASS','cases=',len(checks),'nonempty_faces=',total)
