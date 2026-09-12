"""Replay for lane-1103: constants + Galerkin energy check (numpy + stdlib only).

Model: scalar fractional Burgers on T^2=(R/Z)^2, zero-mean:
  du = [-A u - P (e.grad)(u^2/2)] dt + P dW,  A = (-Delta)^{5/4},
with Fourier truncation |k|<=Kc. Wick constant drops (gradient kills constants).
Physics convention: uh = fft(u)/G^2 coeffs, mean(u^2)=sum|uh|^2.
"""
import json, math, numpy as np

rng = np.random.default_rng(0)

# ---- 1. Closed-form constants ----
gamma = (2 * math.pi) ** 2.5          # Poincare gap of A on zero-mean fields
print(f"gamma = (2pi)^(5/2) = {gamma:.6f}")
assert 98.0 < gamma < 100.0, gamma
for TrQ in [0.5, 1.0, 50.0]:
    K = max(1.0, TrQ / (2 * gamma))
    print(f"TrQ={TrQ}: K=max(1,TrQ/2g)={K:.6f}")

# ---- 2. Compact-embedding tail factor: H^{5/4}-ball -> C^{-kappa} ----
def tail(J, s, kappa):
    return 2.0 ** (-J * (s + kappa - 1.0))
for kappa in [0.25, 0.5, 1.0]:
    t = tail(6, 1.25, kappa)
    print(f"kappa={kappa}: tail J=6 factor={t:.3e}")
    assert t < 1.0

# ---- 3. Galerkin energy check ----
G, Kc, dt, steps, trials = 16, 5, 0.002, 2000, 20
TrQ = 50.0
K1, K2 = np.meshgrid(np.fft.fftfreq(G, d=1.0 / G), np.fft.fftfreq(G, d=1.0 / G), indexing='ij')
Ksq = K1 ** 2 + K2 ** 2
mask = (Ksq <= Kc ** 2) & (Ksq > 0)
A = np.where(mask, (2 * math.pi * np.sqrt(np.where(Ksq > 0, Ksq, 1))) ** 2.5, 0.0)
qk = np.where(mask, (1.0 + Ksq) ** (-3.0), 0.0)
qk *= TrQ / qk.sum()
sq = np.sqrt(qk)
nmodes = int(mask.sum())
# linear OU stationary mean-energy (nonlinearity only redistributes; bound uses Poincare)
lin_stat = float((qk / (2 * np.where(mask, A, 1))).sum())
print(f"modes={nmodes}, linear-theory stationary mean-energy={lin_stat:.6f}")
assert lin_stat > 1e-4, "noise too weak to be a meaningful check"

def hermitian_noise():
    Z = rng.standard_normal((G, G)) + 1j * rng.standard_normal((G, G))
    Z = Z / np.sqrt(2.0)          # unit variance per complex mode
    H = np.zeros_like(Z)
    for i in range(G):
        for j in range(G):
            ii, jj = (-i) % G, (-j) % G
            if (ii, jj) >= (i, j):
                H[i, j] = Z[i, j]
                H[ii, jj] = np.conj(Z[i, j])
    # fix self-conjugate modes to be real
    for (i, j) in [(0, 0), (0, G // 2), (G // 2, 0), (G // 2, G // 2)]:
        H[i, j] = Z[i, j].real
    return H  # unit variance per mode -> increment sqrt(dt)*sq*H has Var dt*qk

def to_phys(uh):
    return np.fft.ifft2(uh * G ** 2).real

def to_spec(u):
    return np.fft.fft2(u) / G ** 2

def nonlinearity(u):
    uh = to_spec(u)
    uh[~mask] = 0
    u2 = to_phys(uh) ** 2 / 2.0
    w2h = to_spec(u2)
    B = to_phys((2j * math.pi * K1) * w2h * np.where(mask, 1, 0))
    return B - B.mean()

# exact cancellation on a fixed smooth field
X, Y = np.meshgrid(np.arange(G) / G, np.arange(G) / G, indexing='ij')
u_test = np.sin(2 * math.pi * X) * np.cos(2 * math.pi * (X + Y)) + 0.5 * np.cos(4 * math.pi * Y)
ip = float((u_test * nonlinearity(u_test)).mean())
print(f"cancellation <u,B> = {ip:.3e}")
assert abs(ip) < 1e-10, ip

V0 = 0.25
u0 = np.sin(2 * math.pi * X) * np.cos(2 * math.pi * Y)
u0 -= u0.mean()
u0 *= math.sqrt(V0 / (u0 ** 2).mean())
Kbound = max(1.0, TrQ / (2 * gamma)) * (1.0 + V0)
Emax, Esum = 0.0, 0.0
for _ in range(trials):
    uh = to_spec(u0)
    for _ in range(steps):
        Bh = to_spec(nonlinearity(to_phys(uh)))
        uh = (uh - dt * np.where(mask, Bh, 0)
              + math.sqrt(dt) * sq * hermitian_noise() * np.where(mask, 1, 0)) / (1.0 + dt * A)
        uh[0, 0] = 0
    E = float((to_phys(uh) ** 2).mean())
    Emax = max(Emax, E)
    Esum += E
print(f"trials={trials}: max terminal mean-energy={Emax:.6f}, mean={Esum/trials:.6f} vs bound {Kbound:.4f}")
assert Esum / trials > 0.1 * lin_stat, "dynamics collapsed: noise not sustaining energy"
assert Emax < Kbound, (Emax, Kbound)

with open("output/artifacts/ledger.json", "w") as f:
    json.dump({"gamma": gamma, "Kbound_V0_0.25_TrQ50": Kbound,
               "cancellation_inner": ip, "sim_max_energy": Emax,
               "sim_mean_energy": Esum / trials, "linear_theory": lin_stat,
               "params": {"G": G, "Kc": Kc, "dt": dt, "steps": steps, "trials": trials}},
              f, indent=2)
print("VERIFY_OK")
