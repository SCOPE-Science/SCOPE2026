#!/usr/bin/env python3
"""Recompute initial non-repetitive complexity for the period-doubling fixed point.

Finite checks accompany an independent proof for every positive length.
"""

def period_doubling_prefix(min_length):
    w = b'0'
    while len(w) < min_length:
        w = b''.join((b'01' if c == 48 else b'00') for c in w)
    return w


def predicted(n):
    if n < 1:
        raise ValueError('positive length required')
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 4
    return 2 * predicted(n // 2)


def closed(n):
    if n == 1:
        return 2
    k = n.bit_length() - 1
    return (3 << (k-1)) if n < 3*(1 << (k-1)) else (1 << (k+1))


def direct(n, word):
    seen = {}
    for i in range(len(word)-n+1):
        f = word[i:i+n]
        if f in seen:
            return i
        seen[f] = i
    raise AssertionError('insufficient word prefix to encounter a repetition')


def main():
    p = period_doubling_prefix(8192)
    assert p[:16] == b'0100010101000100'
    assert b'11' not in p
    assert b'0000' not in p
    assert all(p[2*j] == 48 and p[2*j+1] == (49 if p[j] == 48 else 48)
               for j in range(len(p)//2))
    # Direct factor comparison, rather than hashing, checks 512 complete first repetitions.
    for n in range(1, 513):
        v = direct(n, p)
        assert v == predicted(n), (n, v, predicted(n))
        assert v == closed(n), (n, v, closed(n))
    # Test the arithmetic form at much larger lengths without pretending to
    # enumerate their actual factors.
    for k in range(1, 65):
        a = 1 << k
        for n in (a, a+1, 3*a//2-1, 3*a//2, 2*a-1):
            assert predicted(n) == closed(n), (n, predicted(n), closed(n))
    print('VERIFY_OK: 512 direct factor lengths, 320 large-parameter algebra checks')


if __name__ == '__main__':
    main()
