"""Independent string/set extension census and direct small-length checks.

Usage: python3 verify_direct.py [ENUMERATION.json]
Python 3 standard library only. No assumptions about the optimum enumeration.
"""
import itertools
import json
import sys
from collections import Counter


def valid(word, n):
    seen = set()
    for i in range(len(word) - n + 1):
        x = word[i:i + n]
        if x == x[::-1] or x in seen or x[::-1] in seen:
            return False
        seen.add(x)
    return True


def direct_census(n, maximum):
    tally = Counter()
    winners = []
    # Normalize by the first bit; complement gives a disjoint second half.
    def visit(word, used):
        tally[len(word)] += 1
        if len(word) == maximum:
            winners.append(word)
        if len(word) == maximum + 1:
            return
        for digit in '01':
            x = word[-n + 1:] + digit
            if x != x[::-1] and x not in used and x[::-1] not in used:
                visit(word + digit, used | {x})
    for letters in itertools.product('01', repeat=n - 1):
        first = '0' + ''.join(letters)
        if first != first[::-1]:
            visit(first, {first})
    return tally, sorted(winners)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'ENUMERATION.json'
    with open(path, encoding='utf-8') as f:
        expected = json.load(f)['spans']
    for n, M in ((6, 26), (7, 48)):
        tally, winners = direct_census(n, M)
        e = expected[str(n)]
        assert winners == e['first_bit_zero_maximizers']
        assert all(2 * tally[l] == e['labeled_length_counts'][str(l)] for l in range(n, M + 2))
        assert tally[M + 1] == 0
        assert all(valid(s, n) for s in winners)
        fixed = sum(s == s[::-1].translate(str.maketrans('01', '10')) for s in winners)
        assert 2 * fixed == e['reverse_complement_fixed_count']
        print(f'span={n} normalized={len(winners)} fixed_normalized={fixed} max+1={tally[M + 1]}')
    # Directly test uncompressed enumeration on small instances,
    # checking the recurrence's reversal and palindrome conventions.
    for n, length in ((4, 8), (5, 14), (6, 15), (7, 13)):
        brute = sum(valid(''.join(x), n) for x in itertools.product('01', repeat=length))
        counter = Counter()
        def dfs(s, seen):
            if len(s) == length:
                counter['total'] += 1
                return
            for bit in '01':
                t = s[-n + 1:] + bit
                if t != t[::-1] and t not in seen and t[::-1] not in seen:
                    dfs(s + bit, seen | {t})
        for seq in itertools.product('01', repeat=n):
            s = ''.join(seq)
            if s != s[::-1]:
                dfs(s, {s})
        assert brute == counter['total'], f'short exhaustive check failed at {n}, {length}'
    print('VERIFY_DIRECT_OK')


if __name__ == '__main__':
    main()
