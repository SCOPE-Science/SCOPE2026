"""Deterministic constant verification + Monte-Carlo illustration (non-rigorous) for lane-377."""
import json
import numpy as np
out = {}
# A1: sqrt(3) enclosure by squaring
assert 1.732**2 < 3.0 < 1.733**2
s3_hi = 1.733
c_lo = 1.0/s3_hi
out["one_over_sqrt3_lower"] = c_lo
assert c_lo > 0.5770
# A2: product-cost cap I1 <= 2*pi*a^2+1/a at a=1/2, pi in [3.140,3.142]
pi_lo, pi_hi = 3.140, 3.142
prod_cap = 2*pi_hi*0.25 + 2.0
out["product_cost_cap_per_pair_L1"] = prod_cap
assert prod_cap < 3.572
# A3: gap
gap = prod_cap - c_lo
out["gap_per_pair_G1"] = gap
assert gap < 3.0
# A4: diffuse threshold eps*L > G/(2 tau^2), tau=0.1
tau = 0.1
thr = gap/(2*tau*tau)
out["tau"] = tau
out["threshold_eps_times_L_N2"] = thr
assert thr < 150.0
eta = 150.0
S_bound = gap/eta
TV = (S_bound/2.0)**0.5
out["eta_star_L1"] = eta
out["entropy_bound_N2"] = S_bound
out["TV_bound_N2"] = TV
assert TV < 0.1
# A5: Monge-tube product mass <= (4/3)pi (d/L)^3 at d/L=0.1
tube = (4.0/3.0)*pi_hi*0.1**3
out["tube_ratio"] = 0.1
out["tube_product_mass_bound"] = tube
assert tube < 0.0042
out["tube_plus_TV"] = tube + TV
assert tube + TV < 0.11
# A6: rs factor for N=2: f=(8pi/3)^{1/3} in [2.03,2.033]
assert 2.03**3 < 8*pi_lo/3 and 8*pi_hi/3 < 2.033**3
out["rs_factor_N2_interval"] = [2.03, 2.033]
out["threshold_eps_times_rs_N2"] = thr/2.03
assert out["threshold_eps_times_rs_N2"] < 74.0
# B: Monte-Carlo illustration only (seeded)
rng = np.random.default_rng(377)
M = 400000
U = rng.random((M,3)); V = rng.random((M,3))
rr = np.linalg.norm(U-V,axis=1)
mc_mean = float((1.0/rr).mean()); mc_se = float((1.0/rr).std(ddof=1)/np.sqrt(M))
out["MC_product_cost_mean"] = mc_mean
out["MC_product_cost_se"] = mc_se
out["MC_product_cost_3sigma_interval"] = [mc_mean-3*mc_se, mc_mean+3*mc_se]
out["MC_short_range_alpha0.2"] = float(np.mean(rr < 0.2))
out["short_range_cap_alpha0.2"] = (4.0/3.0)*pi_hi*0.2**3
out["note_MC"] = "Monte-Carlo values are illustration only, not used in any proof."
with open("output/artifacts/results.json","w") as f:
    json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
print("ALL RIGOROUS ASSERTIONS PASSED")
