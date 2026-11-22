#!/usr/bin/env python3
"""Exact finite checks for monotone-path equivalence of antidiagonal vertex filtrations.

Only the Python standard library is required. The mathematical theorem uses a
separate general proof; these finite tests are regression checks.
"""
from functools import lru_cache
from fractions import Fraction
from collections import Counter


def interval_histories(n):
    """Independently grow intervals, recording each labelled simultaneous batch."""
    out = set()
    def grow(lo, hi, hist):
        if hi - lo + 1 == n:
            out.add(hist)
            return
        if lo > 1:
            grow(lo - 1, hi, hist + ((lo - 1,),))
        if hi < n:
            grow(lo, hi + 1, hist + ((hi + 1,),))
        if lo > 1 and hi < n:
            grow(lo - 1, hi + 1, hist + ((lo - 1, hi + 1),))
    for i in range(1, n + 1):
        grow(i, i, ((i,),))
    for i in range(1, n):
        grow(i, i + 1, ((i, i + 1),))
    return out


def witness(n, history):
    """The exact integral-corner monotone path realizing an interval history."""
    corners = [(0, 0)]
    entered = set()
    for batch in history:
        entered.update(batch)
        assert entered == set(range(min(entered), max(entered) + 1))
        corners.append((max(entered), n + 1 - min(entered)))
    corners.append((n + 1, n + 1))
    return corners


def get_history(n, corners):
    """Read threshold events directly from a monotone piecewise-linear path."""
    assert corners[0] == (0, 0) and corners[-1] == (n + 1, n + 1)
    seen = set()
    hist = []
    for (x0, y0), (x1, y1) in zip(corners, corners[1:]):
        assert x0 <= x1 and y0 <= y1
        # All checks here are exact, because each segment endpoints are integers.
        candidates = []
        for i in range(1, n + 1):
            if i in seen:
                continue
            if x1 < i or y1 < n + 1 - i:
                continue
            # First parameter time at which both coordinate thresholds are met.
            tx = 0 if x0 >= i else Fraction(i - x0, x1 - x0)
            ty = 0 if y0 >= n + 1 - i else Fraction(n + 1 - i - y0, y1 - y0)
            candidates.append((max(tx, ty), i))
        times = sorted(set(t for t, _ in candidates))
        for t in times:
            batch = tuple(i for tt, i in candidates if tt == t)
            hist.append(tuple(sorted(batch)))
            seen.update(batch)
    assert seen == set(range(1, n + 1))
    return tuple(hist)


def all_lattice_path_signatures(n):
    """Independent exhaustive walk enumeration, including diagonal moves."""
    dest = n + 1
    signatures = set()
    paths = 0
    def rec(x, y, corners):
        nonlocal paths
        if x == dest and y == dest:
            signatures.add(get_history(n, corners))
            paths += 1
            return
        for dx, dy in ((1, 0), (0, 1), (1, 1)):
            if x + dx <= dest and y + dy <= dest:
                rec(x + dx, y + dy, corners + [(x + dx, y + dy)])
    rec(0, 0, [(0, 0)])
    return paths, signatures


def delannoy(a, b):
    @lru_cache(None)
    def d(x, y):
        if x == 0 or y == 0:
            return 1
        return d(x - 1, y) + d(x, y - 1) + d(x - 1, y - 1)
    return d(a, b)


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def run():
    prev2, prev1 = 1, 3
    total_history_checks = 0
    total_grid_paths = 0
    for n in range(1, 11):
        histories = interval_histories(n)
        for hist in histories:
            assert get_history(n, witness(n, hist)) == hist
        total_history_checks += len(histories)
        count = len(histories)
        diagonal_sum = sum(delannoy(a, n - 1 - a) for a in range(n))
        diagonal_sum += sum(delannoy(a, n - 2 - a) for a in range(n - 1))
        assert count == diagonal_sum
        if n == 1:
            assert count == 1
        elif n == 2:
            assert count == 3
        else:
            assert count == 2 * prev1 + prev2
            prev2, prev1 = prev1, count
        fiber_sizes = Counter(tuple(map(len, h)) for h in histories)
        assert len(fiber_sizes) == fibonacci(n + 1)
        for b, fiber_count in fiber_sizes.items():
            singles = b.count(1)
            assert fiber_count == 2 ** (singles - (b[0] == 1)), (n, b, fiber_count)
        barcode_types = set(fiber_sizes)
        if n <= 6:
            npaths, sig = all_lattice_path_signatures(n)
            assert sig == histories, (n, len(sig), count)
            total_grid_paths += npaths
        print('n=%d paths_classes=%d barcode_classes=%d%s' %
              (n, count, len(barcode_types), ' exhaustive_lattice=yes' if n <= 6 else ''))
    print('PASS histories=%d; exhaustive_lattice_paths=%d' % (total_history_checks, total_grid_paths))


if __name__ == '__main__':
    run()
