"""Standalone checks for universal three-point profiles of nested equivalences.
Uses no libraries besides Python standard library; every asserted mathematical
claim is also proved independently in the accompanying text.
"""
from itertools import combinations, product


def partitions(n):
    """All set partitions as restricted-growth strings."""
    if n == 0:
        yield ()
        return
    def rec(seq, high):
        if len(seq) == n:
            yield tuple(seq)
        else:
            for j in range(high + 2):
                yield from rec(seq + [j], max(high, j))
    yield from rec([0], 0)


def comb_distance(h):
    n = 2 * h + 1
    d = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            j = max(1, (max(a, b) - 1) // 2 + 1)
            d[a][b] = d[b][a] = j
    return d


def tri_types(d):
    n = len(d)
    seen = set()
    for a, b, c in product(range(n), repeat=3):
        seen.add((d[a][b], d[a][c], d[b][c]))
    return seen


def expected_types(h):
    out = {(0, 0, 0)}
    for j in range(1, h + 1):
        out |= {(0, j, j), (j, 0, j), (j, j, 0), (j, j, j)}
    for i in range(1, h + 1):
        for j in range(i+1, h+1):
            out |= {(i, j, j), (j, i, j), (j, j, i)}
    return out


def part_distance(p1, p2):
    n = len(p1)
    d = [[0]*n for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            j = 1 if p1[a] == p1[b] else (2 if p2[a] == p2[b] else 3)
            d[a][b] = d[b][a] = j
    return d


def is_refinement(p1, p2):
    correspondence = {}
    for a, b in zip(p1, p2):
        if a in correspondence and correspondence[a] != b:
            return False
        correspondence[a] = b
    return True


def shape_signature(p1, p2):
    """Unlabelled rooted cluster-tree code for two nested partitions."""
    cl2 = {}
    for v, c in enumerate(p2):
        cl2.setdefault(c, []).append(v)
    roots = []
    for vs in cl2.values():
        cl1 = {}
        for v in vs:
            cl1[p1[v]] = cl1.get(p1[v], 0) + 1
        roots.append(tuple(sorted(cl1.values())))
    return tuple(sorted(roots))


def run():
    for h in range(1, 10):
        actual = tri_types(comb_distance(h))
        expected = expected_types(h)
        assert actual == expected, (h, expected-actual, actual-expected)
        assert len(expected) == 1 + 4*h + 3*h*(h-1)//2
    # Brute all structures with h=2 (one named equivalence) below the
    # proposed threshold, and check unique size-five realizer by class sizes.
    for n in range(1, 6):
        winners = set()
        all_p = list(partitions(n))
        for p in all_p:
            d = [[0 if a==b else (1 if p[a]==p[b] else 2)
                  for b in range(n)] for a in range(n)]
            if tri_types(d) == expected_types(2):
                winners.add(tuple(sorted((p.count(c) for c in set(p)))))
        assert (bool(winners) == (n == 5)), (n, winners)
        if n == 5:
            assert winners == {(1, 1, 3)}, winners
    # Exhaust all labelled two-layer nested partitions through seven points.
    checked = 0
    winners = set()
    for n in range(1, 8):
        parts = list(partitions(n))
        these = 0
        for p1 in parts:
            for p2 in parts:
                if not is_refinement(p1, p2):
                    continue
                checked += 1
                d = part_distance(p1, p2)
                if tri_types(d) == expected_types(3):
                    these += 1
                    winners.add(shape_signature(p1, p2))
        assert (these > 0) == (n == 7), (n, these)
    assert winners == {((1,), (1,), (1, 1, 3))}, winners
    print('VERIFY_OK comb_depths=9 exhaustive_nested_structures=' + str(checked) + ' unique_K2_shape=' + repr(next(iter(winners))))


if __name__ == '__main__':
    run()
