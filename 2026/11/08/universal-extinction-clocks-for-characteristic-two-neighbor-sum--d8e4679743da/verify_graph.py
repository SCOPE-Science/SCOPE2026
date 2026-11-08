#!/usr/bin/env python3
"""Verify parity-tree extinction with direct unrooted graph dynamics over F_2."""
from collections import deque
from itertools import product
import networkx as nx

def bitrows(adj):
    return [sum(1 << j for j in neighbors) for neighbors in adj]

def act(rows,x):
    return sum(((rows[i] & x).bit_count() & 1) << i for i in range(len(rows)))

def rank(mat):
    piv={}
    for z in mat:
        while z:
            p=z.bit_length()-1
            if p in piv:z ^= piv[p]
            else:piv[p]=z;break
    return len(piv)

def test_one(G):
    v=list(G.nodes());ids={w:i for i,w in enumerate(v)}
    adj=[[ids[u] for u in G.neighbors(w)] for w in v]
    rows=bitrows(adj)
    evens=[i for i,w in enumerate(v) if G.degree(w)%2==0]
    assert len(evens)==1
    root=evens[0]
    dist=nx.single_source_shortest_path_length(G,v[root]);h=max(dist.values());N=len(v)
    lvl=[i for i,w in enumerate(v) if dist[w]==h]
    basis=[1<<i for i in range(N)]
    for i in range(N):
        z=basis[i]
        for j in range(h+dist[v[i]]):z=act(rows,z)
        assert z==sum(1<<i for i in lvl),(N,h,i,'impulse last')
        assert act(rows,z)==0,(N,h,i,'impulse extinction')
    P=basis
    ranks=[N]
    for t in range(1,2*h+2):
        P=[act(rows,z) for z in P]
        ranks.append(rank(P))
    assert ranks[-1]==0 and ranks[-2]==1,(N,h,ranks)
    if h>=1:assert ranks[-3]==2,(N,h,ranks)
    # column expression for A^(2h): all deepest input sites give same deepest-output word
    P=basis
    for t in range(2*h):P=[act(rows,z) for z in P]
    layerword=sum(1<<i for i in lvl)
    assert P==[layerword if i in lvl else 0 for i in range(N)]
    if N<=9:
        # Every configuration; first hitting time from direct iteration, no algebraic shortcuts.
        for x in range(1<<N):
            y=x;tt=0
            while y:
                y=act(rows,y);tt+=1
                assert tt<=2*h+1
            if (x & layerword).bit_count()%2: assert tt==2*h+1
            else: assert tt<2*h+1
    return N,h

def main():
    cases=0;hmax=0;Nmax=0
    G=nx.empty_graph(1)
    test_one(G);cases+=1
    for n in range(3,16,2):
        for G in nx.generators.nonisomorphic_trees(n):
            if sum(G.degree(w)%2==0 for w in G.nodes())!=1:continue
            N,h=test_one(G);cases+=1;hmax=max(hmax,h);Nmax=max(Nmax,N)
    # Comb family, every node on the spine has two children: one side leaf, one continuation.
    for h in range(1,31):
        C=nx.Graph();C.add_node(0);u=0;v=1
        for depth in range(h):
            C.add_edge(u,v);C.add_edge(u,v+1)
            if depth<h-1:u=v
            v+=2
        # At the deepest level of the construction the two children are both leaves.
        assert max(dict(nx.single_source_shortest_path_length(C,0)).values())==h
        assert nx.diameter(C)==h+1
        if h<=7:test_one(C)
        cases+=1
    print('VERIFY_GRAPH_OK', 'cases_including_combs', cases, 'nonisomorphic_eligible_trees', cases-30, 'max_order_nonisomorphic',Nmax,'max_height_nonisomorphic',hmax,'comb_diameter_gap_up_to_height',30)
if __name__=='__main__':main()
