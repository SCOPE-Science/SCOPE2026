"""Fallback Attempt 3: Russo-formula reduction of I(f128)>=8 to a slope requirement.

For FK q=2, increasing f, random-cluster Russo (Grimmett):
  F'(p) = sum_e Cov_p(f, w_e) / (p(1-p)),  F(p) = phi_{p,q}(f).
Finite energy at q=2, p=p_c: P(e=1|rest) in {p, p/(p+q(1-p))} = {1-p..p}
numerically [0.414214, 0.585786]; h=phi(1-phi) in [p(1-p), 1/4].
Cov_e = E[g_e * h], g_e = pivotal indicator given rest.
Hence P(e pivotal) in [4, 1/(p(1-p))] * Cov_e, i.e. I in [4p(1-p),1]*F'(p_c).
Computes the exact required slope F'(p_c) >= 8 / (4 p (1-p)).
Then audits: no fused source gives an explicit F' floor (DM qualitative only).
Stdlib only.
"""
import math

p = math.sqrt(2) / (1 + math.sqrt(2))
q = 2.0
a = p / (p + q * (1 - p))
print(f"p_c = {p:.12f}, 1-p_c = {1 - p:.12f}, cond-low a = {a:.12f}")
assert abs(a - (1 - p)) < 1e-12, "q=2 symmetry a=1-p"
v = p * (1 - p)
print(f"p(1-p) = {v:.12f}")
lo, hi = v, 0.25
print(f"h in [{lo:.6f}, {hi:.6f}] -> P(piv)/Cov in [{1/hi:.6f}, {1/lo:.6f}]")
print(f"I(f) in [{4*v:.6f}, 1.0] * F'(p_c)")
req = 8 / (4 * v)
print(f"REQUIRED: F'(p_c) >= {req:.6f} for I>=8 via this route")
print("AUDIT: DM-2022 gives qualitative near-critical stability only (no F' floor);")
print("Gassmann-Manolescu asymptotic 2-arm only; Wu asymptotic exponents only;")
print("Chelkak-DC-Hongler existence-form RSW only. No citable explicit slope.")
print("CONCLUSION: Russo route needs a new quantitative sharp-threshold lemma")
print("at scale 128 (window width << 1/8 with tracked constants) - not closable")
print("from logged inputs; BLOCKED.")
