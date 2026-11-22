#!/usr/bin/env python3
"""Exhaustive prime-field certificate for mixed signs after a nonzero square."""
from hashlib import sha256

LIMIT = 2579  # The character-sum estimate proves the result at primes >= 2579.
EXCEPTIONS = {
    5:16, 7:14, 11:12, 13:13, 17:12, 19:9, 23:6, 29:6,
    31:6, 37:3, 41:6, 43:1, 47:3, 53:3, 61:2, 71:1,
    73:2, 89:2, 97:2, 103:1, 113:1, 137:2, 149:1, 193:1,
}

def primes_below(n):
    flags = bytearray(b'\1') * n
    flags[:2] = b'\0\0'
    for x in range(2, int(n ** 0.5) + 1):
        if flags[x]:
            for y in range(x * x, n, x):
                flags[y] = 0
    return [x for x in range(5, n) if flags[x]]

def by_euler(p):
    # Enumerate nonzero square roots as indexed inputs; Euler test independently.
    mask = 0
    for x in range(1, p):
        sq = x * x % p
        word = 0
        for j in range(1, 5):
            v = (sq + j) % p
            if not v:
                break
            word = (word << 1) | (pow(v, (p - 1) // 2, p) == 1)
        else:
            mask |= 1 << word
    return mask

def by_residue_sets(p):
    # A different enumeration: list distinct square origins and square targets.
    sq = {x * x % p for x in range(1, p)}
    mask = 0
    for y in sq:
        v = [((y + j) % p) for j in range(1, 5)]
        if all(v):
            word = sum((v[j] in sq) << (3 - j) for j in range(4))
            mask |= 1 << word
    return mask

def main():
    primes = primes_below(LIMIT)
    assert len(primes) == 373
    missing = {}
    census = bytearray()
    for p in primes:
        left, right = by_euler(p), by_residue_sets(p)
        assert left == right, (p, left, right)
        census.extend(f'{p}:{left:04x}\n'.encode('ascii'))
        if left != 0xffff:
            missing[p] = 16 - left.bit_count()
            assert p in EXCEPTIONS
        else:
            assert p not in EXCEPTIONS
    assert missing == EXCEPTIONS
    assert by_euler(193) == 0x7fff  # Last obstruction: all-positive word.
    assert by_euler(197) == 0xffff # First prime after last obstruction.
    print('PASS: two independent algorithms match 373 full sixteen-pattern masks')
    print('24 exceptional primes with absent word counts:', sorted(missing.items()))
    print('Last obstruction at 193: only all-positive word missing; prime 197 universal')
    print('Complete-census SHA256:', sha256(census).hexdigest())

if __name__ == '__main__':
    main()
