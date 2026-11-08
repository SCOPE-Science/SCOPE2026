#!/usr/bin/env python3
"""Independent finite verification of ordered two-row one-deletion inverse lists.

No external packages or stored certificates are required. All compatible
source matrices are generated directly from the ordered column alphabet.
"""
from collections import defaultdict
from itertools import combinations_with_replacement, product


def inverse_list_counts(q, n):
    columns = tuple(combinations_with_replacement(range(q), 2))
    counts = defaultdict(int)
    for choices in product(columns, repeat=n):
        lower = tuple(z[0] for z in choices)
        upper = tuple(z[1] for z in choices)
        lower_outputs = {lower[:j] + lower[j + 1:] for j in range(n)}
        upper_outputs = {upper[:j] + upper[j + 1:] for j in range(n)}
        for a in lower_outputs:
            for b in upper_outputs:
                counts[a, b] += 1
    return counts


def predicted(q, n):
    return (1 + n * (q - 1)) ** 2 - n * q * (q - 1) // 2


def check():
    suites = {2: range(1, 9), 3: range(1, 6), 4: range(1, 5),
              5: range(1, 4), 6: range(1, 4)}
    for q, lengths in suites.items():
        for n in lengths:
            counts = inverse_list_counts(q, n)
            expected = predicted(q, n)
            assert max(counts.values()) == expected, (q, n)
            maxima = {pair for pair, size in counts.items() if size == expected}
            singleton = ((0,) * (n - 1), (q - 1,) * (n - 1))
            assert maxima == {singleton}, (q, n, maxima)
            if n >= 2:
                # Distinct received pairs are allowed to have any relative order.
                assert len(counts) <= q ** (2 * (n - 1))
            print(f"q={q} n={n}: max={expected}; unique maximizer; PASS")
    print("VERIFY_OK")


if __name__ == '__main__':
    check()
