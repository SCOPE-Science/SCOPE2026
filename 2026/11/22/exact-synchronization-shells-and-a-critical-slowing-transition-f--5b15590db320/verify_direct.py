#!/usr/bin/env python3
"""Finite exhaustive checker for synchronous incoming NOR on directed de Bruijn graphs."""
from collections import Counter
from itertools import product
from math import comb


def experiment(q, d):
    assert q >= 2 and d >= 1
    words = list(product(range(q), repeat=d))
    word_id = {w: i for i, w in enumerate(words)}
    upstream = []
    for w in words:
        upstream.append(tuple(word_id[(a,) + w[:-1]] for a in range(q)))
    N = len(words)
    size = 1 << N
    assert N <= 16
    hist = [0] * (d + 1)
    ones_at_d = 0
    for x in range(size):
        y = x
        first = None
        for t in range(d + 1):
            if y == 0 or y == size - 1:
                if first is None:
                    first = t
            if t == d:
                break
            z = 0
            for j, nbrs in enumerate(upstream):
                if all((y >> k & 1) == 0 for k in nbrs):
                    z |= 1 << j
            y = z
        assert first is not None
        assert y in (0, size - 1)
        hist[first] += 1
        ones_at_d += (y == size - 1)
    # Compare with independent finite combinatorial count:
    a, b = 1, 1
    cum = []
    for t in range(d + 1):
        m = q ** (d - t)
        cum.append(a**m + b**m)
        if t < d:
            a, b = b**q, 2**(q**(t + 1)) - b**q
    theory = [cum[0]] + [cum[t] - cum[t-1] for t in range(1, d+1)]
    assert hist == theory, (q, d, hist, theory)
    assert sum(hist) == 2**N
    assert ones_at_d == a
    assert hist[-1] > 0
    print(f'q={q} d={d} vertices={N} shell_counts={hist} target_phase_one={ones_at_d}')


def main():
    for q,d in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1),(4,2)]:
        experiment(q,d)
    print('direct_exhaustive: PASS')

if __name__ == '__main__': main()
