#!/usr/bin/env python3
"""Recompute the scale-two subdivision-graph decomposition using standard Python.

This tests a finite census; the all-graphs theorem has a separate symbolic proof.
"""
from itertools import combinations
from collections import deque


def graph(n, edges):
    ed = {tuple(sorted(e)) for e in edges}
    assert all(0 <= a < b < n for a,b in ed)
    return n, ed


def sd(g):
    n,ed=g
    es=sorted(ed)
    return n+len(es), {tuple(sorted((v,n+i))) for i,(a,b) in enumerate(es) for v in (a,b)},es


def square(n, edges):
    adj = [set() for i in range(n)]
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    edges2=set()
    for v in range(n):
        near=set(adj[v]);
        for u in adj[v]: near|=adj[u]
        near.discard(v)
        for w in near: edges2.add(tuple(sorted((v,w))))
    return n,edges2


def cliques(n,edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    faces={()}
    for v in range(n):
        additions={tuple(sorted(s+(v,))) for s in faces if all(u in adj[v] for u in s)}
        faces|=additions
    return faces


def add_simplex(f, s):
    s=tuple(sorted(s))
    for d in range(len(s)+1):
        for ss in combinations(s,d):f.add(ss)


def model(g):
    n,ed=g; N,e2,es=sd(g)
    K=cliques(*square(N,e2))
    X=cliques(n,ed)
    A=set(X)
    for v in range(n):
        E=[n+i for i,(u,w) in enumerate(es) if v in (u,w)]
        add_simplex(A,[v]+E)
    for i,(u,v) in enumerate(es):add_simplex(A,(u,v,n+i))
    triangles={s for s in combinations(range(n),3) if all(tuple(sorted(e)) in ed for e in combinations(s,2))}
    byedge={e:n+i for i,e in enumerate(es)}
    midtriangles={tuple(sorted((byedge[(a,b)],byedge[(a,c)],byedge[(b,c)]))) for a,b,c in triangles}
    return K,X,A,midtriangles,triangles,es


def collapse_model(g,A,X,es):
    n,_=g; A=set(A);steps=0
    def rm(f,coface):
        nonlocal steps
        assert f in A and coface in A and len(coface)==len(f)+1 and set(f).issubset(coface), (f,coface)
        assert sum(set(f).issubset(s) for s in A)==2, (f,coface)
        A.remove(f);A.remove(coface);steps+=1
    for v in range(n):
        incident=sorted(n+i for i,e in enumerate(es) if v in e)
        for d in range(len(incident),1,-1):
            for sigma in combinations(incident,d):
                rm(sigma,tuple(sorted((v,)+sigma)))
    for i,(u,v) in enumerate(es):
        m=n+i
        rm(tuple(sorted((u,m))),tuple(sorted((u,v,m))))
        rm((m,),tuple(sorted((v,m))))
    assert A==X, (len(A),len(X),A^X)
    return steps


def betti(faces):
    bydim={}
    for s in faces:
        if s:bydim.setdefault(len(s)-1,[]).append(s)
    for arr in bydim.values():arr.sort()
    rk={};maxdim=max(bydim,default=-1)
    for d in range(1,maxdim+1):
        idx={s:i for i,s in enumerate(bydim[d-1])};base={}
        for s in bydim.get(d,[]):
            word=0
            for j in range(len(s)):word ^= 1<<idx[s[:j]+s[j+1:]]
            while word:
                p=word.bit_length()-1
                if p in base:word^=base[p]
                else:base[p]=word;break
        rk[d]=len(base)
    return {d:len(bydim.get(d,[]))-rk.get(d,0)-rk.get(d+1,0) for d in range(maxdim+1)}


def check(g,deep=True):
    K,X,A,T,tris,es=model(g)
    assert A.issubset(K)
    assert K-A==T, (K-A,T)
    assert all(len(t)==3 for t in T)
    assert len(T)==len(tris)
    c=collapse_model(g,A,X,es) if deep else None
    b=betti(K);bx=betti(X)
    expected={d:bx.get(d,0)+(len(T) if d==2 else 0) for d in range(max(max(b,default=0),max(bx,default=0),2)+1)}
    assert all(b.get(d,0)==expected.get(d,0) for d in set(b)|set(expected)),(g,b,bx,len(T))
    return c,len(K),len(T)


def all_graphs(n):
    E=list(combinations(range(n),2))
    for mask in range(1<<len(E)):
        yield graph(n,(E[j] for j in range(len(E)) if mask>>j&1))


def named():
    yield 'house',graph(5,[(0,1),(1,2),(2,3),(3,0),(2,4),(3,4)])
    yield 'octahedral',graph(6,((i,j) for i in range(6) for j in range(i+1,6) if i//2!=j//2))
    yield 'K6',graph(6,combinations(range(6),2))
    yield 'K3,3',graph(6,((i,j) for i in range(3) for j in range(3,6)))
    yield 'triangulated_hexagon',graph(6,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(0,2),(0,3),(0,4)])
    yield 'Petersen',graph(10,[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(i+5,((i+2)%5)+5) for i in range(5)])

if __name__=='__main__':
    cnt=0
    for n in range(1,6):
        for G in all_graphs(n):
            check(G,deep=True);cnt+=1
        print('ALL_GRAPHS_MOD2_OK',n,'graphs',1<<(n*(n-1)//2))
    for name,G in named():
        steps,faces,t=check(G,deep=True)
        print('NAMED_OK',name,'faces',faces,'triangles',t,'elementary_pairs_to_clique_complex',steps)
    print('SUBDIVISION_RIPS2_EXHAUSTIVE_SMALL_AND_NAMED_OK',cnt,'graphs')
