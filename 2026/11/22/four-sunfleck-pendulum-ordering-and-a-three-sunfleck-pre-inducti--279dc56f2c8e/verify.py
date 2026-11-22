#!/usr/bin/env python3
"""Reproducible rational checks for the finite sunfleck ordering theorem.

All computations use exact fractions. The mathematical proof applies to
arbitrary positive real durations and is independent of these samples.
"""
from fractions import Fraction as F
from itertools import permutations
from random import Random

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def score(values, s, q):
    # Dimensionless carbon score after removal of the fixed total light time.
    deficit = 1 - s
    loss = F(0)
    for u in values:
        loss += deficit * u
        deficit = 1 - q + q * (1 - u) * deficit
    return -loss

def Q4(v, q):
    a, b, c, d = v
    return (q * (a*b + b*c + c*d)
            + q*q * (a*(1-b)*c + b*(1-c)*d)
            + q*q*q * a*(1-b)*(1-c)*d)

rng = Random(20261121)
for k in range(4000):
    a, b, c, d = sorted(F(i, 101) for i in rng.sample(range(1, 101), 4))
    q = F(rng.randrange(1, 100), 100)
    s = F(rng.randrange(0, 101), 100)
    u = [a, b, c]
    actual = {p: score(p, s, q) for p in permutations(u)}
    top = max(actual.values())
    predicted = (b, c, a) if s < q*a else (c, b, a)
    check(actual[predicted] == top, 'three-pulse max')
    if s == 0:
        check(actual[(a, c, b)] == top, 'zero-induction reverse tie')
    elif s == q*a:
        check(actual[(b, c, a)] == actual[(c, b, a)] == top, 'threshold tie')
    else:
        check(sum(v == top for v in actual.values()) == 1, 'unique three-pulse optimizer')
    # Three adjacent/reversal interchange identities.
    check(score((a, b, c), s, q) - score((b, a, c), s, q)
          == (1-q)*(a-b)*(s-q*c), 'first adjacent identity')
    check(score((a, b, c), s, q) - score((a, c, b), s, q)
          == q*(1-q)*(b-c)*(a+(1-a)*s), 'last adjacent identity')
    check(score((a, b, c), s, q) - score((c, b, a), s, q)
          == s*(1-q)*(a-c)*(1+q*(1-b)), 'end reversal identity')

    vals = [a, b, c, d]
    all4 = {p: score(p, F(0), q) for p in permutations(vals)}
    best = max(all4.values())
    p = (a, c, d, b)
    reverse = tuple(reversed(p))
    check(all4[p] == best == all4[reverse], 'four-pulse pendulum max')
    check(sum(v == best for v in all4.values()) == 2, 'unique reverse pair')
    for perm, value in all4.items():
        check(value == Q4(perm, q) - sum(perm), 'four-pulse Q identity')

# A small rational boundary and numerical illustration.
a, b, c, d = F(1, 5), F(1, 4), F(1, 2), F(3, 4)
q = F(1, 2)
check(Q4((a,c,d,b),q) == F(459, 1280), 'exact four-pulse value')
check(Q4((a,b,c,d),q) == F(83, 256), 'monotone order comparison')
check(Q4((a,c,d,b),q) - Q4((a,b,c,d),q) == F(11, 320), 'exact advantage')
A,B,C = a,c,d
check(score((B,C,A),F(1,10),q) == score((C,B,A),F(1,10),q), 'preinduction tie')
check(score((B,C,A),F(0),q) == score((A,C,B),F(0),q), 'uninduced reflection')
print(f'PASS: {checks} exact rational assertions')
