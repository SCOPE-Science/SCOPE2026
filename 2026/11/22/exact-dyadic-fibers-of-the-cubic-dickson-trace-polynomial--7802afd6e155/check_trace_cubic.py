#!/usr/bin/env python3
"""Exact modular fiber counts for the cubic Dickson trace polynomial.

Independent brute-force recurrence checks, no use of network or external files.
"""
from collections import Counter


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def odd_branch(k, z, positive_input):
    """Number of solutions in x=+1+4Z (if positive_input), else -1+4Z."""
    modulus = 1 << k
    z %= modulus
    if z == 0:
        return 1 << (k // 2)
    valuation = v2(z)
    if valuation < 4 or valuation & 1:
        return 0
    r = valuation // 2
    precision = k - 2*r
    if positive_input:
        local_unit = 7 if r == 2 else 3
    else:
        local_unit = 1 if r == 2 else 5
    local_mask = (1 << min(3, precision)) - 1
    if ((z >> (2*r)) & local_mask) != (local_unit & local_mask):
        return 0
    return 1 << min(k-r-1, r+2)


def formula(k, target):
    assert k >= 4
    if target & 1:
        return 0
    return (1 + odd_branch(k, target+2, True)
              + odd_branch(k, target-2, False))


def count_check(k):
    modulus = 1 << k
    counts = [0] * modulus
    for x in range(modulus):
        counts[(x*x*x-3*x) % modulus] += 1
    for y, actual in enumerate(counts):
        expected = formula(k, y)
        if actual != expected:
            raise AssertionError((k,y,actual,expected))
    assert sum(counts) == modulus
    assert sum(c>0 for c in counts)==modulus//2
    return Counter(counts)


def check_disjoint_and_shapes():
    for k in range(4,18):
        n=1 << k
        for x in range(n):
            y=(x*x*x-3*x)%n
            if x%4==1:
                assert y%16==14
            if x%4==3:
                assert y%16==2
            if x%2==0:
                assert y%2==0
        c=count_check(k)
        print(f'k={k}, target histogram={dict(sorted(c.items()))}')
    print('ALL BRUTE-FORCE FIBER COUNTS AND LOCAL BRANCH TESTS PASS, k=4..17')


if __name__=='__main__':
    check_disjoint_and_shapes()
