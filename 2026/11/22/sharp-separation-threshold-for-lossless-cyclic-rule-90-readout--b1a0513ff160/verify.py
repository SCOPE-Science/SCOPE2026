#!/usr/bin/env python3
"""Exact finite checks for one-step XOR readout of cyclic separated words.

Run: python3 verify.py. Uses only the Python standard library.
"""
from collections import Counter, defaultdict
from math import comb


def allowed(mask, n, r):
    """Every two marked sites must have at least r intervening zeros."""
    for i in range(n):
        if (mask >> i) & 1:
            for d in range(1, r + 1):
                if (mask >> ((i + d) % n)) & 1:
                    return False
    return True


def readout(mask, n):
    return sum(((((mask >> ((i - 1) % n)) & 1)
                 ^ ((mask >> ((i + 1) % n)) & 1)) << i)
               for i in range(n))


def predicted(n, r):
    assert n >= 2 * r + 3 and r >= 1
    s = 1 + sum(n * comb(n - r * k - 1, k - 1) // k
                for k in range(1, n // (r + 1) + 1))
    if n % 2 or r >= 4 or (r in (2, 3) and n % 4 != 0):
        return s, {1: s}
    if r in (2, 3):
        return s - 2, {1: s - 4, 2: 2}
    m = n // 2
    return s - 2 ** m, {1: s - 2 ** (m + 1) + 1,
                        2: 2 ** m - 2, 3: 1}


def brute(n, r):
    fibers = defaultdict(int)
    for mask in range(1 << n):
        if allowed(mask, n, r):
            fibers[readout(mask, n)] += 1
    return len(fibers), dict(Counter(fibers.values()))


def main():
    checked = 0
    # Exhaustive source and output enumerations, all indexed words, not necklaces.
    for r in range(1, 7):
        for n in range(2 * r + 3, min(20, 2 * r + 13) + 1):
            assert brute(n, r) == predicted(n, r), (n, r)
            checked += 1
    # Verify the sharp double-fiber output witnesses against the direct definition.
    for r, n in ((2, 8), (3, 12), (2, 12), (3, 16)):
        fibers = defaultdict(list)
        for x in range(1 << n):
            if allowed(x, n, r):
                fibers[readout(x, n)].append(x)
        doubles = {y for y, xs in fibers.items() if len(xs) == 2}
        phases = {sum(((i % 2) == parity) << i for i in range(n))
                  for parity in (0, 1)}
        assert doubles == phases, (n, r, doubles, phases)
    print(f'VERIFY_OK parameter_pairs={checked} r=1..6 n<=20 direct_fiber_enumeration=complete')


if __name__ == '__main__':
    main()
