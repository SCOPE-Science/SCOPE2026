#!/usr/bin/env python3
"""Exact standalone exhaustive checks of super-coalition partition spectra."""
from collections import Counter
from itertools import combinations
from math import comb
from random import Random


def set_partitions(n):
    blocks=[]
    def rec(v):
        if v==n:
            yield tuple(blocks)
            return
        bit=1<<v
        for j in range(len(blocks)):
            blocks[j]|=bit
            yield from rec(v+1)
            blocks[j]^=bit
        blocks.append(bit)
        yield from rec(v+1)
        blocks.pop()
    yield from rec(0)


def adjacency(profile):
    labels=[i for i,q in enumerate(profile) for _ in range(q)]
    return [sum(1<<v for v in range(len(labels)) if labels[u]!=labels[v])
            for u in range(len(labels))]


def super_dominating(adj, selected):
    n=len(adj)
    omitted=((1<<n)-1)^selected
    for u in range(n):
        if omitted&(1<<u):
            if not any((selected&(1<<v)) and (adj[v]&omitted)==(1<<u)
                       for v in range(n)):
                return False
    return True


def predicted(adj):
    n=len(adj)
    assert n>=6
    full=(1<<n)-1
    if any(a==0 for a in adj):return None
    # Super domination is upward closed: omission of a triple is the boundary test.
    for tri in combinations(range(n),3):
        if super_dominating(adj,full^sum(1<<v for v in tri)):
            return None
    edges=[(u,v) for u,v in combinations(range(n),2)
           if super_dominating(adj,full^(1<<u)^(1<<v))]
    edge_set={frozenset(e) for e in edges}
    e=len(edges)
    m2=sum(len(set(a+b))==4 for a,b in combinations(edges,2))
    m3=sum(len(set(a+b+c))==6 for a,b,c in combinations(edges,3)) if n==6 else 0
    triangles=sum(all(frozenset(pair) in edge_set for pair in combinations(tri,2))
                  for tri in combinations(range(n),3))
    result={2:(1<<(n-1))-1-n-e,
            3:comb(n,2)-e+(n-2)*e+m2-2*m3,
            4:triangles}
    return result,(e,m2,m3,triangles)


def observed(adj, partitions):
    n=len(adj)
    sd=[super_dominating(adj,mask) for mask in range(1<<n)]
    out=Counter()
    for blocks in partitions:
        k=len(blocks)
        if k<2:continue
        if any(sd[b] for b in blocks):continue
        if all(any(i!=j and sd[blocks[i]|blocks[j]] for j in range(k))
               for i in range(k)):
            out[k]+=1
    return {k:out[k] for k in (2,3,4)},sum(v for k,v in out.items() if k>=5)


def graph_from_edges(n,edge_mask):
    adj=[0]*n
    for pos,(u,v) in enumerate(combinations(range(n),2)):
        if edge_mask>>pos&1:
            adj[u]|=1<<v;adj[v]|=1<<u
    return adj


def graph_from_edge_list(n,edges):
    adj=[0]*n
    for u,v in edges:
        adj[u]|=1<<v
        adj[v]|=1<<u
    return adj


def main():
    profiles=[(2,4),(3,3),(2,2,2),(2,5),(3,4),(2,2,3),(2,6),(3,5),
              (4,4),(2,2,4),(2,3,3),(2,2,2,2),(3,3,3),(2,3,4),(2,2,2,3)]
    for profile in profiles:
        a=adjacency(profile)
        p=predicted(a)
        assert p is not None
        count,more=observed(a,list(set_partitions(len(a))))
        assert count==p[0] and more==0,(profile,count,p)
    print('MULTIPARTITE_EXHAUSTIVE_OK',len(profiles))

    partitions6=list(set_partitions(6))
    eligible=0
    for edge_bits in range(1<<15):
        a=graph_from_edges(6,edge_bits)
        p=predicted(a)
        if p is None:continue
        got,more=observed(a,partitions6)
        assert got==p[0] and more==0,(edge_bits,got,p)
        eligible+=1
    print('ALL_SIX_VERTEX_GRAPHS_OK',eligible)
    assert eligible==24509

    rng=Random(49373)
    for n in (7,8):
        ps=list(set_partitions(n));seen=0
        for _ in range(350):
            a=graph_from_edges(n,rng.randrange(1<<comb(n,2)))
            p=predicted(a)
            if p is None:continue
            got,more=observed(a,ps)
            assert got==p[0] and more==0,(n,got,p)
            seen+=1
        print('SEEDED_OTHER_GRAPHS_OK',n,seen)

    # Two connected six-vertex graphs with identical superdomination size
    # polynomial but different coalition spectra and coalition maxima.
    graph1=[(0,2),(0,3),(0,4),(0,5),(1,2),(1,3)]
    graph2=[(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(1,5),(2,3),(2,4)]
    for edges,expected in ((graph1,{2:19,3:39,4:0}),
                           (graph2,{2:19,3:42,4:2})):
        a=graph_from_edge_list(6,edges)
        assert predicted(a)[0]==expected
        assert observed(a,partitions6)==(expected,0)
        full=(1<<6)-1
        assert sum(super_dominating(a,full^om)
                   for om in range(1<<6) if om.bit_count()==2)==6
    print('SAME_SET_POLYNOMIAL_DIFFERENT_COALITION_SPECTRA_OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
