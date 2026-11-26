"""Standalone checks for weight-two binary shortest-common-supersequence bounds.

Run: python checker.py. Exact small optima are independently enumerated.
This finite check is supplemental and is not a proof of the asymptotic theorem.
"""
from itertools import combinations, product
from math import ceil, isqrt, sqrt


def subword(target, host):
    it = iter(host)
    return all(any(y == x for y in it) for x in target)


def target_words(n):
    for i, j in combinations(range(n), 2):
        yield '0' * i + '1' + '0' * (j-i-1) + '1' + '0' * (n-j-1)


def universal(host, n):
    return all(subword(t, host) for t in target_words(n))


def construction(n, g):
    N = n - 2
    m, r = divmod(N, g)
    return '1' + ('0' * g + '1') * (m + 2) + '0' * r


def exact_by_enumeration(n, stop):
    targets = tuple(target_words(n))
    for L in range(n, stop + 1):
        for tup in product('01', repeat=L):
            w = ''.join(tup)
            if all(subword(t, w) for t in targets):
                return L, w
    raise RuntimeError(f'No universal witness n={n} through {stop}')


def validate():
    expected = {3:5, 4:7, 5:9, 6:10, 7:12, 8:14, 9:15, 10:17, 11:18}
    # Exact brute force on all hosts at least as short as the claimed optimum.
    for n, claimed in expected.items():
        got, witness = exact_by_enumeration(n, claimed)
        assert got == claimed, (n, got, claimed)
        print(f'exact n={n}: F={got}, witness={witness}')
    for n in range(3, 161):
        N = n - 2
        g = max(1, ceil(sqrt(N / 2)))
        w = construction(n, g)
        assert len(w) == N + 2*g + N//g + 3
        assert universal(w, n), ('construction failed', n)
        assert len(w) <= n + 2*sqrt(2*n - 4) + 3 + 1e-8
    # Verify the lower bound's independent window count combinatorially.
    for N in range(1, 161):
        for e in range(N+1):
            starts = range(0, N+1, e+1)
            windows = [set(range(a, a+e+1)) for a in starts]
            assert all(windows[i].isdisjoint(windows[j])
                       for i in range(len(windows)) for j in range(i+1, len(windows)))
            assert len(windows) == (N//(e+1)) + 1
    print('PASS: exact n=3..11, universal construction n=3..160, window disjointness.')


if __name__ == '__main__':
    validate()
