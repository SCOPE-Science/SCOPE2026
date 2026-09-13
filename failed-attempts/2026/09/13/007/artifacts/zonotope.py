"""Exact zonotope calculus for C_n short-root zonotopes (numpy only)."""
import itertools
import math
import numpy as np


def c_roots(n):
    """Positive short roots of C_n: e_i - e_j, e_i + e_j for i<j. Returns n x m array."""
    cols = []
    for i in range(n):
        for j in range(i + 1, n):
            v = np.zeros(n)
            v[i] = 1.0
            v[j] = -1.0
            cols.append(v)
            w = np.zeros(n)
            w[i] = 1.0
            w[j] = 1.0
            cols.append(w)
    return np.column_stack(cols)


def mv(*gens):
    """Mixed volume V(A1..An) where Aj = sum of segments [-g,g], g = columns of gens[j].

    V = (2^n / n!) * sum over tuples of |det(g1..gn)|.
    """
    n = gens[0].shape[0]
    assert len(gens) == n
    ranges = [range(g.shape[1]) for g in gens]
    idx = np.array(list(itertools.product(*ranges)))
    N = idx.shape[0]
    M = np.empty((N, n, n))
    for d in range(n):
        M[:, :, d] = gens[d][:, idx[:, d]].T
    dets = np.linalg.det(M)
    return (2.0 ** n / math.factorial(n)) * float(np.sum(np.abs(dets)))


def vol(G):
    n = G.shape[0]
    return mv(*([G] * n))


def support_vals(G, U):
    """h_Z(u) = sum_g |<g,u>| for each row u of U. Returns array length len(U)."""
    return np.sum(np.abs(U @ G), axis=1)


def facet_data(G, tol=1e-8):
    """Enumerate facets of zonotope sum[-g,g] via (n-1)-subsets.

    Returns (U, A): U = (F,n) unit outward normals (one per facet pair side, both signs),
    A = (F,) facet (n-1)-volumes. So S_Z = sum A_F delta_{u_F} over both signs.
    """
    n, m = G.shape
    # candidate normals from rank-(n-1) subsets
    cand = []
    for J in itertools.combinations(range(m), n - 1):
        A = G[:, list(J)]
        # singular values of n x (n-1) matrix
        s = np.linalg.svd(A, compute_uv=False)
        if s[-1] < tol:
            continue
        # null vector = null space of A^T
        _, _, vt = np.linalg.svd(A.T, full_matrices=True)
        u = vt[-1, :]
        u = u / np.linalg.norm(u)
        # canonicalize sign
        for k in range(n):
            if abs(u[k]) > 1e-9:
                if u[k] < 0:
                    u = -u
                break
        cand.append(np.round(u, 6))
    # unique directions (unoriented)
    uniq = []
    seen = set()
    for u in cand:
        key = tuple(u)
        if key not in seen:
            seen.add(key)
            uniq.append(u)
    U_list, A_list = [], []
    for u in uniq:
        u = u / np.linalg.norm(u)
        dots = G.T @ u
        I = [i for i in range(m) if abs(dots[i]) < 1e-6]
        if len(I) < n - 1:
            continue
        GI = G[:, I]
        if np.linalg.matrix_rank(GI, tol=1e-6) != n - 1:
            continue
        area = 0.0
        for J in itertools.combinations(range(len(I)), n - 1):
            B = GI[:, list(J)]
            area += abs(float(np.linalg.det(np.column_stack([B, u]))))
        area *= 2.0 ** (n - 1)
        if area < tol:
            continue
        U_list.append(u)
        U_list.append(-u)
        A_list.append(area)
        A_list.append(area)
    return np.array(U_list), np.array(A_list)


def ratio(K, Z, U, A):
    """R = Delta/dist with K rescaled so Vol(K)=Vol(Z). Reference C = Z^{n-2}.

    Returns (R, Delta, dist, a_star). Symmetric bodies => v_opt = 0.
    """
    n = Z.shape[0]
    V0 = vol(Z)
    VK = vol(K)
    s = (V0 / VK) ** (1.0 / n)
    Ks = K * s
    Cn = [Z] * (n - 2)
    b1 = mv(Ks, Z, *Cn)
    b2 = mv(Ks, Ks, *Cn)
    b0 = V0
    Delta = b1 ** 2 - b2 * b0
    hK = support_vals(Ks, U)
    hZ = support_vals(Z, U)
    denom = float(np.sum(A * hZ * hZ))
    astar = float(np.sum(A * hK * hZ)) / denom
    if astar <= 0:
        astar = 1e-12
    dist = float(np.sum(A * (hK - astar * hZ) ** 2))
    R = Delta / dist if dist > 0 else float("inf")
    return R, Delta, dist, astar
