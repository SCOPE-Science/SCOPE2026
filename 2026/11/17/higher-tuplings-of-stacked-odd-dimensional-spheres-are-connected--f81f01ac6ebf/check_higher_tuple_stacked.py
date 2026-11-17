#!/usr/bin/env python3
"""Exhaustive labeled facet-stacking test for higher simplicial tuplings.
Only finite checks; the associated theorem is proved symbolically.
"""
from itertools import combinations
from math import comb

def build_graph(facets,r):
    verts=set();edges=set()
    for f in facets:
        assert len(f)==2*r
        ordered=tuple(sorted(f))
        for a in combinations(ordered,r):
            b=tuple(x for x in ordered if x not in a)
            verts.add(a);verts.add(b)
            edges.add(frozenset((a,b)))
    return verts,edges

def components(verts,edges):
    adj={x:set() for x in verts}
    for edge in edges:
        x,y=tuple(edge)
        adj[x].add(y);adj[y].add(x)
    unseen=set(verts)
    c=0
    while unseen:
        c+=1
        seen={unseen.pop()};stack=list(seen)
        while stack:
            for y in adj[stack.pop()]-seen:
                seen.add(y);stack.append(y)
        unseen-=seen
    return c

def stack(facets,f,new):
    out=set(facets);out.remove(f)
    for v in f:
        out.add(frozenset((set(f)-{v})|{new}))
    return frozenset(out)

def check(r,max_n):
    n0=2*r+1
    facets=frozenset(frozenset(t) for t in combinations(range(n0),2*r))
    frontier=[facets]
    for n in range(n0,max_n+1):
        expected_beta=1+(n-2*r)*(r-1)*comb(2*r+1,r)//2
        expected_v=comb(2*r+1,r)+(n-n0)*comb(2*r,r-1)
        expected_e=(2*r+1+(n-n0)*(2*r-1))*comb(2*r,r)//2
        next_frontier=[]; dedup=set()
        for fs in frontier:
            v,e=build_graph(fs,r)
            C=components(v,e)
            actual=(len(v),len(e),C,len(e)-len(v)+C)
            want=(expected_v,expected_e,1,expected_beta)
            assert actual==want,(r,n,actual,want)
            if n<max_n:
                for f in fs:
                    nxt=stack(fs,f,n)
                    if nxt not in dedup:
                        dedup.add(nxt);next_frontier.append(nxt)
        print(f'r={r}, n={n}, labeled_types_tested={len(frontier)}, tuple_vertices={expected_v}, tuple_edges={expected_e}, connected=1, beta1={expected_beta}')
        frontier=next_frontier

if __name__=='__main__':
    check(3,10)
    check(4,11)
    check(5,12)
    print('HIGHER_TUPLE_STACKING_CHECK_PASS')
