"""Finite checks for an exact deletion-pivotality law for random circular directions."""
from fractions import Fraction
from itertools import combinations
from math import comb
import random


def pivotal_count(gaps):
    n = len(gaps)
    if max(gaps) * 2 >= sum(gaps):
        return 0
    total = sum(gaps)
    return sum(2 * (gaps[i-1] + gaps[i]) > total for i in range(n))


def is_contained(gaps):
    return 2 * max(gaps) < sum(gaps)


def pivotal_by_direct_removal(gaps):
    n = len(gaps)
    if not is_contained(gaps):
        return 0
    count = 0
    for i in range(n):
        after = [gaps[j] for j in range(n) if j != (i-1) % n and j != i]
        after.append(gaps[i-1] + gaps[i])
        if not is_contained(after):
            count += 1
    return count


def compositions(n, total):
    if n == 1:
        yield (total,)
        return
    for i in range(total + 1):
        for tail in compositions(n-1, total-i):
            yield (i,)+tail


asserts = 0
for n, denom in ((4,31),(5,27),(6,21),(7,15)):
    for g in compositions(n, denom):
        if any(2*z == denom for z in g):
            continue
        a = pivotal_count(g)
        b = pivotal_by_direct_removal(g)
        assert a == b
        assert a <= 2
        asserts += 2

for n in range(4, 201):
    p0 = Fraction(1) - Fraction(n*(n-3),2**(n-1))
    p1 = Fraction(n*(n-4),2**(n-1))
    p2 = Fraction(n,2**(n-1))
    p_fail = Fraction(n,2**(n-1))
    p_robust_joint = Fraction(1) - Fraction(n*(n-2),2**(n-1))
    assert p0+p1+p2 == 1
    assert all(z >= 0 for z in (p0,p1,p2))
    assert p0-p_fail == p_robust_joint
    assert p1+2*p2 == Fraction(n*(n-2),2**(n-1))
    asserts += 4

rng = random.Random(20261120)
for n in range(4, 11):
    trials = 25000
    cnt = [0,0,0]
    for _ in range(trials):
        gaps = [rng.expovariate(1) for _ in range(n)]
        cnt[pivotal_count(gaps)] += 1
    probs = [1 - n*(n-3)/2**(n-1), n*(n-4)/2**(n-1), n/2**(n-1)]
    for seen, p in zip(cnt, probs):
        assert abs(seen/trials - p) < 0.02
        asserts += 1

print(f"PASS: {asserts} deterministic identities, exhaustive rational-grid geometry comparisons, and seeded auxiliary random checks")
