"""Independent, standard-library validation of finite ladder-cycle trace claims.

Usage: python3 verify_ladder_cycles.py [ladder_n5_tree.json]
The universal statements in RESULT.md have separate proofs; these are finite tests.
"""
import itertools
import json
import math
import sys
from functools import lru_cache
from pathlib import Path


def graph(n):
    vertices = [(layer, col) for layer in range(2) for col in range(1, n + 1)]
    edges = [('r', col) for col in range(1, n + 1)]
    edges += [('t', col) for col in range(1, n)]
    edges += [('b', col) for col in range(1, n)]
    E = {}
    for label in edges:
        typ, col = label
        if typ == 'r':
            a, b = (0, col), (1, col)
        else:
            layer = 0 if typ == 't' else 1
            a, b = (layer, col), (layer, col + 1)
        E[frozenset((a, b))] = label
    adj = {v: set() for v in vertices}
    for endpoints in E:
        a, b = tuple(endpoints)
        adj[a].add(b)
        adj[b].add(a)
    return vertices, edges, E, adj


def actual_cycles(n):
    V, labels, E, adj = graph(n)
    cycles = set()
    for root in V:
        def dfs(path, used):
            end = path[-1]
            for nxt in adj[end]:
                if nxt == root and len(path) >= 4:
                    verts = path + [root]
                    edges = frozenset(E[frozenset((a, b))]
                                      for a, b in zip(verts, verts[1:]))
                    cycles.add(edges)
                elif nxt not in used and len(path) < len(V):
                    dfs(path + [nxt], used | {nxt})
        dfs([root], {root})
    return labels, cycles


def formula_cycles(n):
    return {frozenset([('r', i), ('r', j)] +
                      [(layer, k) for layer in ('t', 'b')
                       for k in range(i, j)])
            for i in range(1, n + 1) for j in range(i + 1, n + 1)}


def expected_shattered(n, S):
    if len(S) == 0:
        return True
    if n == 2:
        return False
    if len(S) == 1:
        return True
    if n == 3 or len(S) > 2:
        return False
    a, b = S
    if a[0] in 'tb' and b[0] in 'tb' and a[1] == b[1]:
        return False
    for x, y in ((a, b), (b, a)):
        if x[0] == 'r' and y[0] in 'tb':
            if (x[1], y[1]) in ((1, 1), (n, n - 1)):
                return False
    return True


def shattered(cycles, S):
    traces = {sum((edge in cycle) << k for k, edge in enumerate(S))
              for cycle in cycles}
    return len(traces) == (1 << len(S))


def ldim(labels, cycles):
    seq = list(cycles)
    all_bits = (1 << len(seq)) - 1
    queries = [sum((1 << i) for i, c in enumerate(seq) if e in c)
               for e in labels]
    @lru_cache(None)
    def solve(subset):
        out = 0
        for mask in queries:
            positive = subset & mask
            negative = subset & ~mask
            if positive and negative:
                val = 1 + min(solve(positive), solve(negative))
                out = max(out, val)
        return out
    return solve(all_bits)


def verify_tree(n, tree):
    edges, cycles = actual_cycles(n)
    leaves = []
    def descend(node, answers):
        if 'cycle' in node:
            i, j = node['cycle']
            C = frozenset([('r', i), ('r', j)] +
                          [(layer, k) for layer in ('t', 'b')
                           for k in range(i, j)])
            assert C in cycles
            assert all((edge in C) == answer for edge, answer in answers)
            leaves.append(tuple(node['cycle']))
            return 0
        name = node['query']
        edge = (name[0], int(name[1:]))
        assert edge in edges
        assert edge not in [e for e, _ in answers]
        d0 = descend(node['zero'], answers + [(edge, False)])
        d1 = descend(node['one'], answers + [(edge, True)])
        assert d0 == d1
        return d0 + 1
    depth = descend(tree, [])
    assert len(leaves) == (1 << depth)
    assert len(set(leaves)) == len(leaves)
    return depth, len(leaves)


def main():
    totals = []
    trace_count = 0
    for n in range(2, 10):
        edges, by_graph = actual_cycles(n)
        assert by_graph == formula_cycles(n), ('cycle representation', n)
        counts = [0, 0, 0, 0]
        for k in range(4):
            for S in itertools.combinations(edges, k):
                predicted = expected_shattered(n, S)
                observed = shattered(by_graph, S)
                assert predicted == observed, (n, S, predicted, observed)
                counts[k] += int(observed)
                trace_count += 1
        target = [1, 0, 0, 0] if n == 2 else [1, 7, 0, 0] if n == 3 else [1, 3*n-2, n*(9*n-17)//2, 0]
        assert counts == target, (n, counts, target)
        totals.append((n, len(by_graph), counts))
    ranks = {}
    for n in range(2, 13):
        edges, cycles = actual_cycles(n) if n <= 9 else (graph(n)[1], formula_cycles(n))
        ranks[n] = ldim(edges, cycles)
        lower = 2*int(math.log2(n//2)) if n >= 4 else 0
        upper = int(math.log2(math.comb(n, 2)))
        assert lower <= ranks[n] <= upper, (n, ranks[n], lower, upper)
    assert ranks == {2: 0, 3: 1, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 4, 10: 5, 11: 5, 12: 5}, ranks
    tree_path = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('ladder_n5_tree.json')
    depth, leaves = verify_tree(5, json.loads(tree_path.read_text(encoding='utf8')))
    assert (depth, leaves) == (3, 8)
    print('LADDER_CYCLE_TRACE_CHECK_PASS')
    print('graph_cycle_instances=2..9; total_support_comparisons=', trace_count)
    print('cycle_count_and_coefficients=', totals)
    print('exact_online_ranks_2_through_12=', ranks)
    print('five_rung_online_certificate_depth=', depth, 'distinct_leaves=', leaves)

if __name__ == '__main__':
    main()
