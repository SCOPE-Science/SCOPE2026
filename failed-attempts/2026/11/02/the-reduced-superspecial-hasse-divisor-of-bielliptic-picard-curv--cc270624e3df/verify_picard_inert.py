#!/usr/bin/env python3
"""Exact finite-characteristic tests of the inert-prime Picard Cartier identities.
Uses only the Python standard library. The all-prime proof is in RESULT.md.
"""
from math import comb, factorial
from collections import defaultdict

PRIMES = (5, 11, 17, 23, 29, 41, 47, 53, 59, 71, 83, 89, 101, 107, 113, 131, 137, 149, 167, 173, 179, 191, 197)

def coefficient_table(r, k, p):
    result = defaultdict(int)
    for i in range(k // 2 + 1):
        j = k - 2 * i
        l = r - i - j
        if l < 0:
            continue
        v = comb(r, i) * comb(r - i, j)
        result[(j, l)] = (result[(j, l)] + v) % p
    return {key: v for key, v in result.items() if v}

def mul(x, y, p):
    ans = defaultdict(int)
    for (i, j), a in x.items():
        for (k, l), b in y.items():
            ans[(i + k, j + l)] = (ans[(i + k, j + l)] + a * b) % p
    return {key: v for key, v in ans.items() if v}

def eval_a(f, a, p):
    return sum(v * pow(a, k, p) for k, v in enumerate(f)) % p

def trim(f):
    g = f[:]
    while len(g) > 1 and g[-1] == 0:
        g.pop()
    return g

def remainder(a, b, p):
    a, b = trim(a), trim(b)
    assert any(b)
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b) and any(a):
        coef = a[-1] * inv % p
        offset = len(a) - len(b)
        for j, bj in enumerate(b):
            a[j+offset] = (a[j+offset] - coef * bj) % p
        a = trim(a)
    return a

def gcd(a, b, p):
    a, b = trim(a), trim(b)
    while any(b):
        a, b = b, remainder(a, b, p)
    return trim(a)

def test_prime(p):
    assert p > 3 and p % 6 == 5
    m = (p - 5) // 6
    k = 3*m + 2
    B = coefficient_table(2*m + 1, k, p)
    A = coefficient_table(4*m + 3, k, p)
    D = {(2*(m+1-t), m+1+t): comb(m+1,t) * pow(-4,t,p) % p
         for t in range(m+2)}
    const = comb(4*m+3, m+1) * pow(comb(2*m+1,m), -1,p) % p
    right = {e: const*v % p for e,v in mul(B,D,p).items() if const*v%p}
    assert A == right, (p, A, right)
    poly = [0]*(m+1)
    for (i,j),v in B.items():
        poly[i] = (poly[i]+v) % p
    assert poly[m] != 0
    assert eval_a(poly,2,p) and eval_a(poly,-2,p)
    derivative = [j*poly[j] % p for j in range(1,len(poly))] or [0]
    assert len(gcd(poly, derivative, p)) == 1
    for a in range(p) if p <= 59 else ():
        b = 1
        B_val = sum(v*pow(a,i,p)*pow(b,j,p) for (i,j),v in B.items())%p
        A_val = sum(v*pow(a,i,p)*pow(b,j,p) for (i,j),v in A.items())%p
        assert A_val == const * pow(b,m+1,p)*pow(a*a-4*b,m+1,p)*B_val %p
        if (a*a-4*b)%p:
            assert (A_val==0)==(B_val==0)
    return (p,m,const)

if __name__ == '__main__':
    out = [test_prime(p) for p in PRIMES]
    print('Verified exact bivariate Cartier coefficient identity and squarefree Hasse polynomial in',len(out),'inert primes')
    print('prime / degree / identity scalar:',out)
    print('PICARD_INERT_PRIME_CARTIER_CHECKS_PASS')
