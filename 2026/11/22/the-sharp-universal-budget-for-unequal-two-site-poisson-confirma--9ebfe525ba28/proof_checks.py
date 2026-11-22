#!/usr/bin/env python3
"""Standalone exact-arithmetic and numerical checks for a two-confirmation site allocation theorem.
Only standard Python libraries are used. Finite checks do not replace the analytic proof.
"""
from fractions import Fraction as F
from math import factorial, exp, cosh, sinh
from random import Random

count = 0

def check(test, label):
    global count
    assert test, label
    count += 1


def exp_enclosure(x, n=96):
    """Certified rational enclosure for exp(x), x a nonnegative rational."""
    assert x >= 0 and F(n + 2) > x
    term = F(1)
    total = F(1)
    for k in range(1, n + 1):
        term *= x / k
        total += term
    next_term = term * x / (n + 1)
    top = total + next_term / (1 - x / (n + 2))
    return total, top


def eneg(x):
    lo, hi = exp_enclosure(x)
    return F(1) / hi, F(1) / lo


def qa(x, p):
    qlo, qhi = eneg(x)
    base = 1 - p
    coeff = p * (1 + x)
    return base + coeff * qlo, base + coeff * qhi


def positive_product(a, b):
    return a[0] * b[0], a[1] * b[1]


def g_numerator(y):
    poslo, poshi = exp_enclosure(y)
    neglo, neghi = eneg(y)
    clo, chi = (poslo + neglo) / 2, (poshi + neghi) / 2
    offset = 1 + y + y * y * (y - 1) / 2
    return clo + y * neglo - offset, chi + y * neghi - offset


def exact_tests():
    # Sharp Bc root bracket with rational interval arithmetic.
    left, right = F(420103, 100000), F(420104, 100000)
    check(g_numerator(left)[1] < 0, 'critical-root lower sign')
    check(g_numerator(right)[0] > 0, 'critical-root upper sign')
    # A robust exactly specified asymmetric example.
    p, B, x = F(999, 1000), F(41, 4), F(3)
    asymmetric = positive_product(qa(x, p), qa(B - x, p))
    concentrated = qa(B, p)
    symmetric = positive_product(qa(B / 2, p), qa(B / 2, p))
    check(asymmetric[1] < concentrated[0], 'asymmetric beats concentration')
    check(asymmetric[1] < symmetric[0], 'asymmetric beats equal')
    check(concentrated[1] < symmetric[0], 'concentrated beats equal, despite neither being global')
    # Exact first and second derivative identities, independently by finite differences checked below.
    return left, right, asymmetric, concentrated, symmetric


def numeric_tests():
    random = Random(4019)
    for _ in range(2400):
        p = 0.001 + 0.998 * random.random()
        B = 0.001 + 8.4 * random.random()
        x = B * random.random()
        q = lambda z: 1 - p + p * (1 + z) * exp(-z)
        target = q(x) * q(B - x)
        bestendpoint = min(q(B), q(B / 2)**2)
        check(target >= bestendpoint - 3e-13, 'subcritical global endpoint-or-equal law')
    for _ in range(2400):
        y = 3.2 + 7.0 * random.random()
        t = y * random.random()
        a = 0.0001 + 100 * random.random()
        H = lambda z: (1+y)*(cosh(z)-1)-z*sinh(z)
        Fvalue = lambda z: (y-1)/2 if z == 0 else H(z)/z**2
        P = lambda z: (1+y)**2 - z*z + 2*a*((1+y)*cosh(z)-z*sinh(z))+a*a
        residual = P(t)-P(0)-t*t*(2*a*Fvalue(t)-1)
        check(abs(residual) < 5e-8 * max(1, abs(P(0))), 'factorization identity')
    for _ in range(2400):
        y = 0.1 + 10 * random.random()
        t = 0.001 + y * random.random()
        a = 0.0001 + 100 * random.random()
        P = lambda z: (1+y)**2 - z*z + 2*a*((1+y)*cosh(z)-z*sinh(z))+a*a
        eps = min(0.00001, t / 10)
        d = (P(t+eps)-P(t-eps))/(2*eps)
        prediction = 2*t*(a*(y*sinh(t)/t-cosh(t))-1)
        check(abs(d-prediction) <= 2e-5 * max(1, abs(prediction)), 'stationary-point derivative')

if __name__ == '__main__':
    lo, hi, a, c, s = exact_tests()
    numeric_tests()
    print('all checks passed:', count)
    print('critical y bracket:', lo, hi)
    print('asymmetric success probability lower bound:', float(1 - a[1]))
    print('symmetric success probability upper bound:', float(1 - s[0]))
