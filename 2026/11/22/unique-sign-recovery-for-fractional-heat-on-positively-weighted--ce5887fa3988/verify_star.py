"""Numerical checks for the stated weighted-star spectral sign classification.

Requires numpy and scipy. The mathematical argument in RESULT.md, not these
finite tests, establishes the theorem. No network access is used.
"""
from itertools import combinations
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq


def laplacian(weights):
    weights = np.asarray(weights, dtype=float)
    assert len(weights) >= 2 and np.all(weights > 0)
    L = np.diag(np.r_[weights.sum(), weights])
    L[0, 1:] = -weights
    L[1:, 0] = -weights
    return L


def kernel_data(weights, alpha):
    L = laplacian(weights)
    vals, vecs = eigh(L)
    vals[0] = 0.0
    rates = vals ** alpha
    P = np.einsum('ik,jk->ijk', vecs, vecs)
    def kernel(t):
        return np.einsum('ijk,k->ij', P, np.exp(-t * rates))
    return L, rates, kernel


def root_for_pair(kernel, rates, i, j):
    highest = float(max(rates))
    positive = [r for r in rates if r > 1e-13 * highest]
    smallest = min(positive)
    low = 1e-3 / highest
    while kernel(low)[i, j] >= 0 and low > 1e-15 / highest:
        low /= 5
    assert kernel(low)[i, j] < 0, (low, i, j)
    high = 40 / smallest
    assert kernel(high)[i, j] > 0
    return brentq(lambda t: kernel(t)[i, j], low, high,
                  xtol=1e-14 / highest, rtol=1e-12)


def check(weights, alpha):
    L, rates, K = kernel_data(weights, alpha)
    m = len(weights)
    # Exact combinatorial moments of the ordinary Laplacian.
    for i, j in combinations(range(1, m + 1), 2):
        assert L[i, j] == 0.0
        assert np.isclose((L @ L)[i, j], weights[i-1] * weights[j-1], rtol=1e-12)
    assert np.allclose(K(0), np.eye(m+1), atol=1e-12)
    assert np.allclose(K(0.27 / max(rates))[0, 1:],
                       K(0.27 / max(rates))[1:, 0], atol=1e-12)
    if alpha > 1:
        zeros = {}
        for i, j in combinations(range(1, m+1), 2):
            rt = root_for_pair(K, rates, i, j)
            zeros[i, j] = rt
            for t in [rt * 0.05, rt * 0.3, rt * 0.8]:
                assert K(t)[i, j] < -1e-12, (weights, alpha, t, i, j)
            for t in [rt * 1.2, rt * 2, rt * 10]:
                assert K(t)[i, j] > 0, (weights, alpha, t, i, j)
        t_last = max(zeros.values())
        assert np.min(K(t_last * 1.5)) > -1e-12
        assert np.max(np.abs(K(t_last * 1.5).sum(axis=1) - 1)) < 1e-11
        assert np.max(np.abs(K(t_last * 0.25)).sum()) > 0
        assert np.max(np.sum(np.abs(K(t_last * 0.25)), axis=1)) > 1 + 1e-12
    else:
        for t in [0.0001, .01, 0.1, 1, 10]:
            tt = t/max(rates)
            assert np.min(K(tt)) > -1e-12
            assert np.max(np.abs(K(tt).sum(axis=1)-1)) < 1e-11
    for t in [0.0001 / max(rates), .01/max(rates), 1/max(rates), 100/max(rates)]:
        assert np.all(np.diag(K(t)) > 0)
        assert np.all(K(t)[0, 1:] > 0)
    return len(list(combinations(range(1,m+1),2)))


def main():
    checks = 0
    cases = [
        [1, 1], [1,2], [1,1,1], [1,3,9], [0.5,2,5], [1,1,1,1],
        [1,1,3,3], [1,2,2,5], [1,2,4,8], [1,3,3,3,9],
        [0.4,0.7,1.5,3,5], [1]*7,
    ]
    rng = np.random.default_rng(20261117)
    for m in (3, 4, 6):
        for _ in range(8):
            cases.append(list(np.exp(rng.uniform(-2, 2, size=m))))
    for weights in cases:
        for alpha in [0.5, 1.0, 1.25, 1.8, 2.0, 3.7]:
            checks += check(weights, alpha)
    print('PASS: %d configurations/orders; %d pair-level trials.' % (len(cases)*6, checks))


if __name__ == '__main__':
    main()
