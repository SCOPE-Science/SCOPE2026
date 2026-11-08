"""Exact finite obstruction certificate for total Roman bondage of K_(2,2,m).
Run with Python 3.9+; no third-party packages are required.
The infinite conclusion additionally uses the reduction proof in RESULT.md.
"""
from itertools import combinations, product


def graph(m):
    assert m >= 1
    n = m + 4
    parts = [0, 0, 1, 1] + [2] * m
    return n, frozenset((i, j) for i in range(n) for j in range(i + 1, n)
                        if parts[i] != parts[j])


def adjacency(n, edges):
    out = [set() for _ in range(n)]
    for u, v in edges:
        out[u].add(v)
        out[v].add(u)
    return out


def eligible(n, edges):
    """All vertices have a neighbor and some adjacent pair dominates."""
    adj = adjacency(n, edges)
    if any(not x for x in adj):
        return False, False
    full = set(range(n))
    edge_dominates = any(full <= (adj[u] | adj[v] | {u, v}) for u, v in edges)
    return True, edge_dominates


def small_obstruction_certificate(m, max_deletions):
    n, base = graph(m)
    ordered = sorted(base)
    total = 0
    nonisolated = 0
    for k in range(max_deletions + 1):
        for removed in combinations(ordered, k):
            total += 1
            intact = base.difference(removed)
            no_isolates, dominant = eligible(n, intact)
            if no_isolates:
                nonisolated += 1
                assert dominant, (m, k, removed)
    return total, nonisolated


def deletion(m):
    if m == 1:
        return {(0, 4)}
    if m == 2:
        return {(0, 3), (0, 5), (1, 2), (2, 4)}
    return {(0, 2), (0, 5), (1, 4), (2, 4), (3, 4)}


def total_roman_number(n, edges):
    adj = adjacency(n, edges)
    if any(not a for a in adj):
        return None
    minimum = 2 * n
    for labels in product(range(3), repeat=n):
        weight = sum(labels)
        if weight >= minimum:
            continue
        positive = {v for v in range(n) if labels[v]}
        if any(not adj[v].intersection(positive) for v in positive):
            continue
        defenders = {v for v in range(n) if labels[v] == 2}
        if any(not adj[v].intersection(defenders) for v in range(n) if labels[v] == 0):
            continue
        minimum = weight
    return minimum


def run():
    for m, k, expected in [(2, 3, 299), (3, 4, 2517), (4, 4, 6196)]:
        total, live = small_obstruction_certificate(m, k)
        assert total == expected
        print('EXHAUSTIVE_OBSTRUCTION_OK', m, total, live)
    for m in range(1, 51):
        n, base = graph(m)
        cut = deletion(m)
        assert cut <= base
        no_isolates, dominant = eligible(n, base.difference(cut))
        assert no_isolates
        if m >= 2:
            assert not dominant, m
        else:
            assert max(map(len, adjacency(n, base.difference(cut)))) < n - 1
    print('EXPLICIT_DELETION_WITNESSES_OK m=1..50')
    for m in range(1, 6):
        n, base = graph(m)
        initial = total_roman_number(n, base)
        changed = total_roman_number(n, base.difference(deletion(m)))
        expected = 3 if m == 1 else 4
        assert initial == expected, (m, initial)
        assert changed > initial, (m, initial, changed)
        print('DIRECT_TOTAL_ROMAN_OK', m, initial, changed)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
