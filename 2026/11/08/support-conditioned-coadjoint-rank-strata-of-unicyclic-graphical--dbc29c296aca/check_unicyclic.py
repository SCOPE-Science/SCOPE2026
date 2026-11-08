#!/usr/bin/env python3
"""Independent finite-field rank enumeration for the unicyclic weighted-skew formula."""
from itertools import product
from collections import Counter
from functools import lru_cache

@lru_cache(None)
def matching(vertices, edges):
    if not edges: return 0
    e=edges[0]; a,b=e
    rest=tuple(x for x in edges if a not in x and b not in x)
    return max(matching(vertices,edges[1:]),1+matching(vertices,rest))

def survivor(n, es):
    edges=set(es); vv=set(range(n)); picks=0
    while True:
        degree={v:0 for v in vv}
        for u,v in edges: degree[u]+=1;degree[v]+=1
        leaf=next((v for v in sorted(vv) if degree[v]==1),None)
        if leaf is None: break
        nbr=next((v if u==leaf else u) for u,v in sorted(edges) if leaf in (u,v))
        vv.difference_update((leaf,nbr)); edges={e for e in edges if leaf not in e and nbr not in e}
        picks+=1
    return picks, len(edges)>0, edges, vv

def formula(n,edges,q):
    M=len(edges); counts=Counter()
    # only a graph with one cycle; disjoint support can have no cycle
    for mask in range(1<<M):
        es=tuple(edges[i] for i in range(M) if (mask>>i)&1)
        size=len(es); mx=matching(tuple(range(n)),es)
        picks,cycle,_,_=survivor(n,es)
        assert mx>=picks
        total=(q-1)**size
        if cycle:
            # any surviving cycle is the original cycle; only even-cycle correction
            cycle_len=len(survivor(n,es)[2]); assert cycle_len>=3
            if cycle_len%2==0:
                exc=(q-1)**(size-1)
                counts[2*mx-2]+=exc
                total-=exc
        counts[2*mx]+=total
    return counts

def matrixrank(n,es,vals,q):
    a=[[0]*n for _ in range(n)]
    if q==4:
        # GF4 = F2[t]/(t^2+t+1)
        mul=lambda x,y: ((x&1)*(y&1)) ^ (((x&1)*((y>>1)&1) ^ ((x>>1)&1)*(y&1) ^ ((x>>1)&1)*((y>>1)&1))<<1) ^ ((x>>1)&1)*((y>>1)&1)
        add=lambda x,y:x^y
        inv={1:1,2:3,3:2}
        neg=lambda x:x
    else:
        mul=lambda x,y:x*y%q
        add=lambda x,y:(x+y)%q
        inv={x:pow(x,-1,q) for x in range(1,q)}
        neg=lambda x:(-x)%q
    for (u,v),w in zip(es,vals):
        a[u][v]=w; a[v][u]=neg(w)
    rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,n) if a[i][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        scale=inv[a[rank][col]]
        a[rank]=[mul(x,scale) for x in a[rank]]
        for row in range(rank+1,n):
            v=a[row][col]
            if v:a[row]=[add(x,neg(mul(v,y))) for x,y in zip(a[row],a[rank])]
        rank+=1
    return rank

def sample_graphs():
    # Families with odd/even unique cycles, pendant paths and branching.
    raw=[]
    for k in (3,4,5,6):
        base=[(i,i+1) for i in range(k-1)]+[(0,k-1)]
        raw.append((k,base))
        if k<=5:
            raw.append((k+1,base+[(0,k)]))
        if k<=4:
            raw.append((k+2,base+[(0,k),(k,k+1)]))
            raw.append((k+2,base+[(0,k),(0,k+1)]))
            raw.append((k+2,base+[(0,k),(1,k+1)]))
    return raw

def main():
    tests=0;checked=0
    for n,edges in sample_graphs():
        edges=tuple(sorted(tuple(sorted(e)) for e in edges))
        assert len(edges)==n
        for q in (2,3,4,5):
            if q**len(edges)>25000: continue
            expected=formula(n,edges,q)
            actual=Counter()
            for vals in product(range(q),repeat=len(edges)):
                actual[matrixrank(n,edges,vals,q)]+=1
            assert expected==actual,(n,edges,q,expected,actual)
            tests+=1;checked+=q**len(edges)
    print(f'UNICYCLE_WEIGHTED_RANK_PASS graphs={len(sample_graphs())} field_cases={tests} matrices={checked}')
    # independent high-q Monte Carlo stress testing full 7/8-vertex graph
    import random
    rng=random.Random(340931)
    large=[(8,[(0,1),(1,2),(2,3),(3,0),(0,4),(4,5),(2,6),(6,7)]),
           (8,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(0,6),(6,7)])]
    for n,ee in large:
        ee=tuple(sorted(tuple(sorted(e)) for e in ee))
        for q in (3,5):
            for j in range(300):
                vals=[rng.randrange(q) for _ in ee]
                r=matrixrank(n,ee,vals,q)
                sup=tuple(e for e,w in zip(ee,vals) if w)
                mx=matching(tuple(range(n)),sup)
                if r<2*mx:
                    _,cycle,_,_=survivor(n,sup)
                    assert cycle and r==2*mx-2
    print('UNICYCLE_WEIGHTED_RANK_RANDOM_PASS samples=1200')
if __name__=='__main__':main()
