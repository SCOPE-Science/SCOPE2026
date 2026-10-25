#!/usr/bin/env python3
"""Recompute signed simplicial Lefschetz traces for cycle matching complexes.
No input files or nonstandard packages.  Run: python3 dihedral_cycle_verify.py
"""
from math import gcd


def homology_degree(n):
    if n % 3 == 0:
        return n // 3 - 1
    if n % 3 == 1:
        return (n - 1) // 3 - 1
    return (n - 2) // 3


def path_value(t):
    x, y = 1, 0
    if t == 0:
        return x
    if t == 1:
        return y
    for _ in range(2, t + 1):
        x, y = y, y - x
    return y


def cycle_value(h):
    return (2, 1, -1, -2, -1, 1)[h % 6]


def predicted(n, kind, k):
    mult = (-1) ** (homology_degree(n) + 1)
    if kind == 'r':
        return mult * cycle_value(gcd(n, k))
    if n & 1:
        t = (n - 1) // 2
    elif k & 1:
        t = n // 2 - 2
    else:
        t = n // 2 + 1
    return mult * path_value(t)


def independent_masks(n):
    return [mask for mask in range(1, 1 << n)
            if not (mask & ((mask << 1) | (mask >> (n - 1))
                            | (mask >> 1) | ((mask & 1) << (n - 1))))]


def direct_reduced_trace(n, masks, perm):
    total = -1  # The empty face in the augmented chain complex.
    for mask in masks:
        face = [i for i in range(n) if (mask >> i) & 1]
        image = [perm[i] for i in face]
        if sorted(image) != face:
            continue
        inversions = sum(image[i] > image[j]
                         for i in range(len(image))
                         for j in range(i + 1, len(image)))
        total += (-1) ** (len(face) - 1 + inversions)
    return total


def gf2_ranks(n, masks):
    from collections import defaultdict
    groups = defaultdict(list)
    groups[0] = [0]  # The empty face, with one augmented -1 generator.
    for mask in masks:
        groups[mask.bit_count()].append(mask)
    boundaries = {}
    for size in range(1, max(groups) + 1):
        smaller = {f: i for i, f in enumerate(groups[size - 1])}
        basis = {}
        for mask in groups[size]:
            column = 0
            temp = mask
            while temp:
                bit = temp & -temp
                temp -= bit
                column ^= 1 << smaller[mask ^ bit]
            while column:
                pivot = column.bit_length() - 1
                if pivot in basis:
                    column ^= basis[pivot]
                else:
                    basis[pivot] = column
                    break
        boundaries[size] = len(basis)
    betti = {size - 1: len(group) - boundaries.get(size, 0)
             - boundaries.get(size + 1, 0)
             for size, group in groups.items()}
    assert betti[-1] == 0, (n, betti)
    nonzero = {k: v for k, v in betti.items() if v and k >= 0}
    return nonzero


def main():
    total = 0
    homology_tests = 0
    for n in range(3, 19):
        masks = independent_masks(n)
        for kind in ('r', 's'):
            for k in range(n):
                perm = ([(i + k) % n for i in range(n)] if kind == 'r'
                        else [(k - i) % n for i in range(n)])
                direct = direct_reduced_trace(n, masks, perm)
                expected = (-1) ** homology_degree(n) * predicted(n, kind, k)
                assert direct == expected, (n, kind, k, direct, expected)
                total += 1
        if n <= 15:
            expected_dim = 2 if n % 3 == 0 else 1
            assert gf2_ranks(n, masks) == {homology_degree(n): expected_dim}, n
            homology_tests += 1
        print('n=', n, 'faces=', len(masks), 'elements=', 2 * n, 'OK')
    print('VERIFY_OK signed-traces=', total, 'GF2-homology=', homology_tests)


if __name__ == '__main__':
    main()
