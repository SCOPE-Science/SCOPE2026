#!/usr/bin/env python3
"""Reproducible checks for the finite-path three-state excitable rule.
No external packages are required. Run: python3 verify.py
"""
from itertools import product
from collections import Counter


def direct_update(word):
    n = len(word)
    result = []
    for i, color in enumerate(word):
        if color:
            result.append((color + 1) % 3)
        elif (i > 0 and word[i - 1] == 1) or (i + 1 < n and word[i + 1] == 1):
            result.append(1)
        else:
            result.append(0)
    return tuple(result)


def initial_lift(word):
    values = [word[0]]
    for color in word[1:]:
        delta = (color - values[-1] + 1) % 3 - 1
        values.append(values[-1] + delta)
    return tuple(values)


def height_update(h):
    n = len(h)
    z = []
    for i, a in enumerate(h):
        active = (a % 3 != 0 or
                  (i > 0 and h[i - 1] == a + 1) or
                  (i + 1 < n and h[i + 1] == a + 1))
        z.append(a + int(active))
    return tuple(z)


def height_bounds(word):
    h = initial_lift(word)
    maximum = max(h)
    peak = ((maximum + 2) // 3) * 3
    near = [i for i, v in enumerate(h) if v >= peak - 2]
    far = [i for i, v in enumerate(h) if v == maximum]
    lower = max(near[0], len(h) - 1 - near[-1])
    upper = peak - maximum + min(max(i, len(h) - 1 - i) for i in far)
    return lower, upper


def direct_time(word):
    t = 0
    while any(word):
        word = direct_update(word)
        t += 1
        assert t <= len(word) + 1
    return t


def independent_integer_time(number, n):
    """Separate integer-state reference implementation (not reusing direct_update)."""
    powers = [3 ** i for i in range(n)]
    t = 0
    while number:
        states = [(number // pw) % 3 for pw in powers]
        nxt = 0
        for i in range(n):
            val = states[i]
            if val == 1:
                nv = 2
            elif val == 2:
                nv = 0
            else:
                nv = int((i and states[i - 1] == 1) or
                         (i < n - 1 and states[i + 1] == 1))
            nxt += powers[i] * nv
        number = nxt
        t += 1
        assert t <= n + 1
    return t


def run():
    print('finite-path three-state excitable model: exhaustive correctness checks')
    for n in range(1, 11):
        hist = Counter()
        for word in product(range(3), repeat=n):
            lift = initial_lift(word)
            assert all((a - b) % 3 == 0 for a, b in zip(lift, word))
            assert all(abs(a - b) <= 1 for a, b in zip(lift, lift[1:]))
            lo, hi = height_bounds(word)
            t = 0
            states = word
            h = lift
            start_max = max(lift)
            cap = ((start_max + 2) // 3) * 3
            while any(states):
                states2 = direct_update(states)
                h2 = height_update(h)
                assert tuple(v % 3 for v in h2) == states2
                assert all(v >= u for u, v in zip(h, h2))
                assert all(abs(a - b) <= 1 for a, b in zip(h2, h2[1:]))
                assert max(h2) <= cap
                states, h = states2, h2
                t += 1
                assert t <= n + 1
            assert len(set(h)) == 1 and h[0] == cap
            assert lo <= t <= hi
            hist[t] += 1
        if n <= 9:
            ref = Counter(independent_integer_time(number, n)
                          for number in range(3 ** n))
            assert ref == hist, (n, hist, ref)
        assert sum(hist.values()) == 3 ** n
        assert max(hist) == n + 1
        print(f'n={n:2d} states={3 ** n:6d} maximum_T={max(hist):2d} '
              f'number_maximal={hist[n+1]:6d} mean={sum(k*v for k,v in hist.items())/3**n:.7f}')
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    run()
