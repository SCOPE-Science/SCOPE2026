#!/usr/bin/env python3
"""Exact independent checks for prime-power Schemmel-totient iterate sums."""
from math import gcd, isqrt

def primes_through(m):
    sieve = bytearray(b'\x01') * (m + 1)
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(m) + 1):
        if sieve[d]:
            sieve[d * d:m + 1:d] = b'\x00' * ((m - d * d) // d + 1)
    return [i for i in range(2, m + 1) if sieve[i]]

def schemmel_two(n):
    if n == 0: return 0
    if n == 1: return 1
    x, ans = n, n
    for p in range(2, isqrt(x) + 1):
        if x % p == 0:
            if p == 2: return 0
            ans = ans // p * (p - 2)
            while x % p == 0:
                x //= p
    if x > 1:
        if x == 2: return 0
        ans = ans // x * (x - 2)
    return ans

def iterate_sum(n):
    if n == 1: return 0
    total, x, count = 0, n, 0
    while x > 1:
        x = schemmel_two(x)
        total += x
        count += 1
        assert count <= n
    return total

def from_definition(n):
    if n == 1: return 1
    return sum(gcd(j,n) == 1 and gcd(j+1,n) == 1 for j in range(1,n+1))

def main():
    for n in range(1, 501):
        assert from_definition(n) == schemmel_two(n), ('L2', n)
        if n > 1:
            y = n; sums = 0
            while y > 1:
                y = from_definition(y)
                sums += y
            assert sums == iterate_sum(n), ('D2', n)
    tested = 0
    min_surplus = None
    min_inputs = []
    for p in primes_through(10000):
        power = p
        for a in range(1, 16):
            if power > 10**7: break
            val = iterate_sum(power)
            if p == 2:
                assert val == 0
            elif p == 3:
                assert val == (power-1)//2
            elif p == 5:
                assert val == (3*power+1)//4
            else:
                gap = val-power
                assert gap >= 2
                if a >= 2:
                    assert gap >= (p-6) * p**(a-2) + 3
                if min_surplus is None or gap < min_surplus:
                    min_surplus, min_inputs = gap, [(p,a)]
                elif gap == min_surplus:
                    min_inputs.append((p,a))
            tested += 1
            power *= p
    assert min_surplus == 2 and min_inputs == [(7,1),(11,1),(17,1)], (min_surplus,min_inputs)
    assert [n for n in (5,9,15) if schemmel_two(n) == 3] == [5,9,15]
    assert [n for n in range(5, 100000,2) if schemmel_two(n)==3] == [5,9,15]
    print('VERIFY_OK')
    print('direct_definition_n=1..500')
    print('prime_power_cases=',tested)
    print('prime_bound=10000 power_bound=10000000')
    print('minimum_positive_surplus=',min_surplus,'at',min_inputs)
    print('fiber_L2_equals_3=',[5,9,15], 'searched_n<100000')
    print('exact_integer_arithmetic=True')

if __name__ == '__main__':main()
