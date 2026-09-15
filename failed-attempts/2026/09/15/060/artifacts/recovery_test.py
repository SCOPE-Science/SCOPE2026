"""Bounded recovery test: Gibbs precision barrier at tacnode scale.

Question: can Gibbs-resampling concentration pin a Bernoulli path inside the
tacnode window to precision o(n^{1/3}), as the stated route
("Gibbs-resampling optimal concentration" feeding an RH comparison) requires?

Model: one path resampled as a Bernoulli(p=1/2) 0/1 bridge over the tangential
window L = A n^{2/3}; transverse (gap) scale is n^{1/3}. Conditional on the
endpoint, S_k | S_L=m ~ Hypergeometric(L, m, k); exact variance is known.
We compare bridge std (rescaled by n^{1/3}) to an O(1) rescaled gap, and compute
the limiting non-vanishing conditioning effect (midpoint Gaussian tail +
Brownian-bridge sup tail + Monte Carlo).
"""
import json
import math
import numpy as np

rng = np.random.default_rng(20260915)

A = 1.0
ns = [10**3, 10**6, 10**9, 10**12]
rows = []
for n in ns:
    L = int(round(A * n ** (2.0 / 3.0)))
    L = max(L, 8)
    if L % 2 == 1:
        L += 1
    m = L // 2
    k = L // 2
    # Exact hypergeometric variance of S_k | S_L = m
    p = m / L
    var_exact = k * p * (1 - p) * (L - k) / (L - 1)
    std_exact = math.sqrt(var_exact)
    transverse = n ** (1.0 / 3.0)
    ratio = std_exact / transverse  # -> sqrt(A)/4
    rows.append({"n": n, "L": L, "std_bridge": std_exact,
                 "transverse_scale": transverse, "ratio": ratio})

# Limiting ratio
limit_ratio = math.sqrt(A) / 4.0

# Midpoint conditioning effect: rescaled midpoint ~ N(0, limit_ratio^2);
# gap half-width g/2 with g = 1 (rescaled units) -> P(outside) = 2(1-Phi(2g... ))
def Phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

g = 1.0
z = (g / 2.0) / limit_ratio
p_mid = 2.0 * (1.0 - Phi(z))

# Sup tail for standard Brownian bridge: P(sup|B|>u) ~ 2*exp(-2u^2)-...;
# leading term 2 exp(-2 u^2); here u = (g/2)/limit_ratio in the same normalization
# where midpoint var of standard BB is 1/4 (std 1/2): rescale u by (1/2)/limit_ratio.
u = (g / 2.0) / limit_ratio * 1.0  # both midpoint stds accounted consistently below
# Correct mapping: our rescaled bridge midpoint std = limit_ratio; standard BB
# midpoint std = 1/2. u_std = (g/2) / (2*limit_ratio).
u_std = (g / 2.0) / (2.0 * limit_ratio)
p_sup_leading = 2.0 * math.exp(-2.0 * u_std ** 2)

# Monte Carlo: hypergeometric midpoint draws, fraction outside gap half-width
mc = []
for n in [10**6, 10**9]:
    L = int(round(A * n ** (2.0 / 3.0)))
    if L % 2 == 1:
        L += 1
    m = L // 2
    k = L // 2
    draws = rng.hypergeometric(ngood=m, nbad=L - m, nsample=k, size=200000)
    center = k * m / L
    half_gap = 0.5 * (n ** (1.0 / 3.0))
    frac_out = float(np.mean(np.abs(draws - center) > half_gap))
    mc.append({"n": n, "L": L, "mc_frac_outside_gap": frac_out,
               "gaussian_prediction": p_mid})

out = {
    "model": "Bernoulli(1/2) bridge over tangential window L=A n^{2/3}, A=1; transverse unit n^{1/3}",
    "exact_variance_formula": "Var(S_{L/2}|S_L=L/2) = (L/2)(1/4)(L/2)/(L-1) -> L/16",
    "per_n": rows,
    "limiting_rescaled_std": limit_ratio,
    "gap_test": {
        "rescaled_gap": g,
        "midpoint_outside_prob_limit": p_mid,
        "brownian_bridge_sup_tail_leading": p_sup_leading,
        "monte_carlo": mc,
    },
    "conclusion": ("Bridge std is (sqrt(A)/4 + o(1)) n^{1/3}: the SAME order as the "
                   "tacnode gap O(n^{1/3}). Rescaled boundary error is O(1), not o(1); "
                   "conditioning on the gap is a non-vanishing (positive-probability) "
                   "conditioning, so Gibbs tightness-scale concentration cannot deliver "
                   "the o(n^{1/3}) boundary matching that tacnode-kernel stability needs."),
}
with open("output/artifacts/recovery_results.json", "w") as f:
    json.dump(out, f, indent=2)
print(json.dumps(out, indent=2))
