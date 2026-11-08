#!/usr/bin/env python3
"""Direct exhaustive and randomized checks of the binary-gap criterion.

No nonstandard packages or external files required. Run: python3 verify.py
The tests are finite checks, not a proof of the all-length theorem.
"""
from itertools import product
from random import Random


def predicted(w):
    if not w or any(c not in '01' for c in w):
        raise ValueError('nonempty binary input required')
    pos = [i for i, c in enumerate(w) if c == '1']
    m = len(pos)
    if m <= 2:
        return True
    gaps = [pos[i + 1] - pos[i] - 1 for i in range(m - 1)]
    if len(gaps) != len(set(gaps)):
        raise ValueError('repeated complete zero-gap length')
    a, e = pos[0], len(w) - 1 - pos[-1]
    if m == 3:
        return any(max(a, e) <= z <= a + e for z in gaps) or (a <= gaps[1] and e <= gaps[0])
    if m == 4:
        return max(a, e) <= gaps[1] <= a + e
    return False


def palindrome(t):
    return t == t[::-1]


def palindrome_pair(t):
    return any(palindrome(t[:j]) and palindrome(t[j:]) for j in range(len(t) + 1))


def brute_periodic_palindrome_pair(w):
    n = len(w)
    for p in range(1, n + 1):
        if all(w[j] == w[j - p] for j in range(p, n)):
            if palindrome_pair(w[:p]):
                return True
    return False


def brute_reversed_conjugate(w):
    n = len(w)
    for p in range(1, n + 1):
        if all(w[j] == w[j - p] for j in range(p, n)):
            root = w[:p]
            if root[::-1] in root + root:
                return True
    return False


def eligible(w):
    pos = [i for i, c in enumerate(w) if c == '1']
    gaps = [pos[i + 1] - pos[i] - 1 for i in range(len(pos) - 1)]
    return len(set(gaps)) == len(gaps)


def test():
    total = 0
    by_markers = {}
    # Covers all 524,286 binary strings with lengths 1..18, filtering
    # only on the stated hypothesis. The resulting words are compared
    # against the literal symmetric-period definition.
    for n in range(1, 19):
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            if not eligible(w):
                continue
            exp = predicted(w)
            got = brute_periodic_palindrome_pair(w)
            if exp != got:
                raise AssertionError(('exhaustive', w, exp, got))
            total += 1
            ones = w.count('1')
            by_markers[ones] = by_markers.get(ones, 0) + 1
    assert total == 19530, (total, by_markers)
    print('Exhaustive tested length 1..18: %d qualified words' % total)
    rng = Random(0x5A17)
    sampled = 0
    for j in range(600):
        m = rng.randint(0, 10)
        a, e = rng.randrange(15), rng.randrange(15)
        if m == 0:
            w = '0' * rng.randint(1, 30)
        else:
            gaps = rng.sample(range(0, 22), max(0, m-1))
            w = '0'*a + '1' + ''.join('0'*g+'1' for g in gaps) + '0'*e
        exp = predicted(w)
        got = brute_periodic_palindrome_pair(w)
        if exp != got:
            raise AssertionError(('random', w, exp, got))
        if j < 150:
            got2 = brute_reversed_conjugate(w)
            if got != got2:
                raise AssertionError(('duality', w, got, got2))
        sampled += 1
    print('Randomized qualified examples: %d; second decision method: 150' % sampled)
    sharp = '0' + '1' + '0'*2 + '1' + '0'*3 + '1' + '0'*4 + '1' + '0'*2
    assert sharp.count('1') == 4 and predicted(sharp) and brute_periodic_palindrome_pair(sharp)
    forbidden = '1' + '0' + '1' + '00' + '1' + '000' + '1' + '0000' + '1'
    assert forbidden.count('1') == 5 and not predicted(forbidden) and not brute_periodic_palindrome_pair(forbidden)
    print('Sharp four-marker and forbidden five-marker witnesses: PASS')
    print('PASS: all finite checks complete')

if __name__ == '__main__':
    test()
