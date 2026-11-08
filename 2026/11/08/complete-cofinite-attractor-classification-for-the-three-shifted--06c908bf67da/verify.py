#!/usr/bin/env python3
"""Finite regression checks for the shifted-totient three-attractor theorem.

The mathematical proof uses a uniform descent argument, not these experiments.
"""
from math import gcd

LIMIT = 100000
CAP = LIMIT + 16
phi = list(range(CAP + 1))
for p in range(2, CAP + 1):
    if phi[p] == p:
        for j in range(p, CAP + 1, p):
            phi[j] -= phi[j] // p
phi[1] = 1

def f(n):
    if not 1 <= n <= CAP:
        raise ValueError('outside independently sieved range')
    return phi[n] + 3

# A second, gcd-counting implementation is used for the complete small graph.
small = {n: sum(gcd(n, j) == 1 for j in range(1, n + 1)) + 3
         for n in range(3, 28, 2)}
expected_small = {3: 5, 5: 7, 7: 9, 9: 9, 11: 13, 13: 15,
                  15: 11, 17: 19, 19: 21, 21: 15,
                  23: 25, 25: 23, 27: 21}
assert small == expected_small
assert {n: f(n) for n in expected_small} == expected_small
assert f(1) == f(2) == 4 and f(4) == 5

# Uniform one-to-three-step strict descent for all tested large odd states.
counts = [0, 0, 0]
for n in range(29, LIMIT + 1, 2):
    v = n
    for step in (1, 2, 3):
        v = f(v)
        if v < n:
            counts[step - 1] += 1
            break
    else:
        raise AssertionError(('descent violation', n))
assert [f(29), f(f(29)), f(f(f(29)))] == [31, 33, 23]

# Every preimage table entry is exhaustively verified up to 2*30^2.
# Proof accompanying this checker establishes phi(n) >= sqrt(n/2), so
# a solution of phi(n)=m <= 30 cannot lie beyond 1800.
targets = {
    0: [], 1: [1, 2], 2: [3, 4, 6], 4: [5, 8, 10, 12],
    6: [7, 9, 14, 18], 20: [25, 33, 44, 50, 66],
    22: [23, 46], 26: [], 28: [29, 58], 30: [31, 62],
}
for m, expected in targets.items():
    assert [n for n in range(1, 1801) if phi[n] == m] == expected, m
exception_fixed = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 18}
exception_two = {23, 25, 29, 31, 33, 44, 46, 50, 58, 62, 66}
assert len(exception_fixed) == 13 and len(exception_two) == 11
assert not (exception_fixed & exception_two)

cycles = {(9,), (11, 13, 15), (23, 25)}
hits = {cyc: 0 for cyc in cycles}
max_steps_to_cycle = 0
for start in range(1, LIMIT + 1):
    at = start
    seen = {}
    path = []
    while at not in seen:
        seen[at] = len(path)
        path.append(at)
        at = f(at)
    cyc = path[seen[at]:]
    cyc = tuple(cyc[cyc.index(min(cyc)):] + cyc[:cyc.index(min(cyc))])
    assert cyc in cycles, (start, cyc)
    if cyc == (9,):
        assert start in exception_fixed
    elif cyc == (23, 25):
        assert start in exception_two
    else:
        assert start not in (exception_fixed | exception_two)
    hits[cyc] += 1
    max_steps_to_cycle = max(max_steps_to_cycle, seen[at])

print('small states: 13; transitions match independent gcd counts')
print('odd-state descent: tested every odd n from 29 to 99999')
print('strict descent at steps 1, 2, 3:', *counts)
print('sharp witness: 29 -> 31 -> 33 -> 23')
print('inverse totients: 10 exact finite lists checked over n<=1800')
print('exceptional basins: 13 fixed-point starts and 11 two-cycle starts')
print('start values: 1..100000; periodic orbits exactly:')
for c in sorted(cycles):
    print('  cycle', c, ':', hits[c], 'starting values')
print('largest preperiod in test:', max_steps_to_cycle)
print('PASS: finite regression; unrestricted result requires the symbolic proof')
