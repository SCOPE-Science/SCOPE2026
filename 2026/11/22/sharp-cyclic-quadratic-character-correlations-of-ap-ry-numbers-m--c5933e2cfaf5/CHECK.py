#!/usr/bin/env python3
"""Independent exact checks of the seven-adic Apéry sign-correlation theorem.

Uses only Python's standard library. Enumerations test finite cases; the
all-depth conclusions require the induction printed in RESULT.md.
"""
from math import comb

DIGITS = (1, -1, -1, -1, -1, -1, 1)
ALPHA = (7, 2, 1, 0, -1, -2, 1)
BETA = (0, 1, -2, -1, 0, 1, 2)


def apery_mod7(n):
    return sum(comb(n, k)**2 * comb(n + k, k)**2
               for k in range(n + 1)) % 7


def digit_sign(n):
    a = 1
    while n:
        a *= DIGITS[n % 7]
        n //= 7
    return a


def quadratic_character(a):
    if a == 0:
        return 0
    return 1 if pow(a, 3, 7) == 1 else -1


def recurrence_correlations(depth):
    previous = [1]
    for r in range(1, depth + 1):
        n = len(previous)
        current = [0] * (7 * n)
        for q in range(n):
            x = previous[q]
            y = previous[(q + 1) % n]
            for b in range(7):
                current[7 * q + b] = ALPHA[b] * x + BETA[b] * y
        previous = current
    return previous


def direct_correlations(r):
    n = 7**r
    word = [digit_sign(i) for i in range(n)]
    return [sum(word[j] * word[(j + h) % n] for j in range(n))
            for h in range(n)]


def main():
    tests = 0
    # Compute Apéry numbers from the original sum: this is not an oracle for
    # the digit recurrence, and detects wrong base-seven character values.
    for n in range(101):
        assert quadratic_character(apery_mod7(n)) == digit_sign(n)
        tests += 1
    for r in range(1, 5):
        c = recurrence_correlations(r)
        assert c == direct_correlations(r)
        tests += len(c)
    for r in range(1, 7):
        c = recurrence_correlations(r)
        n = 7**r
        assert c[0] == n
        assert c[1] == c[-1] == (n + 2)//3
        assert sum(c) == 9**r
        tests += 4
        if r == 1:
            assert min(c[1:]) == -1
            assert sorted(i for i in range(1, n) if c[i] == -1) == [2, 3, 4, 5]
            assert max(c[1:]) == 3
            tests += 3
        else:
            high = 3 * 7**(r - 1)
            low = -(5 * 7**(r - 1) - 2) // 3
            assert max(c[1:]) == high
            assert min(c[1:]) == low
            assert [i for i in range(1, n) if c[i] == high] == [n//7, 6*n//7]
            assert [i for i in range(1, n) if c[i] == low] == [5, n-5]
            tests += 4
        # All four ordered pair-fiber counts are nonnegative integers and
        # reconstruct the two marginals and the signed correlation.
        s = (-3)**r
        for h in (0, 1, 5, n//7, n-1):
            x = c[h]
            pp, mm, mixed = (n + 2*s + x)//4, (n - 2*s + x)//4, (n-x)//4
            assert (n + 2*s + x) % 4 == 0
            assert (n - 2*s + x) % 4 == 0
            assert (n-x) % 4 == 0
            assert min(pp, mm, mixed) >= 0
            assert pp + mm + 2*mixed == n
            tests += 5
    print(f'PASS: {tests} independent exact assertions; cyclic depths 1..6')


if __name__ == '__main__':
    main()
