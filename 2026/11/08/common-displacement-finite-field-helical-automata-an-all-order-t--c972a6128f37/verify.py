#!/usr/bin/env python3
"""Exact finite checks for common-displacement helical finite-field maps.

Only the additive group of the field is used, represented as bitwise XOR.
The general assertions in RESULT.md are established algebraically, not by
this finite verification.
"""
from itertools import product


def pairs(q, d):
    return [(x, x ^ d) for x in range(q) if x < (x ^ d)]


def support(q, d, mask):
    return frozenset(z for j, pair in enumerate(pairs(q, d))
                     if (mask >> j) & 1 for z in pair)


def check_equation(q, d, S):
    def f(x):
        return x ^ (d if x in S else 0)
    assert len({f(x) for x in range(q)}) == q
    for x in range(q):
        for y in range(q):
            assert (f(x) ^ f(x ^ f(y))) == f(x ^ f(y ^ f(x)))
    return q*q


def update(z, d, S):
    state = []
    b = z[-1]
    for x in z[:-1]:
        flip = d if (x ^ b) in S else 0
        state.append(x ^ flip)
        b ^= flip
    return tuple(state + [b])


def check_orbits(q, d, S, L):
    fixed = 0
    tested = 0
    for z in product(range(q), repeat=L+1):
        z1 = update(z, d, S)
        assert update(z1, d, S) == z
        fixed += (z1 == z)
        tested += 1
    assert fixed == q * (q-len(S))**L
    assert (tested-fixed) % 2 == 0
    return tested


def main():
    checks = 0
    for n in (2, 3, 4):
        q = 1 << n
        funcs = set()
        for d in range(1, q):
            for mask in range(1 << (q//2)):
                S = support(q, d, mask)
                checks += check_equation(q, d, S)
                funcs.add(tuple(x ^ (d if x in S else 0) for x in range(q)))
        assert len(funcs) == 1 + (q-1) * ((1 << (q//2))-1)
        print('equation_and_map_count', n, len(funcs))
    for n in (2, 3, 4):
        q = 1 << n
        ds = range(1, q) if n <= 3 else (1, 3, 7, 13)
        for d in ds:
            total = 1 << (q//2)
            masks = (range(total) if n <= 3 else
                     (0, 1, 3, 5, 7, 15, 31, 65, total-1))
            for mask in masks:
                S = support(q, d, mask)
                for L in ((1,2,3,4) if n == 2 else
                          ((1,2,3) if n == 3 else (1,2))):
                    checks += check_orbits(q, d, S, L)
    print('VERIFY_OK exact_state_checks=', checks)


if __name__ == '__main__':
    main()
