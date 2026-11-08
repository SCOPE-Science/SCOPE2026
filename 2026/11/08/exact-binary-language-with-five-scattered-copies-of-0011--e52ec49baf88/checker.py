"""Executable checks for the five-occurrence 0011 language theorem.
Run: python3 checker.py (standard library only).
Finite tests corroborate, rather than replace, the proof in RESULT.md.
"""
from itertools import product, combinations
from math import comb


def occurrences_direct(word):
    return sum(word[i] == word[j] == '0' and word[k] == word[l] == '1'
               for i, j, k, l in combinations(range(len(word)), 4))


def occurrences_incremental(word):
    a = b = c = d = 0  # 0, 00, 001, 0011 subsequence counts
    for letter in word:
        if letter == '0':
            b += a
            a += 1
        else:
            d += c
            c += b
    return d


def in_language(word):
    # Parse the four uniquely determined maximal irrelevant zones.
    i = 0
    while i < len(word) and word[i] == '1':
        i += 1
    if i == len(word) or word[i] != '0':
        return False
    i += 1
    while i < len(word) and word[i] == '1':
        i += 1
    if word[i:i + 4] != '0101':
        return False
    i += 4
    while i < len(word) and word[i] == '0':
        i += 1
    if i >= len(word) or word[i] != '1':
        return False
    i += 1
    return all(x == '0' for x in word[i:])


def word_from_parameters(u, v, s, t):
    return '1' * u + '0' + '1' * v + '0101' + '0' * s + '1' + '0' * t


def run():
    compared = 0
    for n in range(0, 15):
        actual = 0
        expected = 0 if n < 6 else comb(n - 3, 3)
        for t in product('01', repeat=n):
            w = ''.join(t)
            count = occurrences_incremental(w)
            assert (count == 5) == in_language(w), (n, w, count)
            if n <= 11:
                assert count == occurrences_direct(w), (n, w)
            actual += count == 5
            compared += 1
        assert actual == expected, (n, actual, expected)

    checked_parameters = 0
    for u in range(8):
        for v in range(8):
            for s in range(8):
                for t in range(8):
                    w = word_from_parameters(u, v, s, t)
                    assert occurrences_incremental(w) == 5
                    assert in_language(w)
                    checked_parameters += 1

    # Independent state recurrence (counters truncated above target 5).
    start = (0, 0, 0, 0)
    dp = {start: 1}
    for n in range(50):
        count = sum(mult for (_, _, _, d), mult in dp.items() if d == 5)
        expected = 0 if n < 6 else comb(n - 3, 3)
        assert count == expected, (n, count, expected)
        nxt = {}
        for (a, b, c, d), multiplicity in dp.items():
            for st in ((min(6, a + 1), min(6, b + a), c, d),
                       (a, b, min(6, c + b), min(6, d + c))):
                if st[3] <= 5:
                    nxt[st] = nxt.get(st, 0) + multiplicity
        dp = nxt
    print(f'PASS: {compared} exhaustively enumerated words (lengths 0..14); '
          f'{checked_parameters} parameter tuples; 50 exact DP length counts')


if __name__ == '__main__':
    run()
