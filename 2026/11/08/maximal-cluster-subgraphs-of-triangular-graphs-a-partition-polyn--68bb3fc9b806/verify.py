"""Exact labeled-block recurrence and size-spectrum checks (standard-library Python 3)."""
from math import comb, factorial
from collections import Counter


def polynomial(n):
    # dp[j] counts full-cover partitions of j labeled base vertices by edge cardinality.
    dp = [Counter({0: 1})]
    for j in range(1, n + 1):
        counts = Counter()
        for k in range(2, j + 1):
            edges, multiplicity = (1, 1) if k == 2 else ((3, 1) if k == 3 else (k - 1, k))
            for old_size, number in dp[j - k].items():
                counts[old_size + edges] += comb(j - 1, k - 1) * multiplicity * number
        dp.append(counts)
    result = dp[n].copy()
    # Exceptional family: exactly one untouched base vertex and triangles elsewhere.
    if n >= 4 and (n - 1) % 3 == 0:
        t = (n - 1) // 3
        result[3*t] += factorial(n) // (factorial(3)**t * factorial(t))
    return result


def expected_support(n):
    if n == 3:
        return {3}
    if n % 2 == 0:
        base = set(range(n // 2, n))
    else:
        base = set(range((n + 3) // 2, n))
    if n % 3 == 0:
        base.add(n)
    return base


def main():
    examples = {3:{3:1},4:{2:3,3:8},5:{4:15},
                6:{3:15,4:60,5:6,6:10},7:{5:210,6:217},
                8:{4:105,5:840,6:728,7:568}}
    for n in range(3, 26):
        counts = polynomial(n)
        assert set(counts) == expected_support(n), (n, counts)
        if n in examples:
            assert counts == examples[n], (n, counts)
        assert (len(counts) == 1) == (n in (3, 5))
    print('RECURRENCE_OK n=3..25 support=PASS pure_cases=3,5 examples=PASS')


if __name__ == '__main__':
    main()
