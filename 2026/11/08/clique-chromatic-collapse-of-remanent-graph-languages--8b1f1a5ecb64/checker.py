"""Auxiliary finite checks for signed-walk remanence and clique--chromatic collapse.
All algorithms are exact (integer bitsets and exhaustive finite-state searches).
They supplement, not replace, the all-parameter mathematical proof.
"""
from itertools import combinations
from collections import deque
import random
from math import factorial


def language_contains_run_bound(n, arcs, k):
    """Check L_k subset language of the oriented n-vertex graph (exact DFA product)."""
    masks = [[], []]
    for u, v in arcs:
        masks[0].append((u, v))
        masks[1].append((v, u))
    trans = [[0] * n for _ in range(2)]
    for c in (0, 1):
        for u, v in masks[c]:
            trans[c][u] |= 1 << v
    start = ((1 << n) - 1, 2, 0)  # last letter=2 means no letter yet
    queue = deque([start])
    seen = {start}
    while queue:
        subset, last, length = queue.popleft()
        if subset == 0:
            return False
        for letter in (0, 1):
            new_len = length + 1 if last == letter else 1
            if new_len >= k:
                continue
            image = 0
            for vertex in range(n):
                if (subset >> vertex) & 1:
                    image |= trans[letter][vertex]
            state = (image, letter, new_len)
            if state not in seen:
                seen.add(state)
                queue.append(state)
    return True


def tournament_arcs(k, mask):
    arcs = []
    bit = 0
    for i in range(k):
        for j in range(i + 1, k):
            arcs.append((j, i) if (mask >> bit) & 1 else (i, j))
            bit += 1
    return arcs


def has_directed_triangle(k, arcs):
    a = set(arcs)
    for i, j, t in combinations(range(k), 3):
        if ((i, j) in a and (j, t) in a and (t, i) in a) or (
            (j, i) in a and (t, j) in a and (i, t) in a
        ):
            return True
    return False


def chromatic(n, undirected):
    adj = [0] * n
    for a, b in undirected:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    for k in range(1, n + 1):
        colors = [-1] * n
        def dfs(i):
            if i == n:
                return colors[:]
            for c in range(k):
                if all(colors[j] != c for j in range(i) if adj[i] >> j & 1):
                    colors[i] = c
                    result = dfs(i + 1)
                    if result is not None:
                        return result
            colors[i] = -1
            return None
        result = dfs(0)
        if result is not None:
            return k, result
    raise AssertionError


def clique_number(n, undirected):
    e = {tuple(sorted(pair)) for pair in undirected}
    for k in range(n, 0, -1):
        if any(all((i, j) in e for i, j in combinations(t, 2)) for t in combinations(range(n), k)):
            return k
    return 0


def graph_arcs(undirected, orientation):
    return [(v, u) if (orientation >> bit) & 1 else (u, v)
            for bit, (u, v) in enumerate(undirected)]


def check():
    tournament_count = 0
    for k in range(1, 6):
        transitive_count = 0
        for mask in range(1 << (k * (k-1) // 2)):
            arcs = tournament_arcs(k, mask)
            assert language_contains_run_bound(k, arcs, k)
            transitive_count += not has_directed_triangle(k, arcs)
            tournament_count += 1
        assert transitive_count == factorial(k)
    assert tournament_count == 1099  # 1+2+8+64+1024

    # Every weakly-perfect graph on <=4 labeled vertices, every orientation.
    oriented_cases = 0
    for n in range(1, 5):
        all_edges = list(combinations(range(n), 2))
        for graph_mask in range(1 << len(all_edges)):
            edges = [edge for bit, edge in enumerate(all_edges) if graph_mask >> bit & 1]
            k, coloring = chromatic(n, edges)
            if clique_number(n, edges) != k:
                continue
            for orientation in range(1 << len(edges)):
                assert language_contains_run_bound(n, graph_arcs(edges, orientation), k)
                oriented_cases += 1
            # The orientation by colors is a direct all-parameter equality witness.
            ordered_arcs = [(u, v) if coloring[u] < coloring[v] else (v, u)
                            for u, v in edges]
            assert language_contains_run_bound(n, ordered_arcs, k)
    assert oriented_cases > 0

    # Random checks for larger weakly-perfect examples via arbitrary complete k-partite graphs.
    rng = random.Random(1711)
    random_count = 0
    for _ in range(400):
        n = rng.randrange(5, 10)
        k = rng.randrange(2, min(6, n+1))
        classes = list(range(k)) + [rng.randrange(k) for _ in range(n-k)]
        rng.shuffle(classes)
        edges = [(u, v) for u, v in combinations(range(n), 2) if classes[u] != classes[v]]
        arcs = graph_arcs(edges, rng.getrandbits(len(edges)))
        assert language_contains_run_bound(n, arcs, k)
        random_count += 1
    print(f'CHECKS_OK tournaments={tournament_count}, oriented_small_graphs={oriented_cases}, random_multipartite_orientations={random_count}')

if __name__ == '__main__':
    check()
