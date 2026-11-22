#!/usr/bin/env python3
"""Finite cross-check of the sharp palindrome k-gram reconstruction threshold."""
from collections import Counter
from itertools import product


def profile(w, k):
    return tuple(sorted((s, int(c)) for r in range(1, k + 1)
                        for s, c in Counter(w[i:i+r] for i in range(len(w)-r+1)).items()))


def palindromes(q, n):
    h = (n + 1) // 2
    for a in product(range(q), repeat=h):
        yield a + (a[-2::-1] if n % 2 else a[::-1])


def witness(k):
    u = (0,)*k + (1,) + (0,)*(k-1) + (1,) + (0,)*k
    v = (0,)*(k-1) + (1,) + (0,)*(k+1) + (1,) + (0,)*(k-1)
    assert u != v and len(u) == len(v) == 3*k+1
    assert u == u[::-1] and v == v[::-1]
    assert profile(u,k) == profile(v,k)


for q, high in ((2, 7), (3, 4), (4, 3)):
    for k in range(1, high+1):
        for n in range(1, 3*k+2):
            by_profile = {}
            found_collision = False
            for w in palindromes(q, n):
                p = profile(w, k)
                if p in by_profile and by_profile[p] != w:
                    found_collision = True
                else:
                    by_profile[p] = w
            assert found_collision == (n == 3*k+1), (q, k, n, found_collision)
        witness(k)
        print(f"PASS q={q} k={k}: injective through {3*k}, noninjective at {3*k+1}")
print('ALL EXHAUSTIVE TESTS PASSED')
