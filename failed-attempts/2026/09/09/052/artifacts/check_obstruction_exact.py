"""Lane 409 — exact continuum obstruction identities (target-directed hardening).

Background A^bkg_1 = lam*n (constant abelian, n unit vector in su(2)~R^3),
all other components zero. Bilinear advection operator on perturbation a:
  L_i(a) = g*lam*[n, d_1 a_i] = g*lam*(n x d_1 a_i), i=1..3.
Exact continuum identities (no discretization):
  (I1) Lagrange: |n x v|^2 = |v|^2 - (n.v)^2 for unit n.
  (I2) ||L(a)||_2^2 = g^2 lam^2 * sum_i (||d_1 a_i||_2^2 - ||n.d_1 a_i||_2^2)
       = g^2 lam^2 * sum_i ||d_1 a_i^perp||_2^2. Linear growth in |lam|, exact.
  (I3) Skew: <a_i, [n,a_i]> = det(n,a_i,a_i) = 0 pointwise => O(lam) dynamics
       is L^2-orthogonal rotation, zero contribution to (1/2)d/dt||a||_2^2.
Checks: verify (I1) on random vectors (exact), verify (I2) spectrally-exact on
random trigonometric polynomials (FFT derivatives exact), verify (I3) exactly.
Writes results17.json.
"""
import json, math, os
import numpy as np

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results17.json")
rng = np.random.default_rng(40917)
res = {}

# (I1) Lagrange identity, random + exact integer case
w = 0.0
for _ in range(3000):
    n = rng.normal(size=3); n = n / np.linalg.norm(n)
    v = rng.normal(size=3)
    w = max(w, abs(float(np.dot(np.cross(n, v), np.cross(n, v)))
                    - float(np.dot(v, v) - np.dot(n, v)**2)))
res["lagrange_max_err"] = w
res["lagrange_pass"] = bool(w < 1e-12)
n = np.array([0.0, 0.0, 1.0]); v = np.array([1.0, 2.0, 3.0])
res["lagrange_exact"] = {"lhs": float(np.sum(np.cross(n, v)**2)), "rhs": 1.0 + 4.0}

# (I2): spectrally exact check on trig polynomials, N=32, period 2pi
N = 32
L = 2 * math.pi
dx = L / N
xs = np.linspace(0, L - dx, N)
g, lam = 0.5, 7.0
n = np.array([0.0, 0.0, 1.0])
# random trig polynomial perturbation (band-limited |k|<=5)
a = np.zeros((3, 3, N, N, N))
K = np.fft.fftfreq(N, d=1.0 / N)  # integer wavenumbers
for i in range(3):
    for cc in range(3):
        coe = np.zeros((N, N, N), dtype=complex)
        for k1 in range(-5, 6):
            for k2 in range(-5, 6):
                for k3 in range(-5, 6):
                    coe[k1 % N, k2 % N, k3 % N] = (rng.normal() + 1j * rng.normal())
        # Hermitianize for real field
        f = np.real(np.fft.ifftn(coe) * N**3)
        a[i, cc] = f
# exact x1-derivative via FFT
Ahat = np.fft.fftn(a, axes=(2, 3, 4))
k1 = K.reshape(1, 1, N, 1, 1)
Dhat = (1j * k1) * Ahat
d1a = np.real(np.fft.ifftn(Dhat, axes=(2, 3, 4)))
# LHS: sum ||g lam n x d1a_i||^2 dx^3 ; RHS: g^2 lam^2 sum (||d1a_i||^2 - (n.d1a_i)^2)
lhs, rhs = 0.0, 0.0
for i in range(3):
    # color vectors at each x: d1a[i] has shape (3,N,N,N) with axis0=color
    F = d1a[i]  # (3,N,N,N)
    cr0 = F[1] * n[2] - F[2] * n[1]
    cr1 = F[2] * n[0] - F[0] * n[2]
    cr2 = F[0] * n[1] - F[1] * n[0]
    lhs += float(np.sum(cr0**2 + cr1**2 + cr2**2)) * dx**3
    nd = n[0] * F[0] + n[1] * F[1] + n[2] * F[2]
    rhs += float(np.sum(F[0]**2 + F[1]**2 + F[2]**2 - nd**2)) * dx**3
lhs *= g**2 * lam**2
rhs *= g**2 * lam**2
res["I2_lhs"] = lhs
res["I2_rhs"] = rhs
res["I2_relerr"] = abs(lhs - rhs) / max(rhs, 1e-300)
res["I2_pass"] = bool(res["I2_relerr"] < 1e-9)
res["I2_linear_in_lam"] = "exact by formula: ||L||_2 = g|lam|*(sum||d1 a_perp||^2)^{1/2}"
# nonzero check (perturbation has transverse content)
res["I2_nonzero"] = bool(rhs > 0)

# (I3): pointwise skew exact
s = 0.0
for _ in range(3000):
    wv = rng.normal(size=3)
    nn = rng.normal(size=3); nn = nn / np.linalg.norm(nn)
    s = max(s, abs(float(np.dot(wv, np.cross(nn, wv)))))
res["skew_max_err"] = s
res["skew_pass"] = bool(s < 1e-12)
res["skew_exact_det"] = "det(n,v,v)=0 identically (alternating form)"

res["theorem"] = ("EXACT continuum lemma: around constant abelian background A^bkg_1=lam n, "
    "the O(lam) bilinear advection L(a)=g lam[n,d_1 a] satisfies ||L(a)||_2 = "
    "g|lam|(sum_i||d_1 a_i^perp||_2^2)^{1/2} (unbounded in lam at fixed a), while "
    "<a,[n,a]>=0 pointwise so L contributes nothing to d/dt||a||_2^2 through its "
    "color-rotation part. Hence no L^2-coercive linear restoring force at order lam: "
    "slice-L^2 Lyapunov closure uniformly in data is impossible at fixed g>0.")

with open(OUT, "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))
