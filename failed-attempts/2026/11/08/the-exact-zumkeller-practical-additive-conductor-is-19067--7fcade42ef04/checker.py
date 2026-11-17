#!/usr/bin/env python3
"""Exact finite certificate for the Zumkeller-plus-practical additive conductor.
All operations are integer arithmetic. Execute: python3 checker.py
"""
from math import gcd, isqrt

LIMIT = 716683
MODULUS = 198450


def smallest_prime_factors(n):
    spf = list(range(n + 1))
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for x in range(p * p, n + 1, p):
                if spf[x] == x:
                    spf[x] = p
    return spf


def factorization(n, spf):
    result = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        result.append((p, e))
    return result


def prime_power_divisor_sum(p, e):
    return (p ** (e + 1) - 1) // (p - 1)


def practical(n, spf):
    if n == 1:
        return True
    if n % 2:
        return False
    previous_sigma = 1
    for p, e in factorization(n, spf):
        if p > previous_sigma + 1:
            return False
        previous_sigma *= prime_power_divisor_sum(p, e)
    return True


def sigma(n, spf):
    ans = 1
    for p, e in factorization(n, spf):
        ans *= prime_power_divisor_sum(p, e)
    return ans


def proper_divisors(n, spf):
    ans = [1]
    for p, e in factorization(n, spf):
        old = ans[:]
        v = 1
        for _ in range(e):
            v *= p
            ans.extend([a * v for a in old])
    ans.remove(n)
    return ans


def zumkeller(n, spf):
    S = sigma(n, spf)
    if S % 2 or S < 2 * n:
        return False
    target = S // 2 - n
    # The largest divisor n is on one side; the other contributing divisors
    # must be distinct and proper. A subset sum of target suffices.
    subset_sums = 1
    for d in proper_divisors(n, spf):
        if d <= target:
            subset_sums |= subset_sums << d
            if (subset_sums >> target) & 1:
                return True
    return target == 0


def practical_by_divisor_intervals(n, spf):
    """Direct divisor-completeness criterion, independent of prime factor tests."""
    ds = sorted(proper_divisors(n, spf) + [n])
    reach = 0
    for d in ds:
        if d > reach + 1:
            return False
        reach += d
    return True


def check():
    spf = smallest_prime_factors(LIMIT)
    even_practicals = [n for n in range(2, LIMIT + 1, 2) if practical(n, spf)]
    # Full-range independent reclassification; neither positive nor negative
    # conclusions rest on only the prime-factor test.
    for q in range(2, LIMIT + 1, 2):
        assert practical(q, spf) == practical_by_divisor_intervals(q, spf), q
    practical_bitset = sum(1 << n for n in even_practicals)

    # Periodic cover: 945u (u odd, gcd(u,105)=1), plus a practical q.
    # At each odd residue modulo 198450 choose the first q reached and its u.
    us = [u for u in range(1, 210, 2) if gcd(u, 105) == 1]
    assert len(us) == 48
    first_base = [0] * MODULUS
    full_at_q = None
    visited = 0
    for q in even_practicals:
        if q > 539968:
            break
        for u in us:
            r = (q + 945 * u) % MODULUS
            if not first_base[r]:
                first_base[r] = q + 945 * u
                visited += 1
        if visited == MODULUS // 2:
            full_at_q = q
            break
    assert visited == 99225
    assert first_base[0] == 0
    assert all(first_base[r] for r in range(1, MODULUS, 2))
    assert full_at_q == 539968
    assert max(first_base) == LIMIT

    # Finite bridge: direct proof of odd Zumkeller status via divisor subsets.
    # Only Z <= 100000 is required in the finite interval.
    odd_z = [z for z in range(3, 100001, 2) if zumkeller(z, spf)]
    assert odd_z and odd_z[0] == 945
    represented = 0
    for z in odd_z:
        represented |= practical_bitset << z
    missing = [n for n in range(19069, LIMIT, 2)
               if not ((represented >> n) & 1)]
    assert missing == [20177], missing[:10]

    # A single even Zumkeller representation covers the bridge gap.
    special_z = 20176
    special_terms = [8, 13, 26, 52, 97, 104, 194, 208, 388]
    assert all(special_z % d == 0 for d in special_terms)
    assert len(special_terms) == len(set(special_terms))
    assert sum(special_terms) == sigma(special_z, spf) // 2 - special_z
    assert special_z + 1 == 20177

    # Sharpness: with q=1, z=19066 is not abundant.
    assert sigma(19066, spf) == 28602 < 2 * 19066
    # Every practical q>1 is even. In the remaining possible splits
    # n=19067=q+z, z is odd and must have even sigma and sigma >= 2z.
    viable = [(q, 19067-q) for q in even_practicals if q < 19067
              and sigma(19067 - q, spf) % 2 == 0
              and sigma(19067 - q, spf) >= 2 * (19067 - q)]
    assert viable == [], viable

    print("CERTIFIED_CONDUCTOR 19067")
    print(f"PRACTICAL_CHECK even_cases={LIMIT//2} practical_count={len(even_practicals)} independent_divisor_criterion=yes")
    print("PERIODIC_COVER modulus=198450 odd_residues=99225 u_count=48")
    print(f"PERIODIC_LIMIT last_practical={full_at_q} maximum_first_base={max(first_base)}")
    print(f"FINITE_BRIDGE odd_z_at_most_100000={len(odd_z)} uncovered=[20177]")
    print("SPECIAL 20177=20176+1 divisor_subset_sum=1090")
    print("SHARPNESS 19067=no_Zumkeller_plus_practical")


if __name__ == '__main__':
    check()
