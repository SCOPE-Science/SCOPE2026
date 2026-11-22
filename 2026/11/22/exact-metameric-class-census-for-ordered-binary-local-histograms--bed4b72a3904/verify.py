#!/usr/bin/env python3
"""Reproducible finite tests for ordered binary sliding-window weight profiles."""
from collections import Counter
from itertools import product
from math import comb, prod


def read_vector(word, width):
    n = len(word)
    return tuple(sum(word[i:i + width]) for i in range(n - width + 1))


def exact_fiber_distribution(n, width):
    lengths = [len(range(j, n, width)) for j in range(width)]
    ans = Counter()
    # Choose which residue columns are mixed; the other columns are pure.
    for mixed in product((0, 1), repeat=width):
        pure_count = width - sum(mixed)
        patterns = prod((2**lengths[j] - 2) for j in range(width) if mixed[j])
        for number_one_pure in range(pure_count + 1):
            ans[comb(pure_count, number_one_pure)] += patterns
    return +ans


def closed_form(n, width):
    lengths = [len(range(j, n, width)) for j in range(width)]
    a = [2**length - 1 for length in lengths]
    b = [q - 1 for q in a]
    outputs = prod(a) + sum(prod(a[:j] + a[j+1:]) for j in range(width))
    singleton = 2 * prod(a) - prod(b)
    return outputs, singleton, outputs - singleton


def main():
    inputs = profiles = positive_fibers = 0
    for n in range(1, 16):
        for width in range(1, n+1):
            brute = Counter(read_vector(bits, width)
                            for bits in product((0, 1), repeat=n))
            actual = Counter(brute.values())
            expected = exact_fiber_distribution(n, width)
            assert actual == expected, (n, width, actual, expected)
            r, u, k = closed_form(n, width)
            assert len(brute) == r, (n, width, len(brute), r)
            assert actual[1] == u, (n, width, actual[1], u)
            assert sum(v for f, v in actual.items() if f > 1) == k
            assert sum(f * c for f, c in expected.items()) == 2**n
            assert max(actual) == comb(width, width//2), (n, width)
            inputs += 2**n
            profiles += len(brute)
            positive_fibers += k
    print('VERIFY_OK', 'parameter_pairs=', sum(range(1, 16)),
          'enumerated_input_instances=', inputs,
          'distinct_profiles=', profiles,
          'nonsingleton_fibers=', positive_fibers,
          'range=1<=width<=n<=15')
    for n,width in [(22,7), (28,7), (100,11), (101,11), (1000,11)]:
        dist = exact_fiber_distribution(n, width)
        outputs, singleton, nontrivial = closed_form(n, width)
        assert sum(dist.values()) == outputs
        assert dist[1] == singleton
        assert sum(v for k,v in dist.items() if k>1) == nontrivial
        assert sum(size*count for size,count in dist.items()) == 2**n
    print('LARGE_PARAMETER_IDENTITY_OK', 5)

if __name__ == '__main__':
    main()
