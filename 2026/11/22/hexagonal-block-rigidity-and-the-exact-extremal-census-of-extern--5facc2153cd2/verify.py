#!/usr/bin/env python3
"""Finite checks for the outerplanar external trace rigidity theorem.

Requires networkx for minor/planarity checks. All results for unbounded m
follow from the accompanying mathematical proof, not this script.
"""
from itertools import combinations
from math import factorial
import networkx as nx


def outerplanar_incidence(m, supports):
    """Outerplanar iff adjoining a universal apex produces a planar graph."""
    g=nx.Graph()
    A=[('a',i) for i in range(m)]
    g.add_nodes_from(A)
    for j,s in enumerate(supports):
        b=('b',j)
        g.add_edges_from((b,A[i]) for i in s)
    apex=('z',0)
    g.add_edges_from((apex,v) for v in list(g.nodes) if v!=apex)
    return nx.check_planarity(g)[0]


def max_support_families(m):
    subsets=[s for size in range(2,m+1) for s in combinations(range(m),size)]
    target=(3*(m-1))//2
    if m==1:
        assert not subsets
        return 1
    count=0
    # Search only families of the target cardinality, with monotonic pruning.
    def visit(first, chosen):
        nonlocal count
        if len(chosen)==target:
            if outerplanar_incidence(m,chosen):
                count+=1
                if m%2==1:
                    G=nx.Graph()
                    G.add_nodes_from([('a',i) for i in range(m)])
                    for b,s in enumerate(chosen):
                        G.add_edges_from((('b',b),('a',i)) for i in s)
                    assert nx.is_connected(G)
                    blocks=list(nx.biconnected_components(G))
                    assert len(blocks)==(m-1)//2
                    for block in blocks:
                        assert len(block)==6, (m,chosen,block)
                        a=[v for v in block if v[0]=='a']
                        b=[v for v in block if v[0]=='b']
                        assert len(a)==len(b)==3
                        assert G.subgraph(block).number_of_edges() in (6,7)
                        assert all(G.subgraph(block).degree(v) in (2,3) for v in b)
            return
        if len(chosen)+(len(subsets)-first)<target:
            return
        for j in range(first,len(subsets)):
            extended=chosen+[subsets[j]]
            if outerplanar_incidence(m,extended):
                visit(j+1,extended)
    visit(0,[])
    return count


def hypertree_family_count(m):
    t=(m-1)//2
    expected=factorial(m)*m**(t-2)//(2**t*factorial(t)) if t>=2 else 1
    if t>=2:
        # Avoid non-integrality of negative powers in formula for m=3.
        expected=(factorial(m-1)//(2**t*factorial(t)))*m**(t-1)
    triples=list(combinations(range(m),3))
    count=0
    for ts in combinations(triples,t):
        edges={tuple(sorted((x,y))) for tri in ts for x,y in combinations(tri,2)}
        K=nx.Graph()
        K.add_nodes_from(range(m))
        K.add_edges_from(edges)
        if not nx.is_connected(K):
            continue
        if K.number_of_edges()!=3*t:
            continue
        blocks=list(nx.biconnected_components(K))
        if len(blocks)==t and all(len(b)==3 and K.subgraph(b).number_of_edges()==3 for b in blocks):
            count+=1
    return count,expected


def construction(m):
    A=list(range(m))
    supports=[]
    i=1
    while i+1<m:
        a,b=i,i+1
        supports.extend([(0,a),(0,b),(a,b)])
        i+=2
    if i<m:
        supports.append((0,i))
    assert outerplanar_incidence(m,supports)
    assert len(supports)==3*(m-1)//2
    assert len(set(supports))==len(supports)
    # Each parameter singleton, plus empty, is added by an external leaf/isolate.
    all_traces={frozenset()}|{frozenset([a]) for a in A}|{frozenset(s) for s in supports}
    assert len(all_traces)==m+1+3*(m-1)//2


if __name__=='__main__':
    for m in range(1,13):
        construction(m)
    # Exhaustive support-family counts for m <= 5.
    for m,expect in [(1,1),(2,1),(3,4),(4,0),(5,240)]:
        got=max_support_families(m)
        if m==4:
            # Even case has many optimal families, only existence tested above.
            assert got>0,got
        else:
            assert got==expect,(m,got,expect)
        print('MAX_FAMILIES',m,got)
    for m,want in [(3,1),(5,15),(7,735)]:
        got,formula=hypertree_family_count(m)
        assert got==formula==want,(m,got,formula,want)
        print('HYPERTREES',m,got,'MAX_PATTERNS_PREDICTED',got*4**((m-1)//2))
    print('VERIFY_OK')
