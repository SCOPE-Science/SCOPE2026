"""Direct semantic test of every binary target subsequence, independent of arch counting."""
from collections import Counter
from itertools import combinations, product
from math import comb
from verify_arch_and_polynomial import formula


def is_subsequence(pattern, source):
    j = 0
    for bit in source:
        if bit == pattern[j]:
            j += 1
            if j == len(pattern):
                return True
    return False


def direct(k):
    n = 2 * k + 2
    targets = tuple(product((0, 1), repeat=k))
    counts = Counter()
    evaluated = 0
    for ones in combinations(range(n), k + 1):
        w = [0] * n
        for j in ones:
            w[j] = 1
        evaluated += 1
        if not all(is_subsequence(t, w) for t in targets):
            continue
        ones_right = sum(w)
        c = 0
        for bit in w:
            if bit == 0:
                c += ones_right
            else:
                ones_right -= 1
        counts[c] += 1
    return dict(counts), evaluated


if __name__ == "__main__":
    total = 0
    for k in range(1, 7):
        observed, n = direct(k)
        total += n
        assert observed == formula(k), (k, observed)
        assert n == comb(2*k+2, k+1)
        print(f"k={k} direct_tested={n} universal={sum(observed.values())}")
    print(f"VERIFY_OK independent_semantic_cases={total}")
