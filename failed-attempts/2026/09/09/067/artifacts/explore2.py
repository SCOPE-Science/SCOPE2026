"""Reliable L6 ratio for 48-sector adjacent bunch: analytic radial integral + GL angular.

F_j(y) = int_{phi in sector j} G(beta(phi)) dphi, beta = y1 cos+ y2 sin + y3,
G(b) = int_{1/2}^1 r e^{i b r} dr  (closed form, stable branch at b=0).
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

R0 = 4096.0
delta = 1.0 / 64.0
N = 48
phis = np.arange(N) * delta

NQ = 48
zq, wq = leggauss(NQ)
off = (delta / 2) * zq
qw = (delta / 2) * wq

def G(beta):
    beta = np.asarray(beta, dtype=complex)
    out = np.empty_like(beta)
    small = np.abs(beta) < 1e-2
    b = beta[~small]
    # [e^{ibr}(r/(ib)+1/b^2)]_{1/2}^1
    e1 = np.exp(1j * b * 1.0); e2 = np.exp(1j * b * 0.5)
    out[~small] = e1 * (1.0 / (1j * b) + 1.0 / b**2) - e2 * (0.5 / (1j * b) + 1.0 / b**2)
    bs = beta[small]
    # Taylor: sum_{k>=0} (ib)^k/k! * (1-2^{-(k+2)})/(k+2)
    s = np.zeros_like(bs)
    for k in range(12):
        from math import factorial
        ck = (1.0 - 2.0**(-(k + 2))) / (k + 2) / factorial(k)
        s = s + ck * (1j * bs) ** k
    out[small] = s
    return out

# sanity: G(0) = (1-1/8)/2 = 0.4375
print("G0 check:", G(np.array([0.0]))[0], "expect 0.4375")
print("G(1.0):", G(np.array([1.0]))[0], " numeric:",
      np.sum(np.linspace(0.5, 1, 200001) * np.exp(1j * np.linspace(0.5, 1, 200001))) / 200000 * 0.5)

# all angular nodes
PH = (phis[:, None] + off[None, :])  # (N,NQ)
QW = np.tile(qw, N)                  # (N*NQ,)
PHf = PH.ravel()
cP = np.cos(PHf); sP = np.sin(PHf)

def fields(Y):
    """Y:(M,3) -> Stot (M,), Ep (M,N)."""
    beta = Y[:, 0:1] * cP[None, :] + Y[:, 1:2] * sP[None, :] + (Y[:, 2:3]) * 1.0
    E = G(beta) * QW[None, :]
    Ep = E.reshape(Y.shape[0], N, NQ).sum(axis=2)
    return Ep.sum(axis=1), Ep

# origin check: E(0) = N * 0.4375 * delta
E0, _ = fields(np.zeros((1, 3)))
print("E(0):", E0[0], " expect:", N * 0.4375 * delta)

rng = np.random.default_rng(1)
vol = 4.0 / 3.0 * np.pi * R0 ** 3

def ball(n):
    Z = rng.normal(size=(n, 3)); Z /= np.linalg.norm(Z, axis=1, keepdims=True)
    return Z * (rng.random((n, 1)) ** (1.0 / 3.0)) * R0

# single packet norm: dedicated large MC (packet 0 only)
M1 = 60000
Y = ball(M1)
_, Ep = fields(Y)
F0 = Ep[:, 0]
m6 = np.mean(np.abs(F0) ** 6)
# batch SE
b = np.abs(F0) ** 6
nb = 12
bm = b.reshape(nb, -1).mean(axis=1)
print("single: mean|F|^6 =", m6, " SE~", bm.std(ddof=1) / np.sqrt(nb))
n0 = (vol * m6) ** (1.0 / 6.0)
print("n0 =", n0, " denom=sqrt(48)n0 =", np.sqrt(N) * n0)
print("single |F|^6: max frac of sum:", b.max() / b.sum() * M1, " q99.9:", np.quantile(b, 0.999) / m6)

# total field
M2 = 60000
Y = ball(M2)
St, _ = fields(Y)
t = np.abs(St) ** 6
mt = t.mean()
tm = t.reshape(nb, -1).mean(axis=1)
print("total: mean|E|^6 =", mt, " SE~", tm.std(ddof=1) / np.sqrt(nb))
num = (vol * mt) ** (1.0 / 6.0)
print("num =", num, " RATIO =", num / (np.sqrt(N) * n0))
print("total |E|^6: maxfrac:", t.max() / t.sum() * M2, " q99.9/mean:", np.quantile(t, 0.999) / mt)
