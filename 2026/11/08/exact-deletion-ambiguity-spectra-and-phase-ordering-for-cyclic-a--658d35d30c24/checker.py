#!/usr/bin/env python3
"""Finite verification for exact common-descendant profiles of cyclic-shift words.

Independent direct subsequence-set enumeration is compared to an algebraic
bounded-composition formula. This checks finite parameters, not the theorem
for arbitrary parameters.
"""
from itertools import combinations


def common_by_subsets(q, n, h, k):
    left = tuple(i % q for i in range(n))
    right = tuple((i + h) % q for i in range(n))
    def subwords(word):
        return {tuple(word[j] for j in ii)
                for ii in combinations(range(n), k)}
    return len(subwords(left) & subwords(right))


def composition_prefix(q, k, cap):
    """Return the number of k-tuples in [1,q]^k summing <= cap."""
    if cap < 0:
        return 0
    ways = [1]
    for _ in range(k):
        nxt = [0] * (len(ways) + q)
        for s, count in enumerate(ways):
            for jump in range(1, q + 1):
                nxt[s + jump] += count
        ways = nxt
    return sum(ways[:cap + 1])


def formula(q, n, h, k):
    if k == 0:
        return 1
    return (sum(composition_prefix(q, k - 1, n - j)
                for j in range(h + 1, q + 1))
          + sum(composition_prefix(q, k - 1, n - j)
                for j in range(q - h + 1, q + 1)))


def run():
    tested_entries = 0
    tested_profiles = 0
    for q in range(2, 9):
        for n in range(1, 11):
            profiles = {}
            for h in range(1, q):
                given = [formula(q, n, h, k) for k in range(n + 1)]
                direct = [common_by_subsets(q, n, h, k)
                          for k in range(n + 1)]
                assert given == direct, (q, n, h, given, direct)
                tested_entries += len(given)
                tested_profiles += 1
                profiles[h] = given
                d = min(h, q - h)
                maxlen = max(0, n - d)
                assert max(i for i, a in enumerate(given) if a) == maxlen
                if n > d:
                    assert given[maxlen] == (2 if 2*h == q else 1)
                if q - h in profiles:
                    assert given == profiles[q - h]
            for d in range(1, (q - 1) // 2 + 1):
                a, b = profiles[d], profiles[d+1]
                assert all(x >= y for x, y in zip(a, b)), (q, n, d)
                if n > d and d+1 <= q//2:
                    assert a[n-d] > b[n-d]
    print("VERIFIED: direct subsequence sets versus bounded-composition formula")
    print(f"VERIFIED: {tested_profiles} distinct parameter profiles, "
          f"{tested_entries} length entries, q=2..8, n=1..10")
    print("VERIFIED: exact LCS lengths, multiplicities and phase ordering")
    print("EXAMPLE q=6,n=12: ")
    for h in (1, 2, 3):
        print(f"h={h}: {[formula(6,12,h,k) for k in range(13)]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
