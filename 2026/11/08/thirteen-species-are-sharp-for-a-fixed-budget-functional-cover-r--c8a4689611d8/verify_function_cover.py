"""Exact check of finite functional-group coverage rankings.

Requires Python 3.9+ standard library; all quantities are integers.
Run: python verify_function_cover.py
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
from math import comb

@lru_cache(None)
def partitions(n, least=1):
    if n == 0:
        return ((),)
    return tuple((j,) + rest
                 for j in range(least, n + 1)
                 for rest in partitions(n - j, j))

def positive_coverage_counts(profile):
    # Coefficients of product ((1+z)^a - 1).
    coefficients = [1]
    for a in profile:
        nxt = [0] * (len(coefficients) + a)
        for i, c in enumerate(coefficients):
            for j in range(1, a + 1):
                nxt[i+j] += c * comb(a, j)
        coefficients = nxt
    return tuple(coefficients)

def counts_inclusion_exclusion(profile):
    # Independently, count subsets touching every group.
    n = sum(profile)
    result = []
    for k in range(n + 1):
        total = 0
        for mask in range(1 << len(profile)):
            blocked = sum(a for i, a in enumerate(profile) if mask & (1 << i))
            if n-blocked >= k:
                total += (-1 if mask.bit_count() % 2 else 1) * comb(n-blocked, k)
        result.append(total)
    return tuple(result)

def crosses(x, y):
    differences = [a-b for a,b in zip(x, y)]
    return min(differences) < 0 < max(differences)

def direct_counts(profile):
    # Independent subset enumeration of all 2^n subsets.
    n = sum(profile)
    group_masks = []
    start = 0
    for a in profile:
        group_masks.append(((1 << a)-1) << start)
        start += a
    counts = [0] * (n+1)
    for mask in range(1 << n):
        if all(mask & gm for gm in group_masks):
            counts[mask.bit_count()] += 1
    return tuple(counts)

def main():
    expected = {
        (5, (1,3,3,3,3), (2,2,2,2,5)),
        (4, (1,3,4,5), (2,2,2,7)),
        (4, (1,4,4,4), (2,2,2,7)),
    }
    compared = 0
    for n in range(1,14):
        by_group_count = defaultdict(list)
        for profile in partitions(n):
            p = positive_coverage_counts(profile)
            q = counts_inclusion_exclusion(profile)
            assert p == q, (n, profile, p, q)
            by_group_count[len(profile)].append((profile, p))
        found = set()
        for g, array in by_group_count.items():
            for (profile1, v1), (profile2, v2) in combinations(array, 2):
                compared += 1
                if crosses(v1, v2):
                    found.add((g, profile1, profile2))
        assert found == (expected if n == 13 else set()), (n, found)
        print(f"n={n}: {len(partitions(n))} profiles; {len(found)} crossing pairs")
    for g, a, b in sorted(expected):
        assert direct_counts(a) == positive_coverage_counts(a)
        assert direct_counts(b) == positive_coverage_counts(b)
        deltas = [x-y for x,y in zip(positive_coverage_counts(a),positive_coverage_counts(b))]
        print(f"g={g}, A={a}, B={b}: numerator differences={deltas}")
    # Infinite fixed-four-function family: products and singleton counts.
    # A=(1,3,4,m), B=(2,2,2,m+2) for every m>=5.
    # At k=4, A-B = 12m-8(m+2)=4(m-4)>0.
    # At k=(m+8)-1, A-B = -1, because A has one singleton, B none.
    for m in range(5,80):
        a,b=(1,3,4,m),(2,2,2,m+2)
        x,y=positive_coverage_counts(a),positive_coverage_counts(b)
        assert x[4]-y[4] == 4*(m-4)
        assert x[-2]-y[-2] == -1
    print(f"PASS: {compared} all-profile pair comparisons through n=13; independent checks and infinite-family endpoint identities")

if __name__ == '__main__':
    main()
