"""Checks of the exact three-one longest-unbordered-factor formula and limit moments.

Usage: python3 VERIFY.py
Requires only Python 3's standard library.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb


def gap_value(a, b, c, d):
    candidates = [1 + max(a, b, c, d)]
    if a > b:
        candidates.append(a + b + 2)
    if a > c:
        candidates.append(a + b + c + 3)
    if b != c:
        candidates.append(b + c + 2)
    if d > b:
        candidates.append(b + c + d + 3)
    if d > c:
        candidates.append(c + d + 2)
    return max(candidates)


def border_array_longest_unbordered(word):
    """Independent prefix-function calculation for every suffix."""
    n = len(word)
    best = 0
    for i in range(n):
        suffix = word[i:]
        pi = [0] * len(suffix)
        if best < 1:
            best = 1
        for j in range(1, len(suffix)):
            k = pi[j - 1]
            while k and suffix[j] != suffix[k]:
                k = pi[k - 1]
            if suffix[j] == suffix[k]:
                k += 1
            pi[j] = k
            if k == 0 and j + 1 > best:
                best = j + 1
    return best


def verify_direct(limit=30):
    tested = 0
    for n in range(3, limit + 1):
        for i, j, k in combinations(range(n), 3):
            a, b, c, d = i, j - i - 1, k - j - 1, n - k - 1
            word = '0' * a + '1' + '0' * b + '1' + '0' * c + '1' + '0' * d
            predicted = gap_value(a, b, c, d)
            actual = border_array_longest_unbordered(word)
            assert predicted == actual, (n, a, b, c, d, predicted, actual)
            tested += 1
    assert tested == comb(limit + 1, 4)
    print('DIRECT_PREFIX_FUNCTION_OK', tested)


def verify_minima(limit=64):
    for n in range(5, limit + 1):
        m = n // 4
        sharp = m + 1
        minima = []
        for a in range(n - 2):
            for b in range(n - a - 2):
                for c in range(n - a - b - 2):
                    d = n - 3 - a - b - c
                    if gap_value(a, b, c, d) == sharp:
                        minima.append((a, b, c, d))
        predicted = [(a, m, m, n - 3 - 2 * m - a)
                     for a in range(m + 1)
                     if 0 <= n - 3 - 2 * m - a <= m]
        assert sorted(minima) == sorted(predicted), (n, minima, predicted)
        assert minima
    assert gap_value(0, 0, 0, 0) == 1
    assert min(gap_value(a,b,c,1-a-b-c) for a in range(2)
               for b in range(2-a) for c in range(2-a-b)) == 3
    print('SHARP_MINIMUM_CLASSIFICATION_OK', limit)


def limiting_piecewise(rank):
    # rank 0 is the greatest simplex coordinate. Names a,b,c,d.
    if rank['a'] < rank['c'] and rank['d'] < rank['b']:
        constant, weights = Q(1), {('a' if rank['a'] > rank['d'] else 'd'): Q(-1)}
    elif rank['a'] < rank['c']:
        constant, weights = Q(1), {'d': Q(-1)}
    elif rank['d'] < rank['b']:
        constant, weights = Q(1), {'a': Q(-1)}
    else:
        constant, weights = Q(0), {'b': Q(1), 'c': Q(1)}
    # Descending sorted simplex coordinates X_(j)=sum_{i=j}^4 T_i/i.
    # The constant 1 is sum(T_i).
    q = [constant] * 4
    for name, value in weights.items():
        for i in range(rank[name], 4):
            q[i] += value / Q(i + 1)
    return q


def verify_moments():
    first = Q(0)
    second = Q(0)
    for ordering in permutations('abcd'):
        rank = {letter: j for j, letter in enumerate(ordering)}
        q = limiting_piecewise(rank)
        first += sum(q) / 4
        second += (sum(q) ** 2 + sum(v * v for v in q)) / 20
    first /= 24
    second /= 24
    variance = second - first ** 2
    assert first == Q(157, 192), first
    assert second == Q(3929, 5760), second
    assert variance == Q(2483, 184320), variance
    print('EXACT_DIRICHLET_MOMENTS_OK', first, second, variance)


if __name__ == '__main__':
    verify_direct()
    verify_minima()
    verify_moments()
