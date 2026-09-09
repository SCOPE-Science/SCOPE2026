"""Deterministic cube integrals of |E|^6 and |F0|^6 via tensor Gauss-Legendre.

Frequency side: exact radial G + GL(16) in phi per sector (smooth for |y|<=~100).
Spatial side: tensor GL(n) on [-a,a]^3. Scan a to find concentration scale.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

R0 = 4096.0
delta = 1.0 / 64.0
N = 48
phis = np.arange(N) * delta

NQ = 16
zq, wq = leggauss(NQ)
off = (delta / 2) * zq
qw = (delta / 2) * wq
PHf = (phis[:, None] + off[None, :]).ravel()
QW = np.tile(qw, N)
cP = np.cos(PHf); sP = np.sin(PHf)
JSEC = np.repeat(np.arange(N), NQ)

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
    for k in range(12):
        ck = (1.0 - 2.0**(-(k + 2))) / (k + 2) / factorial(k)
        s = s + ck * (1j * bs) ** k
    out[small] = s
    return out

def fields(Y, chunk=4000):
    """Y:(M,3) -> Stot, Ep0 (packet-0 field). Chunked over spatial points."""
    M = Y.shape[0]
    St = np.zeros(M, dtype=complex)
    E0 = np.zeros(M, dtype=complex)
    m0 = (JSEC == 0)
    for s in range(0, M, chunk):
        Yc = Y[s:s + chunk]
        beta = Yc[:, 0:1] * cP[None, :] + Yc[:, 1:2] * sP[None, :] + Yc[:, 2:3]
        E = G(beta) * QW[None, :]
        St[s:s + chunk] = E.sum(axis=1)
        E0[s:s + chunk] = E[:, m0].sum(axis=1)
    return St, E0

def cube_integral(a, n):
    z, w = leggauss(n)
    x = a * z
    wx = a * w
    X, Yg, Z = np.meshgrid(x, x, x, indexing='ij')
    W3 = (wx[:, None, None] * wx[None, :, None] * wx[None, None, :]).ravel()
    Y = np.stack([X.ravel(), Yg.ravel(), Z.ravel()], axis=1)
    St, E0 = fields(Y)
    return (W3 * np.abs(St) ** 6).sum(), (W3 * np.abs(E0) ** 6).sum()

for a, n in [(4, 16), (8, 20), (16, 28), (32, 44)]:
    It, I0 = cube_integral(a, n)
    print(f"a={a:3d} n={n:2d}  cube|E|^6={It:.6e}  cube|F0|^6={I0:.6e}  "
          f"implied-ratio-lower={It**(1/6)/(np.sqrt(N)*0.09):.3f} (using n0~0.09 placeholder)")
