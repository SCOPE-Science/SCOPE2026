#!/usr/bin/env python3
"""Independent finite corroboration of cyclic ternary-morphism complexity identities."""
from itertools import product

def block(letter, r, m):
    w = str(letter)
    for _ in range(m):
        w = ''.join(ch * r + str((int(ch) + 1) % 3) for ch in w)
    return w

def direct_extremes(r, m):
    n = (r + 1) ** m
    parts = [block(a, r, m) for a in range(3)]
    lo, hi = n, 0
    # Each ordered adjacent letter pair occurs in the infinite ternary fixed point.
    for a, b in product(range(3), repeat=2):
        w = parts[a] + parts[b]
        zeros = [int(c == '0') for c in w]
        count = sum(zeros[:n])
        lo = min(lo, count)
        hi = max(hi, count)
        for i in range(n, 2*n):
            count += zeros[i] - zeros[i - n]
            lo = min(lo, count)
            hi = max(hi, count)
    return hi, lo

def recurrence_profile(r, depth):
    N = [1, 0, 0]
    A = 2
    for m in range(depth + 1):
        yield m, tuple(N), A
        A += r * (max(N) - min(N))
        N = [r * N[a] + N[(a - 1) % 3] for a in range(3)]

cases = 0
for r in (3, 5, 7, 9, 11):
    for m, N, A in recurrence_profile(r, 3):
        hi, lo = direct_extremes(r, m)
        assert hi - lo + 1 == A, (r, m, N, A, hi, lo)
        cases += 1
print('full factor-language cases:', cases)

parity_checks = 0
for r in (3, 5, 7, 9, 11, 13, 15):
    for m, N, A in recurrence_profile(r, 300):
        if m > 0 and m % 3 == 0:
            g = max(N) - min(N)
            crossing = (N[0] - N[1]) * (N[0] - N[2])
            assert crossing != 0
            assert (g % 2 == 0) == (crossing < 0)
            parity_checks += 1
print('exact integer parity/sign checks:', parity_checks)

# A separate finite stress test of the weighted extremal recursion.
weighted_cases = 0
for r in (3, 5):
    for m in range(3):
        n = (r + 1)**m
        parts = [block(a, r, m+1) for a in range(3)]
        parts_m = [block(a, r, m) for a in range(3)]
        for wt in product(range(-1, 2), repeat=3):
            def maxfactor(parts, size):
                best = -10**99
                for a, b in product(range(3), repeat=2):
                    vals = [wt[int(c)] for c in parts[a] + parts[b]]
                    total = sum(vals[:size]); best = max(best, total)
                    for i in range(size, len(vals)):
                        total += vals[i] - vals[i-size]
                        best = max(best, total)
                return best
            h = maxfactor(parts_m, n)
            hn = maxfactor(parts, (r+1)*n)
            mx = max(sum(wt[int(c)] for c in s) for s in parts_m)
            assert hn == h + r*mx, (r, m, wt, hn, h, mx)
            weighted_cases += 1
print('weighted-recursion tests:', weighted_cases)
print('ALL FINITE CHECKS PASS. Infinite non-regularity follows from the written proof.')
