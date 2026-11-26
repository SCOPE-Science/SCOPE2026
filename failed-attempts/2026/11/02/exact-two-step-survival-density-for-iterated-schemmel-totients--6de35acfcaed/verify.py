#!/usr/bin/env python3
"""Exact finite cross-checks for an arithmetic-density theorem.

This is supplementary testing; infinitude and the asymptotic estimate
follow from the mathematical proof, not from finite computation.
"""
from functools import lru_cache

LIMIT = 40000

def spf_sieve(n):
    spf = list(range(n + 1))
    for p in range(2, int(n**0.5) + 1):
        if spf[p] == p:
            for k in range(p * p, n + 1, p):
                if spf[k] == k:
                    spf[k] = p
    return spf

SPF = spf_sieve(LIMIT)

def is_prime(p):
    return p > 1 and SPF[p] == p

def factors(n):
    while n > 1:
        p = SPF[n]
        exponent = 0
        while n % p == 0:
            exponent += 1
            n //= p
        yield p, exponent

def L(m, n):
    if n < 2:
        return n
    result = 1
    for p, a in factors(n):
        if p <= m:
            return 0
        result *= p**(a - 1) * (p - m)
    return result

def D(m, n):
    if n == 1:
        return 0
    total = 0
    while n > 1:
        n = L(m, n)
        total += n
    return total

def run():
    tests = 0
    direct_witnesses = 0
    depth_two_positive = 0
    exceptional = {}
    for m in (4, 6, 8, 10, 12, 16):
        q = next(p for p in range(m // 2 + 1, m) if is_prime(p))
        exceptional[m] = 0
        all_small_primes = [p for p in range(2, m + 1) if is_prime(p)]
        qmod = 1
        for p0 in all_small_primes:
            qmod *= p0
        residue_count = sum(1 for a in range(qmod) if all(a % p0 != 0 and (a-m) % p0 != 0 for p0 in all_small_primes))
        expected_residue_count = 1
        for p0 in all_small_primes:
            expected_residue_count *= p0 - (1 if m % p0 == 0 else 2)
        assert residue_count == expected_residue_count
        for n in range(1, LIMIT + 1):
            p_witness = any(p > m and p % q == m % q for p, _ in factors(n))
            first = L(m, n)
            allowed = all(p > m and all((p - m) % ell != 0 for ell in all_small_primes) for p, _ in factors(n))
            actually_survives = L(m, first) > 0
            assert allowed == actually_survives, (m, n, allowed, actually_survives)
            if actually_survives:
                depth_two_positive += 1
            if p_witness:
                direct_witnesses += 1
                assert L(m, first) == 0, (m, q, n, first)
                assert D(m, n) < n, (m, n)
            if D(m, n) >= n:
                exceptional[m] += 1
                assert not p_witness, (m, n)
            tests += 1
    print('VERIFY_OK tested_pairs=%d forbidden_factor_checks=%d' % (tests, direct_witnesses))
    print('EXCEPTIONAL_COUNTS_N_40000 ' + str(exceptional))
    print('DEPTH_TWO_POSITIVE_TESTS %d' % depth_two_positive)
    print('CRT_RESIDUES_CHECKED_FOR m=4,6,8,10,12,16')

if __name__ == '__main__':
    run()
