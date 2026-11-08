#!/usr/bin/env python3
"""Exact rational checks for the root-imbalance / fringe-size covariance law.

No external dependencies. Running `python verify.py` enumerates all insertions
through eight keys and separately checks finite-sum identities through 200 keys.
These tests supplement an all-size proof; they do not replace it.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations
from math import factorial


def profile(order):
    """Subtree-size count profile from direct recursive BST insertion."""
    if not order:
        return Counter()
    root = order[0]
    left = tuple(x for x in order[1:] if x < root)
    right = tuple(x for x in order[1:] if x > root)
    answer = profile(left) + profile(right)
    answer[len(order)] += 1
    return answer


def mean_profile(m, k):
    if m < k:
        return Q(0)
    if m == k:
        return Q(1)
    return Q(2 * (m + 1), (k + 1) * (k + 2))


def expected_conditional(n, k, i):
    return mean_profile(i, k) + mean_profile(n - 1 - i, k)


def claimed_q_cov(n, k):
    return Q(4 * k * (3 * k + 1 - 2 * n), 3 * n)


def brute(n):
    total = factorial(n)
    sx = [0] * (n + 1)
    sqx = [0] * (n + 1)
    sq = 0
    cond = [[0] * (n + 1) for _ in range(n)]
    counts = [0] * n
    for order in permutations(range(1, n + 1)):
        i = order[0] - 1
        q = (2 * i - n + 1)**2
        x = profile(order)
        counts[i] += 1
        sq += q
        for k, v in x.items():
            sx[k] += v
            sqx[k] += q * v
            cond[i][k] += v
    for i in range(n):
        assert counts[i] == total // n, (n, i, counts[i])
    for k in range(1, n):
        for i in range(n):
            assert Q(cond[i][k], counts[i]) == expected_conditional(n, k, i), (n, k, i)
        calculated = Q(sqx[k], total) - Q(sq * sx[k], total**2)
        assert calculated == claimed_q_cov(n, k), (n, k, calculated, claimed_q_cov(n, k))
        assert Q(sx[k], total) == mean_profile(n, k)
    assert sx[n] == total
    print('PERMUTATION_EXHAUSTION_PASS', n, total, 'permutations', n-1, 'size strata')


def finite_sum_checks():
    for n in range(2, 201):
        qmean = Q(n*n - 1, 3)
        assert Q(sum((2*i-n+1)**2 for i in range(n)), n) == qmean
        spectrum = []
        for k in range(1, n):
            y = [expected_conditional(n, k, i) for i in range(n)]
            assert sum(y, Q(0)) / n == mean_profile(n, k)
            cov = sum(Q((2*i-n+1)**2)*y[i] for i in range(n)) / n - qmean*mean_profile(n,k)
            assert cov == claimed_q_cov(n, k), (n,k,cov)
            spectrum.append(cov)
            expected_sign = 3*k+1-2*n
            assert (cov > 0) - (cov < 0) == (expected_sign > 0) - (expected_sign < 0)
        assert sum(spectrum) == 0, n
        assert sum(k*spectrum[k-1] for k in range(1,n)) == Q((n-2)*(n-1)*(n+1),9)
    print('FINITE_SUM_AND_PROFILE_PASS n=2..200')


if __name__ == '__main__':
    for size in range(2,9):
        brute(size)
    finite_sum_checks()
    print('VERIFY_OK')
