#!/usr/bin/env python3
from math import comb, factorial


def proper_direct(n):
    no_off = 2 ** (n - 1)
    balanced = 0
    for ell in range(1, n // 2 + 1):
        balanced += factorial(n) // (factorial(ell) ** 2 * factorial(n - 2 * ell)) * 2 ** (n - 2 * ell)
    return no_off + balanced


def total_direct(n):
    no_off = 2 ** n
    balanced = 0
    for ell in range(1, n // 2 + 1):
        balanced += factorial(n) // (factorial(ell) ** 2 * factorial(n - 2 * ell)) * 2 ** (n - 2 * ell)
    one_more = 0
    # Count allocations with n_g = n_{g^{-1}} + 1. The outer factor 2
    # below accounts simultaneously for the second orientation and for the
    # two independent classes in a positive balanced allocation, as in the
    # source's codimension sum.
    for r in range(0, (n - 1) // 2 + 1):
        s = r + 1
        rem = n - r - s
        if rem < 0:
            continue
        one_more += factorial(n) // (factorial(r) * factorial(s) * factorial(rem)) * 2 ** rem
    return no_off + 2 * (balanced + one_more)


def total_closed(n):
    if n == 0:
        return 1
    return comb(2 * n + 2, n + 1) - 2 ** n


def proper_closed(n):
    return comb(2 * n, n) - 2 ** (n - 1)


for n in range(1, 41):
    pd = proper_direct(n)
    pc = proper_closed(n)
    td = total_direct(n)
    tc = total_closed(n)
    assert pd == pc, (n, pd, pc)
    assert td == tc, (n, td, tc)
    assert pc == total_closed(n - 1), (n, pc, total_closed(n - 1))

print('total:', [total_closed(n) for n in range(1, 11)])
print('proper:', [proper_closed(n) for n in range(1, 11)])
print('checked n=1..40')
print('CHECK_OK')
