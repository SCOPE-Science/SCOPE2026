"""Finite direct checks for the distributed-knowledge profile formulas.
Uses only Python's standard library.  Execute: python distributed_knowledge_verifier.py
"""
from collections import Counter
from itertools import product
from math import prod


def data(sizes):
    k = len(sizes)
    all_coalitions = range(1 << k)
    states = list(product(*(range(n) for n in sizes)))
    matching = [sum((1 << i) for i, a in enumerate(x) if a == 0)
                for x in states]
    accessible = [sum((1 << j) for j, mask in enumerate(matching)
                      if mask & g == g) for g in all_coalitions]
    return matching, accessible


def predicted(sizes):
    k = len(sizes)
    count_by_profile = {}
    s = 1 << k
    N = prod(sizes)
    sizes_by_signature = [prod(sizes[i] - 1 for i in range(k)
                               if not (c & (1 << i))) for c in range(s)]
    for q in range(1 << s):
        members = [c for c in range(s) if q & (1 << c)]
        if any(((q & (1 << d)) == 0) for c in members
               for d in range(s) if d & c == d):
            continue
        maxima = [c for c in members if not any(c != d and c & d == c
                                              for d in members)]
        count = 1
        for c in members:
            v = 1 << sizes_by_signature[c]
            count *= v - 1 if c in maxima else v
        count_by_profile[q] = count
    assert sum(count_by_profile.values()) == 1 << N
    return count_by_profile


def directly_enumerated(sizes):
    matching, accessible = data(sizes)
    count_by_profile = Counter()
    for bad in range(1 << len(matching)):
        q = sum((1 << g) for g, a in enumerate(accessible) if bad & a)
        count_by_profile[q] += 1
    return count_by_profile


def check(sizes):
    direct = directly_enumerated(sizes)
    formula = predicted(sizes)
    assert direct == formula, (sizes, direct, formula)
    k = len(sizes)
    full = (1 << (1 << k)) - 1
    proper = full - (1 << ((1 << k) - 1))
    N = prod(sizes)
    assert direct[full] == 1 << (N - 1)
    # Removing the empty-coalition query identifies just the empty and singleton-empty failure ideals.
    projected = {}
    for q in direct:
        projected.setdefault(q & ~1, []).append(q)
    assert len(projected) == len(direct) - 1
    assert sorted([tuple(sorted(v)) for v in projected.values() if len(v) > 1]) == [(0, 1)]
    # For unbiased independent truth values, probability = (1/2)prod_i(1 - 2^(1-n_i)).
    assert direct[proper] * prod(1 << (n - 1) for n in sizes) == (
        (1 << (N - 1)) * prod((1 << (n - 1)) - 1 for n in sizes))
    return len(direct), 1 << N, direct[proper]


if __name__ == '__main__':
    test_cases = [(2, 2), (2, 3), (3, 3), (2, 4),
                  (2, 2, 2), (2, 2, 3), (2, 3, 2), (2, 2, 2, 2)]
    for dimensions in test_cases:
        print(dimensions, check(dimensions))
    print('ALL CHECKS PASSED')
