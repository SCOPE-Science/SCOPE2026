#!/usr/bin/env python3
"""Independent one-letter extension and split-LCS verification."""
from itertools import product


def embeds(pattern, text):
    state = 0
    for c in text:
        if state < len(pattern) and c == pattern[state]:
            state += 1
    return state == len(pattern)


def roots_from_cuts(text):
    roots = set()
    for cut in range(1, len(text)):
        left, right = text[:cut], text[cut:]
        smaller = min(len(left), len(right))
        for k in range(1, smaller + 1):
            for positions in __import__('itertools').combinations(range(len(left)), k):
                x = ''.join(left[i] for i in positions)
                if embeds(x, right):
                    roots.add(x)
    return roots


def has_single_extension(x, w):
    for i in range(len(x) + 1):
        for c in '01':
            root = x[:i] + c + x[i:]
            if embeds(root + root, w):
                return True
    return False


def qualifying(w):
    roots = roots_from_cuts(w)
    longest = max(map(len, roots), default=0)
    return sorted(x for x in roots if len(set(x)) == 2 and
                  len(x) < longest and not has_single_extension(x, w))


def main():
    hits = []
    for n in range(2, 8):
        for tpl in product('01', repeat=n):
            w = ''.join(tpl)
            x = qualifying(w)
            if x:
                assert n == 7
                hits.append(w)
        print('length', n, 'cumulative_hits', len(hits))
    expected = ['0010101', '0101001', '0101011', '0110101',
                '1001010', '1010100', '1010110', '1101010']
    assert hits == expected
    for m in range(3, 41):
        w = '0' * m + '101' + '0' * m
        all_roots = roots_from_cuts(w) if m <= 8 else None
        assert embeds('1010', w)
        assert not has_single_extension('10', w)
        assert embeds('0' * (2 * m), w)
        if all_roots is not None:
            assert max(map(len, all_roots)) == m
    print('length-seven words', hits)
    print('family m=3..40: mixed root 10 is not single-letter extendable;')
    print('m=3..8: all roots independently enumerated, maximum root length m')
    print('PASS: independent maximality and witness verification')


if __name__ == '__main__':
    main()
