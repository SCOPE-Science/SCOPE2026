#!/usr/bin/env python3
"""Exact finite checks for clustered arrivals and the busy-period Borel law."""
from fractions import Fraction as F
from collections import defaultdict
from math import exp, log, lgamma
import random


def busy_intervals(events):
    grouped = defaultdict(F)
    for t, work in events:
        if work < 0:
            raise ValueError('negative work')
        grouped[t] += work
    result = []
    start = None
    last = F(0)
    remaining = F(0)
    for t in sorted(grouped):
        if start is not None and last + remaining < t:
            result.append((start, last + remaining))
            start = None
            remaining = F(0)
        else:
            remaining = max(F(0), remaining - (t - last))
        if grouped[t] > 0:
            if start is None:
                start = t
            remaining += grouped[t]
        last = t
    if start is not None:
        result.append((start, last + remaining))
    return result


def finite_checks():
    rng = random.Random(20261102)
    comparisons = 0
    for trial in range(700):
        t = F(0)
        delayed, batched = [], []
        for k in range(16):
            t += F(rng.randint(1, 30), 10)
            x0 = F(rng.randint(2, 25), 10)
            delayed.append((t, x0))
            B = x0
            previous_delay = F(0)
            for _ in range(rng.randrange(5)):
                y = F(rng.randint(1, 16), 10)
                # Each trigger may be later than the primary's own work, but
                # cannot exceed the work released before its arrival.
                candidate = previous_delay + F(rng.randint(0, 8), 10)
                d = min(B, candidate)
                assert d <= B
                delayed.append((t + d, y))
                B += y
                previous_delay = d
            batched.append((t, B))
        assert busy_intervals(delayed) == busy_intervals(batched), (trial, delayed, batched)
        comparisons += 1
    # Exactly-on-the-boundary triggering is allowed even if it produces an instantaneous zero.
    assert busy_intervals([(F(0), F(2)), (F(2), F(3))]) == [(F(0), F(5))]
    comparisons += 1
    assert busy_intervals([(F(0), F(2)), (F(3), F(3))]) != busy_intervals([(F(0), F(5))])
    comparisons += 1
    # A secondary can arrive after the primary work finishes, provided previous triggers bridge the gap.
    assert busy_intervals([(F(0), F(2)), (F(2), F(3)), (F(4), F(1))]) == [(F(0),F(6))]
    comparisons += 1
    # Borel probability sums and mean from the classical deterministic-batch queue.
    for rho in (0.12, 0.3, 0.6, 0.8):
        probs = [exp(-rho*k + (k-1)*log(rho*k) - lgamma(k+1)) for k in range(1,3000)]
        assert abs(sum(probs) - 1) < 1e-11
        assert abs(sum((k+1)*p for k,p in enumerate(probs)) - 1/(1-rho)) < 1e-10
        comparisons += 2
    print(f'{comparisons} checks passed: exact rational busy/idle coupling, sharpness, Borel normalization/mean')

if __name__ == '__main__':
    finite_checks()
