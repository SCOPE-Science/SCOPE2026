#!/usr/bin/env python3
"""Independent exact finite-level tests for a family of polynomial congruences.

No dependencies beyond the Python standard library.
Run: python3 check.py
The proof for all exponents and moduli is in RESULT.md; finite tests are supplementary.
"""
from collections import Counter


def squares_mod_3_power(L):
    modulus = 3 ** L
    return {v * v % modulus for v in range(modulus)}


def expected_fibers(s, n):
    modulus = 3 ** n
    m = 3 ** s
    c = pow(2, 1 - m, modulus)
    if n == 1:
        return {1: 3}
    count = Counter()
    # x == 0 and -1 (mod 3): each branch is an isometry after normalization.
    ball_modulus = 3 ** min(n, s + 1)
    ball_fiber = 2 * 3 ** min(s, n - 1)
    for y in range(modulus):
        if (y - 1) % ball_modulus == 0:
            count[y] += ball_fiber
    # x == 1 (mod 3): a scaled 3-adic square map after an isometry.
    if n <= s + 2:
        count[c] += 3 ** (n - 1)
    else:
        L = n - s - 2
        sq_fibers = Counter(v * v % (3 ** L) for v in range(3 ** L))
        for z, multiplicity in sq_fibers.items():
            count[(c + (3 ** (s + 2)) * z) % modulus] += (3 ** (s + 1)) * multiplicity
    return dict(count)


def check(s, n):
    modulus = 3 ** n
    m = 3 ** s
    actual = Counter((pow(x + 1, m, modulus) - pow(x, m, modulus)) % modulus
                     for x in range(modulus))
    expected = expected_fibers(s, n)
    if actual != expected:
        for y in sorted(set(actual) | set(expected)):
            if actual[y] != expected.get(y, 0):
                raise AssertionError((s, n, y, actual[y], expected.get(y, 0)))
    assert sum(actual.values()) == modulus
    return len(actual)


def main():
    checks = 0
    for s in range(1, 5):
        depths = range(1, 10) if s <= 2 else range(1, 9)
        counts = []
        for n in depths:
            counts.append(check(s, n))
            checks += 1
        print(f"s={s}: image cardinalities {counts}")
    print(f"PASS: {checks} complete residue-and-fiber enumerations")

if __name__ == '__main__':
    main()
