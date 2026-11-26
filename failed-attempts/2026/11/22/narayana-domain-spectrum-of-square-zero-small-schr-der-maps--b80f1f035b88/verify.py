#!/usr/bin/env python3
"""Direct square-zero census in the finite isotone regressive partial-map semigroup.
This script uses only Python's standard library.  It does not assume the formula
it checks: it enumerates maps from their domains and all admissible images.
"""
from itertools import combinations, product
from fractions import Fraction
from math import comb


def narayana(n, k):
    assert n >= 1 and 0 <= k < n
    return comb(n, k) * comb(n-1, k) // (k+1)


def bruteforce(n):
    # Each map is represented by (increasing domain, nondecreasing image word).
    domain_counts = [0] * n
    nilpotents = 0
    for k in range(n):
        for domain in combinations(range(2, n+1), k):
            for values in product(*(range(1, d+1) for d in domain)):
                if tuple(sorted(values)) != values:
                    continue  # not isotone
                if all(v < d for d,v in zip(domain,values)):
                    nilpotents += 1
                if set(domain).isdisjoint(values):
                    domain_counts[k] += 1
    return domain_counts, nilpotents


def large_schroder(n):
    if n == 0: return 1
    if n == 1: return 2
    r0, r1 = 1, 2
    for j in range(2, n+1):
        numerator = 3*(2*j-1)*r1 - (j-2)*r0
        assert numerator % (j+1) == 0
        r0, r1 = r1, numerator//(j+1)
    return r1


def direct_two_row(n, k):
    # Independent plane-partition/sequence-pair census.
    m = n-k
    if k == 0: return 1
    count = 0
    for upper in combinations_with_replacement(range(1,m+1), k):
        for lower in combinations_with_replacement(range(1,m+1), k):
            if all(j<=x for j,x in zip(lower,upper)):
                count += 1
    return count

from itertools import combinations_with_replacement

def run():
    total_maps_checked = 0
    for n in range(2, 10):
        got, nilpotents = bruteforce(n)
        expected = [narayana(n,k) for k in range(n)]
        assert got == expected, (n, got, expected)
        assert nilpotents == large_schroder(n-1), (n,nilpotents)
        assert sum(got) == comb(2*n,n)//(n+1)
        for k in range(n):
            assert got[k] == direct_two_row(n,k), (n,k)
        t = sum(got)
        mean = sum(Fraction(k * got[k], t) for k in range(n))
        variance = sum(Fraction((k-mean)**2 * got[k],t) for k in range(n))
        assert mean == Fraction(n-1,2), (n,mean)
        assert variance == Fraction(n*n-1,4*(2*n-1)), (n,variance)
        print(f'n={n} domain_counts={got} square_zero={t} nilpotent={nilpotents}')
    print('VERIFY_OK')

if __name__=='__main__':run()
