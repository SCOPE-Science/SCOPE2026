"""Exhaust all acyclic directed multigraphs with up to nine edges and five vertices."""
from itertools import combinations_with_replacement
from functools import lru_cache

@lru_cache(None)
def maximum(p):
    return 1 if p==0 else max(r*maximum(p-r) for r in range(1,p+1))


def number_of_paths(edges, n):
    vals=[0]*n
    vals[n-1]=1
    for v in range(n-2,-1,-1):
        vals[v]=sum(vals[y] for x,y in edges if x==v)
    return vals[0]


def chain_rigidity(edges,n):
    # Every outgoing edge of a productive vertex must meet the same successor.
    at=0
    total=0
    widths=[]
    while at!=n-1:
        nxt=[v for u,v in edges if u==at]
        if not nxt or len(set(nxt))!=1: return False
        widths.append(len(nxt))
        total+=len(nxt)
        at=nxt[0]
    return total==len(edges)

for p in range(1,10):
    tested=0
    maxima=0
    for n in range(2,min(p+2,6)):
        arcs=[(i,j) for i in range(n-1) for j in range(i+1,n)]
        for indices in combinations_with_replacement(range(len(arcs)),p):
            edges=[arcs[i] for i in indices]
            observed=number_of_paths(edges,n)
            assert observed<=maximum(p),(p,n,edges,observed)
            if observed==maximum(p):
                maxima+=1
                assert chain_rigidity(edges,n),(p,n,edges)
            tested+=1
    print(f'p={p}: {tested} labeled DAG multigraphs, {maxima} max-path graphs; bound {maximum(p)}')
