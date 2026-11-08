#!/usr/bin/env python3
"""Standalone finite verification for alternating-host fixed-composition descendants.

Run with Python 3.9+: python3 verify.py
No third-party dependencies.
"""
from collections import defaultdict
from math import comb


def cbin(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def composition(n, positive_parts):
    """Count compositions of nonnegative n into positive_parts positive blocks."""
    if positive_parts == 0:
        return int(n == 0)
    return cbin(n - 1, positive_parts - 1) if n >= positive_parts else 0


def run_count(m, k, r, start):
    """Independent count of length-m, weight-k, r-run words with first bit start."""
    if r < 1 or r > m or k < 0 or k > m:
        return 0
    zeros = (r + (1 - start)) // 2
    ones = r - zeros
    return composition(m - k, zeros) * composition(k, ones)


def exact_penalty_by_runs(m):
    p = defaultdict(int)
    for k in range(m + 1):
        for start in (0, 1):
            for r in range(1, m + 1):
                p[(k, m - r + start)] += run_count(m, k, r, start)
    return {key: val for key, val in p.items() if val}


def exact_penalty_by_transfer(m):
    """Transfer rows for last bit, ones used, greedy waiting excess."""
    d = {(0, 0, 0): 1, (1, 1, 1): 1}
    for _ in range(1, m):
        new = defaultdict(int)
        for (last, k, c), val in d.items():
            for bit in (0, 1):
                new[(bit, k + bit, c + (bit == last))] += val
        d = new
    ans = defaultdict(int)
    for (_, k, c), val in d.items():
        ans[(k, c)] += val
    return dict(ans)


def direct_descendants(n):
    """Independent direct set construction, without greedy matching formula."""
    sets = [set() for _ in range(n + 1)]
    sets[0].add(())
    for i in range(n):
        bit = i % 2
        for m in range(i + 1, 0, -1):
            sets[m].update(v + (bit,) for v in sets[m - 1])
    return sets


def support_lower(m, k):
    return max(0, m - 2 * k - 1, 2 * k - m)


def parity_difference(m, t, k):
    r = m - t
    if r <= 0 or r % 2 == 0:
        return 0
    if r == 1:
        return (1 if k == 0 else -1 if k == m else 0)
    a = (r - 1) // 2
    return ((m - 2 * k) * cbin(m - k - 1, a - 1)
            * cbin(k - 1, a - 1) // a)


def check():
    set_checks = 0
    exact_checks = 0
    summary_checks = 0
    skew_checks = 0
    # Directly enumerate every distinct deletion word for lengths up to 17.
    for n in range(1, 18):
        by_length = direct_descendants(n)
        for m in range(1, n + 1):
            t = n - m
            poly = exact_penalty_by_transfer(m)
            for k in range(m + 1):
                direct = sum(sum(v) == k for v in by_length[m])
                predicted = sum(val for (weight, c), val in poly.items()
                                if weight == k and c <= t)
                assert direct == predicted, ('sets', n, m, k, direct, predicted)
                set_checks += 1
    for m in range(1, 65):
        via_transfer = exact_penalty_by_transfer(m)
        via_runs = exact_penalty_by_runs(m)
        assert via_transfer == via_runs, ('run decomposition', m)
        exact_checks += sum(via_transfer.values()) == (1 << m)
        cumulative = defaultdict(int)
        for t in range(m + 4):
            for (k, c), v in via_transfer.items():
                if c == t:
                    cumulative[k] += v
            total = sum(cumulative.values())
            assert total == sum(cbin(m, j) for j in range(min(t, m) + 1)), (m, t, total)
            summary_checks += 1
            for k in range(m + 1):
                val = cumulative[k]
                assert (val > 0) == (t >= support_lower(m, k)), ('support', m, t, k)
                assert (val == cbin(m, k)) == (t >= (m if k == m else m - 1)) if m > 1 else True
                difference = val - cumulative[m - k]
                assert difference == parity_difference(m, t, k), ('skew', m, t, k, difference)
                skew_checks += 1
    return dict(direct_set_weight_comparisons=set_checks,
                independent_transfer_run_checks=64,
                mass_checks=summary_checks, parity_and_support_checks=skew_checks)


if __name__ == '__main__':
    result = check()
    print('ALL CHECKS PASSED', result)
