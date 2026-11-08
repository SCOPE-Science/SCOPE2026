#!/usr/bin/env python3
"""Finite checks for cycle-bouquet logic; standard library only.

These are finite corroborations, not proofs of unrestricted quantifier depth.
"""
from collections import Counter
from itertools import combinations_with_replacement, product


def bouquet(lengths):
    assert len(lengths) >= 2 and all(n >= 3 for n in lengths)
    edges = set()
    next_v = 1
    for n in lengths:
        path = list(range(next_v, next_v + n - 1))
        next_v += n - 1
        for x, y in zip(path, path[1:]):
            edges.add(tuple(sorted((x, y))))
        for x in (path[0], path[-1]):
            edges.add((0, x))
    return next_v, frozenset(edges)


def extract_cycle_lengths(graph):
    n, edges = graph
    adj = [set() for _ in range(n)]
    for x, y in edges:
        adj[x].add(y)
        adj[y].add(x)
    hub = [x for x in range(n) if len(adj[x]) >= 3]
    assert len(hub) == 1
    hub = hub[0]
    lengths = []
    unseen = set(range(n)) - {hub}
    while unseen:
        start = min(unseen)
        todo = [start]
        comp = {start}
        while todo:
            x = todo.pop()
            for y in adj[x]:
                if y != hub and y not in comp:
                    comp.add(y)
                    todo.append(y)
        unseen -= comp
        assert len([x for x in comp if hub in adj[x]]) == 2
        assert sum(len(adj[x] - {hub}) for x in comp) == 2 * (len(comp) - 1)
        lengths.append(len(comp) + 1)
    return tuple(sorted(lengths))


def color_refinement_equiv(a_graph, b_graph, k, maximum_rounds=80):
    """Complete finite k-pebble game via counting-free tuple refinement.

    All variables can be unassigned. The tuple color is refined using sets,
    rather than multisets, of replacement colors (no counting quantifiers).
    """
    graphs = (a_graph, b_graph)
    states = []
    atoms = []
    empty_positions = []
    for graph_index, (n, edges) in enumerate(graphs):
        for t in product(range(n + 1), repeat=k):
            states.append((graph_index, t))
            sig = [tuple(i for i, x in enumerate(t) if x == n)]
            for i in range(k):
                for j in range(i + 1, k):
                    if t[i] == n or t[j] == n:
                        continue
                    sig.append((i, j, t[i] == t[j],
                                tuple(sorted((t[i], t[j]))) in edges))
            atoms.append(tuple(sig))
        empty_positions.append(len(states) - 1)
    lookup = {}
    old = []
    for a in atoms:
        if a not in lookup:
            lookup[a] = len(lookup)
        old.append(lookup[a])
    for depth in range(maximum_rounds):
        replacements = [dict() for _ in range(k)]
        for p, (g, t) in enumerate(states):
            for i in range(k):
                key = (g, t[:i] + t[i + 1:])
                replacements[i].setdefault(key, set()).add(old[p])
        replacements = [{key: frozenset(vals) for key, vals in d.items()}
                        for d in replacements]
        lookup = {}
        new = []
        for p, (g, t) in enumerate(states):
            s = (old[p], tuple(replacements[i][(g, t[:i] + t[i + 1:])]
                               for i in range(k)))
            if s not in lookup:
                lookup[s] = len(lookup)
            new.append(lookup[s])
        if len(lookup) == len(set(old)):
            return (new[empty_positions[0]] == new[empty_positions[1]], depth + 1)
        old = new
    raise RuntimeError("color refinement did not stabilize")


def clipped_profile(lengths, k):
    return tuple(sorted((n, min(k, count)) for n, count in Counter(lengths).items()))


def verify():
    structural = 0
    for r in (2, 3, 4):
        for ls in combinations_with_replacement(range(3, 8), r):
            n, edges = bouquet(ls)
            if n > 18:
                continue
            assert extract_cycle_lengths((n, edges)) == ls
            structural += 1
    print("structural_instances", structural)

    tests = [
        (4, (3, 3), (3, 3, 3)),
        (4, (3, 3, 3), (3, 3, 3, 3)),
        (4, (3, 3, 3, 3), (3, 3, 3, 3, 3)),
        (4, (3, 4), (4, 3)),
        (4, (3, 4), (3, 5)),
        (4, (3, 4), (4, 4)),
        (4, (3, 3, 4), (3, 4, 4)),
        (4, (3, 4, 5), (3, 5, 4)),
        (4, (3, 4, 5), (3, 4, 6)),
        (4, (4, 4), (4, 4, 4)),
        (4, (3, 3, 4), (3, 3, 5)),
        (3, (3, 3, 3), (3, 3, 3, 3)),
        (3, (4, 4, 4), (4, 4, 4, 4)),
    ]
    for k, a, b in tests:
        actual, steps = color_refinement_equiv(bouquet(a), bouquet(b), k)
        predicted = clipped_profile(a, k) == clipped_profile(b, k)
        assert actual == predicted, (k, a, b, actual, predicted)
        print("pebble_test", "k=" + str(k), "a=" + str(a), "b=" + str(b),
              "equivalent=" + str(actual), "rounds=" + str(steps))
    for k in (4, 5, 6):
        for number_of_lengths in range(1, 5):
            observed = sum(sum(x) >= 2 for x in product(range(k + 1), repeat=number_of_lengths))
            predicted = (k + 1) ** number_of_lengths - number_of_lengths - 1
            assert observed == predicted
            print("theory_count", "k=" + str(k), "lengths=" + str(number_of_lengths),
                  "count=" + str(observed))
    print("ALL_FINITE_CHECKS_PASSED")

if __name__ == '__main__':
    verify()
