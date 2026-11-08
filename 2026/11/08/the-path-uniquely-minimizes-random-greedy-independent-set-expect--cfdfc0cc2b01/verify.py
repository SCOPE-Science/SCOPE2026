#!/usr/bin/env python3
"""Exact-arithmetic checks for the strict path-minimum theorem.

Run: python greedy_tree_strict_check.py
Dependencies: Python 3.9+ and NetworkX 2.8+ (for unlabeled trees).
The proof is analytic; finite verification does not establish the infinite theorem.
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial
import networkx as nx

checks = 0

def assert_true(cond, label):
    global checks
    if not cond:
        raise AssertionError(label)
    checks += 1

@lru_cache(None)
def path_mean(n):
    if n <= 0:
        return Fraction(0)
    return sum((Fraction(-2) ** k) * (n - k) / factorial(k+1)
               for k in range(n))

def eta(a, b, j):
    # eta_j = (-1)^(j+1) [alpha_(a+b+j)+alpha_j-alpha_(a+j)-alpha_(b+j)]
    return ((-1)**(j+1)) * (path_mean(a+b+j)+path_mean(j)
                                -path_mean(a+j)-path_mean(b+j))

def nu_at(graph, v):
    remaining = set(graph.nodes()) - {v} - set(graph.neighbors(v))
    return sum((path_mean(len(c)) for c in nx.connected_components(graph.subgraph(remaining))), Fraction(0))

def nu(graph):
    out = Fraction(0)
    for v in graph.nodes():
        out += nu_at(graph,v)
    return out

def kc(graph, x, y):
    path = nx.shortest_path(graph, x, y)
    if graph.degree(x) < 2 or graph.degree(y) < 2:
        return None
    if any(graph.degree(z) != 2 for z in path[1:-1]):
        return None
    out = graph.copy()
    for z in list(graph.neighbors(y)):
        if z != path[-2]:
            out.remove_edge(y, z)
            out.add_edge(x, z)
    assert_true(nx.is_tree(out), 'KC must remain a tree')
    return out

def greedy_mean(graph):
    vertices = list(graph.nodes())
    n = len(vertices)
    adj = [sum(1 << j for j,u in enumerate(vertices) if graph.has_edge(v,u))
           for v in vertices]
    @lru_cache(None)
    def rec(mask):
        if not mask:
            return Fraction(0)
        s=mask.bit_count()
        value=Fraction(1)
        q=mask
        total=Fraction(0)
        while q:
            lsb=q&(-q); idx=lsb.bit_length()-1
            q-=lsb
            total+=rec(mask & ~(lsb|adj[idx]))
        return value+total/s
    return rec((1<<n)-1)

# Separate test of kernel and strict alternating comparison.
for a in range(1,18):
    for b in range(1,18):
        seq=[eta(a,b,j) for j in range(1,23)]
        assert_true(all(t>0 for t in seq), ('positive eta',a,b))
        assert_true(all(x>y for x,y in zip(seq,seq[1:])), ('decreasing eta',a,b))
        for L in range(1,14):
            alt=sum(((-1)**(j+1))*eta(a,b,j) for j in range(1,L+1))
            assert_true(alt>0, ('strict path sum',a,b,L))

# Test the exact first-vertex formula on every path of length <= 13.
for n in range(1,14):
    G=nx.path_graph(n)
    assert_true(path_mean(n)==greedy_mean(G), ('path recurrence',n))

# Exhaustive unlabeled-tree calculations, and every oriented proper bare-path move.
report=[]
for n in range(4,12):
    count=0; moves=0; min_nu_gap=None; min_mean_gap=None
    p=path_mean(n)
    for G in nx.nonisomorphic_trees(n):
        count+=1
        q=greedy_mean(G)
        if nx.is_isomorphic(G,nx.path_graph(n)):
            assert_true(q==p, ('path equality',n))
        else:
            d=q-p
            assert_true(d>0, ('path strict uniqueness',n,nx.to_graph6_bytes(G,header=False)))
            min_mean_gap=d if min_mean_gap is None else min(min_mean_gap,d)
        before=nu(G)
        nodes=list(G)
        for x in nodes:
            for y in nodes:
                if x==y:
                    continue
                H=kc(G,x,y)
                if H is None:
                    continue
                moves+=1
                delta=nu(H)-before
                assert_true(delta>0, ('strict nu KC',n,x,y,nx.to_graph6_bytes(G,header=False)))
                min_nu_gap=delta if min_nu_gap is None else min(min_nu_gap,delta)
                path=nx.shortest_path(G,x,y)
                P=set(path)
                A={v for v in G if v not in P and x in nx.shortest_path(G,v,y)}
                B=set(G)-P-A
                assert_true(bool(A) and bool(B), ('nonempty sides',n,x,y))
                assert_true(all(nu_at(H,v)>=nu_at(G,v) for v in A|B), ('offpath',n,x,y))
                path_actual=sum((nu_at(H,v)-nu_at(G,v) for v in path),Fraction(0))
                path_formula=sum((path_mean(len(A)+len(B)+j)+path_mean(j)
                              -path_mean(len(A)+j)-path_mean(len(B)+j)
                              for j in range(1,len(path)-1)),Fraction(0))
                assert_true(path_actual==path_formula, ('central identity',n,x,y))
    report.append((n,count,moves,min_mean_gap,min_nu_gap))
for row in report:
    print('n=%d trees=%d proper_oriented_KC=%d min_mean_gap=%s min_nu_gap=%s'%row)
print('PASS',checks,'exact assertions')
