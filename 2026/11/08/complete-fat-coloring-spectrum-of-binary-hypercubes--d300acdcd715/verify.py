"""Finite checks of uniform off-color neighbor construction on Boolean cubes.

Uses the elementary graph adjacency definition, not any outside certificates.
"""
from collections import Counter
from itertools import product


def mask_columns(d, k, t):
    assert k >= 2 and k & (k - 1) == 0
    r = k.bit_length() - 1
    assert 1 <= t and (k - 1) * t <= d
    return [a for a in range(1, k) for _ in range(t)] + [0] * (d - (k - 1) * t)


def color_of(vertex, columns):
    out = 0
    for i, a in enumerate(columns):
        if vertex & (1 << i):
            out ^= a
    return out


def counts_from_graph(d, assignment):
    k = len(set(assignment))
    for v in range(1 << d):
        row = Counter(assignment[v ^ (1 << i)] for i in range(d))
        me = assignment[v]
        off = [row[j] for j in range(k) if j != me]
        if not off or min(off) == 0 or len(set(off)) != 1:
            return None
        if row[me] + sum(off) != d:
            raise AssertionError('neighbor count anomaly')
    return off[0]


def direct_feasible(d, k, t):
    # Enumerate all surjective labeled k-colorings with a pinned origin color.
    # This canonicalization loses none because color relabeling is free.
    n = 1 << d
    for rest in product(range(k), repeat=n-1):
        assignment = (0,) + rest
        if len(set(assignment)) != k:
            continue
        if counts_from_graph(d, assignment) == t:
            return True
    return False


def main():
    cases = 0
    for d in range(1, 13):
        for r in range(1, 5):
            k = 1 << r
            if k > d + 1:
                continue
            for t in range(1, d // (k - 1) + 1):
                columns = mask_columns(d, k, t)
                c = tuple(color_of(v, columns) for v in range(1 << d))
                assert len(set(c)) == k
                assert counts_from_graph(d, c) == t
                cases += 1
    print('EXPLICIT_CONSTRUCTIONS_DIRECT_NEIGHBOR_COUNTS_OK', cases)
    small = 0
    for d in range(1, 4):
        for k in range(2, d + 2):
            for t in range(1, d + 1):
                expected = (k & (k - 1) == 0 and (k - 1) * t <= d)
                actual = direct_feasible(d, k, t)
                assert actual == expected, (d, k, t, expected, actual)
                small += 1
    print('EXHAUSTIVE_SMALL_PALETTES_OK', small)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
