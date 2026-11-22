#!/usr/bin/env python3
"""Exact combinatorial checks for least-deficient-part multiplicity marks."""
from fractions import Fraction
from math import pi


def counts_regular(ell, limit):
    p = [1] + [0] * limit
    for part in range(1, limit + 1):
        if part % ell:
            for n in range(part, limit + 1):
                p[n] += p[n - part]
    return p


def marked_counts(p, ell, s, n):
    out = [0] * s
    prefix = 0
    for m in range(1, n + 2):
        if m % ell == 0:
            continue
        t = n - s * prefix
        if t < 0:
            break
        for a in range(s):
            left = p[t - a * m] if t - a * m >= 0 else 0
            right = p[t - (a + 1) * m] if t - (a + 1) * m >= 0 else 0
            out[a] += left - right
        prefix += m
    return out


def enumerate_partitions(n, ell):
    def walk(rest, maxpart, out):
        if rest == 0:
            yield tuple(out)
            return
        for part in range(min(maxpart, rest), 0, -1):
            if part % ell:
                out.append(part)
                yield from walk(rest - part, part, out)
                out.pop()
    yield from walk(n, n, [])


def direct_mark(partition, ell, s):
    mult = {}
    for part in partition:
        mult[part] = mult.get(part, 0) + 1
    for m in range(1, sum(partition) + 2):
        if m % ell and mult.get(m, 0) < s:
            return mult.get(m, 0)
    raise AssertionError('mark not found')


def theoretical_C(ell, s):
    rho = (ell - 1) / ell
    return pi / (24 ** .25 * s ** 1.5 * rho ** .25)


def main():
    exact = 0
    for ell in range(2, 7):
        p = counts_regular(ell, 19)
        for s in range(2, 5):
            for n in range(20):
                direct = [0] * s
                for part in enumerate_partitions(n, ell):
                    direct[direct_mark(part, ell, s)] += 1
                formula = marked_counts(p, ell, s, n)
                assert formula == direct, (ell, s, n, formula, direct)
                assert sum(formula) == p[n], (ell, s, n)
                exact += 1
    asym = 0
    for ell in (2, 3, 5):
        p = counts_regular(ell, 3000)
        for s in (2, 3, 4):
            for n in (800, 1500, 3000):
                cnt = marked_counts(p, ell, s, n)
                c = theoretical_C(ell, s)
                scaled_diff = float(Fraction(cnt[0] - cnt[-1], p[n])) * n ** .25
                target = (s - 1) * c
                # An independent finite-n diagnostic, not an infinite proof.
                assert abs(scaled_diff - target) < .15, (ell, s, n, scaled_diff, target)
                asym += 1
    print('REGULAR_GAP_MARK_EXACT_OK', exact, asym)

if __name__ == '__main__':
    main()
