"""Self-contained exact combinatorial checks for doubles of stacked 3-spheres.
Only standard library. Uses facet lists, not any external generated data.
"""
from itertools import combinations
from collections import deque
import random

def double_graph(facets):
    vertices=sorted(set(tuple(sorted(e)) for f in facets for e in combinations(f,2)))
    edges=set()
    for f in facets:
        for e in combinations(f,2):
            other=tuple(sorted(set(f)-set(e)))
            e=tuple(e)
            edges.add(tuple(sorted((e,other))))
    return vertices,edges

def components(vertices,edges):
    adj={v:set() for v in vertices}
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    unseen=set(vertices); total=0
    while unseen:
        total+=1
        seen={unseen.pop()}; todo=list(seen)
        while todo:
            for w in adj[todo.pop()]:
                if w in unseen:
                    unseen.remove(w);todo.append(w)
    return total

def stack(facets,i,new_label):
    facet=facets[i]
    return facets[:i]+facets[i+1:]+[tuple(sorted((set(facet)-{x})|{new_label})) for x in facet]

def assert_case(facets):
    n=max(x for f in facets for x in f)+1
    verts,edges=double_graph(facets)
    c=components(verts,edges)
    assert len(verts)==4*n-10,(n,len(verts))
    assert len(facets)==3*n-10,(n,len(facets))
    assert len(edges)==9*n-30,(n,len(edges))
    assert c==1,(n,c)
    assert len(edges)-len(verts)+1==5*n-19
    # Every edge of double corresponds to a unique tetrahedral facet and a partition into two pairs.
    assert len(edges)==3*len(facets)
    return n,len(facets),len(verts),len(edges),5*n-19

if __name__=='__main__':
    initial=[tuple(f) for f in combinations(range(5),4)]
    checked={5:0}
    # Check all possible stacking histories with at most three insertions.
    current=[initial]
    for n in range(5,9):
        next_level=[]
        for facets in current:
            assert_case(facets)
            checked[n]=checked.get(n,0)+1
            if n<8:
                for i in range(len(facets)):
                    next_level.append(stack(facets,i,n))
        current=next_level
    # Sample longer histories with reproducible nontrivial facet choices.
    rng=random.Random(1979)
    for nmax in (9,12,16,20):
        for _ in range(40):
            facets=initial
            for n in range(5,nmax):
                facets=stack(facets,rng.randrange(len(facets)),n)
            assert_case(facets)
    print('STACKED_DOUBLE_PASS')
    print('exhaustive histories for n=5..8:',[(n,checked[n]) for n in range(5,9)])
    print('sampled 40 histories each at n=9,12,16,20')
    print('n,facets,double_vertices,double_edges,betti1:')
    for nmax in (5,6,7,8,9,12,16,20):
        facets=initial
        for n in range(5,nmax):
            facets=stack(facets,0,n)
        print(assert_case(facets))
