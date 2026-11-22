#!/usr/bin/env python3
"""Checks for an exact binary-window covering theorem (stdlib only)."""
from itertools import combinations
from math import comb
from collections import defaultdict, Counter, deque

def rotate(v,n):
    mask=(1<<n)-1
    return ((v<<1)&mask)|(v>>(n-1))

def rotations(v,n):
    r=[]; x=v
    while x not in r:
        r.append(x);x=rotate(x,n)
    return tuple(r)

def orbits(n,k):
    unseen={x for x in range(1<<n) if x.bit_count()==k}
    out=[]
    while unseen:
        o=rotations(min(unseen),n)
        assert set(o)<=unseen
        unseen-=set(o);out.append(o)
    return out

def all_edges(n):
    required={x for x in range(1<<n) if x.bit_count()==3}
    optional={x for x in range(1<<n) if x.bit_count()==2 and len([i for i in range(n) if x>>i&1 and i%2==0]) in (0,2)}
    return required,optional

def components(n,edges):
    mask=(1<<(n-1))-1
    adj=defaultdict(set); indeg=Counter(); outdeg=Counter()
    for x in edges:
        a=x>>1;b=x&mask
        adj[a].add(b);adj[b].add(a);outdeg[a]+=1;indeg[b]+=1
    active=set(indeg)|set(outdeg)
    assert all(indeg[v]==outdeg[v] for v in active)
    count=0
    while active:
        count+=1;start=next(iter(active));stack=[start];active.remove(start)
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if v in active:active.remove(v);stack.append(v)
    return count

def tour(n,edges):
    mask=(1<<(n-1))-1; adj=defaultdict(list)
    for x in sorted(edges,reverse=True):adj[x>>1].append((x&mask,x&1))
    root=min(adj);stack=[(root,None)]; bits=[]
    while stack:
        v,_=stack[-1]
        if adj[v]:
            v2,b=adj[v].pop();stack.append((v2,b))
        else:
            _,b=stack.pop()
            if b is not None:bits.append(b)
    bits=bits[::-1]
    assert len(bits)==len(edges)
    circle=''.join(map(str,bits))
    obs=Counter(int(''.join(circle[(i+j)%len(circle)] for j in range(n)),2) for i in range(len(circle)))
    assert obs==Counter(edges)
    return circle

def triples_hit(n,selected):
    pairs={frozenset(i for i in range(n) if x>>i&1) for o in selected for x in o}
    return all(any(frozenset(p)<=set(t) for p in pairs) for t in combinations(range(n),3))

def verify(n):
    req,canon=all_edges(n)
    opts=orbits(n,2)
    orbit_options=len(opts)
    best=10**9; minimizers=0; minsets=[]
    for bits in range(1<<len(opts)):
        chosen=[opts[i] for i in range(len(opts)) if (bits>>i)&1]
        extras={v for o in chosen for v in o}
        if len(req)+len(extras)<len(req)+best and not triples_hit(n,chosen):
            continue
        if components(n,req|extras)==1:
            size=len(extras)
            if size<best:
                best=size;minimizers=1;minsets=[extras]
            elif size==best:
                minimizers+=1;minsets.append(extras)
    assert best==n*(n-2)//4,(n,best)
    assert minimizers==1,(n,minimizers)
    assert minsets[0]==canon
    assert components(n,req|canon)==1
    witness=tour(n,req|canon)
    print(f'n={n} wt3={len(req)} wt2_added={len(canon)} min_extra={best} unique_min_set={minimizers} orbit_choices={1<<orbit_options} length={len(witness)}')
    if n==6:print('n=6 witness:',witness)

if __name__=='__main__':
    for n in (6,8,10,12,14):verify(n)
    print('ALL_CHECKS_PASSED')
