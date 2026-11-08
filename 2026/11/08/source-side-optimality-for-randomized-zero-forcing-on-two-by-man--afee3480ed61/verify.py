#!/usr/bin/env python3
"""Exact, standalone checks for two-vertex-side randomized zero forcing."""
from fractions import Fraction
from math import comb
from pathlib import Path


def reduced_expectations(a):
    """Return (start_in_two_part, start_in_a_part) using rational size-chain recurrence."""
    assert a >= 2
    H = [Fraction(0) for _ in range(a + 1)]  # H[i] = E(time | i blue in large part, 1 blue in small part)
    H[a] = Fraction(1)
    for i in range(a-1, -1, -1):
        k = a - i
        p = Fraction(i, a)
        numerator = Fraction(1)
        self_loop = Fraction(0)
        for u in range(k + 1):
            probability = Fraction(comb(k, u), 2**k)
            # If the second small-part vertex becomes blue, the other part
            # finishes in one more round unless already completely blue.
            numerator += probability * p * (0 if i + u == a else 1)
            if u == 0:
                self_loop = probability * (1-p)
            else:
                numerator += probability * (1-p) * H[i+u]
        H[i] = numerator / (1-self_loop)
    p1 = Fraction(2*(a-1), a*a)
    p2 = Fraction(1, a*a)
    start_in_large = (1 + p1*H[1] + p2) / (p1+p2)
    return H[0], start_in_large


def independent_vertex_subsets(a):
    """Independent rational DP over all labelled blue subsets, not size states."""
    n = a + 2
    allmask = (1 << n) - 1
    dp = {allmask: Fraction(0)}
    for size in range(n-1, 0, -1):
        for mask in range(1, allmask):
            if mask.bit_count() != size:
                continue
            i = (mask & ((1 << a)-1)).bit_count()
            j = (mask >> a).bit_count()
            whites = [v for v in range(n) if not (mask >> v) & 1]
            probs = [Fraction(j, 2) if v < a else Fraction(i, a) for v in whites]
            numerator = Fraction(1)
            self_loop = Fraction(0)
            for choices in range(1 << len(whites)):
                dst = mask
                p = Fraction(1)
                for k, v in enumerate(whites):
                    if (choices >> k) & 1:
                        dst |= 1 << v
                        p *= probs[k]
                    else:
                        p *= 1-probs[k]
                if dst == mask:
                    self_loop += p
                elif p:
                    numerator += p*dp[dst]
            assert self_loop < 1
            dp[mask] = numerator / (1-self_loop)
    return dp[1 << a], dp[1]  # small-part start, large-part start


def verify_certificate_table():
    rows = (Path(__file__).resolve().parent / 'rational_certificates.tsv').read_text(encoding='utf-8').splitlines()
    assert rows[0] == 'a\tT_B_numerator\tT_B_denominator\tT_A_numerator\tT_A_denominator'
    assert len(rows) == 11
    for row in rows[1:]:
        a, bn, bd, an, ad = map(int, row.split('\t'))
        assert reduced_expectations(a) == (Fraction(bn, bd), Fraction(an, ad))
    print('RATIONAL_CERTIFICATES_REPLAY_OK', len(rows)-1)


def check():
    verify_certificate_table()
    for a in range(3, 12):
        small, large = reduced_expectations(a)
        assert small < Fraction(7,2) < large, a
        print('FINITE_EXACT', a, 'small<7/2<large', True, 'difference', float(large-small))
    assert reduced_expectations(2)[0] == reduced_expectations(2)[1] == 3
    print('BOUNDARY_EQUALITY_AT_TWO_OK')
    for a in range(2, 7):
        pair1 = reduced_expectations(a)
        pair2 = independent_vertex_subsets(a)
        assert pair1 == pair2, (a, pair1, pair2)
        print('LABELLED_STATE_MARKOV_AGREEMENT', a)
    # Code checks these finite boundary inequalities only; the paper supplies
    # the dyadic, all-parameter proof for a >= 12.
    assert Fraction(12*12, 2*12-1) > 6
    assert 2**(5-1)+1 > 2*5+4
    for r in range(5, 101):
        assert 2**(r-1)+1 > 2*r+4
    print('DYADIC_BASE_CASE_AND_SAMPLES_OK')
    print('VERIFY_OK')

if __name__ == '__main__':
    check()
