#!/usr/bin/env python3
"""Independent finite FO^k tuple-type refinement for threshold graphs.

No external modules are required. For a finite collection of structures, the
stable substitution signatures of all k-tuples encode their complete
counting-free k-variable types. Sets of such tuple types determine sentences.
This checks finite instances only; the unlimited theorem needs the proof.
"""
from itertools import product
from collections import defaultdict
import json


def threshold_graph(code):
    n = 1 + len(code)
    adjacency = [[False] * n for _ in range(n)]
    for i, bit in enumerate(code, start=1):
        if bit:
            for j in range(i):
                adjacency[i][j] = adjacency[j][i] = True
    return adjacency


def canonical_peeling(adj):
    rest = tuple(range(len(adj)))
    result = []
    while rest:
        if len(rest) == 1:
            assert not result  # a canonical threshold graph never ends with a singleton
            return (("singleton", 1),)
        universal = tuple(v for v in rest if all(v == w or adj[v][w] for w in rest))
        isolated = tuple(v for v in rest if all(v == w or not adj[v][w] for w in rest))
        assert bool(universal) != bool(isolated)
        tag = "U" if universal else "I"
        block = universal if universal else isolated
        result.append((tag, len(block)))
        rest = tuple(v for v in rest if v not in block)
    assert result[-1][1] >= 2
    assert all(result[i][0] != result[i + 1][0] for i in range(len(result) - 1))
    return tuple(result)


def fo_k_sentence_types(graphs, k):
    state_to_index = {}
    states = []
    graph_ranges = []
    keys = {}
    initial_colors = []
    for g, graph in enumerate(graphs):
        start = len(states)
        for vertices in product(range(len(graph)), repeat=k):
            state_to_index[(g, vertices)] = len(states)
            states.append((g, vertices))
            atom = tuple((vertices[i] == vertices[j], bool(graph[vertices[i]][vertices[j]]))
                         for i in range(k) for j in range(i + 1, k))
            if atom not in keys:
                keys[atom] = len(keys)
            initial_colors.append(keys[atom])
        graph_ranges.append((start, len(states)))
    colors = initial_colors
    rounds = 0
    while True:
        new_colors = []
        lookup = {}
        for g, v in states:
            sig = [colors[state_to_index[(g, v)]]]
            n = len(graphs[g])
            for p in range(k):
                available = {colors[state_to_index[(g, v[:p] + (u,) + v[p+1:])]]
                             for u in range(n)}
                sig.append(tuple(sorted(available)))
            sig = tuple(sig)
            if sig not in lookup:
                lookup[sig] = len(lookup)
            new_colors.append(lookup[sig])
        rounds += 1
        if colors == new_colors:
            break
        assert rounds <= len(states), "partition refinement did not stabilize"
        colors = new_colors
    types = [frozenset(colors[lo:hi]) for lo, hi in graph_ranges]
    return types, rounds, len(set(colors)), len(states)


def test(k, max_order):
    graphs = []
    expected = []
    for n in range(1, max_order + 1):
        for code in product((0, 1), repeat=n - 1):
            graph = threshold_graph(code)
            blocks = canonical_peeling(graph)
            graphs.append(graph)
            expected.append(tuple((tag, min(size, k)) for tag, size in blocks))
    observed, rounds, tuple_colors, tuple_states = fo_k_sentence_types(graphs, k)
    forward = defaultdict(set)
    backward = defaultdict(set)
    for prediction, measured in zip(expected, observed):
        forward[prediction].add(measured)
        backward[measured].add(prediction)
    assert all(len(values) == 1 for values in forward.values()), "predicted equal classes split"
    assert all(len(values) == 1 for values in backward.values()), "predicted different classes merged"
    return {"k": k, "max_order": max_order, "graphs": len(graphs),
            "tuple_states": tuple_states, "iterations": rounds,
            "tuple_colors": tuple_colors,
            "predicted_classes": len(forward),
            "logical_classes": len(backward), "discrepancies": 0}


def main():
    results = [test(2, 7), test(3, 6), test(4, 5)]
    print(json.dumps({"method": "independent_fixed_point_k_tuple_refinement",
                      "checks": results, "result": "PASS"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
