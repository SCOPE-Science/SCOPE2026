"""Exact finite diagnostics for noisy rooted event-tree covariance signatures.

Uses only Python's standard library. These finite checks are not proofs of
claims involving every tree size, noise parameter or sample size.
"""
from collections import deque
from fractions import Fraction as Q
from heapq import heapify, heappop, heappush
from itertools import product


def prufer_edges(n, code):
    degree = [1] * n
    for x in code:
        degree[x] += 1
    heap = [v for v in range(n) if degree[v] == 1]
    heapify(heap)
    edges = []
    for v in code:
        u = heappop(heap)
        edges.append((u, v))
        degree[u] -= 1
        degree[v] -= 1
        if degree[v] == 1:
            heappush(heap, v)
    edges.append((heappop(heap), heappop(heap)))
    return edges


def root_tree(n, edges, root):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    parent = {}
    queue = deque([root]); seen = {root}
    while queue:
        u = queue.popleft()
        for v in sorted(adj[u] - seen):
            seen.add(v); parent[v] = u; queue.append(v)
    assert len(seen) == n
    return parent


def connected_parts(nodes, graph):
    nodes = set(nodes)
    parts = []
    while nodes:
        seed = min(nodes); nodes.remove(seed)
        part = {seed}; stack = [seed]
        while stack:
            u = stack.pop()
            for v in graph[u] & nodes:
                nodes.remove(v); part.add(v); stack.append(v)
        parts.append(part)
    return parts


def reconstruct_quotient(events, graph):
    classes = []
    membership = {}
    for e in sorted(events):
        if e in membership:
            continue
        cl = frozenset(u for u in events if (graph[e] | {e}) == (graph[u] | {u}))
        c = len(classes)
        classes.append(cl)
        for x in cl:
            membership[x] = c
    qgraph = {i: set() for i in range(len(classes))}
    for i in qgraph:
        representative = min(classes[i])
        for j in qgraph:
            if i != j and min(classes[j]) in graph[representative]:
                qgraph[i].add(j)
    recovered_parent = {}

    def rec(nodes, ancestor):
        for part in connected_parts(nodes, qgraph):
            universal = [u for u in part if len(qgraph[u] & part) == len(part) - 1]
            assert len(universal) == 1, (classes, qgraph, part)
            root = universal[0]
            recovered_parent[root] = ancestor
            rec(part - {root}, root)

    rec(qgraph, None)
    return classes, membership, recovered_parent


def run():
    structures = 0
    checked_pairs = 0
    for n in range(2, 7):
        for code in product(range(n), repeat=n - 2):
            edges = prufer_edges(n, code)
            for root in range(n):
                parent = root_tree(n, edges, root)
                events = set(parent)
                ancestors = {}
                for e in events:
                    anc = set(); u = e
                    while u != root:
                        anc.add(u); u = parent[u]
                    ancestors[e] = anc
                descendant = {e: set(z for z in range(n) if e in ancestors.get(z, set())) for e in events}
                weights = {z: Q(z + 1, n * (n + 1) // 2) for z in range(n)}
                p = {e: sum((weights[z] for z in descendant[e]), Q(0)) for e in events}
                false_positive = {e: Q(e % 5 + 1, 20) for e in events}
                true_positive = {e: false_positive[e] + Q(e % 3 + 1, 5) for e in events}
                slopes = {e: true_positive[e] - false_positive[e] for e in events}
                positive_graph = {e: set() for e in events}
                for e in sorted(events):
                    for f in sorted(events):
                        if e >= f:
                            continue
                        intersection = sum((weights[z] for z in descendant[e] & descendant[f]), Q(0))
                        latent_cov = intersection - p[e] * p[f]
                        observed_cov = slopes[e] * slopes[f] * latent_cov
                        comparable = (e in ancestors[f] or f in ancestors[e])
                        assert observed_cov != 0
                        assert (observed_cov > 0) == comparable
                        if observed_cov > 0:
                            positive_graph[e].add(f)
                            positive_graph[f].add(e)
                        checked_pairs += 1

                classes, membership, recovered_parent = reconstruct_quotient(events, positive_graph)
                for cid, cl in enumerate(classes):
                    predicted_parent = []
                    for e in cl:
                        u = parent[e]
                        while u != root and membership[u] == cid:
                            u = parent[u]
                        predicted_parent.append(None if u == root else membership[u])
                    assert len(set(predicted_parent)) == 1
                    assert predicted_parent[0] == recovered_parent[cid]
                structures += 1
    assert structures == 8476, structures
    print('PASS: exact rooted tree structures =', structures)
    print('PASS: pairwise rational covariance sign checks =', checked_pairs)
    print('PASS: true-twin quotient reconstruction for every structure')


if __name__ == '__main__':
    run()
