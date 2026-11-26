"""Exact checks for the inversion-defect distributions of maximal consecutive-321-avoiding Lehmer codes.

No external dependencies. The finite checks support, but do not replace, the
infinite coefficient inequalities proved in the accompanying mathematical text.
"""
from collections import Counter
from itertools import permutations
from math import comb


def cbin(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def by_compositions(n):
    """Count legal first/interior/last blocks directly, independent of formulas."""
    count = Counter()

    def extend(blocks, remaining):
        if remaining in (1, 2):
            full = blocks + (remaining,)
            count[sum(k * (k - 1) // 2 for k in full)] += 1
        for b in (2, 3):
            if remaining - b >= 1:
                extend(blocks + (b,), remaining - b)

    for first in (1, 2):
        if n > first:
            extend((first,), n - first)
    return count


def coefficient_formula(n):
    m = n // 2
    out = Counter()
    for j in range(m):
        h = m - 1 - j
        target = 2 * j + (n % 2)
        for t in range(n + 1):
            endpoints_of_size_two = target - 3 * t
            if 0 <= endpoints_of_size_two <= 2:
                out[(m - 1 + j if n % 2 == 0 else m + j)] += (
                    cbin(2, endpoints_of_size_two) * cbin(h + t, t)
                )
    return +out


def recurrence(max_n):
    out = {2: Counter({0: 1}), 3: Counter({1: 2}),
           4: Counter({1: 1, 2: 1})}
    for n in range(5, max_n + 1):
        c = Counter()
        for k, multiplicity in out[n - 2].items():
            c[k + 1] += multiplicity
        for k, multiplicity in out[n - 3].items():
            c[k + 3] += multiplicity
        out[n] = c
    return out


def brute_permutations(n):
    """Use the original consecutive avoidance and coordinate-order definitions."""
    valid = []
    for p in permutations(range(n)):
        if any(p[i] > p[i + 1] > p[i + 2] for i in range(n - 2)):
            continue
        code = tuple(sum(p[j] < p[i] for j in range(i + 1, n))
                     for i in range(n))
        valid.append(code)
    maxima = [p for p in valid if not any(
        q != p and all(pi <= qi for pi, qi in zip(p, q)) for q in valid)]
    return Counter(cbin(n, 2) - sum(p) for p in maxima)


def is_unimodal(count):
    coeffs = [count[i] for i in range(min(count), max(count) + 1)]
    return any(all(coeffs[i] <= coeffs[i + 1] for i in range(p))
               and all(coeffs[i] >= coeffs[i + 1]
                       for i in range(p, len(coeffs) - 1))
               for p in range(len(coeffs)))


def check():
    rec = recurrence(162)
    for n in range(2, 28):
        assert by_compositions(n) == coefficient_formula(n) == rec[n], n
    for n in range(2, 8):
        assert brute_permutations(n) == rec[n], n
    assert [n for n in range(2, 161) if is_unimodal(rec[n])] == (
        list(range(2, 11)) + [12])
    for m in range(5, 81):
        a = rec[2 * m + 1]
        assert a[m + 1] == m - 1
        assert a[m + 2] == m - 2
        assert a[m + 3] == (m - 2) * (m - 3)
    for m in range(7, 81):
        a = rec[2 * m]
        assert a[m + 2] == cbin(m - 2, 2)
        assert a[m + 3] == cbin(m - 3, 2)
        assert a[m + 4] == 2 * cbin(m - 3, 3)
    for n, expected in {
        11: [2, 4, 3, 6, 1], 12: [1, 1, 8, 6, 3, 2],
        13: [2, 5, 4, 12, 4, 1],
        14: [1, 1, 10, 10, 6, 8, 1],
    }.items():
        actual = [rec[n][i] for i in range(min(rec[n]), max(rec[n]) + 1)]
        assert actual == expected, n
    print("BRUTE_PERMUTATION_OK n=2..7")
    print("THREE_METHOD_COEFFICIENTS_OK n=2..27")
    print("UNIMODALITY_WINDOW_OK n=2..160")
    print("ANALYTIC_VALLEY_IDENTITIES_OK odd_n=11..161 even_n=14..160")
    print("VERIFY_OK")

if __name__ == "__main__":
    check()
