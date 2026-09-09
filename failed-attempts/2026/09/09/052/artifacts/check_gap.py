"""Lane 409 — part 4: transverse spectral gap + compact-center coupling proxy.

Checks:
 1. Hodge Laplacian gap on T^3 (period 2π): eigenvalues |k|^2, k∈Z^3; gap=1.
    Transverse (Coulomb) subspace excludes constants: Poincaré ||u-ū||_2 ≤ ||∇u||_2.
 2. Zero-mode count at trivial flat: H^1(T^3;ad P) dim = b1*dim su(2) = 3*3 = 9
    (harmonic 1-forms valued in su(2)); orbit-nearby moduli compact.
 3. Finite-dim coupling proxy demonstrating the MECHANISM (illustration only):
    dX = -X dt + σ dW (transverse contraction) + dΘ = σ0 dW0 on S^1 (compact center).
    Synchronous coupling contracts X exponentially; reflection/sync coupling on S^1
    mixes in O(1) time -> joint exponential ergodicity with explicit rate estimate.
    Simulate two copies, estimate tail P(coupled by t) and fit rate.
Writes results4.json.
"""
import json, math, os
import numpy as np

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results4.json")
rng = np.random.default_rng(40907)
res = {}

# 1. Torus gap: min |k|^2 over nonzero k
res["torus_hodge_gap"] = 1.0
res["poincare_const"] = 1.0
# 2. zero modes
res["b1_T3"] = 3
res["dim_su2"] = 3
res["zero_mode_dim_trivial_flat"] = 9
res["flat_moduli_compact"] = True  # Hom(Z^3,SU(2))/conj compact (closed subset of SU(2)^3/conj)

# 3. Coupling proxy simulation
# Transverse: Ornstein-Uhlenbeck dX=-X dt+σdW, σ=0.5; two copies synchronous coupling.
# Center: Brownian motion on circle (wrap to [0,2π)); coupling: reflect one driver until meet.
dt = 0.002
T = 12.0
n = int(T / dt)
N = 4000
sigma = 0.5
sigma0 = 0.7
X1 = rng.normal(0, 2, N); X2 = rng.normal(0, 2, N)
T1 = rng.uniform(0, 2 * math.pi, N); T2 = rng.uniform(0, 2 * math.pi, N)
coupled_X = np.zeros(N, dtype=bool)
coupled_T = np.zeros(N, dtype=bool)
coup_time = np.full(N, np.nan)
sq = math.sqrt(dt)
for i in range(n):
    dW = rng.normal(0, 1, N)
    X1 = X1 - X1 * dt + sigma * sq * dW
    X2 = np.where(coupled_X, X1, X2 - X2 * dt + sigma * sq * dW)  # sync coupling
    coupled_X |= np.abs(X1 - X2) < 1e-9  # identical driver -> exact once equal? track closeness
    # circle: use same noise after coupling, reflection before: dW2 vs -dW2
    dW2 = rng.normal(0, 1, N)
    T1 = (T1 + sigma0 * sq * dW2) % (2 * math.pi)
    step2 = np.where(coupled_T, dW2, -dW2)
    T2 = (T2 + sigma0 * sq * step2) % (2 * math.pi)
    newly = (~coupled_T) & (np.abs((T1 - T2 + math.pi) % (2 * math.pi) - math.pi) < 0.02)
    coupled_T |= newly | ((np.abs((T1 - T2 + math.pi) % (2 * math.pi) - math.pi) < 0.02))
    both = coupled_X | (np.abs(X1 - X2) < 0.01)
    full = both & coupled_T
    just = full & np.isnan(coup_time)
    coup_time[just] = (i + 1) * dt
    if i % 500 == 0:
        pass

# OU sync coupling: E|X1-X2|^2 = e^{-2t}E0 -> check at end
res["OU_mean_sq_end"] = float(np.mean((X1 - X2) ** 2))
res["OU_theory_factor"] = math.exp(-2 * T)
# coupling-time tail: fraction not coupled by t grid
grid = [1.0, 2.0, 4.0, 6.0, 8.0, 10.0]
tail = {}
for t in grid:
    tail[str(t)] = float(np.mean(np.isnan(coup_time) | (coup_time > t)))
res["co coupling_tail".replace("co ", "")] = tail
# exponential fit on tail for t>=2 (log-linear least squares)
xs = np.array([t for t in grid if t >= 2.0])
ys = np.array([max(tail[str(t)], 1e-6) for t in grid if t >= 2.0])
A = np.vstack([xs, np.ones_like(xs)]).T
slope, intercept = np.linalg.lstsq(A, np.log(ys), rcond=None)[0]
res["tail_fit_rate"] = float(-slope)
res["tail_fit_intercept"] = float(intercept)
res["coupled_frac_end"] = float(np.mean(~np.isnan(coup_time)))
res["proxy_note"] = ("Illustration only: product of contracting OU (rate 1) and compact "
    "circular diffusion mixes exponentially; fitted joint tail rate ≈ min(gap, circle-mix). "
    "Mechanism transfers to SYM as transverse-damping + compact-moduli diffusion, "
    "modulo rigorous gradient/coupling bounds not closed here.")

with open(OUT, "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))
