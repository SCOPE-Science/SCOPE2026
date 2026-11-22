#!/usr/bin/env python3
"""Exact finite checks for the Fibonacci-source length-two tandem-duplication law.

Requires Python 3 standard library only. Enumeration is evidence for the
finite inputs checked; the all-length claim is established by the proof.
"""
from collections import Counter
from itertools import product


def fibonacci_source(n):
    for w in product((0, 1), repeat=n):
        if not any(w[i] == w[i+1] == 1 for i in range(n-1)):
            yield w


def direct_sphere(w):
    n = len(w)
    return {w[:i] + w[i:i+2] + w[i:i+2] + w[i+2:]
            for i in range(n-1)}


def derivative_count(w):
    return 1 + sum(w[i] != w[i+2] for i in range(len(w)-2))


def polys_up_to(N):
    # A_n(z) coefficient array, where exponent s counts |D_2(w)| - 1.
    a = {2: [3], 3: [3, 2], 4: [3, 4, 1]}
    for n in range(5, N+1):
        result = [0] * (max(len(a[n-1]), len(a[n-2]), len(a[n-3])+2))
        for index, coef in enumerate(a[n-1]): result[index] += coef
        for index, coef in enumerate(a[n-2]): result[index] += coef
        for index, coef in enumerate(a[n-3]):
            result[index+2] += coef
            result[index] -= coef
        while result and result[-1] == 0:
            result.pop()
        assert all(x >= 0 for x in result)
        a[n] = result
    return a


def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a+b
    return a


def test():
    polys = polys_up_to(60)
    tested = 0
    for n in range(2, 19):
        actual = Counter()
        for word in fibonacci_source(n):
            s = len(direct_sphere(word))
            assert s == derivative_count(word), (n, word, s)
            actual[s-1] += 1
            tested += 1
        observed = [actual[j] for j in range(max(actual)+1)]
        assert observed == polys[n], (n, observed, polys[n])
    for n in range(2, 61):
        p = polys[n]
        assert sum(p) == fib(n+2), n
        assert p[0] == 3, n
        L = n - 2
        assert len(p)-1 == (2*L+2)//3, n
        assert p[-1] == (2 if n % 3 == 0 else
                         1 if n % 3 == 1 else (n+7)//3), n
    assert polys[6] == [3,8,8,2]
    assert polys[10] == [3,16,40,44,32,8,1]
    print(f'VERIFY_OK enumerated_sources={tested} exhaustive_lengths=2..18 recurrence_lengths=2..60')

if __name__ == '__main__':
    test()
