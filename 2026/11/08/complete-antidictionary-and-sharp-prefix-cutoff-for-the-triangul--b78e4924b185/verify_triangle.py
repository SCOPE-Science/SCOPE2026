#!/usr/bin/env python3
"""Finite checks for the triangular-marker antidictionary and prefix cutoff.

Proofs in RESULT.md establish all unbounded assertions; these tests are finite
cross-checks only, with their tested ranges reported on execution.
"""
from collections import defaultdict


def word_through_gap(m):
    return ''.join('1' + '0' * j for j in range(1, m + 1))


def factors(word, n):
    if n == 0:
        return {''}
    return {word[i:i+n] for i in range(len(word)-n+1)}


def min_absent(word, n):
    smaller = factors(word, n-1)
    bigger = factors(word, n)
    return {p + b for p in smaller for b in '01'
            if p + b not in bigger and (p + b)[1:] in smaller}


def expected(n):
    ans = {'11'}
    for a in range(1, n+1):
        ans.add('0' * a + '1' + '0' * a + '1')
        ans.add('1' + '0' * a + '1' + '0' * (a+2))
    return {v for v in ans if len(v) == n}


def cutoff(n):
    return n*(n+3)//2


def run():
    maximum = 26
    W = word_through_gap(maximum + 8)
    tested_maws = 0
    compared_factors = 0
    for n in range(1, maximum+1):
        all_factors = factors(W, n)
        assert len(all_factors) == ((n+1)**2//4 + 1), n
        compared_factors += len(all_factors)
        got = min_absent(W, n)
        assert got == expected(n), (n, sorted(got ^ expected(n)))
        tested_maws += len(got)
        L = cutoff(n)
        assert factors(W[:L], n) == all_factors, ('cutoff', n)
        assert factors(W[:L-1], n) != all_factors, ('sharp', n)
        for m in range(1,n+1):
            assert min_absent(W[:L], m) == expected(m), (n,m)
        # Check the shortest defining absence: the first block of n zeros.
        assert '0' * n not in factors(W[:L-1], n)
        assert '0' * n in factors(W[:L], n)
    print(f'CHECK_OK exact_maw_lengths=1..{maximum} '
          f'factor_complexity_lengths=1..{maximum} '
          f'prefix_cutoff=1..{maximum} '
          f'factor_instances={compared_factors} total_minimal_absent={tested_maws}')


if __name__ == '__main__':
    run()
