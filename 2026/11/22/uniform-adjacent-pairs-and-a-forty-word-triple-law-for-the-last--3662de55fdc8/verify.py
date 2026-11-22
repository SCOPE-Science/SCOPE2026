#!/usr/bin/env python3
"""Exact finite-state and independent arithmetic checks for factorial digit triples.

All arithmetic is exact. No third-party libraries are required.
"""
from collections import Counter
from itertools import product
from math import factorial

GAMMA = (0, 0, 1, 0, 2)
STATES = tuple(product(range(4), repeat=3))
INDEX = {s: i for i, s in enumerate(STATES)}
DIGITS = (6, 2, 4, 8)


def step(s, r):
    a, b, t = s
    x = (a + t + GAMMA[r]) % 4
    y = ((a + t + GAMMA[r+1]) if r < 4 else (b + t + 1)) % 4
    return (x, y, (t + r) % 4)


def triple(s, r):
    a, b, t = s
    def digit(j):
        carry, rr = divmod(r + j, 5)
        return (((a if carry == 0 else b) + (t + carry) + GAMMA[rr])) % 4
    return (digit(0), digit(1), digit(2))


def last_digit_by_factorial(n):
    num = factorial(n)
    while num % 10 == 0:
        num //= 10
    return num % 10


def independent_digits(limit):
    d = [1] * (limit + 1)
    for n in range(1, limit + 1):
        q, r = divmod(n, 5)
        d[n] = (d[q] * (1, 1, 2, 6, 4)[r] * pow(2, q, 10)) % 10
    return d


def main():
    inbound = Counter(step(s, r) for s in STATES for r in range(5))
    assert len(inbound) == 64 and set(inbound.values()) == {5}

    minimum, maximum = 10**100, 0
    for start in STATES:
        counts = {start: 1}
        for _ in range(4):
            next_counts = Counter()
            for s, w in counts.items():
                for r in range(5):
                    next_counts[step(s, r)] += w
            counts = next_counts
        assert len(counts) == 64 and sum(counts.values()) == 625
        minimum = min(minimum, min(counts.values()))
        maximum = max(maximum, max(counts.values()))
    print('M^4 is strictly positive: min=', minimum, 'max=', maximum,
          '; each row sum=625; stationary state law=1/64')

    freq = Counter(triple(s, r) for s in STATES for r in range(5))
    assert sum(freq.values()) == 320
    assert Counter(freq.values()) == {4: 24, 8: 4, 16: 12}
    assert len(freq) == 40

    for x, y, z in product(range(4), repeat=3):
        formula = 16 * ((y == x and z == (x+1)%4)
                      + (y == (x+1)%4 and z == x)
                      + (y == (x-1)%4 and z == (x+1)%4))
        formula += 4 * (y == (x+2)%4) + 4 * (z == y)
        assert freq[x,y,z] == formula, ((x,y,z),freq[x,y,z],formula)

    pair = Counter()
    for (x,y,z),m in freq.items():
        pair[x,y] += m
    assert set(pair.values()) == {20} and len(pair) == 16
    assert sum(m for (x,y,z),m in freq.items() if x==y==z)==16
    print('16 pair types each frequency 20/320=1/16')
    print('Triple types: 12 of frequency 16/320, 4 of 8/320, '
          '24 of 4/320, and 24 forbidden')
    print('P(all three equal) = 16/320 = 1/20')

    f = independent_digits(60000)
    for n in range(0, 501):
        assert f[n] == last_digit_by_factorial(n), (n,f[n],last_digit_by_factorial(n))
    for n in range(10, 59998):
        assert f[n] in DIGITS and f[n+1] in DIGITS and f[n+2] in DIGITS
        q, r = divmod(n,5)
        s = (DIGITS.index(f[q]), DIGITS.index(f[q+1]), q%4)
        observed = tuple(DIGITS.index(f[n+j]) for j in range(3))
        assert observed == triple(s,r), (n,s,r,observed,triple(s,r))
        assert step(s,r) == (observed[0],observed[1],n%4)
        assert freq[observed] > 0
    print('Independent factorial integers: 501 cases; 59988 triple checks; all exact')


if __name__ == '__main__':
    main()
