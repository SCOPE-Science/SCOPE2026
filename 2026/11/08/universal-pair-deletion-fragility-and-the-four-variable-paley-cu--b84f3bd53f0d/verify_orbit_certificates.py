#!/usr/bin/env python3
"""Compact independent residue-set checks of six orbit certificates.
The tests use multiplicative character signs, not the adjacency-mask census.
"""

CERTIFICATES = [
    (29, (0,1), (3,11,24), '001'),
    (29, (0,2), (1,6,7), '111'),
    (37, (0,1), (6,14,19), '000'),
    (37, (0,2), (1,11,27), '111'),
    (41, (0,1), (5,21,37), '111'),
    (41, (0,3), (15,22,29), '000'),
]


def verify(p, forbidden, triple, pattern):
    assert p % 4 == 1
    sq = {x*x % p for x in range(1,p)}
    assert len(sq) == (p-1)//2
    assert not (set(forbidden) & set(triple))
    expected = set(forbidden)
    choices = {
        z for z in range(p)
        if z not in triple and all(
            ((z - anchor) % p in sq) == (flag == '1')
            for anchor, flag in zip(triple,pattern)
        )
    }
    assert choices == expected, (p, forbidden, triple, pattern, sorted(choices))
    if forbidden[1] == 1:
        assert forbidden[1] in sq
    else:
        assert forbidden[1] not in sq
    return {'q':p,'pair':forbidden,'base_triple':triple,'adjacency_pattern':pattern,'unique_witness_set':sorted(choices)}


def main():
    for p, pair, triple, pattern in CERTIFICATES:
        print(verify(p,pair,triple,pattern))
    print('PASS: one adjacent-pair and one nonadjacent-pair certificate at each order; affine square-scaling acts transitively on each type.')

if __name__ == '__main__':
    main()
