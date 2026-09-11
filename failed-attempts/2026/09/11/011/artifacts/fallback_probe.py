"""Bounded fallback-feasibility probe for lane-692 (logged 30-min gate evidence).

Fallback claim: for G_q=LPS X^{5,q} (6-reg, m=3n edges), rho=1/2 independent
variable-retention, P[width(residual Tseitin) >= n/40] >= 1-exp(-n/100).

Attempt F1: per-set Chernoff + union bound over medium sets.
Attempt F2: Karger near-mincut counting (does it rescue the union bound?).
Attempt F3: matrix-Bernstein spectral preservation (does random subgraph keep gap?).
All bounds use explicit conservative constants (sqrt5_hi, ln2_hi as in check_constants.py).
"""
import math

sqrt5_hi = 2.23606797749979
assert sqrt5_hi**2 > 5
h_lo = 3 - sqrt5_hi          # edge-expansion/vertex lower bound, |delta(S)|>=h|S|, |S|<=n/2
print(f"h_lo={h_lo:.6f}")

# ---- F1: one medium set S, |S|=n/3 ----
# k=|delta(S)|>=h*n/3; X=retained boundary ~ Bin(k,1/2); need X>=n/40.
s_frac = 1/3
k_per_n = h_lo * s_frac       # >=0.25464... per n
mu = k_per_n / 2              # E[X]/n
t = 1/40                      # threshold/n
delta = 1 - t/mu
chernoff_per_n = mu*delta**2/2   # P(X<t*n) <= exp(-chernoff_per_n * n)
# union bound over C(n,n/3): entropy H(1/3) nats
H = -s_frac*math.log(s_frac)-(1-s_frac)*math.log(1-s_frac)
print(f"F1: k/n>={k_per_n:.5f} mu={mu:.5f} delta={delta:.4f}")
print(f"    per-set tail exponent={chernoff_per_n:.5f}/n; set-count entropy={H:.5f}/n")
print(f"    union-bound margin={chernoff_per_n-H:.5f} -> {'CLOSES' if chernoff_per_n>H else 'FAILS by factor %.1f'%(H/chernoff_per_n)}")
print(f"    (single-set tail exp(-{chernoff_per_n:.4f}n) vs required exp(-0.01n): single set OK, union over family FAILS)")

# ---- F2: Karger — #cuts of size <= alpha*c is <= n^{2alpha}; mincut c>=6 ----
# Our threshold needs cuts up to K~0.25n controlled; alpha=K/6 ~ 0.04n -> n^{2alpha} astronomically useless.
c = 6
K_per_n = k_per_n  # representative cut size per n
alpha_per_n = K_per_n*1000/6  # per 1000 vertices, symbolic
print(f"F2: Karger alpha for medium cuts ~ {K_per_n:.4f}n/{c} = {K_per_n/c*1000:.1f} per 1000 verts -> bound n^(2alpha) vacuous; only near-mincut (alpha=O(1)) cuts are few, but threshold n/40 lives far above mincut. Karger DOES NOT rescue.")

# ---- F3: matrix Bernstein for spectral gap preservation ----
# A' = retained-edge adjacency, E[A']=A/2; summands X_e (per edge, var<=1/4, R<=1).
# sigma^2 <= max-degree*1/4 = 1.5; need deviation t < gap/2 ~ (6-2*sqrt5)/2 ~ 0.76.
sig2 = 1.5; R = 1.0; tgap = (6-2*2.23606797749979)/2
exp_arg = tgap**2/(2*sig2+2*R*tgap/3)
print(f"F3: need t<{tgap:.4f}; Bernstein exponent={exp_arg:.4f} -> bound 2n*exp(-{exp_arg:.4f}) > 1 for all n: VACUOUS.")
print("F3b: true percolated-expander theorems (giant component is expander) exist asymptotically but with")
print("     unspecified constants and multi-page proofs; exact (n/40, exp(-n/100)) not derivable in-session.")

print("CONCLUSION: fallback blocked after 3 bounded analytic attempts (F1 quantified 15x shortfall; F2/F3 structurally vacuous).")
