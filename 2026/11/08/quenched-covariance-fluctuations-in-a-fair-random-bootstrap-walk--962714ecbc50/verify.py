"""Exact finite-horizon checks for Bernoulli-scene bootstrap covariation.

The proof of its infinite-horizon limit theorems is analytic; these
finite checks verify algebraic identities and normalizations only.
"""
from fractions import Fraction
from itertools import product
from math import comb

checks = 0

# The lower-triangular parity/Pascal transform is bijective over F_2.
for m in range(1, 9):
    images = set()
    for beta in product((0, 1), repeat=m):
        omega = tuple(1 if sum((comb(j, k) & 1) * beta[k] for k in range(j + 1)) % 2 == 0 else -1 for j in range(m))
        images.add(omega)
    assert len(images) == (1 << m)
    checks += 1

# Pathwise Poisson-equation/coboundary identity and predictable increment signs.
for n in range(1, 9):
    total, total2, cnt = 0, 0, 0
    for scene in product((-1, 1), repeat=n):
        a = [0]
        for w in scene:
            a.append(a[-1] + w)
        for bits in product((0, 1), repeat=n):
            s, obs, mart = 0, 0, 0
            for b in bits:
                obs += scene[s]
                mart += (1 - 2*b)*scene[s]
                s += b
                assert obs == 2*a[s] + mart
                checks += 1
            q = obs + 1 - scene[0]
            total += q
            total2 += q*q
            cnt += 1
    mean = Fraction(total, cnt)
    var = Fraction(total2, cnt) - mean * mean
    assert mean == 1
    assert var == 3*n - 7 + Fraction(8, 2**n)
    checks += 2

# For each fixed scenery the martingale increment sequence is exactly iid fair.
for n in range(1, 7):
    for scene in product((-1, 1), repeat=n):
        outputs = set()
        for bits in product((0, 1), repeat=n):
            s=0
            increments=[]
            for b in bits:
                increments.append((1-2*b)*scene[s])
                s += b
            outputs.add(tuple(increments))
        assert len(outputs) == (1 << n)
        checks += 1

print(f"PASS: {checks:,} exact integer/rational assertions; n <= 8 for variance, n <= 6 for conditional iid transform")
