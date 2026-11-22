#!/usr/bin/env python3
"""Independent finite checks of parking-preference membership shattering."""
from itertools import product, combinations
from math import comb
from collections import Counter


def parking(vec):
    return all(v <= k for k, v in enumerate(sorted(vec), 1))


def criterion(n, support):
    if len({i for i, j in support}) != len(support):
        return False
    vals = [1] * n
    for i, j in support:
        vals[i] = max(2, j)
    return parking(vals)


def brute(n, support, concepts):
    k = len(support)
    seen = set()
    for word in concepts:
        bits = tuple(int(word[i] == j) for i, j in support)
        seen.add(bits)
        if len(seen) == 1 << k:
            return True
    return len(seen) == 1 << k


def count_by_independent_preferences(n, s):
    if s == 0:
        return 1
    count = 0
    for targets in product(range(1,n+1), repeat=s):
        vals = [max(2, j) for j in targets] + [1] * (n-s)
        if parking(vals):
            count += 1
    return count


def main():
    assert criterion(1, [])
    assert not criterion(1, [(0,1)])
    for n in range(2, 6):
        concepts = [word for word in product(range(1,n+1), repeat=n) if parking(word)]
        assert len(concepts) == (n+1)**(n-1)
        total = 0
        actual = [0]*(n+1)
        for s in range(n+1):
            for rows in combinations(range(n), s):
                for targets in product(range(1,n+1), repeat=s):
                    support = tuple(zip(rows,targets))
                    got = brute(n,support,concepts)
                    want = criterion(n,support)
                    if got != want:
                        raise AssertionError((n,support,got,want))
                    if got:
                        actual[s] += 1
                    total += 1
        expected = [comb(n,s) * (n+1-s)*(n+1)**(s-1) for s in range(n)] + [0]
        assert actual == expected, (n, actual, expected)
        print('full n=',n,'support_tests=',total,'polynomial=',actual,'PFn=',len(concepts))
    for n in range(2, 7):
        for s in range(n):
            a = count_by_independent_preferences(n,s)
            b = (n+1-s)*(n+1)**(s-1)
            assert a == b,(n,s,a,b)
        print('weighted enumeration n=',n,'OK')
    # a rank-two exchange failure, for every n >=3
    for n in range(3,9):
        A = [(0,n)]
        B = [(0,1),(1,n)]
        assert criterion(n,A) and criterion(n,B)
        assert all(not criterion(n,A+[v]) for v in B)
    print('all tests PASSED')

if __name__ == '__main__':
    main()
