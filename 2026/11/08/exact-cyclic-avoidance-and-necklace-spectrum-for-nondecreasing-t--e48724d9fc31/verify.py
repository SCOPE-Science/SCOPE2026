"""Standalone exact verification of cyclic avoidance formula (Python standard library)."""
from itertools import product
from math import comb


def delta_coeff(q):
    periodic = (1, 1, 0, -1, -1, 0)
    d = [0] * (q + 1)
    d[0] = 1
    for j in range(2, q + 1):
        d[j] = -periodic[(j - 2) % 6] * comb(q, j)
    return d


def formula_counts(q, end):
    d = delta_coeff(q)
    a = [0] * (end + 1)
    for n in range(1, end + 1):
        a[n] = -n * (d[n] if n < len(d) else 0)
        a[n] -= sum(d[j] * a[n - j] for j in range(1, min(n, q) + 1))
    return a


def matrix_counts(q, end):
    # State order: (letter, prior comparison non-increasing/weakly ascending).
    N = 2 * q
    A = [[0] * N for _ in range(N)]
    for i in range(q):
        for j in range(q):
            if i > j:
                A[i][j] = 1
                A[q + i][j] = 1
            else:
                A[i][q + j] = 1
    P = [[int(i == j) for j in range(N)] for i in range(N)]
    result = [0]
    for _ in range(end):
        P = [[sum(P[i][k] * A[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
        result.append(sum(P[i][i] for i in range(N)))
    return result


def brute(q, n):
    return sum(
        all(not (a[i] <= a[(i + 1) % n] <= a[(i + 2) % n]) for i in range(n))
        for a in product(range(q), repeat=n)
    )


def main():
    for q in range(1, 9):
        c = formula_counts(q, 12)
        assert c == matrix_counts(q, 12), ('matrix', q)
        for n in range(1, min(9, 12) + 1):
            if q**n <= 450000:
                assert brute(q, n) == c[n], ('brute', q, n)
        if q == 2:
            assert all(c[n] == (2 if n % 2 == 0 else 0) for n in range(1, 13))
    assert formula_counts(3, 6)[1:] == [0, 6, 3, 18, 15, 57]
    print('PASS: q=1..8 trace/formula through m=12; direct cyclic word enumeration where q^m<=450000')


if __name__ == '__main__':
    main()
