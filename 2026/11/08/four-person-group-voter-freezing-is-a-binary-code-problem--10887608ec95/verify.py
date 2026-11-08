"""Standalone exact checks for the four-person simplicial group-voter rule.

Run with Python 3: python verify.py
No non-standard packages or network access are needed.
"""
from collections import Counter
from itertools import combinations
import random


def active_from_update_rule(edges, state):
    """List groups in which some focal agent can change opinion."""
    ans = []
    for group in edges:
        possible = False
        for focal in group:
            own = (state >> focal) & 1
            if all(((state >> other) & 1) != own for other in group if other != focal):
                possible = True
                break
        ans.append(int(possible))
    return tuple(ans)


def rank_binary_rows(rows):
    """Binary Gaussian elimination, independent of the state enumeration."""
    basis = {}
    for row in rows:
        x = row
        while x:
            pivot = x.bit_length() - 1
            if pivot in basis:
                x ^= basis[pivot]
            else:
                basis[pivot] = x
                break
    return len(basis)


def inspect_hypergraph(n, edges):
    rows = tuple(sum(1 << v for v in e) for e in edges)
    assert all(len(e) == 4 and len(set(e)) == 4 for e in edges)
    num_states = 1 << n
    outcomes = Counter()
    for state in range(num_states):
        direct = active_from_update_rule(edges, state)
        linear = tuple((r & state).bit_count() & 1 for r in rows)
        assert direct == linear, (n, edges, state, direct, linear)
        outcomes[direct] += 1
    rank = rank_binary_rows(rows)
    assert len(outcomes) == (1 << rank), (n, edges, rank, len(outcomes))
    assert set(outcomes.values()) == {1 << (n - rank)}, (n, edges, outcomes)
    assert outcomes[(0,) * len(edges)] == (1 << (n - rank))
    assert (len(outcomes) == (1 << len(edges))) == (rank == len(edges))
    return num_states


def main():
    graph_tests = 0
    config_tests = 0
    for n in (4, 5):
        all_edges = list(combinations(range(n), 4))
        for mask in range(1 << len(all_edges)):
            edges = tuple(e for j, e in enumerate(all_edges) if (mask >> j) & 1)
            config_tests += inspect_hypergraph(n, edges)
            graph_tests += 1

    # Deterministic random sample across the 32768 labeled six-node hypergraphs.
    n = 6
    all_edges = list(combinations(range(n), 4))
    rng = random.Random(20261104)
    choices = set((0, (1 << len(all_edges)) - 1))
    while len(choices) < 3500:
        choices.add(rng.randrange(1 << len(all_edges)))
    for mask in sorted(choices):
        edges = tuple(e for j, e in enumerate(all_edges) if (mask >> j) & 1)
        config_tests += inspect_hypergraph(n, edges)
        graph_tests += 1

    # Deliberately dependent and independent hyperedge systems.
    examples = [
        (6, ((0, 1, 2, 3), (0, 1, 4, 5), (2, 3, 4, 5))),
        (10, ((0, 1, 2, 3), (0, 4, 5, 6), (0, 7, 8, 9))),
        (9, ((0, 1, 3, 4), (1, 2, 5, 6), (2, 0, 7, 8))),
    ]
    for n, edges in examples:
        config_tests += inspect_hypergraph(n, edges)
        graph_tests += 1

    # Dense complete 4-uniform hypergraph on five vertices has only consensus frozen.
    complete_five = tuple(combinations(range(5), 4))
    full_rows = [sum(1 << v for v in edge) for edge in complete_five]
    assert rank_binary_rows(full_rows) == 4
    assert [x for x in range(32) if not any(active_from_update_rule(complete_five, x))] == [0, 31]

    e1, e2, e3 = examples[0][1]
    rows = [sum(1 << v for v in edge) for edge in (e1, e2, e3)]
    assert rows[0] ^ rows[1] ^ rows[2] == 0
    assert rank_binary_rows(rows) == 2
    assert (1 << (6-2)) == 16
    for state in range(1 << 6):
        flags = active_from_update_rule((e1, e2, e3), state)
        assert (flags[0] ^ flags[1] ^ flags[2]) == 0

    # At three- and five-person group size, activity is NOT an affine parity
    # rule: all-zero is inactive, singleton is active, and weight-three is
    # respectively inactive at s=3 or inactive at s=5.
    for size in (3, 5, 6):
        edge = (tuple(range(size)),)
        assert active_from_update_rule(edge, 0) == (0,)
        assert active_from_update_rule(edge, 1) == (1,)
        assert active_from_update_rule(edge, 7) == (0,)
        assert ((7).bit_count() & 1) == 1

    print('VERIFIED: %d hypergraphs, %d exact complete configurations' % (graph_tests, config_tests))
    print('VERIFIED: update-rule activity equals binary row parity')
    print('VERIFIED: all attainable activity vectors have equal preimage sizes')
    print('VERIFIED: frozen-state count and full-row-rank independence criterion')
    print('VERIFIED: dependent triple obstruction and unique four-person parity case')


if __name__ == '__main__':
    main()
