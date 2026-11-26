#!/usr/bin/env python3
"""Finite, exact certificate for the five-site random-majority class theorem.

Uses only the Python 3 standard library. All graph and opinion states
are bit masks, and transition support is computed by integer comparisons.
"""

from collections import Counter, defaultdict
from itertools import permutations


def edge_list(n):
    return [(a, b) for a in range(n) for b in range(a + 1, n)]


def adjacency(n, graph_bits):
    neighbor = [0] * n
    for k, (a, b) in enumerate(edge_list(n)):
        if graph_bits & (1 << k):
            neighbor[a] |= 1 << b
            neighbor[b] |= 1 << a
    return neighbor


def connected(neighbor):
    seen = 1
    while True:
        new = seen
        for i, mask in enumerate(neighbor):
            if seen & (1 << i):
                new |= mask
        if new == seen:
            return seen == (1 << len(neighbor)) - 1
        seen = new


def support_by_tie_subsets(neighbor):
    n = len(neighbor)
    support = []
    for state in range(1 << n):
        ones, tied = 0, 0
        for i, nbrs in enumerate(neighbor):
            blue = (state & nbrs).bit_count()
            white = nbrs.bit_count() - blue
            if blue > white:
                ones |= 1 << i
            if blue == white:
                tied |= 1 << i
        successors = set()
        sub = tied
        while True:
            successors.add(ones | sub)
            if sub == 0:
                break
            sub = (sub - 1) & tied
        support.append(successors)
    return support


def support_by_pairwise_test(neighbor):
    """Independently test every source/target coloring pair."""
    n = len(neighbor)
    out = []
    for source in range(1 << n):
        possible = set()
        for target in range(1 << n):
            ok = True
            for i, nbrs in enumerate(neighbor):
                blue = (source & nbrs).bit_count()
                white = nbrs.bit_count() - blue
                target_blue = (target >> i) & 1
                if (blue > white and not target_blue) or (blue < white and target_blue):
                    ok = False
                    break
            if ok:
                possible.add(target)
        out.append(possible)
    return out


def terminal_components_by_closure(support):
    """Independent Floyd-Warshall Boolean transitive closure."""
    q = len(support)
    reach = [sum(1 << t for t in targets) | (1 << s)
             for s, targets in enumerate(support)]
    for mid in range(q):
        bit = 1 << mid
        row = reach[mid]
        for s in range(q):
            if reach[s] & bit:
                reach[s] |= row
    unassigned = set(range(q))
    comps = []
    while unassigned:
        state = min(unassigned)
        comp = frozenset(t for t in unassigned
                         if ((reach[state] >> t) & 1)
                         and ((reach[t] >> state) & 1))
        unassigned.difference_update(comp)
        if all(t in comp for s in comp for t in support[s]):
            comps.append(comp)
    return frozenset(comps)


def terminal_components_by_dfs(support):
    """Independent Kosaraju decomposition of the support digraph."""
    q = len(support)
    backward = [set() for _ in range(q)]
    for s, targets in enumerate(support):
        for t in targets:
            backward[t].add(s)
    marked, finishing = set(), []

    def first(v):
        marked.add(v)
        for w in sorted(support[v]):
            if w not in marked:
                first(w)
        finishing.append(v)

    for v in range(q):
        if v not in marked:
            first(v)
    marked.clear()
    terminal = []

    def second(v, component):
        marked.add(v)
        component.add(v)
        for w in sorted(backward[v]):
            if w not in marked:
                second(w, component)

    for v in reversed(finishing):
        if v not in marked:
            component = set()
            second(v, component)
            if all(t in component for s in component for t in support[s]):
                terminal.append(frozenset(component))
    return frozenset(terminal)


def canonical_mask(n, graph_bits):
    edges = edge_list(n)
    source_edges = {p for k, p in enumerate(edges)
                    if graph_bits & (1 << k)}
    best = (1 << len(edges)) - 1
    for p in permutations(range(n)):
        transformed = 0
        for k, (a, b) in enumerate(edges):
            if tuple(sorted((p[a], p[b]))) in source_edges:
                transformed |= 1 << k
        best = min(best, transformed)
    return best


def classify():
    expected = {
        2: (1, {2: 1}),
        3: (4, {1: 1, 2: 3}),
        4: (38, {1: 12, 2: 26}),
        5: (728, {1: 188, 2: 405, 4: 135}),
    }
    large_classes = Counter()
    classes_by_shape = Counter()
    for n in range(2, 6):
        num_connected = 0
        size_distribution = Counter()
        for mask in range(1 << len(edge_list(n))):
            neighbor = adjacency(n, mask)
            if not connected(neighbor):
                continue
            num_connected += 1
            support1 = support_by_tie_subsets(neighbor)
            support2 = support_by_pairwise_test(neighbor)
            assert support1 == support2, ('transition support', n, mask)
            c1 = terminal_components_by_closure(support1)
            c2 = terminal_components_by_dfs(support2)
            assert c1 == c2, ('terminal components', n, mask)
            maximum = max(map(len, c1))
            size_distribution[maximum] += 1
            if maximum > 2:
                assert n == 5 and maximum == 4
                assert sum(len(c) == 4 for c in c1) == 1
                large_classes[canonical_mask(n, mask)] += 1
                classes_by_shape[tuple(sorted(map(len, c1)))] += 1
        assert (num_connected, dict(size_distribution)) == expected[n]
        print('n=%d connected_labeled=%d max_terminal_sizes=%s' %
              (n, num_connected, dict(sorted(size_distribution.items()))))
    expected_orbits = {59: 60, 221: 60, 495: 15}
    assert dict(large_classes) == expected_orbits, large_classes
    assert dict(classes_by_shape) == {(1, 1, 2, 4): 60,
                                       (1, 1, 4): 75}
    print('exceptional_canonical_masks=', dict(sorted(large_classes.items())))
    print('exceptional_terminal_shapes=', dict(sorted(classes_by_shape.items())))
    for canonical, orbit in sorted(large_classes.items()):
        n = 5
        nbrs = adjacency(n, canonical)
        c = [part for part in terminal_components_by_dfs(
             support_by_tie_subsets(nbrs)) if len(part) == 4]
        assert len(c) == 1
        print('canonical=%d orbit=%d edges=%s size4_class=%s' %
              (canonical, orbit,
               [edge for k, edge in enumerate(edge_list(n))
                if canonical & (1 << k)], sorted(c[0])))
    print('ALL EXACT CHECKS PASSED')


if __name__ == '__main__':
    classify()
