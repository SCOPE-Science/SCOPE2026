#!/usr/bin/env python3
"""Reproduce finite checks for the Delannoy fourth-power supercongruence.
No third-party dependencies. Exact integer arithmetic only.
Usage: python3 verify.py
The finite cases corroborate rather than prove the uniform congruence.
"""
from math import comb


def mul(a, b, modulus=None):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i + j] += u * v
            if modulus:
                out[i + j] %= modulus
    return out


def delannoy_coeffs(n):
    return [comb(n, j) * comb(n + j, j) for j in range(n + 1)]


def eval_poly(coeffs, x):
    result = 0
    for c in reversed(coeffs):
        result = result * x + c
    return result


def guo_lemma_4_2(n):
    left = sum(comb(n, i) * comb(2 * i, i) * comb(2 * (n - i), n - i)
               for i in range(n + 1))
    right = sum(comb(2 * i, i) ** 2 * comb(i, n - i) * (-4) ** (n - i)
                for i in range(n + 1) if 0 <= n - i <= i)
    assert left == right, (n, left, right)
    return left


def guo_lemma_4_1(n, x):
    # Exact identity (4.2), not merely a congruence.
    z = x * (x + 1)
    numerator = sum((-1) ** (n - m - 1) * (2 * m + 1) *
                    eval_poly(delannoy_coeffs(m), x) ** 4
                    for m in range(n))
    assert numerator % n == 0
    rhs = 0
    for i in range(n):
        for j in range(n):
            factor = comb(i + j, i) * comb(2 * i, i) * comb(2 * j, j) * z ** (i + j)
            for k in range(i + 1):
                h = j + k
                if h < n and i - k <= j:
                    rhs += (comb(n - 1, h) * comb(n + h, h) *
                            comb(j, i - k) * comb(h, k) * factor)
    assert numerator // n == rhs, (n, x, numerator // n, rhs)


def coefficientwise_conjecture(p):
    modulus = p ** 3
    lhs = [0] * (4 * (p - 1) + 1)
    for m in range(p):
        d = [v % modulus for v in delannoy_coeffs(m)]
        square = mul(d, d, modulus)
        fourth = mul(square, square, modulus)
        factor = (-1) ** m * (2 * m + 1)
        for i, c in enumerate(fourth):
            lhs[i] = (lhs[i] + factor * c) % modulus

    rhs = [0] * len(lhs)
    for r in range((p - 1) // 2 + 1):
        # (x^2+x)^r(2x+1)^(2r) = x^r (1+x)^r (1+2x)^(2r)
        p1 = [0] * r + [comb(r, i) for i in range(r + 1)]
        p2 = [comb(2 * r, i) * 2 ** i for i in range(2 * r + 1)]
        term = mul(p1, p2, modulus)
        factor = p * (-1) ** r * comb(2 * r, r) ** 2
        for i, c in enumerate(term):
            rhs[i] = (rhs[i] + factor * c) % modulus
    assert lhs == rhs, (p, [(i,(a-b)%modulus) for i,(a,b) in enumerate(zip(lhs,rhs)) if a != b][:5])
    return len(lhs)


def normalized_triple_to_double(p):
    # Check the key normalized-mod-p^2 reduction coefficientwise in T=x(x+1).
    modulus = p ** 2
    triple = [0] * (2 * p - 1)
    double = [0] * (2 * p - 1)
    for i in range(p):
        for j in range(p):
            n = i + j
            factor = comb(n, i) * comb(2 * i, i) * comb(2 * j, j)
            double[n] = (double[n] + (-1) ** n * factor) % modulus
            for k in range(i + 1):
                h = j + k
                if h < p and i - k <= j:
                    val = (comb(p - 1, h) * comb(p + h, h) *
                           comb(j, i - k) * comb(h, k) * factor)
                    triple[n] = (triple[n] + val) % modulus
    assert triple == double, (p, [(j, a, b) for j,(a,b) in enumerate(zip(triple,double)) if a != b][:5])
    return len(triple)


def main():
    vals = [guo_lemma_4_2(n) for n in range(0, 23)]
    for n in range(0, 21):
        if n + 2 < len(vals):
            recurrence = ((n + 2) ** 2 * vals[n + 2]
                          - 4 * (3*n*n+9*n+7) * vals[n + 1]
                          + 32 * (n+1)**2 * vals[n])
            assert recurrence == 0, n
    lemma41 = 0
    for n in range(1, 8):
        for x in (-3, -2, -1, 0, 1, 2, 3):
            guo_lemma_4_1(n, x)
            lemma41 += 1
    stratified = (3, 5, 7, 11, 13, 17, 19)
    triple_coefficients = sum(normalized_triple_to_double(p) for p in stratified)
    primes = (3, 5, 7, 11, 13, 17, 19, 23, 29)
    total = sum(coefficientwise_conjecture(p) for p in primes)
    print('VERIFY_OK primes={} coefficients={} lemma_4_2={} recurrence={} lemma_4_1={} intermediate_primes={} intermediate_coefficients={} all_exact=True'.format(
        len(primes), total, len(vals), 21, lemma41, len(stratified), triple_coefficients))

if __name__ == '__main__':
    main()
