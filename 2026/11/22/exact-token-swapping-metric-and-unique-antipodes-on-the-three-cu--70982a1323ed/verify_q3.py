#!/usr/bin/env python3
"""Exhaustive, standalone verification of optimal sequential token swapping on Q3.
Python 3.9+; no external dependencies. Vertex labels are integers 0,...,7
written as three-bit words; placement[p] is the token on vertex p.
"""
from collections import Counter, deque
from itertools import permutations
from math import factorial
import json

N=8
EDGES=tuple((u,v) for u in range(N) for v in range(u+1,N)
            if (u^v).bit_count()==1)
HIST=(1,12,90,476,1903,5472,10388,11756,7347,2408,430,36,1)
EXCESS=(19064,18088,3144,24)
ROOT=tuple(range(N))


def next_placements(p):
    for a,b in EDGES:
        q=list(p)
        q[a],q[b]=q[b],q[a]
        yield tuple(q)


def bfs_dictionary():
    depths={ROOT:0}
    queue=deque([ROOT])
    while queue:
        p=queue.popleft()
        for q in next_placements(p):
            if q not in depths:
                depths[q]=depths[p]+1
                queue.append(q)
    return depths


def cantor_rank(p):
    rank=0
    unused=list(range(N))
    for v in p:
        a=unused.index(v)
        rank+=a*factorial(len(unused)-1)
        unused.pop(a)
    return rank


def cantor_unrank(j):
    unused=list(range(N))
    out=[]
    for k in range(N-1,-1,-1):
        f=factorial(k)
        a,j=divmod(j,f)
        out.append(unused.pop(a))
    assert j==0
    return tuple(out)


def bfs_rank_array():
    depth=[-1]*factorial(N)
    depth[0]=0
    queue=deque([0])
    while queue:
        r=queue.popleft()
        p=cantor_unrank(r)
        for q in next_placements(p):
            s=cantor_rank(q)
            if depth[s]==-1:
                depth[s]=depth[r]+1
                queue.append(s)
    return depth


def main():
    assert len(EDGES)==12
    assert all((a^b).bit_count()==1 for a,b in EDGES)
    assert cantor_rank(ROOT)==0
    # Round-trip indexing independent of BFS route generation.
    for i,p in enumerate(permutations(range(N))):
        assert cantor_rank(p)==i
        assert cantor_unrank(i)==p
    d=bfs_dictionary()
    a=bfs_rank_array()
    assert len(d)==factorial(N)==len(a)
    assert all(x>=0 for x in a)
    assert all(a[cantor_rank(p)]==v for p,v in d.items())
    hist=Counter(d.values())
    assert tuple(hist[i] for i in range(max(hist)+1))==HIST
    assert max(hist)==12
    far=[p for p,v in d.items() if v==12]
    assert far==[tuple(i^7 for i in range(N))]
    # Every swap changes the sum of Hamming travel distances by at most 2.
    # Cube is bipartite, so the sum is even and half is an integer.
    excess=Counter()
    for p,v in d.items():
        l=sum((pos^tok).bit_count() for pos,tok in enumerate(p))
        assert l%2==0
        assert v>=l//2
        excess[v-l//2]+=1
        assert all((pos^tok).bit_count()<=3 for pos,tok in enumerate(p))
    assert tuple(excess[i] for i in range(max(excess)+1))==EXCESS
    assert sum(HIST)==sum(EXCESS)==factorial(N)
    # Every source has the same spectrum by relabelling token identities.
    # For any p, the map q -> p o q carries the identity to p and preserves
    # every position swap; its inverse is relabelling by p^{-1}.
    for p in (ROOT,tuple(range(N-1,-1,-1)),(1,3,0,7,2,5,4,6)):
        image={tuple(p[t] for t in q) for q in d}
        assert len(image)==factorial(N)
        for u,v in EDGES:
            lhs=tuple(p[t] for t in next_swap(ROOT,u,v))
            rhs=next_swap(p,u,v)
            assert lhs==rhs
    output={
        'base_graph':'Q3',
        'labelled_vertices':list(range(N)),
        'edges':[list(e) for e in EDGES],
        'permutations_visited':len(d),
        'bfs_crosscheck':'tuple-dictionary equals independent Cantor-rank-array BFS at all 40320 states',
        'distance_histogram':list(HIST),
        'diameter':max(d.values()),
        'number_of_diameter_targets_per_start':len(far),
        'diameter_target_from_identity':list(far[0]),
        'unordered_diameter_pairs':factorial(N)//2,
        'distance_minus_travel_lower_bound_histogram':list(EXCESS),
        'maximum_excess':max(excess),
        'maximum_excess_placements':excess[max(excess)],
    }
    print(json.dumps(output,ensure_ascii=False,sort_keys=True,indent=2))


def next_swap(p,u,v):
    q=list(p);q[u],q[v]=q[v],q[u]
    return tuple(q)

if __name__=='__main__':
    main()
