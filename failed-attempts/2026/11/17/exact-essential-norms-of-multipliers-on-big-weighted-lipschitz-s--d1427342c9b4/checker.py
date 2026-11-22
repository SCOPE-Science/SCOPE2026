#!/usr/bin/env python3
"""Finite-coordinate checks for weighted rooted-tree multiplier identities.

These checks supplement, and do not replace, the infinite-dimensional proof.
"""
import cmath
import math
import random

rng = random.Random(260213534)
checks = 0

for trial in range(120):
    n = rng.randrange(5, 42)
    parent = [-1]
    depth = [0]
    for v in range(1, n):
        p = rng.randrange(v)
        parent.append(p)
        depth.append(depth[p] + 1)
    c = [1.0] + [math.exp(rng.uniform(-2.0, 2.0)) for _ in range(1, n)]
    psi = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(n)]
    x = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(n)]
    f = [0j] * n
    f[0] = x[0]
    for v in range(1, n):
        f[v] = f[parent[v]] + x[v] / c[v]
    y = [psi[0] * x[0]] + [0j] * (n - 1)
    for v in range(1, n):
        y[v] = c[v] * (psi[v] * f[v] - psi[parent[v]] * f[parent[v]])
        delta = psi[v] - psi[parent[v]]
        row = psi[v] * x[v] + c[v] * delta * f[parent[v]]
        assert abs(y[v] - row) < 1e-10
        checks += 1
    for k in range(max(depth) + 1):
        tails = []
        for v in range(1, n):
            if depth[v] <= k:
                continue
            delta = psi[v] - psi[parent[v]]
            ancestors = []
            w = parent[v]
            while w > 0:
                if depth[w] > k:
                    ancestors.append(w)
                w = parent[w]
            predicted = abs(psi[v]) + c[v] * abs(delta) * sum(1 / c[w] for w in ancestors)
            explicit = [psi[v]] + [c[v] * delta / c[w] for w in ancestors]
            assert abs(predicted - sum(abs(a) for a in explicit)) < 1e-11
            checks += 1
            if explicit:
                phased = [a.conjugate() / abs(a) if abs(a) else 1 for a in explicit]
                attained = abs(sum(a * z for a, z in zip(explicit, phased)))
                assert abs(attained - predicted) < 1e-10
                checks += 1
            tails.append(predicted)
        if tails:
            assert max(tails) <= sum(2 * abs(z) for z in psi) * (max(c) / min(c)) * n
            checks += 1

# On a ray with exponentially growing edge weights, a compact multiplier
# need not preserve the corresponding little weighted Lipschitz space.
for K in range(0, 22):
    c = lambda j: 2.0 ** j
    psi = lambda j: 2.0 ** (-j)
    for n in range(K + 1, K + 48):
        d = psi(n) - psi(n-1)
        v = abs(psi(n)) + c(n) * abs(d) * sum(1/c(j) for j in range(K + 1, n))
        assert v <= 2.0 ** (-K) + 1e-12
        checks += 1
    assert abs(c(K + 1) * (psi(K + 1) - psi(K))) == 1.0
    checks += 1
print(f"PASS: {checks} finite identities and estimates")
