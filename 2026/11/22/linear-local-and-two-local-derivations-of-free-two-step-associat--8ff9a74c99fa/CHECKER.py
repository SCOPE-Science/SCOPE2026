#!/usr/bin/env python3
"""Exact finite-field checks for local and linear two-local derivations.

For N=V+(V tensor V) with tensor-length >=3 products zero, this script
constructs the tensor-square derivation action directly and computes its
algebraic reflexive hull over small prime fields. It also exhausts the
necessary obstruction to nonglobal linear two-local derivations in rank 2.
No dependencies beyond the Python standard library.
"""
from itertools import product


def rref_rank(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    if not a:
        return 0
    row_count, col_count = len(a), len(a[0])
    r = 0
    for c in range(col_count):
        pivot = next((i for i in range(r, row_count) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(inv * x) % p for x in a[r]]
        for i in range(r + 1, row_count):
            if a[i][c]:
                scale = a[i][c]
                a[i] = [(x - scale * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == row_count:
            break
    return r


def nullspace(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    m, n = len(a), len(a[0])
    piv = []
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(inv * x) % p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [(x - factor * y) % p for x, y in zip(a[i], a[r])]
        piv.append(c)
        r += 1
        if r == m:
            break
    vectors = []
    for c in range(n):
        if c in piv:
            continue
        vec = [0] * n
        vec[c] = 1
        for row, pivot_col in enumerate(piv):
            vec[pivot_col] = (-a[row][c]) % p
        vectors.append(vec)
    return vectors


def rho(matrix, n, p):
    # rho(T)(e_i tensor e_j)=Te_i tensor e_j + e_i tensor Te_j
    out = [[0] * (n * n) for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                out[k * n + j][i * n + j] = (out[k * n + j][i * n + j] + matrix[k][i]) % p
                out[i * n + k][i * n + j] = (out[i * n + k][i * n + j] + matrix[k][j]) % p
    return out


def act(matrix, vector, p):
    return [sum(a * b for a, b in zip(row, vector)) % p for row in matrix]


def projective_vectors(n, p):
    # exactly one normalized representative of each nonzero line of F_p^n
    for v in product(range(p), repeat=n):
        if any(v):
            lead = next(x for x in v if x)
            if lead == 1:
                yield v


def check_reflexive_hull(p, n, rank_one_only=False):
    dim = n * n
    rho_basis = []
    for i in range(n):
        for j in range(n):
            unit = [[int(a == i and b == j) for b in range(n)] for a in range(n)]
            rho_basis.append(rho(unit, n, p))
    assert rref_rank([[x for row in R for x in row] for R in rho_basis], p) == n * n
    if rank_one_only:
        vectors = [tuple(u[i] * v[j] % p for i in range(n) for j in range(n))
                   for u in projective_vectors(n, p) for v in projective_vectors(n, p)]
    else:
        vectors = [v for v in product(range(p), repeat=dim) if any(v)]
    constraints = []
    for w in vectors:
        evals = [act(R, w, p) for R in rho_basis]
        for covector in nullspace(evals, p):
            constraints.append([covector[i] * w[j] % p for i in range(dim) for j in range(dim)])
    hull_dim = dim * dim - rref_rank(constraints, p)
    assert hull_dim == n * n, (p, n, hull_dim)
    print("TENSOR_REFLEXIVE_HULL_OK", "p=", p, "n=", n,
          "vectors=", len(vectors), "dimension=", hull_dim)


def check_two_point_obstruction(p, n=2):
    tested = 0
    for entries in product(range(p), repeat=n * n):
        if not any(entries):
            continue
        M = [entries[i * n:(i + 1) * n] for i in range(n)]
        witnessed = False
        for diag in product(range(1, p), repeat=n):
            for v in product(range(p), repeat=n):
                if not any(v):
                    continue
                mv = [sum(M[i][j] * v[j] for j in range(n)) % p for i in range(n)]
                # Every skew-adjoint T-S fixing an invertible symmetric tensor
                # has v^T diag^-1 (T-S)v=0.  A nonzero value rules out the
                # common two-point derivation witness for this M=A-S.
                if sum(v[i] * pow(diag[i], -1, p) * mv[i] for i in range(n)) % p:
                    witnessed = True
                    break
            if witnessed:
                break
        assert witnessed, (p, n, "unexcluded mismatch", M)
        tested += 1
    print("TWO_POINT_RIGIDITY_OBSTRUCTION_OK", "p=", p,
          "n=", n, "excluded_nonzero_matrices=", tested)


if __name__ == "__main__":
    check_reflexive_hull(3, 2)
    check_reflexive_hull(5, 2)
    check_reflexive_hull(3, 3, rank_one_only=True)
    check_two_point_obstruction(3)
    check_two_point_obstruction(5)
    print("ASSOCIATIVE_LOCAL_DERIVATION_CHECKS_OK")
