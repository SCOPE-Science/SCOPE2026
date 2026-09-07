"""Hand-rolled primal simplex (numpy-only, no external LP solver available).
Solves: max c^T x  s.t.  A x <= b, x >= 0, with b >= 0 (origin feasible).
Returns primal x, objective, and dual y (min b^T y s.t. A^T y >= c, y>=0).
Uses Bland's rule (smallest-index) to avoid cycling.
"""
import numpy as np


def simplex_le(c, A, b, max_iter=200000, tol=1e-11):
    c = np.asarray(c, float).copy()
    A = np.asarray(A, float).copy()
    b = np.asarray(b, float).copy()
    m, n = A.shape
    assert np.all(b >= -1e-12), "need b>=0 for origin-feasible start"
    # tableau: rows 0..m-1 constraints, row m objective; cols 0..n-1 x, n..n+m-1 slacks, last rhs
    T = np.zeros((m + 1, n + m + 1))
    T[:m, :n] = A
    T[:m, n:n + m] = np.eye(m)
    T[:m, -1] = b
    T[m, :n] = -c
    basis = list(range(n, n + m))  # basic var index per row
    for _ in range(max_iter):
        row_obj = T[m, :-1]
        # entering: most negative reduced cost, Bland tie-break
        cand = np.where(row_obj < -tol)[0]
        if len(cand) == 0:
            break
        # choose most negative; tie -> smallest index
        j = int(cand[np.argmin(row_obj[cand])])
        col = T[:m, j]
        pos = np.where(col > tol)[0]
        if len(pos) == 0:
            raise ValueError("LP unbounded")
        ratios = T[pos, -1] / col[pos]
        rmin = ratios.min()
        # Bland: smallest basis index among near-tied rows
        tied = pos[np.where(ratios <= rmin + 1e-12 * (1 + abs(rmin)))[0]]
        i = int(min(tied, key=lambda t: basis[t]))
        # pivot on (i,j)
        piv = T[i, j]
        T[i, :] /= piv
        for r in range(m + 1):
            if r != i:
                T[r, :] -= T[r, j] * T[i, :]
        basis[i] = j
    else:
        raise RuntimeError("simplex: iteration limit")
    N = n + m
    x = np.zeros(N)
    for i, j in enumerate(basis):
        x[j] = T[i, -1]
    y = T[m, n:n + m].copy()  # dual vars = final objective-row entries in slack columns
    return {"x": x[:n], "obj": float(T[m, -1]),
            "y": y, "basis": basis,
            "iters": None}


if __name__ == "__main__":
    # max 3x+2y s.t. x+y<=4, x+3y<=6, x,y>=0 -> vertex (4,0), obj 12
    # (dual: min 4u+6v s.t. u+v>=3,u+3v>=2 -> (3,0), obj 12)
    r = simplex_le([3, 2], [[1, 1], [1, 3]], [4, 6])
    print("test1 x=", r["x"], "obj=", r["obj"], "y=", r["y"])
    assert abs(r["obj"] - 12) < 1e-9 and abs(r["x"][0]-4) < 1e-9 and abs(r["x"][1]) < 1e-9
    assert abs(4*r["y"][0]+6*r["y"][1]-12) < 1e-9 and r["y"][0]+r["y"][1] >= 3-1e-9 \
        and r["y"][0]+3*r["y"][1] >= 2-1e-9 and np.all(r["y"] >= -1e-9)
    # degenerate test (Klee-Minty n=3): max 4x1+2x2+x3 s.t. x1<=5,4x1+x2<=25,8x1+4x2+x3<=125
    r2 = simplex_le([4, 2, 1], [[1,0,0],[4,1,0],[8,4,1]], [5,25,125])
    print("test2 x=", r2["x"], "obj=", r2["obj"])
    assert abs(r2["obj"] - 125) < 1e-7, r2["obj"]
    print("simplex unit tests PASS")
