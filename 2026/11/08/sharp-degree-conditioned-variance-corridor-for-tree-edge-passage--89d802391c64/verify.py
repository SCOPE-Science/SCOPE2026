#!/usr/bin/env python3
"""Reproduce exact rooted-tree passage-time variance checks for the stated finite ranges.
This is a supplementary finite check, not a proof for unbounded tree order.
Requires networkx and sympy.
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd
import networkx as nx
import sympy as sp


def descendants(tree, v, parent):
    count = 1
    for w in tree.neighbors(v):
        if w != parent:
            count += descendants(tree, w, v)
    return count


def fringe_structure(tree, root):
    kids = [u for u in tree.neighbors(root)]
    return [descendants(tree, u, root) for u in kids]


def signature(tree, root, parent=None):
    return tuple(sorted(signature(tree, u, root) for u in tree.neighbors(root) if u != parent))


def variance_fringe(tree, root):
    s = len(tree)
    def proper(v, parent):
        t = descendants(tree, v, parent)
        return t*(t-1) + sum(proper(u, v) for u in tree.neighbors(v) if u != parent)
    return 4*s*(s-1) + 8*sum(proper(u, root) for u in tree.neighbors(root))


def extrema(s, k):
    a,b = divmod(s-1,k)
    lower = 4*s*(s-1) + 8*((k-b)*a*(a-1) + b*a*(a+1))
    t = s-k
    upper = 4*s*(s-1) + (8*(t*t*t-t))//3
    assert (8*(t*t*t-t)) % 3 == 0
    return lower, upper


def exact_chain_moments(tree, root):
    labels = list(tree.nodes())
    ix = {v:i for i,v in enumerate(labels)}
    n = len(labels)
    Q = sp.zeros(n)
    for v in labels:
        # The root has one additional, absorbing parent attached externally.
        deg = tree.degree(v) + (v==root)
        for w in tree.neighbors(v):
            Q[ix[v],ix[w]] = sp.Rational(1,deg)
    N = (sp.eye(n)-Q).inv()
    first = N*sp.ones(n,1)
    second = (2*N-sp.eye(n))*first
    i = ix[root]
    return first[i], sp.factor(second[i]-first[i]**2)

checks=0
shape_values = defaultdict(list)
for s in range(2,9):
    for T in nx.nonisomorphic_trees(s):
        for root in T.nodes():
            k = T.degree(root)
            L,U=extrema(s,k)
            v=variance_fringe(T,root)
            assert L <= v <= U, (s,k,v,L,U)
            m,v_direct=exact_chain_moments(T,root)
            assert m == 2*s-1 and v_direct == v, (s,k,m,v,v_direct)
            checks += 3
            shape_values[(s,k)].append((int(v),signature(T,root)))
for (s,k),vlist in shape_values.items():
    L,U=extrema(s,k)
    vals=[v for v,sg in vlist]
    assert min(vals)==L and max(vals)==U, (s,k,min(vals),max(vals),L,U)
    checks += 2
    # exactly one rooted isomorphism class at the minimum and maximum
    assert len(set(sg for v,sg in vlist if v==L))==1
    assert len(set(sg for v,sg in vlist if v==U))==1
    checks += 2

# Fixed-degree asymptotic witness: same order & root degree yet linear variance ratio.
for m in range(2,70):
    s=2*m+1; k=m; L,U=extrema(s,k)
    assert U>=L and L==4*s*(s-1)+16*m
    checks+=2

print(f'PASS: {checks} exact assertions, s=2..8 rooted nonisomorphic trees and fixed-degree comparisons; no infinite-claim inference from enumeration')
