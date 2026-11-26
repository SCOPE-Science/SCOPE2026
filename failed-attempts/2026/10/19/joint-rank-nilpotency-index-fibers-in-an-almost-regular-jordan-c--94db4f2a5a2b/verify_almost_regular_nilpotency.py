#!/usr/bin/env python3
"""Standalone exhaustive tests for nilpotency-index fibers in a Jordan centralizer.
No dependencies outside the Python standard library. Run: python3 verify_almost_regular_nilpotency.py
"""
from itertools import product


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    # F_4 = F_2[u]/(u^2+u+1), encoded by binary coefficients.
    x = 0
    aa, bb = a, b
    while bb:
        if bb & 1:
            x ^= aa
        aa <<= 1
        if aa & 4:
            aa ^= 7
        bb >>= 1
    return x


def matmul(A, B, q):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            aik = A[i][k]
            if not aik:
                continue
            for j in range(n):
                if B[k][j]:
                    C[i][j] = add(C[i][j], mul(aik, B[k][j], q), q)
    return C


def rank_of_matrix(X, q):
    A = [row[:] for row in X]
    n = len(A)
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, n) if A[i][c]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = next(z for z in range(1, q) if mul(z, A[r][c], q) == 1)
        A[r] = [mul(v, inv, q) for v in A[r]]
        for i in range(r + 1, n):
            if A[i][c]:
                # Subtraction equals addition in characteristic 2.
                factor = A[i][c]
                A[i] = [add(A[i][k],
                            mul(factor, A[r][k], q) if q == 4 else
                            (-mul(factor, A[r][k], q)) % q, q)
                        for k in range(n)]
        r += 1
    return r


def index_of_matrix(X, q):
    if not any(v for row in X for v in row):
        return 1
    n = len(X)
    power = X
    for idx in range(2, n + 1):
        power = matmul(power, X, q)
        if not any(v for row in power for v in row):
            return idx
    raise AssertionError('Unexpected nonnilpotent matrix')


def independent_census(m, q):
    n = m + 1
    table = {}
    for coeffs in product(range(q), repeat=m + 1):
        a = coeffs[:m - 1]
        b, c = coeffs[-2:]
        X = [[0] * n for _ in range(n)]
        for j in range(m):
            for i in range(1, m - j):
                X[j + i][j] = a[i - 1]
        X[m - 1][m] = b
        X[m][0] = c
        # Verify centralizing the fixed Jordan operator directly.
        J = [[0] * n for _ in range(n)]
        for j in range(m - 1):
            J[j + 1][j] = 1
        assert matmul(X, J, q) == matmul(J, X, q)
        idx = index_of_matrix(X, q)
        rank = rank_of_matrix(X, q)
        key = (rank, idx)
        table[key] = table.get(key, 0) + 1
    return table


def joint_formula(m, q):
    out = {(0, 1): 1, (1, 2): (q - 1) * (2 * q + 1),
           (2, 3): q * (q - 1)**2}
    for v in range(1, m - 1):
        h = (m + v - 1) // v
        mult = (q - 1) * q**(m - v - 1)
        if h >= 4:
            fibers = {h: q**2}
        elif h == 3:
            c = (q - 1) if (2 * v == m - 1) else 0
            fibers = {2: c, 3: q**2 - c}
        else:
            fibers = {2: 2 * q - 1, 3: (q - 1)**2}
        for j, a in fibers.items():
            if a:
                key = (m - v, j)
                out[key] = out.get(key, 0) + mult * a
    return {k: v for k, v in out.items() if v}


def formula(m, q):
    z = m // 2
    N = {1: 1}
    N[2] = (2 * q - 1) * q ** z - 1 if m % 2 == 0 else q ** (z + 2) - 1
    N[3] = q**2 * (q ** (m - ((m + 2) // 3)) - q**z)
    if m % 2 == 0:
        N[3] += (q - 1)**2 * q**z
    for j in range(4, m + 1):
        N[j] = q**2 * (q ** (m - ((m + j - 1) // j)) - q ** (m - ((m + j - 2) // (j - 1))))
    return {j: c for j, c in N.items() if c}


def main():
    tested = 0
    for q, max_m in [(2, 9), (3, 6), (4, 5), (5, 4)]:
        for m in range(2, max_m + 1):
            actual = independent_census(m, q)
            expected_joint = joint_formula(m, q)
            assert actual == expected_joint, (q, m, actual, expected_joint)
            expected_idx = formula(m, q)
            observed_idx = {}
            for (rank, idx), count in actual.items():
                observed_idx[idx] = observed_idx.get(idx, 0) + count
            assert observed_idx == expected_idx, (q, m, observed_idx, expected_idx)
            assert sum(actual.values()) == q ** (m + 1)
            if m >= 3:
                assert observed_idx[m] == (q - 1) * q**m
            tested += 1
            print('checked', q, m, dict(sorted(actual.items())))
    # Symbolic parameter sweep checks normalization, gap support and the
    # maximal-index fraction without enumerating larger matrix populations.
    for q in (2, 3, 4, 5, 7, 9):
        for m in range(2, 101):
            jnt = joint_formula(m, q)
            marg = {}
            for (_, idx), count in jnt.items():
                marg[idx] = marg.get(idx, 0) + count
            assert marg == formula(m, q)
            assert sum(marg.values()) == q**(m + 1)
            if m >= 3:
                assert marg[m] == (q - 1) * q**m
    print('VERIFY_OK_ALMOST_REGULAR_NILPOTENCY', tested)


if __name__ == '__main__':
    main()
