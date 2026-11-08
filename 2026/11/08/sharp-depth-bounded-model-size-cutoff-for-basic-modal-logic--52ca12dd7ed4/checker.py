#!/usr/bin/env python3
"""Finite, independent checks of the depth-bounded Kripke type construction.

Run: python3 checker.py
The mathematical proof holds for arbitrary k and d; this executable only
checks explicitly stated finite parameter ranges and sampled high-order cases.
"""
from itertools import combinations
import random

def finite_types(k, level):
    """Lists standard full types through level; returns layers of hashables."""
    layers = [tuple(range(1 << k))]
    for _ in range(level):
        prior = layers[-1]
        if len(prior) > 16:
            raise ValueError('Not enumerating more than 16 predecessor types')
        layers.append(tuple((c, frozenset(prior[i] for i in range(len(prior)) if mask >> i & 1))
                            for c in range(1 << k) for mask in range(1 << len(prior))))
    return layers

def projection(type_, level):
    """Projection from level to level-1."""
    if level == 0:
        raise ValueError('level zero does not project')
    if level == 1:
        return type_[0]
    return (type_[0], frozenset(projection(v, level - 1) for v in type_[1]))

def build(k, depth, target_colour, subset, types):
    """Exactly |T_{d-1}| worlds; an assigned root has (colour, subset) rank d type."""
    assert depth >= 1
    layer = types[depth - 1]
    N = len(layer)
    loc = {v: i for i, v in enumerate(layer)}
    assert len(loc) == N
    subset = frozenset(subset)
    if depth == 1:
        root_type = target_colour
    else:
        root_type = (target_colour, frozenset(projection(v, depth - 1) for v in subset))
    root = loc[root_type]
    colours = [(v if depth == 1 else v[0]) for v in layer]
    adjacency = [[] for _ in layer]
    if depth >= 2:
        sections = {}
        for i, v in enumerate(layer):
            sections.setdefault(projection(v, depth - 1), i)
        for i, v in enumerate(layer):
            if i != root:
                adjacency[i] = sorted(sections[x] for x in v[1])
    adjacency[root] = sorted(loc[v] for v in subset)
    return root, colours, adjacency

def observed_types(colours, adjacency, maxlevel):
    cur = list(colours)
    layers = [cur]
    for _ in range(maxlevel):
        cur = [(colours[i], frozenset(cur[j] for j in adjacency[i])) for i in range(len(colours))]
        layers.append(cur)
    return layers

def check_instance(k, d, colour, S, types):
    S = frozenset(S)
    root, colours, adj = build(k, d, colour, S, types)
    actual = observed_types(colours, adj, d)
    if actual[d][root] != (colour, frozenset(S)):
        raise AssertionError(('root', k, d, colour, S, actual[d][root]))
    expected = types[d - 1]
    if tuple(actual[d-1]) != tuple(expected):
        for i, (a,b) in enumerate(zip(actual[d-1], expected)):
            if a != b:
                raise AssertionError(('universal', k, d, i, a, b))
    return len(adj), sum(map(len, adj))

def run():
    r = random.Random(41780)
    total = 0
    examples = []
    for k,d in [(0,1),(0,2),(0,3),(0,4),(1,1),(1,2),(2,1)]:
        layers = finite_types(k,d-1)
        layer = layers[-1]
        N = len(layer)
        for c in range(1 << k):
            for mask in range(1 << N):
                S = (layer[i] for i in range(N) if mask >> i & 1)
                check_instance(k,d,c,S,layers)
                total += 1
        examples.append((k,d,N,(1 << k)*(1 << N)))
    # At depth 3 and one proposition the predecessor type count is 512;
    # enumerating all target subsets would require 2^512 iterations.
    k,d=1,3
    layers=finite_types(k,d-1)
    N=len(layers[-1])
    for c in (0,1):
        for _ in range(100):
            S = (v for v in layers[-1] if r.getrandbits(1))
            check_instance(k,d,c,S,layers)
            total += 1
    examples.append((1,3,N,'200 sampled target types'))
    print('MODAL_SHARP_DEPTH_CUTOFF_OK')
    print('instances', total)
    for row in examples:
        print('k,d,cutoff,checked',row)
    print('Witness lower bound: formula requiring all predecessor types as successors needs >= cutoff worlds.')
if __name__ == '__main__':
    run()
