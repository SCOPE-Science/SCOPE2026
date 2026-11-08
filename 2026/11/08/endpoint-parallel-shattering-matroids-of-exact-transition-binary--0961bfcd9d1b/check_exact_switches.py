#!/usr/bin/env python3
"""Independent exhaustive checks for exact-transition binary-word shattering.

Requires only the Python standard library. Run: python check_exact_switches.py
"""
from itertools import combinations
from collections import Counter
from functools import lru_cache
from math import comb, floor, log2


def words_with_switches(n, k):
    return [w for w in range(1 << n)
            if sum(((w >> i) & 1) != ((w >> (i + 1)) & 1)
                   for i in range(n - 1)) == k]


def predicted(n, k, support):
    r = min(k + 1, n - k)
    return len(support) <= r and not (0 in support and n - 1 in support)


def exact_ldim(words, n):
    masks = [sum(1 << j for j, w in enumerate(words) if (w >> i) & 1)
             for i in range(n)]
    @lru_cache(maxsize=None)
    def recursion(version_space):
        best = 0
        for mask in masks:
            left = version_space & mask
            right = version_space & ~mask
            if left and right:
                best = max(best, 1 + min(recursion(left), recursion(right)))
        return best
    return recursion((1 << len(words)) - 1)


def main():
    checked = 0
    for n in range(2, 12):
        for k in range(n):
            concepts = words_with_switches(n, k)
            assert len(concepts) == 2 * comb(n - 1, k)
            counts = Counter()
            for s in range(n + 1):
                for S in combinations(range(n), s):
                    traces = {tuple((w >> i) & 1 for i in S) for w in concepts}
                    actual = len(traces) == (1 << s)
                    assert actual == predicted(n, k, S), (n, k, S, actual)
                    counts[s] += actual
                    checked += 1
                expected = (comb(n, s) - (comb(n - 2, s - 2) if s >= 2 else 0))
                if s > min(k + 1, n - k):
                    expected = 0
                assert counts[s] == expected, (n, k, s, counts[s], expected)
            assert max(s for s in counts if counts[s] > 0) == min(k + 1, n - k)
    online = []
    for n in range(2, 10):
        for k in range(n):
            words = words_with_switches(n, k)
            d = exact_ldim(words, n)
            upper = (2 * comb(n - 1, k)).bit_length() - 1
            lower = (k * (int(log2((n - 1) // k)) if k else 0))
            assert lower <= d <= upper, (n, k, d, lower, upper)
            online.append((n, k, d))
    print('EXACT_SWITCH_SHATTERING_PASS')
    print('exhaustive_n=2..11; all_transition_counts_and_all_supports')
    print(f'support_subsets_checked={checked}')
    print('exact_online_n=2..9; all_transition_counts; bounds_confirmed')
    for n in range(2, 10):
        print(f'n={n}: ' + ','.join(str(d) for nn, k, d in online if nn == n))


if __name__ == '__main__':
    main()
