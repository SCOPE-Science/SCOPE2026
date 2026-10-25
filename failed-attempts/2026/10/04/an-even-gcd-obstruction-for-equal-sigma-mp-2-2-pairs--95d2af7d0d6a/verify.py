#!/usr/bin/env python3
from math import isqrt

LIMIT = 200000

def sigma_sieve(n):
    s = [0] * (n + 1)
    for d in range(1, n + 1):
        for k in range(d, n + 1, d):
            s[k] += d
    return s

def is_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n

def main():
    sig = sigma_sieve(LIMIT)

    parity_checks = 0
    for n in range(1, LIMIT + 1):
        form = is_square(n) or (n % 2 == 0 and is_square(n // 2))
        assert (sig[n] % 2 == 1) == form, (n, sig[n], form)
        parity_checks += 1

    fibers = {}
    for n in range(1, LIMIT + 1):
        fibers.setdefault(sig[n], []).append(n)

    equal_sigma_pythagorean = []
    for c, vals in fibers.items():
        if len(vals) < 2:
            continue
        S = set(vals)
        c2 = c * c
        for m in vals:
            d = c2 - m * m
            if d <= 0:
                continue
            n = isqrt(d)
            if n > m and n in S and n * n == d:
                equal_sigma_pythagorean.append((m, n, c))

    assert not equal_sigma_pythagorean, equal_sigma_pythagorean

    examples = [(1, 2), (13, 21), (13, 27), (17, 175), (45, 123)]
    for m, n in examples:
        lhs = sig[m] * sig[m] + sig[n] * sig[n]
        rhs = 2 * (m * m + n * n)
        assert lhs == rhs, (m, n, lhs, rhs)
        assert sig[m] != sig[n], (m, n, sig[m])

    print("VERIFY_OK")
    print("parity_criterion_checked_through=" + str(LIMIT))
    print("equal_sigma_pythagorean_pairs_through_limit=0")
    print("source_MP22_examples_checked=" + str(len(examples)))

if __name__ == "__main__":
    main()
