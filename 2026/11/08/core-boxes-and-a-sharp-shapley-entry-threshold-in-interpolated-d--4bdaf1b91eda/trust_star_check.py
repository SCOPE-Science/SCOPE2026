#!/usr/bin/env python3
"""Exact-rational checks for weighted directed in-stars with an interpolated trust game.

No external dependencies. Run: python3 trust_star_check.py
All finite checks supplement, rather than replace, the symbolic proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial


def values(weights, alpha):
    """Coalition-value table; tail indices 0..m-1, hub index m."""
    m = len(weights)
    full = 1 << (m + 1)
    out = [Q(0)] * full
    tailmask = (1 << m) - 1
    for mask in range(full):
        if not mask & (1 << m):
            continue
        chosen = mask & tailmask
        inside = sum((weights[j] for j in range(m) if chosen >> j & 1), Q(0))
        missing = [weights[j] for j in range(m) if not (chosen >> j & 1)]
        outside_min = min(missing) if missing else Q(0)
        out[mask] = alpha * inside + (1 - alpha) * outside_min
    return out


def shapley(v, n):
    total = factorial(n)
    out = [Q(0) for _ in range(n)]
    for i in range(n):
        for mask in range(1 << n):
            if mask >> i & 1:
                continue
            s = mask.bit_count()
            p = Q(factorial(s) * factorial(n-s-1), total)
            out[i] += p * (v[mask | (1 << i)] - v[mask])
    return out


def external_tail_coefficients(weights):
    w = sorted(weights)
    m = len(w)
    b = []
    for j in range(m):
        b.append(sum(((w[t] - w[t-1]) / (t+1) for t in range(j+1, m)), Q(0)) - w[-1]/(m+1))
    return b


def threshold(weights):
    w = sorted(weights)
    b = external_tail_coefficients(w)
    r = b[0] / w[0]
    return (1 + r) / (Q(3,2) + r)


def in_core(v, x):
    n = len(x)
    if sum(x) != v[(1 << n)-1]:
        return False
    for mask in range(1 << n):
        if sum((x[j] for j in range(n) if mask >> j & 1), Q(0)) < v[mask]:
            return False
    return True


def run():
    families = [
        [1], [1,1], [1,2], [2,2], [1,3], [1,5],
        [1,1,1], [1,2,5], [1,3,3], [2,3,4],
        [1,1,2,3], [1,2,3,8], [2,3,3,7],
        [1,1,2,3,5], [1,2,2,4,6], [1,2,3,4,5,6]
    ]
    alpha_grid = [Q(0), Q(1,5), Q(1,3), Q(1,2), Q(3,5), Q(2,3), Q(3,4), Q(9,10), Q(1)]
    cases = vertices = coalitional_inequalities = shapley_cases = 0
    for raw in families:
        weights = sorted(map(Q, raw))
        weights = [w / weights[-1] for w in weights]  # Normalize to permitted trust weights.
        m = len(weights)
        b = external_tail_coefficients(weights)
        assert all(b[i]/weights[i] >= b[i+1]/weights[i+1] for i in range(m-1))
        assert all(bi /wi >= Q(-1,m+1) for bi, wi in zip(b,weights))
        cut = threshold(weights)
        assert Q(1,2) <= cut < 1
        for alpha in sorted(set(alpha_grid + [cut])):
            v = values(weights,alpha)
            sh = shapley(v,m+1)
            formula = [alpha*weights[i]/2 + (1-alpha)*b[i] for i in range(m)]
            assert sh[:m] == formula, (weights,alpha,sh,formula)
            assert sh[m] == alpha*sum(weights) - sum(formula)
            if alpha >= Q(1,2):
                assert in_core(v, [Q(0)]*m + [alpha*sum(weights)])
                length = 2*alpha-1
                for bits in product((0,1), repeat=m):
                    tails = [length*weights[i]*bits[i] for i in range(m)]
                    x = tails+[alpha*sum(weights)-sum(tails)]
                    assert in_core(v,x), (weights,alpha,x)
                    vertices += 1
                    coalitional_inequalities += 2**(m+1)
                assert in_core(v,sh) == (alpha >= cut), (weights,alpha,sh,cut)
            else:
                # Singleton positivity contradicts the upper bound from the
                # coalition omitting that singleton: x_i >= 0 > (2a-1)w_i.
                assert 2*alpha-1 < 0
            cases += 1
            shapley_cases += 1
    assert threshold([Q(1),Q(1)]) == Q(4,7)
    assert threshold([Q(1),Q(2)]) == Q(5,8)
    assert threshold([Q(1),Q(1),Q(1)]) == Q(3,5)
    assert threshold([Q(1)]*4) == Q(8,13)
    print('PASS: exact Shapley formulas and threshold on',shapley_cases,'weighted/rational cases')
    print('PASS: core box vertices',vertices,'and coalition inequalities',coalitional_inequalities)
    print('PASS: threshold examples, Shapley inclusion, and monotone normalized coefficients')


if __name__ == '__main__':
    run()
