#!/usr/bin/env python3
"""Elementary independent checks for balanced singleton-symbol BWT rigidity.

The infinite theorem has a symbolic proof; these checks exercise its boundary
cases and the modular conjugacy formula without assuming the classification.
"""
from math import isqrt


def stable_permutation(word):
    counts = [word.count(x) for x in '012']
    starts = [0, counts[0], counts[0] + counts[1]]
    encountered = [0, 0, 0]
    pi = []
    for char in word:
        c = int(char)
        pi.append(starts[c] + encountered[c])
        encountered[c] += 1
    return pi


def single_cycle(pi):
    x = 0
    for step in range(len(pi)):
        x = pi[x]
        if x == 0:
            return step == len(pi) - 1
    return False


def hamming_to_sorted(word):
    return sum(a != b for a, b in zip(word, sorted(word)))


def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def primitive_two(p):
    if not is_prime(p):
        return False
    seen, x = set(), 1
    while x not in seen:
        seen.add(x)
        x = (2 * x) % p
    return len(seen) == p - 1 and x == 1


def all_unclustered_fixed_content(m):
    n = 2 * m + 1
    out = []
    w = []

    def dfs(z, o, t):
        if len(w) == n:
            out.append(''.join(w))
            return
        for symbol, remaining in [('0', z), ('1', o), ('2', t)]:
            if remaining == 0 or (w and w[-1] == symbol):
                continue
            w.append(symbol)
            if symbol == '0':
                dfs(z - 1, o, t)
            elif symbol == '1':
                dfs(z, o - 1, t)
            else:
                dfs(z, o, t - 1)
            w.pop()

    dfs(m, m, 1)
    return out


def restricted_unclustered_fixed_content(m):
    # Removing the sole 2 creates at most one pair of equal adjacent bits.
    n = 2 * m + 1
    results = set()
    for initial in (0, 1):
        for equal_edge in range(-1, 2 * m - 1):
            binary, bit = [], initial
            for i in range(2 * m):
                binary.append(str(bit))
                if i != equal_edge:
                    bit ^= 1
            b = ''.join(binary)
            if b.count('0') != m:
                continue
            for pos in range(n):
                word = b[:pos] + '2' + b[pos:]
                if all(a != c for a, c in zip(word, word[1:])):
                    results.add(word)
    return results


def fixedpoint_free_words(words):
    return {word for word in words if all(i != x for i, x in enumerate(stable_permutation(word)))}


def expected_words(m):
    return {'10' * (m - 1) + '120', '10' * (m - 2) + '10201'}


def direct_bwt_of_necklace(word):
    pi = stable_permutation(word)
    assert single_cycle(pi)
    x, predecessor_symbols = 0, []
    for _ in range(len(word)):
        predecessor_symbols.append(word[x])
        x = pi[x]
    necklace = ''.join(reversed(predecessor_symbols))
    rotations = sorted(necklace[i:] + necklace[:i] for i in range(len(necklace)))
    return ''.join(row[-1] for row in rotations)


def verify():
    for m in range(2, 11):
        raw = set(all_unclustered_fixed_content(m))
        reduced = restricted_unclustered_fixed_content(m)
        assert raw == reduced, ('exhaustive decomposition', m)
        assert fixedpoint_free_words(raw) == expected_words(m), ('fixed-point rigidity', m)
    for m in range(2, 101):
        words = restricted_unclustered_fixed_content(m)
        assert fixedpoint_free_words(words) == expected_words(m), ('rigidity', m)
        w_a, w_b = '10' * (m - 1) + '120', '10' * (m - 2) + '10201'
        assert hamming_to_sorted(w_a) == (m + 1 if m % 2 == 0 else m + 2)
        assert hamming_to_sorted(w_b) == (m + 2 if m % 2 == 0 else m + 3)
        M = 2 * m + 1
        pi = stable_permutation(w_a)
        inv2 = (M + 1) // 2
        for i in range(M):
            y = (i + 1) % M
            observed = (pi[i] + 1) % M
            predicted = (0 if y == M - 1 else m if y == 0 else (inv2 * y) % M)
            assert observed == predicted, ('modular conjugacy', m, i)
        assert single_cycle(pi) == primitive_two(M), ('cycle criterion', m)
        if m % 2 == 0:
            assert sum(single_cycle(stable_permutation(w)) and hamming_to_sorted(w) == m + 1
                       for w in words) == int(primitive_two(M)), ('sharp count', m)
    for m in (2, 6, 14, 18):
        w = '10' * (m - 1) + '120'
        assert direct_bwt_of_necklace(w) == w
    print('BWT_SINGLETON_RIGIDITY_VERIFY_OK')


if __name__ == '__main__':
    verify()
