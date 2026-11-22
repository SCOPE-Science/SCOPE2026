#!/usr/bin/env python3
"""Exact finite verification of one-deletion codes over signed permutations of order four.
All checks use integer arithmetic and the Python standard library.
"""
from itertools import permutations, product

BASE = (
    (-1, -2, -3, -4),
    (-1,  2,  3, -4),
    (-2, -1, -4, -3),
    (-2, -1,  4,  3),
    (-2,  1, -4,  3),
    (-3, -4, -1, -2),
    (-3,  4, -1,  2),
    (-3, -4,  2,  1),
    (-4, -3,  1,  2),
    (-4, -3, -2, -1),
)


def signed_permutations(n):
    return {
        tuple(a * s for a, s in zip(p, signs))
        for p in permutations(range(1, n + 1))
        for signs in product((-1, 1), repeat=n)
    }


def deletion(w, i):
    kept = w[:i] + w[i + 1:]
    ranks = {v: rank for rank, v in enumerate(sorted(abs(x) for x in kept), 1)}
    return tuple((1 if x > 0 else -1) * ranks[abs(x)] for x in kept)


def deck(w):
    return {deletion(w, i) for i in range(len(w))}


def inverse_insert(v, k, i, sign):
    # Insert signed absolute rank k in the given position; shift existing ranks >= k.
    lifted = tuple((1 if a > 0 else -1) * (abs(a) + (abs(a) >= k)) for a in v)
    return lifted[:i] + (sign * k,) + lifted[i:]


def twice_weight(v):
    signs = tuple(x > 0 for x in v)
    if signs[0] == signs[2] != signs[1]:
        return 0
    if signs[0] == signs[1] == signs[2] and (
        tuple(abs(x) for x in v) in ((1, 2, 3), (3, 2, 1))
    ):
        return 2
    return 1


def main():
    source = signed_permutations(4)
    received = signed_permutations(3)
    assert len(source) == 384 and len(received) == 48
    forward = {w: deck(w) for w in source}
    assert all(0 < len(b) <= 4 and b <= received for b in forward.values())

    # Independent inverse-channel incidence verification.
    reverse = {}
    for v in received:
        parents = {inverse_insert(v, rank, pos, sgn)
                   for rank in range(1, 5)
                   for pos in range(4)
                   for sgn in (-1, 1)}
        assert len(parents) == 26
        assert parents <= source
        reverse[v] = parents
    for w in source:
        assert forward[w] == {v for v in received if w in reverse[v]}

    # All 48 output weights and all 384 primal constraints, checked as integers.
    weight = {v: twice_weight(v) for v in received}
    assert {k: sum(x == k for x in weight.values()) for k in range(3)} == {0: 12, 1: 32, 2: 4}
    assert sum(weight.values()) == 40
    coverage = {w: sum(weight[v] for v in forward[w]) for w in source}
    assert min(coverage.values()) >= 2

    # Explicit symmetric code, including pairwise disjointness of whole deletion sets.
    code = set(BASE) | {tuple(-x for x in w) for w in BASE}
    assert len(code) == 20 and code <= source
    owner = {}
    for w in code:
        assert coverage[w] == 2  # each codeword meets the weight bound with equality
        for v in forward[w]:
            assert v not in owner, (w, owner.get(v), v)
            owner[v] = w
    assert len(owner) == 46
    assert received - set(owner) == {(3, -2, 1), (-3, 2, -1)}
    # Given any disjoint collection of decks C, 2*|C|<=total weight 40.
    print('VERIFY_OK source=384 received=48 weights=(12,32,4) total_twice_weight=40')
    print('VERIFY_OK dual_feasible=384 inverse_incidence=all_384_by_48')
    print('VERIFY_OK code=20 pairwise_disjoint_outputs=46 sign_invariant=True')


if __name__ == '__main__':
    main()
