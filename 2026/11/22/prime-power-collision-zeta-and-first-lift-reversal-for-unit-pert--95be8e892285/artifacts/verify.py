#!/usr/bin/env python3
"""Direct finite checks of biquadratic equal-value collision counts.

No external dependencies. Run with: python3 artifacts/verify.py
"""
from collections import Counter


def chi(a, p):
    a %= p
    if not a:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def formula(p, k, c):
    assert p % 2 == 1 and c % p != 0 and k >= 1
    epsilon = chi(-1, p)
    eta = chi(-c * pow(2, -1, p), p)
    return p ** (k - 1) * (3 * p - 3 - epsilon - 2 * eta
            + (k - 1) * (p - 1) * (3 + 2 * eta))


def direct(p, k, c):
    modulus = p ** k
    counts = [0] * modulus
    for x in range(modulus):
        y = (pow(x, 4, modulus) + c * pow(x, 2, modulus)) % modulus
        counts[y] += 1
    assert sum(counts) == modulus
    return sum(v * v for v in counts)


def geometric_counts(p, c):
    r = 0
    smooth = 0
    crossing = 0
    for x in range(p):
        for y in range(p):
            zero_count = sum((x-y) % p == 0 for _ in range(1))
            zero_count += int((x+y) % p == 0)
            zero_count += int((x*x + y*y + c) % p == 0)
            if zero_count:
                r += 1
                if zero_count == 1:
                    smooth += 1
                else:
                    crossing += 1
            assert zero_count < 3
    return r, smooth, crossing


def run():
    cases = 0
    checks = 0
    direct_pairs = 0
    geometry = 0
    for p in (3, 5, 7, 11, 13, 17):
        for c in (1, 2, 3, 4, 1 + p, 2 + 2 * p):
            if c % p == 0:
                continue
            eta = chi(-c * pow(2, -1, p), p)
            union, smooth, crosses = geometric_counts(p, c)
            assert crosses == 3 + 2 * eta
            assert union == 3 * p - 3 - chi(-1, p) - 2 * eta
            assert smooth + crosses == union
            geometry += 1
            for k in (1, 2, 3):
                mod = p**k
                got = direct(p, k, c)
                expected = formula(p, k, c)
                assert got == expected, (p, k, c, got, expected)
                checks += mod
                cases += 1
                if mod <= 121:
                    brute = sum(1 for x in range(mod) for y in range(mod)
                                if (x**4+c*x*x-y**4-c*y*y) % mod == 0)
                    assert brute == got
                    direct_pairs += mod * mod
        for k in range(1, 5):
            pos = next(c for c in range(1, p) if chi(-c * pow(2, -1, p), p) == 1)
            neg = next(c for c in range(1, p) if chi(-c * pow(2, -1, p), p) == -1)
            assert formula(p, k, pos) - formula(p, k, neg) == (
                4 * p ** (k-1) * ((k-1)*(p-1)-1))
    print(f'PASS histogram_cases={cases} input_residues={checks} '
          f'direct_pair_checks={direct_pairs} finite_field_geometry_cases={geometry} '
          f'phase_comparisons={6*4}')


if __name__ == '__main__':
    run()
