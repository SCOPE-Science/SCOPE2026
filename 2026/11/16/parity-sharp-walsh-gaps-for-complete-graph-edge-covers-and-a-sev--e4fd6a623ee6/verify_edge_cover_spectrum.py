#!/usr/bin/env python3
"""Exact integer verification for complete-graph edge-cover Walsh spectra.

Requires Python 3, numpy, and networkx. No remote services or external data files.
Run: python verify_edge_cover_spectrum.py
Produces edge_cover_zero_orbits.csv and edge_cover_summary.csv.
"""
import csv
import itertools
import math
from collections import Counter
from pathlib import Path
import numpy as np
import networkx as nx

ROOT=Path(__file__).resolve().parent

def edges(n):
    return list(itertools.combinations(range(n),2))

def direct_fourier(n):
    E=edges(n); m=len(E); N=1<<m
    covered=np.zeros(N,dtype=np.uint16)
    for k,(i,j) in enumerate(E):
        h=1<<k
        covered[h:2*h]=covered[:h] | (1<<i) | (1<<j)
    a=np.asarray(covered==(1<<n)-1,dtype=np.int64)
    cover_count=int(a.sum())
    for k in range(m):
        h=1<<k
        v=a.reshape(-1,2*h)
        x=v[:,:h].copy();y=v[:,h:].copy()
        v[:,:h]=x+y
        v[:,h:]=x-y
    return a,cover_count

def independent_zeta(n):
    E=edges(n);m=len(E);N=1<<m
    g=np.zeros(N,dtype=np.int64)
    g[0]=1-n                 # empty and singleton vertex subsets
    for S in range(1<<n):
        k=S.bit_count()
        if k<2:continue
        mask=sum(1<<j for j,(u,v) in enumerate(E) if (S>>u&1) and (S>>v&1))
        g[mask]+=(-1 if k&1 else 1)*(1<<(k*(k-1)//2))
    # subset zeta: q[Q] = sum_{A subset Q} g[A]
    for k in range(m):
        h=1<<k
        v=g.reshape(-1,2*h)
        v[:,h:]+=v[:,:h]
    return ((-1 if n&1 else 1)*g)[(N-1)^np.arange(N,dtype=np.int64)]

def indpoly(graph):
    n=len(graph)
    adj=[0]*n
    for u,v in graph.edges():adj[u]|=1<<v;adj[v]|=1<<u
    p=[0]*(n+1)
    for S in range(1<<n):
        if all(not(adj[i]&S) for i in range(n) if S>>i&1):
            p[S.bit_count()]+=1
    return p

def spectrum_weight(p):
    n=len(p)-1
    return ((-1)**n)*sum((-1)**k*(1<<(k*(k-1)//2))*pk for k,pk in enumerate(p))

def orbit_census(n):
    result=[];seen=0
    for graph in nx.graph_atlas_g():
        if len(graph)!=n:continue
        seen+=1;p=indpoly(graph)
        if spectrum_weight(p)!=0:continue
        aut=sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(graph,graph).isomorphisms_iter())
        assert math.factorial(n)%aut==0
        result.append(dict(n=n,graph6=nx.to_graph6_bytes(graph,header=False).decode().strip(),
                           edges=graph.number_of_edges(),independent_coefficients=';'.join(map(str,p)),
                           automorphisms=aut,labelled_multiplicity=math.factorial(n)//aut,walsh_multiplier=0))
    return seen,result

def main():
    summaries=[]; all_orbits=[]
    for n in range(2,8):
        direct,num=direct_fourier(n)
        formula=independent_zeta(n)
        assert np.array_equal(direct,formula), ('two computations differ',n)
        assert int(np.dot(direct,direct))==(1<<len(edges(n)))*num, ('Parseval',n)
        zero=int(np.count_nonzero(direct==0))
        gap=int(np.min(np.abs(direct[direct!=0])))
        assert num==sum((-1)**(n-k)*math.comb(n,k)*2**(k*(k-1)//2) for k in range(n+1))
        assert zero==0 if n%2==0 else zero>0
        assert gap==(1 if n%2==0 else 2)
        if n%2:
            # precisely one half with valuation exactly one
            assert int(np.count_nonzero(direct%4==2))==(1<<(len(edges(n))-1))
        if n in (5,7):
            all_graphs,orbits=orbit_census(n)
            assert all_graphs==({5:34,7:1044}[n])
            assert sum(x['labelled_multiplicity'] for x in orbits)==zero
            assert len(orbits)==({5:3,7:39}[n])
            all_orbits.extend(orbits)
        expected={2:(1,0),3:(4,3),4:(41,0),5:(768,105),6:(27449,0),7:(1887284,73115)}
        assert (num,zero)==expected[n]
        summaries.append(dict(n=n,vertices=n,edge_coordinates=len(edges(n)),edge_covers=num,
                              zero_multipliers=zero,positive_rank=len(direct)-zero,
                              min_nonzero_abs=gap,max_abs=int(np.max(np.abs(direct))),
                              distinct_signed_values=len(set(map(int,direct)))))
        print('n=',n,'count=',num,'zeros=',zero,'rank=',len(direct)-zero,'gap=',gap)
    if all_orbits:
        with (ROOT/'edge_cover_zero_orbits.csv').open('w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=list(all_orbits[0]));writer.writeheader();writer.writerows(all_orbits)
    with (ROOT/'edge_cover_summary.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(summaries[0]));writer.writeheader();writer.writerows(summaries)
    print('EDGE_COVER_COMPLETE_GRAPH_FOURIER_EXACT_PASS', 'n7_orbits=39','n7_zeros=73115')

if __name__=='__main__':main()
