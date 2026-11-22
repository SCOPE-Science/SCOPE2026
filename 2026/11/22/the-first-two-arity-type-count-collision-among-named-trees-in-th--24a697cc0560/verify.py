#!/usr/bin/env python3
"""An isomorphism-free exhaustive census of one-, two- and three-point Henson types over trees.
Requires Python 3.9+ standard library only; no external data or graph package.
"""
from collections import defaultdict
from functools import lru_cache

EXPECTED = [1, 1, 1, 2, 3, 6, 11, 23, 47, 106]


def canonical_tree(edges, n):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    def rooted(u, parent):
        return '(' + ''.join(sorted(rooted(v, u) for v in adj[u] if v != parent)) + ')'
    return min(rooted(u, -1) for u in range(n))


def trees_through_ten():
    current = [tuple()]
    for n in range(1, 11):
        assert len(current) == EXPECTED[n-1], (n, len(current))
        yield n, current
        if n == 10:
            break
        nxt = {}
        for edges in current:
            for vertex in range(n):
                candidate = tuple(sorted(edges + ((vertex, n),)))
                nxt.setdefault(canonical_tree(candidate, n+1), candidate)
        current = list(nxt.values())


def independent_sets(edges, n):
    out = []
    for mask in range(1 << n):
        if all(not ((mask & (1 << u)) and (mask & (1 << v))) for u, v in edges):
            out.append(mask)
    return out


def types_profile(edges, n, include_arity_three=False):
    independent = independent_sets(edges, n)
    one = len(independent)
    two_adjacency = sum(1 for x in independent for y in independent if not (x & y))
    if not include_arity_three:
        return one, two_adjacency
    # Exact empty-, one-edge-, and two-edge-internal labelled 3-vertex extensions.
    # Two-edge extensions have two leaves constrained to be disjoint from the centre's neighbourhood.
    exact_three_path = sum(sum(1 for x in independent if not (x & middle)) ** 2 for middle in independent)
    return one, two_adjacency, exact_three_path


def independently_count_triples(edges, n, graph_on_new_vertices):
    """Independent 8-state tree-transfer recurrence, not using independent-set enumeration."""
    forbidden = set(graph_on_new_vertices)
    states = [s for s in range(8) if all(not ((s >> i & 1) and (s >> j & 1)) for i, j in forbidden)]
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    def compute(node, parent):
        child_arrays = [compute(v, node) for v in adj[node] if v != parent]
        return {s: __import__('math').prod(sum(a for t, a in arr.items() if not (s & t)) for arr in child_arrays) for s in states}
    return sum(compute(0, -1).values())


def main():
    first_collisions = []
    all_last = []
    for n, trees in trees_through_ten():
        cells = defaultdict(list)
        for edges in trees:
            i, d = types_profile(edges, n)
            cells[(i, d)].append(edges)
            if n == 10:
                all_last.append((canonical_tree(edges, n), i, d))
        collisions = [v for v in cells.values() if len(v) > 1]
        print('TREE_ORDER', n, 'ISOMORPHISM_CLASSES', len(trees), 'COLLISION_FIBRES', len(collisions))
        if n < 10:
            assert not collisions, ('premature', n)
        else:
            assert len(collisions) == 1 and len(collisions[0]) == 2
            first_collisions = collisions[0]
    a, b = sorted(first_collisions, key=lambda e: canonical_tree(e, 10))
    cs = [canonical_tree(x, 10) for x in (a,b)]
    assert cs[0] != cs[1]
    p1, p2 = [types_profile(x, 10, True) for x in (a, b)]
    assert p1[:2] == p2[:2] == (160, 8649), (p1, p2)
    assert sorted([p1[2], p2[2]]) == [578337, 578961], (p1,p2)
    arity_three = [i**3 + 3*i*d + 3*j for i,d,j in (p1,p2)]
    assert sorted(arity_three) == [9982531,9984403]
    assert p2[2]-p1[2] != 0
    print('FIRST_COLLISION_N', 10)
    print('FIRST_COLLISION_PAIR_ISOMORPHISM_CODES', *cs)
    print('FIRST_COLLISION_PAIR_EDGES', repr(a), repr(b))
    print('ONE_TYPES', 160)
    print('TWO_TYPES', 160**2 + 8649)
    print('TWO_ADJACENCY_TYPES', 8649)
    print('TRIPLE_PATH_CONTRIBUTIONS', p1[2], p2[2])
    print('THREE_TYPES', *arity_three)
    for edges, (i,d,j) in zip((a,b),(p1,p2)):
        assert independently_count_triples(edges,10,[]) == i**3
        assert independently_count_triples(edges,10,[(0,1)]) == i*d
        assert independently_count_triples(edges,10,[(0,1),(1,2)]) == j
    print('DIRECT_TRIPLE_EXTENSION_CHECKS_PASS', 6)
    print('ALL_TESTS_PASS')
    return all_last, [(a,p1),(b,p2)]

if __name__ == '__main__':
    main()
