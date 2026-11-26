"""Exact finite-field checks for the bielliptic Picard superspecial-locus theorem.

This verifier illustrates finite instances of identities proved uniformly in the
accompanying mathematical argument. It does not replace the proof for all primes.
Pure Python 3 standard library; no external input or network access.
"""
from math import factorial


def trim(v):
    v = list(v)
    while len(v) > 1 and v[-1] == 0:
        v.pop()
    return v


def add(a, b, p):
    return trim([((a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)) % p
                 for i in range(max(len(a), len(b)))])


def scale(a, s, p):
    return trim([int(s * x % p) for x in a])


def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % p
    return trim(c)


def powpoly(a, n, p):
    res = [1]
    while n:
        if n & 1:
            res = mul(res, a, p)
        a = mul(a, a, p)
        n >>= 1
    return res


def derivative(a, p):
    return trim([(i * a[i]) % p for i in range(1, len(a))] or [0])


def rem(a, b, p):
    a = trim(a)
    b = trim(b)
    assert b != [0]
    while a != [0] and len(a) >= len(b):
        d = len(a) - len(b)
        c = a[-1] * pow(b[-1], -1, p) % p
        for i in range(len(b)):
            a[i + d] = (a[i + d] - c * b[i]) % p
        a = trim(a)
    return a


def monic_gcd(a, b, p):
    while b != [0]:
        a, b = b, rem(a, b, p)
    return scale(a, pow(a[-1], -1, p), p)


def B(n, k, p):
    assert 0 <= k <= 2*n < 2*p
    d = min(k, 2*n-k)
    out = [0]*(d+1)
    for r in range(d//2 + 1):
        j = d-2*r
        out[j] = (factorial(n) //
                  (factorial(r)*factorial(j)*factorial(n-d+r))) % p
    return trim(out)


def ode(poly, n, d, p):
    D = [(-4)%p, 0, 1]
    part1 = mul(D, derivative(derivative(poly, p), p), p)
    part2 = mul([0, 1], derivative(poly, p), p)
    return add(add(part1, scale(part2, -(2*n-1), p), p),
               scale(poly, d*(2*n-d), p), p)


def primes_under(bound):
    for p in range(5, bound):
        if all(p % q != 0 for q in range(2, int(p**.5)+1)):
            yield p


D = [0, 0, 1]  # replaced modulo prime below
checked = 0
for p in primes_under(200):
    if p % 6 != 5:
        continue
    m = (p-5)//6
    smalln, bign, k = 2*m+1, 4*m+3, 3*m+2
    Q, P = B(smalln, k, p), B(bign, k, p)
    D = [(-4)%p, 0, 1]
    leading_c = P[-1]*pow(Q[-1], -1, p)%p
    rhs = scale(mul(powpoly(D, m+1, p), Q, p), leading_c, p)
    assert P == rhs, ('coefficient identity', p)
    assert ode(Q, smalln, m, p) == [0], ('Q ODE', p)
    assert ode(P, bign, 3*m+2, p) == [0], ('P ODE', p)
    assert len(Q) == m+1, ('degree', p)
    assert monic_gcd(Q, derivative(Q, p), p) == [1], ('separable', p)
    assert monic_gcd(Q, D, p) == [1], ('smooth roots', p)
    checked += 1

assert B(1, 2, 5) == [1]
assert B(3, 5, 11) == [0, 3]
assert B(5, 8, 17) == [5, 0, 10]
assert B(7, 11, 23) == [0, 19, 0, 12]
assert [a for a in range(17) if sum(c * pow(a, i, 17)
       for i, c in enumerate(B(5, 8, 17))) % 17 == 0] == [5, 12]
print('EXACT_COEFFICIENT_AND_ODE_TESTS', checked, 'PRIMES_P_CONGRUENT_5_MOD_6_BELOW_200')
print('SQUAREFREE_AND_DISCRIMINANT_COPRIMALITY=OK')
print('P_17_Q_POLYNOMIAL_COEFFICIENTS_ASCENDING', B(5, 8, 17))
print('P_17_SUPERSPECIAL_PARAMETERS', [5, 12])
print('P_23_Q_POLYNOMIAL_COEFFICIENTS_ASCENDING', B(7, 11, 23))
print('VERIFY_OK')
