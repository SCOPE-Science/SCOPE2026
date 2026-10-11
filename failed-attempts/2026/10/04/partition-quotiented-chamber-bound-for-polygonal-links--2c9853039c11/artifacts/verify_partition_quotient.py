#!/usr/bin/env python3
from itertools import permutations
from collections import Counter
from math import factorial

def cycle_type(p):
    n = len(p)
    seen = [False] * n
    parts = []
    for i in range(n):
        if not seen[i]:
            j = i
            k = 0
            while not seen[j]:
                seen[j] = True
                k += 1
                j = p[j]
            parts.append(k)
    return tuple(sorted(parts, reverse=True))

def restricted_partitions(n, min_part=3, max_part=None):
    if n == 0:
        return {()}
    if max_part is None:
        max_part = n
    out = set()
    for first in range(min(max_part, n), min_part - 1, -1):
        rem = n - first
        if rem == 0:
            out.add((first,))
        elif rem >= min_part:
            for tail in restricted_partitions(rem, min_part, first):
                out.add((first,) + tail)
    return out

def class_size(n, parts):
    mult = Counter(parts)
    den = 1
    for k, m in mult.items():
        den *= (k ** m) * factorial(m)
    return factorial(n) // den

def partition_count_dp(n, min_part=3):
    dp = [0] * (n + 1)
    dp[0] = 1
    for part in range(min_part, n + 1):
        for s in range(part, n + 1):
            dp[s] += dp[s - part]
    return dp[n]

total_checked = 0
for n in range(3, 10):
    observed = Counter()
    for p in permutations(range(n)):
        t = cycle_type(p)
        if all(k >= 3 for k in t):
            observed[t] += 1
            total_checked += 1

    expected_types = restricted_partitions(n, 3)
    assert set(observed) == expected_types, (n, set(observed), expected_types)
    assert len(expected_types) == partition_count_dp(n, 3), n

    for t, count in observed.items():
        assert count == class_size(n, t), (n, t, count, class_size(n, t))

    print(
        f"N={n}: cycle_types={len(expected_types)} "
        f"admissible_labeled_decompositions={sum(observed.values())}"
    )

print(f"VERIFY_OK total_admissible_permutations_checked={total_checked}")
