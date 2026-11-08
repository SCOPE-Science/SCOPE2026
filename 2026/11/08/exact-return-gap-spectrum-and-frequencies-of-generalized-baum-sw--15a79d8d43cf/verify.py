#!/usr/bin/env python3
"""Finite diagnostics for a return-gap theorem on generalized Baum–Sweet words."""
from collections import Counter


def accepted(n, r):
    if n == 0:
        return True
    bits = bin(n)[2:]
    return all(len(run) % r == 0 for run in bits.split('1') if run)


def formula_gap(n, r):
    if n == 0:
        return 1
    bits = bin(n)[2:]
    if '0' not in bits:
        return 1 << (len(bits) % r)
    t = len(bits) - len(bits.rstrip('1'))
    return ((1 << (r - 1)) - 1) * (1 << t) + (1 << ((r - 1 + t) % r))


def tilings(m, r, memo):
    if m < 0:
        return 0
    if m == 0:
        return 1
    if m not in memo:
        memo[m] = tilings(m - 1, r, memo) + tilings(m - r, r, memo)
    return memo[m]


def run():
    gap_checks = 0
    shell_checks = 0
    for r in range(2, 9):
        bound = 1 << 15
        positions = [n for n in range(bound) if accepted(n, r)]
        for a, b in zip(positions, positions[1:]):
            assert b - a == formula_gap(a, r), (r, a, b)
            gap_checks += 1
        for bits in range(1, 16):
            lo, hi = 1 << (bits - 1), 1 << bits
            entries = [n for n in range(lo, hi) if accepted(n, r)]
            memo = {}
            assert len(entries) == tilings(bits - 1, r, memo)
            assert sum('0' not in bin(n)[2:] for n in entries) == 1
            observed = Counter()
            for n in entries:
                s = bin(n)[2:]
                if '0' in s:
                    t = len(s) - len(s.rstrip('1'))
                    observed[t] += 1
            expected = Counter({t: tilings(bits - r - t - 1, r, memo)
                                for t in range(bits)})
            assert all(observed[t] == expected[t] for t in range(bits)), (r, bits, observed, expected)
            assert sum(observed.values()) + 1 == len(entries)
            shell_checks += 1
        assert ((1 << (r - 1)) - 1) + (1 << ((r - 1) % r)) == (1 << r) - 1
        assert ((1 << (r - 1)) - 1) * 2 + 1 == (1 << r) - 1
    print(f'VERIFY_OK orders=2..8 gap_checks={gap_checks} shell_checks={shell_checks}')


if __name__ == '__main__':
    run()
