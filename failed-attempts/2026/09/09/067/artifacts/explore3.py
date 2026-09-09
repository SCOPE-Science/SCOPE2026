"""Tube-adapted importance-sampled L6 estimates for 48-sector adjacent bunch."""
import numpy as np
from numpy.polynomial.legendre import leggauss

R0 = 4096.0
delta = 1.0 / 64.0
N = 48
phis = np.arange(N) * delta

NQ = 40
zq, wq = leggauss(NQ)
off = (delta / 2) * zq
qw = (delta / 2) * wq
PH = (phis[:, None] + off[None, :])
PHf = PH.ravel()
QW = np.tile(qw, N)
cP = np.cos(PHf); sP = np.sin(PHf)

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

def fields(Y, pack=None):
    beta = Y[:, 0:1] * cP[None, :] + Y[:, 1:2] * sP[None, :] + Y[:, 2:3]
    E = G(beta) * QW[None, :]
    Ep = E.reshape(Y.shape[0], N, NQ).sum(axis=2)
    if pack is not None:
        return Ep[:, pack]
    return Ep.sum(axis=1), Ep

# tube frames
D = np.stack([np.cos(phis), np.sin(phis), np.ones(N)], axis=1) / np.sqrt(2)
E1 = np.stack([-np.sin(phis), np.cos(phis), np.zeros(N)], axis=1)
E2 = np.stack([-np.cos(phis), -np.sin(phis), np.ones(N)], axis=1) / np.sqrt(2)

W = 256.0
Vb = 2 * R0 * (2 * W) ** 2
print("tube box vol:", Vb, " ball vol:", 4/3*np.pi*R0**3)

def coords_of(Y):
    """Return s,u,v arrays (M,N)."""
    s = Y @ D.T
    u = Y @ E1.T
    v = Y @ E2.T
    return s, u, v

def coverage(Y):
    s, u, v = coords_of(Y)
    inside = (np.abs(s) <= R0) & (np.abs(u) <= W) & (np.abs(v) <= W)
    return inside.sum(axis=1), inside

rng = np.random.default_rng(7)

# ---- denominator: single packet 0 ----
M = 40000
j = 0
s = rng.uniform(-R0, R0, M)
u = rng.uniform(-W, W, M)
v = rng.uniform(-W, W, M)
Y = (s[:, None] * D[j][None, :] + u[:, None] * E1[j][None, :]
     + v[:, None] * E2[j][None, :])
F0 = fields(Y, pack=0)
g = np.abs(F0) ** 6
I_box = Vb * g.mean()
se = Vb * g.std(ddof=1) / np.sqrt(M)
print("single packet: box integral =", I_box, " SE=", se)
print("  maxfrac:", g.max() / g.sum() * M)

# tail probe: sample ball outside box0, estimate tail of |F0|^6
M3 = 60000
Z = rng.normal(size=(M3, 3)); Z /= np.linalg.norm(Z, axis=1, keepdims=True)
Yb = Z * (rng.random((M3, 1)) ** (1/3)) * R0
cov, _ = coverage(Yb[:1])
cov, _ = coverage(Yb)
out = cov == 0
print("frac outside all boxes:", out.mean())
F0b = fields(Yb, pack=0)
gt = np.abs(F0b) ** 6
vol = 4/3*np.pi*R0**3
print("single tail probe: vol*mean_out =", vol * (gt[out].sum() / M3),
      " frac pts out:", out.mean())

# ---- numerator: mixture over tube boxes ----
M = 60000
js = rng.integers(0, N, M)
s = rng.uniform(-R0, R0, M)
u = rng.uniform(-W, W, M)
v = rng.uniform(-W, W, M)
Y = (s[:, None] * D[js] + u[:, None] * E1[js] + v[:, None] * E2[js])
St, _ = fields(Y)
n, _ = coverage(Y)
n = np.maximum(n, 1)
g = np.abs(St) ** 6
est = g * (N * Vb / n)
I_num = est.mean()
se = est.std(ddof=1) / np.sqrt(M)
print("numerator union integral =", I_num, " SE=", se)
print("  maxfrac:", est.max() / est.sum() * M)

# background probe for total field
Stb, _ = fields(Yb)
gb = np.abs(Stb) ** 6
print("total-field background probe: vol*mean_out =", vol * (gb[out].sum() / M3))
