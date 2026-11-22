#!/usr/bin/env python3
"""Reproduce the saturation-composition theorem's numerical and algebraic checks.

The proof is analytic. These finite checks test implementations and examples;
they do not certify the universal quantifiers.
"""
import math
import random


def S(v, q):
    return -math.expm1(v * math.log(q)) / (1.0 - q)


def Sp(v, q):
    z = q ** v
    return (1.0 - z - v * q ** (v - 1.0) * (1.0 - q)) / (1.0 - q) ** 2


def H(m, r, q):
    return S(m, q) * Sp(r, q) / Sp(m, q) - S(r, q)


def p(a, b, c, m, r, q):
    return b * S(m, q) / (a + b * S(m, q) + c * S(r, q))


def stationary_q(a, c, m, r):
    threshold = r * (r - m) / (m - 1.0)
    if a / c >= threshold:
        return None
    lo, hi = 1e-11, 1.0 - 1e-9
    for _ in range(95):
        mid = (lo + hi) / 2
        if H(m, r, mid) < a / c:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    rng = random.Random(481109)
    checks = 0
    # Compare the exact quotient-rule derivative with its factorization.
    for _ in range(9000):
        m = rng.uniform(1.15, 9)
        r = m + rng.uniform(0.3, 35)
        q = rng.uniform(0.03, 0.89)
        a, b, c = (math.exp(rng.uniform(-2, 2)) for _ in range(3))
        sm, sr = S(m, q), S(r, q)
        smp, srp = Sp(m, q), Sp(r, q)
        den = a + b * sm + c * sr
        derivative = b * (smp * den - sm * (b * smp + c * srp)) / den**2
        factorized = b * smp * (a - c * H(m, r, q)) / den**2
        assert math.isclose(derivative, factorized, abs_tol=1e-9, rel_tol=1e-8)
        checks += 1
    # Strict positivity and endpoint values for H and its derivative-ratio.
    for _ in range(3000):
        m = rng.uniform(1.15, 7)
        r = m + rng.uniform(0.4, 40)
        x = [0.04 + j * 0.88 / 50 for j in range(51)]
        vals = [H(m, r, z) for z in x]
        assert all(vals[i + 1] > vals[i] for i in range(len(vals) - 1))
        assert vals[0] > 0 and vals[-1] < r * (r - m) / (m - 1)
        checks += 1
    # Existence, uniqueness, derivative sign, and monotone/nonmonotone phases.
    for _ in range(4000):
        m = rng.uniform(1.2, 8)
        r = m + rng.uniform(0.5, 50)
        c = math.exp(rng.uniform(-2, 2))
        threshold = r * (r - m) / (m - 1)
        a = c * threshold * rng.uniform(0.0005, 0.999)
        b = math.exp(rng.uniform(-2, 2))
        q = stationary_q(a, c, m, r)
        assert q is not None
        assert abs(H(m, r, q) - a / c) < 3e-7 * max(1, a/c)
        assert p(a, b, c, m, r, q) > p(a, b, c, m, r, min(0.99999, (q + 1) / 2))
        assert p(a, b, c, m, r, q) > p(a, b, c, m, r, q / 2)
        assert stationary_q(a + 2 * c * threshold, c, m, r) is None
        checks += 1
    # Endpoint-matched compositions have one peak and amplification strictly < m.
    for _ in range(3000):
        m = rng.uniform(1.2, 15)
        r = m + rng.uniform(0.5, 75)
        b, c = math.exp(rng.uniform(-3, 3)), math.exp(rng.uniform(-3, 3))
        a = c * (r - m) / (m - 1)
        p0 = b / (a + b + c)
        assert math.isclose(p0, b*m/(a + b*m + c*r), rel_tol=1e-12)
        q = stationary_q(a, c, m, r)
        assert q is not None
        pp = p(a, b, c, m, r, q)
        assert p0 < pp < m * p0
        checks += 1
    # Scale-sharpness and exact symmetric 1:2:3 example.
    a=b=c=1.0
    q = math.sqrt(2.0)-1.0
    assert math.isclose(H(2, 3, q), a/c, rel_tol=1e-12)
    assert math.isclose(p(a,b,c,2,3,q), math.sqrt(2)/4, rel_tol=1e-12)
    assert math.isclose(-math.log(q), math.log(1+math.sqrt(2)), rel_tol=1e-12)
    checks += 3
    for m in (1.5, 2, 5, 12):
        r = 1_000_000.0
        a = (r-m)/(m-1)
        q = 1.0 - 1.0/math.sqrt(r)
        fold = p(a,1,1,m,r,q)/(1/(a+2))
        assert fold < m and fold > 0.96*m
        checks += 1
    print(f'PASS: {checks} independent numerical/algebraic assertions')
    print('Example 1:1:1 amplitude, 1:2:3 rates: t*=log(1+sqrt(2)), p*=sqrt(2)/4')
    print('Finite assertions are only supplementary to the analytic proof.')

if __name__ == '__main__':
    main()
