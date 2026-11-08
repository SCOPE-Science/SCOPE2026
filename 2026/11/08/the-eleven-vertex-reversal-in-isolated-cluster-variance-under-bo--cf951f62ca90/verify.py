#!/usr/bin/env python3
"""Exact, dependency-free finite tree enumeration and percolation variance checker."""
from fractions import Fraction as Q
from itertools import product
from heapq import heappush, heappop
from collections import deque

COUNTS = (0,1,1,1,2,3,6,11,23,47,106,235)

def adjacency(edges,n):
    out=[set() for _ in range(n)]
    for u,v in edges:
        out[u].add(v);out[v].add(u)
    return out

def canonical(edges,n):
    """Unrooted-tree AHU code: centers obtained by simultaneous leaf peeling."""
    adj=adjacency(edges,n)
    if n==1:return '()'
    degree=[len(a) for a in adj]
    fringe=[i for i,d in enumerate(degree) if d<=1]
    remaining=n
    while remaining>2:
        remaining-=len(fringe)
        new=[]
        for v in fringe:
            for w in adj[v]:
                degree[w]-=1
                if degree[w]==1:new.append(w)
            degree[v]=0
        fringe=new
    def rooted(v,parent):
        return '('+''.join(sorted(rooted(w,v) for w in adj[v] if w!=parent))+')'
    if remaining==1:return rooted(fringe[0],-1)
    a,b=fringe
    return '('+''.join(sorted((rooted(a,b),rooted(b,a))))+')'

def unique_trees(max_n):
    trees={canonical((),1):((),1)}
    yield 1,trees
    for n in range(2,max_n+1):
        nxt={}
        for edges,_ in trees.values():
            for v in range(n-1):
                ne=edges+((v,n-1),)
                c=canonical(ne,n)
                if c not in nxt:nxt[c]=(ne,n)
        trees=nxt
        yield n,trees

def variance(edges,n):
    d=[0]*n
    for u,v in edges:d[u]+=1;d[v]+=1
    return sum((Q(1,2**k)-Q(1,4**k) for k in d),Q(0))+sum((Q(1,2**(d[u]+d[v]-1)) for u,v in edges),Q(0))

def star(n):return tuple((0,v) for v in range(1,n))
def double_star(a,b):
    # central labels 0 and 1, with a-1 leaves at center 0, b-1 at center 1
    return ((0,1),)+tuple((0,v) for v in range(2,a+1))+tuple((1,v) for v in range(a+1,a+b))

def direct_variance(edges,n):
    # enumerate all 2^(n-1) retention outcomes, independently of covariance formula
    vals=[]
    for s in range(1<<len(edges)):
        deg=[0]*n
        for j,(u,v) in enumerate(edges):
            if (s>>j)&1:deg[u]+=1;deg[v]+=1
        vals.append(sum(k==0 for k in deg))
    ex=Q(sum(vals),len(vals))
    return Q(sum(v*v for v in vals),len(vals))-ex*ex

def star_formula(n):
    return Q(n-1,4)+Q(n,2**(n-1))-Q(1,4**(n-1))

def ds_formula(a,b):
    n=a+b
    return Q(n-2,4)+Q(a,2**a)+Q(b,2**b)-Q(1,4**a)-Q(1,4**b)+Q(1,2**(n-1))

def prufer_to_tree(seq,n):
    # Independent Cayley-code tree generator; exhaustive in ordered Prüfer words.
    degrees=[1]*n
    for k in seq:degrees[k]+=1
    heap=[]
    for v,d in enumerate(degrees):
        if d==1:heappush(heap,v)
    edges=[]
    for k in seq:
        v=heappop(heap)
        edges.append((v,k))
        degrees[v]-=1;degrees[k]-=1
        if degrees[k]==1:heappush(heap,k)
    a,b=heap
    edges.append((a,b))
    return tuple(edges)

count=0
for n,trees in unique_trees(11):
    assert len(trees)==COUNTS[n], (n,len(trees),COUNTS[n])
    count+=1
    values={key:variance(edges,n) for key,(edges,_) in trees.items()}
    vmin=min(values.values()); optimizers=[key for key,v in values.items() if v==vmin]
    assert len(optimizers)==1, (n,len(optimizers))
    if n<=10:
        assert optimizers==[canonical(star(n),n)], ('star',n)
        assert vmin==star_formula(n)
    else:
        assert optimizers==[canonical(double_star(5,6),n)], ('double-star',n)
        assert vmin==ds_formula(5,6)==Q(10239,4096)
        assert star_formula(n)-vmin==Q(11519,1048576)
    for edges,_ in trees.values():
        count+=1
        if n<=7:
            assert direct_variance(edges,n)==variance(edges,n), ('enumeration',n,edges)
            count+=1
    print('n',n,'shapes',len(trees),'min',vmin,'unique', True)

# Prüfer words independently cover every labeled tree through order seven.
for n in range(3,8):
    known={canonical(edges,n) for edges,_ in next(t for k,t in unique_trees(n) if k==n).values()}
    observed=set()
    low=None
    for word in product(range(n),repeat=n-2):
        edges=prufer_to_tree(word,n)
        observed.add(canonical(edges,n))
        v=variance(edges,n)
        low=v if low is None or v<low else low
        count+=1
    assert observed==known
    assert low==star_formula(n)
    count+=2

for n in range(11,101):
    a=n//2;b=n-a
    assert ds_formula(a,b)<star_formula(n)
    assert Q(a,2**a)+Q(b,2**b)<=Q(1,4)
    count+=2
print('VERIFY_OK',count,'exact assertions / checks')
