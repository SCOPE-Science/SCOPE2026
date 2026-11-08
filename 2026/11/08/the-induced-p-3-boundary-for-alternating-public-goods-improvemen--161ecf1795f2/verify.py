#!/usr/bin/env python3
"""Independent finite checks for the parity best-response graph theorem.
Usage: python3 verify.py. Requires only the Python standard library.
"""
from itertools import combinations


def neighborhoods(n, edge_mask):
    adj = [0] * n
    for k, (a, b) in enumerate(combinations(range(n), 2)):
        if edge_mask & (1 << k):
            adj[a] |= 1 << b
            adj[b] |= 1 << a
    return adj


def components(adj):
    unseen = (1 << len(adj)) - 1
    blocks = []
    while unseen:
        bit = unseen & -unseen
        unseen ^= bit
        block = bit
        frontier = bit
        while frontier:
            vbit = frontier & -frontier
            frontier ^= vbit
            v = vbit.bit_length() - 1
            add = adj[v] & unseen
            unseen ^= add
            block |= add
            frontier |= add
        blocks.append(block)
    return blocks


def induced_p3(adj):
    n = len(adj)
    for middle in range(n):
        nbrs = [v for v in range(n) if (adj[middle] >> v) & 1]
        for i, left in enumerate(nbrs):
            for right in nbrs[i + 1:]:
                if not ((adj[left] >> right) & 1):
                    return left, middle, right
    return None


def best_response(adj, state, vertex):
    # Even number of active OPEN neighbors -> 1; odd -> 0.
    return 1 - ((adj[vertex] & state).bit_count() & 1)


def is_improving(adj, state, vertex):
    return ((state >> vertex) & 1) != best_response(adj, state, vertex)


def verify(max_n=6):
    graph_checks = 0
    cluster_graphs = 0
    noncluster_graphs = 0
    state_checks = 0
    improvement_checks = 0
    witness_checks = 0
    for n in range(1, max_n + 1):
        total_edges = n * (n - 1) // 2
        for edge_mask in range(1 << total_edges):
            adj = neighborhoods(n, edge_mask)
            comps = components(adj)
            witness = induced_p3(adj)
            is_cluster = all(all((adj[v] & (part ^ (1 << v))) == (part ^ (1 << v))
                                 for v in range(n) if part & (1 << v)) for part in comps)
            assert is_cluster == (witness is None)
            graph_checks += 1
            if not is_cluster:
                noncluster_graphs += 1
                a, b, c = witness
                assert a != c and not (adj[a] & (1 << c))
                start = 1 << c
                state = start
                for v in (a, b, a, b):
                    assert is_improving(adj, state, v), (n, edge_mask, a, b, c, state, v)
                    state ^= 1 << v
                    witness_checks += 1
                assert state == start
                continue
            cluster_graphs += 1
            for state in range(1 << n):
                oddcount = sum((state & part).bit_count() & 1 for part in comps)
                even_count = len(comps) - oddcount
                legal = [v for v in range(n) if is_improving(adj, state, v)]
                assert (len(legal) == 0) == (even_count == 0)
                assert len(legal) == sum(part.bit_count() for part in comps
                                         if (state & part).bit_count() % 2 == 0)
                for v in legal:
                    nextstate = state ^ (1 << v)
                    nextodd = sum((nextstate & part).bit_count() & 1 for part in comps)
                    assert nextodd == oddcount + 1
                    improvement_checks += 1
                state_checks += 1
            observed_eq = sum(all(not is_improving(adj, state, v) for v in range(n))
                              for state in range(1 << n))
            assert observed_eq == 1 << (n - len(comps))
    print(f'graphs={graph_checks} cluster_graphs={cluster_graphs} noncluster_graphs={noncluster_graphs}')
    print(f'cluster_state_checks={state_checks} cluster_improvement_edges={improvement_checks}')
    print(f'four_step_witness_moves={witness_checks}')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
