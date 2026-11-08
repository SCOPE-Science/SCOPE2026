#!/usr/bin/env python3
"""Independent finite-state enumeration using exact ten-step parity recurrence."""
from collections import Counter


def weights(n):
    solutions = set()
    for first_ten in range(1 << 10):
        p = tuple((first_ten >> i) & 1 for i in range(10))
        if not all(p[i] ^ p[(i+1) % 10] ^ p[(i+5) % 10] ^ p[(i+6) % 10] == 0
                   for i in range(10)):
            continue
        if not all(p[i] == p[(i+n) % 10] for i in range(10)):
            continue
        x = tuple(p[i % 10] for i in range(n))
        y = tuple(1 ^ x[(i-1) % n] ^ x[i] ^ x[(i+1) % n] for i in range(n))
        assert all((y[(i-2) % n] ^ y[i] ^ y[(i+2) % n] ^ x[i]) == 1
                   for i in range(n))
        solutions.add((x, y))
    return dict(Counter(sum(x) + sum(y) for x, y in solutions))


def formula(n):
    if n % 5:
        return {n: 2 if n % 2 else 4}
    return ({3*n//5: 10, n: 12, 7*n//5: 10} if n % 2
            else {3*n//5: 10, n: 44, 7*n//5: 10})


if __name__ == '__main__':
    for n in range(5, 101):
        actual = weights(n)
        assert actual == formula(n), (n, actual)
        if n in (5, 6, 7, 10, 15, 20, 25, 30, 100):
            print('periodic', n, 'weight_counts', sorted(actual.items()))
    assert len([b for b in range(1 << 10) if
        all(((b >> i) ^ (b >> ((i+1) % 10)) ^ (b >> ((i+5) % 10)) ^
             (b >> ((i+6) % 10))) & 1 == 0 for i in range(10))]) == 64
    print('PERIODIC_RECURRENCE_PASS_n5_to100')
