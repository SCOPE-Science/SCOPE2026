#!/usr/bin/env python3
"""Independent direct exact attractor computation for five-run palindromes."""
from itertools import combinations, product


def masks_of_factors(w):
    n = len(w)
    occurrence_masks = {}
    for left in range(n):
        for right in range(left + 1, n + 1):
            factor = w[left:right]
            covered = ((1 << right) - 1) ^ ((1 << left) - 1)
            occurrence_masks[factor] = occurrence_masks.get(factor, 0) | covered
    return tuple(occurrence_masks.values())


def attracts(factor_masks, positions):
    selected = sum(1 << p for p in positions)
    return all(selected & mask for mask in factor_masks)


def claimed(a, b, c):
    return 3 if a >= 2 and b >= 2 and c < a else 2


def proof_positions(a, b, c):
    if c >= a:
        return (a + b - 1, a + b + c - 1)
    if b == 1:
        return (a - 1, a + b + c)
    return (a - 1, a + b, a + 2*b + c - 1)


def run():
    cases = checked_pairs = 0
    for a, b, c in product(range(1, 7), repeat=3):
        w = '0'*a + '1'*b + '0'*c + '1'*b + '0'*a
        masks = masks_of_factors(w)
        k = claimed(a, b, c)
        assert attracts(masks, proof_positions(a, b, c)), (a, b, c, 'witness')
        assert not any(attracts(masks, (p,)) for p in range(len(w)))
        if k == 3:
            assert not any(attracts(masks, pair) for pair in combinations(range(len(w)), 2)), (a, b, c, 'unexpected pair')
            checked_pairs += len(w)*(len(w)-1)//2
        else:
            assert any(attracts(masks, pair) for pair in combinations(range(len(w)), 2)), (a, b, c, 'no pair')
        cases += 1
    print(f'EXHAUSTIVE_OK triples={cases} rejected_pairs_in_three_regime={checked_pairs} parameter_range=1..6')

if __name__ == '__main__':
    run()
