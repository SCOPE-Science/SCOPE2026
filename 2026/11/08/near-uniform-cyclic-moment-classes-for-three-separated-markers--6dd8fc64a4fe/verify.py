"""Direct independent enumeration of three-one circular separation moment classes.

Usage: python verify.py
"""
from collections import Counter
from itertools import combinations
from math import comb


def direct_counts(n, h):
    out = Counter()
    for a, b, c in combinations(range(n), 3):
        if min(b-a, c-b, n-c+a) < h:
            continue
        out[(a+b+c) % n] += 1
    return [out[s] for s in range(n)]


def exact_counts(n, h):
    q = comb(n-3*h+2, 2)
    if n % 3:
        assert q % 3 == 0
        return [q//3] * n
    assert q % 3 == 1
    return [(q-1)//3 + (s % 3 == 0) for s in range(n)]


def main():
    count = 0
    for n in range(6, 43):
        for h in range(2, n//3+1):
            actual = direct_counts(n, h)
            expected = exact_counts(n, h)
            assert actual == expected, (n, h, actual, expected)
            assert sum(actual) == n * comb(n-3*h+2, 2)//3
            count += 1
    print(f'VERIFY_OK {count} independent parameter checks (6 <= n <= 42, h >= 2)')


if __name__ == '__main__':
    main()
