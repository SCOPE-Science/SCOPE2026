#!/usr/bin/env python3
"""Direct, integer-based finite checks for the dyadic Baum-Sweet pair theorem.
Run with: python3 checks/direct_check.py
"""

def admissible(n):
    assert n >= 0
    if n == 0:
        return True
    bits = bin(n)[2:]
    return all(len(run) % 2 == 0 for run in bits.split('1'))


def tiling_suffixes(r):
    if r == 0:
        return {0}
    out = {int(s, 2) for s in build(r)}
    return out


def build(length):
    if length == 0:
        yield ''
    if length >= 1:
        for rest in build(length - 1):
            yield '1' + rest
    if length >= 2:
        for rest in build(length - 2):
            yield '00' + rest


def explicit_pairs(m, r):
    for t in range((m - r - 1) // 2 + 1):
        for s in tiling_suffixes(r):
            yield ((1 << (2 * t)) - 1) * (1 << r) + s


def verify():
    fib = [0, 1]
    for _ in range(25):
        fib.append(fib[-1] + fib[-2])
    for m in range(1, 16):
        b = [admissible(i) for i in range(1 << m)]
        for r in range(m):
            d = 1 << r
            brute = {i for i in range((1 << m) - d) if b[i] and b[i + d]}
            explicit = set(explicit_pairs(m, r))
            assert brute == explicit, (m, r, sorted(brute ^ explicit)[:10])
            assert len(brute) == fib[r + 1] * ((m - r + 1) // 2), (m, r)
    print('DIRECT_OK: exact paired-index sets and counts, 1<=m<=15, 0<=r<m')

if __name__ == '__main__':
    verify()
