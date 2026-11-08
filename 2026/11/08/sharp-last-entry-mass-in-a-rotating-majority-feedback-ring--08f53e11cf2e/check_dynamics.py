"""Independent labelled-state verification of majority-feedback ring dynamics.

Usage: python3 check_dynamics.py
"""
from collections import Counter
from math import gcd


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def no_singletons(word, n):
    return all((word >> i & 1) == (word >> ((i-1) % n) & 1) or
               (word >> i & 1) == (word >> ((i+1) % n) & 1)
               for i in range(n))


def step(word, n):
    feedback = int(((word >> (n-2)) & 1) + ((word >> (n-1)) & 1) + (word & 1) >= 2)
    return ((word << 1) & ((1 << n) - 1)) | feedback


def expected_population(n):
    return lucas(n) + (2 if n % 6 == 0 else 1 if n % 6 in (1, 5) else -1 if n % 6 in (2, 4) else -2)


def expected_last(n):
    return ((1 << (n-2)) + (2 if n % 2 == 0 else 4)) // 3


def check(n):
    N = 1 << n
    initial = sum(no_singletons(x, n) for x in range(N))
    assert initial == expected_population(n), (n, initial)
    hit = Counter()
    for x in range(N):
        y = x
        k = 0
        while not no_singletons(y, n):
            y = step(y, n)
            k += 1
            assert k <= n, (n, x, k)
        hit[k] += 1
        assert step(y, n) == ((y << 1) & (N-1)) | ((y >> (n-1)) & 1)
    assert sum(hit.values()) == N
    assert max(hit) == n
    assert hit[n] == expected_last(n), (n, hit[n], expected_last(n))
    cycles = Counter()
    seen = set()
    for x in range(N):
        if not no_singletons(x, n) or x in seen:
            continue
        y = x
        k = 0
        while y not in seen:
            seen.add(y)
            y = step(y, n)
            k += 1
        assert y == x
        assert n % k == 0
        cycles[k] += 1
    assert sum(k*v for k,v in cycles.items()) == initial
    return initial, hit[n], len(seen), dict(sorted(cycles.items()))


if __name__ == '__main__':
    total = 0
    for n in range(3, 15):
        out = check(n)
        total += 1 << n
        print(f'n={n}: recurrent={out[0]}, latest-entry={out[1]}, cycles={out[3]}')
    print(f'PASS: {total} initial configurations checked across n=3..14')
