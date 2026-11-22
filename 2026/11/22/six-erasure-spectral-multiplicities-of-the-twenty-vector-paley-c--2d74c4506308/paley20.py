"""Exact six-erasure type census for the Paley skew-conference matrix of order 20.

No external dependencies. Run: python paley20.py
"""
from collections import Counter
from itertools import combinations
from math import comb

EXPECTED = {(0, 1): 1140, (3, 9): 6840, (4, 1): 13680,
            (5, 25): 6840, (6, 49): 7980, (6, 81): 2280}


def paley(p=19):
    squares = {(x * x) % p for x in range(1, p)}
    n = p + 1
    s = [[0] * n for _ in range(n)]
    for i in range(1, n):
        s[0][i], s[i][0] = 1, -1
    for i in range(1, n):
        for j in range(i + 1, n):
            v = 1 if (i - j) % p in squares else -1
            s[i][j], s[j][i] = v, -v
    for i in range(n):
        for j in range(n):
            dot = sum(s[i][h] * s[j][h] for h in range(n))
            assert dot == (p if i == j else 0)
    return s


def determinant(a):
    n = len(a)
    x = [row[:] for row in a]
    prev = 1
    sign = 1
    for k in range(n-1):
        if not x[k][k]:
            pivot = next((i for i in range(k + 1, n) if x[i][k]), None)
            if pivot is None:
                return 0
            x[k], x[pivot] = x[pivot], x[k]
            sign *= -1
        q = x[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                t = x[i][j] * q - x[i][k] * x[k][j]
                assert t % prev == 0
                x[i][j] = t // prev
            x[i][k] = 0
        prev = q
    return sign * x[n - 1][n - 1]


def census():
    s = paley()
    out = Counter()
    for I in combinations(range(20), 6):
        a = [[s[i][j] for j in I] for i in I]
        # For real skew S: tr(S^4) = sum_{i,j} (S^2_ij)^2.
        t4 = sum(sum(a[i][h] * a[h][j] for h in range(6)) ** 2
                 for i in range(6) for j in range(6))
        # Char poly det(zI-S) = z^6+15z^4+c*z^2+det(S).
        # c=((15)^2 - tr(S^4)/2)/2.
        assert t4 % 2 == 0 and (225 - t4 // 2) % 2 == 0
        c = (225 - t4 // 2) // 2
        assert (c - 15) % 8 == 0
        k = (c - 15) // 8
        b = determinant(a)
        assert b >= 0
        out[(k, b)] += 1
    assert out == EXPECTED, out
    assert sum(out.values()) == comb(20, 6)
    for (k, b), count in sorted(out.items()):
        print(f'k={k}, determinant={b}, six_sets={count}')
    print('PASS: all 38760 Paley twenty-frame erasure sets; independent determinant/trace methods.')


if __name__ == '__main__':
    census()
