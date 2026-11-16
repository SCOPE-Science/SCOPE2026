#!/usr/bin/env python3
"""Exact two-pixel three-interval Fourier-magnitude census.

Only Python's standard library is required.  The two independent enumerators
and two independent correlation calculations all use integer arithmetic.
"""
from itertools import combinations
from math import comb

MIN_LEN = 2
START = 3 * MIN_LEN + 2 * MIN_LEN
END = 24


def compositions(n):
    # Stars and bars: five positive feature lengths at least two.
    r = n - START
    for cuts in combinations(range(r + 4), 4):
        seq = (-1,) + cuts + (r + 4,)
        yield tuple(seq[j + 1] - seq[j] - 1 + MIN_LEN
                    for j in range(5))


def cut_compositions(n):
    # Independent exhaustive four-breakpoint construction.
    for b0, a1, b1, a2 in combinations(range(1, n), 4):
        tup = (b0, a1 - b0, b1 - a1, a2 - b1, n - a2)
        if min(tup) >= MIN_LEN:
            yield tup


def mask_from_tuple(tup):
    a, u, b, v, c = tup
    mask = (1 << a) - 1
    mask |= ((1 << b) - 1) << (a + u)
    mask |= ((1 << c) - 1) << (a + u + b + v)
    return mask


def direct_corr(mask, n):
    return tuple(sum(((mask >> j) & 1) * ((mask >> (j + h)) & 1)
                     for j in range(n - h)) for h in range(n))


def bit_corr(mask, n):
    return tuple((mask & (mask >> h)).bit_count() for h in range(n))


def generate_polynomial(tup):
    a, u, b, v, c = tup
    return {j for j in range(a)} | {a + u + j for j in range(b)} | {a + u + b + v + j for j in range(c)}


def polynomial_autocorr(index_set, n):
    return tuple(sum(j + h in index_set for j in index_set) for h in range(n))



def multivariate_endpoint_signature(terms):
    """Laurent autocorrelation in two independent formal variables X,Y."""
    out = {}
    for (a, b), c in terms.items():
        for (d, e), f in terms.items():
            key = (a-d, b-e)
            out[key] = out.get(key, 0) + c*f
    return {key: value for key, value in out.items() if value}


def check_parametric_homometry():
    # Q=(1-z)P for three-run words. Formal X=z^w, Y=z^g.
    first = {(0, 0): 1, (3, 2): -1, (3, 3): 1,
             (5, 4): -1, (6, 5): 1, (7, 5): -1}
    second = {(0, 0): 1, (1, 1): -1, (2, 2): 1,
              (6, 4): -1, (6, 5): 1, (7, 5): -1}
    assert multivariate_endpoint_signature(first) == multivariate_endpoint_signature(second)
    for w in range(1, 7):
        for g in range(1, 7):
            left = (3*w+2*g, g, 2*w+g, w+g, w)
            right = (w+g, w+g, 4*w+2*g, g, w)
            assert sum(left) == sum(right) == 7*w+5*g
            assert bit_corr(mask_from_tuple(left), sum(left)) == bit_corr(mask_from_tuple(right), sum(right))
            assert left != right and left != right[::-1]


def main():
    check_parametric_homometry()
    total_tuples = total_classes = 0
    expected = []
    for n in range(START, END + 1):
        by_cuts = set(cut_compositions(n))
        by_stars = set(compositions(n))
        assert by_cuts == by_stars
        assert len(by_cuts) == comb(n - START + 4, 4)
        total_tuples += len(by_cuts)
        classes = {}
        fibers = {}
        for tup in sorted(by_cuts):
            canonical_tup = min(tup, tup[::-1])
            mask = mask_from_tuple(tup)
            sig = bit_corr(mask, n)
            assert sig == direct_corr(mask, n)
            assert sig == polynomial_autocorr(generate_polynomial(tup), n)
            assert sig[n - 1] == 1
            classes[canonical_tup] = sig
            fibers.setdefault(sig, set()).add(canonical_tup)
        fixed = sum(tup == tup[::-1] for tup in by_cuts)
        assert len(classes) == (len(by_cuts) + fixed) // 2
        assert len(fibers) == len(set(classes.values()))
        nontrivial = [f for f in fibers.values() if len(f) > 1]
        total_classes += len(classes)
        if n < END:
            assert not nontrivial, (n, nontrivial)
        else:
            assert len(nontrivial) == 1
            assert len(nontrivial[0]) == 2
            assert sorted(nontrivial[0]) == [
                (2, 2, 12, 4, 4), (2, 4, 6, 2, 10)]
            # Independently check the explicit two witnesses (in non-canonical orientation).
            x = (10, 2, 6, 4, 2)
            y = (4, 4, 12, 2, 2)
            cx, cy = min(x, x[::-1]), min(y, y[::-1])
            assert {cx, cy} == nontrivial[0]
            assert bit_corr(mask_from_tuple(x), n) == bit_corr(mask_from_tuple(y), n)
            assert x != y and x != y[::-1]
            print('EXCEPTION',n,'tuples',x,y,
                  'correlation',bit_corr(mask_from_tuple(x), n))
        expected.append((n, len(by_cuts), len(classes), len(fibers), len(nontrivial)))
    print('N raw_words reflection_classes distinct_signatures ambiguous_fibers')
    for row in expected:
        print(*row)
    print('CHECK_OK','raw_words='+str(total_tuples),
          'reflection_classes='+str(total_classes),
          'first_ambiguity=24','exceptional_unordered_pairs=1')


if __name__ == '__main__':
    main()
