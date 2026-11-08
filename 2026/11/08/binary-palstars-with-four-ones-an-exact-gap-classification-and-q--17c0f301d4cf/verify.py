"""Separate computational checks for binary four-one palstar classification and enumeration.

Run: python3 verify.py
Requires Python standard library only.
"""
from itertools import combinations
from math import comb


def palindrome_factorable(w):
    """Direct DP over all nonempty even-length palindrome blocks."""
    reachable = [False] * (len(w) + 1)
    reachable[0] = True
    for j in range(2, len(w) + 1, 2):
        reachable[j] = any(
            reachable[i] and w[i:j] == w[i:j][::-1]
            for i in range(0, j, 2)
        )
    return reachable[-1]


def predicted(a, b, c, d, e):
    """Two two-one blocks or one four-one block."""
    alpha, beta = a % 2, e % 2
    two_blocks = (b % 2 == 0 and d % 2 == 0
                  and c >= alpha + beta
                  and (c - alpha - beta) % 2 == 0)
    one_block = (b == d and c % 2 == 0 and alpha == beta)
    return two_blocks or one_block


def exact_formula(m):
    return (4 * m**4 - 4 * m**3 + 2 * m**2 - 8 * m
            + 3 - 3 * ((-1) ** m)) // 24


def bivariate_count(m):
    """Independently count five gaps by direct composition enumeration."""
    L = 2 * m - 4
    total = 0
    for a in range(L + 1):
        for b in range(L - a + 1):
            for c in range(L - a - b + 1):
                for d in range(L - a - b - c + 1):
                    e = L - a - b - c - d
                    total += predicted(a, b, c, d, e)
    return total


def generating_coefficient(m):
    """Coefficient via the independently parametrized two-block and four-block families."""
    n = m - 2
    # Coefficients of (1+x)^2 are (1,2,1).
    A = sum(c * comb(n - i + 4, 4)
            for i, c in enumerate((1, 2, 1)) if n >= i)
    B = comb(n + 3, 3) + (comb(n + 2, 3) if n >= 1 else 0)
    # Intersection: (1+x^2) / [(1-x^2)(1-x)^3]
    I = 0
    for j in range(n // 2 + 1):
        rem = n - 2 * j
        I += comb(rem + 2, 2)
        if rem >= 2:
            I += comb(rem, 2)
    return A + B - I


def main():
    comparisons = 0
    word_count = 0
    for m in range(2, 12):
        n = 2 * m
        observed = 0
        for pos in combinations(range(n), 4):
            chosen = set(pos)
            w = ''.join('1' if i in chosen else '0' for i in range(n))
            a = pos[0]
            b = pos[1] - pos[0] - 1
            c = pos[2] - pos[1] - 1
            d = pos[3] - pos[2] - 1
            e = n - pos[3] - 1
            expected = predicted(a, b, c, d, e)
            actual = palindrome_factorable(w)
            assert actual == expected, (m, w, expected, actual)
            observed += actual
            comparisons += 1
        assert observed == exact_formula(m), (m, observed, exact_formula(m))
        word_count += observed
    for m in range(2, 40):
        if m < 12:
            assert bivariate_count(m) == exact_formula(m)
        assert generating_coefficient(m) == exact_formula(m)
    print(f'VERIFY_OK checked_words={comparisons} positive={word_count} closed_forms=38')


if __name__ == '__main__':
    main()
