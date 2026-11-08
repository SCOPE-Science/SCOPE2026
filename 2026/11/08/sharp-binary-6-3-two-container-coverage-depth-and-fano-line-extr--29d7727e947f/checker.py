#!/usr/bin/env python3
"""Exact finite certificate for a binary [6,3] balanced two-container recovery theorem.

Requires Python 3.10+ standard library; run: python checker.py
Enumerates multisets, including zero and repeated columns, not just simple codes.
"""
from itertools import combinations_with_replacement
from collections import Counter
from fractions import Fraction
from functools import lru_cache

V = tuple(range(8))  # 3-bit representations of F_2^3
HYPERPLANES = tuple(frozenset(v for v in V if ((v & h).bit_count() % 2) == 0)
                    for h in range(1, 8))
LINES = tuple(frozenset((0, v)) for v in range(1, 8))


def rank(columns):
    basis = [0, 0, 0]
    for v in columns:
        while v:
            pivot = v.bit_length() - 1
            if basis[pivot] == 0:
                basis[pivot] = v
                break
            v ^= basis[pivot]
    return sum(v != 0 for v in basis)


def counts(triple):
    return (tuple(sum(v in h for v in triple) for h in HYPERPLANES),
            tuple(sum(v in h for v in triple) for h in LINES),
            triple.count(0))


def expectation(A, B, C=None):
    ah, al, a0 = C[A] if C is not None else counts(A)
    bh, bl, b0 = C[B] if C is not None else counts(B)
    if rank(A + B) < 3:
        raise ValueError('cannot recover full rank')
    # Mobius coefficients on the subspace lattice: -1, +2, -8.
    geometric = lambda c: Fraction(9, 9 - c)
    return (sum((geometric(x*y) for x,y in zip(ah,bh)), Fraction(0))
            - 2*sum((geometric(x*y) for x,y in zip(al,bl)), Fraction(0))
            + 8*geometric(a0*b0))


def optimal_geometry(A, B):
    # Ordered containers: one triple is exactly the three nonzero points
    # of a 2-plane; the other consists of 3 distinct points outside it.
    for X, Y in ((A,B),(B,A)):
        if len(set(X)) != 3 or 0 in X or len(set(Y)) != 3:
            continue
        for h in HYPERPLANES:
            if set(X) == h - {0} and all(y not in h for y in Y):
                return True
    return False


def dp_expectation(A, B):
    # Independent exact first-step recursion on the 64 observed-position
    # states; does not use subspace Mobius inversion or geometric sums.
    @lru_cache(None)
    def f(sa, sb):
        observed = tuple(A[i] for i in range(3) if sa & (1 << i)) + tuple(
                    B[j] for j in range(3) if sb & (1 << j))
        if rank(observed) == 3:
            return Fraction(0)
        num = Fraction(1)
        self_loops = 0
        for i in range(3):
            for j in range(3):
                na, nb = sa | (1 << i), sb | (1 << j)
                if na == sa and nb == sb:
                    self_loops += 1
                else:
                    num += f(na, nb) / 9
        return num / (1 - Fraction(self_loops, 9))
    return f(0,0)


def main():
    T = tuple(combinations_with_replacement(V, 3))
    assert len(T) == 120
    C = {A:counts(A) for A in T}
    frequencies = Counter()
    minimizers=[]
    full_rank=0
    for i,A in enumerate(T):
        for B in T[i:]:
            if rank(A+B) < 3:
                continue
            full_rank += 1
            z = expectation(A,B,C)
            frequencies[z] += 1
            if z == Fraction(125,56):
                minimizers.append((A,B))
            assert (z >= Fraction(125,56)), ('claimed bound failed', A,B,z)
            if z == Fraction(125,56):
                assert optimal_geometry(A,B), ('unexpected equality',A,B)
            else:
                assert not optimal_geometry(A,B), ('geometry with nonoptimal value',A,B)
    assert full_rank == 5922
    assert len(frequencies) == 55
    assert len(minimizers) == 28
    assert sorted(frequencies.items())[:2] == [(Fraction(125,56),28), (Fraction(127,56),42)]
    assert len({(min(A,B),max(A,B)) for A,B in minimizers}) == 28
    # A second algebraically independent exact computation.
    verified_pairs = 0
    for i,A in enumerate(T):
        for B in T[i:]:
            if rank(A+B) == 3:
                assert expectation(A,B,C) == dp_expectation(A,B), (A,B)
                verified_pairs += 1
    assert verified_pairs == full_rank
    assert dp_expectation((1,2,3),(4,5,6)) == Fraction(125,56)
    # Independent symbolic law for a minimizing layout, from its rank pattern:
    # P(tau>t)=3*(2/9)^t+3*(1/9)^t for integers t>=1.
    for t in range(1,9):
        A,B=(1,2,3),(4,5,6)
        # Count the 9^t histories through dynamic programming on seen positions.
        states={(0,0):1}
        for _ in range(t):
            nxt=Counter()
            for (sa,sb),count in states.items():
                for i in range(3):
                    for j in range(3):
                        nxt[sa | (1<<i),sb | (1<<j)] += count
            states=nxt
        failed=sum(count for (sa,sb),count in states.items() if rank(
                   tuple(A[i] for i in range(3) if sa & (1 << i)) +
                   tuple(B[j] for j in range(3) if sb & (1 << j)))<3)
        assert Fraction(failed,9**t) == 3*Fraction(2,9)**t + 3*Fraction(1,9)**t
    print('PASS: 120 triples; 5922 full-rank unordered pairs; 55 exact values;')
    print('minimum E[tau] = 125/56, attained by precisely 28 unordered pairs;')
    print('second value = 127/56 (42 pairs); geometry iff equality;')
    print('independent rational first-step recursion for all 5922 pairs and exact tail tests passed.')

if __name__ == '__main__':
    main()
