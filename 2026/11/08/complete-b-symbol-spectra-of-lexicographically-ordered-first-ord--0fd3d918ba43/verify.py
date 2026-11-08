#!/usr/bin/env python3
"""Independent finite checks of cyclic sliding-window weights in affine binary words.

Run with Python 3: python verify.py
"""
from collections import Counter, defaultdict
from random import Random


def predicted(m, b, k):
    n = 1 << m
    if k == 0:
        return 0  # all-zero word; all-one word is tested separately
    if k == 1:
        return n - max(0, n // 2 - b + 1)
    j = (k - 1).bit_length()
    s = n >> (j + 1)
    short = 2 * (k - (1 << (j - 1)))
    long = (1 << j) - k
    assert short >= 0 and long >= 0 and short + long == k
    assert s * (short + 2 * long) == n // 2
    return n - short * max(0, s - b + 1) - long * max(0, 2 * s - b + 1)


def observed_profile(a, c, m):
    n = 1 << m
    w = [((a & x).bit_count() + c) & 1 for x in range(n)]
    zeros_forward = [0] * (2 * n + 1)
    for i in range(2 * n - 1, -1, -1):
        zeros_forward[i] = 0 if w[i % n] else 1 + zeros_forward[i + 1]
    count = Counter(min(n, zeros_forward[i]) for i in range(n))
    all_zero_windows = n
    profile = []
    for b in range(1, n + 1):
        all_zero_windows -= count[b - 1]
        profile.append(n - all_zero_windows)
    return w, profile


def check(m, a, c):
    n = 1 << m
    w, obs = observed_profile(a, c, m)
    k = sum(w[i] != w[(i + 1) % n] for i in range(n)) // 2
    if a:
        assert 1 <= k <= n // 2
        if k == 1:
            expected_runs = [n // 2]
        else:
            j = (k - 1).bit_length()
            s = n >> (j + 1)
            expected_runs = sorted([s] * (2 * (k - (1 << (j - 1)))) +
                                   [2 * s] * ((1 << j) - k))
        runs = []
        for i in range(n):
            if w[i] == 0 and w[(i - 1) % n] == 1:
                t = 0
                while w[(i + t) % n] == 0:
                    t += 1
                runs.append(t)
        assert sorted(runs) == expected_runs, (m, a, c, k, runs, expected_runs)
        for b in range(1, n + 1):
            assert obs[b - 1] == predicted(m, b, k), (m, a, c, k, b, obs[b - 1])
    else:
        assert obs == ([0] * n if c == 0 else [n] * n)
    return k, obs


def run():
    configs = 0
    individual_checks = 0
    distribution_checks = 0
    for m in range(2, 10):
        n = 1 << m
        multiplicity = Counter()
        weights = [Counter() for _ in range(n)]
        for a in range(n):
            for c in (0, 1):
                k, profile = check(m, a, c)
                if a:
                    multiplicity[k] += 1
                for b, weight in enumerate(profile):
                    weights[b][weight] += 1
                configs += 1
                individual_checks += n
        assert multiplicity == Counter({k: 4 if k < n // 2 else 2
                                        for k in range(1, n // 2 + 1)})
        for b in range(1, n + 1):
            if b == 1:
                expected = Counter({0: 1, n // 2: 2 * n - 2, n: 1})
            else:
                K = 1
                while 2 * K * b <= n:
                    K *= 2
                expected = Counter({0: 1, n: 2 * n + 3 - 4 * K})
                for k in range(1, K):
                    weight = predicted(m, b, k)
                    assert weight < n and weight not in expected
                    expected[weight] = 4
            assert weights[b - 1] == expected, (m, b, weights[b - 1], expected)
            distribution_checks += 1
    rng = Random(1729)
    for m in (10, 11):
        for _ in range(120):
            a = rng.randrange(1, 1 << m)
            c = rng.randrange(2)
            check(m, a, c)
            configs += 1
            individual_checks += 1 << m
    print('VERIFY_OK configs=%d individual_b_weights=%d full_distributions=%d' %
          (configs, individual_checks, distribution_checks))


if __name__ == '__main__':
    run()
