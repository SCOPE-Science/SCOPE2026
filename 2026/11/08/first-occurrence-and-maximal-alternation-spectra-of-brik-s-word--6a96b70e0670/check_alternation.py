"""Independent finite-prefix checks for the alternating-factor theorem.

All word positions in the accompanying mathematical statement are one-based.
The script uses Python's zero-based str.find and converts explicitly.
"""


def blocks(up_to):
    b = "101"
    for i in range(1, up_to + 1):
        yield i, b
        b = b + b[i:]


def longest_alternating(s):
    best = cur = 1
    for j in range(1, len(s)):
        cur = cur + 1 if s[j] != s[j - 1] else 1
        best = max(best, cur)
    return best


def first_start(k):
    """Proved 1-based first position of (01)^k for k >= 1."""
    if k == 1:
        return 2
    if k == 2:
        return 2
    x = 38
    for n in range(4, k + 1):
        x = (1 << (x - 2)) + x - 1
    return x


def first_alternating_pattern(s):
    n = len(s)
    if n == 1:
        return 1 if s == '1' else 2
    if any(s[j] == s[j - 1] for j in range(1, n)):
        raise ValueError('not alternating')
    if n % 2 == 0:
        k = n // 2
        return first_start(k) if s[0] == '0' else first_start(k) - 1
    k = n // 2
    return first_start(k + 1) if s[0] == '0' else first_start(k) - 1


def stage(k):
    if k == 1:
        return 1
    if k == 2:
        return 2
    if k == 3:
        return 7
    return first_start(k - 1)


def main():
    instances = 0
    positions = 0
    for i, b in blocks(19):
        assert len(b) == (1 << (i - 1)) + i + 1
        assert b[0] == '1' and b[-1] == '1' and '00' not in b
        if i >= 3:
            assert b[-4:] == '1101'
        K = max(k for k in range(1, 5) if stage(k) <= i)
        assert longest_alternating(b) == 2 * K + 1, (i, K)
        for m in range(1, 9):
            for first in '01':
                alt = ''.join(first if j % 2 == 0 else str(1-int(first)) for j in range(m))
                predicted = first_alternating_pattern(alt)
                actual0 = b.find(alt)
                actual = actual0 + 1 if actual0 >= 0 else None
                expected = predicted if predicted + m - 1 <= len(b) else None
                assert actual == expected, (i, alt, actual, expected)
                instances += 1
                if actual is not None:
                    positions += 1
    # The first crossing of 010101 is at the sixth construction boundary.
    B = list(blocks(7))
    b6, b7 = B[5][1], B[6][1]
    assert '010101' not in b6
    assert b6[6:10] == '0101'  # 1-based position 7
    assert b7.find('010101') == 37  # 1-based position 38
    # The next root is beyond any feasible direct expansion; check the
    # finite source window and exact integer arithmetic, not a huge word.
    r3 = 38
    r4 = (1 << (r3-2)) + r3 - 1
    assert r4 == 68719476773
    assert b7[37:43] == '010101'
    assert ((1 << 36) + 38) - 1 == r4
    print('PASS: 19 blocks; %d alternating-factor checks (%d present);' %
          (instances, positions))
    print('PASS: maximal alternating lengths, prefix tails, first 010101,'
          ' and symbolic next witness r4=%d' % r4)
    print('Note: arbitrary giant later terms are consequences of the proof,'
          ' not exhaustively generated.')

if __name__ == '__main__':
    main()
