#!/usr/bin/env python3
"""Standalone finite checks for the Cantor-word initial non-repetitive theorem.
Only finite checks; the infinite statement is proved separately in RESULT.md.
"""

def substitute(w):
    return ''.join('101' if c == '1' else '000' for c in w)


def digit_value(n):
    while n:
        if n % 3 == 1:
            return '0'
        n //= 3
    return '1'


def test_scale(k):
    n = 3 ** k
    m = 3 ** (k - 1)
    expected = 5 * m
    seq = '1'
    for _ in range(k + 1):
        seq = substitute(seq)
    assert len(seq) == 3 * n
    assert all(seq[i] == digit_value(i) for i in range(3 * n))
    seen = {}
    for j in range(expected + 1):
        factor = seq[j:j + n]
        if factor in seen:
            assert j == expected, (k, 'early collision', j, seen[factor])
            assert seen[factor] == m, (k, 'wrong collision partner', seen[factor])
            break
        seen[factor] = j
    else:
        raise AssertionError((k, 'no predicted collision'))
    base = seq[:m]
    assert seq[:n] == base + '0' * m + base
    assert seq[n:2*n] == '0' * n
    assert seq[2*n:3*n] == seq[:n]
    assert seq[m:m+n] == seq[expected:expected+n]
    return n, expected


def main():
    assert substitute('1') == '101'
    assert substitute('0') == '000'
    for k in range(1, 9):
        n, first = test_scale(k)
        print(f'k={k} length={n} first_repeat_start={first} PASS')
    print('VERIFY_OK: scales k=1..8; both sequence generators agree')

if __name__ == '__main__':
    main()
