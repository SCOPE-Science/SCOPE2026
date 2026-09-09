"""Convergence checks + geometry/phase variants (target-directed exploration).

Uses analytic-radial G + GL angular; deterministic tensor-GL center cubes
with refinement, plus tube-MC cross-checks.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

R0 = 4096.0
delta = 1.0 / 64.0
N = 48

NQ = 24
zq, wq = leggauss(NQ)
off = (delta / 2) * zq
qw = (delta / 2) * wq

def build(phis):
    n = len(phis)
    PHf = (phis[:, None] + off[None, :]).ravel()
    QW = np.tile(qw, n)
    return np.cos(PHf), np.sin(PHf), QW, np.repeat(np.arange(n), NQ)

def G(beta):
    beta = np.asarray(beta, dtype=complex)
    out = np.empty_like(beta)
    small = np.abs(beta) < 1e-2
    b = beta[~small]
    e1 = np.exp(1j * b); e2 = np.exp(1j * b * 0.5)
    ib = 1j * b
    out[~small] = e1 * (1.0 / ib + 1.0 / b**2) - e2 * (0.5 / ib + 1.0 / b**2)
    bs = beta[small]
    s = np.zeros_like(bs)
    from math import factorial
    for k in range(14):
        ck = (1.0 - 2.0**(-(k + 2))) / (k + 2) / factorial(k)
        s = s + ck * (1j * bs) ** k
    out[small] = s
    return out

def total_field(Y, cP, sP, QW, weights=None, chunk=3000):
    M = Y.shape[0]
    St = np.zeros(M, dtype=complex)
    for s in range(0, M, chunk):
        Yc = Y[s:s + chunk]
        beta = Yc[:, 0:1] * cP[None, :] + Yc[:, 1:2] * sP[None, :] + Yc[:, 2:3]
        E = G(beta) * QW[None, :]
        if weights is not None:
            E = E * weights[None, :]
        St[s:s + chunk] = E.sum(axis=1)
    return St

def cube_cube(a, n, cP, sP, QW, weights=None):
    z, w = leggauss(n)
    x = a * z; wx = a * w
    X, Yg, Z = np.meshgrid(x, x, x, indexing='ij')
    W3 = (wx[:, None, None] * wx[None, :, None] * wx[None, None, :]).ravel()
    Y = np.stack([X.ravel(), Yg.ravel(), Z.ravel()], axis=1)
    St = total_field(Y, cP, sP, QW, weights)
    return (W3 * np.abs(St) ** 6).sum()

phis_adj = np.arange(N) * delta
cP, sP, QW, JS = build(phis_adj)

print("== convergence: adjacent bunch center cube ==")
for a, n in [(8, 12), (8, 20), (8, 28), (16, 20), (16, 28), (16, 36)]:
    print(f"a={a} n={n}: {cube_cube(a, n, cP, sP, QW):.6e}")

print("== geometry variants, cube a=16 n=28 ==")
print("adjacent:", cube_cube(16, 28, cP, sP, QW))
# spread 48 evenly over full circle
phis_spr = np.linspace(0, 2 * np.pi, N, endpoint=False)
c2, s2, Q2, _ = build(phis_spr)
print("spread-full-circle:", cube_cube(16, 28, c2, s2, Q2))
# antipodal 24+24
phis_ant = np.concatenate([np.arange(24) * delta, np.pi + np.arange(24) * delta])
c3, s3, Q3, _ = build(phis_ant)
print("antipodal:", cube_cube(16, 28, c3, s3, Q3))
# random phases on adjacent (3 draws, fixed seed)
rng = np.random.default_rng(3)
sec_w = np.repeat(np.arange(N), NQ)
for t in range(3):
    th = rng.uniform(0, 2 * np.pi, N)
    w = np.exp(1j * th[sec_w])
    print(f"adjacent random-phase {t}:", cube_cube(16, 28, cP, sP, QW, w))
# full cone calibration: all 402 sectors, center cube
nsec = int(round(2 * np.pi / delta))
phis_full = np.arange(nsec) * delta
cF, sF, QF, _ = build(phis_full)
print("nsec_full =", nsec)
print("full-cone center cube:", cube_cube(16, 28, cF, sF, QF))
print("full-cone E(0):", QF.sum() * 0.375)
