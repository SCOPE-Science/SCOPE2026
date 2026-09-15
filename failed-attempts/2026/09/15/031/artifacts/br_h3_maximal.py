"""Recovery test v2: maximal Bochner-Riesz envelope on H^3 (numpy only).
Probes: (a) kernel-envelope growth (R2 fate); (b) round-trip with fitted constant;
(c) ENVELOPE L2 mass of nested spikes from adversarial F (p=2 maximal probe);
(d) A2-weight diagnostic (R3 obstruction).
Writes output/artifacts/br_h3_results.json
"""
import json
import numpy as np

ART = "/srv/scope-research/rounds/2026-09-14-hands-on-first-light-01/workspaces/research/lane-20226/output/artifacts"
res = {}

# ---------- (a) Closed-form kernel envelope ----------
Agrid = np.linspace(0.05, 160, 4000)
env = {}
for r in [0.5, 1.0, 2.0]:
    K = np.sin(Agrid * r) / r**2 - Agrid * np.cos(Agrid * r) / r
    run = np.maximum.accumulate(np.abs(K))
    env[str(r)] = [float(run[np.searchsorted(Agrid, a)]) for a in [10, 20, 40, 80, 160]]
res["a_kernel_envelope_max_vs_Amax"] = env
res["a_envelope_over_Amax_at_160"] = {k: v[-1] / 160.0 for k, v in env.items()}

# ---------- (b) Round-trip with fitted inversion constant ----------
r = np.linspace(0, 12, 2401); dr = r[1] - r[0]
f = np.exp(-r**2 / 2.0)
lam = np.linspace(0, 25, 2501); dlam = lam[1] - lam[0]
with np.errstate(divide="ignore", invalid="ignore"):
    Smat = np.where(lam[:, None] == 0, r[None, :],
                    np.sin(lam[:, None] * r[None, :]) / np.maximum(lam[:, None], 1e-300))
M = np.sinh(r)[None, :] * Smat
fhat = M @ (f * dr)
F = fhat * lam
sh = np.sinh(np.maximum(r, 1e-12))
raw = (Smat.T @ F) * dlam / sh
m = r <= 6
cfit = float((raw[m] @ f[m]) / (raw[m] @ raw[m]))
rel = float(np.sqrt(np.sum((cfit * raw[m] - f[m])**2) / np.sum(f[m]**2)))
res["b_inversion_constant_fit"] = {"cfit": cfit, "rel_L2_err_r_le_6": rel}

# ---------- (c) Envelope L2 mass: nested spikes, adversarial F ----------
Lam = np.linspace(0, 320, 32001); dl = Lam[1] - Lam[0]
Fadv = np.where(Lam >= 1.0, Lam**-0.5 / np.log1p(Lam), 0.0)
L2F = float(np.sqrt(np.sum(Fadv**2) * dl))
r3 = np.linspace(0, 1.0, 2001)
sh3 = np.sinh(np.maximum(r3, 1e-12)); w3 = np.sinh(r3)**2 * (r3[1] - r3[0])
S3 = np.sin(Lam[:, None] * r3[None, :])
Avals = np.array([10, 20, 40, 80, 160, 320])
gos = []
for A in Avals:
    idx = Lam <= A
    g = (S3[idx, :].T @ Fadv[idx]) * dl / sh3
    g[0] = float((Fadv[idx] * Lam[idx]).sum() * dl)
    gos.append(np.abs(g))
gos = np.array(gos)
run = np.maximum.accumulate(gos, axis=0)
envmass = [float(np.sqrt(np.sum(run[k]**2 * w3))) for k in range(len(Avals))]
singlemass = [float(np.sqrt(np.sum(gos[k]**2 * w3))) for k in range(len(Avals))]
res["c_nested_spike"] = {"L2_norm_F_up_to_const": L2F,
                         "Amax": [float(a) for a in Avals],
                         "single_scale_L2_mass": singlemass,
                         "envelope_L2_mass": envmass,
                         "origin_spike_height": [float(g[0]) for g in gos]}

# ---------- (d) A2 diagnostic for l^2 weight ----------
def ap_ratio(a, b):
    xs = np.linspace(a, b, 20001); wgt = xs**2
    return float(wgt.mean() * (1.0 / wgt).mean())
res["d_A2_ratio_l2_weight"] = {"interval_[1,2]": ap_ratio(1, 2),
                               "interval_[0.001,1]": ap_ratio(0.001, 1.0),
                               "interval_[1,100]": ap_ratio(1, 100)}

with open(f"{ART}/br_h3_results.json", "w") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({k: v for k, v in res.items() if not k.startswith("c")}, indent=1))
print("NESTED_SPIKE:", json.dumps(res["c_nested_spike"], indent=1))
