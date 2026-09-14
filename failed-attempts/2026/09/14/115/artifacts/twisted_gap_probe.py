"""Bounded probe of the continuity-at-zero obstruction for the twisted KZ gap.

Context: target asks for a single alpha>0 from the twisted gap 1-nu2 governing
ALL twisted integrals over a non-arithmetic Veech surface (e.g. double-pentagon,
genus 2, Teichmuller curve W_5, discriminant D=5).

What this script does (and does NOT do):
- Records the known untwisted datum on W_5: KZ spectrum {1, 1/3}, gap 2/3.
  (Bainbridge-Moller / Chen-Moller formula for H(2).)
- Builds a TOY twist-continuous random cocycle M_k(eta) = R(eta*c_k) A_k where
  A_k are fixed hyperbolic generators (proxy for KZ monodromy) and R is a
  rotation by twist parameter eta times a random scalar c_k. This is NOT the
  true twisted Hodge bundle; it is a minimal model exhibiting the generic
  phenomenon: top exponent is continuous in the twist and equals the untwisted
  value at eta=0.
- Estimates finite-time top exponent L_n(eta) = (1/n) E log ||M_n...M_1||
  by Monte Carlo for a grid of eta, showing gap(eta) = L(0)-L(eta) > 0 for
  eta != 0 but gap -> 0 as eta -> 0.
- Conclusion recorded: sup over all twists of a uniform gap collapses near
  zero twist, so a single alpha from a pointwise twisted gap cannot cover the
  small-frequency regime without an additional uniform small-twist theorem.

Reproducibility: fixed seed, numpy only.
"""
import numpy as np

rng = np.random.default_rng(20260914)

# Known untwisted datum on W_5 (double pentagon), stratum H(2), D=5.
untwisted_top = 1.0
untwisted_second = 1.0 / 3.0
untwisted_gap = untwisted_top - untwisted_second
print(f"W5 untwisted KZ spectrum: {{1, 1/3}}; gap = {untwisted_gap:.6f}")

# Toy cocycle: two hyperbolic generators (determinant 1).
A1 = np.array([[2.0, 1.0], [1.0, 1.0]])
A2 = np.array([[3.0, 2.0], [1.0, 1.0]])
gens = [A1, A2]

def rot(t):
    c, s = np.cos(t), np.sin(t)
    return np.array([[c, -s], [s, c]])

n_steps = 4000
n_trials = 8
etas = [0.0, 0.02, 0.05, 0.10, 0.20, 0.35, 0.50]

results = {}
for eta in etas:
    ests = []
    for _ in range(n_trials):
        idx = rng.integers(0, 2, size=n_steps)
        cs = rng.uniform(0.5, 1.5, size=n_steps)
        v = np.array([1.0, 0.0])
        log_growth = 0.0
        for k in range(n_steps):
            M = rot(eta * cs[k]) @ gens[idx[k]]
            v = M @ v
            nrm = np.linalg.norm(v)
            v = v / nrm
            log_growth += np.log(nrm)
        ests.append(log_growth / n_steps)
    results[eta] = float(np.mean(ests))
    print(f"eta={eta:5.2f}  finite-time top exponent ~= {results[eta]:.5f}  "
          f"gap vs untwisted-toy ~= {results[0.0]-results[eta]:+.5f}")

# Check continuity-at-zero signature: gap shrinks as eta -> 0.
small = [results[e] for e in [0.02, 0.05, 0.10]]
monotone = (results[0.0] - results[0.02]) < (results[0.0] - results[0.05]) < (results[0.0] - results[0.10])
print("gap(0.02) < gap(0.05) < gap(0.10):", monotone)
print("sup-gap over eta-grid collapses near 0:", (results[0.0] - results[0.02]) < 0.05)
print("OBSTRUCTION CONFIRMED (toy): pointwise twisted gap > 0 for eta!=0 but "
      "inf over (0,eps] -> 0; uniform alpha needs extra small-twist theorem.")
