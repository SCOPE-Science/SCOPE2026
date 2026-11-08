#!/usr/bin/env python3
"""Exact finite checks for symmetric-ballot Hare-core probability bounds.

Requires only Python's standard library. Run: python3 verify.py
The infinite-sample concentration and CLT conclusions are mathematical,
not consequences of the finite checks below.
"""
from itertools import combinations, product
from math import comb
from fractions import Fraction


def core(ballots, m, k, W):
    n = len(ballots)
    for t in range(1, k + 1):
        for Tsub in combinations(range(m), t):
            T = sum(1 << j for j in Tsub)
            supporters = sum((a & T).bit_count() > (a & W).bit_count() for a in ballots)
            if k * supporters >= n * t:
                return False
    return True


def verify_exchangeable_lemma():
    cases = 0
    for m in range(2, 9):
        ballots = range(1 << m)
        by_card = [[b for b in ballots if b.bit_count() == j] for j in range(m + 1)]
        for k in range(1, m):
            for Wsub in combinations(range(m), k):
                W = sum(1 << j for j in Wsub)
                for t in range(1, k + 1):
                    bound = Fraction(1, k // t + 1)
                    assert Fraction(t, k) > bound
                    for Tsub in combinations(range(m), t):
                        T = sum(1 << j for j in Tsub)
                        for j in range(m + 1):
                            ns = by_card[j]
                            hits = sum((b & T).bit_count() > (b & W).bit_count() for b in ns)
                            assert Fraction(hits, len(ns)) <= bound, (m, k, t, j, W, T)
                            cases += 1
            assert min(Fraction(t, k) - Fraction(1, k // t + 1)
                       for t in range(1, k + 1)) == Fraction(1, k * (k + 1))
    return cases


def verify_exact_one_hot():
    counts = 0
    for k in range(1, 4):
        m = k + 1
        for n in range(1, 7):
            for ballot_ids in product(range(m), repeat=n):
                ballots = [1 << i for i in ballot_ids]
                counts_by_candidate = [ballot_ids.count(i) for i in range(m)]
                all_core_bruteforce = all(core(ballots, m, k, ((1 << m) - 1) ^ (1 << missed))
                                         for missed in range(m))
                all_core_count_formula = all(k * c < n for c in counts_by_candidate)
                assert all_core_bruteforce == all_core_count_formula, (k, n, ballot_ids)
                counts += 1
    return counts


def verify_bias_tv():
    tests = 0
    for k in range(1, 15):
        m = k + 1
        delta = Fraction(1, k * (k + 1))
        special = Fraction(1, k)
        ordinary = (1 - special) / k
        probs = [special] + [ordinary] * k
        uniform = Fraction(1, m)
        tv = sum(abs(p - uniform) for p in probs) / 2
        assert tv == delta
        assert special - uniform == delta
        if k >= 2:
            assert ordinary < Fraction(1, k)
        tests += 1
    return tests


if __name__ == "__main__":
    a = verify_exchangeable_lemma()
    b = verify_exact_one_hot()
    c = verify_bias_tv()
    print("PASS: exact exchangeable-cardinality comparison cases:", a)
    print("PASS: direct finite one-approval core profiles:", b)
    print("PASS: sharp TV-boundary rational tests:", c)
    print("NOTE: tail asymptotics require the analytical proof.")
