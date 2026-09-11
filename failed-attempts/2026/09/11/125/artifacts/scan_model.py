"""Lane-1020 viability scan (MODEL evidence, not a certificate).

Target: normalized h_*=e^{ie1.x}phi_*, Re lam in [-0.03,-0.01], residual<=0.01
for cutoff hard spheres, T^3=(R/2piZ)^3.

Normalization fixed here (standard math-PDE Grad cutoff):
  M(v)=(2pi)^-3/2 exp(-|v|^2/2) (rho=1,T=1),
  B(|u|,cos)=|u| with b=1 (surface measure d-sigma on S^2, total 4pi),
  G_k = L - i*v1 on L^2(M dv), k=e1.
This is the TARGET-FRIENDLIEST standard choice (largest standard collision
strength -> smallest viscosity -> branches closest to the window).

Contents:
 1. First/second-Sonine transport numbers + Navier-Stokes branch Re at |k|=1
    and distances to window top (-0.03).
 2. Relaxation-model Galerkin (L_model=-nu(v)(I-P5), nu(v)=4pi*E|v-w| exactly
    quadratured, exact Hermite transport): branch locations with kinetic
    corrections + SVD pseudospectrum scan min_{lam in window} sigma_min(G-lam).
Run: python3 output/artifacts/scan_model.py
"""
import numpy as np
import json
from numpy.polynomial.hermite import hermgauss

OUT = "output/artifacts/scan_results.json"
PI = np.pi

# ---------------- 1. Sonine transport ----------------
mu1 = 5.0 / (64.0 * np.sqrt(PI))      # first Sonine, B=|u|,d_eff=2
mu2 = mu1 * 1.016                     # second-Sonine (~+1.6% for HS)
kap1 = 15.0 / 4.0 * mu1               # Pr=2/3 first approx
Gamma1 = 0.5 * (4.0 / 3.0 * mu1 + kap1 * (1.0 / 1.5 - 1.0 / 2.5))
chi1 = kap1 / 2.5
br = {
    "mu1": float(mu1), "mu2": float(mu2),
    "shear_Re": float(-mu1), "acoustic_Re": float(-Gamma1), "thermal_Re": float(-chi1),
    "d_shear": float(abs(-mu1 + 0.03)), "d_ac": float(abs(-Gamma1 + 0.03)),
    "d_th": float(abs(-chi1 + 0.03)),
}

# ---------------- 2. Galerkin with L_model ----------------
def gh3(order):
    x, w = hermgauss(order)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    Wx, Wy, Wz = np.meshgrid(w, w, w, indexing="ij")
    c = np.sqrt(2.0)
    return (c * X).ravel(), (c * Y).ravel(), (c * Z).ravel(), ((Wx * Wy * Wz) / (PI ** 1.5)).ravel()

def collision_freq(V1, V2, V3, order=8):
    x, w = hermgauss(order)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    Wx, Wy, Wz = np.meshgrid(w, w, w, indexing="ij")
    c = np.sqrt(2.0)
    W1 = (c * X).ravel(); W2 = (c * Y).ravel(); W3 = (c * Z).ravel()
    Wt = ((Wx * Wy * Wz) / (PI ** 1.5)).ravel()
    nu = np.empty_like(V1)
    CH = 256
    for a in range(0, len(V1), CH):
        b = min(a + CH, len(V1))
        d = np.sqrt((V1[a:b, None] - W1[None, :]) ** 2
                    + (V2[a:b, None] - W2[None, :]) ** 2
                    + (V3[a:b, None] - W3[None, :]) ** 2)
        nu[a:b] = 4.0 * PI * (d * Wt[None, :]).sum(axis=1)
    return nu

Q = 12
V1, V2, V3, W = gh3(Q)
NU = collision_freq(V1, V2, V3, order=8)
nu0_check = float(4.0 * PI * np.sqrt(8.0 / PI))  # analytic nu(0)

def Hn(n, v):
    # orthonormal probabilists' Hermite h_n
    H0 = np.ones_like(v); 
    if n == 0:
        return H0
    H1 = v.copy()
    if n == 1:
        return H1
    for k in range(1, n):
        H2 = v * H1 - k * H0
        H0, H1 = H1, H2
    import math
    return H1 / np.sqrt(float(math.factorial(n)))

NL, NT = 8, 8  # Hermite degrees 0..NL-1 (longitudinal), 0..NT-1 (transverse)
# longitudinal basis A[n,s]: h_n(v1)*t_s, t_0=1, t_1=(v2^2+v3^2-2)/2
LB = [(n, s) for n in range(NL) for s in (0, 1)]
nL = len(LB)
T2 = (V2 ** 2 + V3 ** 2 - 2.0) / 2.0
BL = np.array([Hn(n, V1) * (np.ones_like(V1) if s == 0 else T2) for (n, s) in LB])
# transverse basis B_n = v2*h_n(v1)
BT = np.array([V2 * Hn(n, V1) for n in range(NT)])

