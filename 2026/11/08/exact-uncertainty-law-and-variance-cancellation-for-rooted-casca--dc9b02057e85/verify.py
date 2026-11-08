#!/usr/bin/env python3
"""Exact-rational finite-tree tests for the one-cascade FJ opinion law.

Run: python3 verify.py
The exhaustive transition enumeration is independent of the tree-law
convolution and moment-message implementations. This checks finite cases,
not the universal proof in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from random import Random


def model(parent, theta, h, gamma, initial, anchors, weights):
    n = len(parent)
    assert parent[0] == -1 and theta[0] == 1
    assert all(0 <= parent[i] < i for i in range(1, n))
    z = list(initial)
    delta = [Q(1)] * n
    a = [Q(0)] * n
    children = [[] for _ in range(n)]
    for i in range(1, n):
        j = parent[i]
        children[j].append(i)
        z[i] = h[i] * ((1 - gamma[i]) * initial[i] + gamma[i] * z[j]) + (1 - h[i]) * anchors[i]
        delta[i] = delta[j] * theta[j]
        a[i] = weights[i] * (z[i] - initial[i])
    return z, delta, a, children


def message_law(theta, a, children):
    n = len(a)
    means = [Q(0)] * n
    variances = [Q(0)] * n
    distributions = [None] * n
    for v in range(n - 1, -1, -1):
        subtotal = sum((means[c] for c in children[v]), Q(0))
        means[v] = a[v] + theta[v] * subtotal
        variances[v] = (theta[v] * sum((variances[c] for c in children[v]), Q(0))
                        + theta[v] * (1 - theta[v]) * subtotal * subtotal)
        # Exact discrete distribution for Z_v conditioned on exposure.
        conditional = {Q(0): Q(1)}
        for c in children[v]:
            next_dist = defaultdict(Q)
            for x, px in conditional.items():
                for y, py in distributions[c].items():
                    next_dist[x + y] += px * py
            conditional = dict(next_dist)
        out = defaultdict(Q)
        out[a[v]] += 1 - theta[v]
        for x, px in conditional.items():
            out[a[v] + x] += theta[v] * px
        distributions[v] = {x: p for x, p in out.items() if p != 0}
        assert sum(distributions[v].values()) == 1
    return means, variances, distributions[0]


def enumerate_transitions(parent, theta, h, gamma, initial, anchors, weights):
    n = len(parent)
    dist = defaultdict(Q)
    marginal = [Q(0)] * n
    cross = [[Q(0) for _ in range(n)] for _ in range(n)]
    for bits in product((0, 1), repeat=n - 1):
        b = (1,) + bits
        prob = Q(1)
        for i in range(1, n):
            prob *= theta[i] if b[i] else (1 - theta[i])
        if prob == 0:
            continue
        active = [0] * n
        active[0] = 1
        x = list(initial)
        for v in range(1, n):
            p = parent[v]
            active[v] = active[p] * b[p]
            if active[v]:
                x[v] = h[v] * ((1 - gamma[v]) * x[v] + gamma[v] * x[p]) + (1 - h[v]) * anchors[v]
        total = sum((weights[i] * (x[i] - initial[i]) for i in range(n)), Q(0))
        dist[total] += prob
        for i in range(n):
            marginal[i] += prob * x[i]
            for j in range(n):
                cross[i][j] += prob * x[i] * x[j]
    return dict(dist), marginal, cross


def run_checks():
    rng = Random(28394)
    total_tests = 0
    for n in range(2, 10):
        # Exhaustive 2^(n-1) broadcast outcomes for each case.
        for rep in range(45):
            parent = [-1] + [rng.randrange(i) for i in range(1, n)]
            theta = [Q(1)] + [Q(rng.randrange(0, 7), 7) for _ in range(1, n)]
            h = [Q(1)] + [Q(rng.randrange(1, 6), 6) for _ in range(1, n)]
            gamma = [Q(0)] + [Q(rng.randrange(1, 6), 6) for _ in range(1, n)]
            initial = [Q(rng.randrange(-4, 5), 4) for _ in range(n)]
            anchors = [Q(rng.randrange(-4, 5), 4) for _ in range(n)]
            weights = [Q(rng.randrange(-3, 4), 3) for _ in range(n)]
            z, delta, a, children = model(parent, theta, h, gamma, initial, anchors, weights)
            mu, va, dist = message_law(theta, a, children)
            actual, node_means, cross = enumerate_transitions(parent, theta, h, gamma, initial, anchors, weights)
            assert dist == actual, (n, rep, 'full distribution')
            expected_m = sum((v * p for v, p in actual.items()), Q(0))
            expected_var = sum((p * (v - expected_m)**2 for v, p in actual.items()), Q(0))
            assert (mu[0], va[0]) == (expected_m, expected_var), (n, rep, 'moments')
            assert all(node_means[i] == initial[i] + delta[i] * (z[i] - initial[i]) for i in range(n))
            for i in range(n):
                anc_i = set()
                x = i
                while x > 0:
                    x = parent[x]
                    anc_i.add(x)
                for j in range(n):
                    anc_j = set()
                    x = j
                    while x > 0:
                        x = parent[x]
                        anc_j.add(x)
                    union = anc_i | anc_j
                    joint = Q(1)
                    for k in union:
                        joint *= theta[k]
                    pred = (z[i] - initial[i]) * (z[j] - initial[j]) * (joint - delta[i]*delta[j])
                    assert cross[i][j] - node_means[i]*node_means[j] == pred, (n, rep, i, j)
            # Explicit nonnegative gate-by-gate variance decomposition.
            decomposition = sum((delta[v] * theta[v] * (1-theta[v]) *
                                 sum((mu[c] for c in children[v]), Q(0))**2
                                 for v in range(n)), Q(0))
            assert decomposition == va[0], (n, rep, 'variance decomposition')
            total_tests += 1
    # Signed opinion changes can cancel all aggregate uncertainty.
    parent = [-1, 0, 1, 1]
    theta = [Q(1), Q(1, 2), Q(1, 3), Q(2, 3)]
    h = [Q(1), Q(1, 2), Q(1, 2), Q(1, 2)]
    gamma = [Q(0), Q(1), Q(1), Q(1)]
    initial = [Q(0), Q(0), Q(-1), Q(1)]
    weights = [Q(0), Q(0), Q(1), Q(1)]
    z, delta, a, children = model(parent,theta,h,gamma,initial,initial,weights)
    m,v,dist = message_law(theta,a,children)
    assert v[0] == 0 and dist == {Q(0): Q(1)}
    print('PASS: %d independent exact-rational finite-tree instances (n=2..9), including all-pair covariances, full law and variance decomposition; cancellation case verified.' % total_tests)


if __name__ == '__main__':
    run_checks()
