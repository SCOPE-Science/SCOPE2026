"""Independent finite replay for the mixed-length palindromic-duplication theorem.
No external packages are required. Exact tuples, no randomness or numerical tolerances.
"""
from itertools import product
from collections import defaultdict


def duplicate(word, length, start):
    assert 1 <= length <= len(word)
    assert 0 <= start <= len(word) - length
    return word[:start + length] + word[start:start + length][::-1] + word[start + length:]


def histories(word, first_length, second_length):
    assert 1 <= first_length <= len(word)
    assert 1 <= second_length <= len(word) + first_length
    for first_start in range(len(word) - first_length + 1):
        intermediate = duplicate(word, first_length, first_start)
        for second_start in range(len(intermediate) - second_length + 1):
            yield (first_start, second_start), duplicate(intermediate, second_length, second_start)


def original_gaps(descendant, n):
    # For the canonical distinct-letter source (0,...,n-1), only positions
    # of first occurrences are used to separate the inserted runs.
    positions = [descendant.index(i) for i in range(n)]
    assert positions == sorted(positions)
    assert positions[0] == 0
    return [descendant[positions[i] + 1:(positions[i + 1] if i < n - 1 else len(descendant))]
            for i in range(n)]


def check_distinct_sources(max_n=11):
    count = 0
    for n in range(1, max_n + 1):
        source = tuple(range(n))
        for k in range(1, n + 1):
            for ell in range(2, n + k + 1):
                if ell == k:
                    continue
                mapping = dict(histories(source, k, ell))
                target = (n - k + 1) * (n + k - ell + 1)
                assert len(mapping) == target
                descendants = set(mapping.values())
                assert len(descendants) == target, (n, k, ell)
                for word in descendants:
                    gaps = original_gaps(word, n)
                    nonempty = [len(g) for g in gaps if len(g)]
                    assert nonempty == [k + ell] or sorted(nonempty) == sorted([k, ell]), (n, k, ell, nonempty)
                count += 1
    return count


def check_noninjectivity_at_unit_copy():
    n, k, ell = 5, 3, 1
    hist = list(histories(tuple(range(n)), k, ell))
    assert len({z for _, z in hist}) < len(hist)


def check_ambiguous_same_length():
    source = tuple(range(5))
    hist = list(histories(source, 2, 2))
    assert len({z for _, z in hist}) < len(hist)


def check_small_alphabets():
    # A separate check that the operation-count upper bound holds for words
    # with repeated symbols (universal bound is immediate mathematically).
    count = 0
    for n in range(1, 7):
        for source in product(range(2), repeat=n):
            for k in range(1, n + 1):
                for ell in range(2, n + k + 1):
                    if ell == k: continue
                    total = (n - k + 1) * (n + k - ell + 1)
                    assert len({z for _, z in histories(source, k, ell)}) <= total
                    count += 1
    return count


if __name__ == '__main__':
    n = check_distinct_sources()
    m = check_small_alphabets()
    check_noninjectivity_at_unit_copy()
    check_ambiguous_same_length()
    print(f'PASS: {n} canonical distinct-letter parameter triples (n<=11)')
    print(f'PASS: {m} repeated-symbol binary parameter/word instances (n<=6)')
    print('PASS: the excluded length-one and equal-length boundaries can collide')
