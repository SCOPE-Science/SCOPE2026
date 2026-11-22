#!/usr/bin/env python3
"""Direct PID-deletion enumeration of layered permutations, with no bond formula in the oracle."""
from collections import Counter
from fractions import Fraction
from math import comb


def composition(mask, n):
    sizes = []
    run = 1
    for i in range(n - 1):
        if mask & (1 << i):
            sizes.append(run)
            run = 1
        else:
            run += 1
    sizes.append(run)
    return sizes


def layered(sizes):
    out = []
    offset = 0
    for size in sizes:
        out.extend(range(offset + size, offset, -1))
        offset += size
    return out


def standardize(seq):
    ranking = {x: j + 1 for j, x in enumerate(sorted(seq))}
    return tuple(ranking[x] for x in seq)


def distinct_descendants(word):
    return {standardize(word[:i] + word[i+1:]) for i in range(len(word))}


def extremal_count(n):
    k, r = divmod(n, 3)
    return k + 1 if r == 0 else 1 if r == 1 else 2*k + 1 + comb(k + 2, 2)


def main():
    for n in range(1, 13):
        hist = Counter()
        for mask in range(1 << (n-1)):
            sizes = composition(mask, n)
            word = layered(sizes)
            d = len(distinct_descendants(word))
            macro = len(sizes) - sum(sizes[i] == sizes[i+1] == 1 for i in range(len(sizes)-1))
            assert d == macro, (word, sizes, d, macro)
            hist[d] += 1
        M = (2*n+1)//3
        assert sorted(hist) == list(range(1, M+1))
        assert hist[M] == extremal_count(n), (n, hist[M])
        assert sum(hist.values()) == 1 << (n-1)
        if n > 2:
            mean = sum(Fraction(k*v, 1<<(n-1)) for k, v in hist.items())
            assert mean == Fraction(3*(n+1),8), (n,mean)
            if n >= 5:
                var = sum(Fraction((k-mean)**2 * v, 1<<(n-1)) for k, v in hist.items())
                assert var == Fraction(7*(n-1),64),(n,var)
        print(f'n={n:2d} layered={1<<(n-1):5d} distribution={dict(sorted(hist.items()))}')
    print('PASS: direct PID descendant oracle, structural rule, support, extremizers, moments')


if __name__ == '__main__':
    main()
