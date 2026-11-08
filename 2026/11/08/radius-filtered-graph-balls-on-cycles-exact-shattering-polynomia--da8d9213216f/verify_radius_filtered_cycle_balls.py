#!/usr/bin/env python3
"""Standalone finite trace verifier for radius-filtered graph balls on cycles.

Run: python3 verify_radius_filtered_cycle_balls.py
No third-party dependencies.
"""
from itertools import combinations
from math import comb


def choose2(z):
    return z * (z-1) // 2 if z >= 2 else 0


def bounded_three_compositions(n, u):
    """Count ordered positive triples summing to n, each at most u."""
    return sum((-1)**j * comb(3, j) * choose2(n-j*u-1)
               for j in range(4))


def predicted(n, R):
    assert n >= 3 and 0 <= R <= n//2
    s1 = n
    if 2*R >= n//2:
        s2 = comb(n, 2)
    else:
        s2 = 2*R*n
    if n == 3:
        s3 = 0
    elif R == n//2:
        s3 = comb(n, 3) - (n if n % 2 else 0)
    elif 4*R < n:
        s3 = 0
    else:
        t = (bounded_three_compositions(n, 2*R)
             - bounded_three_compositions(n, n-2*R-1))
        assert (n*t) % 3 == 0
        s3 = n*t//3
    return (1, s1, s2, s3, 0)


def trace_count(balls, positions):
    signatures = set()
    for ball in balls:
        signature = 0
        for i, p in enumerate(positions):
            if ball & (1 << p):
                signature |= (1 << i)
        signatures.add(signature)
        if len(signatures) == 1 << len(positions):
            return True
    return False


def cyclic_gaps(n, tri):
    a,b,c = tri
    return b-a, c-b, n-c+a


def predicted_triple(n, R, tri):
    if n == 3:
        return False
    gaps = cyclic_gaps(n, tri)
    if R == n//2:
        return n % 2 == 0 or max(gaps) <= n-3
    return n-2*R <= max(gaps) <= 2*R


def main():
    families = 0
    supports = 0
    triples = 0
    for n in range(3, 21):
        for R in range(n//2 + 1):
            masks = set()
            for r in range(R+1):
                for center in range(n):
                    mask = sum(1 << ((center+t) % n)
                               for t in range(-r, r+1))
                    masks.add(mask)
            observed = [1]
            for k in range(1, 5):
                count = 0
                for pos in combinations(range(n), k):
                    shattered = trace_count(masks, pos)
                    if k == 3:
                        assert shattered == predicted_triple(n, R, pos), (n, R, pos)
                        triples += 1
                    count += shattered
                    supports += 1
                observed.append(count)
            expected = predicted(n, R)
            assert tuple(observed) == expected, (n, R, observed, expected)
            families += 1
    print(f'ALL_CYCLE_BALL_SHATTERING_CHECKS_PASS {families} families {supports} supports {triples} triples')
    for n,R in [(8,2),(9,3),(12,3),(12,4),(17,5),(20,5),(20,9)]:
        print(f'n={n} R={R} coefficients={predicted(n,R)}')

if __name__ == '__main__':
    main()
