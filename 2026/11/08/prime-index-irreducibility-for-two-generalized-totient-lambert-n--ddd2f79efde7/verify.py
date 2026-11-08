"""Exact finite checks for two prime-index Lambert-series numerator identities.

This script tests polynomial identities and the explicit Eisenstein hypotheses
in finitely many cases. The proofs of the infinite statements are in RESULT.md.
"""
from math import comb


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def plus(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim(c)


def times(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] += u * v
    return trim(c)


def scalar(a, k):
    return trim([k * x for x in a])


def monomial(k, coeff):
    return [0] * k + [coeff]


def compose_square(a):
    b = [0] * (2 * len(a) - 1)
    for i, v in enumerate(a):
        b[2 * i] = v
    return trim(b)


def value(a, x):
    r = 0
    for v in reversed(a):
        r = r * x + v
    return r


def shift_by_one(a):
    out = [0] * len(a)
    for j, c in enumerate(a):
        for k in range(j + 1):
            out[k] += c * comb(j, k)
    return trim(out)


def prime_list(limit):
    result = []
    for n in range(2, limit + 1):
        if all(n % d for d in range(2, int(n ** 0.5) + 1)):
            result.append(n)
    return result


def check_prime(p):
    s = [1] * p
    sq = times(s, s)
    P = plus(sq, monomial(p - 1, p))
    assert len(P) == 2 * p - 1 and P[-1] == 1
    assert value(P, 1) == p * (p + 1)
    Q = plus(
        times(P, times(plus([1], monomial(p, 1)), plus([1], monomial(p, 1)))),
        scalar(times(monomial(1, 1), compose_square(P)), -2),
    )
    shifted_P = shift_by_one(P)
    assert shifted_P[-1] == 1
    assert shifted_P[0] == p * (p + 1)
    assert all(c % p == 0 for c in shifted_P[:-1])
    assert shifted_P[0] % (p * p) != 0
    if p % 2:
        r = (p - 1) // 2
        T = [(-1)**j for j in range(p)]
        H = plus(sq, times(monomial(r, p), T))
        assert H[-1] == 1 and len(H) == 2*p - 1
        assert Q == times([1, 0, 1], compose_square(H))
        shifted_H = shift_by_one(H)
        assert shifted_H[-1] == 1
        assert shifted_H[0] == p * (p + 1)
        assert all(c % p == 0 for c in shifted_H[:-1])
        assert shifted_H[0] % (p*p) != 0
        if p % 4 == 3:
            assert value(H, -1) == 1 - p * p
            assert value(H, 0) == 1
        else:
            assert value(H, -1) == 1 + p * p
    return p


if __name__ == '__main__':
    primes = prime_list(47)
    for p in primes:
        check_prime(p)
    print('VERIFY_OK primes_2..47=%d p_congruence_three_mod_four=%d identities=PASS shifted_Eisenstein=PASS negative_root_sign=PASS' % (
        len(primes), sum(p % 4 == 3 for p in primes)))
