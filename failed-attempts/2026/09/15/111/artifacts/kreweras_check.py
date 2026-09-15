"""Reproducible check for lane-20343 target.

Verifies the discrete Kreweras-walk covariance structure that underlies the
mating-of-trees identification:
  steps a=(1,0), b=(0,1), c=(-1,-1) each w.p. 1/3 (Bernardi-Holden-Sun encoding).
Claims checked:
  1. mean zero, one-step covariance [[2/3,1/3],[1/3,2/3]], correlation +1/2.
  2. Donsker scaling: Z^n_t = sqrt(3/(2n)) Z_{floor(nt)} has Cov ~ t*[[1,1/2],[1/2,1]].
  3. Empirical correlation of the two coordinates ~ +1/2 = -cos(4*pi/6),
     the gamma=sqrt(8/3) mating-of-trees value.
Uses only numpy (no scipy). Deterministic seed.
"""
import json
import numpy as np

rng = np.random.default_rng(20343)

STEPS = np.array([[1.0, 0.0], [0.0, 1.0], [-1.0, -1.0]])
P = np.array([1 / 3, 1 / 3, 1 / 3])

THEORY_COV_1 = np.array([[2 / 3, 1 / 3], [1 / 3, 2 / 3]])
C_SCALE = np.sqrt(3.0 / 2.0)  # per-unit-time normalization factor family


def sample_walks(n_steps, n_walks):
    idx = rng.choice(3, size=(n_walks, n_steps), p=P)
    return STEPS[idx].cumsum(axis=1)  # (n_walks, n_steps, 2)


# ---- 1. one-step covariance ----
N1, M1 = 1, 400000
W1 = sample_walks(N1, M1)[:, 0, :]
mean1 = W1.mean(axis=0)
cov1 = np.cov(W1, rowvar=False, bias=False)
corr1 = cov1[0, 1] / np.sqrt(cov1[0, 0] * cov1[1, 1])

# ---- 2. Donsker-scale covariance at macroscopic times ----
N2, M2 = 2000, 60000
W2 = sample_walks(N2, M2)
results_t = {}
for t in (0.25, 0.5, 1.0):
    k = int(N2 * t)  # number of steps
    c = np.sqrt(3.0 / (2.0 * N2))
    Zn = c * W2[:, k - 1, :]
    cov = np.cov(Zn, rowvar=False, bias=False)
    t_eff = k / N2
    target = t_eff * np.array([[1.0, 0.5], [0.5, 1.0]])
    results_t[str(t)] = {
        "k": k,
        "emp_cov": cov.tolist(),
        "target_cov": target.tolist(),
        "max_abs_err": float(np.abs(cov - target).max()),
        "emp_corr": float(cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])),
    }

# ---- 3. endpoint correlation over full walks ----
end = W2[:, -1, :]
emp_corr_end = float(np.corrcoef(end[:, 0], end[:, 1])[0, 1])

out = {
    "one_step": {
        "emp_mean": mean1.tolist(),
        "emp_cov": cov1.tolist(),
        "theory_cov": THEORY_COV_1.tolist(),
        "max_abs_cov_err": float(np.abs(cov1 - THEORY_COV_1).max()),
        "emp_corr": float(corr1),
        "theory_corr": 0.5,
    },
    "donsker_times": results_t,
    "endpoint_corr_full_walk": emp_corr_end,
    "mating_of_trees_prediction": {
        "gamma": "(8/3)^0.5",
        "corr_formula": "-cos(pi*gamma^2/4) = -cos(2pi/3) = +1/2",
        "value": 0.5,
    },
    "n_steps_scaling": N2,
    "n_walks": M2,
    "seed": 20343,
}

with open("output/artifacts/kreweras_check_results.json", "w") as f:
    json.dump(out, f, indent=2)

print(json.dumps(out, indent=2))

# Pass/fail gates (generous Monte Carlo tolerances)
assert abs(corr1 - 0.5) < 0.02, corr1
assert np.abs(cov1 - THEORY_COV_1).max() < 0.02
for t, r in results_t.items():
    assert r["max_abs_err"] < 0.08, (t, r)
    assert abs(r["emp_corr"] - 0.5) < 0.05, (t, r)
assert abs(emp_corr_end - 0.5) < 0.05
print("ALL CHECKS PASSED")
