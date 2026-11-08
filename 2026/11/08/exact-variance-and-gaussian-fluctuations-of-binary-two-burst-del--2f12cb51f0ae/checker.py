"""Standalone exact check for the binary two-disjoint-double-deletion theorem.

Usage: python3 checker.py
No third-party dependencies. Exhaustive small-word checks do not replace
its all-length symbolic argument.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from random import Random


def direct_ball(word):
    n = len(word)
    return {word[:i] + word[i+2:j] + word[j+2:]
            for i in range(n-1) for j in range(i+2,n-1)}


def canonical_count(word):
    n = len(word)
    m = n-2
    t = [int(word[i] != word[i+2]) for i in range(m)]
    c = [int(word[i] == word[i+2] != word[i+4])
         for i in range(m-2)]
    return (1 + sum(c) + sum(t[:m-2])
            + sum(t[i]*t[j] for i in range(m)
                  for j in range(i+3,m)))


def formula_mean(n):
    return Fraction(n*n-3*n+4,8)


def formula_variance(n):
    return Fraction((n-4)*(2*n*n-15*n+31),32)


def main():
    tested = 0
    for n in range(4,14):
        counts = Counter()
        for w in product((0,1), repeat=n):
            b = len(direct_ball(w))
            assert b == canonical_count(w), (n, w, b, canonical_count(w))
            counts[b] += 1
            tested += 1
        total = 2**n
        mean = Fraction(sum(k*v for k,v in counts.items()),total)
        var = Fraction(sum(k*k*v for k,v in counts.items()),total)-mean*mean
        assert mean == formula_mean(n), (n,mean,formula_mean(n))
        assert var == formula_variance(n), (n,var,formula_variance(n))
        print(f'n={n} words={total} mean={mean} variance={var}')
    rand = Random(373737)
    for n in (14,18,24,30):
        for _ in range(250):
            w = tuple(rand.randrange(2) for _ in range(n))
            assert len(direct_ball(w)) == canonical_count(w)
            tested += 1
    print(f'PASS: {tested} source words; exact direct-channel and moment checks')


if __name__ == '__main__':
    main()
