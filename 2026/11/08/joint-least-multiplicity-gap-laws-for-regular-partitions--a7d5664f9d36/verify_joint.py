#!/usr/bin/env python3
"""Finite independent coefficient/partition checks for joint least-gap law.
Finite checks only; the limiting theorem requires its separate analytic proof.
"""
from itertools import product
from math import exp, pi, sqrt


def restricted_partition_counts(ell, top):
    dp = [0] * (top + 1)
    dp[0] = 1
    for a in range(1, top + 1):
        if a % ell:
            for n in range(a, top + 1):
                dp[n] += dp[n-a]
    return dp


def admissible_sum(ell, bound):
    return sum(a for a in range(1, bound + 1) if a % ell)


def shift(ell, cutoffs):
    return sum(admissible_sum(ell, max(cutoffs[j:])) for j in range(len(cutoffs)))


def enumerate_partitions(n, ell, last=1):
    if n == 0:
        yield ()
        return
    for a in range(last, n + 1):
        if a % ell:
            for tail in enumerate_partitions(n - a, ell, a):
                yield (a,) + tail


def direct_survivors(n, ell, cutoffs):
    ans = 0
    for part in enumerate_partitions(n, ell):
        mult = {}
        for a in part:
            mult[a] = mult.get(a, 0) + 1
        ok = all(all(mult.get(a, 0) >= r for a in range(1, t+1) if a % ell)
                 for r, t in enumerate(cutoffs, start=1))
        if ok:
            ans += 1
    return ans


def test():
    cases = 0
    for ell in range(2, 8):
        p = restricted_partition_counts(ell, 24)
        for n in range(25):
            for cutoffs in product(range(0, 4), repeat=3):
                s = shift(ell, cutoffs)
                expected = p[n - s] if s <= n else 0
                got = direct_survivors(n, ell, cutoffs)
                if got != expected:
                    raise AssertionError((ell, n, cutoffs, got, expected))
                cases += 1
    print('DIRECT_PARTITION_ENUMERATION_OK', cases, 'ell=2..7 n=0..24 R=3 thresholds=0..3')
    for ell in (2, 3, 5, 7, 11):
        for cutoffs in ((1, 2, 3), (4, 2, 1), (3, 1, 5), (0, 3, 2)):
            s = shift(ell, cutoffs)
            direct = sum(a * max((r for r, t in enumerate(cutoffs, start=1) if a <= t), default=0)
                         for a in range(1, max(cutoffs) + 1) if a % ell)
            assert s == direct
    print('LAYER_CAKE_IDENTITY_OK ell=2,3,5,7,11, nonmonotone thresholds')
    for ell in (2, 3, 5):
        p = restricted_partition_counts(ell, 1500)
        n = 1500
        x = (1.0, 1.3, 1.9)
        cutoffs = tuple(int(v * n ** .25) for v in x)
        s = shift(ell, cutoffs)
        observed = p[n-s] / p[n]
        rho = (ell - 1)/ell
        alpha = pi*rho**1.5/(2*sqrt(6))
        predicted = exp(-alpha*sum(max(x[j:])**2 for j in range(3)))
        print('ASYMPTOTIC_SANITY ell={} n={} cutoffs={} exact={:.8f} limit={:.8f}'
              .format(ell, n, cutoffs, observed, predicted))
    print('FINITE_CHECKS_OK independent_audit=False symbolic_proof_required=True')

if __name__ == '__main__':
    test()
