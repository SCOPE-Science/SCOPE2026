#!/usr/bin/env python3
"""Direct reproducibility checks for two-token cycle edge partitions and cuts."""
from itertools import combinations


def token_graph(n):
    vertices = list(combinations(range(n), 2))
    index = {v: i for i, v in enumerate(vertices)}
    edges = set()
    for i, tokens in enumerate(vertices):
        for moved in tokens:
            for destination in ((moved - 1) % n, (moved + 1) % n):
                if destination not in tokens:
                    other = tuple(sorted((set(tokens) - {moved}) | {destination}))
                    edges.add(tuple(sorted((i, index[other]))))
    return vertices, edges


def candidate_cycles(n):
    for j in range(1, n - 1):
        path = [(j, n - 1), (j - 1, n - 1)]
        path += [(j - 1, b) for b in range(n - 2, j - 1, -1)]
        path += [(a, j) for a in range(j - 2, -1, -1)]
        yield path


def validate_partition(n):
    vertices, edges = token_graph(n)
    index = {v: i for i, v in enumerate(vertices)}
    used = set()
    for cycle in candidate_cycles(n):
        assert len(cycle) == n and len(set(cycle)) == n
        for u, v in zip(cycle, cycle[1:] + cycle[:1]):
            edge = tuple(sorted((index[u], index[v])))
            assert edge in edges and edge not in used
            used.add(edge)
    assert used == edges and len(edges) == n * (n - 2)
    parity = [sum(x % 2 for x in tokens) % 2 for tokens in vertices]
    lifted = sum(parity[a] != parity[b] for a, b in edges)
    assert lifted == (n - 2) * (n - n % 2)
    return vertices, edges


def validate_brute_max_cut(n):
    vertices, edges = token_graph(n)
    adj = [[] for _ in vertices]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    bits = [0] * len(vertices)
    current = 0
    best = 0
    for step in range(1 << (len(vertices) - 1)):
        if step:
            bit = (step & -step).bit_length()
            old = bits[bit]
            bits[bit] ^= 1
            current += sum(1 if bits[u] == old else -1 for u in adj[bit])
        if current > best:
            best = current
    expected = (n - 2) * (n - n % 2)
    assert best == expected, (n, best, expected)
    print("EXHAUSTIVE_MAX_CUT_PASS", n, len(vertices), len(edges), best)


def main():
    for n in range(3, 151):
        validate_partition(n)
    print("DIRECT_EDGE_PARTITION_AND_PARITY_CUT_PASS n=3..150")
    for n in range(3, 8):
        validate_brute_max_cut(n)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
