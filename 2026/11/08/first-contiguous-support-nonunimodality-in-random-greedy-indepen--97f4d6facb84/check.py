"""Exact exhaustive certificate for the first gap-free nonunimodal random greedy independent-set law."""
from itertools import product, permutations
from collections import Counter
from fractions import Fraction
import heapq

def prufer_edges(code,n):
    degree=[1]*n
    for x in code: degree[x]+=1
    free=[v for v in range(n) if degree[v]==1]
    heapq.heapify(free)
    edges=[]
    for x in code:
        u=heapq.heappop(free)
        edges.append((u,x))
        degree[u]-=1; degree[x]-=1
        if degree[x]==1: heapq.heappush(free,x)
    assert len(free)==2
    edges.append(tuple(sorted(free)))
    return edges

def adj_masks(edges,n):
    adj=[0]*n
    for u,v in edges:
        adj[u]|=1<<v;adj[v]|=1<<u
    return tuple(adj)

def distribution_by_order(adj,orders):
    counts=[0]*(len(adj)+1)
    for order in orders:
        picked=0
        for v in order:
            if not (adj[v] & picked):picked|=1<<v
        counts[picked.bit_count()]+=1
    return tuple(counts)

def gap_free_nonunimodal(counts):
    positive=[i for i,c in enumerate(counts) if c]
    if len(positive)!=positive[-1]-positive[0]+1:return False
    vals=[counts[i] for i in positive]
    return not any(all(vals[i]<=vals[i+1] for i in range(k)) and all(vals[i]>=vals[i+1] for i in range(k,len(vals)-1)) for k in range(len(vals)))

def spider_113(edges,n):
    if n!=6:return False
    adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    deg=[len(a) for a in adj]
    if sorted(deg)!=[1,1,1,2,2,3]:return False
    center=deg.index(3)
    arms=[]
    for v in adj[center]:
        prev=center;cur=v;length=1
        while len(adj[cur])==2:
            next_v=next(w for w in adj[cur] if w!=prev)
            prev,cur=cur,next_v;length+=1
        arms.append(length)
    return sorted(arms)==[1,1,3]

def exhaustive():
    for n in range(1,7):
        orders=list(permutations(range(n)))
        codes=[()] if n==1 else product(range(n),repeat=n-2)
        nonunimodal=0;witness=[];types=Counter();labeled=0
        for code in codes:
            edges=[] if n==1 else prufer_edges(code,n)
            counts=distribution_by_order(adj_masks(edges,n),orders)
            labeled+=1
            if gap_free_nonunimodal(counts):
                nonunimodal+=1
                assert spider_113(edges,n),(n,edges,counts)
                assert counts==(0,0,190,160,370,0,0),(n,edges,counts)
                if len(witness)<1:witness.append(edges)
            if n==6:types[tuple(i for i,c in enumerate(counts) if c)]+=1
        expected=n**(n-2) if n>=2 else 1
        assert labeled==expected
        assert nonunimodal==(360 if n==6 else 0),(n,nonunimodal)
        print('n',n,'labeled trees',labeled,'nonunimodal gap-free',nonunimodal,'witness',witness)
        if n==6:print('n6 size-support census',sorted(types.items()))
    edges=[(1,0),(1,2),(1,3),(0,4),(4,5)]
    counts=distribution_by_order(adj_masks(edges,6),list(permutations(range(6))))
    assert counts==(0,0,190,160,370,0,0)
    print('canonical S(1,1,3) distribution',tuple(Fraction(x,720) for x in counts))
    print('CERTIFICATE PASSED')

if __name__=='__main__':exhaustive()
