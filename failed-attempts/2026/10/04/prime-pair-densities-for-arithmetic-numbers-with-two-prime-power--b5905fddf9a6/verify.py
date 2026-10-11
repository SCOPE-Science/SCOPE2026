#!/usr/bin/env python3
from math import gcd


def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * (((n - p*p) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def order_mod_prime(a, prime):
    a %= prime
    if a == 0:
        return None
    x = 1
    for k in range(1, prime):
        x = (x * a) % prime
        if x == 1:
            return k
    raise AssertionError('order not found')


def arithmetic_direct(ell, m, P, Q):
    sigma1 = (P ** ell - 1) // (P - 1)
    sigma2 = (Q ** m - 1) // (Q - 1)
    return (sigma1 * sigma2) % (ell * m) == 0


def structural_criterion(ell, m, P, Q):
    return ((P - 1) % ell == 0 and
            (((Q - 1) % m == 0) or order_mod_prime(P, m) == ell))


def residue_count_check(ell, m):
    count = 0
    for a in range(1, ell * m + 1):
        if gcd(a, ell * m) != 1:
            continue
        if a % ell == 1 % ell and order_mod_prime(a, m) == ell:
            count += 1
    expected = ell - 1 if (m - 1) % ell == 0 else 0
    assert count == expected, (ell, m, count, expected)


def main():
    exponent_pairs = [(2, 3), (2, 5), (3, 5), (3, 7), (3, 13), (5, 7), (5, 11), (5, 31)]
    ps = primes_upto(500)
    pair_checks = 0
    for ell, m in exponent_pairs:
        residue_count_check(ell, m)
        for P in ps:
            for Q in ps:
                if P == Q or P in (ell, m) or Q in (ell, m):
                    continue
                pair_checks += 1
                direct = arithmetic_direct(ell, m, P, Q)
                predicted = structural_criterion(ell, m, P, Q)
                assert direct == predicted, (ell, m, P, Q, direct, predicted)
    print(f'VERIFY_OK pair_checks={pair_checks} exponent_pairs={len(exponent_pairs)} prime_bound=500')


if __name__ == '__main__':
    main()
