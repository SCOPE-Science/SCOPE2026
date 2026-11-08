"""Reproduce exact counts of minimal common supersequences of opposite binary runs.
Public science-only checks; Python 3.9+ standard library.
"""
from itertools import combinations, product
from math import comb


def is_subsequence(pattern, text):
    j = 0
    for letter in text:
        if j < len(pattern) and letter == pattern[j]:
            j += 1
    return j == len(pattern)


def is_minimal_common_supersequence(first, second, word):
    if not is_subsequence(first, word) or not is_subsequence(second, word):
        return False
    return all(not (is_subsequence(first, word[:i] + word[i + 1:])
                    and is_subsequence(second, word[:i] + word[i + 1:]))
               for i in range(len(word)))


def fixed_weight_words(num_zero, num_one):
    length = num_zero + num_one
    for one_places in combinations(range(length), num_one):
        s = ['0'] * length
        for p in one_places:
            s[p] = '1'
        yield ''.join(s)


def classified(a, b):
    result = set()
    for t in range(1, b + 1):
        left = [s for s in fixed_weight_words(a, b - t) if s[-1] == '0']
        right = [s for s in fixed_weight_words(a, b - t) if s[0] == '0']
        result.update(u + '1' * t + v for u in left for v in right)
    for t in range(1, a + 1):
        left = [s for s in fixed_weight_words(a - t, b) if s[-1] == '1']
        right = [s for s in fixed_weight_words(a - t, b) if s[0] == '1']
        result.update(u + '0' * t + v for u in left for v in right)
    return result


def predicted_length_count(a, b, n):
    t = 2 * (a + b) - n
    return (comb(a + b - t - 1, a - 1)**2 if 1 <= t <= b else 0) + \
           (comb(a + b - t - 1, b - 1)**2 if 1 <= t <= a else 0)


def brute_all(a, b):
    first, second = '0' * a + '1' * b, '1' * b + '0' * a
    all_words = set()
    start = 2 * (a + b) - max(a, b)
    stop = 2 * (a + b)
    for n in range(start, stop):
        for bits in product('01', repeat=n):
            word = ''.join(bits)
            if is_minimal_common_supersequence(first, second, word):
                all_words.add(word)
    return all_words


def main():
    total = 0
    for a in range(1, 5):
        for b in range(1, 5):
            from_classification = classified(a, b)
            from_exhaustion = brute_all(a, b)
            assert from_classification == from_exhaustion, (a, b,
                    len(from_classification - from_exhaustion),
                    len(from_exhaustion - from_classification))
            for n in range(2 * (a + b) - max(a, b), 2 * (a + b)):
                actual = sum(len(w) == n for w in from_exhaustion)
                assert actual == predicted_length_count(a, b, n), (a, b, n, actual)
            max_words = sum(len(w) == 2*(a+b)-1 for w in from_exhaustion)
            assert max_words == 2 * comb(a + b - 2, a - 1)**2
            total += len(from_exhaustion)
    # Second, very different cross-check: generate all possible two-string merges,
    # then apply deletion minimality for larger unbalanced parameters.
    from functools import lru_cache
    def merged(x, y):
        @lru_cache(None)
        def visit(i, j):
            if i == len(x): return {y[j:]}
            if j == len(y): return {x[i:]}
            z = {x[i] + v for v in visit(i+1, j)}
            z |= {y[j] + v for v in visit(i, j+1)}
            if x[i] == y[j]:
                z |= {x[i] + v for v in visit(i+1,j+1)}
            return z
        return visit(0, 0)
    for a,b in [(1, 6), (2, 5), (3, 5), (5, 3)]:
        x,y = '0'*a+'1'*b,'1'*b+'0'*a
        got = {s for s in merged(x,y) if is_minimal_common_supersequence(x,y,s)}
        assert got == classified(a,b),(a,b,len(got),len(classified(a,b)))
    print('OPPOSITE_RUN_MCS_VERIFY_OK', '16 exhaustive parameter pairs',
          '4 interleaving checks', 'total first-grid words', total)


if __name__ == '__main__':
    main()
