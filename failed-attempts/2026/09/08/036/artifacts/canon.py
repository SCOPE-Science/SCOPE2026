"""Canonical representative of a lattice tetrahedron under unimodular affine maps.

Equivalence: positioned edge matrices (rows = edge vectors) transform by
  E -> L E W,  L in P (24 vertex-repositionings: translate origin to a vertex +
  permute remaining), W in GL(3,Z) (ambient basis change, right action).
Canonical key = min over 24 repositionings of column-HNF(E) (invariant under
right GL action). Column-HNF via transpose of row-HNF.
"""
import math, itertools

def egcd(a, b):
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def hnf_row_upper(M):
    """Row-HNF upper triangular: H = U M, U unimodular.
    H[1][0]=H[2][0]=H[2][1]=0, diag>0, 0<=H[i][j]<H[j][j] for i<j."""
    R = [list(map(int, r)) for r in M]
    row = 0
    for c in range(3):
        while True:
            nz = [i for i in range(row, 3) if R[i][c] != 0]
            if len(nz) <= 1:
                break
            i, j = nz[0], nz[1]
            g, x, y = egcd(R[i][c], R[j][c])
            ri, rj = R[i][:], R[j][:]
            a, b = ri[c] // g, rj[c] // g
            R[i] = [x * u + y * v for u, v in zip(ri, rj)]
            R[j] = [-b * u + a * v for u, v in zip(ri, rj)]
        piv = None
        for i in range(row, 3):
            if R[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        R[row], R[piv] = R[piv], R[row]
        if R[row][c] < 0:
            R[row] = [-x for x in R[row]]
        row += 1
        if row == 3:
            break
    assert row == 3, f"singular? {M} -> {R}"
    for j in range(3):
        for i in range(j):
            q = R[i][j] // R[j][j]
            R[i] = [u - q * v for u, v in zip(R[i], R[j])]
    for i in range(3):
        assert R[i][i] > 0, (M, R)
        for j in range(i):
            assert R[i][j] == 0, (M, R)
        for j in range(i + 1, 3):
            assert 0 <= R[i][j] < R[j][j], (M, R)
    return tuple(tuple(r) for r in R)

def hnf_col(E):
    """Column-HNF: H = E W, W unimodular. = transpose of row-HNF of transpose."""
    T = tuple(tuple(E[r][c] for r in range(3)) for c in range(3))
    H = hnf_row_upper(T)
    return tuple(tuple(H[c][r] for c in range(3)) for r in range(3))

def positioned_edge_matrices(verts):
    for j in range(4):
        o = verts[j]
        rest = [verts[i] for i in range(4) if i != j]
        for perm in itertools.permutations(rest):
            yield tuple(tuple(p[k] - o[k] for k in range(3)) for p in perm)

def canon_key(verts):
    return min(hnf_col(E) for E in positioned_edge_matrices(verts))

def selftest():
    import numpy as np
    rng = np.random.default_rng(0)
    # 1) row-HNF left invariance: HNF(U M) == HNF(M)
    for _ in range(200):
        M = rng.integers(-5, 6, size=(3, 3))
        if round(abs(np.linalg.det(M))) == 0:
            continue
        # random unimodular U (product of elementary)
        U = np.eye(3, dtype=int)
        for _ in range(6):
            i, j = rng.choice(3, size=2, replace=False)
            E = np.eye(3, dtype=int); E[i, j] = int(rng.integers(-2, 3))
            if rng.random() < 0.2:
                E[i, i] = -1
            U = E @ U
        assert round(abs(np.linalg.det(U))) == 1
        assert hnf_row_upper(U @ M) == hnf_row_upper(M), (U, M)
    # 2) col-HNF right invariance: colHNF(E W) == colHNF(E)
    for _ in range(200):
        M = rng.integers(-5, 6, size=(3, 3))
        if round(abs(np.linalg.det(M))) == 0:
            continue
        W = np.eye(3, dtype=int)
        for _ in range(6):
            i, j = rng.choice(3, size=2, replace=False)
            E = np.eye(3, dtype=int); E[i, j] = int(rng.integers(-2, 3))
            W = W @ E
        assert round(abs(np.linalg.det(W))) == 1
        assert hnf_col(M @ W) == hnf_col(M), (M, W)
    # 3) tetra equivalence: permute vertices / GL-map -> same key
    T = ((0,0,0),(2,0,0),(0,3,0),(1,1,7))
    T2 = ((2,0,0),(0,0,0),(0,3,0),(1,1,7))
    assert canon_key(T) == canon_key(T2)
    U = np.array([[1,1,0],[0,1,0],[0,0,1]])
    T3 = tuple(tuple(int(x) for x in (U @ np.array(v))) for v in T)
    assert canon_key(T) == canon_key(T3), (canon_key(T), canon_key(T3))
    # shear + translate + reflect
    U2 = np.array([[0,1,0],[1,0,0],[0,0,-1]])
    t = np.array([3,-2,5])
    T4 = tuple(tuple(int(x) for x in (U2 @ np.array(v) + t)) for v in T)
    assert canon_key(T) == canon_key(T4)
    # different volume -> different key
    T5 = ((0,0,0),(1,0,0),(0,1,0),(0,0,1))
    assert canon_key(T) != canon_key(T5)
    print("canon selftest OK")

if __name__ == "__main__":
    selftest()
