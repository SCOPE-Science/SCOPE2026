#!/usr/bin/env python3
"""Exact finite certificate for the three-prime adjacent-pair obstruction."""
from itertools import combinations_with_replacement, product
from math import gcd

LENGTH = 14
FULL = (1 << LENGTH) - 1
SMALL = (3, 5, 7, 11, 13)
LARGE = 17  # represents every prime at least 17

# At prime p, a phase r eliminates exactly i = r,r+1 modulo p.
def local_masks(p):
    if p == LARGE:
        return tuple(sorted({0, *(1 << i for i in range(LENGTH)),
                             *(3 << i for i in range(LENGTH - 1))}))
    return tuple(sum(1 << i for i in range(LENGTH)
                     if i % p == r or i % p == (r + 1) % p)
                 for r in range(p))


def analyze():
    masks = {p: local_masks(p) for p in SMALL + (LARGE,)}
    records = []
    extremal = []
    for triple in combinations_with_replacement(SMALL + (LARGE,), 3):
        if any(triple.count(p) > 1 for p in SMALL):
            continue
        maximum, count = 0, 0
        for triple_masks in product(*(masks[p] for p in triple)):
            mask = triple_masks[0] | triple_masks[1] | triple_masks[2]
            maximum = max(maximum, mask.bit_count())
            if mask == FULL:
                count += 1
                extremal.append((triple, triple_masks))
        records.append((triple, maximum, count))
    assert len(records) == 26
    # Confirm every reported table entry against fixed expected certificate data.
    expected_max = (14, 13, 13, 13, 13, 13, 13, 12, 12, 12, 12,
                    11, 11, 11, 11, 11, 10, 10, 10, 10, 9, 8, 8, 8, 7, 6)
    assert tuple(maximum for _, maximum, _ in records) == expected_max, (tuple(maximum for _, maximum, _ in records), expected_max)
    assert tuple(count for _, _, count in records) == (2,) + (0,) * 25
    assert sum(c for _, _, c in records) == 2
    assert [triple for triple, _, count in records if count] == [(3, 5, 7)]
    # Independent direct CRT-period verification: both and only both starts.
    starts = [a for a in range(105)
              if all(gcd((a+i)*(a+i+1),105)>1 for i in range(LENGTH))]
    assert starts == [2,89], starts
    for a in starts:
        assert gcd((a-1)*a, 105) == 1
        assert gcd((a+14)*(a+15), 105) == 1
    # Independent direct period-by-period sanity checks for sample supports.
    for primes in ((3, 5, 7), (3, 5, 11), (3, 7, 11),
                   (3, 5, 17), (5, 7, 11), (3, 5, 19)):
        modulus = primes[0] * primes[1] * primes[2]
        local_longest = max(sum(1 for j in range(LENGTH)
                                if all(gcd((a+i)*(a+i+1), modulus)>1
                                       for i in range(j+1)))
                            for a in range(modulus))
        if modulus == 105:
            assert local_longest == LENGTH
        else:
            assert local_longest < LENGTH
    assert (3,5,7) in [r[0] for r in records]
    assert all(not count for triple, _, count in records if triple != (3,5,7))
    return records, starts


def main():
    records, starts = analyze()
    for triple, maximum, count in records:
        names = ','.join('large' if p == LARGE else str(p) for p in triple)
        print(f'{names:>17}: max={maximum:2d}, complete={count}')
    print('Complete-start residues modulo 105:', starts)
    print('PASS: all 26 possible prime-class triples exhausted')


if __name__ == '__main__':
    main()
