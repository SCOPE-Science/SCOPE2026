"""Reproducible exhaustive tests for exactly two scattered occurrences.

Only Python 3 standard-library modules are required. All counts are of indexed
subsequence embeddings, not distinct subsequence strings or contiguous factors.
"""
from collections import defaultdict
from itertools import product


def embeddings(word, pattern):
    """Independent index-tuple backtracking for two-occurrence witnesses."""
    paths = [()]
    for target in pattern:
        nxt = []
        for path in paths:
            start = path[-1] + 1 if path else 0
            for j in range(start, len(word)):
                if word[j] == target:
                    nxt.append(path + (j,))
        paths = nxt
    return paths


def occurrences_capped(word, pattern):
    """A separate, early-capped dynamic program; 3 means at least three."""
    m = len(pattern)
    counts = [1] + [0] * m
    for letter in word:
        for j in range(m - 1, -1, -1):
            if letter == pattern[j]:
                counts[j + 1] = min(3, counts[j + 1] + counts[j])
    return counts[m]


def gap_sizes(q, pattern, fork):
    """Two boundaries, m-1 ordinary gaps and a single fork gap."""
    m = len(pattern)
    sizes = [q - 1, q - 1]
    sizes += [q - len({pattern[i], pattern[i + 1]})
              for i in range(m - 1)]
    forbidden = {pattern[fork]}
    if fork:
        forbidden.add(pattern[fork - 1])
    if fork + 1 < m:
        forbidden.add(pattern[fork + 1])
    sizes.append(q - len(forbidden))
    return sizes


def coefficient(gaps, extra_length):
    """Coefficient of z^extra_length in a product of geometric series."""
    if extra_length < 0:
        return 0
    coeff = [1] + [0] * extra_length
    for g in gaps:
        for k in range(1, extra_length + 1):
            coeff[k] += g * coeff[k - 1]
    return coeff[extra_length]


def predicted_forks(q, pattern, n):
    return [coefficient(gap_sizes(q, pattern, j), n - len(pattern) - 1)
            for j in range(len(pattern))]


def main():
    instances = 0
    enumerated_words = 0
    witnesses = 0
    for q in (2, 3, 4):
        for m in range(2, 5 if q < 4 else 4):
            cap = {2: 10, 3: 8, 4: 7}[q]
            for p in product(range(q), repeat=m):
                if any(p[i] == p[i + 1] for i in range(m - 1)):
                    continue
                palindrome_triples = sum(p[i - 1] == p[i + 1]
                                         for i in range(1, m - 1))
                for n in range(m, cap + 1):
                    observed = 0
                    fork_hist = defaultdict(int)
                    for word in product(range(q), repeat=n):
                        if occurrences_capped(word, p) != 2:
                            continue
                        observed += 1
                        paths = embeddings(word, p)
                        assert len(paths) == 2, (q, p, n, word, paths)
                        fork_coordinates = [i for i, (a, b) in
                                            enumerate(zip(*paths)) if a != b]
                        assert len(fork_coordinates) == 1
                        fork_hist[fork_coordinates[0]] += 1
                        witnesses += 1
                    expected = predicted_forks(q, p, n)
                    assert observed == sum(expected), (q, p, n, observed, expected)
                    assert [fork_hist[j] for j in range(m)] == expected, (
                        q, p, n, fork_hist, expected)
                    if n == m + 2:
                        exact = m * m * (q - 2) + m * (2 * q - 3) + palindrome_triples + 2
                        assert observed == exact
                    instances += 1
                    enumerated_words += q ** n
        print('alphabet', q, 'cumulative_instances', instances,
              'cumulative_words', enumerated_words,
              'two_occurrence_witnesses', witnesses)

    for q, p in ((3, (0, 1, 2)), (3, (0, 1, 0)),
                 (4, (0, 1, 2, 3)), (4, (0, 1, 0, 1))):
        print('example', q, ''.join(map(str, p)),
              [sum(predicted_forks(q, p, n))
               for n in range(len(p) + 1, len(p) + 6)])

    print('PASS', instances, 'instances', enumerated_words,
          'host words', witnesses, 'two-occurrence embeddings classified')


if __name__ == '__main__':
    main()
