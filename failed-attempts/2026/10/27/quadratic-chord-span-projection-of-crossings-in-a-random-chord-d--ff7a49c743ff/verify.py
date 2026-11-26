"""Exact finite checks for a random perfect matching on a labeled circle.

Run with: python verify.py
Requires only Python 3 standard library.
The unrestricted assertions in the accompanying proof do not rely on finite tests.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations
from math import isqrt


def all_matchings(free):
    if not free:
        yield ()
        return
    first = free[0]
    for j in range(1, len(free)):
        pair = (first, free[j])
        for rest in all_matchings(free[1:j] + free[j + 1:]):
            yield (pair,) + rest


def circular_distance(a, b, n):
    sep = abs(b - a)
    return min(sep, 2 * n - sep)


def crossings(edges):
    ans = 0
    for (a, b), (c, d) in combinations(edges, 2):
        if a < c < b < d or c < a < d < b:
            ans += 1
    return ans


def check(n):
    edges = list(combinations(range(2*n), 2))
    edge_index = {e: i for i, e in enumerate(edges)}
    count = total_X = total_X2 = total_Q = total_Q2 = total_XQ = 0
    present_count = [0] * len(edges)
    present_X = [0] * len(edges)
    present_Q = [0] * len(edges)
    length_count = [0] * (n + 1)
    length_X = [0] * (n + 1)

    for matching in all_matchings(tuple(range(2*n))):
        x = crossings(matching)
        q = sum((n-circular_distance(a,b,n))**2 for a,b in matching)
        count += 1
        total_X += x
        total_X2 += x*x
        total_Q += q
        total_Q2 += q*q
        total_XQ += x*q
        for a,b in matching:
            i = edge_index[(a,b)]
            d = circular_distance(a,b,n)
            present_count[i] += 1
            present_X[i] += x
            present_Q[i] += q
            length_count[d] += 1
            length_X[d] += x

    ex = F(total_X,count)
    eq = F(total_Q,count)
    vx = F(total_X2,count) - ex*ex
    vq = F(total_Q2,count) - eq*eq
    cxq = F(total_XQ,count) - ex*eq
    assert ex == F(n*(n-1),6)
    assert eq == F(n*n*(n-1),3)
    assert vx == F(n*(n-1)*(n+3),45)
    assert vq == F(2*n*n*(n-1)**2*(2*n+1),45)
    assert cxq == -F(n*n*(n-1)*(2*n+1),45)

    checks = 5
    for i,(a,b) in enumerate(edges):
        d = circular_distance(a,b,n)
        w = (n-d)**2
        assert F(present_count[i],count) == F(1,2*n-1)
        cx = F(present_X[i],count) - ex*F(present_count[i],count)
        cq = F(present_Q[i],count) - eq*F(present_count[i],count)
        wantx = F(n*(n-1)-3*w, 3*(2*n-1)*(2*n-3))
        wantq = F(2*n-2,(2*n-1)*(2*n-3))*(w-F(n*(n-1),3))
        assert cx == wantx
        assert cq == wantq
        assert cx == -F(1,2*n-2)*cq
        checks += 4

    for d in range(1,n+1):
        m = n if d==n else 2*n
        assert F(length_count[d],count) == F(m,2*n-1)
        cxl = F(length_X[d],count) - ex*F(length_count[d],count)
        formula = F(m*(n*(n-1)-3*(n-d)**2),3*(2*n-1)*(2*n-3))
        assert cxl == formula
        checks += 2

    explained = cxq*cxq/vq
    residual = vx-explained
    assert explained == F(n*n*(2*n+1),90)
    assert residual == F(n*(n-2),30)
    assert F(explained,vx) == F(n*(2*n+1),2*(n-1)*(n+3))
    checks += 3
    return count, checks


def pell_check():
    # The proof gives the infinite Pell parametrization; this is a bounded sanity check.
    sols = []
    for n in range(2,2000):
        y=n*(n-1)
        if y%3 == 0 and isqrt(y//3)**2==y//3:
            k=isqrt(y//3)
            d=n-k
            assert 1<=d<=n
            sols.append((n,d))
    assert sols == [(4,2),(49,21),(676,286)]
    return len(sols)


if __name__ == '__main__':
    total=0
    for n in range(2,8):
        m,c=check(n);total+=c
        print(f'n={n}: {m} perfect matchings, {c} exact assertions')
    p=pell_check()
    print(f'VERIFY_OK {total} exact assertions; {p} Pell-zero pairs through n=1999')