def Lmat(B, ovl, Ebase):
    # L_model = -nu + nu*P ; ovl[j,a] = <b_j, e_a>; Ebase[a] = e_a on grid
    K1 = (B * NU[None, :] * W[None, :]) @ B.T
    K2 = (B * NU[None, :] * W[None, :]) @ Ebase.T
    return -K1 + K2 @ ovl.T

def Tmat_herm(N):
    T = np.zeros((N, N))
    for n in range(N):
        if n + 1 < N:
            T[n + 1, n] += np.sqrt(n + 1); T[n, n + 1] += np.sqrt(n + 1)
    return T
import math
# longitudinal transport: block diag over s (v1 acts only on h_n)
TH = Tmat_herm(NL)
TL = np.zeros((nL, nL))
for i, (n, s) in enumerate(LB):
    for j, (m, sp) in enumerate(LB):
        if s == sp:
            TL[i, j] = TH[n, m] if (n < NL and m < NL) else 0.0
# overlaps <b, e_a>, a=(e0,e1,e4) for longitudinal
OL = np.zeros((nL, 3))
for i, (n, s) in enumerate(LB):
    OL[i, 0] = 1.0 if (n == 0 and s == 0) else 0.0
    OL[i, 1] = 1.0 if (n == 1 and s == 0) else 0.0
    OL[i, 2] = (np.sqrt(1.0 / 3.0) if (n == 2 and s == 0) else 0.0) + \
               (np.sqrt(2.0 / 3.0) if (n == 0 and s == 1) else 0.0)
TT = Tmat_herm(NT)
OT = np.zeros((NT, 1)); OT[0, 0] = 1.0  # <B_n, v2>

S = V1 ** 2 + V2 ** 2 + V3 ** 2 - 3.0
EL = np.array([np.ones_like(V1), V1, S / np.sqrt(6.0)])   # e0,e1,e4 (longitudinal)
ET = np.array([V2])                                        # e2 (transverse)
LL = Lmat(BL, OL, EL)
LT = Lmat(BT, OT, ET)
GL = LL - 1j * TL
GT = LT - 1j * TT

eL = np.linalg.eigvals(GL); eT = np.linalg.eigvals(GT)
eL = eL[np.argsort(-eL.real)]; eT = eT[np.argsort(-eT.real)]

# pseudospectrum scan over the target window (Re in [-0.03,-0.01])
res = np.linspace(-0.03, -0.01, 5)
ims = np.linspace(-2.0, 2.0, 161)
best = (1e9, None, None)
for re in res:
    for im in ims:
        lam = re + 1j * im
        sL = float(np.linalg.svd(GL - lam * np.eye(nL), compute_uv=False).min())
        sT = float(np.linalg.svd(GT - lam * np.eye(NT), compute_uv=False).min())
        s = min(sL, sT)
        if s < best[0]:
            best = (s, float(re), float(im))
# refine around best Im
for re in res:
    for im in np.linspace(best[2] - 0.05, best[2] + 0.05, 41):
        lam = re + 1j * im
        sL = float(np.linalg.svd(GL - lam * np.eye(nL), compute_uv=False).min())
        sT = float(np.linalg.svd(GT - lam * np.eye(NT), compute_uv=False).min())
        s = min(sL, sT)
        if s < best[0]:
            best = (s, float(re), float(im))

# eigenvector condition number of slowest transverse mode (pseudospectral factor)
wT, VR = np.linalg.eig(GT)
j = int(np.argmax(wT.real))
VL = np.linalg.inv(VR)
phi = VR[:, j]; psi = VL[j, :]
kappa = float(np.linalg.norm(phi) * np.linalg.norm(psi) / abs(psi @ phi))

out = {
    "normalization": "M unit Maxwellian; B=|u|, b=1, d-sigma surface (4pi); G=L-i v1",
    "sonine": br,
    "nu0_analytic": nu0_check,
    "nu_mean_model": float((NU * W).sum()),
    "galerkin_dims": {"long": int(nL), "trans": int(NT), "GH": Q},
    "slowest_long_eigs": [[float(z.real), float(z.imag)] for z in eL[:4]],
    "slowest_trans_eigs": [[float(z.real), float(z.imag)] for z in eT[:3]],
    "scan_min_sigma": float(best[0]),
    "scan_arglam": [best[1], best[2]],
    "slow_shear_condition_number": kappa,
}
with open(OUT, "w") as f:
    json.dump(out, f, indent=2)
print(json.dumps(out, indent=2))
