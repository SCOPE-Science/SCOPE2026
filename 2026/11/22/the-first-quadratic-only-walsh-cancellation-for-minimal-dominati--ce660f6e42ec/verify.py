#!/usr/bin/env python3
"""Exact integer certificate for Fourier recovery of minimal dominating sets of paths.

No nonstandard dependencies. Run: python3 verify.py
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256


def neighborhoods(n):
    return tuple(sum(1 << j for j in range(max(0, i-1), min(n, i+2)))
                 for i in range(n))


def by_private_neighbors(n):
    """Exhaustive subset scan using the private-neighbor characterization."""
    H = neighborhoods(n)
    out = []
    for x in range(1, 1 << n):
        if any((x & h) == 0 for h in H):
            continue
        good = True
        for i in range(n):
            if x & (1 << i):
                if not any((x & H[j]) == (1 << i)
                           for j in range(max(0, i-1), min(n, i+2))):
                    good = False
                    break
        if good:
            out.append(x)
    return out


def by_minimal_transversals(n):
    """Berge-style incremental minimal hitting sets of all closed neighborhoods."""
    family = {0}
    for H in neighborhoods(n):
        enlarged = set()
        for x in family:
            if x & H:
                enlarged.add(x)
            else:
                for v in range(n):
                    if H & (1 << v):
                        enlarged.add(x | (1 << v))
        # Keep exactly the inclusion-minimal partial transversals.
        family = {x for x in enlarged
                  if not any(y != x and (y & x) == y for y in enlarged)}
    return sorted(family)


def walsh(values):
    a = values[:]
    h = 1
    while h < len(a):
        for b in range(0, len(a), 2*h):
            for j in range(b, b+h):
                u, v = a[j], a[j+h]
                a[j], a[j+h] = u+v, u-v
        h *= 2
    return a


def main():
    first_singular_without_linear_zeros = None
    observed = []
    for n in range(1, 18):
        A = by_private_neighbors(n)
        B = by_minimal_transversals(n)
        assert A == B, (n, len(A), len(B))
        N = 1 << n
        kernel = [0] * N
        for x in A:
            kernel[x] = 1
        W = walsh(kernel)
        zeros = [j for j, w in enumerate(W) if w == 0]
        zero_singletons = [i+1 for i in range(n) if W[1 << i] == 0]
        observed.append((n, len(A), len(zeros), len(zero_singletons)))
        if zeros and not zero_singletons and first_singular_without_linear_zeros is None:
            first_singular_without_linear_zeros = n
        if n == 17:
            assert len(A) == 268
            assert len(zeros) == 19516
            assert all(W[1 << i] for i in range(n))
            assert min(j.bit_count() for j in zeros) == 2
            pairs = [(i+1, j+1) for i in range(n) for j in range(i+1, n)
                     if W[(1 << i) | (1 << j)] == 0]
            expected = [(1,16),(1,17),(2,16),(2,17),(3,5),(3,7),(3,8),
                        (3,11),(3,12),(4,14),(6,15),(7,15),(10,15),(11,15),(13,15)]
            assert pairs == expected
            assert sorted((abs(w) for w in W if w))[:1] == [2]
            assert max(abs(w) for w in W) == 268
            E = walsh([int(w != 0) for w in W])
            assert sum(abs(z) for z in E) == 3341768
            projection_norm = Fraction(sum(abs(z) for z in E), N)
            assert projection_norm == Fraction(417721, 16384)
            assert sum(Counter(j.bit_count() for j in zeros).values()) == 19516
            print('P17: count=268, nullity=19516, rank=111556, min-zero-degree=2')
            print('P17: zero-pairs=' + str(pairs))
            print('P17: least nonzero Walsh modulus=2, maximum modulus=268')
            print('P17: sharp endpoint projection norm=' + str(projection_norm))
            print('P17: set-list SHA256=' + sha256(','.join(map(str,A)).encode()).hexdigest())
            print('P17: zero-degree distribution=' + str(sorted(Counter(j.bit_count() for j in zeros).items())))
    assert first_singular_without_linear_zeros == 17
    assert observed == [
        (1,1,0,0),(2,2,2,2),(3,2,4,3),(4,4,12,4),
        (5,4,12,4),(6,7,0,0),(7,9,0,0),(8,13,0,0),
        (9,18,152,6),(10,25,0,0),(11,36,952,4),
        (12,49,0,0),(13,70,1848,2),(14,97,0,0),
        (15,137,0,0),(16,191,0,0),(17,268,19516,0)]
    print('P1..P17: (n, minimal dominating sets, zero modes, zero singleton modes)')
    print(observed)
    print('PASS')

if __name__ == '__main__':
    main()
