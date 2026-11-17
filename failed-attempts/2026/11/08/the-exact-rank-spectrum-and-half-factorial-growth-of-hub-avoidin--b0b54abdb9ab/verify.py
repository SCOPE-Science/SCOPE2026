#!/usr/bin/env python3
"""Exact independent checks for cycle partial-automorphism rank enumeration.

No external modules, data files, or network access are required.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def rank_formula(n):
    """Cyclic-run coefficient formula, using exact rational arithmetic."""
    out = {0: 1, n: 2 * n}
    for k in range(1, n):
        total = Fraction(0)
        for r in range(1, min(k, n - k) + 1):
            ell = k - r
            coefficient = sum(
                comb(r, i) * comb(r + ell - i - 1, ell - i)
                for i in range(min(r, ell) + 1)
            )
            total += Fraction(
                n * n * factorial(r - 1) ** 2
                * comb(n - k - 1, r - 1) ** 2 * coefficient,
                factorial(r),
            )
        assert total.denominator == 1
        out[k] = int(total)
    return out


def signature(A, n):
    """Induced cycle-graph component sizes, derived from subsets directly."""
    A = set(A)
    if not A:
        return ()
    if len(A) == n:
        return (n + 1,)  # unique sentinel for the full cycle
    starts = [v for v in A if (v - 1) % n not in A]
    sizes = []
    for st in starts:
        size = 0
        v = st
        while v in A:
            size += 1
            v = (v + 1) % n
        sizes.append(size)
    return tuple(sorted(sizes))


def rank_by_subset_types(n):
    """Enumerate all domain subsets; count graph isomorphisms by actual types."""
    out = {}
    for k in range(n + 1):
        types = Counter(signature(A, n) for A in combinations(range(n), k))
        number = 0
        for t, multiplicity in types.items():
            if k == n:
                aut = 2 * n
            else:
                aut = 2 ** sum(z >= 2 for z in t)
                for z, m in Counter(t).items():
                    aut *= factorial(m)
            number += multiplicity * multiplicity * aut
        out[k] = number
    return out


def rank_by_actual_partial_maps(n):
    """Enumerate actual ordered partial injections; check every pair's adjacency."""
    out = Counter()
    for k in range(n + 1):
        for A in combinations(range(n), k):
            pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
            source_edges = [((A[i] - A[j]) % n in (1, n - 1)) for i, j in pairs]
            for B in combinations(range(n), k):
                for perm in permutations(B):
                    if all(
                        (((perm[i] - perm[j]) % n in (1, n - 1)) == adj)
                        for (i, j), adj in zip(pairs, source_edges)
                    ):
                        out[k] += 1
    return dict(out)


def extendible(n):
    """Deduplicate restrictions of all 2n dihedral wheel automorphisms."""
    elements = set()
    for a in range(n):
        for b in (-1, 1):
            p = tuple((a + b * i) % n for i in range(n))
            for mask in range(1 << n):
                elements.add(tuple((i, p[i]) for i in range(n) if mask >> i & 1))
    return len(elements)


def main():
    totals = {3: 34, 4: 97, 5: 286, 6: 955, 7: 3396,
              8: 12753, 9: 50482, 10: 208251}
    for n in range(3, 13):
        formula = rank_formula(n)
        assert formula == rank_by_subset_types(n), n
        if n in totals:
            assert sum(formula.values()) == totals[n], n
        if n <= 7:
            assert formula == rank_by_actual_partial_maps(n), n
            print(f'DIRECT_PARTIAL_MAPS_OK n={n} total={sum(formula.values())}')
        if 4 <= n <= 10:
            ext = extendible(n)
            assert 2 * n <= ext <= 2 * n * 2 ** n
            assert ext <= sum(formula.values())
            print(f'EXTENSIONS_OK n={n} extendible={ext} total={sum(formula.values())}')
    print('COEFFICIENT_AND_SUBSET_TYPES_OK n=3..12')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
