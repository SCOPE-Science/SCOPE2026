"""Exhaustive short-input oracle for opposite two-run shortest common supersequences."""
from itertools import product
from math import comb


def is_subsequence(needle, haystack):
    it = iter(haystack)
    return all(any(ch == target for ch in it) for target in needle)


def formula(a, b, c, d):
    zero = (comb(d - a + b, b) if a <= d else comb(a - d + c, c))
    one = (comb(c - b + a, a) if b <= c else comb(b - c + d, d))
    r0, r1 = min(a, d), min(b, c)
    return (zero if r0 >= r1 else 0) + (one if r1 >= r0 else 0)


def run():
    checked = 0
    total_words = 0
    for n in range(4, 14):
        for a in range(1, n - 2):
            for b in range(1, n - a - 1):
                for c in range(1, n - a - b):
                    d = n - a - b - c
                    u, v = '0' * a + '1' * b, '1' * c + '0' * d
                    l = n - max(min(a, d), min(b, c))
                    count = 0
                    for letters in product('01', repeat=l):
                        w = ''.join(letters)
                        total_words += 1
                        if is_subsequence(u, w) and is_subsequence(v, w):
                            count += 1
                    assert count == formula(a, b, c, d), (a, b, c, d, count)
                    checked += 1
    print(f'LITERAL_OK tuples={checked} tested_words={total_words} max_total_length=13')


if __name__ == '__main__':
    run()
