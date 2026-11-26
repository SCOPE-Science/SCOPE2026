#!/usr/bin/env python3
"""Independent finite checks for reflexive meet-compatible relations on flat semilattices.

Usage: python3 star_semilattice_checker.py
Standard library only.
"""
from itertools import combinations
from math import comb


def meet(a, b):
    return a if a == b else 0  # 0 is bottom; only nonzero unequal meet is zero


def predicted(n):
    # First choose L (atoms relating to 0), then choose U and allowed atom pairs.
    # Avoid negative exponent at a=0 (zero-th power is 1 by definition).
    return sum(comb(n, a) * ((1 + 2 ** (a - 1)) ** a if a else 1)
               * (1 + 2 ** a) ** (n - a) for a in range(n + 1))


def predicted_direct(n):
    ans = 0
    for lm in range(1 << n):
        for um in range(1 << n):
            ans += 2 ** (lm.bit_count() * um.bit_count() - (lm & um).bit_count())
    return ans


def brute(n):
    S = range(n + 1)
    all_pairs = [(i, j) for i in S for j in S if i != j]
    diagonal = {(i, i) for i in S}
    num = sym = cong = 0
    for bits in range(1 << len(all_pairs)):
        R = diagonal | {all_pairs[k] for k in range(len(all_pairs)) if bits >> k & 1}
        if not all((meet(a, c), meet(b, d)) in R for a, b in R for c, d in R):
            continue
        num += 1
        symmetry = all((b, a) in R for a, b in R)
        if symmetry:
            sym += 1
            if all(((a, c) in R) for a, b in R for bb, c in R if b == bb):
                cong += 1
    return num, sym, cong


def predicted_symmetric(n):
    return sum(comb(n, k) * 2 ** (k * (k - 1) // 2) for k in range(n + 1))


def main():
    for n in range(1, 4):
        result = brute(n)
        expected = (predicted(n), predicted_symmetric(n), 2 ** n)
        assert result == expected, (n, result, expected)
        print('exhaustive n=%d: diagonal=%d symmetric=%d congruences=%d' % (n, *result))
    for n in range(1, 12):
        assert predicted(n) == predicted_direct(n)
    print('formula crosscheck n=1..11: PASS')
    for n in (4, 5, 6, 10, 20, 40):
        D = predicted(n)
        ratio = D / 2 ** (n * (n - 1))
        print('n=%d diagonal=%d dominant-ratio=%.12g' % (n, D, ratio))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
