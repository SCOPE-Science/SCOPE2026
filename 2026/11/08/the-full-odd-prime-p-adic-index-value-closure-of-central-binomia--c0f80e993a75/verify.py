#!/usr/bin/env python3
"""Independent finite checks for the odd-prime index–central-binomial closure theorem."""
from math import comb


def primes_upto(n):
    return [p for p in range(3, n + 1, 2) if all(p % d for d in range(3, int(p ** 0.5) + 1, 2))]


def carries_in_suffix(a, p, s):
    carry = count = 0
    for _ in range(s):
        digit = a % p
        carry = (2 * digit + carry) // p
        count += carry
        a //= p
    return count


def subgroup_order(generators, modulus):
    seen = {1}
    queue = [1]
    for x in queue:
        for g in generators:
            y = x * g % modulus
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return len(seen)


def modular_binomials(p, k, limit):
    m = p ** k
    val_unit = 1
    valuation = 0
    for n in range(limit + 1):
        yield n, (val_unit * pow(p, valuation, m)) % m if valuation < k else 0
        if n == limit:
            break
        numerator, denominator = 4*n+2, n+1
        while numerator % p == 0:
            numerator //= p
            valuation += 1
        while denominator % p == 0:
            denominator //= p
            valuation -= 1
        assert valuation >= 0
        val_unit = val_unit * numerator * pow(denominator, -1, m) % m


def check_progression(p, s, k, limit):
    m = p ** k
    stride = p ** s
    seen = [set() for _ in range(stride)]
    direct_cases = 0
    for n, value in modular_binomials(p, k, limit):
        seen[n % stride].add(value)
        if n < 35:
            assert value == comb(2*n, n) % m
            direct_cases += 1
    uncovered = []
    for a, actual in enumerate(seen):
        c = carries_in_suffix(a, p, s)
        expected = {x for x in range(m) if x % pow(p, min(c, k)) == 0}
        if actual != expected:
            uncovered.append((a, c, len(actual), len(expected)))
    assert not uncovered, (p,s,k,limit,uncovered[:8])
    return stride, direct_cases


def main():
    group_primes = primes_upto(47)
    for p in group_primes:
        m = p*p
        digit_values = [comb(2*d,d) % m for d in range(1,(p+1)//2)]
        assert subgroup_order(digit_values, m) == p*(p-1), p
        for d in range(1,(p+1)//2):
            assert comb(2*d*p, d*p) % m == comb(2*d,d) % m, (p,d)
    cases = [(3,1,2,35000),(3,2,2,45000),(3,1,3,100000),
             (5,1,2,60000),(5,2,2,100000),(7,1,2,650000)]
    groups_checked = direct = 0
    for p,s,k,limit in cases:
        count, verified = check_progression(p,s,k,limit)
        groups_checked += count
        direct += verified
    print('VERIFY_OK generator_prime_count={} constrained_progressions={} exact_small_n={} progression_cases={}'.format(
        len(group_primes), groups_checked,direct,len(cases)))

if __name__ == '__main__':
    main()
