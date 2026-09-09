"""Explore true L6 ratio for bunched cone packets (NOT certificate; MC exploration)."""
import numpy as np
from numpy.polynomial.legendre import leggauss

R0 = 4096.0
delta = 1.0 / 64.0
N = 48
phis = np.arange(N) * delta

# Gauss-Legendre frequency quadrature per sector
nr, np_ = 8, 8
zr, wr = leggauss(nr)
zp, wp = leggauss(np_)
r_nodes = 0.75 + 0.25 * zr          # [0.5,1]
r_w = 0.25 * wr
o_nodes = (delta / 2) * zp          # offsets
o_w = (delta / 2) * wp

# Build all frequency nodes: (N*nr*np_, 3), weights
F_list, W_list, J_list = [], [], []
for j, ph in enumerate(phis):
    for a in range(nr):
        for b in range(np_):
            r = r_nodes[a]; o = o_nodes[b]
            phi = ph + o
            F_list.append([r * np.cos(phi), r * np.sin(phi), r])
            W_list.append(r * r_w[a] * o_w[b])
            J_list.append(j)
F = np.array(F_list); W = np.array(W_list); J = np.array(J_list)
print("freq nodes:", F.shape, "total cap area approx:", W.sum())

def fields(Y):
    """Y: (M,3). Returns Stot (M,), Epack (M,N)."""
    Ph = Y @ F.T
    E = np.exp(1j * Ph) * W[None, :]
    Ep = np.zeros((Y.shape[0], N), dtype=complex)
    for j in range(N):
        Ep[:, j] = E[:, J == j].sum(axis=1)
    return Ep.sum(axis=1), Ep

rng = np.random.default_rng(0)
vol = 4.0 / 3.0 * np.pi * R0 ** 3

# --- denominator: single packet L6 via tube-adapted sampling ---
# packet 0 tube axis: (cos0,sin0,1)=(1,0,1)/... direction d=(1,0,1)/sqrt2
# sample uniform in ball, MC estimate of mean |F0|^6
M = 120000
Z = rng.normal(size=(M, 3)); nrm = np.linalg.norm(Z, axis=1, keepdims=True)
U = rng.random((M, 1)) ** (1.0 / 3.0)
Y = Z / nrm * U * R0
_, Ep = fields(Y)
F0 = Ep[:, 0]
m6 = np.mean(np.abs(F0) ** 6)
n0 = (vol * m6) ** (1.0 / 6.0)
print("single-packet mean|F|^6 =", m6, " n0 =", n0, " denom =", np.sqrt(N) * n0)

# --- numerator: total field MC over ball (will be noisy; just rough) ---
St, _ = fields(Y)
mt = np.mean(np.abs(St) ** 6)
num = (vol * mt) ** (1.0 / 6.0)
print("total mean|E|^6 =", mt, " num =", num, " ratio =", num / (np.sqrt(N) * n0))

# --- numerator detail: central region profile along axes ---
for rho in [2, 5, 10, 20, 40, 80]:
    Mm = 60000
    Z = rng.normal(size=(Mm, 3)); nrm = np.linalg.norm(Z, axis=1, keepdims=True)
    U = rng.random((Mm, 1)) ** (1.0 / 3.0)
    Yc = Z / nrm * U * rho
    Stc, _ = fields(Yc)
    volc = 4.0 / 3.0 * np.pi * rho ** 3
    print(f"rho={rho} central integral ~ {(volc*np.mean(np.abs(Stc)**6)):.6f}")
