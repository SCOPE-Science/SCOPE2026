#!/usr/bin/env python3
"""Exhaustive finite enumerations for the minimum cyclic label in a uniform self-map.

Run: python3 check.py. No external dependencies.
"""
import itertools
import math
from fractions import Fraction


def rising(a, r):
    z = 1
    for j in range(r):
        z *= a + j
    return z


def count_and_minimum(mapping):
    cyclic = set()
    for start in range(len(mapping)):
        route = []
        loc = {}
        at = start
        while at not in loc:
            loc[at] = len(route)
            route.append(at)
            at = mapping[at]
        cyclic.update(route[loc[at]:])
    return len(cyclic), min(cyclic) + 1


def core_probabilities(n):
    p = {}
    q = Fraction(1)
    for k in range(1, n + 1):
        q *= Fraction(n - k + 1, n)
        p[k] = Fraction(k, n) * q
    return p


def conditional_rising(n, k, r):
    return Fraction(math.factorial(r) * rising(n + 1, r), rising(k + 1, r))


def run():
    checks = 0
    for n in range(1, 7):
        rows = {}
        for mapping in itertools.product(range(n), repeat=n):
            k, first = count_and_minimum(mapping)
            rows.setdefault(k, []).append(first)
        pk = core_probabilities(n)
        assert sum(pk.values()) == 1
        checks += 1
        for k in range(1, n + 1):
            observed = rows[k]
            assert Fraction(len(observed), n ** n) == pk[k]
            checks += 1
            for r in range(1, 6):
                obs = Fraction(sum(rising(first, r) for first in observed), len(observed))
                assert obs == conditional_rising(n, k, r), (n, k, r, obs)
                checks += 1
            for m in range(n + 1):
                lhs = Fraction(sum(first > m for first in observed), len(observed))
                rhs = (Fraction(math.comb(n - m, k), math.comb(n, k))
                       if k <= n - m else Fraction(0))
                assert lhs == rhs, (n, k, m, lhs, rhs)
                checks += 1
    print(f"PASS: {checks} exact finite assertions; exhaustive mappings for n=1..6")
    for n in (100, 1000, 10000, 100000):
        q = 1.0
        mean = second = third_rising = fourth_rising = 0.0
        for k in range(1, n + 1):
            q *= (n - k + 1) / n
            p = k * q / n
            if p < 1e-220 and k > 20 * math.sqrt(n):
                break
            mean += p * conditional_rising(n, k, 1)
            second += p * (conditional_rising(n, k, 2)
                           - conditional_rising(n, k, 1))
            third_rising += p * float(conditional_rising(n, k, 3))
            fourth_rising += p * float(conditional_rising(n, k, 4))
        ratios = (mean / math.sqrt(n), second / (n * math.log(n)),
                  third_rising / n**2, fourth_rising / n**3)
        assert all(math.isfinite(v) and v > 0 for v in ratios)
        print('n=', n, 'ratios=', tuple(round(x, 8) for x in ratios))
    print('Targets in the limit: sqrt(pi/2), 1, 3/2, 2/3.')
    print('The asymptotic assertions require the proofs; finite checks do not prove limits.')


if __name__ == '__main__':
    run()
