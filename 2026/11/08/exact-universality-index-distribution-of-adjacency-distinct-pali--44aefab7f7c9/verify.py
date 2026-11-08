"""Reproduce the coefficient law for proper palindromic subsequence-universal words.

The alphabet is the labeled set range(q). All comparisons use integer arithmetic.
"""
from itertools import product
from collections import Counter
from math import factorial, comb


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def coefficients(q, H):
    """Coefficient dicts [u^k] [z^h] F_q(z,u), for h=0..H."""
    assert q >= 2
    D = [1]
    for j in range(q - 1):
        D = multiply(D, [1, -j])
    Cs = []
    for s in range(1, q):
        C = [factorial(q - 1) // factorial(q - s)]
        for j in range(s, q - 1):
            C = multiply(C, [1, -j])
        C = [0] * s + C
        Cs.append(C)
    def get(a, h):
        return a[h] if 0 <= h < len(a) else 0
    N0 = [q * get(D, h) + q * (q - 1) * sum(get(c, h) for c in Cs)
          - q * get(Cs[-1], h) for h in range(q)]
    N1 = [q * get(Cs[-1], h) for h in range(q)]
    alpha = (q - 1) * factorial(q - 1)
    out = []
    for h in range(H + 1):
        row = Counter()
        if h < q:
            row[0] += N0[h]
            row[1] += N1[h]
        for j in range(1, min(h, q - 1) + 1):
            for k, v in out[h - j].items():
                row[k] -= D[j] * v
        if h >= q:
            for k, v in out[h - q].items():
                row[k + 2] += alpha * v
        row = {k: v for k, v in row.items() if v}
        assert all(v > 0 for v in row.values()), (q, h, row)
        assert sum(row.values()) == q * (q - 1) ** h, (q, h, row)
        out.append(row)
    return out


def is_subsequence(pattern, word):
    i = 0
    for symbol in word:
        if i < len(pattern) and symbol == pattern[i]:
            i += 1
    return i == len(pattern)


def brute_index(word, q):
    for k in range(len(word) // q, 0, -1):
        if all(is_subsequence(t, word) for t in product(range(q), repeat=k)):
            return k
    return 0


def greedy_index(word, q):
    seen = set()
    arches = 0
    for x in word:
        seen.add(x)
        if len(seen) == q:
            arches += 1
            seen.clear()
    return arches, len(seen)


def check():
    brute_cases = 0
    direct_patterns = 0
    for q, H in [(2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]:
        pred = coefficients(q, H)
        for h in range(H + 1):
            counts = Counter()
            if h == 0:
                for middle in range(q):
                    w = (middle,)
                    counts[brute_index(w, q)] += 1
                    brute_cases += 1
            else:
                for v in product(range(q), repeat=h):
                    if any(v[j] == v[j + 1] for j in range(h - 1)):
                        continue
                    arches, rest_size = greedy_index(v, q)
                    for middle in range(q):
                        if middle == v[-1]:
                            continue
                        w = v + (middle,) + v[::-1]
                        actual = brute_index(w, q)
                        # Recompute the rest directly from the original half-word.
                        if rest_size:
                            seen = set()
                            for letter in v:
                                seen.add(letter)
                                if len(seen) == q:
                                    seen.clear()
                            predicted = 2 * arches + int(len(seen) == q - 1 and middle not in seen)
                        else:
                            predicted = 2 * arches
                        assert actual == predicted, (q, h, v, middle, actual, predicted)
                        counts[actual] += 1
                        brute_cases += 1
            assert dict(counts) == pred[h], (q, h, dict(counts), pred[h])
    extremal_checks = 0
    for q in range(2, 9):
        arr = coefficients(q, 7 * q)
        alpha = (q - 1) * factorial(q - 1)
        for k in range(1, 8):
            if k % 2 == 0:
                m = k // 2
                hmin = m * q
                count = factorial(q) * alpha ** (m - 1) * (q - 1)
            else:
                m = k // 2
                hmin = (m + 1) * q - 1
                count = factorial(q) * alpha ** m
            assert arr[hmin].get(k, 0) == count, (q, k, hmin)
            assert all(arr[h].get(t, 0) == 0 for h in range(hmin) for t in range(k, k + 15)), (q, k)
            extremal_checks += 1
    # The simple ternary specialization F_3 = 3(1+z+2uz^2)/(1-z-4u^2z^3).
    arr3 = coefficients(3, 50)
    for h in range(51):
        for k, value in arr3[h].items():
            if k % 2 == 1:
                m = (k - 1) // 2
                expected = (6 * 4 ** m * comb(h - 2 * m - 2, m)
                            if h - 2 * m - 2 >= m else 0)
            else:
                m = k // 2
                expected = 3 * 4 ** m * (
                    (comb(h - 2 * m, m) if h - 2 * m >= m else 0) +
                    (comb(h - 2 * m - 1, m) if h - 2 * m - 1 >= m else 0))
            assert value == expected, (h, k, value, expected)
    print(f"VERIFY_OK q=2..8 half_length<=56 brute_palindromes={brute_cases} "
          f"extremal_checks={extremal_checks} ternary_coefficients=0..50")


if __name__ == '__main__':
    check()
