"""Independent exhaustive checks of finite-field averaging-projection counts.

No third-party packages are needed. For field order four use F_2[u]/(u^2+u+1).
The matrix conditions are tested directly on basis pairs, independently
of the structural proof.
"""
from collections import Counter
from itertools import product


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def neg(a, q):
    return a if q == 4 else (-a) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    x = 0
    while b:
        if b & 1:
            x ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return x


def dot(a, b, q):
    result = 0
    for x, y in zip(a, b):
        result = add(result, mul(x, y, q), q)
    return result


def matrix_product(a, b, q):
    n = len(a)
    return [[dot(a[i], [b[k][j] for k in range(n)], q) for j in range(n)] for i in range(n)]


def bracket(a, b, q):
    return [0] + [add(mul(a[0], b[j], q), neg(mul(b[0], a[j], q), q), q)
                  for j in range(1, len(a))]


def matrix_vector(a, x, q):
    return [dot(row, x, q) for row in a]


def matrix_rank(a, q):
    a = [row[:] for row in a]
    n = len(a)
    rank = 0
    for j in range(n):
        pivot = next((i for i in range(rank, n) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = next(x for x in range(1, q) if mul(a[rank][j], x, q) == 1)
        a[rank] = [mul(x, inv, q) for x in a[rank]]
        for i in range(n):
            if i == rank:
                continue
            factor = a[i][j]
            a[i] = [add(x, neg(mul(factor, y, q), q), q)
                    for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def passes_averaging(a, q):
    n = len(a)
    if matrix_product(a, a, q) != a:
        return False
    columns = [[a[i][j] for i in range(n)] for j in range(n)]
    basis = [[int(i == j) for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            rhs = bracket(columns[i], columns[j], q)
            for x, y in ((columns[i], basis[j]), (basis[i], columns[j])):
                if matrix_vector(a, bracket(x, y, q), q) != rhs:
                    return False
    return True


def passes_homomorphism(a, q):
    n = len(a)
    columns = [[a[i][j] for i in range(n)] for j in range(n)]
    basis = [[int(i == j) for i in range(n)] for j in range(n)]
    return all(matrix_vector(a, bracket(basis[i], basis[j], q), q) ==
               bracket(columns[i], columns[j], q)
               for i in range(n) for j in range(n))


def gaussian(m, r, q):
    numerator = 1
    denominator = 1
    for j in range(r):
        numerator *= q ** (m - j) - 1
        denominator *= q ** (r - j) - 1
    return numerator // denominator


def predicted(q, n):
    m = n - 1
    counts = {0: 1}
    for r in range(m + 1):
        counts[r + 1] = gaussian(m, r, q) * q ** ((m-r) * (r+1))
    return counts


def exhaustive(q, n):
    totals = Counter()
    for flat in product(range(q), repeat=n*n):
        a = [list(flat[i*n:(i+1)*n]) for i in range(n)]
        if passes_averaging(a, q):
            assert passes_homomorphism(a, q), 'non-endomorphism found'
            totals[matrix_rank(a, q)] += 1
    expected = predicted(q, n)
    assert dict(totals) == expected, (q, n, totals, expected)
    print('EXHAUSTIVE_OK', q, n, dict(sorted(totals.items())))


if __name__ == '__main__':
    for q, n in ((2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (4, 2), (4, 3)):
        exhaustive(q, n)
    print('VERIFY_OK')
