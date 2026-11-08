#!/usr/bin/env python3
"""Independent exact modular checks for prime-power-row binomial power sums."""
from math import comb

PRIMES = [3, 5, 7, 11, 13, 17, 19]
EXPONENTS = [2, 3, 4, 5, 6, 8, 10, 12, 19, 26, 28, 50, 126]


def valuation(n, p):
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def check(p, q, t):
    n = p ** q - 1
    m = valuation(t - 1, p)
    modulus = p ** (q + m + 1)
    # Recurrence avoids factorial computation, and all residues are exact integers.
    coefficient = 1
    signed = 0
    unsigned = 0
    for k in range(n + 1):
        signed += pow(coefficient if k % 2 == 0 else -coefficient, t, modulus)
        if t % 2 == 0:
            unsigned += pow(coefficient, t, modulus)
        if k < n:
            coefficient = coefficient * (n - k) // (k + 1)
    signed %= modulus
    assert signed == (-(t - 1) * p ** q) % modulus, (p, q, t, signed)
    assert signed % p ** (q + m) == 0
    assert signed % modulus != 0
    if t % 2 == 0:
        assert signed == unsigned % modulus
    return t % 2 == 0


def main():
    count = 0
    unsigned = 0
    maximal_row = 0
    for p in PRIMES:
        for q in range(1, 6):
            n = p ** q - 1
            if n > 2300:
                continue
            maximal_row = max(maximal_row, n)
            for t in EXPONENTS:
                unsigned += check(p, q, t)
                count += 1
    print(f"VERIFY_OK signed_cases={count} unsigned_cases={unsigned} "
          f"primes={len(PRIMES)} maximal_row={maximal_row} exact_congruences=PASS")


if __name__ == "__main__":
    main()
