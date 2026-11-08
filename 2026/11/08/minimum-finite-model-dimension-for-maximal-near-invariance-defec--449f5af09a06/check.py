#!/usr/bin/env python3
"""Independent finite-dimensional diagnostics for the monomial model formulas.
All matrix arithmetic uses Python integers and prime-field elimination.
The all-ranks theorem is proved symbolically in RESULT.md, not by this script.
"""


def unit(n, j):
    return [int(k == j) for k in range(n)]


def backshift(x):
    return x[1:] + [0]


def rank_mod(columns, p=1000000007):
    if not columns:
        return 0
    rows = [[v[i] % p for v in columns] for i in range(len(columns[0]))]
    k, cols = 0, len(columns)
    for j in range(cols):
        pivot = next((i for i in range(k, len(rows)) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[k], rows[pivot] = rows[pivot], rows[k]
        inv = pow(rows[k][j], -1, p)
        for i in range(k + 1, len(rows)):
            if rows[i][j]:
                c = rows[i][j] * inv % p
                for h in range(j, cols):
                    rows[i][h] = (rows[i][h] - c * rows[k][h]) % p
        k += 1
        if k == len(rows):
            break
    return k


def check(n):
    N, k = 4 * n + 2, 2 * n + 2

    def pert(x):
        y = [0] * N
        for r in range(n):
            y[2 * r + 1] = x[2 * r + 2]
        return y

    def original(x):
        y = [0] * N
        for j in range(2 * n):
            y[j] = x[k + j]
        y[N - 1] = x[0]
        return y

    def B(x):
        a, b = original(x), pert(x)
        return [u - v for u, v in zip(a, b)]

    basis = [unit(N, 1)]
    expected = [unit(N, N - 1)]
    for r in range(n):
        u = unit(N, 2 * r + 2)
        u[k + 2 * r + 1] = 1
        basis.append(u)
        basis.append(unit(N, 2 * r + 3))
        expected.append(unit(N, 2 * r))
        expected.append([-x for x in unit(N, 2 * r + 1)])

    assert len(basis) == 2 * n + 1
    assert all(v[0] == 0 and B(v) == [0] * N for v in basis)
    assert [B(backshift(v)) for v in basis] == expected
    assert rank_mod([pert(unit(N, j)) for j in range(N)]) == n
    assert rank_mod([B(unit(N, j)) for j in range(N)]) == 2 * n + 1
    assert rank_mod(basis) == 2 * n + 1
    assert rank_mod(basis + [backshift(v) for v in basis]) == N
    return N


def main():
    for n in range(1, 14):
        N = check(n)
        print(f"rank={n}, model_dim={N}, kernel_dim={2*n+1}, exact_defect={2*n+1}: OK")
    print('FINITE_DIAGNOSTICS_PASS; all-n proof is separate.')


if __name__ == '__main__':
    main()
