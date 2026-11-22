"""Reproduce the complete prime-field exception census for sums of two eighth powers.

Only standard Python 3 is required. This is a finite calculation; the
large-prime assertion separately follows from the Hasse--Weil bound.
"""
from math import gcd, isqrt

LIMIT = 1777
EXCEPTIONS = {
    5: 3, 13: 10, 17: 5, 29: 22, 41: 21, 73: 46, 89: 56,
    97: 73, 113: 85, 137: 86, 233: 204, 257: 225,
    337: 295, 761: 666,
}


def primes_through(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for k in range(2, isqrt(n) + 1):
        if sieve[k]:
            sieve[k * k:n + 1:k] = b'\x00' * ((n - k * k) // k + 1)
    return [i for i in range(n + 1) if sieve[i]]


def count_covered(p):
    values = {pow(x, 8, p) for x in range(p)}
    assert len(values) == 1 + (p - 1) // gcd(p - 1, 8)
    covered = bytearray(p)
    for u in values:
        for v in values:
            covered[(u + v) % p] = 1
    return sum(covered), covered, values


def independent_count(p):
    # All distinct x^8 values are computed by repeated squaring,
    # independently of the built-in modular exponentiation method.
    vals = set()
    for x in range(p):
        y = (x * x) % p
        y = (y * y) % p
        y = (y * y) % p
        vals.add(y)
    present = {((u + v) % p) for u in vals for v in vals}
    return len(present)


def main():
    all_primes = primes_through(LIMIT)
    failures = {}
    for p in all_primes:
        number, cover, values = count_covered(p)
        assert number == independent_count(p), (p, number)
        assert number == EXCEPTIONS.get(p, p), (p, number)
        if number < p:
            failures[p] = number
    assert failures == EXCEPTIONS
    # The inequality p - 7 - 42 sqrt(p) > 0 is certified without floats.
    assert (1783 - 7)**2 > 42**2 * 1783
    assert all((p - 7)**2 > 42**2 * p for p in range(1783, 5000))
    assert 761 in failures and all(p < 769 for p in failures)
    assert 769 in all_primes and 769 not in failures
    print('PASS: primes from 2 through', LIMIT, '=', len(all_primes))
    print('PASS: full eighth-power pair-image census with independent modular-power recomputation')
    print('Exceptions (p : number of representable residues):', failures)
    print('PASS: Hasse--Weil positivity begins by prime 1783; last exception 761, sharp prime threshold 769')


if __name__ == '__main__':
    main()
