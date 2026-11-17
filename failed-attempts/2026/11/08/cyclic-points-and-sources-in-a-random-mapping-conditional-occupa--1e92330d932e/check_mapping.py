#!/usr/bin/env python3
"""Exact small-n checks for cyclic-point / zero-indegree statistics of a uniform random mapping."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, factorial


def cyclic_count(f):
    n = len(f)
    seen = [False] * n
    result = 0
    for start in range(n):
        x = start
        path, pos = [], {}
        while x not in pos and not seen[x]:
            pos[x] = len(path)
            path.append(x)
            x = f[x]
        if x in pos:
            result += len(path) - pos[x]
        for y in path:
            seen[y] = True
    return result


def falling(n, k):
    z = 1
    for i in range(k):
        z *= n-i
    return z


def conditional_binom(n, k, r):
    if k == n:
        return F(int(r == 0))
    if r > n-k:
        return F(0)
    return F(comb(n-k, r)) * F(n-r, n) ** (n-k-1)


def conditional_pmf(n, k, z):
    if k == n:
        return F(int(z == 0))
    t = n-k
    if z > t:
        return F(0)
    return comb(t, z) * sum(((-1)**j) * comb(t-z, j) * F(n-z-j, n)**(t-1)
                            for j in range(t-z+1))


checks = 0
for n in range(2, 8):
    groups = defaultdict(lambda: defaultdict(int))
    for f in product(range(n), repeat=n):
        k = cyclic_count(f)
        z = n-len(set(f))
        groups[k][z] += 1
    for k in range(1, n+1):
        d = groups[k]
        total = sum(d.values())
        expected_count = F(k * falling(n, k) * n**n, n**(k+1))
        assert total == expected_count, (n, k, total, expected_count)
        checks += 1
        for z in range(n+1):
            actual = F(d[z], total)
            assert actual == conditional_pmf(n, k, z), (n, k, z, actual)
            checks += 1
        for r in range(n+1):
            actual = F(sum(comb(z, r)*v for z, v in d.items() if z >= r), total)
            assert actual == conditional_binom(n, k, r), (n, k, r, actual)
            checks += 1
    means = [sum(F(z*v, sum(groups[k].values())) for z, v in groups[k].items())
             for k in range(1, n+1)]
    assert all(means[i] > means[i+1] for i in range(len(means)-1)), (n, means)
    checks += 1
    print(f"n={n}: {n**n} complete mappings verified")

for n in range(2, 101):
    means = [conditional_binom(n,k,1) for k in range(1,n+1)]
    assert all(means[i] > means[i+1] for i in range(n-1))
    checks += 1

print(f"VERIFY_OK {checks} exact assertions")
