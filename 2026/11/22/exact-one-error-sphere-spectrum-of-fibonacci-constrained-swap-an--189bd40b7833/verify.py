#!/usr/bin/env python3
"""Independent finite checks for the Fibonacci-constrained swap-or-replace sphere law.

Pure Python 3 standard library. Run with: python verify.py
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def allowed(w):
    return all((w[i], w[i + 1]) != (1, 1) for i in range(len(w) - 1))


def one_error_outputs(w):
    """Distinct admissible words after one adjacent swap or bit replacement."""
    n = len(w)
    outputs = set()
    for i in range(n):
        v = w[:i] + (1 - w[i],) + w[i + 1:]
        if allowed(v):
            outputs.add(v)
    for i in range(n - 1):
        if w[i] != w[i + 1]:
            v = w[:i] + (w[i + 1], w[i]) + w[i + 2:]
            if allowed(v):
                outputs.add(v)
    return outputs


def stat(w):
    return sum(w[i:i + 3] == (1, 0, 1) for i in range(len(w) - 2))


def closed_count(n, c):
    if c < 0:
        return 0
    total = int(c == 0)
    for k in range(c + 1, n + 1):
        top = n - 2 * k + 2
        bottom = k - c
        if 0 <= bottom <= top:
            total += comb(k - 1, c) * comb(top, bottom)
    return total


def state_dp(n):
    """An independent transfer recurrence, not using gap enumeration."""
    state = {((), 0): 1}
    for _ in range(n):
        new = defaultdict(int)
        for (last, c), mult in state.items():
            for bit in (0, 1):
                if last and last[-1] == bit == 1:
                    continue
                inc = int(len(last) == 2 and last == (1, 0) and bit == 1)
                new[((last + (bit,))[-2:], c + inc)] += mult
        state = new
    counts = Counter()
    for (_, c), mult in state.items():
        counts[c] += mult
    return counts


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    examined = 0
    for n in range(1, 21):
        counts = Counter()
        for w in product((0, 1), repeat=n):
            if not allowed(w):
                continue
            examined += 1
            c = stat(w)
            assert len(one_error_outputs(w)) == n - c, (n, w)
            counts[c] += 1
        assert counts == state_dp(n), ('transfer', n)
        assert sum(counts.values()) == fib(n + 2), ('count', n)
        assert all(counts[c] == closed_count(n, c)
                   for c in range(n + 1)), ('gap formula', n)
    for n in range(21, 101):
        counts = state_dp(n)
        assert all(counts[c] == closed_count(n, c)
                   for c in range(n + 1)), ('large gap formula', n)
    for n in range(1, 101):
        counts = state_dp(n)
        edges_by_degrees = sum((n - c) * mult for c, mult in counts.items())
        assert edges_by_degrees % 2 == 0
        edges = ((n + 1) * fib(n + 3) + (n - 2) * fib(n + 1)) // 5
        assert edges_by_degrees // 2 == edges, ('published edges', n)
        assert min(n - c for c in counts) == (n + 2) // 2, ('min-degree', n)
        assert max(n - c for c in counts) == n, ('max-degree', n)
        assert set(counts) == set(range((n - 1) // 2 + 1))
        min_count = counts[(n - 1) // 2]
        assert min_count == (2 if n == 1 else 3 if n == 2 else 1 if n & 1 else 2), ('extremizers', n)
    print('PASS: exhaustive one-edit neighborhoods for all admissible words, n=1..20')
    print('PASS: independent two-symbol transfer recurrence, n=1..100')
    print('PASS: closed degree histogram, full support, extremizers, n=1..100')
    print('PASS: first moment equals published exact edge count, n=1..100')
    print('admissible words directly checked:', examined)
    print('n=10 degree histogram:', sorted((10 - c, closed_count(10, c))
                                            for c in range(6) if closed_count(10, c)))


if __name__ == '__main__':
    main()
