#!/usr/bin/env python3
"""Construct and check a cubic-tree indexed family of block graphs.
Standard library only. Run: python verify.py
"""
from collections import Counter, deque


def canon_tree(adj):
    n=len(adj)
    degree=[len(x) for x in adj]
    leaves=deque(i for i,d in enumerate(degree) if d<=1)
    rest=n
    while rest>2:
        k=len(leaves)
        rest-=k
        for _ in range(k):
            v=leaves.popleft()
            for w in adj[v]:
                degree[w]-=1
                if degree[w]==1:
                    leaves.append(w)
    def rooted(v,p):
        return '('+''.join(sorted(rooted(w,v) for w in adj[v] if w!=p))+')'
    return min(rooted(c,-1) for c in leaves)


def all_trees(n):
    trees=[(set(),)]
    for k in range(2,n+1):
        seen={}
        for T in trees:
            for v in range(k-1):
                S=[set(x) for x in T]+[{v}]
                S[v].add(k-1)
                key=canon_tree(S)
                if key not in seen:
                    seen[key]=tuple(S)
        trees=list(seen.values())
    return trees


def expanded(T):
    N=len(T)
    assert all(len(T[v]) in (1,3) for v in range(N))
    H=[set() for _ in range(4*N)]
    def edge(u,v):
        assert v not in H[u]
        H[u].add(v); H[v].add(u)
    available={v:list(range(N+3*v,N+3*v+3)) for v in range(N)}
    for v in range(N):
        for s in available[v]: edge(v,s)
    for u in range(N):
        for v in sorted(w for w in T[u] if w>u):
            edge(available[u].pop(),available[v].pop())
    for v in range(N):
        if len(T[v])==1:
            a,b=available[v]
            edge(a,b)
        else:
            assert not available[v]
    return H


def extracted_tree(H):
    N=len(H)//4
    assert len(H)==4*N
    C=[v for v in range(len(H)) if len(H[v])==3]
    S=[v for v in range(len(H)) if len(H[v])==2]
    assert len(C)==N and len(S)==3*N
    recovered=[set() for _ in C]
    idx={c:i for i,c in enumerate(C)}
    for s in S:
        c=[v for v in H[s] if v in idx]
        t=[v for v in H[s] if v not in idx]
        assert len(c)==len(t)==1
        other=[v for v in H[t[0]] if v in idx]
        assert len(other)==1
        if other[0]!=c[0]:
            recovered[idx[c[0]]].add(idx[other[0]])
    assert sum(map(len,recovered))==2*(N-1)
    return recovered


def block_check(H):
    # Tarjan edge-block decomposition; confirms all maximal blocks are K2 or K3.
    t=0;disc={};low={};stk=[];blocks=[]
    def visit(v,p):
        nonlocal t
        disc[v]=low[v]=t; t+=1
        for w in H[v]:
            if w==p:continue
            if w not in disc:
                stk.append((v,w));visit(w,v)
                low[v]=min(low[v],low[w])
                if low[w]>=disc[v]:
                    B=set()
                    while True:
                        e=stk.pop();B.update(e)
                        if e==(v,w):break
                    blocks.append(B)
            elif disc[w]<disc[v]:
                low[v]=min(low[v],disc[w]);stk.append((v,w))
    visit(0,-1)
    assert len(disc)==len(H) and not stk
    assert all(len(B) in (2,3) and all((b in H[a]) for a in B for b in B if a!=b) for B in blocks)
    return Counter(len(B) for B in blocks)


def refine_pair(A,B):
    H=[set(x) for x in A]+[{len(A)+v for v in x} for x in B]
    color=[0]*len(H)
    palette=[]
    for t in range(5):
        descriptors=[(color[v],tuple(sorted(Counter(color[w] for w in H[v]).items()))) for v in range(len(H))]
        ordered={k:i for i,k in enumerate(sorted(set(descriptors)))}
        new=[ordered[k] for k in descriptors]
        palette.append((Counter(new[:len(A)]),Counter(new[len(A):])))
        if t>=2: assert len(set(new))==2
        color=new
    return palette


def verify():
    ntypes={}
    families={}
    for I in range(0,9):
        subcubic=[]
        internal_trees=all_trees(I) if I else [None]
        for T in internal_trees:
            if T is None:
                subcubic.append([{1},{0}]);continue
            if max(map(len,T))<=3:
                full=[set(x) for x in T]
                for v in range(I):
                    for _ in range(3-len(T[v])):
                        new=len(full);full[v].add(new);full.append({v})
                assert len(full)==2*I+2
                subcubic.append(full)
        ntypes[I]=len(subcubic)
        families[I]=[]
        for T in subcubic:
            H=expanded(T)
            assert canon_tree(extracted_tree(H))==canon_tree(T)
            assert all(len(H[c])==3 for c in range(len(T)))
            assert all(len(H[s])==2 for s in range(len(T),len(H)))
            sizes=block_check(H)
            assert sizes[3]==I+2 and sizes[2]==3*(len(T)-1)
            families[I].append(H)
        for a in range(len(families[I])):
            for b in range(a+1,len(families[I])):
                pa=refine_pair(families[I][a],families[I][b])
                assert all(x==y for x,y in pa)
                assert canon_tree(extracted_tree(families[I][a]))!=canon_tree(extracted_tree(families[I][b]))
        print('internal',I,'nonisomorphic_images',ntypes[I], 'vertices',8*I+8)
    assert [ntypes[i] for i in range(0,5)]==[1,1,1,1,2]
    # For each I>=4, a path and an internal branching tree are distinct.
    for I in range(4,30):
        P=[set() for _ in range(I)]
        for j in range(I-1):P[j].add(j+1);P[j+1].add(j)
        Q=[set() for _ in range(I)]
        for j in range(I-2):Q[j].add(j+1);Q[j+1].add(j)
        Q[1].add(I-1);Q[I-1].add(1)
        def fill(X):
            R=[set(z) for z in X]
            for j in range(len(X)):
                for _ in range(3-len(X[j])):
                    k=len(R);R[j].add(k);R.append({j})
            return R
        A,B=expanded(fill(P)),expanded(fill(Q))
        assert canon_tree(extracted_tree(A))!=canon_tree(extracted_tree(B))
        assert all(x==y for x,y in refine_pair(A,B))
    print('VERIFY_OK first_internal_collision=4 first_graph_order=40 infinite_pairs_4_to_29=True')

if __name__=='__main__':verify()
