"""Exact finite checks for local versus global independence in interval graphs.

Only the Python standard library is required. Every possible perfect pairing
of the 2n sorted, distinct endpoints is enumerated for 2 <= n <= 7.
The analytic theorem is not inferred from this finite enumeration.
"""
from collections import Counter
from functools import lru_cache


def pairings(points):
    if not points:
        yield ()
        return
    first = points[0]
    for j in range(1, len(points)):
        other = points[j]
        rem = points[1:j] + points[j + 1:]
        for rest in pairings(rem):
            yield ((first, other),) + rest


def disjoint(a, b):
    return a[1] < b[0] or b[1] < a[0]


def independence_bitmask(intervals, included):
    """Independent backtracking solution on an arbitrary included subset."""
    items = [i for i in range(len(intervals)) if included >> i & 1]
    m = len(items)
    best = 0
    for sub in range(1 << m):
        count = sub.bit_count()
        if count <= best:
            continue
        sel = [items[i] for i in range(m) if sub >> i & 1]
        if all(disjoint(intervals[u], intervals[v]) for j, u in enumerate(sel)
               for v in sel[j + 1:]):
            best = count
    return best


def independence_earliest_finish(intervals, included):
    """Independent interval scheduling solution using endpoint order."""
    chosen = [intervals[i] for i in range(len(intervals)) if included >> i & 1]
    chosen.sort(key=lambda x: x[1])
    count = 0
    last = -1
    for left, right in chosen:
        if left > last:
            count += 1
            last = right
    return count


def analyze(intervals):
    n = len(intervals)
    allmask = (1 << n) - 1
    a = independence_bitmask(intervals, allmask)
    assert a == independence_earliest_finish(intervals, allmask)
    b = 0
    for hub in range(n):
        mask = sum(1 << j for j in range(n)
                   if j != hub and not disjoint(intervals[j], intervals[hub]))
        local = independence_bitmask(intervals, mask)
        assert local == independence_earliest_finish(intervals, mask)
        b = max(b, local)
    assert 0 <= b <= a <= n
    return a - b


EXPECTED = {
    2: {0: 2, 2: 1},
    3: {0: 10, 1: 4, 3: 1},
    4: {0: 74, 1: 24, 2: 6, 4: 1},
    5: {0: 686, 1: 208, 2: 42, 3: 8, 5: 1},
    6: {0: 7650, 1: 2264, 2: 406, 3: 64, 4: 10, 6: 1},
    7: {0: 100346, 1: 29068, 2: 4942, 3: 676, 4: 90, 5: 12, 7: 1},
}


def main():
    total = 0
    for n, expected in EXPECTED.items():
        observed = Counter()
        for intervals in pairings(tuple(range(2*n))):
            observed[analyze(intervals)] += 1
            total += 1
        assert dict(observed) == expected, (n, observed)
        double_fact = 1
        for x in range(1, 2*n, 2):
            double_fact *= x
        assert sum(observed.values()) == double_fact
        print(f"n={n}: {double_fact} exhaustive matchings; D histogram={dict(sorted(observed.items()))}")
    assert total == 146598
    print("PASS: 146598 exact pairing configurations and independent optimization checks")


if __name__ == '__main__':
    main()
