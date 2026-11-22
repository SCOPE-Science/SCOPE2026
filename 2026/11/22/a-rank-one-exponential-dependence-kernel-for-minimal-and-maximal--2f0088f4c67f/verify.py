#!/usr/bin/env python3
"""Exact finite consequences of a bivariate random graph-order theorem."""
from collections import defaultdict
from fractions import Fraction
from itertools import product


def distribution(n, p):
    q = 1 - p
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    law = defaultdict(Fraction)
    for bits in product((0, 1), repeat=len(edges)):
        minimal = [True] * n
        maximal = [True] * n
        k = sum(bits)
        weight = p**k * q**(len(edges) - k)
        for present, (i, j) in zip(bits, edges):
            if present:
                minimal[j] = False
                maximal[i] = False
        law[(sum(minimal), sum(maximal))] += weight
    return law


def convolve_bernoulli(probs):
    law = {0: Fraction(1)}
    for x in probs:
        out = defaultdict(Fraction)
        for k, prob in law.items():
            out[k] += prob * (1 - x)
            out[k + 1] += prob * x
        law = dict(out)
    return law


def check(n, p):
    q = 1 - p
    joint = distribution(n, p)
    assert sum(joint.values()) == 1
    marg = convolve_bernoulli([q**k for k in range(n)])
    for k in range(1, n + 1):
        assert sum(v for (s, t), v in joint.items() if s == k) == marg.get(k, 0)
        assert sum(v for (s, t), v in joint.items() if t == k) == marg.get(k, 0)
    ms = sum(s * v for (s, t), v in joint.items())
    mt = sum(t * v for (s, t), v in joint.items())
    cov = sum(s * t * v for (s, t), v in joint.items()) - ms * mt
    expected = q**(n-1) * (n * p - 1 + q**n) / p
    weights = sum(q**(n+i-j-3) for j in range(1, n+1)
                  for i in range(j+1, n+1))
    assert weights == q**(n-2) * (n*p - 1 + q**n) / p**2
    assert cov == expected == p * q * weights
    assert cov > 0
    return len(joint)


if __name__ == '__main__':
    checks = 0
    for order in range(2, 7):
        for probability in (Fraction(1, 2), Fraction(2, 3)):
            cells = check(order, probability)
            checks += 1
            print('PASS order', order, 'probability', str(probability), 'joint_cells', cells)
    assert checks == 10
    print('PASS: 10 full rational enumerations and all finite identities')
