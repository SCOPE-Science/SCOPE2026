#!/usr/bin/env python3
"""Exact independent checks of sharp-peak Walsh sums of Motzkin paths."""
from collections import Counter
from functools import lru_cache


def profile_counts(n):
    counts = Counter()
    def walk(i, h, was_up, mask):
        if i == n:
            if h == 0:
                counts[mask] += 1
            return
        walk(i + 1, h, False, mask)
        walk(i + 1, h + 1, True, mask)
        if h:
            new_mask = mask | ((1 << (i - 1)) if was_up else 0)
            walk(i + 1, h - 1, False, new_mask)
    walk(0, 0, False, 0)
    return counts


def hadamard(values):
    a = list(values)
    stride = 1
    while stride < len(a):
        for block in range(0, len(a), 2 * stride):
            for j in range(block, block + stride):
                a[j], a[j + stride] = a[j] + a[j + stride], a[j] - a[j + stride]
        stride *= 2
    return a


def motif_sum(n, selected, motzkin):
    """Independent inclusion-exclusion on disjoint forced two-step peaks."""
    @lru_cache(None)
    def rec(i, forbidden_next, k):
        if i >= n-1:
            return (-2)**k * motzkin[n-2*k]
        a = rec(i+1, False, k)
        if not forbidden_next and (selected >> i) & 1:
            a += rec(i+1, True, k+1)
        return a
    return rec(0, False, 0)


def direct_signed_dp(n, selected):
    """Independent stepwise height and previous-up dynamic program."""
    states = {(0, False): 1}
    for i in range(n):
        next_states = {}
        def add(k, v):
            next_states[k] = next_states.get(k, 0) + v
        for (height, up), total in states.items():
            add((height, False), total)
            add((height+1, True), total)
            if height:
                factor = -1 if (up and (selected >> (i-1)) & 1) else 1
                add((height-1, False), factor*total)
        states = next_states
    return sum(w for (h, _), w in states.items() if h == 0)


def verify():
    motzkin = [sum(profile_counts(n).values()) for n in range(15)]
    total_checked = 0
    for n in range(2, 13):
        c = profile_counts(n)
        m = 1 << (n-1)
        spectrum = hadamard(c.get(s, 0) for s in range(m))
        assert spectrum[0] == motzkin[n] == sum(c.values())
        minimum = spectrum[m-1]
        for s in range(m):
            assert spectrum[s] == motif_sum(n, s, motzkin)
            assert spectrum[s] == direct_signed_dp(n, s)
            assert minimum <= spectrum[s] <= motzkin[n]
            if n >= 4:
                assert spectrum[s] >= 1
            total_checked += 1
    assert [hadamard(profile_counts(n).get(s, 0) for s in range(1 << (n-1)))[-1] for n in range(2, 11)] == [0, 0, 1, 1, 1, 3, 5, 7, 14]
    assert [sum(x == 0 for x in hadamard(profile_counts(n).get(s, 0) for s in range(1 << (n-1)))) for n in range(2, 7)] == [1, 1, 0, 0, 0]
    print('PASS: three exact independent methods, orders 2..12,', total_checked, 'Walsh characters')

if __name__ == '__main__':
    verify()
