#!/usr/bin/env python3
"""Independent stream-DP test against a weighted-gap calculation."""
from collections import defaultdict


def weighted_gap_count(n, k):
    if k == 0:
        return 1 + n * (n + 1) // 2
    ans = 0
    for zeros in range(2, k + 2):
        weights = tuple(j * (zeros-j) for j in range(1, zeros))
        # State: (occurrence weight, number of interior ones) -> multiplicity.
        states = {(0, 0): 1}
        for weight in weights:
            new = defaultdict(int)
            for (occurrences, ones), count in states.items():
                for times in range((k - occurrences) // weight + 1):
                    new[(occurrences + times * weight, ones + times)] += count
            states = new
        for (occurrences, ones), count in states.items():
            if occurrences == k:
                ans += count * max(n - zeros - ones + 1, 0)
    return ans


def test():
    limit_n, limit_k = 30, 30
    # State: (number of zeros, 01 subsequences, 010 subsequences).
    states = {(0, 0, 0): 1}
    for n in range(limit_n + 1):
        frequencies = defaultdict(int)
        for (_, _, triples), multiplicity in states.items():
            frequencies[triples] += multiplicity
        for k in range(limit_k + 1):
            expected = weighted_gap_count(n, k)
            assert frequencies[k] == expected, (n, k, frequencies[k], expected)
        new_states = defaultdict(int)
        for (zeros, pairs, triples), count in states.items():
            # Appending 0 adds one to the zero count and one 010 per old 01.
            if triples + pairs <= limit_k:
                new_states[(zeros + 1, pairs, triples + pairs)] += count
            # Appending 1 adds one 01 per old zero, without adding any 010.
            new_states[(zeros, pairs + zeros, triples)] += count
        states = new_states
    print('PASS: independent letter-stream dynamic program vs. gap count for n,k=0,...,30')


if __name__ == '__main__':
    test()
