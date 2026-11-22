#!/usr/bin/env python3
"""Independent finite verification of the nonunit threefactor parity-color theorem.
Uses only Python's standard library. Finite tests do not prove the infinite claim.
"""
from math import prod, comb


def prime_exponents(n):
    if n == 1:
        return []
    es = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                e += 1
                n //= d
            es.append(e)
        d += 1 if d == 2 else 2
    if n > 1:
        es.append(1)
    return es


def formula(n):
    es = prime_exponents(n)
    a = prod(comb(e + 2, 2) for e in es)
    b = prod((e * e - 5 * e + 2) // 2 for e in es)
    c = prod(e + 1 for e in es)
    d = prod(1 - e for e in es)
    h = prod(e - 3 for e in es)
    numerator = a + 3 * b - 3 * c - 6 * d - 3 * h
    assert numerator % 4 == 0, (n, numerator)
    return numerator // 4 + 3 * (1 + (-1) ** len(es)) // 2 - (n == 1)


def brute(n):
    divs = [v for v in range(1, n + 1) if n % v == 0]
    colors = {v: len(prime_exponents(v)) % 2 for v in divs}
    total = 0
    for a in divs:
        if a == 1:
            continue
        m = n // a
        for b in divs:
            if b == 1 or m % b:
                continue
            c = m // b
            if c > 1 and colors[a] == colors[b] == colors[c]:
                total += 1
    return total


def excluded(n):
    es = prime_exponents(n)
    r = len(es)
    return n == 1 or (r == 1 and es[0] in (1, 2)) or (r == 2 and es == [1, 1]) or (r == 4 and all(e == 1 for e in es))


def main():
    checked = 0
    for n in range(1, 2501):
        v = brute(n)
        assert formula(n) == v, ('count', n, formula(n), v)
        assert (v == 0) == excluded(n), ('support', n, v)
        checked += 1
    for n in (2 * 3 * 5 * 7 * 11, 2 * 3 * 5 * 7 * 11 * 13,
              4 * 3 * 5 * 7, 2**8 * 3**3 * 5, 2**5 * 3**4 * 5**3 * 7,
              2**12, 2**7 * 3, 2**4 * 3 * 5 * 7 * 11):
        v = brute(n)
        assert formula(n) == v and (v == 0) == excluded(n), ('spot', n)
        checked += 1
    print('PASS:', checked, 'independently enumerated integers; support and counts agree')


if __name__ == '__main__':
    main()
