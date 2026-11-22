#!/usr/bin/env python3
"""Finite checks for pair-type recovery over multipartite Henson-graph bases.

All direct checks build the labelled graph and inspect EVERY possible
forbidden clique, rather than evaluating the analytic obstruction criterion.
The generic proof uses Henson homogeneity and Bang--Zsigmondy's theorem;
finite checks do not establish the theorem for unbounded part sizes.
"""
from itertools import combinations
from collections import defaultdict
from math import comb


def partitions(n, smallest=1):
    if n == 0:
        yield ()
    else:
        for i in range(smallest, n+1):
            for tail in partitions(n-i, i):
                yield (i,) + tail


def closed_counts(sizes, forbidden_order):
    n, ell = sum(sizes), len(sizes)
    assert 1 <= ell <= forbidden_order-2 and min(sizes) > 0
    if ell < forbidden_order-2:
        return 2**n, 2 * 4**n, 4**n, 4**n
    blocked = 1
    for a in sizes:
        blocked *= 4**a - 3**a
    return 2**n, 2*4**n-blocked, 4**n, 4**n-blocked


def build_base(sizes):
    colors = [i for i,a in enumerate(sizes) for _ in range(a)]
    edges = set()
    for i,j in combinations(range(len(colors)),2):
        if colors[i] != colors[j]:
            edges.add((i,j))
    return colors, edges


def direct_counts(sizes, forbidden_order):
    n = sum(sizes)
    _,base_edges = build_base(sizes)
    all_cliques = list(combinations(range(n+2), forbidden_order))
    # For each graph on the named base plus two ordered extra vertices,
    # explicitly inspect all size-forbidden_order cliques.
    nonedge = edge = 0
    for a in range(1 << n):
        a_edges = {(j,n) for j in range(n) if a>>j & 1}
        for b in range(1 << n):
            b_edges = {(j,n+1) for j in range(n) if b>>j & 1}
            common = base_edges | a_edges | b_edges
            for e in (False,True):
                edges = common | ({(n,n+1)} if e else set())
                valid = True
                for clique in all_cliques:
                    if all((u,v) in edges for u,v in combinations(clique,2)):
                        valid = False
                        break
                if valid:
                    if e: edge += 1
                    else: nonedge += 1
    return nonedge,edge


def run():
    checks=0
    for m in (5,6,7):
        for n in range(1,7):
            for sizes in partitions(n):
                if len(sizes)>m-2: continue
                if n > 5 and len(sizes) < 3: continue
                want = closed_counts(sizes,m)
                got = direct_counts(sizes,m)
                assert got == want[2:], (m,sizes,got,want)
                checks+=1
    print('PASS direct labelled graph clique checks:',checks)

    # With fixed n, every unordered partition into k=m-2 positive parts
    # has a distinct corrected pair-type count, tested through n=36.
    recon=0
    for n in range(3,37):
        for k in range(3,min(n,12)+1):
            seen={}
            for sizes in partitions(n):
                if len(sizes)!=k: continue
                t1,t2,_,_ = closed_counts(sizes,k+2)
                assert t1 == 2**n
                assert t2 not in seen,(n,k,seen.get(t2),sizes)
                seen[t2]=sizes
                recon+=1
    print('PASS partition fingerprint uniqueness through n=36:',recon)
    assert closed_counts((3,1,1),5)[:2] == (32,2011)
    assert closed_counts((2,2,1),5)[:2] == (32,1999)
    assert closed_counts((2,2),6)[:2] == (16,512)
    print('PASS threshold example: K_(3,1,1) 2011 versus K_(2,2,1) 1999')
    print('PASS subcritical complete bipartite base has unrestricted pair types in H_6')
    print('FINITE CHECKS ARE NOT AN UNBOUNDED PROOF')

if __name__=='__main__':
    run()
