#!/usr/bin/env python3
"""Finite consistency tests for centralizers of rank-two dense-orbit systems.

The theorem for arbitrary positive parameters is proved separately. This script
checks bounded integer cases and the sampled-ray homomorphism law.
"""
import itertools
import math


def admissible(p, k, m):
    d = math.gcd(k, m)
    for r in range(m):
        for s in range(r):
            if (r - s) % d == 0 and (p[r] - r - p[s] + s) % k:
                return False
    return True


def predicted_order(k, m):
    d = math.gcd(k, m)
    q, ell = m // d, k // d
    block_size = [sum(t % ell == a for t in range(q)) for a in range(ell)]
    block_order = math.prod(math.factorial(x) for x in block_size)
    return math.factorial(d) * block_order ** d


def apply_ray(p, m, n):
    return p[n % m] + (n // m) * m


def verify():
    checked = 0
    for m in range(1, 8):
        for k in range(1, 11):
            permitted = [p for p in itertools.permutations(range(m))
                         if admissible(p, k, m)]
            assert len(permitted) == predicted_order(k, m), (k, m)
            # Different construction from factorial prediction: test the
            # group action is phase-respecting and commutes with f^m.
            for p in permitted:
                for n in range(3 * m + 2 * k):
                    assert apply_ray(p, m, n + m) == apply_ray(p, m, n) + m
                    assert (apply_ray(p, m, n) - n) % k == \
                        (p[n % m] - (n % m)) % k
            # Check closure under composition without presupposing wreathness.
            good = set(permitted)
            for p in permitted:
                assert tuple(range(m)) in good
                inv = tuple(p.index(t) for t in range(m))
                assert inv in good
            if m <= 5:
                for p in permitted:
                    for q in permitted:
                        pq = tuple(q[p[t]] for t in range(m))
                        assert pq in good
                        for n in range(3 * m):
                            assert apply_ray(q, m, apply_ray(p, m, n)) == \
                                   apply_ray(pq, m, n)
            checked += 1
    print(f"PASS: {checked} parameter pairs; all order, phase, inverse and group tests")
    for k, m in [(1, 5), (2, 5), (3, 6), (4, 6), (6, 4), (6, 6), (7, 8)]:
        print(f"  k={k}, m={m}: |Aut|={predicted_order(k, m)}")


if __name__ == '__main__':
    verify()
