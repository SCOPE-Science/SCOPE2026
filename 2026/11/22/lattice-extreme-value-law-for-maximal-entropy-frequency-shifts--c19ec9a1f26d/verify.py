#!/usr/bin/env python3
"""Exact finite checks for a geometric-block frequency-shift theorem.

The infinite assertions use the proof in RESULT.md, not this finite program.
"""
from fractions import Fraction
from itertools import product


def q(m):
    return Fraction(1, 2**m)


def check_blocks():
    for k in range(1, 9):
        for m in range(1, 14):
            word = [0]*m + [1]*(k*m)
            d = 0
            seen = [d]
            for b in word:
                d += (k+1)*b-k
                seen.append(d)
            assert d == 0
            assert min(seen) == -k*m
            assert max(seen) == 0
            assert len(word) == (k+1)*m


def check_geometric_max():
    # Finite enumeration exactly sums the unnormalised probabilities of
    # the event M_1,...,M_J <= r under the infinite geometric source.
    for j in range(1, 5):
        for r in range(1, 7):
            lhs = sum((__import__('math').prod(q(m) for m in ms)
                      for ms in product(range(1,r+1), repeat=j)), Fraction())
            rhs = (1-Fraction(1,2**r))**j
            assert lhs == rhs, (j,r,lhs,rhs)


def check_size_bias():
    # Exact power-series identities, not a truncated probability census.
    # Sum_{m>=1} m z^m = z/(1-z)^2 and
    # Sum_{m>=1} m^2 z^m = z(1+z)/(1-z)^3.
    z = Fraction(1,2)
    em = z/(1-z)**2
    em2 = z*(1+z)/(1-z)**3
    assert em == 2 and em2 == 6
    assert em2/em == 3  # expected m in the size-biased origin block
    for k in range(1,9):
        e_length = (k+1)*em
        e_ones = k*em
        assert e_ones/e_length == Fraction(k,k+1)
        assert e_length == 2*(k+1)


def check_compositions():
    # Different compositions of t index all ordered concatenations of
    # complete generators of total length (k+1)t.
    for k in range(1,5):
        for t in range(1,10):
            generated=set()
            for mask in range(2**(t-1)):
                sizes=[]; cur=1
                for i in range(t-1):
                    if mask>>i & 1:
                        sizes.append(cur);cur=1
                    else:
                        cur+=1
                sizes.append(cur)
                word=''.join('0'*m+'1'*(k*m) for m in sizes)
                assert len(word)==(k+1)*t
                generated.add(word)
            assert len(generated)==2**(t-1)


def main():
    check_blocks()
    check_geometric_max()
    check_size_bias()
    check_compositions()
    print('PASS: exact block excursions, return-index maxima, size bias, and compositions')


if __name__=='__main__':
    main()
