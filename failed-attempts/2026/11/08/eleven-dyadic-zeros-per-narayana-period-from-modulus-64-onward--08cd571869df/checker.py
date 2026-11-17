"""Exact arithmetic checks for dyadic zero counts of Narayana's-cows numbers.

The computation verifies finite base cases and matrix identities. The infinite
claim additionally needs the 2-adic argument in RESULT.md.
"""

from math import comb


def mm(a, b):
    return [[sum(a[i][j] * b[j][k] for j in range(3)) for k in range(3)] for i in range(3)]


def power(a, n):
    out = [[int(i == j) for j in range(3)] for i in range(3)]
    while n:
        if n & 1:
            out = mm(out, a)
        a = mm(a, a)
        n //= 2
    return out


def mv(a, v):
    return [sum(a[i][j] * v[j] for j in range(3)) for i in range(3)]


def plus_eye(a, factor):
    return [[(a[i][j] - int(i == j)) // factor for j in range(3)] for i in range(3)]


def narayana_mod(k):
    m = 2**k
    period = 7 * 2 ** (k - 1)
    s = [0, 0, 1]
    for n in range(3, period):
        s.append((s[-1] + s[-3]) % m)
    return [n for n, value in enumerate(s) if value % m == 0]


def main():
    M = [[0, 1, 0], [0, 0, 1], [1, 0, 1]]
    M7, M14, M28 = (power(M, n) for n in (7, 14, 28))
    assert M7 == [[3, 2, 4], [4, 3, 6], [6, 4, 9]]
    assert M28 == [[8641, 5896, 12664], [12664, 8641, 18560], [18560, 12664, 27201]]
    assert any((M7[i][j] - (i == j)) % 4 for i in range(3) for j in range(3))
    assert any((M14[i][j] - (i == j)) % 8 for i in range(3) for j in range(3))
    C = plus_eye(M28, 8)
    assert C == [[1080, 737, 1583], [1583, 1080, 2320], [2320, 1583, 3400]]
    B = plus_eye(M7, 2)
    v = [0, 0, 1]
    assert mv(M, v) == [0, 1, 1]
    c1, c2, c3 = [], [], []
    for A, arr, how_many in ((B, c1, 3), (C, c2, 3)):
        w = v
        for j in range(how_many):
            w = mv(A, w)
            arr.append(mv(M, w)[0])
    assert c1 == [3, 19, 129]
    assert c2 == [2320, 12899489, 71724385960]
    assert [mv(C, mv(power(M, r), v))[0] % 2 for r in (0, 1, 5)] == [1, 0, 1]
    total = [3, 4, 5, 5, 7] + [11] * 7
    for k in range(1, 13):
        zz = narayana_mod(k)
        assert len(zz) == total[k - 1], (k, len(zz))
        assert all(n % 7 in (0, 1, 5) for n in zz)
        if k >= 6:
            cnt = {r: sum(n % 7 == r for n in zz) for r in (0, 1, 5)}
            assert cnt == {0: 2, 1: 8, 5: 1}, (k, cnt)
    print('matrix identities, 2-adic initial data, and exact zero counts for 1<=k<=12: PASS')
    print('count sequence:', total)
    print('k=6 zero residues:', narayana_mod(6))
    print('Infinite proof requires the documented isometry and lifting argument.')


if __name__ == '__main__':
    main()
