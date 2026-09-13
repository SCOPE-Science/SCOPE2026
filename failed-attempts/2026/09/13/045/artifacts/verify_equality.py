"""Sanity checks for lane-1554: inverse-invariance of Hilbert length and w=g3^{-1} equality.

H(M) = log(|l1|/|l3|), eigenvalues ordered by decreasing modulus.
Checks:
 1. H(M) == H(M^{-1}) for generic loxodromic M in SL(3,R) (incl. totally positive M).
 2. Pants relation: with W = M1*M2 and M3 = W^{-1}, H(W) == H(M3).
 3. Fuchsian embeddings: reducible diag embedding gives H = cuff length l;
    principal Sym^2 embedding gives H = 2*l (matching is by H-values, so J(rho)
    exists for any prescribed triple of positive H's either way).
"""
import numpy as np


def H(M):
    ev = np.linalg.eigvals(M)
    m = np.sort(np.abs(ev))[::-1]
    assert m[0] > m[1] > m[2] > 0, f"not loxodromic: {m}"
    return float(np.log(m[0] / m[2]))


def sl3(M):
    d = float(np.linalg.det(M))
    assert d > 0, f"det must be positive, got {d}"
    return M / (d ** (1.0 / 3.0))


def totpos_seed(u1, u2, u3, l1, l2, l3, dd):
    n = 3
    U = np.eye(n)
    for (i, v) in ((0, u1), (1, u2), (0, u3)):
        E = np.eye(n)
        E[i, i + 1] = v
        U = U @ E
    L = np.eye(n)
    for (i, v) in ((1, l1), (0, l2), (1, l3)):
        E = np.eye(n)
        E[i + 1, i] = v
        L = E @ L
    return sl3(L @ np.diag(dd) @ U)


print("== 1. inverse invariance on totally positive matrices ==")
seeds = [(1.7, 0.9, 0.4, 1.3, 0.6, 0.5, (2.0, 1.0, 0.7)),
         (0.3, 2.1, 1.1, 0.8, 1.9, 0.2, (3.0, 1.0, 0.4)),
         (2.5, 0.2, 0.8, 1.1, 0.3, 1.4, (1.5, 1.0, 0.9))]
for t, s in enumerate(seeds):
    M = totpos_seed(*s)
    a, b = H(M), H(np.linalg.inv(M))
    print(f"  trial {t}: H(M)={a:.12f} H(M^-1)={b:.12f} diff={abs(a-b):.2e}")
    assert abs(a - b) < 1e-9

print("== 2. pants triple W=M1*M2, M3=W^-1 => H(W)==H(M3) ==")
M1 = totpos_seed(*seeds[0])
M2 = totpos_seed(*seeds[1])
W = M1 @ M2
M3 = np.linalg.inv(W)
a, b = H(W), H(M3)
print(f"  H(w)={a:.12f} H(g3)={b:.12f} diff={abs(a-b):.2e}")
assert abs(a - b) < 1e-12

print("== 3. Fuchsian embeddings ==")
for ell in (0.7, 1.5, 2.3):
    D = sl3(np.diag([np.exp(ell / 2), np.exp(-ell / 2), 1.0]))  # reducible, det 1
    print(f"  reducible: ell={ell} H={H(D):.12f} (expect {ell})")
    assert abs(H(D) - ell) < 1e-12
    ch, sh = np.cosh(ell / 2), np.sinh(ell / 2)
    A = np.array([[ch, sh], [sh, ch]])  # hyperbolic in SL(2,R)
    a, b, c, d = A.ravel()
    S = np.array([[a * a, 2 * a * b, b * b],   # Sym^2 (principal) embedding, det 1
                  [a * c, a * d + b * c, b * d],
                  [c * c, 2 * c * d, d * d]])
    assert abs(float(np.linalg.det(S)) - 1.0) < 1e-12
    print(f"  principal: ell={ell} H={H(S):.12f} (expect {2 * ell})")
    assert abs(H(S) - 2 * ell) < 1e-9

print("ALL CHECKS PASSED")
