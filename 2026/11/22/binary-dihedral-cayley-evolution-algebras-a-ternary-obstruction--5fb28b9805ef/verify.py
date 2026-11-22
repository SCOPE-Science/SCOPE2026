#!/usr/bin/env python3
"""Standalone exact verifier for a three-support dihedral evolution algebra.

Scientific computation only: binary structure matrices, ranks, Cayley digraph
symmetry, and the crossed-product unit criterion.
"""
from math import gcd
from itertools import permutations


def product(x, y, n):
    a, b = x
    c, d = y
    return ((a + (-1 if b else 1) * c) % n, b ^ d)


def elements(n):
    return [(a,b) for b in (0,1) for a in range(n)]


def matrix(n):
    el = elements(n)
    pos = {g: i for i, g in enumerate(el)}
    S = [(0,0), (1,0), (0,1)]
    return [sum(1 << pos[product(g,h,n)] for h in S) for g in el]


def binary_rank(rows, d):
    pivots = {}
    for r in rows:
        while r:
            p = r.bit_length() - 1
            if p not in pivots:
                pivots[p] = r
                break
            r ^= pivots[p]
    return len(pivots)


def circ_unit(n):
    # polynomial gcd via Euclidean division over F_2
    def mod(a,b):
        while a and a.bit_length() >= b.bit_length():
            a ^= b << (a.bit_length() - b.bit_length())
        return a
    a, b = (1 << n) | 1, 0b111
    while b:
        a, b = b, mod(a,b)
    return a == 1


def graph_automorphism_count(n):
    # Backtracking with directed adjacency and rank-one features;
    # pure graph search independent of the group presentation proof.
    rows=matrix(n); d=2*n
    # Use outgoing neighborhoods of each vertex; supports uniquely include self.
    adj=[{j for j in range(d) if rows[i]>>j&1} for i in range(d)]
    # Count possible extensions of a partial bijection; naively fixed image of
    # vertex zero and propagate all uniquely recoverable colored arcs.
    reciprocal=[next(v for v in adj[i] if v!=i and i in adj[v]) for i in range(d)]
    rotation=[next(v for v in adj[i] if v!=i and i not in adj[v]) for i in range(d)]
    invrot=[0]*d
    for i,j in enumerate(rotation): invrot[j]=i
    count=0
    for initial in range(d):
        f={0: initial}; todo=[0]
        while todo:
            x=todo.pop()
            for a,b in ((reciprocal[x],reciprocal[f[x]]),(rotation[x],rotation[f[x]]),(invrot[x],invrot[f[x]])):
                if a not in f: f[a]=b;todo.append(a)
                elif f[a]!=b: raise AssertionError('inconsistent action')
        assert len(f)==d and len(set(f.values()))==d
        assert all({f[j] for j in adj[i]}==adj[f[i]] for i in range(d))
        count+=1
    return count


def exhaustive_graph_automorphisms(n):
    # Independent digraph-isomorphism search for all permutations when n<=6.
    import networkx as nx
    from networkx.algorithms.isomorphism import DiGraphMatcher
    rows = matrix(n)
    graph = nx.DiGraph()
    graph.add_nodes_from(range(2*n))
    graph.add_edges_from((i,j) for i in range(2*n) for j in range(2*n) if rows[i] >> j & 1)
    return sum(1 for _ in DiGraphMatcher(graph, graph).isomorphisms_iter())


def run():
    for n in range(3,61):
        rows=matrix(n)
        rank=binary_rank(rows,2*n)
        # For this 3-support family: exactly corank 2 when 3 divides n.
        assert 2*n-rank == (2 if n%3==0 else 0), (n,rank)
        assert circ_unit(n) == (n%3!=0)
        assert graph_automorphism_count(n)==2*n
    for n in range(3,7):
        assert exhaustive_graph_automorphisms(n) == 2*n
    print('BINARY_DIHEDRAL_EVOLUTION_VERIFIED n=3..60; graph_aut=2n; corank=2*indicator(3|n)')

if __name__=='__main__': run()
