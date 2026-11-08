"""Exact finite-profile checks for a facility-omission spacing identity.

Uses the Python standard library. It is a finite diagnostic, not a proof of
any asymptotic claim.
"""
from fractions import Fraction
from itertools import combinations
from math import isclose
from random import Random


def profile_checks():
    checks = 0
    for n in range(3, 8):
        for seq in combinations(range(1, 13), n):
            x = [Fraction(v, 13) for v in seq]
            gaps = [x[i + 1] - x[i] for i in range(n - 1)]
            delta = [gaps[0]] + [min(gaps[i - 1], gaps[i]) for i in range(1, n - 1)] + [gaps[-1]]
            p = [1 / (d * d) for d in delta]
            expectation = sum(w * d for w, d in zip(p, delta)) / sum(p)
            optimum = min(gaps)
            ratio = expectation / optimum
            inverse = [1 / d for d in delta]
            identity = sum(inverse) / (min(gaps) * sum(v * v for v in inverse))
            assert expectation == sum((w / sum(p)) * d for w, d in zip(p, delta))
            assert ratio == identity
            for power in (1, 2):
                lhs = sum(1 / d**power for d in delta)
                rhs = 2 * sum(1 / g**power for g in gaps)
                rhs -= sum(1 / max(gaps[i], gaps[i+1])**power for i in range(n - 2))
                assert lhs == rhs
            checks += 1
    return checks


def spacing_scale_checks():
    rnd = Random(90177)
    checks = 0
    for n in [10, 40, 100, 400, 2000]:
        for _ in range(25):
            exp_gaps = [rnd.expovariate(1) for _ in range(n - 1)]
            d = [exp_gaps[0]] + [min(exp_gaps[i-1], exp_gaps[i]) for i in range(1, n-1)] + [exp_gaps[-1]]
            a = sum(1/u for u in d)
            b = sum(1/(u*u) for u in d)
            r = a/(min(exp_gaps)*b)
            d2 = [u/7.5 for u in d]
            r2 = sum(1/u for u in d2)/(min(exp_gaps)/7.5*sum(1/(u*u) for u in d2))
            assert isclose(r, r2, rel_tol=5e-13, abs_tol=5e-13)
            assert r >= 1-1e-12
            checks += 1
    return checks


if __name__ == '__main__':
    p = profile_checks()
    s = spacing_scale_checks()
    print('Exact rational profiles checked:', p)
    print('Scale and basic bounds checked:', s)
    print('All finite checks passed.')
