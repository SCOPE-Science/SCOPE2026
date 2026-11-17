#!/usr/bin/env python3
"""Exact finite checks for the Catalan commuting-idempotent profile.

No external packages required. Infinite statements follow from the written proof.
"""
from collections import Counter
from itertools import product
from math import comb


def all_catalan_maps(n):
    """Directly enumerate weakly increasing regressive maps."""
    def extend(prefix):
        i = len(prefix) + 1
        if i > n:
            yield tuple(prefix)
            return
        lower = prefix[-1] if prefix else 1
        for y in range(lower, i + 1):
            yield from extend(prefix + [y])
    return list(extend([]))


def direct_profile(n):
    maps = []
    for mask in range(1 << (n - 1)):
        fixed = frozenset([1] + [i + 2 for i in range(n-1) if mask & (1 << i)])
        image = tuple(max(t for t in fixed if t <= j) for j in range(1, n+1))
        maps.append((fixed, image))
    profile = Counter()
    centers = {}
    for fixed, f in maps:
        centralizer_size = 0
        for other, g in maps:
            fg = tuple(f[g[i]-1] for i in range(n))
            gf = tuple(g[f[i]-1] for i in range(n))
            if fg == gf:
                centralizer_size += 1
                profile[(len(fixed-other), len(other-fixed), len(fixed & other)-1)] += 1
                meet = fixed & other
                want = tuple(max(t for t in meet if t <= j) for j in range(1,n+1))
                assert fg == want
        centers[fixed] = centralizer_size
    return profile, centers


def gap_profile(n):
    """A distinct method: enumerate sequences of marked gaps and their colors."""
    parts = {}
    for d in range(1, n+1):
        # The two monochromatic weights both contain the all-unoccupied
        # configuration; subtract its extra occurrence.
        weights = Counter({(0,0): 1})
        for i in range(1,d):
            weights[(i,0)] += comb(d-1,i)
            weights[(0,i)] += comb(d-1,i)
        parts[d] = weights
    out = Counter()
    def visit(used, k, a, b, multiplicity):
        if used == n:
            out[(a,b,k-1)] += multiplicity
            return
        for d in range(1,n-used+1):
            for (da,db),ways in parts[d].items():
                visit(used+d,k+1,a+da,b+db,multiplicity*ways)
    visit(0,0,0,0,1)
    return out


def exact_centralizer(n, fixed):
    s = sorted(fixed)
    result = 0
    for mid in product([0,1], repeat=len(s)-1):
        selected = [1] + list(mid)
        free = sum((s[i+1]-s[i]-1)*selected[i]*selected[i+1]
                   for i in range(len(s)-1)) + (n-s[-1])*selected[-1]
        result += 1 << free
    return result


def main():
    for n in range(1,8):
        cat = all_catalan_maps(n)
        predicted = {tuple(max(t for t in ([1] + [i+2 for i in range(n-1)
                           if (mask >> i) & 1]) if t <= j)
                           for j in range(1,n+1))
                     for mask in range(1<<(n-1))}
        ids = {f for f in cat if tuple(f[f[i]-1] for i in range(n)) == f}
        assert ids == predicted, (n,ids^predicted)
        print('IDEMPOTENTS_OK', n, len(cat), len(ids))

    previous2, previous1 = None, None
    for n in range(1,10):
        actual, centers = direct_profile(n)
        inferred = gap_profile(n)
        assert actual == inferred, (n, actual-inferred, inferred-actual)
        for fixed, count in centers.items():
            assert count == exact_centralizer(n, fixed), (n, fixed)
        total = sum(actual.values())
        if n >= 3:
            assert total == 4 * previous1 - 2 * previous2
        assert total == [1,4,14,48,164,560,1912,6528,22288][n-1]
        previous2,previous1 = previous1,total
        print('TRIVARIATE_AND_CENTRALIZERS_OK', n, total, 'monomials', len(actual))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
