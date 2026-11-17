#!/usr/bin/env python3
"""Independent finite checks for minimal connected dominating sets in S(K_n)."""
from itertools import combinations, product
from collections import Counter

def graph(n):
    pairs=list(combinations(range(n),2))
    adj=[0]*(n+len(pairs))
    for j,(a,b) in enumerate(pairs,n):
        adj[a]|=1<<j; adj[b]|=1<<j
        adj[j]=(1<<a)|(1<<b)
    return adj,pairs

def connected_dominating(mask,adj):
    if not mask: return False
    covered=mask
    for i in range(len(adj)):
        if (mask>>i)&1: covered|=adj[i]
    if covered!=(1<<len(adj))-1: return False
    seen=mask&-mask
    while True:
        new=seen
        for i in range(len(adj)):
            if (seen>>i)&1:new|=adj[i]&mask
        if new==seen:break
        seen=new
    return seen==mask

def prufer_edges(vertices, seq):
    deg={v:1 for v in vertices}
    for v in seq: deg[v]+=1
    edges=[]
    for v in seq:
        leaf=min(x for x in vertices if deg[x]==1)
        edges.append(tuple(sorted((leaf,v))))
        deg[leaf]-=1;deg[v]-=1
    a,b=[x for x in vertices if deg[x]==1]
    edges.append(tuple(sorted((a,b))))
    return edges

def predicted(n,pairs):
    lookup={e:n+k for k,e in enumerate(pairs)}
    out=set()
    for omitted in range(n):
        verts=tuple(v for v in range(n) if v!=omitted)
        for word in product(verts,repeat=n-3):
            spanning=prufer_edges(verts,word)
            tree_mask=sum(1<<lookup[e] for e in spanning)
            old_mask=sum(1<<v for v in verts)
            for witness in verts:
                edge=tuple(sorted((omitted,witness)))
                out.add(old_mask | tree_mask | (1<<lookup[edge]))
    return out

def run():
    results=[]
    masks=0
    for n in (3,4,5,6):
        adj,pairs=graph(n)
        want=predicted(n,pairs)
        have=set()
        N=len(adj)
        for mask in range(1,1<<N):
            masks+=1
            if connected_dominating(mask,adj):
                if all(not connected_dominating(mask^(1<<i),adj) for i in range(N) if mask>>i&1):
                    have.add(mask)
        if have!=want:
            miss=list(want-have)[:5]; extras=list(have-want)[:5]
            raise AssertionError(f'n={n}: missing {miss}, extra {extras}')
        assert len(want)==n*(n-1)**(n-2)
        assert {x.bit_count() for x in want}=={2*n-2}
        results.append((n,N,len(have)))
    # For n=7, construct all predicted sets and directly check definition and minimality.
    adj,pairs=graph(7)
    want=predicted(7,pairs)
    assert len(want)==7*6**5
    for mask in want:
        assert connected_dominating(mask,adj)
        assert all(not connected_dominating(mask^(1<<i),adj) for i in range(len(adj)) if mask>>i&1)
    print('VERIFY_OK exhaustive_n=3..6 checked_nonempty_subsets='+str(masks)+
        ' minimal_counts='+','.join(f'{n}:{c}' for n,N,c in results)+
        ' generated_n7='+str(len(want))+' membership=PASS minimality=PASS formula=PASS')
if __name__=='__main__': run()
