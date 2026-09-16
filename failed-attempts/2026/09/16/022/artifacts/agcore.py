"""Core Macaulay-duality linear algebra for ternary septics (v2, corrected)."""
import numpy as np


def monomials(d):
    m = []
    for a in range(d, -1, -1):
        for b in range(d - a, -1, -1):
            m.append((a, b, d - a - b))
    return m


M = {d: monomials(d) for d in range(8)}
IDX = {d: {e: i for i, e in enumerate(M[d])} for d in range(8)}
DIM = {d: len(M[d]) for d in range(8)}


def fall(A, gam):
    r = 1
    for a, g in zip(A, gam):
        for i in range(g):
            r *= (a - i)
    return r


def catalecticant(c, e, d=7):
    """N[beta, gamma] = c_{beta+gamma} * fall(beta+gamma, gamma),
    rows beta in M[d-e], cols gamma in M[e]. Ann_e = ker(N: R_e -> k^{dim[d-e]}).
    rank(N) = dim A_e."""
    rows, cols = M[d - e], M[e]
    N = np.zeros((len(rows), len(cols)))
    idx7 = IDX[d]
    for i, beta in enumerate(rows):
        for j, gam in enumerate(cols):
            A = (beta[0] + gam[0], beta[1] + gam[1], beta[2] + gam[2])
            N[i, j] = c[idx7[A]] * fall(A, gam)
    return N


def apprank(N, tol=1e-8):
    return int(np.linalg.matrix_rank(N, tol=tol))


def hvector(c):
    return [apprank(catalecticant(c, e)) for e in range(8)]


def is_compressed(c):
    r1 = apprank(catalecticant(c, 1))
    r2 = apprank(catalecticant(c, 2))
    r3 = apprank(catalecticant(c, 3))
    return (r1 == 3 and r2 == 6 and r3 == 10), (r1, r2, r3)


def hess3_tensor(c):
    """T[i,j,k]: (i,j) over M3 x M3 (cubics), k in {0,1,2} coeff of y_k in
    the linear form d^{alpha_i+alpha_j} F.  T[i,j,k] = c_{gam+e_k}*(gam_k+1)."""
    T = np.zeros((10, 10, 3))
    idx7 = IDX[7]
    for i, a in enumerate(M[3]):
        for j, b in enumerate(M[3]):
            gam = (a[0] + b[0], a[1] + b[1], a[2] + b[2])
            for k in range(3):
                A = list(gam)
                A[k] += 1
                T[i, j, k] = c[idx7[tuple(A)]] * (gam[k] + 1)
    return T


def hess3_at(T, y):
    return T[:, :, 0] * y[0] + T[:, :, 1] * y[1] + T[:, :, 2] * y[2]


def hess3_det_at(T, y):
    return float(np.linalg.det(hess3_at(T, y)))


def eval_points(n=80, seed=0):
    rng = np.random.default_rng(seed)
    return rng.standard_normal((n, 3))


def hess_dets(c, pts):
    T = hess3_tensor(c)
    return np.array([hess3_det_at(T, y) for y in pts])


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    c = rng.standard_normal(36)
    print("h-vector:", hvector(c))
    print("compressed:", is_compressed(c))
    pts = eval_points(80)
    d = hess_dets(c, pts)
    print("generic hess3 dets: max abs =", np.max(np.abs(d)), " min abs =", np.min(np.abs(d)))
    # Fermat
    cf = np.zeros(36)
    cf[IDX[7][(7, 0, 0)]] = 1
    cf[IDX[7][(0, 7, 0)]] = 1
    cf[IDX[7][(0, 0, 7)]] = 1
    print("fermat h-vector:", hvector(cf))
    print("fermat hess3 dets max abs:", np.max(np.abs(hess_dets(cf, pts))))
    # cone: binary septic in y,z
    cc = np.zeros(36)
    for e in M[7]:
        if e[0] == 0:
            cc[IDX[7][e]] = rng.standard_normal()
    print("cone h-vector:", hvector(cc))
    print("cone hess3 dets max abs:", np.max(np.abs(hess_dets(cc, pts))))
