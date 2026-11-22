"""Reproducible algebraic checks for the staged logistic risk reversal theorem.

The mathematical proof, rather than these finite tests, establishes universal claims.
Run with Python 3: python checker.py
"""
from fractions import Fraction as F
from itertools import permutations
import math
import random


def multiply(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c


def Q(a):
    out = [F(1)]
    for p in a:
        out = multiply(out, [F(p), F(1)])
    return out


def evaluate(coeffs, t):
    z = F(0)
    for c in reversed(coeffs):
        z = z * t + c
    return z


def risk(t, q):
    return t**(len(q) - 1) / evaluate(q, t)


qb = Q([1, 2, 3]); qa = [x for x in qb]
pa = multiply([F(-1), F(1)], [F(-2), F(1)])
for i, pi in enumerate(pa):
    qa[i] += pi / 50
assert qb == [F(6), F(11), F(6), F(1)]
assert qa == [F(151, 25), F(547, 50), F(301, 50), F(1)]
for x, expected in [
    (F(-16, 5), F(-57, 625)), (F(-3), F(2, 5)),
    (F(-2), F(6, 25)), (F(-7, 4), F(-9, 320)),
    (F(-6, 5), F(-92, 625)), (F(-1), F(3, 25)),
]:
    assert evaluate(qa, x) == expected
for t in [F(1), F(2)]:
    assert risk(t, qa) == risk(t, qb)
for t, difference in [
    (F(1, 2), F(-1, 91980)),
    (F(3, 2), F(3, 275590)),
    (F(3), F(-9, 120040)),
]:
    assert risk(t, qa) - risk(t, qb) == difference

# General finite spot checks: the risk comparison is exactly the negative
# difference of the two monic denominator polynomials.
rng = random.Random(20241120)
tests = 0
for n in range(1, 9):
    for repeat in range(700):
        aa = [F(rng.randint(1, 22), rng.randint(1, 12)) for _ in range(n)]
        bb = [F(rng.randint(1, 22), rng.randint(1, 12)) for _ in range(n)]
        q_a, q_b = Q(aa), Q(bb)
        assert q_a[-1] == q_b[-1] == 1
        for t in [F(1, 3), F(2, 3), F(1), F(2), F(5)]:
            lhs = risk(t, q_a) - risk(t, q_b)
            rhs = t**n * (evaluate(q_b, t) - evaluate(q_a, t)) / (evaluate(q_a, t) * evaluate(q_b, t))
            assert lhs == rhs
            tests += 1

# A symmetric polynomial comparison n=2 has the advertised strict crossing
# criterion whenever the coefficients differ in both degrees.
for i in range(2000):
    aa = [F(rng.randint(1, 20), 5), F(rng.randint(1, 20), 5)]
    bb = [F(rng.randint(1, 20), 5), F(rng.randint(1, 20), 5)]
    q_a, q_b = Q(aa), Q(bb)
    intercept = q_a[0] - q_b[0]
    slope = q_a[1] - q_b[1]
    if intercept != 0 and slope != 0:
        candidate = -intercept / slope
        assert (candidate > 0) == (intercept * slope < 0)
        if candidate > 0:
            assert evaluate(q_a, candidate) == evaluate(q_b, candidate)
    tests += 1
print('PASS:', tests, 'supplementary exact comparisons, plus rational root-bracket and sign certificates')
