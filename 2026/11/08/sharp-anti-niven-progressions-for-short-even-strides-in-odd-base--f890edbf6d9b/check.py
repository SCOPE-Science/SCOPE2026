#!/usr/bin/env python3
"""Exact finite spot checks of the CRT construction for anti-Niven progressions."""
from math import gcd, lcm


def digit_sum(n, b):
    s = 0
    while n:
        n, r = divmod(n, b)
        s += r
    return s


def prime_factors(n):
    out = []
    t = 2
    while t * t <= n:
        if n % t == 0:
            out.append(t)
            while n % t == 0:
                n //= t
        t += 1
    if n > 1:
        out.append(n)
    return out


def construction(b, d):
    assert b >= 3 and b % 2 == 1 and d >= 2 and d % 2 == 0
    p = next((q for q in prime_factors(b - 1) if d % q), None)
    if p is None or (p - 2) * d > b + 1:
        return None
    c = next((c for c in range(b - 1) if all(gcd(b - 1, 1 + c + j * d) == 1 for j in range(p - 1))), None)
    assert c is not None, (b, d, p)
    offsets = [c + j * d for j in range(p - 1)]
    assert max(offsets) < 2 * b
    sums = [1 + digit_sum(x, b) for x in offsets]
    T = 1
    for s in sums:
        for q in prime_factors(s):
            if b % q:
                T = lcm(T, q - 1)
    m = T + 1
    assert b**m > max(offsets) if m < 1000 else m >= 3
    assert all(gcd((pow(b, m, s) + x) % s, s) == 1 for x, s in zip(offsets, sums))
    assert all(gcd(b - 1, 1 + x) == 1 for x in offsets)
    return p, c, m, sums


def main():
    cases = 0
    maxp = 0
    examples = {}
    for b in range(3, 302, 2):
        for d in range(2, 43, 2):
            w = construction(b, d)
            if w is None:
                continue
            p, c, m, sums = w
            cases += 1
            maxp = max(maxp, p)
            if (b, d) in {(11, 4), (21, 4), (29, 4), (45, 4), (77, 4), (169, 4)}:
                examples[(b, d)] = (p, c, m, sums)
    assert cases > 250
    print('Checked admissible pairs: ' + str(cases))
    print('Largest p in checked region: ' + str(maxp))
    for (b, d), (p, c, m, sums) in sorted(examples.items()):
        print(f'b={b}, d={d}: p={p}, c={c}, m={m}, digit sums={sums}')
    for b, d in ((11, 4), (21, 4)):
        p, c, m, sums = construction(b, d)
        for j, s in enumerate(sums):
            n = b ** m + c + j * d
            assert digit_sum(n, b) == s and gcd(n, s) == 1
    print('Explicit integers independently checked for bases 11 and 21.')
    print('All exact modular checks passed.')

if __name__ == '__main__':
    main()
