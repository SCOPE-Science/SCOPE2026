"""Verification for large-block AR(1) KLT/DCT boundary-layer formulas.

For R_N(rho) = [rho**abs(i-j)], the exact phase equation is used to compare
finite blocks with the critical scaling N(1-rho) -> c.  A small dense NumPy
check independently diagonalizes R_N(rho) and compares its Perron eigenvector
with the closed-form first mode.
"""
import math
import numpy as np


def phase_root(N, rho, m=1):
    lo = (m - 1) * math.pi / (N + 1)
    hi = m * math.pi / (N + 1)

    def F(w):
        theta = math.atan2(rho * math.sin(w), 1.0 - rho * math.cos(w))
        return (N + 1) * w + 2.0 * theta - m * math.pi

    a = lo + 1e-16
    b = hi - 1e-16
    if F(a) > 0.0 or F(b) < 0.0:
        raise RuntimeError("root bracket failed")
    for _ in range(100):
        mid = 0.5 * (a + b)
        if F(mid) <= 0.0:
            a = mid
        else:
            b = mid
    return 0.5 * (a + b)


def critical_root(c, m=1):
    if c == 0.0:
        return (m - 1) * math.pi
    lo = (m - 1) * math.pi
    hi = m * math.pi

    def F(x):
        return math.tan(0.5 * (m * math.pi - x)) - x / c

    a = lo + 1e-14
    b = hi - 1e-14
    for _ in range(120):
        mid = 0.5 * (a + b)
        if F(mid) > 0.0:
            a = mid
        else:
            b = mid
    return 0.5 * (a + b)


def ar1_eigenvalue(rho, w):
    return (1.0 - rho * rho) / (1.0 - 2.0 * rho * math.cos(w) + rho * rho)


def first_mode_overlap_from_x(x):
    if abs(x) < 1e-12:
        return 1.0
    mean = 2.0 * math.sin(x / 2.0) / x
    sq = 0.5 + math.sin(x) / (2.0 * x)
    return mean / math.sqrt(sq)


def discrete_first_mode(N, rho):
    w = phase_root(N, rho, 1)
    x = N * w
    vals = [math.cos(w * (k - (N - 1) / 2.0)) for k in range(N)]
    norm = math.sqrt(sum(v * v for v in vals))
    vals = [v / norm for v in vals]
    overlap = sum(vals) / math.sqrt(N)
    distance = math.sqrt(max(0.0, 2.0 - 2.0 * overlap))
    return x, overlap, distance, np.asarray(vals)


def dense_matrix_check(c, N):
    rho = math.exp(-c / N)
    idx = np.arange(N)
    R = rho ** np.abs(idx[:, None] - idx[None, :])
    eigvals, eigvecs = np.linalg.eigh(R)
    u = eigvecs[:, -1]
    if u.sum() < 0:
        u = -u
    x, _, _, closed = discrete_first_mode(N, rho)
    err = np.linalg.norm(u - closed)
    dc = np.ones(N) / math.sqrt(N)
    dist = np.linalg.norm(u - dc)
    print(
        f"dense N={N:4d} c={c:g}: N*w={x:.12f} "
        f"mode_formula_error={err:.3e} distance_to_DC={dist:.12f} "
        f"lambda1/N={eigvals[-1]/N:.12f}"
    )


def report_critical(c):
    xstar = critical_root(c, 1)
    astar = first_mode_overlap_from_x(xstar)
    dstar = math.sqrt(2.0 - 2.0 * astar)
    print(f"critical c={c:g}: x*={xstar:.15f} overlap*={astar:.15f} distance*={dstar:.15f}")
    for N in (64, 128, 256, 512, 1024):
        rho = math.exp(-c / N)
        x, a, d, _ = discrete_first_mode(N, rho)
        print(f"  N={N:4d} rho={rho:.15f} x={x:.15f} overlap={a:.15f} distance={d:.15f}")


def report_regime(label, rho_fun):
    print(label)
    for N in (64, 128, 256, 512, 1024, 2048):
        rho = rho_fun(N)
        cN = N * (1.0 - rho)
        x, _, d, _ = discrete_first_mode(N, rho)
        print(f"  N={N:4d} c_N={cN:.9f} x={x:.12f} distance={d:.12f}")


def report_fixed_modes(c=1.0, N=2048, modes=4):
    rho = math.exp(-c / N)
    print(f"fixed-mode critical scaling c={c:g}, N={N}")
    for m in range(1, modes + 1):
        w = phase_root(N, rho, m)
        xN = N * w
        xstar = critical_root(c, m)
        lam_scaled = ar1_eigenvalue(rho, w) / N
        lam_limit = 2.0 * c / (c * c + xstar * xstar)
        print(
            f"  m={m}: N*w={xN:.12f} x*={xstar:.12f} "
            f"lambda/N={lam_scaled:.12f} limit={lam_limit:.12f}"
        )


if __name__ == "__main__":
    print(f"NumPy {np.__version__}")
    for c in (0.5, 1.0, 5.0):
        report_critical(c)
    print()
    report_fixed_modes()
    print()
    dense_matrix_check(1.0, 64)
    dense_matrix_check(1.0, 256)
    print()
    report_regime("DCT-side regime rho_N = 1 - N^{-2}", lambda N: 1.0 - N ** -2)
    print()
    report_regime("Dirichlet-side regime rho_N = 1 - N^{-1/2}", lambda N: 1.0 - N ** -0.5)
    a_inf = 2.0 * math.sqrt(2.0) / math.pi
    d_inf = math.sqrt(2.0 - 2.0 * a_inf)
    print(f"Dirichlet-side predicted overlap={a_inf:.15f} distance={d_inf:.15f}")
