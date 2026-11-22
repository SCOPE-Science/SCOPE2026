#!/usr/bin/env python3
"""Independent exact-rational Bayes-risk integrator for parallel noisy threshold designs.
Only verifies finite parameter cases; the asymptotic theorem is established analytically.
"""
from fractions import Fraction as Q
from itertools import product


def information(thresholds, e):
    """Var(E[X|Y]) for X uniform [0,1], bit contrast e=1-2p."""
    t = sorted(thresholds)
    assert all(Q(0) <= x <= Q(1) for x in t)
    assert Q(0) <= e < Q(1)
    v = [Q(0), *t, Q(1)]
    cellmass = [v[j+1]-v[j] for j in range(len(v)-1)]
    cellcentered = [(v[j+1]**2-v[j]**2 - v[j+1]+v[j])/2 for j in range(len(v)-1)]
    out = Q(0)
    n = len(t)
    for y in product([-1, 1], repeat=n):
        prob = Q(0)
        moment = Q(0)
        for j in range(n+1):
            like = Q(1)
            for i in range(n):
                sgn = 1 if j > i else -1
                like *= (1 + e*y[i]*sgn)/2
            prob += cellmass[j]*like
            moment += cellcentered[j]*like
        assert prob > 0
        out += moment*moment/prob
    return out


def check():
    cases = 0
    for n in range(1, 6):
        for e in (Q(1, 8), Q(1, 16), Q(1, 32)):
            repeated = [Q(1, 2)]*n
            base = information(repeated, e)
            # General Bayes bounds and label permutation invariance.
            assert 0 <= base <= Q(1, 12)
            offsets = [Q(2*i-n-1, 4) for i in range(1, n+1)]
            t = [Q(1, 2)+e**2*v for v in offsets]
            value = information(t,e)
            assert value >= base
            assert value == information(list(reversed(t)),e)
            if n >= 2:
                gain = (value-base)/e**6
                expected = Q(n*(n*n-1), 96)
                # For the tested contrasts the exact ratio lies below
                # its rigorous asymptotic leading coefficient.
                assert 0 < gain < expected
                if e == Q(1,32):
                    assert abs(gain/expected-1) < Q(1, 8)
                cases += 1
            else:
                assert value == base
            # Perturb each predicted location (in scaled coordinates)
            # and check local improvement at weak contrast.
            if e == Q(1,32) and n >= 2:
                for i in range(n):
                    for shift in [-Q(1, 4), Q(1, 4)]:
                        probe = list(t)
                        probe[i] += e**2*shift
                        assert value > information(probe, e)
                        cases += 1
    print('PASS: exact-rational posterior integrals; weak-signal clustered designs; local offsets')
    print('Checked', cases, 'nontrivial rational inequalities across one to five queries.')
    print('Limits: finite checks only; no claim of exhaustive finite-e global optimization.')


if __name__ == '__main__':
    check()
