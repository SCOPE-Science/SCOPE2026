#!/usr/bin/env python3
"""Exact Walsh spectrum of the rank-three projective-plane matroid PG(2,3).

Run with Python 3 standard library: python3 verify_pg23.py
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def canonical(v):
    for a in v:
        if a != 0:
            return tuple(a * x % 3 for x in v)
    return None


def determinant3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0])) % 3


def krawtchouk3(k, m):
    return sum((-1)**j * comb(k, j) * comb(m-k, 3-j)
               for j in range(4) if j <= k and 3-j <= m-k)


def fwht(a):
    a = a[:]
    h = 1
    while h < len(a):
        for i in range(0, len(a), h*2):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def check():
    pts = sorted({canonical(v) for v in product(range(3), repeat=3)} - {None})
    assert len(pts) == 13
    lines = sorted({tuple(i for i, p in enumerate(pts)
                          if sum(x*y for x, y in zip(p, a)) % 3 == 0)
                    for a in pts})
    assert len(lines) == 13 and all(len(L) == 4 for L in lines)
    assert all(sum(i in L and j in L for L in lines) == 1
               for i,j in combinations(range(13),2))
    line_masks = [sum(1 << i for i in L) for L in lines]

    # First path: all 286 triples are tested by a direct determinant over F_3.
    f = [0] * (1 << 13)
    for T in combinations(range(13), 3):
        if determinant3(*(pts[i] for i in T)) != 0:
            f[sum(1 << i for i in T)] = 1
    assert sum(f) == 234
    degrees = [sum(f[mask] for mask in range(1<<13) if mask>>i & 1)
               for i in range(13)]
    assert degrees == [54]*13
    W = fwht(f)

    # Second path: complement of collinear triples, with line-intersection data.
    W2 = []
    for S in range(1 << 13):
        val = krawtchouk3(S.bit_count(), 13) - sum(
            krawtchouk3((S & L).bit_count(), 4) for L in line_masks)
        W2.append(val)
    assert W == W2
    assert all(w % 4 == 2 for w in W)
    assert all(W[S ^ ((1 << 13)-1)] == -W[S] for S in range(1 << 13))
    assert sum(w*w for w in W) == (1 << 13) * 234

    # Complete signed histogram, independently reproduced by each evaluation path.
    positive_half = {234:1,126:13,54:78,18:611,14:234,10:1872,6:1053,2:234}
    expected = dict(positive_half)
    expected.update({-k:v for k,v in positive_half.items()})
    assert dict(Counter(W)) == expected

    # Refined shell data. Remaining shells are negatives of complementary shells.
    shells = [
        {234:1},
        {126:13},
        {54:78},
        {10:234,18:52},
        {-14:234,-6:468,18:13},
        {-18:468,-10:702,6:117},
        {-18:78,-10:936,-2:234,6:468},
    ]
    for k, expected_shell in enumerate(shells):
        assert dict(Counter(W[S] for S in range(1<<13)
                            if S.bit_count()==k)) == expected_shell

    witness = sum(1 << i for i in (0,1,3,4,5,7))
    assert witness.bit_count() == 6 and W[witness] == -2
    assert min(abs(w) for w in W) == 2
    assert max(abs(w) for w in W) == 234
    assert len({k for k in W}) == 16
    assert sum(w > 0 for w in W) == sum(w < 0 for w in W) == 4096
    print('PG23_WALSH_PASS')
    print('points=13 lines=13 bases=234 frequencies=8192 zero=0')
    print('sharp_gap=2 norm_inverse=1/2 condition_number=117')
    print('positive_multiplicities=', dict(sorted(positive_half.items())))
    print('witness_indices_0_based=0,1,3,4,5,7 witness_eigenvalue=-2')


if __name__ == '__main__':
    check()
