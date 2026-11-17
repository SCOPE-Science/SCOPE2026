"""Exact, standalone certificate for cycle-length power-sum collisions.

Run with Python 3.9 or newer: python3 verify.py
Only standard-library integer arithmetic is used.
"""

from collections import Counter, defaultdict
from fractions import Fraction

BOUND = 14


def partition_signatures_by_recurrence(bound=BOUND):
    """Coefficient recurrence for prod_j (1-z^j u^(j*j) v^(j*j*j))^(-1)."""
    states = [defaultdict(int) for _ in range(bound + 1)]
    states[0][(0, 0)] = 1
    for size in range(1, bound + 1):
        # Ascending weight uses the current-stage entry at weight m-size,
        # implementing unlimited copies of the given part size.
        for m in range(size, bound + 1):
            for (s2, s3), count in list(states[m - size].items()):
                states[m][(s2 + size * size,
                           s3 + size * size * size)] += count
    return states


def partitions_of(n, upper=None):
    """Independent integer-partition generator in decreasing order."""
    if upper is None:
        upper = n
    if n == 0:
        yield ()
        return
    for head in range(min(upper, n), 0, -1):
        for tail in partitions_of(n - head, head):
            yield (head,) + tail


def signature(parts):
    return sum(x * x for x in parts), sum(x * x * x for x in parts)


def compare():
    dp = partition_signatures_by_recurrence()
    partition_numbers = [0, 1, 2, 3, 5, 7, 11, 15, 22,
                         30, 42, 56, 77, 101, 135]
    print('size partitions signatures nontrivial_fibres max_fibre')
    for m in range(1, BOUND + 1):
        explicit = defaultdict(list)
        for parts in partitions_of(m):
            explicit[signature(parts)].append(parts)
        counts = Counter({sig: len(pre) for sig, pre in explicit.items()})
        assert dict(counts) == dict(dp[m]), ('independent mismatch', m)
        assert sum(counts.values()) == partition_numbers[m], m
        collisions = {sig: lst for sig, lst in explicit.items() if len(lst) > 1}
        print(m, partition_numbers[m], len(counts), len(collisions), max(counts.values()))
        if m < 14:
            assert not collisions, ('unanticipated smaller collision', m, collisions)
        else:
            assert len(collisions) == 1 and set(collisions) == {(74, 434)}, collisions
            assert set(collisions[(74, 434)]) == {(7, 4, 3), (6, 6, 1, 1)}
            assert max(counts.values()) == 2

    p = (7, 4, 3)
    q = (6, 6, 1, 1)
    assert (sum(p), signature(p)) == (14, (74, 434))
    assert (sum(q), signature(q)) == (14, (74, 434))
    assert Fraction(74, 14) == Fraction(37, 7)
    assert Fraction(434, 14) - Fraction(74, 14) ** 2 == Fraction(150, 49)
    # The all-size family is proved symbolically by adding M-14 singleton
    # cycles: S_2=M+60 and S_3=M+420, with dissimilar cycle profiles.
    for m in range(14, 1001):
        f = p + (1,) * (m - 14)
        g = q + (1,) * (m - 14)
        assert f != g and signature(f) == signature(g) == (m + 60, m + 420)
    print('PASS: unique smallest collision and all-size witness identities')


if __name__ == '__main__':
    compare()
