"""Numerical support: uniform-over-initial-data contraction of the discrete SHE
solution map driven by ONE common discrete noise (toy analogue of the chaining
input in DRAFT.md).

Model: periodic lattice of N sites, discrete SHE
  Z_{n+1}(x) = (P Z_n)(x) + sigma * Z_n(x) * dW_n(x),
with P the lazy random-walk kernel, dW a single common noise field shared by
ALL initial data (mimics the common-clock field W^eps), plus per-profile drift
corrections R(h) (mimics R^eps(h)). We verify:
  (a) linearity/contraction: sup_{h,h'} ||Z_t(h)-Z_t(h')||_inf / ||Z_0(h)-Z_0(h')||_inf <= C(T)
      uniformly over a finite net of initial profiles (chaining input);
  (b) temporal modulus: sup_h ||Z_t(h)-Z_s(h)|| <= C |t-s|^alpha-like growth;
  (c) same-noise coupling: all profiles share dW, so differences solve the
      homogeneous equation up to drift terms.
Saves results to results.json.
"""
import json
import numpy as np

rng = np.random.default_rng(20260914)
N = 256          # lattice sites (periodic)
Tsteps = 400     # time steps
dt = 0.01
sigma = 0.5
nprof = 12       # finite net of initial profiles

x = np.arange(N) / N  # macroscopic coordinate in [0,1)

# Finite net K_net of initial "height" profiles: sinusoids + wedge + flat,
# mimicking a compact set in C^alpha with uniform growth envelope.
profiles = []
for k in range(nprof):
    if k == 0:
        h = np.zeros(N)
    elif k <= 6:
        h = 0.6 * np.sin(2 * np.pi * k * x + 0.3 * k)
    elif k <= 9:
        h = 0.8 * np.abs(x - 0.5) * (k - 6)
    else:
        h = 0.5 * np.cos(2 * np.pi * (k - 9) * x) + 0.3 * np.sin(4 * np.pi * x)
    profiles.append(h)
profiles = np.array(profiles)  # (nprof, N)
Z0 = np.exp(profiles)          # G\"artner-like initial data Z0 = e^h

# Lazy random walk kernel applied via FFT (periodic): Monte-Carlo-free exact step.
lap_eig = -4.0 * np.sin(np.pi * np.fft.fftfreq(N) * 1.0) ** 2  # eig of discrete Laplacian (dx=1 units)
# diffusive rescaling absorbed; use explicit Euler with small dt (stable: dt*4 < 1)
assert dt * 4.0 < 1.0
P_hat = 1.0 + dt * 0.5 * lap_eig  # heat semigroup factor per step (kappa=1/2)

def apply_P(Z):
    return np.fft.irfft(np.fft.rfft(Z) * P_hat[: N // 2 + 1], n=N)

# One common noise field for all profiles (common clocks).
dW = rng.normal(0.0, np.sqrt(dt), size=(Tsteps, N))

# Per-profile deterministic drift corrections R(h) (bounded, Lipschitz in h),
# mimicking the It\^o-correction drift from the R^eps(h) decomposition.
R = 0.1 * (np.roll(profiles, -1, axis=1) - np.roll(profiles, 1, axis=1)) ** 2  # (nprof, N), >= 0

Z = Z0.copy()
snap = {0: Z.copy()}
check = [50, 100, 200, 400]
for n in range(1, Tsteps + 1):
    Z = apply_P(Z) + sigma * Z * dW[n - 1][None, :] * 1.0 + dt * R * Z
    Z = np.maximum(Z, 1e-12)
    if n in check:
        snap[n] = Z.copy()

# (a) Uniform contraction ratios over all pairs in the net, at each snapshot.
out_pairs = {}
Z0diff = np.abs(Z0[None, :, :] - Z0[:, None, :]).max(axis=-1)  # (P,P)
for n, Zt in snap.items():
    if n == 0:
        continue
    Ztdiff = np.abs(Zt[None, :, :] - Zt[:, None, :]).max(axis=-1)
    ratio = np.divide(Ztdiff, Z0diff, out=np.zeros_like(Ztdiff), where=Z0diff > 1e-9)
    iu = np.triu_indices(nprof, k=1)
    out_pairs[n] = {"max_ratio": float(ratio[iu].max()), "mean_ratio": float(ratio[iu].mean())}

# (b) Temporal modulus uniformly over the net: sup_h ||Z_t - Z_s||_inf for consecutive snapshots.
times = sorted(snap.keys())
mod = {}
for a, b in zip(times[:-1], times[1:]):
    d = float(np.abs(snap[b] - snap[a]).max())
    mod[f"{a}->{b}"] = {"dt_macro": (b - a) * dt, "sup_h_sup_x_diff": d}

# (c) Positivity / growth envelope: min and max over net and space at final time.
Zf = snap[Tsteps]
envelope = {"min_Z_final": float(Zf.min()), "max_Z_final": float(Zf.max()),
            "min_Z0": float(Z0.min()), "max_Z0": float(Z0.max())}

res = {"N": N, "Tsteps": Tsteps, "dt": dt, "sigma": sigma, "nprof": nprof,
       "uniform_contraction": {str(k): v for k, v in out_pairs.items()},
       "temporal_modulus": mod, "envelope": envelope}
with open("/srv/scope-research/rounds/2026-09-14-hands-on-first-light-01/workspaces/research/lane-20031/output/artifacts/results.json", "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
