#!/usr/bin/env python3
"""Exact checks of the random master-priority Nash-product formula.
Run: python3 check.py
Only finite checks; the all-n proof is in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial


def model(n):
    perms = list(permutations(range(n)))
    signatures = Counter()
    total_product = 0
    total_square = 0
    num_profiles = 0
    for profile in product(perms, repeat=n):
        remaining = set(range(n))
        sig = []
        for ranking in profile:
            match = next(w for w in ranking if w in remaining)
            remaining.remove(match)
            sig.append(n - ranking.index(match))
        assert not remaining
        # All women agree on the priority order 0,1,...,n-1, so their
        # utility product is n! regardless of the selected matching.
        val = factorial(n)
        for u in sig:
            val *= u
        num_profiles += 1
        total_product += val
        total_square += val * val
        signatures[tuple(sig)] += 1
    assert num_profiles == factorial(n) ** n
    # Exact joint law: the man with k remaining women has the maximum
    # of a uniform k-subset of {1,...,n}, independently across men.
    for sig, multiplicity in signatures.items():
        p = Fraction(1)
        for j, u in enumerate(sig):
            k = n-j
            p *= Fraction(comb(u-1, k-1), comb(n,k))
        assert Fraction(multiplicity,num_profiles) == p, (n,sig,p)
    expected = Fraction(total_product,num_profiles)
    assert expected == factorial(n) * (n+1) ** (n-1), (n, expected)
    # Second moment derived using the exact finite-population variance.
    e2 = Fraction(factorial(n) ** 2)
    for k in range(1,n+1):
        e2 *= Fraction((n+1)**2 * k,(k+2)) * (1-Fraction(1,(n+1)*(k+1)))
    assert Fraction(total_square,num_profiles) == e2
    print(f"n={n} profiles={num_profiles} signature_atoms={len(signatures)} first={expected} second={e2} PASS")


if __name__ == '__main__':
    for n in range(1,5):
        model(n)
    print('ALL EXACT FINITE CHECKS PASS')
