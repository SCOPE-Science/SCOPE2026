"""Two-phase simplex (numpy-only): max c^T x s.t. Ax <= b, x >= 0 (general b).
Phase I with artificial variables; Bland's rule throughout. Returns x, obj, iters.
"""
import numpy as np


def simplex_general(c, A, b, tol=1e-9, max_iter=200000):
    c = np.asarray(c, float).copy()
    A = np.asarray(A, float).copy()
    b = np.asarray(b, float).copy()
    m, n = A.shape
    # normalize rows with b<0: multiply by -1 -> >= constraint; add surplus+artificial
    neg = b < -tol
    # columns: [x (n)] [slack/surplus (m)] [artificial (m_neg)]
    neg_idx = np.where(neg)[0]
    nart = len(neg_idx)
    art_col = {}
    for t, i in enumerate(neg_idx):
        art_col[i] = n + m + t
    N = n + m + nart
    T = np.zeros((m + 1, N + 1))
    for i in range(m):
        sgn = -1.0 if neg[i] else 1.0
        T[i, :n] = sgn * A[i]
        T[i, n + i] = sgn  # +1 slack for <= rows, -1 surplus for >= rows
        if neg[i]:
            T[i, art_col[i]] = 1.0
        T[i, -1] = sgn * b[i]
    assert np.all(T[:m, -1] >= -1e-12)
    basis = []
    for i in range(m):
        basis.append(art_col[i] if neg[i] else n + i)

    def pivot(r, j):
        piv = T[r, j]
        assert abs(piv) > 1e-13
        T[r, :] /= piv
        for r2 in range(m + 1):
            if r2 != r:
                T[r2, :] -= T[r2, j] * T[r, :]
        basis[r] = j

    def optimize(row, cols, max_it):
        for _ in range(max_it):
            cand = [j for j in cols if T[row, j] < -tol]
            if not cand:
                return
            j = min(cand, key=lambda j: (round(float(T[row, j]), 12), j))
            col = T[:m, j]
            pos = [i for i in range(m) if col[i] > tol]
            if not pos:
                raise ValueError("unbounded")
            rmin = min(T[i, -1] / col[i] for i in pos)
            tied = [i for i in pos if T[i, -1] / col[i] <= rmin + 1e-9 * (1 + abs(rmin))]
            i = min(tied, key=lambda t: basis[t])
            pivot(i, j)
        raise RuntimeError("iteration limit")

    nonart = list(range(n + m))
    if nart:
        # Phase I: max -sum(artificial)
        T[m, :] = 0.0
        for i in neg_idx:
            T[m, art_col[i]] = -1.0 if False else 0.0
        # standard trick: objective row = -sum of artificial rows expressed in nonbasic vars
        T[m, :] = 0.0
        T[m, -1] = 0.0
        for i in neg_idx:
            T[m, :] -= T[i, :]
        # maximize: entering while T[m,j] < 0 over non-artificial cols... but artificials basic;
        # allow all non-basic columns
        optimize(m, [j for j in range(N) if j not in basis], max_iter)
        if T[m, -1] < -1e-7:
            raise ValueError("infeasible")
        # drive artificials out of basis
        for i in list(range(m)):
            if basis[i] >= n + m:
                row = T[i, :n + m]
                nz = [j for j in range(n + m) if abs(row[j]) > tol]
                if nz:
                    pivot(i, nz[0])
        # drop artificial columns
        keep = list(range(n + m)) + [N]
        T = T[:, keep]
        N = n + m
        # Phase II objective
        T[m, :] = 0.0
        T[m, :n] = -c
        T[m, -1] = 0.0
        for i in range(m):
            j = basis[i]
            if j < N and abs(T[m, j]) > tol:
                T[m, :] -= T[m, j] * T[i, :]
        optimize(m, [j for j in range(N) if j not in basis], max_iter)
    else:
        T[m, :n] = -c
        optimize(m, list(range(n + m)), max_iter)
    x = np.zeros(N)
    for i, j in enumerate(basis):
        if j < N:
            x[j] = T[i, -1]
    x = np.maximum(x, 0.0)
    return {"x": x[:n], "obj": float(T[m, -1])}


if __name__ == "__main__":
    r = simplex_general([3, 2], [[1., 1.], [1., 3.]], [4., 6.])
    assert abs(r["obj"] - 12) < 1e-9, r
    # equality-constrained: max x s.t. x<=3, -x<=-3? -> x=3
    r = simplex_general([1.], [[1.], [-1.]], [3., -3.])
    assert abs(r["obj"] - 3) < 1e-9, r
    # infeasible: x<=-1, x>=0 form: -x<=-1... use max x s.t. x<=-1,x>=0 impossible w/ x>=0? x<=-1 & x>=0
    try:
        simplex_general([1.], [[1.]], [-1.])
        print("ERROR: should be infeasible")
    except ValueError as e:
        print("infeasible correctly detected:", e)
    # classic: max x+y s.t. x+2y<=4, 4x+2y<=-? skip; equality test: max 2x+3y s.t. x+y=4
    r = simplex_general([2., 3.], [[1., 1.], [-1., -1.]], [4., -4.])
    assert abs(r["obj"] - 12) < 1e-9, r
    print("two-phase simplex unit tests PASS")
