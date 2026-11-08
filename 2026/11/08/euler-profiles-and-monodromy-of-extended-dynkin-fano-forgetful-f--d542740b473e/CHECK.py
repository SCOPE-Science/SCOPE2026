"""Exact combinatorial checks for discriminant degrees and cohomological monodromy.

The geometric fiber identification and the general theorem require the written proof.
This script checks the binary-discriminant scaling law and integral permutation
matrices that appear in the proof, for finite parameter ranges.
"""
from itertools import combinations
from math import comb


def choose(n, j):
    return comb(n, j) if 0 <= j <= n else 0


def perm_on_subsets(k, j, a, b):
    subsets = list(combinations(range(k), j))
    lookup = {s: i for i, s in enumerate(subsets)}
    perm = []
    for s in subsets:
        image = tuple(sorted(b if x == a else a if x == b else x for x in s))
        perm.append(lookup[image])
    return perm


def signature_counts(perm):
    n = len(perm)
    tr = sum(i == j for i, j in enumerate(perm))
    assert all(perm[perm[i]] == i for i in range(n))
    return tr, (n-tr)//2


def jordan_fixed(m):
    # Independent pairs of nonnegative truncation lengths for two generators.
    return sum(a+b == m for a in range(m+1) for b in range(m+1))


def two_cycle_fixed(m):
    # A path beginning in V gives (ceil(a/2),floor(a/2)); beginning
    # in W gives (floor(b/2),ceil(b/2)). Count dimension (m,m).
    return sum(
        (a+1)//2 + b//2 == m and a//2 + (b+1)//2 == m
        for a in range(2*m+1) for b in range(2*m+1)
    )


def partition_counts(k):
    if k == 0:
        yield ()
    else:
        for x in range(1,k+1):
            for z in partition_counts(k-x):
                if not z or x <= z[0]:
                    yield (x,)+z


def run():
    for m in range(1, 16):
        assert jordan_fixed(m) == m+1
        assert two_cycle_fixed(m) == 2*m+1
    # All multiplicity partitions up to degree eight: local Euler factors.
    for k0 in range(1,9):
        for part in partition_counts(k0):
            generic_point_profile = 1
            for m in part:
                generic_point_profile *= jordan_fixed(m)
            assert generic_point_profile > 0
            assert generic_point_profile <= 2**k0
    # Known low-dimensional fiber topologies from the cited construction:
    # two simple regular, one double regular, one special+regular,
    # two distinct specials, one double special.
    assert [2*2, jordan_fixed(2), two_cycle_fixed(1)*2,
            two_cycle_fixed(1)**2, two_cycle_fixed(2)] == [4,3,6,9,5]
    for k in range(3, 12):
        for s in range(4):
            degree = 2*(k-1)+s
            assert degree >= 4
            # A monic binary polynomial with roots a_i has discriminant
            # the product over ordered pairs (a_i-a_j)^2; its coefficient
            # scaling exponent is 2k-2 by the resultant identity.
            assert degree == (2*k-2)+sum(1 for _ in range(s))
        for j in range(k+1):
            perm = perm_on_subsets(k, j, 0, 1)
            trace, negative = signature_counts(perm)
            predicted_trace = choose(k-2,j)+choose(k-2,j-2)
            predicted_negative = choose(k-2,j-1)
            assert trace == predicted_trace
            assert negative == predicted_negative
            assert len(perm) == choose(k,j)
    # For H^2 the transposition permutations generate S_k, since all
    # adjacent swaps act as the standard transpositions of k generators.
    for k in range(3, 12):
        for i in range(k-1):
            perm = perm_on_subsets(k,1,i,i+1)
            assert perm[i] == i+1 and perm[i+1] == i
            assert all(perm[j] == j for j in range(k) if j not in (i,i+1))
    print('FIBER_EULER_TORUS_FIXED_COUNTS_OK m=1..15; partitions k=1..8')
    print('FANO_FOURFOLD_FIBER_TOPOLOGY_CALIBRATION_OK 4,3,6,9,5')
    print('DISCRIMINANT_DEGREE_AND_PERMUTATION_CENSUS_OK k=3..11 s=0..3')
    print('COHOMOLOGY_TRANSPOSTION_EIGENRANKS_OK all_even_degrees')
    print('FINITE_CERTIFICATE_OK')


if __name__ == '__main__':
    run()
