#!/usr/bin/env python3
"""Exact all-size finite quotient and extinction-shell coefficients for GH4 on windmills.
Run: python3 finite_certificate.py
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement

TYPES = list(combinations_with_replacement(range(4), 2))
INDEX = {pair: i for i, pair in enumerate(TYPES)}
M = len(TYPES)
WEIGHTS = [1 if a == b else 2 for a,b in TYPES]
EXCITED = sum(1 << i for i,(a,b) in enumerate(TYPES) if a == 1 or b == 1)
LOCAL = []
for hub in range(4):
    images = []
    for a, b in TYPES:
        na = ((hub == 1 or b == 1) if a == 0 else (a + 1) % 4)
        nb = ((hub == 1 or a == 1) if b == 0 else (b + 1) % 4)
        images.append(1 << INDEX[tuple(sorted((int(na), int(nb))))])
    LOCAL.append(images)


def step(hub, support):
    newhub = (hub + 1) % 4 if hub else int(bool(support & EXCITED))
    new_support = 0
    while support:
        bit = support & -support
        i = bit.bit_length() - 1
        new_support |= LOCAL[hub][i]
        support -= bit
    return newhub, new_support


def extinction_time(hub, support):
    assert support
    for t in range(8):
        if hub == 0 and support == 1: return t
        hub, support = step(hub, support)
    raise AssertionError("Extinction not reached within seven updates")


def main():
    shell_cases = Counter()
    c = defaultdict(Counter)
    wsum = [0]*(1 << M)
    for s in range(1, 1 << M):
        bit = s & -s
        i = bit.bit_length() - 1
        wsum[s] = wsum[s - bit] + WEIGHTS[i]
    A = 1 << INDEX[(0,1)]
    B = (1 << INDEX[(1,2)]) | (1 << INDEX[(1,3)])
    for hub in range(4):
        for support in range(1, 1 << M):
            t = extinction_time(hub, support)
            shell_cases[(hub,t)] += 1
            assert (t == 7) == (hub == 3 and bool(support & A) and bool(support & B))
            sub = support
            while True:
                c[t][wsum[sub]] += (-1)**((support^sub).bit_count())
                if not sub: break
                sub = (sub - 1) & support
    expected = [
        {1:1},
        {4:2,1:-1},
        {9:3,4:-2},
        {14:2,9:-1},
        {16:1,9:-1,6:1,1:-1},
        {16:1,14:-1,12:1,6:-1,5:-1,3:1},
        {16:1,10:-1,9:-1,5:1,3:-1,1:1},
        {16:1,14:-1,12:-1,10:1},
    ]
    for t in range(8):
        got = {base:count for base,count in c[t].items() if count and base > 0}
        assert got == expected[t], (t,got)
    assert sum(shell_cases.values()) == 4*((1 << M)-1)
    print('unordered_types:', M)
    print('all_support_cases:', sum(shell_cases.values()))
    print('cases_by_hub_and_time:', sorted(shell_cases.items()))
    print('seven_step_criterion: hub=3 and type 01 and (12 or 13)')
    for k in range(1,7):
        counts = [sum(v*(b**k) for b,v in c[t].items()) for t in range(8)]
        assert sum(counts) == 4**(2*k+1)
        assert counts[7] == 16**k-14**k-12**k+10**k
        print('k', k, 'shells', counts)
    print('finite_certificate: PASS')

if __name__ == '__main__': main()
