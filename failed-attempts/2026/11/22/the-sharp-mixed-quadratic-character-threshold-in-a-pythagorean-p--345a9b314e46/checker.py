#!/usr/bin/env python3
"""Finite verification for mixed quadratic-character patterns of a Pythagorean parametrization.

No third-party packages. The finite enumeration establishes only the small-prime cases;
the uniform infinite assertion uses the character-sum proof in RESULT.md.
"""
from itertools import product
from math import isqrt

MIXED = {e for e in product((-1, 1), repeat=3) if len(set(e)) == 2}
EXPECTED_EXCEPTIONS = {3, 5, 7, 13, 17, 29}
EXPECTED_MISSING = {
    3: MIXED,
    5: MIXED,
    7: {(-1, -1, 1), (-1, 1, 1), (1, -1, 1)},
    13: {(-1, 1, -1), (-1, 1, 1), (1, -1, -1), (1, -1, 1)},
    17: {(-1, 1, 1), (1, -1, 1), (1, 1, -1)},
    29: {(-1, -1, 1), (1, 1, -1)},
}


def isprime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def legendre_euler(v, p):
    v %= p
    if v == 0:
        return 0
    x = pow(v, (p - 1)//2, p)
    assert x in (1, p - 1)
    return 1 if x == 1 else -1


def word_mask(p, method):
    qrs = {x*x % p for x in range(1, p)} if method == 'square_set' else None
    def chi(v):
        v %= p
        if method == 'square_set':
            return 0 if v == 0 else (1 if v in qrs else -1)
        return legendre_euler(v, p)
    counts = {eps: 0 for eps in product((-1, 1), repeat=3)}
    first_witness = {}
    for t in range(p):
        fs = ((t*t-1) % p, (2*t) % p, (t*t+1) % p)
        if 0 in fs:
            continue
        eps = tuple(chi(z) for z in fs)
        assert 0 not in eps
        counts[eps] += 1
        first_witness.setdefault(eps, t)
    assert sum(counts.values()) == p - 3 - (2 if p%4 == 1 else 0)
    return counts, first_witness


def main():
    primes = [p for p in range(3, 149, 2) if isprime(p)]
    observed = set()
    for p in primes:
        c1, w1 = word_mask(p, 'square_set')
        c2, w2 = word_mask(p, 'euler')
        assert c1 == c2 and w1 == w2
        missing = MIXED - {e for e in MIXED if c1[e] > 0}
        if missing:
            observed.add(p)
            assert missing == EXPECTED_MISSING[p], (p, missing)
        else:
            assert p not in EXPECTED_EXCEPTIONS
    assert observed == EXPECTED_EXCEPTIONS
    for p in (149, 151, 157, 163, 167, 173, 179, 181, 191, 199, 211, 223, 251, 257, 509, 1009, 2003):
        assert isprime(p)
        counts, _ = word_mask(p, 'euler')
        assert all(counts[e] > 0 for e in MIXED)
    assert all(word_mask(31, 'euler')[0][e] > 0 for e in MIXED)
    print('PASS: two independent residue-character constructions agree for every odd prime below 149.')
    print(f'Primes completely enumerated below 149: {len(primes)}.')
    print('Precisely these primes fail to realize all six mixed patterns:', sorted(observed))
    for p in sorted(observed):
        print(f'  p={p}: missing {sorted(EXPECTED_MISSING[p])}')
    counts, witnesses = word_mask(31, 'euler')
    print('All six mixed-pattern first witnesses at p=31:',
          [(eps, witnesses[eps]) for eps in sorted(MIXED)])
    print('PASS: 17 additional primes from 149 to 2003 satisfy mixed-pattern universality.')
    print('The analytic bound p-23-10*sqrt(p)>0 for p>=149 is proved separately.')

if __name__ == '__main__':
    main()
