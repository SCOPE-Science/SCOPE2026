"""Finite-field matrix verification for the square-bouquet decomposition.

Usage: python3 verify_matrices.py
No dependencies beyond Python standard library.
"""


def multiply(a, b):
    n = len(a)
    return [[sum(a[i][h] * b[h][j] for h in range(n)) & 1
             for j in range(n)] for i in range(n)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def rank(a):
    pivots = {}
    for row in a:
        x = sum((v & 1) << i for i, v in enumerate(row))
        while x:
            i = x.bit_length() - 1
            if i not in pivots:
                pivots[i] = x
                break
            x ^= pivots[i]
    return len(pivots)


def nullity_of_power(m, t):
    n = len(m)
    r = identity(n)
    for _ in range(t):
        r = multiply(r, m)
    e = identity(n)
    return n - rank([[r[i][j] ^ e[i][j] for j in range(n)] for i in range(n)])


def scan_matrix(k):
    n = 3 * k + 1
    cols = []
    for j in range(n):
        x = [int(i == j) for i in range(n)]
        h_new = x[0] ^ (sum(x[3 * i + 1] + x[3 * i + 3] for i in range(k)) & 1)
        y = [h_new]
        for i in range(k):
            a, b, c = x[3 * i + 1:3 * i + 4]
            y.extend((a ^ b ^ h_new, a ^ c ^ h_new, a))
        cols.append(y)
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def fixed_dim_formula(k, t):
    p = t & -t
    if k % 2:
        return 2 + 2 * int(t % 3 == 0) + (k - 1) * min(3, p)
    return 2 + min(5, p) + (k - 2) * min(3, p)


def main():
    a = [[1, 1, 0], [1, 0, 1], [1, 0, 0]]
    n = [[a[i][j] ^ int(i == j) for j in range(3)] for i in range(3)]
    p = identity(3)
    for r in range(1, 4):
        p = multiply(p, n)
        assert rank(p) == 3 - r
    b = scan_matrix(1)
    b3 = multiply(multiply(b, b), b)
    assert b3 == identity(4)
    assert nullity_of_power(b, 1) == 2
    c = scan_matrix(2)
    u = [[c[i][j] ^ int(i == j) for j in range(7)] for i in range(7)]
    p = identity(7)
    ranks = []
    for r in range(1, 6):
        p = multiply(p, u)
        ranks.append(rank(p))
    assert ranks == [4, 3, 2, 1, 0], ranks
    print('Base matrices: A has one size-3 unipotent block;')
    print('B has I_2 plus one irreducible quadratic block;')
    print('C has unipotent blocks of sizes 5,1,1.')
    for k in range(1, 13):
        m = scan_matrix(k)
        order = 3 if k == 1 else (12 if k % 2 else 8)
        for t in range(1, order + 1):
            actual = nullity_of_power(m, t)
            predicted = fixed_dim_formula(k, t)
            assert actual == predicted, (k, t, actual, predicted)
        print('k={} dimension={} order={} all powers verified'.format(k, len(m), order))
    print('PASS: fixed-space dimensions for all powers, k=1 through 12')


if __name__ == '__main__':
    main()
