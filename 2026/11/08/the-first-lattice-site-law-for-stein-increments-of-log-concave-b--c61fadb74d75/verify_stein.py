#!/usr/bin/env python3
"""Finite rational diagnostics for log-concave constant-birth Stein factor identities.

Run: python3 verify_stein.py. Python standard library only.
The infinite-support statements are proved analytically in RESULT.md; finite tests
are diagnostics and are not substituted for proof.
"""
from fractions import Fraction as F
from itertools import combinations
import math

checks = 0

def test(ok, message):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(message)

def probabilities(weights):
    total = sum(weights)
    return [x / total for x in weights]

def test_case(weights):
    p = probabilities(weights)
    N = len(p) - 1
    r = [None] + [p[j] / p[j-1] for j in range(1, N+1)]
    for j in range(2, N+1):
        test(r[j] <= r[j-1], 'input not log-concave')
    pref = [sum(p[:j+1]) for j in range(N+1)]
    tail = [sum(p[j:]) for j in range(N+1)] + [F(0)]
    best = F(0)
    for j in range(1, N):
        C = tail[j+1] + r[j] * pref[j-1]
        gap = sum((p[i] * (r[i+1] - r[j]) for i in range(j)), F(0))
        test(C == (1-p[0]) - gap, 'exact deficit')
        test(gap >= 0, 'deficit sign')
        test(C <= 1-p[0], 'global factor')
        test((gap == 0) == all(r[i+1] == r[j] for i in range(j)), 'optimizer classification')
        positive_singleton = F(0)
        localmax = F(0)
        for mask in range(1 << (N+1)):
            a = [(mask >> i) & 1 for i in range(N+1)]
            pa = sum((p[i] for i in range(N+1) if a[i]),F(0))
            def g(m):
                if m == 0:
                    return F(0)
                return sum(((a[i]-pa)*p[i] for i in range(m)), F(0)) / p[m-1]
            step = g(j+1) - g(j)
            if mask == (1 << j):
                positive_singleton = step
            localmax = max(localmax, abs(step))
            test(abs(step) <= C, 'subset bound')
        test(localmax == C, 'pointwise envelope')
        test(positive_singleton == C, 'singleton attains')
        best = max(best, localmax)
    test(best == 1-p[0], 'global optimizer at j=1')
    # First increment at the boundary, with g(0) = 0.
    for mask in range(1 << (N+1)):
        a = [(mask >> i) & 1 for i in range(N+1)]
        pa = sum((p[i] for i in range(N+1) if a[i]),F(0))
        g1 = F(a[0]) - pa
        test(abs(g1) <= 1-p[0], 'zero-boundary step')

pool = [F(4), F(3), F(2), F(1), F(2,3), F(1,2), F(1,3), F(1,4)]
for ids in combinations(range(len(pool)),5):
    weights = [F(1)]
    for idx in ids:
        weights.append(weights[-1]*pool[idx])
    test_case(weights)
for q in [F(1,5), F(1,2), F(4,5)]:
    weights = [q**j for j in range(7)]
    test_case(weights)

# The super-geometric family has infinitely many strictly positive atoms.
# The finite prefixes below check numerical asymptotics only; the proof
# bounds the omitted tail explicitly.
ratios = []
for den in [10, 20, 50, 100, 200]:
    t = F(1, den)
    a = [t**((j-1)**2) for j in range(11)]
    p = probabilities(a)
    mean = sum((j*p[j] for j in range(11)), F(0))
    var = sum(((F(j)-mean)**2*p[j] for j in range(11)), F(0))
    ratio = float((1-p[0])) / math.sqrt(float(var))
    ratios.append(ratio)
    test(ratio > 0, 'positive factor-to-sd ratio')
    test(abs(float(var / (2*t))-1) < 0.4, 'variance asymptotics')
for a, b in zip(ratios, ratios[1:]):
    test(a < b, 'ratio diverges in diagnostics')
print(f'PASS {checks} exact-rational and numeric diagnostic assertions')
print('Near-point-mass lower ratios:', ', '.join(f'{x:.4f}' for x in ratios))
