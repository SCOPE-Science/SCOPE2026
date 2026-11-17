"""Exact finite tests for balanced-subset L1 extension extremizers.
The universal conclusion follows from the manuscript proof, not enumeration.
"""
from itertools import combinations
from fractions import Fraction
from math import comb

def verify(n):
    assert n >= 2 and n % 2 == 0
    k = n // 2
    subsets = list(combinations(range(n), k))
    m = len(subsets)
    vectors = [tuple(1 if i in s else -1 for s in subsets) for i in range(n)]
    assert m == comb(n, k)
    assert all(sum(v[s] for v in vectors) == 0 for s in range(m))
    pair = [sum(abs(a-b) for a,b in zip(vectors[i],vectors[j]))
            for i in range(n) for j in range(i)]
    D = max(pair)
    assert min(pair) == D
    assert D == 4 * comb(n - 2, k - 1)
    assert D * (n - 1) == n * m
    radius_at_zero = max(sum(abs(x) for x in v) for v in vectors)
    assert radius_at_zero == m
    # Each coordinate has exactly k of each sign; for any scalar center c,
    # k * (|1-c|+|-1-c|) >= n. So any L1 enclosing radius >= m.
    assert Fraction(2 * radius_at_zero, D) == Fraction(2 * (n - 1), n)
    return n, m, D, radius_at_zero

if __name__ == '__main__':
    for n in (2, 4, 6, 8, 10, 12):
        print(verify(n))
    print('PASS: six exact balanced-subset test configurations')
