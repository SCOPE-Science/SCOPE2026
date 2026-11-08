#!/usr/bin/env python3
"""Reproduce finite checks for the robust-clique complexes of quadrilateral bouquets.
This verifier is independent of the symbolic critical-face classification: faces are
built by dynamic programming on the induced-subgraph independence number.
"""
from collections import deque, Counter
from itertools import combinations
from math import comb


def graph(m):
    n = 3*m+1
    E = []
    for i in range(m):
        a,b,c = 3*i+1,3*i+2,3*i+3
        E.extend(((0,a),(a,b),(b,c),(c,0)))
    adj = [0]*n
    for u,v in E:
        adj[u] |= 1<<v
        adj[v] |= 1<<u
    return n, adj


def compute_faces(m,k):
    n, adj = graph(m)
    alpha = bytearray(1<<n)
    for s in range(1,1<<n):
        bit = s & -s
        v = bit.bit_length()-1
        without = s ^ bit
        alpha[s] = max(alpha[without], 1+alpha[without & ~adj[v]])
    F = {s for s in range(1,1<<n) if alpha[s] < k}
    return n, adj, F


def morse_matching(m,k,F):
    active = F.copy()
    pairs = {}
    stages = [0]+[3*i+1 for i in range(m)]
    counts = []
    for v in stages:
        bit=1<<v
        new=[]
        for s in active:
            if s&bit: continue
            t=s|bit
            if t in active:
                new.append((s,t))
        for s,t in new:
            assert s in active and t in active
            active.remove(s);active.remove(t)
            assert s.bit_count()+1 == t.bit_count()
            pairs[s]=t
        counts.append(len(new))
    expected={1}
    for I in combinations(range(m),k-1):
        s=0
        for i in I:
            s |= (1<<(3*i+2)) | (1<<(3*i+3))
        expected.add(s)
    assert active==expected,(m,k,active^expected)
    assert len(F)==2*len(pairs)+len(expected)
    return pairs,expected,counts


def check_acyclic(F,pairs):
    indegree={f:0 for f in F}
    adj={f:[] for f in F}
    edges=0
    for upper in F:
        x=upper
        while x:
            v=x&-x;x-=v
            lower=upper^v
            if lower not in F:continue
            edges+=1
            if pairs.get(lower)==upper:
                adj[lower].append(upper)
                indegree[upper]+=1
            else:
                adj[upper].append(lower)
                indegree[lower]+=1
    q=deque(f for f in F if indegree[f]==0)
    visited=0
    while q:
        f=q.popleft();visited+=1
        for w in adj[f]:
            indegree[w]-=1
            if indegree[w]==0:q.append(w)
    assert visited==len(F),(visited,len(F))
    return edges


def direct_small_check(m,k,F,adj):
    n=len(adj)
    for s in range(1,1<<n):
        forbidden=False
        vv=[i for i in range(n) if s>>i&1]
        for choice in combinations(vv,k):
            if all(not (adj[i]>>j&1) for i,j in combinations(choice,2)):
                forbidden=True;break
        assert (s in F) != forbidden,(m,k,s)


def verify():
    checked=0
    for m in range(1,7):
        for k in range(2,7):
            n,adj,F=compute_faces(m,k)
            if m<=3 and k<=5:direct_small_check(m,k,F,adj)
            P,C,stages=morse_matching(m,k,F)
            covers=check_acyclic(F,P)
            crit=Counter(s.bit_count()-1 for s in C)
            want={0:1}
            if comb(m,k-1):want[2*k-3]=comb(m,k-1)
            assert dict(crit)==want,(m,k,crit,want)
            print('OK m=%d k=%d vertices=%d faces=%d pairs=%d covers=%d critical=%s'%(m,k,n,len(F),len(P),covers,dict(crit)),flush=True)
            checked+=1
    print('ALL_VERIFY_OK %d parameter pairs; complete face-poset acyclicity'%checked)

if __name__=='__main__':verify()
