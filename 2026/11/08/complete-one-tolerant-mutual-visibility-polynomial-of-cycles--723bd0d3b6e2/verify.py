"""Standalone finite checks of one-tolerant mutual visibility on cycles.

Run with Python 3: python verify.py. Only standard-library modules are used.
"""
from collections import Counter
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted(n):
    if n in (3, 4):
        return [choose(n, j) for j in range(n + 1)]
    m = n // 2
    values = [choose(n, j) for j in range(4)]
    if n % 2:
        a4 = m * (m - 1) * (m + 1) * (2 * m + 1) // 6
        a5 = m * (m - 1) * (m + 1) * (m + 2) * (2 * m + 1) // 120
    else:
        a4 = m * (m - 1) * (2 * m * m + 2 * m - 9) // 6
        a5 = m * (m - 2) * (m - 1) * (m + 1) * (m + 12) // 60
    return values + [a4, a5]


def is_visible(n, S):
    selected = set(S)
    for a, b in combinations(S, 2):
        distance = min((b - a) % n, (a - b) % n)
        possible = False
        for direction in (-1, 1):
            if (a + direction * distance) % n != b:
                continue
            interior = [(a + direction * j) % n for j in range(1, distance)]
            if sum(v in selected for v in interior) <= 1:
                possible = True
                break
        if not possible:
            return False
    return True


def independent_gap_count(n, size):
    if size == 0:
        return 1
    m = n // 2
    count = 0
    def rec(prefix, remaining):
        nonlocal count
        if len(prefix) == size - 1:
            if remaining < 1:
                return
            gaps = prefix + [remaining]
            if size == 4 and max(gaps) <= m:
                count += 1
            elif size == 5 and all(gaps[i] + gaps[(i + 1) % 5] <= m for i in range(5)):
                count += 1
            return
        reserve = size - len(prefix) - 1
        for gap in range(1, remaining - reserve + 1):
            rec(prefix + [gap], remaining - gap)
    rec([], n)
    assert (n * count) % size == 0
    return n * count // size


def main():
    for n in range(3, 19):
        counts = Counter()
        for size in range(n + 1):
            for S in combinations(range(n), size):
                if is_visible(n, S):
                    counts[size] += 1
        actual = [counts[k] for k in range(max(n + 1, 6))]
        expected = predicted(n) + [0] * (len(actual) - len(predicted(n)))
        assert actual == expected, (n, actual, expected)
        print('GEODESIC_EXHAUSTIVE_OK', n, expected[:6])
    for n in range(5, 33):
        p = predicted(n)
        assert (independent_gap_count(n, 4), independent_gap_count(n, 5)) == tuple(p[4:6]), n
    print('CYCLIC_COMPOSITION_CHECK_OK 5..32')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
