#!/usr/bin/env python3
"""Independent finite tests for the subdivision connected-cover enumerator.

Runs using only the Python standard library. Recomputes cover and connectivity
from the subdivided edge list, without using a graph package.
"""
from itertools import combinations
from collections import Counter


def connected(selected, adj):
    if not selected:
        return False
    reached = selected & -selected
    while True:
        nxt = reached
        for i, neigh in enumerate(adj):
            if (reached >> i) & 1:
                nxt |= neigh & selected
        if nxt == reached:
            return nxt == selected
        reached = nxt


def corona_edges(n, edges):
    """The edge list of the one-subdivision, with original vertices 0,...,n-1."""
    return [(u, n + k) for k, (u, v) in enumerate(edges)] + [
        (v, n + k) for k, (u, v) in enumerate(edges)
    ]


def masks_graph(n, edges):
    size = n + len(edges)
    adj = [0] * size
    hyperedges = corona_edges(n, edges)
    for u, v in hyperedges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj, [(1 << u) | (1 << v) for u, v in hyperedges]


def is_cover(mask, edge_masks):
    return all(mask & e for e in edge_masks)


def exhaustive_minimal(n, edges):
    adj, edge_masks = masks_graph(n, edges)
    ans = Counter()
    masks = set()
    examined = 0
    for mask in range(1, 1 << len(adj)):
        examined += 1
        if not is_cover(mask, edge_masks) or not connected(mask, adj):
            continue
        if any(is_cover(mask ^ bit, edge_masks) and connected(mask ^ bit, adj)
               for bit in (1 << j for j in range(len(adj)) if mask >> j & 1)):
            continue
        masks.add(mask)
        ans[mask.bit_count()] += 1
    return masks, ans, examined


def forest_is_tree(U, t_edges):
    if len(t_edges) != len(U) - 1:
        return False
    if len(U) <= 1:
        return True
    adjacency = {x: set() for x in U}
    for u, v in t_edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    todo = [next(iter(U))]
    visited = set(todo)
    while todo:
        u = todo.pop()
        for w in adjacency[u]:
            if w not in visited:
                visited.add(w)
                todo.append(w)
    return len(visited) == len(U)


def predicted_minimal(n, edges):
    answers = set()
    vertex_universe = set(range(n))
    for umask in range(1, 1 << n):
        U = {v for v in range(n) if umask >> v & 1}
        if any(u not in U and v not in U for u, v in edges):
            continue
        internals = [j for j, (u, v) in enumerate(edges) if u in U and v in U]
        crossings = [j for j, (u, v) in enumerate(edges) if (u in U) != (v in U)]
        selected_originals = sum(1 << v for v in U)
        selected_forced = sum(1 << (n + j) for j in crossings)
        for comb in combinations(internals, len(U)-1):
            if forest_is_tree(U, [edges[j] for j in comb]):
                mask = selected_originals | selected_forced
                for j in comb:
                    mask |= 1 << (n + j)
                answers.add(mask)
    return answers


def viable_original_graph(n, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return all(a.bit_count() >= 2 for a in adj) and connected((1 << n)-1,adj)


def run():
    total_graphs = total_masks = total_minimals = 0
    base_masks = 0
    bip_masks = 0
    by_n = {}
    for n in range(3, 6):
        all_edges = list(combinations(range(n), 2))
        checked = 0
        for e_mask in range(1 << len(all_edges)):
            ed = [e for j, e in enumerate(all_edges) if e_mask >> j & 1]
            if not viable_original_graph(n, ed):
                continue
            brute, actual, examined = exhaustive_minimal(n, ed)
            predicted = predicted_minimal(n, ed)
            assert brute == predicted, (n, ed, brute ^ predicted)
            checked += 1
            total_masks += examined
            base_masks += examined
            total_minimals += len(brute)
        total_graphs += checked
        by_n[n] = checked
    # A parameterized specialization with a growing cardinality gap.
    specialized = {}
    for right in range(2, 7):
        n = 2 + right
        ed = [(a, b) for a in range(2) for b in range(2, n)]
        if right <= 5:
            brute, poly, examined = exhaustive_minimal(n, ed)
            total_masks += examined
            bip_masks += examined
            expected = Counter()
            expected[2*right + 3] += right * 3**(right-1)
            expected[3*right + 1] += 2
            assert poly == expected, (right, poly, expected)
            assert brute == predicted_minimal(n, ed)
            specialized[right] = dict(poly)
        else:
            pred = predicted_minimal(n, ed)
            poly = Counter(x.bit_count() for x in pred)
            expected = Counter({2*right+3: right * 3**(right-1),
                                3*right+1: 2})
            assert poly == expected, (right, poly, expected)
            specialized[right] = dict(poly)
    print('VERIFY_OK', 'all_labeled_graphs_by_order='+str(by_n),
          'graphs='+str(total_graphs), 'base_examined_subsets='+str(base_masks),
          'bipartite_examined_subsets='+str(bip_masks), 'total_examined_subsets='+str(total_masks),
          'minimal_sets='+str(total_minimals), 'exact_family=PASS',
          'bipartite_specialization=PASS')
    print('K2,n coefficients:',specialized)


if __name__ == '__main__':
    run()
