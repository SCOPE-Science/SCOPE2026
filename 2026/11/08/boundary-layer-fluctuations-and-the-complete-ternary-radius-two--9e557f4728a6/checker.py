#!/usr/bin/env python3
"""Independent finite checks for the uniform-multiset ball-volume law.

Run with Python 3.10 or later: python checker.py.
All computations use exact integers and rational arithmetic.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for v in range(n + 1):
            for tail in compositions(n-v, k-1):
                yield (v,) + tail


def difference_set(q, r):
    return [z for z in product(range(-r, r+1), repeat=q)
            if sum(z) == 0 and sum(max(a, 0) for a in z) <= r]


def displacement_volume(x, differences):
    return sum(all(a + b >= 0 for a, b in zip(x, z)) for z in differences)


def direct_volume(x, all_centers, r):
    return sum(sum(abs(a-b) for a, b in zip(x, y)) <= 2*r
               for y in all_centers)


def choose_nonnegative(N, K):
    return comb(N, K) if N >= K >= 0 else 0


def second_moment_count(n, q, differences):
    return sum(choose_nonnegative(n - sum(max(0, -z[i], -w[i])
                                               for i in range(q)) + q-1, q-1)
               for z in differences for w in differences)


def test():
    instances = 0
    for q in (2, 3, 4):
        for r in (1, 2, 3):
            differences = difference_set(q, r)
            h = [sum(z[0] < -s for z in differences) for s in range(r)]
            assert all(h[i] > h[i+1] for i in range(r-1)) and h[-1] > 0
            for n in range(max(q*r, 3), max(q*r, 3)+4):
                centers = list(compositions(n, q))
                sizes = []
                for x in centers:
                    a = direct_volume(x, centers, r)
                    b = displacement_volume(x, differences)
                    assert a == b, (q, r, n, x, a, b)
                    sizes.append(a)
                    instances += 1
                N = len(centers)
                assert sum(v*v for v in sizes) == second_moment_count(n, q, differences)
                assert max(sizes) == len(differences)
                assert sum(v == len(differences) for v in sizes) == choose_nonnegative(n-q*r+q-1,q-1)
    for n in range(6, 41):
        centers = list(compositions(n, 3))
        differences = difference_set(3, 2)
        counts = Counter(displacement_volume(x, differences) for x in centers)
        expected = {19: comb(n+2, 2)-6*n+9,
                    16: 3*(n-4), 13: 3,
                    12: 3*(n-3), 9: 6, 6: 3}
        assert counts == expected, (n, counts, expected)
        N = comb(n+2, 2)
        deficit = [19-displacement_volume(x, differences) for x in centers]
        assert Fraction(sum(deficit), N) == Fraction(30*n+18, N)
        assert Fraction(sum(t*t for t in deficit), N) == Fraction(174*n+666, N)
    assert [sum(z[0]<-s for z in difference_set(3, 2)) for s in range(2)] == [7,3]
    print('PASS direct-distance and difference-vector enumeration;', instances, 'centers')
    print('PASS exact ordered-pair second moments and interior-center counts')
    print('PASS all-length ternary radius-two frequency laws at n=6..40')


if __name__ == '__main__':
    test()
