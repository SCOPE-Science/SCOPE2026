#!/usr/bin/env python3
"""Independent finite check of the sixteen Gaussian-norm quadratic-character words."""
from math import isqrt
from hashlib import sha256

LIMIT = 2529
EXCEPTIONS = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 61)


def primes_below(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[0:2] = b'\x00\x00'
    for a in range(2, isqrt(limit - 1) + 1):
        if sieve[a]:
            for j in range(a*a, limit, a):
                sieve[j] = 0
    return [i for i in range(3, limit, 2) if sieve[i]]


def histogram_square_lookup(p):
    squares = {i*i % p for i in range(1, p)}
    counts = [0]*16
    for n in range(p):
        m = 0
        for j in range(4):
            v = ((n+j)*(n+j)+1) % p
            if v == 0:
                break
            m = 2*m + int(v in squares)
        else:
            counts[m] += 1
    return counts


def histogram_euler(p):
    counts = [0]*16
    for n in range(p):
        m = 0
        for j in range(4):
            v = ((n+j)*(n+j)+1) % p
            if not v:
                break
            euler = pow(v, (p-1)//2, p)
            assert euler in (1, p-1)
            m = 2*m + int(euler == 1)
        else:
            counts[m] += 1
    return counts


def main():
    primes = primes_below(LIMIT)
    failures = []
    digest = sha256()
    for p in primes:
        a = histogram_square_lookup(p)
        b = histogram_euler(p)
        assert a == b, ('independent computation mismatch', p)
        assert len(a) == 16 and all(n >= 0 for n in a)
        absent = [i for i, v in enumerate(a) if not v]
        if absent:
            failures.append(p)
        if p >= 67:
            assert not absent, ('counterexample to threshold', p, absent)
        digest.update((f'{p}:' + ','.join(map(str, a)) + '\n').encode('ascii'))
        if p == 61:
            assert absent == [9], ('sharp p=61 obstruction', absent)
        if p == 59:
            assert not absent
    assert tuple(failures) == EXCEPTIONS, (failures, EXCEPTIONS)
    assert any(p == 67 for p in primes)
    assert len([p for p in primes if p >= 67]) == 351
    print('PASS: two independent 16-word histograms agree for all', len(primes), 'odd primes below', LIMIT)
    print('Exact exceptional primes:', failures)
    print('Sharp boundary: 59 complete; 61 missing only (+,-,-,+); 67 complete')
    print('Prime-histogram SHA-256:', digest.hexdigest())


if __name__ == '__main__':
    main()
