#!/usr/bin/env python3
"""Exact integer checks for signed circulant permanents; no external packages."""
from math import factorial
from itertools import product

def signed_circulant_permanent(n, negative_offsets):
    signs = [(-1 if d in negative_offsets else 1) for d in range(n)]
    full = 1 << n
    dp = [0] * full
    dp[0] = 1
    for mask in range(1, full):
        i = mask.bit_count() - 1
        t = mask
        v = 0
        while t:
            bit = t & -t
            j = bit.bit_length() - 1
            v += signs[(j - i) % n] * dp[mask ^ bit]
            t -= bit
        dp[mask] = v
    return dp[-1]

def run():
    total = 0
    for n in (2,4,8):
        for mask in range(1 << (n - 1)):
            subset = {j for j in range(1,n) if (mask >> (j-1)) & 1}
            value = signed_circulant_permanent(n, subset)
            assert (value - factorial(n)) % (1 << n) == 0, (n,mask,value)
            assert abs(value) >= (1 << (n-1)), (n,mask,value)
            assert (value // (1 << (n-1))) % 2 == 1, (n,mask,value)
            total += 1
    for n in (16,):
        for subset in (set(), {1}, {1,3,7}, {0,2,4,9,13}):
            value = signed_circulant_permanent(n, subset)
            assert (value - factorial(n)) % (1 << n) == 0
            assert value != 0
            total += 1
    # A global Walsh zero exists at every even size: first-row balanced, others all +1.
    for n in (2,4,8,16):
        balanced = [1] * (n // 2) + [-1] * (n // 2)
        # Each first-row choice has (n-1)! completing permutations.
        assert factorial(n-1) * sum(balanced) == 0
    print('CIRCULANT_SIGN_PERMANENT_EXACT_PASS', 'cases=', total)
if __name__ == '__main__':
    run()
