#!/usr/bin/env python3
"""Independent exhaustive substring-frequency test of a periodic net-frequency law."""
from collections import Counter
from itertools import product


def primitive(s):
    return not any(len(s) % d == 0 and s == s[:d] * (len(s) // d)
                   for d in range(1, len(s)))


def net_occurrences(text):
    frequencies = Counter(text[i:j] for i in range(len(text))
                          for j in range(i + 1, len(text) + 1))
    result = []
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            sub = text[i:j]
            if (frequencies[sub] >= 2 and
                (i == 0 or frequencies[text[i - 1:j]] == 1) and
                (j == len(text) or frequencies[text[i:j + 1]] == 1)):
                result.append((i, j, sub))
    return result


def main():
    cases = 0
    for alphabet, max_length in [('01', 7), ('012', 5), ('0123', 4)]:
        for length in range(1, max_length + 1):
            for tup in product(alphabet, repeat=length):
                root = ''.join(tup)
                if not primitive(root):
                    continue
                for exponent in (3, 4, 5):
                    T = root * exponent
                    p, N = len(root), len(T)
                    actual = net_occurrences(T)
                    expected = [(0, N - p, root * (exponent - 1)),
                                (p, N, root * (exponent - 1))]
                    assert actual == expected, (root, exponent, actual, expected)
                    cases += 1
    assert net_occurrences('00100' * 2) == [
        (0, 5, '00100'), (3, 6, '000'),
        (4, 7, '000'), (5, 10, '00100')]
    print(f'PASS brute-force: {cases} primitive-root/exponent cases; square sharpness verified')

if __name__ == '__main__':
    main()
