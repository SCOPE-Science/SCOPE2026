#!/usr/bin/env python3
"""Exact three-color excitation activity laws on parallel-path graphs.

All computations use integer coefficients and exact rational rate keys.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import pi, sqrt, prod


def trinomial(n):
    counts = {0: 1}
    for _ in range(n):
        nxt = defaultdict(int)
        for s, weight in counts.items():
            for step in (-1, 0, 1):
                nxt[s + step] += weight
        counts = dict(nxt)
    return counts


def rate_counts(lengths):
    r = len(lengths)
    assert r >= 3 and all(n >= 2 for n in lengths)
    polys = [trinomial(n) for n in lengths]
    out = Counter()
    # A complete r-path vector has a single common end-color iff
    # all its path sums are congruent mod 3.  Three root colors remain.
    for residue in range(3):
        choices = [[(s, w) for s, w in p.items() if s % 3 == residue]
                   for p in polys]
        for selected in product(*choices):
            vals = [v for v, _ in selected]
            weight = 3
            for _, w in selected:
                weight *= w
            activity = max(Fraction(abs(vals[i] - vals[j]), lengths[i] + lengths[j])
                           for i in range(r) for j in range(i + 1, r))
            out[activity] += weight
    assert sum(out.values()) == 3 ** (2 + sum(n - 1 for n in lengths))
    return dict(sorted(out.items()))


def equal_arm_fast(r, n):
    """O(n^2) coefficient formula for the full CCA activity census."""
    a = trinomial(n)
    result = [0] * (2 * n // 3 + 1)
    for c in range(3):
        w = {m: a.get(3*m+c, 0) for m in range(-n, n+1)}
        def total(lo, hi):
            return sum(w.get(i, 0) for i in range(lo, hi+1)) if lo <= hi else 0
        for k in range(2*n//3 + 1):
            for m in range(-n, n+1):
                result[k] += 3 * (total(m, m+k)**r
                                  - total(m+1, m+k)**r
                                  - total(m, m+k-1)**r
                                  + total(m+1, m+k-1)**r)
    assert sum(result) == 3 ** (2 + r*(n-1))
    return result


def zero_count(lengths):
    a = [trinomial(n) for n in lengths]
    return 3 * sum(prod(p.get(s, 0) for p in a)
                   for s in range(-max(lengths), max(lengths)+1))

# The two edge forms differ by an exact integer coboundary.
def check_forms():
    h = [0, -2, -1]
    for a in range(3):
        for b in range(3):
            cca = ((b-a+1) % 3)-1
            ghm = (a==0 and b==1) - (a==1 and b==0)
            assert cca == 3*ghm + h[b]-h[a]
    return True

if __name__ == '__main__':
    assert check_forms()
    examples = [(2,2,2), (2,2,2,2), (2,2,2,2,2), (3,3,3),
                (3,3,3,3), (4,4,4), (2,3,4), (2,2,3,3), (2,3,3,4)]
    for lengths in examples:
        counts = rate_counts(lengths)
        assert counts[Fraction(0)] == zero_count(lengths)
        if len(set(lengths)) == 1:
            r, n = len(lengths), lengths[0]
            assert list(counts.values()) == equal_arm_fast(r, n)
        print('COEFFICIENT_OK', str(lengths),
              'colorings', sum(counts.values()),
              'activity_count', {str(a): c for a,c in counts.items()})
    for r in (3,4,5):
        asym = (27/(4*pi))**((r-1)/2)/sqrt(r)
        values = []
        for n in (10,20,40,80):
            z = 3*sum(v**r for v in trinomial(n).values())
            p = z / 3**(2+r*(n-1))
            values.append((n, round(n**((r-1)/2)*p, 8)))
        print('LOCAL_LIMIT_CHECK', r, 'constant', round(asym, 8), values)
    print('ALL_COEFFICIENT_CHECKS_OK')
