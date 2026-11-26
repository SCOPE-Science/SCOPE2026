#!/usr/bin/env python3
"""Exact bitset certificate for the factorial divisor-sum cardinality threshold.

All tests use Python arbitrary-precision integers; no probabilistic tests.
Run beside EXTREMAL_TARGETS.json.
"""
import json
import math
from pathlib import Path


def genuine_divisors(n):
    """Enumerate divisors using direct factorization and full checks."""
    original = n
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                exponent += 1
                n //= p
            factors.append((p, exponent))
        p += 1 if p == 2 else 2
    if n > 1:
        factors.append((n, 1))
    divisors = [1]
    for prime, exponent in factors:
        previous = divisors[:]
        power = 1
        for _ in range(exponent):
            power *= prime
            divisors.extend(d * power for d in previous)
    divisors.sort()
    assert len(divisors) == len(set(divisors))
    assert divisors[0] == 1 and divisors[-1] == original
    assert all(original % d == 0 for d in divisors)
    expected = math.prod(exponent + 1 for _, exponent in factors)
    assert len(divisors) == expected
    return divisors


def verify(n, expected_h, expected_count=None, target_file=None):
    N = math.factorial(n)
    ds = genuine_divisors(N)
    cap = 1 << (N + 1)
    mask = cap - 1
    reachable = [1] + [0] * expected_h
    for d in ds:
        for k in range(expected_h, 0, -1):
            reachable[k] |= (reachable[k - 1] << d) & mask
    all_reachable = 0
    previous_missing = None
    for k in range(expected_h + 1):
        all_reachable |= reachable[k]
        missing = (N + 1) - all_reachable.bit_count()
        if k == expected_h - 1:
            previous_missing = missing
        if k == expected_h:
            assert missing == 0, (n, k, missing)
    assert previous_missing is not None and previous_missing > 0, (n, previous_missing)
    if expected_count is not None:
        assert previous_missing == expected_count, (n, previous_missing)
    if target_file:
        before = 0
        for k in range(expected_h):
            before |= reachable[k]
        missing_bits = mask ^ before
        missing_bits &= mask ^ 1
        targets=[]
        while missing_bits:
            low = missing_bits & -missing_bits
            targets.append(low.bit_length()-1)
            missing_bits -= low
        doc = json.loads(Path(target_file).read_text(encoding='utf-8'))
        assert doc['n']==n and doc['N']==N and doc['count']==len(targets)==expected_count
        assert targets == doc['targets']
        assert all(t % 2 == 1 for t in targets)
        assert targets[0] == 475785157 and targets[-1] == 479001547
        print('TARGETS_12_OK count=175 all_odd=YES min=475785157 max=479001547')
    print(f'FACTORIAL_OK n={n} N={N} divisors={len(ds)} h={expected_h} misses_at_h_minus_1={previous_missing}')


def main():
    values = [1,1,2,3,4,5,5,6,7,7,7,8]
    for n in range(1,13):
        verify(n, values[n-1], 175 if n==12 else None,
               str(Path(__file__).with_name('EXTREMAL_TARGETS.json')) if n==12 else None)
    print('VERIFY_OK first_eight_threshold=12 exact_full_range=PASS targets=175 finite_only=YES')

if __name__ == '__main__':
    main()
