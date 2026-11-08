#!/usr/bin/env python3
"""Exhaustive independent factor-incidence verification for finite Tribonacci words.

Standard library only. Indices in this file are zero based. The loops over
all triples are exhaustive; a size-two attractor is impossible for words
containing all three distinct letters.
"""
from itertools import product
from math import comb

BOXES = {
    8: [
        ([12,14],[23,27],[43,44,50,51]),
        ([23,27],[36,38],[43,44,50,51]),
        ([23,27],[43,44,50,51],[56,58]),
        ([36],[43,44,50,51],[67,71]),
    ],
    9: [
        ([23,27],[43,44,50,51],[80,82,93,95]),
        ([43,44,50,51],[67,71],[80,82,93,95]),
        ([43,44,50,51],[80,82,93,95],[104,108]),
        ([67],[80,82,93,95],[124,125,131,132]),
    ],
    10: [
        ([43,44,50,51],[80,82,93,95],[148,152,172,176]),
        ([80,82,93,95],[124,125,131,132],[148,152,172,176]),
        ([80,82,93,95],[148,152,172,176],[192,193,199,200]),
        ([124,125],[148,152,172,176],[229,231,242,244]),
    ],
}
LENGTHS = {8:81, 9:149, 10:274}
COUNTS = {8:56, 9:112, 10:224}
FACTORS = {8:2135, 9:7125, 10:23914}


def tribonacci(order):
    word = '0'
    subst = {'0':'01', '1':'02', '2':'0'}
    for _ in range(order - 1):
        word = ''.join(subst[c] for c in word)
    return word


def explicit_boxes(order):
    solutions = set()
    for xx, yy, zz in BOXES[order]:
        for a, b, c in product(xx, yy, zz):
            assert 0 <= a < b < c < LENGTHS[order]
            assert (a,b,c) not in solutions, 'overlapping boxes'
            solutions.add((a,b,c))
    assert len(solutions) == COUNTS[order]
    return solutions


def brute_incidence(word):
    """Build factor->id and position->set-of-factors from occurrences directly."""
    n = len(word)
    factor_ids = {}
    position_factors = [0] * n
    for start in range(n):
        for stop in range(start + 1, n + 1):
            substring = word[start:stop]
            if substring not in factor_ids:
                factor_ids[substring] = len(factor_ids)
            flag = 1 << factor_ids[substring]
            for p in range(start, stop):
                position_factors[p] |= flag
    return len(factor_ids), position_factors


def exhaustive_triples(position_factors, nfactors):
    """Visit every choose(n,3) triple, checking literal factor coverage."""
    n = len(position_factors)
    all_factors = (1 << nfactors) - 1
    result = set()
    attempted = 0
    for i in range(n):
        for j in range(i + 1, n):
            partial = position_factors[i] | position_factors[j]
            for k in range(j + 1, n):
                attempted += 1
                if (partial | position_factors[k]) == all_factors:
                    result.add((i,j,k))
    assert attempted == comb(n,3)
    return result, attempted


def main():
    for order in (8,9,10):
        w = tribonacci(order)
        assert len(w) == LENGTHS[order] and set(w) == set('012')
        nfactors, hit = brute_incidence(w)
        assert nfactors == FACTORS[order]
        actual, tested = exhaustive_triples(hit, nfactors)
        assert actual == explicit_boxes(order), (order, actual ^ explicit_boxes(order))
        print(f'order={order} length={len(w)} factors={nfactors} '
              f'triples_tested={tested} optimal_triples={len(actual)} PASS')

if __name__ == '__main__':
    main()
