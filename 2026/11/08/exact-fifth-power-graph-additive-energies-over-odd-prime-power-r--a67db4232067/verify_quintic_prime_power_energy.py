#!/usr/bin/env python3
"""Exact finite checks for fifth-power graph energy over odd, 5-free residue rings.

Uses standard-library integer arithmetic. Finite checks are not a proof for all moduli.
"""
from collections import Counter
from math import prod


def local_coefficients(p):
    assert p % 2 and p != 5 and p >= 3
    chi = 1 if p % 4 == 1 else -1
    d = 3 * (p - 1) * (2 + chi)
    s = 4 * p * p - 6 * p + 2 - 6 * (p - 1) * (1 + chi)
    return s, d


def local_energy(p, k):
    assert k >= 0
    if k == 0:
        return 1
    s, d = local_coefficients(p)
    regular = p ** (2 * k - 2) * (s + d * (1 + (k - 1) * (p - 1)))
    singular = p ** (3 * k - 3) if k <= 5 else p ** 12 * local_energy(p, k - 5)
    return regular + singular


def factor_odd_five_free(q):
    assert q >= 1 and q % 2 and q % 5
    factors = []
    t = q
    p = 3
    while p * p <= t:
        if t % p == 0:
            k = 0
            while t % p == 0:
                t //= p
                k += 1
            factors.append((p, k))
        p += 2
    if t > 1:
        factors.append((t, 1))
    return factors


def predicted_energy(q):
    return prod(local_energy(p, k) for p, k in factor_odd_five_free(q))


def direct_energy(q):
    fifths = [pow(x, 5, q) for x in range(q)]
    fibers = Counter()
    for x in range(q):
        for y in range(q):
            fibers[((x + y) % q, (fifths[x] + fifths[y]) % q)] += 1
    return sum(v * v for v in fibers.values())


def check_strata(p):
    chi = 1 if p % 4 == 1 else -1
    expect_s, expect_d = local_coefficients(p)
    c0 = c1 = c2 = c3 = 0
    for s in range(p):
        for a in range(p):
            for b in range(p):
                qzero = (a * a + b * b + 4 * s * s) % p == 0
                z = (s == 0) + (a == 0) + (b == 0) + qzero
                if z == 0:
                    c0 += 1
                elif z == 1:
                    c1 += 1
                elif z == 2:
                    c2 += 1
                else:
                    assert s == 0 and a == 0 and b == 0
                    c3 += 1
    assert c1 == expect_s, (p, c1, expect_s)
    assert c2 == expect_d, (p, c2, expect_d)
    assert c3 == 1 and c0 + c1 + c2 + c3 == p ** 3
    assert c1 + c2 + 1 == 4 * p * p - 3 * p - 3 * (1 + chi) * (p - 1)


def main():
    primes = (3, 7, 11, 13, 17, 19, 23)
    for p in primes:
        check_strata(p)
    local_cases = [(3, k) for k in range(1, 7)] + [(7, k) for k in range(1, 4)] + [(11, k) for k in (1, 2)] + [(13, k) for k in (1, 2)] + [(17, k) for k in (1, 2)] + [(19, 1), (23, 1)]
    for p, k in local_cases:
        q = p ** k
        got, predicted = direct_energy(q), local_energy(p, k)
        assert got == predicted, (p, k, got, predicted)
    composites = (21, 33, 39, 63, 77, 91, 99, 143, 231)
    for q in composites:
        got, predicted = direct_energy(q), predicted_energy(q)
        assert got == predicted, (q, got, predicted)
    assert local_energy(7, 2) == 14161
    assert local_energy(3, 6) == 19427121
    print('VERIFY_OK', 'strata_primes=' + str(len(primes)),
          'local_cases=' + str(len(local_cases)),
          'composite_cases=' + str(len(composites)),
          'max_local_modulus=729', 'crossed_singular_k6=PASS')


if __name__ == '__main__':
    main()
