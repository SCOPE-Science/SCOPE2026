import numpy as np

np.set_printoptions(precision=12, suppress=True)


def lanczos_min_ritz(Q, v, m):
    """Return the smallest Ritz value after at most m Lanczos steps."""
    v = np.asarray(v, dtype=float)
    q = v / np.linalg.norm(v)
    q_prev = np.zeros_like(q)
    beta_prev = 0.0
    basis = []
    alpha = []
    beta = []

    for j in range(m):
        basis.append(q.copy())
        w = Q @ q - beta_prev * q_prev
        a = float(q @ w)
        w = w - a * q

        # Full reorthogonalization makes this finite-dimensional check reproducible.
        for p in basis:
            w = w - (p @ w) * p

        alpha.append(a)
        if j == m - 1:
            break

        b = float(np.linalg.norm(w))
        if b < 1e-14:
            break
        beta.append(b)
        q_prev, q = q, w / b
        beta_prev = b

    T = np.diag(alpha)
    for j, b in enumerate(beta):
        T[j, j + 1] = b
        T[j + 1, j] = b
    return float(np.linalg.eigvalsh(T)[0])


def signed_comparison(Q):
    """C_ii = Q_ii and C_ij = -abs(Q_ij) for i != j."""
    C = -np.abs(Q)
    np.fill_diagonal(C, np.diag(Q))
    return C


def collatz_gershgorin_bounds(Q, steps=100):
    C = signed_comparison(Q)
    mu = float(np.max(np.diag(Q)) + 1.0)
    A = mu * np.eye(Q.shape[0]) - C
    d = np.ones(Q.shape[0])
    bounds = []
    for _ in range(steps):
        d_next = A @ d
        U = float(np.max(d_next / d))
        bounds.append(mu - U)
        d = d_next
    return np.asarray(bounds), C


# 1. A finite-step Lanczos estimate can under-regularize.
m = 8
delta = 1e-2
Q_bad = np.diag(np.r_[-1.0, np.linspace(0.0, 0.5, m)])
v_bad = np.r_[1e-8, np.ones(m)]
lam_true = float(np.linalg.eigvalsh(Q_bad)[0])
lam_ritz = lanczos_min_ritz(Q_bad, v_bad, m)
M = max(1.0, float(np.linalg.norm(Q_bad, ord=np.inf)))
shift = -lam_ritz + delta * M
shifted_min = lam_true + shift

print("finite-Lanczos example")
print(f"lambda_min(Q)         = {lam_true: .12e}")
print(f"m-step min Ritz       = {lam_ritz: .12e}")
print(f"PDNQP-style shift     = {shift: .12e}")
print(f"lambda_min(Q+sI)      = {shifted_min: .12e}")
assert shifted_min < 0.0

# 2. Certified weighted-Gershgorin / Collatz bounds.
diag = np.array([0.2, -0.1, 0.4, 0.0, 0.3, -0.2])
off = np.array([0.4, 0.7, 0.5, 0.6, 0.3])
C = np.diag(diag)
for i, a in enumerate(off):
    C[i, i + 1] = C[i + 1, i] = -a

signature = np.diag([1.0, -1.0, -1.0, 1.0, -1.0, 1.0])
Q = signature @ C @ signature
bounds, C_check = collatz_gershgorin_bounds(Q, steps=100)
lam_Q = float(np.linalg.eigvalsh(Q)[0])
lam_C = float(np.linalg.eigvalsh(C_check)[0])

print("\ncertified bound example")
print(f"lambda_min(Q)         = {lam_Q: .12f}")
print(f"lambda_min(C(Q))      = {lam_C: .12f}")
for k in [0, 1, 2, 4, 9, 19, 49, 99]:
    print(f"L_{k:<2d}                  = {bounds[k]: .12f}")

assert np.all(bounds[1:] >= bounds[:-1] - 2e-14)
assert np.all(bounds <= lam_Q + 2e-13)
assert abs(lam_Q - lam_C) < 1e-13

eta = 1e-2
safe_shift = eta - min(float(bounds[-1]), 0.0)
safe_min = lam_Q + safe_shift
print(f"certified shift        = {safe_shift: .12f}")
print(f"lambda_min(Q+sI)       = {safe_min: .12f}")
assert safe_min >= eta - 1e-8
