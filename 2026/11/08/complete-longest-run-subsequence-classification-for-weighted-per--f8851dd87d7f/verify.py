"""Independent finite tests for optimal longest run subsequences of run-permutation powers.

Usage: python3 verify.py
Only the Python standard library is needed.
"""
from itertools import product, combinations, permutations
from math import comb


def make_word(weights, copies):
    return tuple(x for _ in range(copies) for i, a in enumerate(weights) for x in [i] * a)


def optimum_dp(word, q):
    # State (used-letter mask, final symbol) -> best length.
    d = {(0, -1): 0}
    for x in word:
        nd = d.copy()
        for (mask, last), length in d.items():
            if last == x:
                key = (mask, x)
            elif mask & (1 << x):
                continue
            else:
                key = (mask | (1 << x), x)
            nd[key] = max(nd.get(key, -1), length + 1)
        d = nd
    return max(d.values())


def embeds(pattern, word):
    j = 0
    for x in word:
        if j < len(pattern) and x == pattern[j]:
            j += 1
    return j == len(pattern)


def compositions(n, m):
    if m == 0:
        if n == 0:
            yield ()
        return
    if m == 1:
        if n >= 1:
            yield (n,)
        return
    for first in range(1, n - m + 2):
        for rest in compositions(n - first, m - 1):
            yield (first,) + rest


def all_length_optimal_words_bruteforce(word, weights, length):
    q = len(weights)
    result = set()
    for m in range(1, q + 1):
        for indices in permutations(range(q), m):
            max_counts = tuple(word.count(c) for c in indices)
            for counts in compositions(length, m):
                if any(counts[j] > max_counts[j] for j in range(m)):
                    continue
                candidate = tuple(x for j, x in enumerate(indices) for _ in range(counts[j]))
                if embeds(candidate, word):
                    result.add(candidate)
    return result


def formula_optimal_words(weights, k):
    q = len(weights)
    M = max(weights)
    heavy = [i for i, a in enumerate(weights) if a == M]
    res = set()
    # Nonnegative weak compositions of k-1 among heavy symbols.
    for weak in compositions(k - 1 + len(heavy), len(heavy)):
        extra = [0] * q
        for i, val in zip(heavy, weak):
            extra[i] = val - 1
        res.add(tuple(i for i, a in enumerate(weights) for _ in range(a * (1 + extra[i]))))
    return res


def run_checks():
    length_cases = 0
    unique_solution_cases = 0
    embeddings = 0
    for q in range(2, 6):
        for weights in product(range(1, 4), repeat=q):
            for k in range(1, 5):
                w = make_word(weights, k)
                expected = sum(weights) + (k - 1) * max(weights)
                actual = optimum_dp(w, q)
                assert actual == expected, (weights, k, expected, actual)
                length_cases += 1
                r = sum(a == max(weights) for a in weights)
                predicted = formula_optimal_words(weights, k)
                assert len(predicted) == comb(k + r - 2, r - 1)
                for x in predicted:
                    assert len(x) == expected and embeds(x, w), (weights, k, x)
                    embeddings += 1
    # Separate explicit enumeration of ALL distinct feasible run-subsequence strings
    # at optimal length, not relying on the length-DP's choice of final symbol.
    for q in range(2, 5):
        for weights in product(range(1, 3), repeat=q):
            for k in range(1, 4):
                w = make_word(weights, k)
                target = sum(weights) + (k - 1) * max(weights)
                actual = all_length_optimal_words_bruteforce(w, weights, target)
                predicted = formula_optimal_words(weights, k)
                assert actual == predicted, (weights, k, actual, predicted)
                unique_solution_cases += 1
    print('VERIFY_OK')
    print(f'dynamic_programming_cases={length_cases}')
    print(f'exhaustive_distinct_optimal_language_cases={unique_solution_cases}')
    print(f'constructive_replays={embeddings}')


if __name__ == '__main__':
    run_checks()
