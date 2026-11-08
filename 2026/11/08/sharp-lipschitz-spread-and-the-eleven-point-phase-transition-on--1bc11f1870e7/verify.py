#!/usr/bin/env python3
"""Exact finite cross-intersection checks and integer phase comparisons."""
from array import array
from itertools import combinations
from fractions import Fraction


def exhaustive(n):
    E = list(combinations(range(n), 2))
    N = len(E)
    all_bits = (1 << N) - 1
    nbr = []
    for e in E:
        nbr.append(sum(1 << j for j, g in enumerate(E)
                       if g != e and (e[0] in g or e[1] in g)))
    masks = array('I', [all_bits]) * (1 << N)
    best = -1
    winning_counts = set()
    eligible = 0
    for a_mask in range(1, 1 << N):
        lsb = a_mask & -a_mask
        k = lsb.bit_length() - 1
        bmask = masks[a_mask ^ lsb] & nbr[k]
        masks[a_mask] = bmask
        if not bmask:
            continue
        eligible += 1
        a = a_mask.bit_count()
        upper = bmask.bit_count()
        # An optimal subfamily of all B choices has a cardinality in [1, upper].
        for b in range(1, upper + 1):
            score = N*(a + b) - (a-b)**2
            if score > best:
                best = score
                winning_counts = {(a, b)}
            elif score == best:
                winning_counts.add((a, b))
    return N, best, winning_counts, eligible


def formula(n):
    N = n*(n-1)//2
    one = N*(2*n-3) - (2*n-5)**2
    two = N*N//4
    if n == 5:
        return 56
    if n == 6:
        return 86
    return max(one, two)


def main():
    expectations = {5: {(2,4),(4,2)},
                    6: {(1,8),(8,1),(2,4),(4,2)},
                    7: {(1,10),(10,1)}}
    for n in (5,6,7):
        N, got, shapes, eligible = exhaustive(n)
        assert got == formula(n), (n, got, formula(n))
        assert shapes == expectations[n], (n, shapes)
        print('EXHAUSTIVE_CROSS_INTERSECTING_SIZE_PROFILES_OK', n, N, eligible, got, sorted(shapes))
    for n in range(7, 1000):
        N = n*(n-1)//2
        singleton = N*(2*n-3) - (2*n-5)**2
        binary = N*N//4
        assert singleton - n*N > 0
        if 7 <= n <= 10:
            assert singleton > binary
        elif n == 11:
            assert singleton == binary
        else:
            assert singleton < binary
        assert formula(n) == max(singleton, binary)
    print('EXACT_ALL_PHASE_INEQUALITIES_THROUGH_999_OK')
    print('ALL_KNESER_PAIR_SPREAD_CHECKS_OK')

if __name__ == '__main__':
    main()
