#!/usr/bin/env python3
"""Exact two-read graph check by constructing distinct deletion sets.
Standard-library only. This finite check does not prove the general theorem.
"""
from itertools import product
from math import comb


def allowed(w, r):
    return all(not all(w[i] == w[j] for j in range(i, i+r+1))
               for i in range(len(w)-r))


def deck(w):
    return {w[:i] + w[i+1:] for i in range(len(w))}


def admissible_context(w, letters, r, side):
    if not w:
        return True
    run = 1
    if side == 'left':
        for j in range(len(w)-2, -1, -1):
            if w[j] == w[-1]:
                run += 1
            else:
                break
        return w[-1] not in letters or run < r
    for j in range(1, len(w)):
        if w[j] == w[0]:
            run += 1
        else:
            break
    return w[0] not in letters or run < r


def expected_by_context(q, r, n):
    # No deletion-ball inspection in this comparator.
    total = [0]*(n+1)
    for a in range(n+1):
        total[a] = sum(admissible_context(w, {0, 1}, r, 'left')
                       for w in product(range(q), repeat=a) if allowed(w, r))
    return comb(q, 2) * sum(total[a]*total[n-L-a]
                            for L in range(2, n+1)
                            for a in range(n-L+1))


def verify(q, r, n):
    words = [w for w in product(range(q), repeat=n) if allowed(w, r)]
    deletion = [deck(w) for w in words]
    actual = [0]*(n+1)
    for i, x in enumerate(words):
        for j in range(i+1, len(words)):
            if len(deletion[i] & deletion[j]) >= 2:
                y = words[j]
                diffs = [k for k in range(n) if x[k] != y[k]]
                length = diffs[-1] - diffs[0] + 1
                assert length == len(diffs) and length >= 2
                a, b = x[diffs[0]:diffs[-1]+1], y[diffs[0]:diffs[-1]+1]
                assert len(set(a)) == 2 and set(a) == set(b)
                assert all(a[k] != a[k+1] for k in range(len(a)-1))
                assert all(a[k] != b[k] for k in range(len(a)))
                actual[length] += 1
    expected = expected_by_context(q, r, n)
    assert sum(actual) == expected, (q, r, n, actual, expected)
    print(f'q={q} r={r} n={n}: {len(words)} vertices, '
          f'{sum(actual)} confusable unordered pairs')


if __name__ == '__main__':
    for q, cases in [(2, [(1,8),(2,8),(3,8),(4,7)]),
                     (3, [(1,6),(2,6),(3,5)]),
                     (4, [(1,5),(2,5)]), (5, [(1,4),(2,4)])]:
        for r, nmax in cases:
            for n in range(2, nmax+1):
                verify(q, r, n)
    print('ALL DIRECT DELETION-DECK CHECKS PASSED')
