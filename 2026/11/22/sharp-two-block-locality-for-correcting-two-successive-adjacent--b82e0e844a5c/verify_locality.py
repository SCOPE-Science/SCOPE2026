#!/usr/bin/env python3
"""Independent exhaustive block-set check for the two-swap concatenation criterion."""
from itertools import product, combinations


def distance(x, y):
    if x.count('1') != y.count('1'):
        return None
    imbalance = 0
    cost = 0
    for a, b in zip(x, y):
        imbalance += (a == '1') - (b == '1')
        cost += abs(imbalance)
    return cost


def first_collision(P, m):
    by_weight = {}
    for blocks in product(P, repeat=m):
        word = ''.join(blocks)
        by_weight.setdefault(word.count('1'), []).append(word)
    for group in by_weight.values():
        for x, y in combinations(group, 2):
            d = distance(x, y)
            if d is not None and d <= 4:
                return (x, y, d)
    return None


if __name__ == '__main__':
    for b in range(1, 5):
        alphabet = [''.join(bits) for bits in product('01', repeat=b)]
        safe_count = 0
        maximal_set_size = 0
        checked_powers = 0
        for mask in range(1, 1 << len(alphabet)):
            P = tuple(w for i, w in enumerate(alphabet) if mask & (1 << i))
            if first_collision(P, 2) is not None:
                continue
            safe_count += 1
            maximal_set_size = max(maximal_set_size, len(P))
            for m in (3, 4, 5):
                assert first_collision(P, m) is None, (P, m)
                checked_powers += 1
        print(f'block_length={b} two_block_safe_families={safe_count} largest_safe_set={maximal_set_size} later_powers_checked={checked_powers}')
    # Sharpness of the horizon: one-block correction need not imply two-block correction.
    assert first_collision(('0', '1'), 1) is None
    assert first_collision(('0', '1'), 2) == ('01', '10', 1)
    print('PASS exhaustive block-set locality through block length four; sharp binary block-length-one witness')
