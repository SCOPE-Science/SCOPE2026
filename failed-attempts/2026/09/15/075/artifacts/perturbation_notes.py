"""Branch-perturbation bookkeeping + transplant error model for Bolza lambda1 local-max reduction.
Toy model only: verifies logic that sum-zero first order forces min-branch decrease
unless fully first-order degenerate; and quantifies why transplant bound is insufficient.
"""
import numpy as np

rng = np.random.default_rng(0)

def min_branch(d, e, t):
    # 3 branches: mu_i = lam0 + t*d_i + t^2*e_i
    lam0 = 3.838887258
    mus = lam0 + np.outer(t, d) + np.outer(t**2, e)
    return mus.min(axis=1)

# Case A: non-degenerate first order, sum zero, e.g. d=(a,b,-a-b)
d = np.array([0.5, -0.2, -0.3])
e = np.array([-1.0, -0.5, 0.3])
ts = np.array([1e-3, -1e-3, 1e-2, -1e-2])
lam0 = 3.838887258
vals = min_branch(d, e, ts)
print("Case A (sum d = 0, not all zero):")
for t, v in zip(ts, vals):
    print(f"  t={t:+.4f} min_branch-lam0 = {v-lam0:+.3e}  (first-order predicts {t*min(d) if t>0 else t*max(d):+.3e})")

# Case B: fully degenerate first order d=0; outcome decided by min e
d0 = np.zeros(3)
e2 = np.array([-0.7, 0.2, 0.4])
vals2 = min_branch(d0, e2, ts)
print("Case B (d=0):")
for t, v in zip(ts, vals2):
    print(f"  t={t:+.4f} min_branch-lam0 = {v-lam0:+.3e}  (second-order predicts {t**2*min(e2):+.3e})")

# Transplant error model: Rayleigh quotient of transplanted trial function
# R = lam0*(1 + C1*k + C2*k^2) + mean-correction; k = quasiconformal dilatation ~ d_Teich
# C1 averages to 0 over Aut(B) orbit (first-order sum-zero analogue); sign of sharp
# quadratic term depends on unknown eigenfunction gradient L^4 norms + resolvent norm.
print("\nTransplant model: R-lam0 for k=1e-3, C1=0 (symmetrized), C2 unknown in [-50,50]:")
for C2 in [-50.0, -5.0, 5.0, 50.0]:
    print(f"  C2={C2:+.1f} -> R-lam0 = {lam0*C2*1e-6:+.3e}  (sign = sign of C2, uncertified)")

print("\nConclusion: first-order symmetry decides all non-degenerate directions;")
print("degenerate cone needs certified E1 integrals (not available analytically).")
