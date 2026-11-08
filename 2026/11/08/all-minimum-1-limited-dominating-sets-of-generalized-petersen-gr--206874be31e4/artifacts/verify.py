#!/usr/bin/env python3
"""Exact finite-state check for minimum 1-limited dominating sets of GP(n,2).

Python 3 standard library only. All 256 four-column states are inspected.
The finite graph check covers arbitrarily long cyclic column words.
"""
from itertools import product

STATES = tuple(product(range(4), repeat=4))

def bit(mask, position):
    return (mask >> position) & 1

def edge_allowed(a, b, c, d, e):
    # One opposite-colour neighbour at each of the two central vertices.
    outer = ((bit(b, 0) != bit(c, 0))
             + (bit(d, 0) != bit(c, 0))
             + (bit(c, 1) != bit(c, 0)))
    inner = ((bit(a, 1) != bit(c, 1))
             + (bit(e, 1) != bit(c, 1))
             + (bit(c, 0) != bit(c, 1)))
    return outer == inner == 1

def transition_graph():
    return {s: tuple((*s[1:], e) for e in range(4)
                     if edge_allowed(*s, e)) for s in STATES}

def components(graph):
    # Tarjan algorithm on every four-column state, including isolated states.
    index, low, stack, active, answer = {}, {}, [], set(), []
    def visit(v):
        index[v] = len(index)
        low[v] = index[v]
        stack.append(v)
        active.add(v)
        for w in graph[v]:
            if w not in index:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in active:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            part = set()
            while True:
                w = stack.pop()
                active.remove(w)
                part.add(w)
                if w == v:
                    break
            answer.append(frozenset(part))
    for v in graph:
        if v not in index:
            visit(v)
    assert sum(map(len, answer)) == 256
    return answer

def graph_neighbors(n):
    # Vertices 0..n-1 are outer, n..2n-1 inner.
    ans = []
    for j in range(2*n):
        if j < n:
            ans.append(( (j-1)%n, (j+1)%n, j+n))
        else:
            i = j-n
            ans.append((n+(i-2)%n, n+(i+2)%n, i))
    return ans

def valid_selected(n, mask):
    for v, nbrs in enumerate(graph_neighbors(n)):
        count = sum((mask>>u)&1 for u in nbrs)
        if ((mask>>v)&1 and count < 2) or (not ((mask>>v)&1) and count < 1):
            return False
    return True

def expected_masks(n):
    words = [(1,), (2,)]
    if n%5 == 0:
        for basic in ((0,3,1,3,0),(0,3,3,0,2)):
            for shift in range(5):
                words.append(tuple(basic[(i+shift)%5] for i in range(5)))
    masks = set()
    for seq in words:
        k=0
        for i in range(n):
            v=seq[i%len(seq)]
            if v&1:k |= 1<<i
            if v&2:k |= 1<<(n+i)
        masks.add(k)
    assert len(masks) == 2 + 10*(n%5 == 0)
    return masks

def run():
    graph=transition_graph()
    assert len(graph)==256
    cycle_parts = [p for p in components(graph)
                   if len(p)>1 or next(iter(p)) in graph[next(iter(p))]]
    expected = [
        frozenset({(1,1,1,1)}), frozenset({(2,2,2,2)}),
        frozenset({(0,3,1,3), (3,1,3,0), (1,3,0,0),
                   (3,0,0,3), (0,0,3,1)}),
        frozenset({(0,3,3,0), (3,3,0,2), (3,0,2,0),
                   (0,2,0,3), (2,0,3,3)}),
    ]
    assert set(cycle_parts)==set(expected), cycle_parts
    for part in cycle_parts:
        for v in part:
            assert len(set(graph[v]) & part) == 1
            assert sum(v in graph[u] for u in part) == 1
    print('ALL_256_STATES_AND_FOUR_CYCLIC_COMPONENTS_OK',
          len(cycle_parts), sorted(map(len,cycle_parts)))

    for n in range(5,151):
        target=expected_masks(n)
        assert all(v.bit_count()==n and valid_selected(n,v) for v in target)
    print('ALL_PREDICTED_MINIMIZERS_VALID_OK n=5..150')

    # Independent brute force: no transfer-state assumptions.
    for n in range(5,11):
        found=set()
        for mask in range(1<<(2*n)):
            if mask.bit_count()==n and valid_selected(n,mask):
                found.add(mask)
        target=expected_masks(n)
        assert found==target,(n,len(found),len(target),found^target)
        print('EXACT_MINIMUM_CENSUS_OK',n,len(found))
    print('VERIFY_OK')

if __name__=='__main__': run()
