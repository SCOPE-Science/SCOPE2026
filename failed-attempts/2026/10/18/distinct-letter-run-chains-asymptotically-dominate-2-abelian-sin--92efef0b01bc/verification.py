#!/usr/bin/env python3
"""Exhaustive bounded checks of factor-2 signatures and run-chain uniqueness.

The infinite asymptotic theorem relies on cited structural lemmas, not this finite checker.
"""
from itertools import product
from collections import defaultdict
from math import comb, factorial


def signature(word, q):
    edges = [0] * (q * q)
    for x, y in zip(word, word[1:]):
        edges[q*x + y] += 1
    return word[0], tuple(edges)


def is_permutation_run_chain(word, q):
    if len(word) < q:
        return False
    runs = [word[0]]
    for x in word[1:]:
        if x != runs[-1]:
            runs.append(x)
    return len(runs) == q and len(set(runs)) == q


def check(q, n):
    groups = defaultdict(int)
    representative = {}
    for word in product(range(q), repeat=n):
        sig = signature(word, q)
        groups[sig] += 1
        representative[sig] = word
    singleton_words = [representative[s] for s, cnt in groups.items() if cnt == 1]
    singleton_keys = {signature(w, q) for w in singleton_words}
    chains = [w for w in product(range(q), repeat=n) if is_permutation_run_chain(w, q)]
    expected = factorial(q) * comb(n-1, q-1)
    assert len(chains) == expected, (q, n, len(chains), expected)
    assert all(signature(w, q) in singleton_keys for w in chains), (q, n)
    observed = len(singleton_words)
    assert observed >= expected, (q, n, observed, expected)
    if q == 2 and n >= 4:
        assert observed == 2*n+4, (q, n, observed)
    if q == 3 and n >= 6:
        assert observed == 3*n*n+27*n-63, (q, n, observed)
    return observed, expected


def main():
    for q, nmax in [(2, 13), (3, 10), (4, 8), (5, 7)]:
        for n in range(q, nmax + 1):
            total, chains = check(q, n)
            print(f'q={q} n={n} singleton={total} run_chains={chains} remainder={total-chains}')
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    main()
